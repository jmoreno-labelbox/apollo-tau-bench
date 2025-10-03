from tau_bench.envs.tool import Tool
import json
from typing import Any

class OpenIssue(Tool):
    """Initiate a new issue."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, title: str = None, body: str = "") -> str:
        owner = owner or _actor_name(data)
        if not (_find_repo(data, owner, repo)):
            raise RuntimeError("Repository not found")
        if not title:
            raise RuntimeError("'title' is required")
        seq = (
            sum(
                1
                for it in _issues(data)
                if it.get("owner") == owner and it.get("repo") == repo
            )
            + 1
        )
        issue = {
            "owner": owner,
            "repo": repo,
            "number": seq,
            "title": title,
            "body": body,
            "state": "open",
            "assignees": [],
            "labels": [],
            "comments": [],
            "created_at": get_current_timestamp(),
        }
        _issues(data).append(issue)
        payload = issue
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "OpenIssue",
                "description": "Create an issue in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                    },
                    "required": ["repo", "title"],
                },
            },
        }
