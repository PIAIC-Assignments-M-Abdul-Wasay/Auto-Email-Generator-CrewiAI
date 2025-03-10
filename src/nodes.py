import os
import time
from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.search import GmailSearch

class Nodes:
    def __init__(self):
        self.gmail = GmailToolkit()

    def check_email(self, state):
        print("# Checking for new emails")
        search = GmailSearch(api_resource=self.gmail.api_resource)
        try:
            emails = search('newer_than:5m')
        except UnicodeDecodeError as e:
            print(f"Error decoding emails: {e}. Skipping problematic email.")
            emails = []  # Fallback to empty list if decoding fails entirely

        checked_emails = state.get('checked_emails_ids', [])
        thread = []
        new_emails = []

        for email in emails:
            # Ensure we are not processing already checked emails or threads
            if (
                email.get('id') not in checked_emails
                and email.get('threadId') not in thread
                and os.environ.get('MY_EMAIL') not in email.get('sender', '')
            ):
                thread.append(email['threadId'])
                new_email = {
                    "id": email.get('id', ''),
                    "threadId": email.get('threadId', ''),
                    "snippet": self.safe_decode(email.get('snippet', '')),
                    "sender": email.get('sender', '')
                }
                new_emails.append(new_email)

        checked_emails.extend([email.get('id', '') for email in emails])
        return {
            **state,
            "emails": new_emails,
            "checked_emails_ids": checked_emails
        }

    def safe_decode(self, text):
        if isinstance(text, bytes):
            try:
                return text.decode("utf-8")
            except UnicodeDecodeError:
                return text.decode("latin-1", errors="ignore")
        return text  # Return as-is if already a string

    def wait_next_run(self, state):
        print("## Waiting for 2 seconds")
        time.sleep(2)
        return state

    def new_emails(self, state):
        if len(state['emails']) == 0:
            print("## No new emails")
            return "end"
        else:
            print("## New emails")
            return "continue"