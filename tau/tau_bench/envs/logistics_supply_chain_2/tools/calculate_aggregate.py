# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateAggregate(Tool):
    """Tool to calculate aggregates."""

    @staticmethod
    def invoke(data: Dict[str, Any], agg, json, key, value, list_of_ids = None, value2 = None) -> str:
        agg_kw = agg
        data_kw = json
        value_kw = value
        value_kw2 = value2
        key_kw = key
        dataset = data.get(data_kw, [])

        result = []
        for instance in dataset:
            if value_kw2:
                result.append([instance[key_kw], instance[value_kw][value_kw2]])
            else:
                result.append([instance[key_kw], instance[value_kw]])
        if list_of_ids:
            result = [r for r in result if r[0] in list_of_ids]
        result = sorted(result, key=lambda x: x[1])
        min_value = min([result[i][1] for i in range(len(result))])
        min_keys = [r[0] for r in result if r[1]==min_value]
        max_value = max([result[i][1] for i in range(len(result))])
        max_keys = [r[0] for r in result if r[1]==max_value]

        if agg_kw == "min":
            return json.dumps({
                key_kw: min_keys,
                value_kw: min_value
            }, indent=2)
        elif agg_kw == "max":
            return json.dumps({
                key_kw: max_keys,
                value_kw: max_value
            }, indent=2)
        elif agg_kw == "both":
            return json.dumps({
                'min_key': min_keys,
                'min_value': min_value,
                'max_key': max_keys,
                'max_value': max_value
            }, indent=2)
        elif agg_kw == "avg":
            return json.dumps(sum([r[1] for r in result])/len(result), indent=2)
        else:
            return json.dumps({"error": "No aggregate mentioned."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_aggregate",
                "description": "Calculate aggregate by IDs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "agg": {
                            "type": "string",
                            "description": "aggregate minimum, maximum, average"
                        },
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
                        "value2": {
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
                    "required": ["agg", "data", "value", "key"]
                }
            }
        }
