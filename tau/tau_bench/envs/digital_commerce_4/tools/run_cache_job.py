from tau_bench.envs.tool import Tool
import json
from typing import Any

class RunCacheJob(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], org_id: str, job_name: str) -> str:
        org_id = _sid(org_id)
        jobs = data.get("cache_jobs", [])
        valid_jobs = {"Load API Metadata", "Populate Cache Job"}
        if job_name not in valid_jobs:
            payload = {"error": "invalid job name"}
            out = json.dumps(payload, indent=2)
            return out
        updated = []
        for j in jobs:
            if j.get("org_id") == org_id and j.get("job_name") == job_name:
                j["last_run_status"] = "Success"
                j["last_run_time"] = FIXED_NOW
                updated.append(j.get("job_id"))
        _append_audit(data, "RUN_CACHE_JOB", org_id, {"job_name": job_name})
        _ws_append(
            data, org_id, "RUN_CACHE_JOB", {"job_name": job_name, "updated": updated}
        )
        payload = {"org_id": org_id, "job_name": job_name, "updated": updated}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "runCacheJob",
                "description": "Run a cache job for an org; sets deterministic status/time on matching job rows.",
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
