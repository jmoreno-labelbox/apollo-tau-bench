from tau_bench.envs.tool import Tool
import json
from typing import Any

class LabelEmailByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message_id: str = None, label_name: str = None) -> str:
        el = CreateOrGetEmailLabel.invoke
        label_info = json.loads(el(data, name=label_name))
        lid = label_info.get("label_id")
        ae = AddLabelsToEmail.invoke
        res = json.loads(ae(data, message_id=message_id, label_ids=[lid]))
        payload = {
                "message_id": message_id,
                "label_id": lid,
                "labels_ids": res.get("labels_ids", []),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "labelEmailByName",
                "description": "Ensure a label by name exists and apply it to an email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "label_name": {"type": "string"},
                    },
                    "required": ["message_id", "label_name"],
                },
            },
        }
