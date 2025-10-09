from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class list_tms_jobs(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        pass
        tms_jobs = data.get("tms_jobs", {}).values()
        payload = {"count": len(tms_jobs), "results": tms_jobs}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListTmsJobs",
                "description": "Retrieves a list of all jobs in the Translation Management System (TMS).",
                "parameters": {"type": "object", "properties": {}},
            },
        }
