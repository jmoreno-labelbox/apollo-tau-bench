from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpsertCustomList(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], custom_list: dict[str, Any]) -> str:
        if not custom_list:
            payload = {"error": "custom_list object required"}
            out = json.dumps(payload, indent=2)
            return out
        lists = _load("custom_lists", data)
        idx, _ = _find(lists, custom_list["list_id"])
        if idx is not None:
            lists[idx].update(custom_list)
            msg = "updated"
        else:
            lists.append(custom_list)
            msg = "added"
            data["custom_lists"] = lists
        payload = {"success": f"list {msg}", "list": custom_list}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertCustomList",
                "description": "Create a new custom list or update an existing one (metadata & tags, not line-items).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "custom_list": {
                            "type": "object",
                            "description": "Full or partial custom list object.",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["custom_list"],
                    "additionalProperties": False,
                },
            },
        }
