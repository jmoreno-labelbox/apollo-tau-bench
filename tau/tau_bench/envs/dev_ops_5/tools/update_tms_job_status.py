from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateTmsJobStatus(Tool):
    """Modifies the status of a TMS job."""

    @staticmethod
    def invoke(data: dict[str, Any], job_id: str = None, status: str = None) -> str:
        jobs = data.get("tms_jobs", [])
        for job in jobs:
            if job.get("id") == job_id:
                job["status"] = status
                payload = {
                    "status": "success",
                    "message": f"Status for TMS job '{job_id}' updated to '{status}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"TMS job with ID '{job_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateTmsJobStatus",
                "description": "Updates the status of a TMS job.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["job_id", "status"],
                },
            },
        }
