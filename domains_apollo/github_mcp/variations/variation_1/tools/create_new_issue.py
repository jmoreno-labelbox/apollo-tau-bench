from tau_bench.envs.tool import Tool
import json
from typing import Any

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
    def invoke(
        data: dict[str, Any],
        owner: str = "",
        repo_name: str = "",
        title: str = "",
        issue_title: str = "",
        body: str = "",
        issue_body: str = "",
        labels: Any = None,
        label: Any = None,
        lable: Any = None,
        assignees: Any = None,
        assignee: Any = None,
    ) -> str:
        owner = owner.strip()
        repo_name = (repo_name or repo_name or "").strip()

        # Optional fields
        title = (title or issue_title or "").strip()
        body = (body or issue_body or "").strip()

        # Accept label(s) via 'label', 'lable' (typo), or 'labels'
        labels_input = labels or label or lable
        if isinstance(labels_input, str):
            labels_list: list[str] = (
                [labels_input.strip()] if labels_input.strip() else []
            )
        elif isinstance(labels_input, list):
            labels_list = [
                str(x).strip()
                for x in labels_input
                if isinstance(x, (str, int, float)) and str(x).strip()
            ]
        else:
            labels_list = []

        # Accept assignee(s) via 'assignees' or 'assignee'
        assignees_input = assignees or assignee
        if isinstance(assignees_input, str):
            assignees_list: list[str] = (
                [assignees_input.strip()] if assignees_input.strip() else []
            )
        elif isinstance(assignees_input, list):
            assignees_list = [
                str(x).strip()
                for x in assignees_input
                if isinstance(x, (str, int, float)) and str(x).strip()
            ]
        else:
            assignees_list = []

        if not owner or not repo_name:
            payload = {
                "error": "Parameters 'owner' and 'repo_name' (or 'repo_name') are required."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Load issues DB
        issues_db = data.get("issues", [])
        if not isinstance(issues_db, list):
            payload = {"error": "Invalid issues DB: expected a list at data['issues']."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Find or create the repo bucket
        rec = next(
            (
                r
                for r in issues_db
                if r.get("owner") == owner and r.get("repo_name") == repo_name
            ),
            None,
        )
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
                "updated_ts": [],
            }
            issues_db.append(rec)
            created_bucket = True

        # Next issue number & timestamp (helpers provided by your env)
        next_issue_number = get_next_issue_number(data)
        new_ts = get_current_timestamp()

        # Ensure arrays exist
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

        # Append the new issue
        rec["issue_numbers"].append(next_issue_number)
        rec["issue_titles"].append(title)  # provided or ""
        rec["issue_bodies"].append(body)  # provided or ""
        rec["issue_states"].append("open")
        rec["labels"].append(labels_list)  # list[str]
        rec["assignees"].append(assignees_list)  # list[str]
        rec["issue_comments"].append([])  # none yet
        rec["issue_comment_users"].append([])  # none yet
        rec["created_ts"].append(new_ts)
        rec["updated_ts"].append(new_ts)

        add_terminal_message(
            data,
            (
                f"Created new issues bucket and issue #{next_issue_number}"
                if created_bucket
                else f"Added issue #{next_issue_number} to existing bucket"
            ),
            get_current_timestamp(),
        )
        payload = {
            "success": (
                f"Created new issues bucket and issue #{next_issue_number}"
                if created_bucket
                else f"Added issue #{next_issue_number} to existing bucket"
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
                "updated_ts": new_ts,
            },
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
                "name": "CreateNewIssue",
                "description": "Create a new issue for a repo in the issues DB (creates repo bucket if missing). Supports title, body, labels, assignees.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name (alias accepted as 'repo_name').",
                        },
                        "title": {"type": "string", "description": "Issue title."},
                        "body": {
                            "type": "string",
                            "description": "Issue body/description.",
                        },
                        "labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of labels to attach.",
                        },
                        "assignees": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of usernames to assign.",
                        },
                    },
                    "required": [
                        "owner",
                        "repo_name",
                        "title",
                        "body",
                        "labels",
                        "assignees",
                    ],
                },
            },
        }
