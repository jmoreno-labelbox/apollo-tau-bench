from tau_bench.envs.tool import Tool
import json
from typing import Any
from tau_bench.envs.retail_1.tools import _match




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetInfoFromDB(Tool):  #READ
    @staticmethod
    def invoke(
        data: dict[str, Any],
        database_name: str,
        filter_params: dict[str, Any],
        required_fields: list[str] = None,
    ) -> str:
        pass
        db = _convert_db_to_list(data.get(database_name, {}))

        filtered_db = [row for row in db.values() if _match(row, filter_params)]
        if not filtered_db:
            payload = {"error": "No entries found matching the filter parameters."}
            out = json.dumps(
                payload)
            return out

        #If no specific fields are requested, return the entire filtered database.
        if required_fields is None:
            payload = filtered_db
            out = json.dumps(payload)
            return out
        payload = [
                {
                    required_field: row.get(required_field)
                    for required_field in required_fields
                }
                for row in filtered_db
            ]
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInfoFromDb",
                "description": "Filter users by parameters and return specified fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "database_name": {
                            "type": "string",
                            "description": "The name of the database to filter. This should match the key in the data dictionary.",
                        },
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary/List of ways to filter items in the database. Dictionaries are AND conditions, lists are OR conditions.",
                        },
                        "required_fields": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries.",
                        },
                    },
                    "required": ["database_name", "filter_params"],
                },
            },
        }
