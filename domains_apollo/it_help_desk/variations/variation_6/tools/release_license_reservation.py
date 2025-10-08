from tau_bench.envs.tool import Tool
import json
from typing import Any

class ReleaseLicenseReservation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str, count: int) -> str:
        pass
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            payload = {"status": "error", "reason": "license_not_found"}
            out = json.dumps(payload)
            return out
        inv["reserved_seats"] = max(0, inv["reserved_seats"] - count)
        payload = {"status": "ok", "inventory": inv}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReleaseLicenseReservation",
                "description": "Release previously reserved license seats.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {"type": "string"},
                        "count": {"type": "integer"},
                    },
                    "required": ["license_id", "count"],
                },
            },
        }
