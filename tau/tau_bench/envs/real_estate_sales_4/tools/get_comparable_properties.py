from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetComparableProperties(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], property_id: str = None) -> str:
        if not property_id:
            payload = {"error": "property_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        comparables = data.get("comparables", [])
        property_comps = [c for c in comparables if c.get("property_id") == property_id]
        payload = {
                "property_id": property_id,
                "comparable_count": len(property_comps),
                "comparables": property_comps,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetComparableProperties",
                "description": "Get comparable properties for a specific property",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {
                            "type": "string",
                            "description": "Property ID to get comparables for",
                        }
                    },
                    "required": ["property_id"],
                },
            },
        }
