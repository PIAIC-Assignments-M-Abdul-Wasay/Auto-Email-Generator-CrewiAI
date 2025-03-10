from src.graph import WorkFlow

app = WorkFlow().app
initial_state = {
    "emails": [],  # Initial list of emails (empty for now)
    "checked_emails_ids": [],
    "action_required_emails": []
}
result = app.invoke(initial_state)
print(result)