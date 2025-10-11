# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTotal(Tool):
    """Tool to calculate totals."""

    @staticmethod
    def invoke(data: Dict[str, Any], json, key, value, list_of_ids = None) -> str:
        data_kw = json
        value_kw = value
        key_kw = key
        dataset = data.get(data_kw, [])

        total = 0
        if list_of_ids:
            for instance in dataset:
                if instance[key_kw] in list_of_ids:
                    total += instance[value_kw]
        else:
            for instance in dataset:
                total += instance[value_kw]
        return json.dumps(total, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_total",
                "description": "Calculate total by IDs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "json": {
                            "type": "string",
                            "description": "json file name"
                        },
                        "key": {
                            "type": "string",
                            "description": "key name"
                        },
                        "value": {
                            "type": "string",
                            "description": "value name"
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of suppliers to choose from."
                        }
                    },
                    "required": ["data", "value", "key"]
                }
            }
        }
