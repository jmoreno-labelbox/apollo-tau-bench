from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class NormalizeOrgCacheTimestamps(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], org_id: str) -> str:
        org_id = _sid(org_id)
        jobs = data.get("cache_jobs", {}).values()
        updated: list[str] = []
        for j in jobs.values():
            if j.get("org_id") == org_id:
                j["last_run_time"] = FIXED_NOW
                updated.append(j.get("job_id"))
        payload = {"org_id": org_id, "updated": updated}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NormalizeOrgCacheTimestamps",
                "description": "Normalize all cache job timestamps for an org to the fixed time.",
                "parameters": {
                    "type": "object",
                    "properties": {"org_id": {"type": "string"}},
                    "required": ["org_id"],
                },
            },
        }
