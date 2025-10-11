# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
def _repos(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("repositories", [])


def _issues(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("issues", [])

def _find_repo(data: Dict[str, Any], owner: str, repo: str) -> Optional[Dict[str, Any]]:
    for r in _repos(data):
        if r.get("owner") == owner and (r.get("repo_name") or r.get("name")) == repo:
            return r
    return None

def _actor_name(data: Dict[str, Any]) -> str:
    auth = data.get("authentication") or [{}]
    return auth[0].get("username") or "anonymous"

class OpenIssue(Tool):
    """Open a new issue."""
    @staticmethod
    def invoke(data: Dict[str, Any], owner, repo, title, body = "") -> str:
        owner = owner or _actor_name(data)
        if not (_find_repo(data, owner, repo)):
            raise RuntimeError("Repository not found")
        if not title:
            raise RuntimeError("'title' is required")
        seq = sum(1 for it in _issues(data) if it.get("owner") == owner and it.get("repo") == repo) + 1
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
        return json.dumps(issue)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "open_issue",
                "description": "Create an issue in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"}
                    },
                    "required": ["repo", "title"]
                }
            },
        }