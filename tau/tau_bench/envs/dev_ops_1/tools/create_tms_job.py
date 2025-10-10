# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateTmsJob(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], bundle_name: str, locales: List[str], status: str) -> str:
        tms = _get_table(data, "tms_jobs")
        max_id = _max_int_suffix(tms, "job_id", "TMS", 0)
        job_id = f"TMS-{max_id + 1}"
        rec = {"job_id": job_id, "bundle_name": bundle_name, "locales": locales, "status": status}
        tms.append(rec)
        return json.dumps({"job_id": job_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_tms_job", "description": "Creates a deterministic TMS job with next job_id.", "parameters": {"type": "object", "properties": {"bundle_name": {"type": "string"}, "locales": {"type": "array", "items": {"type": "string"}}, "status": {"type": "string"}}, "required": ["bundle_name", "locales", "status"]}}}
