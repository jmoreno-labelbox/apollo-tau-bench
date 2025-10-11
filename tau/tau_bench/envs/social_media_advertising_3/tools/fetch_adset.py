# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchAdset(Tool):
    """Return details for an ad set by ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id) -> str:
        aid = adset_id
        for a in data.get("adsets", []):
            if a.get("adset_id") == aid:
                return json.dumps(a)
        return json.dumps({"error": f"Adset {aid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_adset",
                "description": "Return details for an ad set by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }
