from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPreferredSuppliers(Tool):
    """Utility for compiling a list of suppliers that have a 'Preferred' relationship status."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_ids: list[str] = None) -> str:
        suppliers = data.get("supplier_master", [])
        result = [
            s["supplier_id"]
            for s in suppliers
            if s["relationship_status"].lower() == "preferred"
        ]
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPreferredSuppliers",
                "description": "List all suppliers with 'Preferred' relationship status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of suppliers to choose from.",
                        }
                    },
                },
            },
        }
