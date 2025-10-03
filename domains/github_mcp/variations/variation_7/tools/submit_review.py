from tau_bench.envs.tool import Tool
import json
from typing import Any

class SubmitReview(Tool):
    """Provide a review on a pull request (approve, request changes, or comment)."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, number: int = None, state: str = None, note: str = "") -> str:
        owner = owner or _actor_name(data)
        for p in _prs(data):
            if (
                p.get("owner") == owner
                and p.get("repo") == repo
                and p.get("number") == number
            ):
                p.setdefault("review_states", []).append(
                    {
                        "reviewer": _actor_name(data),
                        "state": state,
                        "note": note,
                        "created_at": get_current_timestamp(),
                    }
                )
                payload = {"ok": True}
                out = json.dumps(payload)
                return out
        raise RuntimeError("PR not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "submitReview",
                "description": "Submit a review on a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "state": {
                            "type": "string",
                            "enum": ["approve", "request_changes", "comment"],
                        },
                        "note": {"type": "string"},
                    },
                    "required": ["repo", "number", "state"],
                },
            },
        }
