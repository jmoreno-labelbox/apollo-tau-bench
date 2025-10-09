from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateIssue(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str,
        repo: str,
        issue_number: int,
        labels: list[str] = None,
        assignees: list[str] = None,
        title: str = None,
        body: str = None,
        state: str = None,
        milestone: str = None,
    ) -> str:
        """Update issue with comprehensive tracking of changes, activity, and automated workflow triggers."""
        pass
        issues_data = data.get("issues", [])
        auth_users = data.get("authentication", [])

        #Retrieve the current user for tracking purposes
        current_user = auth_users[0]["username"] if auth_users else "system"
        update_timestamp = "2023-12-05T12:00:00Z"

        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                try:
                    issue_idx = issue_entry["issue_numbers"].index(issue_number)

                    #Save previous values for tracking changes
                    previous_values = {
                        "title": issue_entry["issue_titles"][issue_idx],
                        "body": (
                            issue_entry.get("issue_bodies", [""])[issue_idx]
                            if issue_idx < len(issue_entry.get("issue_bodies", []))
                            else ""
                        ),
                        "state": issue_entry["issue_states"][issue_idx],
                        "labels": issue_entry["labels"][issue_idx].copy(),
                        "assignees": issue_entry["assignees"][issue_idx].copy(),
                        "updated_at": (
                            issue_entry.get("updated_ts", [""])[issue_idx]
                            if issue_idx < len(issue_entry.get("updated_ts", []))
                            else ""
                        ),
                    }

                    #Monitor which fields are being modified
                    updated_fields = []

                    #Modify fields if they are supplied
                    if title is not None and title != previous_values["title"]:
                        issue_entry["issue_titles"][issue_idx] = title
                        updated_fields.append("title")

                    if body is not None and body != previous_values["body"]:
                        if "issue_bodies" not in issue_entry:
                            issue_entry["issue_bodies"] = [""] * len(
                                issue_entry["issue_numbers"]
                            )
                        if issue_idx < len(issue_entry["issue_bodies"]):
                            issue_entry["issue_bodies"][issue_idx] = body
                        else:
                            issue_entry["issue_bodies"].append(body)
                        updated_fields.append("body")

                    if state is not None and state != previous_values["state"]:
                        issue_entry["issue_states"][issue_idx] = state
                        updated_fields.append("state")

                    if labels is not None and labels != previous_values["labels"]:
                        issue_entry["labels"][issue_idx] = labels
                        updated_fields.append("labels")

                    if (
                        assignees is not None
                        and assignees != previous_values["assignees"]
                    ):
                        #Confirm the assignees parameter is valid
                        if assignees is None:
                            assignees = []
                        elif not isinstance(assignees, list):
                            assignees = [assignees] if assignees else []

                        issue_entry["assignees"][issue_idx] = assignees
                        updated_fields.append("assignees")

                    #Refresh the timestamp
                    if "updated_ts" not in issue_entry:
                        issue_entry["updated_ts"] = ["2023-12-05T12:00:00Z"] * len(
                            issue_entry["issue_numbers"]
                        )
                    issue_entry["updated_ts"][issue_idx] = update_timestamp

                    #Compute activity metrics (simulated based on changes)
                    comments_added_today = (
                        1
                        if any(
                            field in ["body", "assignees"] for field in updated_fields
                        )
                        else 0
                    )
                    label_changes_this_week = 1 if "labels" in updated_fields else 0
                    assignee_changes = 1 if "assignees" in updated_fields else 0
                    state_changes = 1 if "state" in updated_fields else 0

                    #Create events for the timeline
                    timeline_events = []
                    for field in updated_fields:
                        if field == "labels":
                            timeline_events.append(
                                f"Labels changed from {previous_values['labels']} to {labels}"
                            )
                        elif field == "assignees":
                            timeline_events.append(
                                f"Assignees changed from {previous_values['assignees']} to {assignees}"
                            )
                        elif field == "state":
                            timeline_events.append(
                                f"State changed from {previous_values['state']} to {state}"
                            )
                        elif field == "title":
                            timeline_events.append("Title updated")
                        elif field == "body":
                            timeline_events.append("Description updated")

                    #Simulate notifications sent (based on changes in assignees)
                    notifications_sent = []
                    if "assignees" in updated_fields:
                        notifications_sent = (
                            assignees[:3] if assignees else []
                        )  #Restrict to 3

                    #Simulate automation triggered (based on changes in labels/states)
                    automation_triggered = []
                    if "labels" in updated_fields:
                        if "bug" in (labels or []):
                            automation_triggered.append("bug-triage-workflow")
                        if "high-priority" in (labels or []):
                            automation_triggered.append("priority-escalation")
                    if "state" in updated_fields:
                        if state == "closed":
                            automation_triggered.append("closure-notification")
                        elif state == "open":
                            automation_triggered.append("reopened-alert")

                    #Retrieve current issue data for the response
                    current_data = {
                        "number": issue_number,
                        "title": issue_entry["issue_titles"][issue_idx],
                        "state": issue_entry["issue_states"][issue_idx],
                        "labels": issue_entry["labels"][issue_idx],
                        "assignees": issue_entry["assignees"][issue_idx],
                        "milestone": milestone,  #Utilize the given milestone or None
                        "updated_fields": updated_fields,
                    }

                    #Create a version number (simulated incremental version)
                    version = len(updated_fields) + 1

                    result = {
                        "success": True,
                        "data": current_data,
                        "metadata": {
                            "updated_at": update_timestamp,
                            "updated_by": current_user,
                            "previous_values": previous_values,
                            "version": version,
                        },
                        "relationships": {
                            "repository": f"{owner}/{repo}",
                            "timeline_events": timeline_events,
                            "notifications_sent": notifications_sent,
                            "automation_triggered": automation_triggered,
                        },
                        "activity": {
                            "comments_added_today": comments_added_today,
                            "label_changes_this_week": label_changes_this_week,
                            "assignee_changes": assignee_changes,
                            "state_changes": state_changes,
                        },
                    }
                    payload = result
                    out = json.dumps(payload, indent=2)
                    return out
                except ValueError:
                    pass
        payload = {
                "success": False,
                "error": f"Issue #{issue_number} not found in repository {owner}/{repo}",
                "error_code": "ISSUE_NOT_FOUND",
                "metadata": {
                    "repository": f"{owner}/{repo}",
                    "requested_issue": issue_number,
                    "search_timestamp": update_timestamp,
                },
                "suggestions": [
                    f"Check if issue #{issue_number} exists in repository {owner}/{repo}",
                    "Verify repository name and owner are correct",
                    "Use search_issues tool to find available issues",
                ],
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateIssue",
                "description": "Update issue with comprehensive change tracking, activity monitoring, automation triggers, and detailed audit trail of all modifications.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "issue_number": {
                            "type": "integer",
                            "description": "Issue number",
                        },
                        "labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "New labels (optional)",
                        },
                        "assignees": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "New assignees (optional)",
                        },
                        "title": {
                            "type": "string",
                            "description": "New title (optional)",
                        },
                        "body": {
                            "type": "string",
                            "description": "New body/description (optional)",
                        },
                        "state": {
                            "type": "string",
                            "description": "New state: 'open' or 'closed' (optional)",
                        },
                        "milestone": {
                            "type": "string",
                            "description": "Milestone name (optional)",
                        },
                    },
                    "required": ["owner", "repo", "issue_number"],
                },
            },
        }
