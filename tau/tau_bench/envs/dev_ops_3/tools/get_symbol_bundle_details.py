from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class get_symbol_bundle_details(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], symbol_id: str) -> str:
        pass
        symbols = data.get("symbols", [])
        for s in symbols:
            if s.get("id") == symbol_id:
                payload = s
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Symbol bundle with id '{symbol_id}' not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSymbolBundleDetails",
                "description": "Retrieves the details of a specific symbol bundle by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"symbol_id": {"type": "string"}},
                    "required": ["symbol_id"],
                },
            },
        }
