from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateDB(Tool):  #WRITE
    @staticmethod
    #For values that are lists, it will simply add the new value to the list.
    #To modify or delete a value in a list, you need to provide the complete list as desired, and it will replace the existing list.
    def invoke(
        data: dict[str, Any],
        database_name: str,
        filter_params: dict[str, Any],
        update_params: dict[str, Any],
    ) -> str:
        pass
        db = data.get(database_name, [])
        filtered_db = [row for row in db if _match(row, filter_params)]
        for row in filtered_db:
            _apply_update(row, update_params)
        payload = filtered_db
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDb",
                "description": "Edit entries in the database based on filter parameters and update parameters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "database_name": {
                            "type": "string",
                            "description": "The name of the database to edit. This should match the key in the data dictionary.",
                        },
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary/List of ways to filter items in the database. Dictionaries are AND conditions, lists are OR conditions.",
                        },
                        "update_params": {
                            "type": "object",
                            "description": "Dictionary of fields to update and their new values.",
                        },
                    },
                    "required": ["filter_params", "update_params"],
                },
            },
        }
