# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTmsJobStatus(Tool):
    """Updates the status of a TMS job."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        job_id = kwargs.get("job_id")
        new_status = kwargs.get("status")
        jobs = data.get("tms_jobs", [])
        for job in jobs:
            if job.get("id") == job_id:
                job["status"] = new_status
                return json.dumps({"status": "success", "message": f"Status for TMS job '{job_id}' updated to '{new_status}'."})
        return json.dumps({"error": f"TMS job with ID '{job_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_tms_job_status",
                "description": "Updates the status of a TMS job.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {"type": "string"},
                        "status": {"type": "string"}
                    },
                    "required": ["job_id", "status"],
                },
            },
        }
