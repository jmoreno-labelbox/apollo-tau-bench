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

def _apply_update(row, update_params):
    for key, value in update_params.items():
        if isinstance(value, dict) and isinstance(row.get(key), dict):
            _apply_update(row[key], value)
        elif isinstance(row.get(key), list) and not isinstance(value, list):
                row[key].append(value)
        else:
            row[key] = value
    return row

class UpdateDB(Tool): # CREATE
    @staticmethod
    # It will simply add the new value to the existing list.
    # To modify or delete a value in a list, the complete list must be provided in its desired state, which will overwrite the existing list.
    def invoke(data: Dict[str, Any], database_name:str, filter_params: Dict[str, Any], update_params: Dict[str, Any]) -> str:
        db = data.get(database_name, [])
        filtered_db = [row for row in db if _match(row, filter_params)]
        for row in filtered_db:
            _apply_update(row, update_params)
        return json.dumps(filtered_db)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_db",
                "description": "Edit entries in the database based on filter parameters and update parameters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "database_name": {
                            "type": "string",
                            "description": "The name of the database to edit. This should match the key in the data dictionary."
                        },
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary/List of ways to filter items in the database. Dictionaries are AND conditions, lists are OR conditions."
                        },
                        "update_params": {
                            "type": "object",
                            "description": "Dictionary of fields to update and their new values."
                        }
                    },
                    "required": ["filter_params", "update_params"]
                }
            }
        }