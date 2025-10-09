from tau_bench.envs.tool import Tool
import json
from typing import Any

class DeleteFromDB(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        database_name: str,
        filter_params: dict[str, Any],
        delete_params: dict[str, Any],
    ) -> str:
        pass
        db = data.get(database_name, [])
        filtered_db = [row for row in db if _match(row, filter_params)]
        filtered_db = _apply_delete(filtered_db, delete_params)
        payload = filtered_db
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteFromDb",
                "description": "Delete entries from the database based on filter parameters and delete parameters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "database_name": {
                            "type": "string",
                            "description": "The name of the database to delete from. This should match the key in the data dictionary.",
                        },
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary/List of ways to filter items in the database. Dictionaries are AND conditions, lists are OR conditions.",
                        },
                        "delete_params": {
                            "type": "object",
                            "description": "Dictionary of fields to delete and their values.",
                        },
                    },
                    "required": ["database_name", "filter_params", "delete_params"],
                },
            },
        }
