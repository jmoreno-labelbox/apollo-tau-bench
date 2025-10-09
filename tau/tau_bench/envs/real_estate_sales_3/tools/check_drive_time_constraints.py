from tau_bench.envs.tool import Tool
import json
from typing import Any

class CheckDriveTimeConstraints(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], property_ids: list = None, max_minutes: int = 30) -> str:
        stops = property_ids or []
        hops = [
            {"from": stops[i], "to": stops[i + 1], "minutes": 20}
            for i in range(max(0, len(stops) - 1))
        ]
        ok = all(h["minutes"] <= max_minutes for h in hops.values())
        payload = {"ok": ok, "hops": hops, "max_minutes": max_minutes}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckDriveTimeConstraints",
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
