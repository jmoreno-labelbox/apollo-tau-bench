from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListWarehousesByCapability(Tool):
    """A utility to locate all warehouses that possess a particular certification."""

    @staticmethod
    def invoke(data: dict[str, Any], certification: str = None) -> str:
        if not certification:
            payload = {"error": "certification is a required argument."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        warehouses = data.get("warehouses", [])
        matching_warehouses = [
            wh for wh in warehouses if certification in wh.get("certifications", [])
        ]
        payload = matching_warehouses
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListWarehousesByCapability",
                "description": "Finds all warehouses that hold a specific certification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification": {
                            "type": "string",
                            "description": "The certification to filter warehouses by (e.g., 'FDA Registered').",
                        }
                    },
                    "required": ["certification"],
                },
            },
        }
