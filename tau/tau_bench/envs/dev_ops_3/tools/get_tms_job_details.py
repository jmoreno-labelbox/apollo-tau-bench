from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class get_tms_job_details(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tms_job_id: str) -> str:
        pass
        tms_jobs = data.get("tms_jobs", {}).values()
        for job in tms_jobs.values():
            if job.get("id") == tms_job_id:
                payload = job
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"TMS job with id '{tms_job_id}' not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTmsJobDetails",
                "description": "Retrieves the full details for a given TMS job.",
                "parameters": {
                    "type": "object",
                    "properties": {"tms_job_id": {"type": "string"}},
                    "required": ["tms_job_id"],
                },
            },
        }
