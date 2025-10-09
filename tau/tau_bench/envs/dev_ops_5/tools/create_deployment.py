from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateDeployment(Tool):
    """Generates a new deployment entry."""

    @staticmethod
    def invoke(data: dict[str, Any], pipeline_id: str = None, environment_id: str = None, 
               deployed_by: str = None, version: str = None, status: str = None) -> str:
        deployments = data.get("deployments", {}).values()
        new_id_num = max([int(d["id"].split("_")[1]) for d in deployments]) + 1
        new_id = f"deploy_{new_id_num:03d}"

        new_deployment = {
            "id": new_id,
            "pipeline_id": pipeline_id,
            "environment_id": environment_id,
            "deployed_by": deployed_by,
            "version": version,
            "status": status,
            "deployed_at": "2025-01-28T00:00:00Z",
            "duration_minutes": 0,
        }
        data["deployments"][new_deployment["deployment_id"]] = new_deployment
        payload = new_deployment
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDeployment",
                "description": "Creates a new deployment record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pipeline_id": {"type": "string"},
                        "environment_id": {"type": "string"},
                        "deployed_by": {"type": "string"},
                        "version": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": [
                        "pipeline_id",
                        "environment_id",
                        "deployed_by",
                        "version",
                        "status",
                    ],
                },
            },
        }
