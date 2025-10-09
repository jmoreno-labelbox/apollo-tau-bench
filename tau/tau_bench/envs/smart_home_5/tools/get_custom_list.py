from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCustomList(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], list_id: str | None = None, list_name: str | None = None
    ) -> str:
        custom_lists = data.get("custom_lists", [])
        if not list_id and not list_name:
            payload = custom_lists
            out = json.dumps(payload, indent=2)
            return out

        result = []
        for l in custom_lists:
            if list_id and l.get("list_id") == list_id:
                result.append(l)
            elif list_name and l.get("name") == list_name:
                result.append(l)
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomList",
                "description": "Get one or more custom lists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The ID of the list to retrieve.",
                        },
                        "list_name": {
                            "type": "string",
                            "description": "The name of the list to retrieve.",
                        },
                    },
                    "additionalProperties": False,
                },
            },
        }
