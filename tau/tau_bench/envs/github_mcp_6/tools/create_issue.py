from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateIssue(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str,
        repo: str,
        title: str,
        body: str,
        assignees: list[str],
        labels: list[str] = None,
    ) -> str:
        """Create an issue with labels/assignees."""
        pass
        issues_data = data.get("issues", [])

        #Confirm the validity of the assignees parameter
        if assignees is None:
            assignees = []
        elif not isinstance(assignees, list):
            assignees = [assignees] if assignees else []

        #Ensure the labels parameter is valid
        if labels is None:
            labels = []
        elif not isinstance(labels, list):
            labels = [labels] if labels else []

        #Locate the existing issue entry for this repository
        repo_issues = None
        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                repo_issues = issue_entry
                break

        if not repo_issues:
            #Establish a new issue entry
            issue_number = 1
            repo_issues = {
                "owner": owner,
                "repo_name": repo,
                "issue_numbers": [issue_number],
                "issue_titles": [title],
                "issue_bodies": [body],
                "issue_states": ["open"],
                "labels": [labels],
                "assignees": [assignees],
                "issue_comments": [[]],
                "issue_comment_users": [[]],
                "created_ts": ["2023-12-05T12:00:00Z"],
                "updated_ts": ["2023-12-05T12:00:00Z"],
            }
            issues_data.append(repo_issues)
        else:
            #Append to the current issue entry - retrieve the highest existing issue number and increment by 1
            issue_number = max(repo_issues["issue_numbers"]) + 1
            repo_issues["issue_numbers"].append(issue_number)
            repo_issues["issue_titles"].append(title)
            repo_issues["issue_bodies"].append(body)
            repo_issues["issue_states"].append("open")
            repo_issues["labels"].append(labels)
            repo_issues["assignees"].append(assignees)
            repo_issues["issue_comments"].append([])
            repo_issues["issue_comment_users"].append([])
            repo_issues["created_ts"].append("2023-12-05T12:00:00Z")
            repo_issues["updated_ts"].append("2023-12-05T12:00:00Z")
        payload = {"issue_number": issue_number}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateIssue",
                "description": "Create an issue with labels/assignees.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "title": {"type": "string", "description": "Issue title"},
                        "body": {"type": "string", "description": "Issue body"},
                        "assignees": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Issue assignees",
                        },
                        "labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Issue labels",
                        },
                    },
                    "required": ["owner", "repo", "title", "body", "assignees"],
                },
            },
        }
