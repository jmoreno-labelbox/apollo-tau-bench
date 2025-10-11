# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

class GetAircraftByTail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], tail_number: str) -> str:
        for a in list(data.get("aircraft", {}).values()):
            if a.get("tail_number") == tail_number:
                return _j(a)
        return _j({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_aircraft_by_tail",
            "description":"Return an aircraft row by tail number.",
            "parameters":{"type":"object","properties":{"tail_number":{"type":"string"}},"required":["tail_number"]}
        }}