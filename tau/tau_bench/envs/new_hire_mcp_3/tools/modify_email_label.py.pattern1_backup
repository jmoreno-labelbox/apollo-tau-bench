# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ModifyEmailLabel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        label_id = kwargs.get("label_id")
        labels = data.get("email_labels", [])
        for l in labels:
            if l.get("label_id") == label_id:
                l.update(updates)
                l["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_label_id": label_id, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_email_label",
            "description":"Update an email label.",
            "parameters":{"type":"object","properties":{"label_id":{"type":"string"},"updates":{"type":"object"}},"required":["label_id","updates"]}
        }}
