# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdatePullRequestState(Tool):
    """Updates the state of a pull request (e.g., 'open', 'closed')."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pull_request_id = kwargs.get("id")
        new_state = kwargs.get("state")
        pull_requests = list(data.get("pull_requests", {}).values())
        
        for pr in pull_requests:
            if pr.get("id") == pull_request_id:
                pr["state"] = new_state
                if new_state == "closed" and not pr.get("merged_at"):
                    pr["closed_at"] = "2025-01-28T00:00:00Z"  # Use a consistent placeholder timestamp
                return json.dumps({
                    "status": "success",
                    "message": f"State for pull request '{pull_request_id}' updated to '{new_state}'."
                })
        
        return json.dumps({"error": f"Pull request with ID '{pull_request_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_pull_request_state",
                "description": "Updates the state of a pull request (e.g., 'open', 'closed').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "The unique ID of the pull request.",
                        },
                        "state": {
                            "type": "string",
                            "description": "The new state for the pull request (e.g., 'open', 'closed').",
                        }
                    },
                    "required": ["id", "state"],
                },
            },
        }
