from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetTmsJobByName(Tool):
    """Fetches a TMS job using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], job_name: str = None) -> str:
        jobs = data.get("tms_jobs", {}).values()
        for job in jobs:
            if job.get("job_name") == job_name:
                payload = job
                out = json.dumps(payload)
                return out
        payload = {"error": f"TMS job with name '{job_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTmsJobByName",
                "description": "Retrieves a TMS job by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"job_name": {"type": "string"}},
                    "required": ["job_name"],
                },
            },
        }
