from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCustomListByIdOrFilter(Tool):
    """Fetch a custom list using name or id."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        list_id: str = "",
        name: str = "",
        filters: dict[str, Any] | None = None
    ) -> str:
        custom_lists = data.get("custom_lists", {}).values()
        if list_id:
            result = [l for l in custom_lists.values() if l.get("list_id") == list_id]
        elif name:
            result = [l for l in custom_lists.values() if l.get("name") == name]
        elif filters:
            result = [
                l
                for l in custom_lists.values() if all(l.get(k) == v for k, v in filters.items())
            ]
        else:
            payload = {"error": "Either 'list_id', 'name', or 'filters' must be provided"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCustomListByFilterOrId",
                "description": "Retrieve a custom list by list_id, name, or filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "Custom list id to retrieve (optional if using name or filters)",
                        },
                        "name": {
                            "type": "string",
                            "description": "Custom list name to retrieve (optional if using list_id or filters)",
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter custom lists (optional if using list_id or name)",
                            "additionalProperties": True,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
