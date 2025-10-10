# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _first_user_id


class ListInventoryByHousehold(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        if household_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
        rows = [i for i in data.get("inventory_items", []) if i.get("household_id") == household_id]
        return _json_dump({"household_id": household_id, "inventory_items": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"list_inventory_by_household","description":"Get inventory items for a household; defaults to primary household.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"}},"required":[]}}}
