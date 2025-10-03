from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetDeploymentById(Tool):
    """Fetches a deployment using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        deployment_id = id
        deployments = data.get("deployments", [])
        for d in deployments:
            if d.get("id") == deployment_id:
                payload = d
                out = json.dumps(payload)
                return out
        payload = {"error": f"Deployment with ID '{deployment_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDeploymentById",
                "description": "Retrieves a deployment by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
