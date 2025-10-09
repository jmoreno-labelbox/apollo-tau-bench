from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetJobLicenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], job_title: str = None) -> str:
        if job_title is None:
            payload = {"status": "error", "reason": "The job_title parameter is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        group_data = data.get("rbac_group_map")

        for group in group_data:
            if group["job_title"] == job_title:
                payload = group["default_license_bundle"]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"status": "error", "reason": "Unable to find specified job_title."}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getJobLicenses",
                "description": "Gets all default licenses for a specific job title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_title": {
                            "type": "string",
                            "description": "The name of the job.",
                        },
                    },
                    "required": ["job_title"],
                },
            },
        }
