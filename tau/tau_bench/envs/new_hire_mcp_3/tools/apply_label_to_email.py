from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ApplyLabelToEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], email_id: str = None, label_id: str = None) -> str:
        email_labels = data.get("email_labels", [])

        # Search for the email in the list and assign the tag
        for e in email_labels:
            if e.get("email_id") == email_id:
                applied_labels = e.setdefault("labels", [])
                if label_id not in applied_labels:
                    applied_labels.append(label_id)
                break
        else:
            # If the email is not located, you may create a new record
            email_labels.append({"email_id": email_id, "labels": [label_id]})
            data["email_labels"] = email_labels
        payload = {"email_id": email_id, "applied_label_id": label_id, "status": "Success"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyLabelToEmail",
                "description": "Applies a label to an email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email_id": {"type": "string"},
                        "label_id": {"type": "string"},
                    },
                    "required": ["email_id", "label_id"],
                },
            },
        }
