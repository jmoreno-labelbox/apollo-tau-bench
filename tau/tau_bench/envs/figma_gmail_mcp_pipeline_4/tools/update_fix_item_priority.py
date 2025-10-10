# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateFixItemPriority(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates the priority of a fix item.
        """
        item_id = kwargs.get('item_id')
        new_priority = kwargs.get('new_priority')
        updated_by = kwargs.get('updated_by')

        if not all([item_id, new_priority, updated_by]):
            return json.dumps({"error": "item_id, new_priority, and updated_by are required"})

        # Check the validity of priority values.
        valid_priorities = ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL']
        if new_priority not in valid_priorities:
            return json.dumps({"error": f"Invalid priority. Must be one of: {', '.join(valid_priorities)}"})

        # Locate and modify the correction item.
        for item in data.get('fix_items', []):
            if item.get('item_id') == item_id:
                item['priority'] = new_priority
                item['last_updated'] = datetime.now().isoformat()
                item['updated_by'] = updated_by
                return json.dumps({"status": "success", "item_id": item_id, "new_priority": new_priority})

        return json.dumps({"error": f"Fix item with ID {item_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_fix_item_priority",
                "description": "Updates the priority of a fix item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string", "description": "The ID of the fix item to update."},
                        "new_priority": {"type": "string", "description": "The new priority level."},
                        "updated_by": {"type": "string", "description": "Email of the user updating the priority."},
                        "notes": {"type": "string", "description": "Optional notes about the priority change."}
                    },
                    "required": ["item_id", "new_priority", "updated_by"]
                }
            }
        }
