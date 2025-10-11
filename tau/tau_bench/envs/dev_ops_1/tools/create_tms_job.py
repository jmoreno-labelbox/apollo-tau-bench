# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _max_int_suffix(items: List[Dict[str, Any]], key: str, prefix: str, default: int = 0) -> int:
    max_val = default
    for it in items:
        raw = it.get(key)
        if isinstance(raw, str) and raw.startswith(prefix + "-"):
            try:
                num = int(raw.split("-")[-1])
                if num > max_val:
                    max_val = num
            except ValueError:
                continue
    return max_val

def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

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