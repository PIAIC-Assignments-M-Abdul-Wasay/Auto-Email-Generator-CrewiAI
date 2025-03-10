from crewai import Crew

from .agents import EmailFilterAgents
from .tasks import EmailFilterTasks

class EmailFilterCrew():
    def __init__(self):
        agents = EmailFilterAgents()
        self.filter_agent = agents.email_filter_agent()
        self.action_agent = agents.email_action_agent()
        self.writer_agent = agents.email_response_writer()

    def kickoff(self, state):
        print("### Filtering emails")
        tasks = EmailFilterTasks()

        # Ensure state has all required keys, even if empty
        default_state = {
            "emails": state.get("emails", []),
            "checked_emails_ids": state.get("checked_emails_ids", []),
            "action_required_emails": state.get("action_required_emails", [])
        }

        # Format emails if they exist, otherwise use an empty string
        formatted_emails = self._format_emails(default_state["emails"]) if default_state["emails"] else "No emails provided"

        crew = Crew(
            agents=[self.filter_agent, self.action_agent, self.writer_agent],
            tasks=[
                tasks.filter_emails_task(self.filter_agent, formatted_emails),
                tasks.action_required_emails_task(self.action_agent),
                tasks.draft_responses_task(self.writer_agent)
            ],
            verbose=True
        )
        result = crew.kickoff()

        # Ensure result is a list for action_required_emails
        action_emails = result if isinstance(result, list) else [result] if result else []

        # Return updated state with all required keys
        return {
            "emails": default_state["emails"],  # Preserve original emails
            "checked_emails_ids": default_state["checked_emails_ids"],  # Update if task provides this
            "action_required_emails": action_emails  # Update with crew result
        }

    def _format_emails(self, emails):
        emails_string = []
        for email in emails:
            print(email)
            arr = [
                f"ID: {email['id']}",
                f"- Thread ID: {email['threadId']}",
                f"- Snippet: {email['snippet']}",
                f"- From: {email['sender']}",
                f"--------"
            ]
            emails_string.append("\n".join(arr))
        return "\n".join(emails_string)