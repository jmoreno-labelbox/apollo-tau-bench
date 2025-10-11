# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddIssueComment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, issue_number: int, body: str) -> str:
        """Add a comment to an issue."""
        issues_data = list(data.get("issues", {}).values())

        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                try:
                    issue_idx = issue_entry["issue_numbers"].index(issue_number)
                    issue_entry["issue_comments"][issue_idx].append(body)
                    issue_entry["issue_comment_users"][issue_idx].append(owner)
                    issue_entry["updated_ts"][issue_idx] = "2023-12-05T12:00:00Z"

                    comment_id = len(issue_entry["issue_comments"][issue_idx])
                    return json.dumps({"comment_id": comment_id}, indent=2)
                except ValueError:
                    pass

return json.dumps({"error": f"Issue number {issue_number} is missing"}, indent=2)

@staticmethod
def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_issue_comment",
                "description": "Add a comment to an issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "issue_number": {"type": "integer", "description": "Issue number"},
                        "body": {"type": "string", "description": "Comment body"}
                    },
                    "required": ["owner", "repo", "issue_number", "body"]
                }
            }
        }