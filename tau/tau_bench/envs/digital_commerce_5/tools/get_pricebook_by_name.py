from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPricebookByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: Any) -> str:
        pricebooks = data.get("pricebooks", {}).values()
        match = next(
            (pb for pb in pricebooks.values() if pb.get("pricebook_name") == name), None
        )
        payload = match or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPricebookByName",
                "description": "Resolve a pricebook by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
