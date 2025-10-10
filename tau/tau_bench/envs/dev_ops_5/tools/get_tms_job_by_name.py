# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTmsJobByName(Tool):
    """Retrieves a TMS job by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], job_name) -> str:
        jobs = data.get("tms_jobs", [])
        for job in jobs:
            if job.get("job_name") == job_name:
                return json.dumps(job)
        return json.dumps({"error": f"TMS job with name '{job_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_tms_job_by_name",
                "description": "Retrieves a TMS job by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"job_name": {"type": "string"}},
                    "required": ["job_name"],
                },
            },
        }
