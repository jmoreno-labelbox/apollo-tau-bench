from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DeprecateSymbol(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "DeprecateSymbol",
                "description": "Marks a symbol record as deprecated.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol_id": {"type": "string", "description": "Symbol id"}
                    },
                    "required": ["symbol_id"],
                },
            },
        }

    @staticmethod
    def invoke(data, symbol_id=None):
        pass
        symbols = data.get("symbols", {}).values()
        sym = next((s for s in symbols.values() if s.get("id") == symbol_id), None)
        if not sym:
            payload = {"error": "symbol_not_found", "symbol_id": symbol_id}
            out = json.dumps(payload)
            return out
        sym["status"] = "deprecated"
        payload = {"symbol": sym}
        out = json.dumps(payload, indent=2)
        return out
