from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddLabelToWorkItem(Tool):
    """Inserts a label into a work item."""

    @staticmethod
    def invoke(data: dict[str, Any], work_item_id: str = None, label_id: str = None) -> str:
        links = data.get("work_item_labels", {}).values()
        new_link = {
            "work_item_id": work_item_id,
            "label_id": label_id,
        }
        data["work_item_labels"][new_link["work_item_label_id"]] = new_link
        payload = {
                "status": "success",
                "message": f"Label '{label_id}' added to work item '{work_item_id}'.",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddLabelToWorkItem",
                "description": "Adds a label to a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "work_item_id": {"type": "string"},
                        "label_id": {"type": "string"},
                    },
                    "required": ["work_item_id", "label_id"],
                },
            },
        }
