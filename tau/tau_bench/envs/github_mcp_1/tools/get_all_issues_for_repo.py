from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAllIssuesForRepo(Tool):
    """
    Lists all issues for a given repository from the issues DB.
    Inputs: owner, repo_name (alias: repo_name)
    """

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = "", repo_name: str = "") -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()

        if not owner or not repo_name:
            payload = {
                    "error": "Parameters 'owner' and 'repo_name' (or 'repo_name') are required."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Load issues DB
        issues_db = _convert_db_to_list(data.get("issues", {}).values())
        if not isinstance(issues_db, list):
            payload = {"error": "Invalid issues DB: expected a list at data['issues']."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Find repo bucket
        rec = next(
            (
                r
                for r in issues_db
                if r.get("owner") == owner and r.get("repo_name") == repo_name
            ),
            None,
        )
        if rec is None:
            payload = {"error": f"No issues found for repository '{owner}/{repo_name}'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        issue_numbers: list[int] = rec.get("issue_numbers", [])

        def get_at(key: str, i: int):
            arr = rec.get(key, [])
            return arr[i] if i < len(arr) else None

        # Build (number, index) pairs and sort by issue number
        indexed: list[tuple] = [(num, i) for i, num in enumerate(issue_numbers)]
        indexed.sort(key=lambda t: t[0])

        issues_out: list[dict[str, Any]] = []
        for num, idx in indexed:
            issues_out.append(
                {
                    "number": num,
                    "title": get_at("issue_titles", idx),
                    "body": get_at("issue_bodies", idx),
                    "state": get_at("issue_states", idx),
                    "labels": get_at("labels", idx),
                    "assignees": get_at("assignees", idx),
                    "comments": get_at("issue_comments", idx),
                    "comment_users": get_at("issue_comment_users", idx),
                    "created_ts": get_at("created_ts", idx),
                    "updated_ts": get_at("updated_ts", idx),
                }
            )
        payload = {
                "owner": owner,
                "repo_name": repo_name,
                "count": len(issues_out),
                "issues": issues_out,
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
                "name": "GetAllIssuesForRepo",
                "description": "List all issues for a repository from the issues DB.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name (alias accepted as 'repo_name').",
                        },
                    },
                    "required": ["owner", "repo_name"],
                },
            },
        }
