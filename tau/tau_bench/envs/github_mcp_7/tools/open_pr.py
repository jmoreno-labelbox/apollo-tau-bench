# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class OpenPR(Tool):
    """Open a pull request."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        title = kwargs.get("title")
        head = kwargs.get("head_branch")
        base = kwargs.get("base_branch", "main")
        if not (_find_repo(data, owner, repo)):
            raise RuntimeError("Repository not found")
        seq = sum(1 for pr in _prs(data) if pr.get("owner") == owner and pr.get("repo") == repo) + 1
        pr = {
            "owner": owner,
            "repo": repo,
            "number": seq,
            "title": title or f"PR {seq}",
            "state": "open",
            "head": head,
            "base": base,
            "labels": [],
            "review_states": [],
            "created_at": get_current_timestamp(),
        }
        _prs(data).append(pr)
        return json.dumps(pr)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "open_pr",
                "description": "Open a pull request with head and base branches.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "title": {"type": "string"},
                        "head_branch": {"type": "string"},
                        "base_branch": {"type": "string"}
                    },
                    "required": ["repo", "head_branch"]
                }
            },
        }
