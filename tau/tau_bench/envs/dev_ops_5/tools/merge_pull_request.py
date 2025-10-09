from tau_bench.envs.tool import Tool
import json
from typing import Any

class MergePullRequest(Tool):
    """Combines a pull request."""

    def invoke(
        data: dict[str, Any],
        id: Any = None,
        pr_id: str = None
    ) -> str:
        prs = data.get("pull_requests", [])
        for pr in prs:
            if pr.get("id") == pr_id:
                pr["state"] = "merged"
                pr["merged_at"] = "2025-01-28T00:00:00Z"
                pr["closed_at"] = "2025-01-28T00:00:00Z"
                payload = {"status": "success", "message": f"PR '{pr_id}' merged."}
                out = json.dumps(payload)
                return out
        payload = {"error": f"PR with ID '{pr_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "mergePullRequest",
                "description": "Merges a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
