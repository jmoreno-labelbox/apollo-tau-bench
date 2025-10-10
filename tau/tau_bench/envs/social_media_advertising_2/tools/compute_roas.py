# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeRoas(Tool):
    """Compute ROAS (revenue/spend) for an adset on a date."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid, date = kwargs.get("adset_id"), kwargs.get("date")
        for i in list(data.get("f_insights", {}).values()):
            if i.get("adset_id") == aid and i.get("date") == date:
                s, r = i.get("spend", 0), i.get("revenue", 0)
                return json.dumps({"adset_id": aid, "roas": round(r / s, 2) if s > 0 else 0})
        return json.dumps({"error": "No data to calc ROAS"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_roas",
                "description": "Compute ROAS (revenue/spend) for an adset on a date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["adset_id", "date"],
                },
            },
        }
