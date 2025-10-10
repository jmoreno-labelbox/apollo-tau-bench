# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LabelEmailByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        message_id = kwargs.get("message_id")
        label_name = kwargs.get("label_name")
        el = CreateOrGetEmailLabel.invoke
        label_info = json.loads(el(data, name=label_name))
        lid = label_info.get("label_id")
        ae = AddLabelsToEmail.invoke
        res = json.loads(ae(data, message_id=message_id, label_ids=[lid]))
        return json.dumps({"message_id": message_id, "label_id": lid, "labels_ids": res.get("labels_ids", [])},
                          indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "label_email_by_name",
                                                 "description": "Ensure a label by name exists and apply it to an email.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"message_id": {"type": "string"},
                                                                               "label_name": {"type": "string"}},
                                                                "required": ["message_id", "label_name"]}}}
