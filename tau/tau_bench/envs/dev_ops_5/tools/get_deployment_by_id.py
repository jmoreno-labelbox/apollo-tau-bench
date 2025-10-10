# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDeploymentById(Tool):
    """Retrieves a deployment by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        deployment_id = kwargs.get("id")
        deployments = list(data.get("deployments", {}).values())
        for d in deployments:
            if d.get("id") == deployment_id:
                return json.dumps(d)
        return json.dumps({"error": f"Deployment with ID '{deployment_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_deployment_by_id",
                "description": "Retrieves a deployment by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
