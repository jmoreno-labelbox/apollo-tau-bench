from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RemoveEmailLabel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], label_id: str = None) -> str:
        labels = data.get("email_labels", {}).values()
        data["email_labels"] = [l for l in labels.values() if l.get("label_id") != label_id]
        payload = {"removed_label_id": label_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeEmailLabel",
                "description": "Remove an email label by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"label_id": {"type": "string"}},
                    "required": ["label_id"],
                },
            },
        }
