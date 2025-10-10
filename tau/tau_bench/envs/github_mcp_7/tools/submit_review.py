# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SubmitReview(Tool):
    """Submit a review on a PR (approve, request_changes, or comment)."""
    @staticmethod
    def invoke(data: Dict[str, Any], number, owner, repo, state, note = "") -> str:
        owner = owner or _actor_name(data)
        for p in _prs(data):
            if p.get("owner") == owner and p.get("repo") == repo and p.get("number") == number:
                p.setdefault("review_states", []).append({
                    "reviewer": _actor_name(data),
                    "state": state,
                    "note": note,
                    "created_at": get_current_timestamp(),
                })
                return json.dumps({"ok": True})
        raise RuntimeError("PR not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "submit_review",
                "description": "Submit a review on a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "state": {"type": "string", "enum": ["approve", "request_changes", "comment"]},
                        "note": {"type": "string"}
                    },
                    "required": ["repo", "number", "state"]
                }
            },
        }
