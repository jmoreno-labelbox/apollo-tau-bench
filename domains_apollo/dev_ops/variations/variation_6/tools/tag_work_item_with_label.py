from tau_bench.envs.tool import Tool
import json
from typing import Any

class TagWorkItemWithLabel(Tool):
    """Assign a label to a work item; generate label by name if necessary (deterministic ids)."""

    @staticmethod
    def invoke(data: dict[str, Any], work_item_id: str = None, label_id: str = None, label_name: str = None) -> str:
        labels = _table(data, "labels")
        wils = _table(data, "work_item_labels")
        if not label_id:
            if not label_name:
                return _err("either label_id or label_name must be provided")
            found = next((l for l in labels if l.get("name") == label_name), None)
            if found:
                label_id = found.get("id")
            else:
                label_id = f"label_{len(labels) + 1:03d}"
                labels.append(
                    {
                        "id": label_id,
                        "project_id": "project_001",
                        "name": label_name,
                        "color": "#000000",
                    }
                )
        for m in wils:
            if m.get("work_item_id") == work_item_id and m.get("label_id") == label_id:
                return _ok(
                    {
                        "message": "label already attached",
                        "work_item_id": work_item_id,
                        "label_id": label_id,
                    }
                )
        wils.append({"work_item_id": work_item_id, "label_id": label_id})
        return _ok({"tagged": {"work_item_id": work_item_id, "label_id": label_id}})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "tagWorkItemWithLabel",
                "description": "Attach a label to a work item (idempotent).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "work_item_id": {"type": "string"},
                        "label_id": {"type": "string"},
                        "label_name": {"type": "string"},
                    },
                    "required": ["work_item_id"],
                },
            },
        }
