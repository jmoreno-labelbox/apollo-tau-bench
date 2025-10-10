# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveChecklistItem(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_id = kwargs.get("item_id")
        items = list(data.get("checklist_items", {}).values())
        data["checklist_items"] = [i for i in items if i.get("item_id") != item_id]
        return json.dumps({"removed_item_id": item_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"remove_checklist_item",
            "description":"Remove a checklist item by ID.",
            "parameters":{"type":"object","properties":{"item_id":{"type":"string"}},"required":["item_id"]}
        }}
