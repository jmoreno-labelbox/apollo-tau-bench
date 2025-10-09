from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateApplicationStatus(Tool):
    """Update the status of a job application."""

    @staticmethod
    def invoke(data: dict[str, Any], application_id: str = None, status: str = None) -> str:
        for a in data.get("job_applications", {}).values():
            if a.get("application_id") == application_id:
                a["status"] = status
                a["last_updated"] = datetime.utcnow().date().isoformat()
                payload = {"success": f"{application_id} status {status}"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Application not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateApplicationStatus",
                "description": "Update app status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "application_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["application_id", "status"],
                },
            },
        }
