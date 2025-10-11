# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateDriveTimeHops(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], property_ids, max_minutes = 30) -> str:
        stops = property_ids or []
        hops = [{"from": stops[i], "to": stops[i + 1], "minutes": 20} for i in range(max(0, len(stops) - 1))]
        ok = all(h["minutes"] <= max_minutes for h in hops)
        return json.dumps({"ok": ok, "hops": hops, "max_minutes": max_minutes}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_drive_time_hops",
                "description": "Compute if sequential hops fit within max drive minutes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_ids": {"type": "array", "items": {"type": "string"}},
                        "max_minutes": {"type": "integer"},
                    },
                    "required": ["property_ids", "max_minutes"],
                },
            },
        }
