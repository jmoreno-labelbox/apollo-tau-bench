from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CalculateTotal(Tool):
    """Utility for computing total amounts."""

    @staticmethod
    def invoke(data: dict[str, Any], json: str = None, value: str = None, key: str = None, list_of_ids: list = None, json_name: str = None) -> str:
        # Support both 'json' and 'json_name' for backward compatibility
        data_key = json_name or json
        dataset = data.get(data_key, {}).values()

        total = 0
        if list_of_ids:
            for instance in dataset:
                if instance[key] in list_of_ids:
                    total += instance[value]
        else:
            for instance in dataset:
                total += instance[value]
        payload = total
        import json as json_module
        out = json_module.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotal",
                "description": "Calculate total by IDs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "json": {"type": "string", "description": "json file name"},
                        "key": {"type": "string", "description": "key name"},
                        "value": {"type": "string", "description": "value name"},
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of suppliers to choose from.",
                        },
                    },
                    "required": ["data", "value", "key"],
                },
            },
        }
