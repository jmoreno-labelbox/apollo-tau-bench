from tau_bench.envs.tool import Tool
import json
from typing import Any

class ReserveLicense(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str, count: int, reason: str) -> str:
        pass
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            payload = {"status": "error", "reason": "license_not_found"}
            out = json.dumps(payload)
            return out
        if inv["used_seats"] + inv["reserved_seats"] + count > inv["total_seats"]:
            payload = {"status": "error", "reason": "no_capacity"}
            out = json.dumps(payload)
            return out
        inv["reserved_seats"] += count
        payload = {"status": "ok", "inventory": inv, "reason": reason}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReserveLicense",
                "description": "Reserve seats for a license (inventory reserved_seats).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {"type": "string"},
                        "count": {"type": "integer"},
                        "reason": {"type": "string"},
                    },
                    "required": ["license_id", "count", "reason"],
                },
            },
        }
