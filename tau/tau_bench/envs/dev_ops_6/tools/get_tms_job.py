from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetTmsJob(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        rows = _table(data, "tms_jobs")
        row = next((r for r in rows if r.get("id") == id), None)
        return _ok({"tms_job": row}) if row else _err("tms_job not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTmsJob",
                "description": "Fetch TMS job by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
