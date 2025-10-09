from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CalculateAggregate(Tool):
    """Utility for computing aggregate values."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        agg: str,
        json: str = None,
        value: str = None,
        key: str = None,
        value2: str = None,
        list_of_ids: list = None,
        json_name: str = None
    ) -> str:
        import json as json_module
        # Support both 'json' and 'json_name' for backward compatibility
        data_key = json_name or json
        dataset = data.get(data_key, [])

        result = []
        for instance in dataset:
            if value2:
                result.append([instance[key], instance[value][value2]])
            else:
                result.append([instance[key], instance[value]])
        if list_of_ids:
            result = [r for r in result if r[0] in list_of_ids]
        result = sorted(result, key=lambda x: x[1])
        min_value = min([result[i][1] for i in range(len(result))])
        min_keys = [r[0] for r in result if r[1] == min_value]
        max_value = max([result[i][1] for i in range(len(result))])
        max_keys = [r[0] for r in result if r[1] == max_value]

        if agg == "min":
            payload = {key: min_keys, value: min_value}
            out = json_module.dumps(payload, indent=2)
            return out
        elif agg == "max":
            payload = {key: max_keys, value: max_value}
            out = json_module.dumps(payload, indent=2)
            return out
        elif agg == "both":
            payload = {
                "min_key": min_keys,
                "min_value": min_value,
                "max_key": max_keys,
                "max_value": max_value,
            }
            out = json_module.dumps(payload, indent=2)
            return out
        elif agg == "avg":
            payload = sum([r[1] for r in result]) / len(result)
            out = json_module.dumps(payload, indent=2)
            return out
        else:
            payload = {"error": "No aggregate mentioned."}
            out = json_module.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateAggregate",
                "description": "Calculate aggregate by IDs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "agg": {
                            "type": "string",
                            "description": "aggregate minimum, maximum, average",
                        },
                        "json": {"type": "string", "description": "json file name"},
                        "key": {"type": "string", "description": "key name"},
                        "value": {"type": "string", "description": "value name"},
                        "value2": {"type": "string", "description": "value name"},
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of suppliers to choose from.",
                        },
                    },
                    "required": ["agg", "data", "value", "key"],
                },
            },
        }
