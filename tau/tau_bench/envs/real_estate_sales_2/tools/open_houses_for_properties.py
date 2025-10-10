# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class OpenHousesForProperties(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pids = set(kwargs.get("property_ids") or [])
        date_from = kwargs.get("date_from")
        date_to = kwargs.get("date_to")
        rows = []
        for oh in (data.get("open_houses", []) or []):
            if pids and oh.get("property_id") not in pids:
                continue
            dt = oh.get("start_at", "")
            if date_from and dt < f"{date_from}T00:00:00Z":
                continue
            if date_to and dt > f"{date_to}T23:59:59Z":
                continue
            rows.append(oh)
        return json.dumps({"matches": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "open_houses_for_properties",
                "description": "Fetch open house windows for specific properties within a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_ids": {"type": "array", "items": {"type": "string"}},
                        "date_from": {"type": "string"},
                        "date_to": {"type": "string"},
                    },
                    "required": ["property_ids", "date_from", "date_to"],
                },
            },
        }
