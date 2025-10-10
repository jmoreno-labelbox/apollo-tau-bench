# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReserveLicense(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], license_id: str, count: int, reason: str) -> str:
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            return json.dumps({"status": "error", "reason": "license_not_found"})
        if inv["used_seats"] + inv["reserved_seats"] + count > inv["total_seats"]:
            return json.dumps({"status": "error", "reason": "no_capacity"})
        inv["reserved_seats"] += count
        return json.dumps({"status": "ok", "inventory": inv, "reason": reason})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reserve_license",
                "description": "Reserve seats for a license (inventory reserved_seats).",
                "parameters": {
                    "type": "object",
                    "properties": {"license_id": {"type": "string"}, "count": {"type": "integer"}, "reason": {"type": "string"}},
                    "required": ["license_id", "count", "reason"],
                },
            },
        }
