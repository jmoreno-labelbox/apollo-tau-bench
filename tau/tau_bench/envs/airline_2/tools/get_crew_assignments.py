# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

class GetCrewAssignments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], crew_member_id: Optional[str]=None, flight_number: Optional[str]=None) -> str:
        out=[]
        for a in list(data.get("flight_crew_assignments", {}).values()):
            if crew_member_id and (a.get("crew_member") or {}).get("crew_member_id") != crew_member_id:
                continue
            if flight_number and (a.get("flight") or {}).get("flight_number") != flight_number:
                continue
            out.append(a)
        return _j(out)

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_crew_assignments",
            "description":"List flight crew assignments filtered by crew_member_id and/or flight_number.",
            "parameters":{"type":"object","properties":{
                "crew_member_id":{"type":"string"},
                "flight_number":{"type":"string"},
            }}
        }}