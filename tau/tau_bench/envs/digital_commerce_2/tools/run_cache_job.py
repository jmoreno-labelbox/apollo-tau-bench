# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RunCacheJob(Tool):
    """Run a cache job for an org (idempotent). Sets last_run_status='Success' and last_run_time=policy NOW."""

    POLICY_NOW = "2025-08-10T12:00:00Z"

    @staticmethod
    def invoke(data: Dict[str, Any], org_id: Any, job_name: Any) -> str:
        if not org_id or not job_name:
            return json.dumps(
                {"error": "Missing required fields: org_id and/or job_name"}, indent=2
            )
        jobs = data.setdefault("cache_jobs", [])
        for job in jobs:
            if job.get("org_id") == org_id and job.get("job_name") == job_name:
                job["last_run_status"] = "Success"
                job["last_run_time"] = RunCacheJob.POLICY_NOW
                return json.dumps(job, indent=2)
        next_id = str(max([int(j.get("job_id")) for j in jobs] + [300]) + 1)
        record = {
            "job_id": next_id,
            "org_id": org_id,
            "job_name": job_name,
            "last_run_status": "Success",
            "last_run_time": RunCacheJob.POLICY_NOW,
        }
        jobs.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "run_cache_job",
                "description": "Mark a cache job as run for the org (Success at policy NOW); creates job if missing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "job_name": {"type": "string"},
                    },
                    "required": ["org_id", "job_name"],
                },
            },
        }
