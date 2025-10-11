# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

class GetAircraftByAirport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], airport_id: str) -> str:
        res = []
        for a in list(data.get("aircraft", {}).values()):
            if a.get('location').get("airport_id") == airport_id:
                res.append(_j(a))
        return _j(res)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_aircraft_by_airport",
            "description":"Return aircraft by their base airport.",
            "parameters":{"type":"object","properties":{"airport_id":{"type":"string"}},"required":["airport_id"]}
        }}