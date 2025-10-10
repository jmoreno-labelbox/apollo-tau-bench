# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllIssuesForRepo(Tool):
    """
    Lists all issues for a given repository from the issues DB.
    Inputs: owner, repo_name (alias: repo_name)
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()

        if not owner or not repo_name:
            return json.dumps(
                {"error": "Parameters 'owner' and 'repo_name' (or 'repo_name') are required."},
                indent=2
            )

        # Load issues DB
        issues_db = list(data.get("issues", {}).values())
        if not isinstance(issues_db, list):
            return json.dumps({"error": "Invalid issues DB: expected a list at data['issues']."}, indent=2)

        # Find repo bucket
        rec = next((r for r in issues_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No issues found for repository '{owner}/{repo_name}'."}, indent=2)

        issue_numbers: List[int] = rec.get("issue_numbers", [])

        def get_at(key: str, i: int):
            arr = rec.get(key, [])
            return arr[i] if i < len(arr) else None

        # Build (number, index) pairs and sort by issue number
        indexed: List[tuple] = [(num, i) for i, num in enumerate(issue_numbers)]
        indexed.sort(key=lambda t: t[0])

        issues_out: List[Dict[str, Any]] = []
        for num, idx in indexed:
            issues_out.append({
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
            })

        return json.dumps(
            {
                "owner": owner,
                "repo_name": repo_name,
                "count": len(issues_out),
                "issues": issues_out
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_issues_for_repo",
                "description": "List all issues for a repository from the issues DB.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias accepted as 'repo_name')."}
                    },
                    "required": ["owner", "repo_name"]
                }
            }
        }
