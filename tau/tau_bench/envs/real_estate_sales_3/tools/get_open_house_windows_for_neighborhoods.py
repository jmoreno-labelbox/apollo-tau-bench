# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOpenHouseWindowsForNeighborhoods(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        nids = set(kwargs.get("neighborhood_ids") or [])
        props = [p for p in list(data.get("properties", {}).values()) if p.get("neighborhood_id") in nids]
        prop_ids = {p.get("property_id") for p in props}
        rows = [oh for oh in data.get("open_houses", []) if oh.get("property_id") in prop_ids]
        return json.dumps({"neighborhood_ids": list(nids), "open_houses": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_open_house_windows_for_neighborhoods",
            "description":"Fetch open house windows for neighborhoods.",
            "parameters":{"type":"object","properties":{"neighborhood_ids":{"type":"array","items":{"type":"integer"}}},"required":["neighborhood_ids"]}
        }}
