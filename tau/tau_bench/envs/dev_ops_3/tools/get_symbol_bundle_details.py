# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_symbol_bundle_details(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], symbol_id: str) -> str:
        symbols = data.get("symbols", [])
        for s in symbols:
            if s.get("id") == symbol_id:
                return json.dumps(s, indent=2)
        return json.dumps({"error": f"Symbol bundle with id '{symbol_id}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "get_symbol_bundle_details", "description": "Retrieves the details of a specific symbol bundle by its ID.", "parameters": { "type": "object", "properties": { "symbol_id": { "type": "string" } }, "required": ["symbol_id"] } } }
