# Sierra copyright notice

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckDriveTimeConstraints(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        stops = kwargs.get("property_ids") or []
        max_minutes = kwargs.get("max_minutes", 30)
        hops = [{"from": stops[i], "to": stops[i+1], "minutes": 20} for i in range(max(0, len(stops)-1))]
        ok = all(h["minutes"] <= max_minutes for h in hops)
        return json.dumps({"ok": ok, "hops": hops, "max_minutes": max_minutes}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"check_drive_time_constraints",
            "description":"Compute if sequential hops fit within max drive minutes.",
            "parameters":{"type":"object","properties":{
                "property_ids":{"type":"array","items":{"type":"string"}},
                "max_minutes":{"type":"integer"}
            },"required":["property_ids","max_minutes"]}
        }}
