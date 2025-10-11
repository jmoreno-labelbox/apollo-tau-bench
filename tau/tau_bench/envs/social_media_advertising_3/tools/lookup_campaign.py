# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LookupCampaign(Tool):
    """Return details for a campaign by name."""
    @staticmethod
    def invoke(data: Dict[str, Any], name) -> str:
        for c in list(data.get("campaigns", {}).values()):
            if c.get("name") == name:
                return json.dumps(c)
        return json.dumps({"error": f"Campaign {name} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "lookup_campaign",
                "description": "Return details for a campaign by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
