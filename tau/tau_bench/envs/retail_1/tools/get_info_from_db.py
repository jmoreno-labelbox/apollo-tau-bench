# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInfoFromDB(Tool): # READ
    @staticmethod
    def invoke(data: Dict[str, Any], database_name:str, filter_params: Dict[str, Any], required_fields: List[str] = None) -> str:
        db = data.get(database_name, [])

        filtered_db = [row for row in db if _match(row, filter_params)]
        if not filtered_db:
            return json.dumps({"error": "No entries found matching the filter parameters."})

        # If no specific fields are requested, return the full filtered database.
        if required_fields is None:
            return json.dumps(filtered_db)

        # Otherwise, return only the specified fields.
        return json.dumps([{required_field: row.get(required_field) for required_field in required_fields} for row in filtered_db])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_info_from_db",
                "description": "Filter users by parameters and return specified fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "database_name": {
                            "type": "string",
                            "description": "The name of the database to filter. This should match the key in the data dictionary."
                        },
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary/List of ways to filter items in the database. Dictionaries are AND conditions, lists are OR conditions."
                        },
                        "required_fields": {
                            "type": "list",
                            "items": {"type": "string"},
                            "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries."
                        }
                    },
                    "required": ["filter_params"]
                }
            }
        }
