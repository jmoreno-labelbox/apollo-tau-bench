from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetConsultantProfile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], consultant_id: str = None) -> str:
        cid = consultant_id
        cons = next(
            (c for c in data.get("consultants", []) if c.get("consultant_id") == cid),
            None,
        )
        payload = cons or {"error": f"Consultant {cid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getConsultantProfile",
                "description": "Retrieve consultant master data.",
                "parameters": {
                    "type": "object",
                    "properties": {"consultant_id": {"type": "string"}},
                    "required": ["consultant_id"],
                },
            },
        }
