# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ModifyChecklistItem(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        item_id = kwargs.get("item_id")
        items = list(data.get("checklist_items", {}).values())
        for i in items:
            if i.get("item_id") == item_id:
                i.update(updates)
                i["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_item_id": item_id, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_checklist_item",
            "description":"Update a checklist task.",
            "parameters":{"type":"object","properties":{"item_id":{"type":"string"},"updates":{"type":"object"}},"required":["item_id","updates"]}
        }}
