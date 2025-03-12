# Automated Email Responder with CrewAI, Langraph and Gmail API

Project Working : https://www.linkedin.com/feed/update/urn:li:activity:7304425730707251201/


This project uses CrewAI and the Gmail API to automatically respond to emails.  It checks for new messages every 2 seconds and uses AI agents to draft replies.

## Overview

1.  **Polling:** Checks for new emails in a Gmail account every 2 seconds.
2.  **Retrieval:**  Gets the subject and body of new emails.
3.  **Agent Crew:**  CrewAI agents:
    *   Understand the email.
    *   Draft a reply.
    *   (Optionally) Review/approve the draft.
4.  **Reply:** Creates a draft reply (or sends automatically, depending on configuration).

## Example

**Sent Email:**

`hi wasay how was your day`

**Drafted Reply:**

`hey abdul my day has been good ,thanks for asking! i hope your day is going well too what have you been up to?`

## Key Features

*   Automated email responses (with optional review).
*   Gmail API integration.
*   CrewAI agent collaboration.
*   2-second polling interval.
*   Draft reply creation.

## Installation and Usage
(Instructions for installation (`pip install crewai google-api-python-client...`) and running, *including detailed Gmail API credential setup*.)  **Gmail API requires OAuth 2.0 credentials.**

## Future Improvements

*   More specialized agent roles (spam filtering, categorization).
*   Personalized responses.
*   Improved error handling.
*   Configurable polling.
*   Attachment handling.
*   Security enhancements.
*   Optional user interface.
* Agent loop for self-evaluation
