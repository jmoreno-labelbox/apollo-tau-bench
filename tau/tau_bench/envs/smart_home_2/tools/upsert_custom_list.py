# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find






def _load(entity: str, data: Dict[str, Any]):
    """Return a *mutable copy* of a top-level collection list."""
    return [*data.get(entity, [])]

def _find(collection: List[Dict[str, Any]], entity_id: str):
    for idx, item in enumerate(collection):
        if item.get("id") == entity_id or item.get("reminder_id") == entity_id \
           or item.get("list_id") == entity_id or item.get("member_id") == entity_id:
            return idx, item
    return None, None

class UpsertCustomList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], custom_list: Dict[str, Any]) -> str:
        if not custom_list:
            return json.dumps({"error": "custom_list object required"}, indent=2)
        lists = _load("custom_lists", data)
        idx, _ = _find(lists, custom_list["list_id"])
        if idx is not None:
            lists[idx].update(custom_list)
            msg = "updated"
        else:
            lists.append(custom_list)
            msg = "added"
            data["custom_lists"] = lists
        return json.dumps({"success": f"list {msg}", "list": custom_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_custom_list",
                "description": "Create a new custom list or update an existing one (metadata & tags, not line-items).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "custom_list": {
                            "type": "object",
                            "description": "Full or partial custom list object.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["custom_list"],
                    "additionalProperties": False
                }
            }
        }