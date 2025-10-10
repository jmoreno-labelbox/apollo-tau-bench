# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_tms_job_details(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], tms_job_id: str) -> str:
        tms_jobs = data.get("tms_jobs", [])
        for job in tms_jobs:
            if job.get("id") == tms_job_id:
                return json.dumps(job, indent=2)
        return json.dumps({"error": f"TMS job with id '{tms_job_id}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "get_tms_job_details", "description": "Retrieves the full details for a given TMS job.", "parameters": { "type": "object", "properties": { "tms_job_id": { "type": "string" } }, "required": ["tms_job_id"] } } }
