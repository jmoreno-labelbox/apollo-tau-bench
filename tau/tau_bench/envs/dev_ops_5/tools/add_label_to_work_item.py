# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddLabelToWorkItem(Tool):
    """Adds a label to a work item."""
    @staticmethod
    def invoke(data: Dict[str, Any], label_id, work_item_id) -> str:
        links = data.get("work_item_labels", [])
        new_link = {
            "work_item_id": work_item_id,
            "label_id": label_id,
        }
        links.append(new_link)
        return json.dumps({"status": "success", "message": f"Label '{label_id}' added to work item '{work_item_id}'."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_label_to_work_item",
                "description": "Adds a label to a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "work_item_id": {"type": "string"},
                        "label_id": {"type": "string"}
                    },
                    "required": ["work_item_id", "label_id"],
                },
            },
        }
