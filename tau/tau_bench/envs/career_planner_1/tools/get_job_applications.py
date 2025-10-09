from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetJobApplications(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], job_id: str = None) -> str:
        apps = [
            app
            for app in data.get("job_applications", [])
            if app.get("job_id") == job_id
        ]
        payload = apps
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetJobApplications",
                "description": "Returns all applications for a given job ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {
                            "type": "string",
                            "description": "Job ID to fetch applications for",
                        }
                    },
                    "required": ["job_id"],
                },
            },
        }
