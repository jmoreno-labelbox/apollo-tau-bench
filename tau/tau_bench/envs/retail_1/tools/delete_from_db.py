# © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteFromDB(Tool): # COMPOSE
    @staticmethod
    def invoke(data: Dict[str, Any], database_name:str, filter_params: Dict[str, Any], delete_params: Dict[str, Any]) -> str:
        db = data.get(database_name, [])
        filtered_db = [row for row in db if _match(row, filter_params)]
        filtered_db = _apply_delete(filtered_db, delete_params)
        return json.dumps(filtered_db)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_from_db",
                "description": "Delete entries from the database based on filter parameters and delete parameters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "database_name": {
                            "type": "string",
                            "description": "The name of the database to delete from. This should match the key in the data dictionary."
                        },
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary/List of ways to filter items in the database. Dictionaries are AND conditions, lists are OR conditions."
                        },
                        "delete_params": {
                            "type": "object",
                            "description": "Dictionary of fields to delete and their values."
                        }
                    },
                    "required": ["database_name","filter_params", "delete_params"]
                }
            }
        }
