# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyLabelToEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], email_id, label_id) -> str:
        email_labels = list(data.get("email_labels", {}).values())

        # Locate the email within the list and assign the label.
        for e in email_labels:
            if e.get("email_id") == email_id:
                applied_labels = e.setdefault("labels", [])
                if label_id not in applied_labels:
                    applied_labels.append(label_id)
                break
        else:
            # If the email is absent, optionally generate a new record.
            email_labels.append({"email_id": email_id, "labels": [label_id]})
            data["email_labels"] = email_labels

        return json.dumps({
            "email_id": email_id,
            "applied_label_id": label_id,
            "status": "Success"
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_label_to_email",
                "description": "Applies a label to an email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email_id": {"type": "string"},
                        "label_id": {"type": "string"}
                    },
                    "required": ["email_id", "label_id"]
                }
            }
        }
