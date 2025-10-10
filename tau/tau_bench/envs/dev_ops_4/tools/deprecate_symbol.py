# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeprecateSymbol(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "deprecate_symbol",
                "description": "Marks a symbol record as deprecated.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol_id": {"type": "string", "description": "Symbol id"}
                    },
                    "required": ["symbol_id"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        symbol_id = kwargs.get("symbol_id")
        symbols = list(data.get("symbols", {}).values())
        sym = next((s for s in symbols if s.get("id") == symbol_id), None)
        if not sym:
            return json.dumps({"error": "symbol_not_found", "symbol_id": symbol_id})
        sym["status"] = "deprecated"
        return json.dumps({"symbol": sym}, indent=2)
