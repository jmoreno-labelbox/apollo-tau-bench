# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddChecklistItem(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], item) -> str:
        new_item = item or {}
        items = list(data.get("checklist_items", {}).values())
        items.append(new_item)
        data["checklist_items"] = items
        return json.dumps({"added_item": new_item}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_checklist_item",
            "description":"Add a new checklist item.",
            "parameters":{"type":"object","properties":{"item":{"type":"object"}},"required":["item"]}
        }}
