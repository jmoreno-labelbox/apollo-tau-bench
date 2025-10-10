# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddEmailLabel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        new_label = kwargs.get("label") or {}
        labels = list(data.get("email_labels", {}).values())
        labels.append(new_label)
        data["email_labels"] = labels
        return json.dumps({"added_label": new_label}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_email_label",
            "description":"Add a new email label.",
            "parameters":{"type":"object","properties":{"label":{"type":"object"}},"required":["label"]}
        }}
