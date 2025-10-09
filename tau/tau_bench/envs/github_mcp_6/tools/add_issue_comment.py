from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddIssueComment(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], owner: str, repo: str, issue_number: int, body: str
    ) -> str:
        """Add a comment to an issue."""
        pass
        issues_data = data.get("issues", {}).values()

        for issue_entry in issues_data.values():
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                try:
                    issue_idx = issue_entry["issue_numbers"].index(issue_number)
                    issue_entry["issue_comments"][issue_idx].append(body)
                    issue_entry["issue_comment_users"][issue_idx].append(owner)
                    issue_entry["updated_ts"][issue_idx] = "2023-12-05T12:00:00Z"

                    comment_id = len(issue_entry["issue_comments"][issue_idx])
                    payload = {"comment_id": comment_id}
                    out = json.dumps(payload, indent=2)
                    return out
                except ValueError:
                    pass
        payload = {"error": f"Issue #{issue_number} not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddIssueComment",
                "description": "Add a comment to an issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "issue_number": {
                            "type": "integer",
                            "description": "Issue number",
                        },
                        "body": {"type": "string", "description": "Comment body"},
                    },
                    "required": ["owner", "repo", "issue_number", "body"],
                },
            },
        }
