# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
