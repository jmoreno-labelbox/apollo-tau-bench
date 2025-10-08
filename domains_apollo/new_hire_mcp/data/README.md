# New Hire Onboarding MCP - Simulated Data

This directory contains a set of JSON files that simulate the database and file system state for the New Hire Onboarding MCP (Mission Critical Process). These files are designed to be used by an agent to simulate the execution of the tasks outlined in the `proposal.md` file.

## Task-to-File Manipulation Mapping

Below is a breakdown of which files are manipulated during each onboarding task.

### Task 1: New Hire Onboarding Packet

This task focuses on creating and sending the initial welcome packet to a new hire.

-   **`candidates.json`**: A new candidate record is created. Later, it's updated with the `welcome_email_message_id`.
-   **`onboarding_files.json`**: The personalized `welcome_<candidate_name>.md` is written here.
-   **`emails.json`**: A welcome email is drafted and then marked as sent.
-   **`attachments.json`**: Records are created to link the "Company-Policies.pdf", "Benefits-Guide.pdf", and the personalized welcome markdown to the welcome email.

### Task 2: Equipment Provisioning Request

This task handles the request for new hardware for the new hire.

-   **`asset_requests.json`**: A new record for the asset request is created and then updated once the notification is sent.
-   **`onboarding_files.json`**: The `asset_request.json` file is created.
-   **`emails.json`**: An email to the IT assets team is drafted and sent.
-   **`attachments.json`**: A record is created to link the `asset_request.json` to the IT email.
-   **`email_labels.json`**: The "Asset-Request" label is retrieved and applied to the sent email.
-   **`inventory_assets.json`**: This file is queried to check for the availability of the requested asset.
-   **`candidates.json`**: The candidate's record is updated with the asset tag once it's allocated.

### Task 3: Day-1 Access Verification & Orientation Scheduling

This task ensures the new hire has the necessary system access and receives orientation invites.

-   **`access_checks.json`**: Records are created to store the pass/fail status for each system access check.
-   **`emails.json`**: Two emails are drafted and sent: one for the orientation and another for the manager intro. A third email is sent to IT if any access checks fail.
-   **`candidates.json`**: The candidate's record is updated with timestamps for the sent invitations and a summary of the access checks.

### Task 4: Onboarding Checklist Follow-Up

This task involves checking for incomplete onboarding items after the first week and sending reminders.

-   **`checklist_items.json`**: This file is queried to find pending tasks. The status of these tasks is then updated to "Reminder Sent".
-   **`onboarding_files.json`**: A `pending_tasks.md` file is written with a summary of outstanding items.
-   **`emails.json`**: A reminder email is drafted and sent to the candidate.
-   **`attachments.json`**: A record is created to attach `pending_tasks.md` to the reminder email.
-   **`email_labels.json`**: The "Onboarding-Reminder" label is retrieved and applied to the reminder email.
-   **`candidates.json`**: The candidate record is updated with a timestamp for the checklist follow-up.
