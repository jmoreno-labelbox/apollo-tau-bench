# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReleaseLicenseReservation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], license_id: str, count: int) -> str:
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            return json.dumps({"status": "error", "reason": "license_not_found"})
        inv["reserved_seats"] = max(0, inv["reserved_seats"] - count)
        return json.dumps({"status": "ok", "inventory": inv})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "release_license_reservation",
                "description": "Release previously reserved license seats.",
                "parameters": {
                    "type": "object",
                    "properties": {"license_id": {"type": "string"}, "count": {"type": "integer"}},
                    "required": ["license_id", "count"],
                },
            },
        }
