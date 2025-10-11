# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewIssue(Tool):
    """
    Create a new issue entry for a repo in the issues DB.
    - Inputs: owner, repo_name (alias: repo_name), plus optional: title, body, label(s), assignee(s)
    - Behavior:
        * If (owner, repo_name) bucket does NOT exist: create a brand-new record and add the first issue.
        * Else: append a new issue to the existing record with next issue_number from get_next_issue_number(data).
    - Timestamps: created_ts/updated_ts come from get_current_updated_timestamp().
    - Defaults: title/body "", state "open", labels/assignees/comments empty.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()

        # Fields that are not mandatory
        title = (kwargs.get("title") or kwargs.get("issue_title") or "").strip()
        body = (kwargs.get("body") or kwargs.get("issue_body") or "").strip()

        # Accept labels through 'label', 'lable' (misspelling), or 'labels'.
        labels_input = kwargs.get("labels", kwargs.get("label", kwargs.get("lable", None)))
        if isinstance(labels_input, str):
            labels_list: List[str] = [labels_input.strip()] if labels_input.strip() else []
        elif isinstance(labels_input, list):
            labels_list = [str(x).strip() for x in labels_input if isinstance(x, (str, int, float)) and str(x).strip()]
        else:
            labels_list = []

        # Receive assignee(s) through 'assignees' or 'assignee'.
        assignees_input = kwargs.get("assignees", kwargs.get("assignee", None))
        if isinstance(assignees_input, str):
            assignees_list: List[str] = [assignees_input.strip()] if assignees_input.strip() else []
        elif isinstance(assignees_input, list):
            assignees_list = [str(x).strip() for x in assignees_input if isinstance(x, (str, int, float)) and str(x).strip()]
        else:
            assignees_list = []

        if not owner or not repo_name:
            return json.dumps(
                {"error": "Parameters 'owner' and 'repo_name' (or 'repo_name') are required."},
                indent=2
            )

        # Load the issues database.
        issues_db = list(data.get("issues", {}).values())
        if not isinstance(issues_db, list):
            return json.dumps({"error": "Invalid issues DB: expected a list at data['issues']."}, indent=2)

        # Locate or establish the repository bucket.
        rec = next((r for r in issues_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        created_bucket = False
        if rec is None:
            rec = {
                "owner": owner,
                "repo_name": repo_name,
                "issue_numbers": [],
                "issue_titles": [],
                "issue_bodies": [],
                "issue_states": [],
                "labels": [],
                "assignees": [],
                "issue_comments": [],
                "issue_comment_users": [],
                "created_ts": [],
                "updated_ts": []
            }
            issues_db.append(rec)
            created_bucket = True

        # Upcoming issue identifier and timestamp (utilities available in your environment)
        next_issue_number = get_next_issue_number(data)
        new_ts = get_current_timestamp()

        # Verify the presence of arrays.
        for key, default in [
            ("issue_numbers", []),
            ("issue_titles", []),
            ("issue_bodies", []),
            ("issue_states", []),
            ("labels", []),
            ("assignees", []),
            ("issue_comments", []),
            ("issue_comment_users", []),
            ("created_ts", []),
            ("updated_ts", []),
        ]:
            rec.setdefault(key, default)

        # Add the new issue.
        rec["issue_numbers"].append(next_issue_number)
        rec["issue_titles"].append(title)            # offered or ""
        rec["issue_bodies"].append(body)             # supplied or ""
        rec["issue_states"].append("open")
        rec["labels"].append(labels_list)            # List of strings
        rec["assignees"].append(assignees_list)      # array of strings
        rec["issue_comments"].append([])             # not available at this time
        rec["issue_comment_users"].append([])        # not available at this time
        rec["created_ts"].append(new_ts)
        rec["updated_ts"].append(new_ts)

add_terminal_message(data, f"Created new issues bucket and issue #{next_issue_number}" if created_bucket else f"Added issue #{next_issue_number} to existing bucket", get_current_timestamp())

return json.dumps(
            {
                "success": (
f"Created new issues bucket and issue # {subsequent_issue_number}"
                    if created_bucket else
f"Added issue # {next_issue_number} to the current bucket."
                ),
                "repo": f"{owner}/{repo_name}",
                "issue": {
                    "number": next_issue_number,
                    "title": title,
                    "body": body,
                    "state": "open",
                    "labels": labels_list,
                    "assignees": assignees_list,
                    "created_ts": new_ts,
                    "updated_ts": new_ts
                }
            },
            indent=2
        )

@staticmethod
def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_issue",
                "description": "Create a new issue for a repo in the issues DB (creates repo bucket if missing). Supports title, body, labels, assignees.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias accepted as 'repo_name')."},
                        "title": {"type": "string", "description": "Issue title."},
                        "body": {"type": "string", "description": "Issue body/description."},
                        "labels": {"type": "array", "items": {"type": "string"}, "description": "List of labels to attach."},
                        "assignees": {"type": "array", "items": {"type": "string"}, "description": "List of usernames to assign."}
                    },
                    "required": ["owner", "repo_name","title","body","labels","assignees"]
                }
            }
        }