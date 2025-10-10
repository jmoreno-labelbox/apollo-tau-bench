# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetAircraftStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], aircraft_id: str, new_status: str) -> str:
        new_status = new_status[:1].upper() + new_status[1:]
        for a in list(data.get("aircraft", {}).values()):
            if a.get("aircraft_id") == aircraft_id:
                a["status"] = new_status
                return _j(a)
        return _j({"error":"aircraft_not_found","aircraft_id":aircraft_id})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"set_aircraft_status",
            "description":"Set status on an aircraft deterministically.",
            "parameters":{"type":"object","properties":{
                "aircraft_id":{"type":"string"},
                "new_status":{"type":"string"}
            },"required":["aircraft_id","new_status"]}
        }}
