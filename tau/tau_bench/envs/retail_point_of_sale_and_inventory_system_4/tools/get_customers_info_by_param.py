from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCustomersInfoByParam(Tool):  #VIEW
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filter_params: dict[str, Any],
        info_items: list[str] = None
    ) -> str:
        db = _convert_db_to_list(data.get("customers", {}).values())
        filtered_db = _filter_db(db, filter_params)
        if not info_items:
            payload = filtered_db
            out = json.dumps(payload)
            return out
        payload = [
            {info_item: row.get(info_item) for info_item in info_items}
            for row in filtered_db
        ]
        out = json.dumps(payload)
        return out
        pass
        db = _convert_db_to_list(data.get("customers", {}).values())
        filtered_db = _filter_db(db, filter_params)
        if not info_items:
            payload = filtered_db
            out = json.dumps(payload)
            return out
        payload = [
                {info_item: row.get(info_item) for info_item in info_items}
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
                "name": "GetCustomersInfoByParam",
                "description": "Filter customers by parameters and return specified fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary of ways to filter items in the database. To pass the filter an item must match one of the possible given values for all the filtering paramets",
                        },
                        "info_items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries.",
                        },
                    },
                    "required": ["filter_params"],
                },
            },
        }
