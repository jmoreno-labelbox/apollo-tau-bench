# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRollbackByDeploymentId(Tool):
    """Retrieves rollback details for a failed deployment ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        deployment_id = kwargs.get("deployment_id")
        rollbacks = data.get("rollbacks", [])
        for r in rollbacks:
            if r.get("deployment_id") == deployment_id:
                return json.dumps(r)
        return json.dumps({"error": f"Rollback for deployment ID '{deployment_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_rollback_by_deployment_id",
                "description": "Retrieves rollback details for a failed deployment ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"deployment_id": {"type": "string"}},
                    "required": ["deployment_id"],
                },
            },
        }
