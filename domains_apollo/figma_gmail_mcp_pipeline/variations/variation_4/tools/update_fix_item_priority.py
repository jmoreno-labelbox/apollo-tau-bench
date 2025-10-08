from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateFixItemPriority(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_id: str = None, new_priority: str = None, updated_by: str = None, priority_reason: str = None) -> str:
        """
        Modifies the priority of a fix item.
        """
        if not all([item_id, new_priority, updated_by]):
            payload = {"error": "item_id, new_priority, and updated_by are required"}
            out = json.dumps(payload)
            return out

        # Check the correctness of priority values
        valid_priorities = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
        if new_priority not in valid_priorities:
            payload = {
                "error": f"Invalid priority. Must be one of: {', '.join(valid_priorities)}"
            }
            out = json.dumps(payload)
            return out

        # Locate and modify the fix item
        for item in data.get("fix_items", []):
            if item.get("item_id") == item_id:
                item["priority"] = new_priority
                item["last_updated"] = datetime.now().isoformat()
                item["updated_by"] = updated_by
                payload = {
                    "status": "success",
                    "item_id": item_id,
                    "new_priority": new_priority,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Fix item with ID {item_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFixItemPriority",
                "description": "Updates the priority of a fix item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "string",
                            "description": "The ID of the fix item to update.",
                        },
                        "new_priority": {
                            "type": "string",
                            "description": "The new priority level.",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Email of the user updating the priority.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about the priority change.",
                        },
                    },
                    "required": ["item_id", "new_priority", "updated_by"],
                },
            },
        }
