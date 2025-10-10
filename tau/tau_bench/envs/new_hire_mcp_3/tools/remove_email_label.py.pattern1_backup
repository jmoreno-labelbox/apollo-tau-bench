# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveEmailLabel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        label_id = kwargs.get("label_id")
        labels = data.get("email_labels", [])
        data["email_labels"] = [l for l in labels if l.get("label_id") != label_id]
        return json.dumps({"removed_label_id": label_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"remove_email_label",
            "description":"Remove an email label by ID.",
            "parameters":{"type":"object","properties":{"label_id":{"type":"string"}},"required":["label_id"]}
        }}
