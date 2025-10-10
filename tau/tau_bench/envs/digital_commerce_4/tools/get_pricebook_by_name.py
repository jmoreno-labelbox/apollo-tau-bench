# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPricebookByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: Any) -> str:
        pricebooks = data.get("pricebooks", [])
        match = next((pb for pb in pricebooks if pb.get("pricebook_name") == name), None)
        return json.dumps(match or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pricebook_by_name",
                "description": "Resolve a pricebook by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
