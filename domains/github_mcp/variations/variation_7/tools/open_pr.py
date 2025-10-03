from tau_bench.envs.tool import Tool
import json
from typing import Any

class OpenPR(Tool):
    """Initiate a pull request."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str = None,
        repo: str = None,
        title: str = None,
        head_branch: str = None,
        base_branch: str = "main"
    ) -> str:
        owner = owner or _actor_name(data)
        if not (_find_repo(data, owner, repo)):
            raise RuntimeError("Repository not found")
        seq = (
            sum(
                1
                for pr in _prs(data)
                if pr.get("owner") == owner and pr.get("repo") == repo
            )
            + 1
        )
        pr = {
            "owner": owner,
            "repo": repo,
            "number": seq,
            "title": title or f"PR {seq}",
            "state": "open",
            "head": head_branch,
            "base": base_branch,
            "labels": [],
            "review_states": [],
            "created_at": get_current_timestamp(),
        }
        _prs(data).append(pr)
        payload = pr
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "OpenPr",
                "description": "Open a pull request with head and base branches.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "title": {"type": "string"},
                        "head_branch": {"type": "string"},
                        "base_branch": {"type": "string"},
                    },
                    "required": ["repo", "head_branch"],
                },
            },
        }
