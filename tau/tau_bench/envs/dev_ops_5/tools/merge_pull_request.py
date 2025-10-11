# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MergePullRequest(Tool):
    """Merges a pull request."""
    @staticmethod
    def invoke(data: Dict[str, Any], id) -> str:
        pr_id = id
        prs = list(data.get("pull_requests", {}).values())
        for pr in prs:
            if pr.get("id") == pr_id:
                pr["state"] = "merged"
                pr["merged_at"] = "2025-01-28T00:00:00Z"
                pr["closed_at"] = "2025-01-28T00:00:00Z"
                return json.dumps({"status": "success", "message": f"PR '{pr_id}' merged."})
        return json.dumps({"error": f"PR with ID '{pr_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "merge_pull_request",
                "description": "Merges a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
