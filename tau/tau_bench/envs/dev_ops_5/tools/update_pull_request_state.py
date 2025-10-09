from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdatePullRequestState(Tool):
    """Modifies the status of a pull request (e.g., 'open', 'closed')."""

    def invoke(
        data: dict[str, Any],
        id: Any = None,
        new_state: str = None,
        pull_request_id: str = None
    ) -> str:
        pull_requests = data.get("pull_requests", [])

        for pr in pull_requests:
            if pr.get("id") == pull_request_id:
                pr["state"] = new_state
                if new_state == "closed" and not pr.get("merged_at"):
                    pr["closed_at"] = (
                        "2025-01-28T00:00:00Z"  # Employ a uniform placeholder timestamp
                    )
                payload = {
                    "status": "success",
                    "message": f"State for pull request '{pull_request_id}' updated to '{new_state}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Pull request with ID '{pull_request_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updatePullRequestState",
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
                        },
                    },
                    "required": ["id", "state"],
                },
            },
        }
