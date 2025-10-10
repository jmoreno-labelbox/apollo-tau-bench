# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindAvailableCrew(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], role: str, home_base_iata: Optional[str]=None, status: Optional[str]=None) -> str:
        crew = data.get("crew_members", [])
        out=[]
        for m in crew:
            if m.get("role") != role:
                continue
            if home_base_iata and ((m.get("home_base") or {}).get("iata_code") != home_base_iata):
                continue
            if status and m.get("status") != status:
                continue
            out.append(m)
        return _j(out)

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"find_available_crew",
            "description":"Find crew members by role, optionally filtering by home base IATA and status.",
            "parameters":{"type":"object","properties":{
                "role":{"type":"string"},
                "home_base_iata":{"type":"string"},
                "status":{"type":"string"}
            },"required":["role"]}
        }}
