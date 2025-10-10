# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateDeployment(Tool):
    """Creates a new deployment record."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        deployments = list(data.get("deployments", {}).values())
        new_id_num = max([int(d["id"].split("_")[1]) for d in deployments]) + 1
        new_id = f"deploy_{new_id_num:03d}"
        
        new_deployment = {
            "id": new_id,
            "pipeline_id": kwargs.get("pipeline_id"),
            "environment_id": kwargs.get("environment_id"),
            "deployed_by": kwargs.get("deployed_by"),
            "version": kwargs.get("version"),
            "status": kwargs.get("status"),
            "deployed_at": "2025-01-28T00:00:00Z",
            "duration_minutes": 0
        }
        deployments.append(new_deployment)
        return json.dumps(new_deployment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_deployment",
                "description": "Creates a new deployment record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pipeline_id": {"type": "string"},
                        "environment_id": {"type": "string"},
                        "deployed_by": {"type": "string"},
                        "version": {"type": "string"},
                        "status": {"type": "string"}
                    },
                    "required": ["pipeline_id", "environment_id", "deployed_by", "version", "status"],
                },
            },
        }
