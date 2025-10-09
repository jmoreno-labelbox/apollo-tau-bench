from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateApplicationStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], application_id: str = None, new_status: str = None) -> str:
        for app in data.get("job_applications", []):
            if app["application_id"] == application_id:
                app["status"] = new_status
                app["last_updated"] = datetime.now().isoformat()
                return f"{application_id} {new_status}"
        return "Application not found"
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateApplicationStatus",
                "description": "Updates the status of a job application.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "application_id": {
                            "type": "string",
                            "description": "Application to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status label",
                        },
                    },
                    "required": ["application_id", "new_status"],
                },
            },
        }
