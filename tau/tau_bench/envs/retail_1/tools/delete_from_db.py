# © Sierra

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

def _apply_delete(db, delete_params):
    # If db is a dictionary, it will return None if the delete_params match the row, or the row otherwise (which may be modified at a lower level)

    # If db is a list, we need to iterate through each row
    if isinstance(db, list):
        # If delete_params is a dictionary, we go a step deeper
        if isinstance(delete_params, dict):
            new_db = []
            for row in db:
                new_row = _apply_delete(row, delete_params)
                if new_row is not None:
                    new_db.append(new_row)
            return new_db
        elif isinstance(delete_params, list):
            # If delete_params is a list, we remove each item from the db
            for item in delete_params:
                db.remove(item)
        else:
            # If delete_params is a single value, we remove it from the db
            if delete_params in db:
                db.remove(delete_params)
    elif isinstance(db, dict):
        if isinstance(delete_params, dict):
            # If delete_params is a dictionary, we go a step deeper
            for key, value in delete_params.items():
                if key in db.keys():
                    if db[key] == value:
                        return None  # Will remove the whole row from the level above
                    else:
                        new_row = _apply_delete(db[key], value)
                        if new_row is None:
                            return None
                        else:
                            db[key] = new_row
    return db

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