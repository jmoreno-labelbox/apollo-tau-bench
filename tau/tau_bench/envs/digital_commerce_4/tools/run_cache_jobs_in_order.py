from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RunCacheJobsInOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        org_id: str,
        cache_jobs: list[dict[str, Any]] = None
    ) -> str:
        org_id = _sid(org_id)
        required_seq = ["Load API Metadata", "Populate Cache Job"]
        jobs = cache_jobs if cache_jobs is not None else data.get("cache_jobs", [])
        updated: list[str] = []
        for job_name in required_seq:
            for j in jobs:
                if j.get("org_id") == org_id and j.get("job_name") == job_name:
                    j["last_run_status"] = "Success"
                    j["last_run_time"] = FIXED_NOW
                    updated.append(j.get("job_id"))
            _append_audit(data, "RUN_CACHE_JOB", org_id, {"job_name": job_name})
            _ws_append(
                data,
                org_id,
                "RUN_CACHE_JOB",
                {"job_name": job_name, "updated": updated},
            )
        payload = {"org_id": org_id, "updated": updated, "sequence": required_seq}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RunCacheJobsInOrder",
                "description": "Run 'Load API Metadata' then 'Populate Cache Job' for an org; self-audits; deterministic.",
                "parameters": {
                    "type": "object",
                    "properties": {"org_id": {"type": "string"}},
                    "required": ["org_id"],
                },
            },
        }
