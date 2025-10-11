# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _match(rows, filters):
    # Make the row values a list if not for uniform handling
    if not isinstance(rows, list):
        rows = [rows]

    if isinstance(filters, list):
        # OR condition for lists; return true if any match
        return any(_match(rows, single_filter) for single_filter in filters)

    elif isinstance(filters, dict):
        for filter_key, filter_value in filters.items():
            # AND condition for dictionaries; any filter can return false
            # Only if none return false does it pass and return true
            if not any(_match(row.get(filter_key), filter_value) for row in rows):
                return False

    else:
        if filters not in rows:
            return False
    return True

class GetInfoFromDB(Tool): # ACCESS
    @staticmethod
    def invoke(data: Dict[str, Any], database_name:str, filter_params: Dict[str, Any], required_fields: List[str] = None) -> str:
        db = data.get(database_name, [])

        filtered_db = [row for row in db if _match(row, filter_params)]
        if not filtered_db:
            return json.dumps({"error": "No entries found matching the filter parameters."})

        # Return the complete filtered database if no particular fields are specified.
        if required_fields is None:
            return json.dumps(filtered_db)

        # If not, return solely the designated fields.
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
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries."
                        }
                    },
                    "required": ["filter_params"]
                }
            }
        }