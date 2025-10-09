from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateTmsJob(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], bundle_name: str, locales: list[str], status: str
    ) -> str:
        tms = _get_table(data, "tms_jobs")
        max_id = _max_int_suffix(tms, "job_id", "TMS", 0)
        job_id = f"TMS-{max_id + 1}"
        rec = {
            "job_id": job_id,
            "bundle_name": bundle_name,
            "locales": locales,
            "status": status,
        }
        tms.append(rec)
        payload = {"job_id": job_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTmsJob",
                "description": "Creates a deterministic TMS job with next job_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "bundle_name": {"type": "string"},
                        "locales": {"type": "array", "items": {"type": "string"}},
                        "status": {"type": "string"},
                    },
                    "required": ["bundle_name", "locales", "status"],
                },
            },
        }
