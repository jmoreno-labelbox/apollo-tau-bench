# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _next_numeric_suffix






def _next_numeric_suffix(prefix: str, items: List[Dict[str, Any]], key: str) -> str:
    mx = 0
    for it in items:
        s = it.get(key)
        if not isinstance(s, str) or not s.startswith(prefix):
            continue
        try:
            num = int(s[len(prefix):])
            mx = max(mx, num)
        except Exception:
            pass
    return f"{prefix}{mx+1:03d}"

def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

class CreateCrewAssignment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], flight_number: str, crew_member_id: str, assigned_role: str) -> str:
        assigns = data.setdefault("flight_crew_assignments", [])
        new_id = _next_numeric_suffix("AS", assigns, "assignment_id")
        rec = {
            "assignment_id": new_id,
            "flight": {"flight_number": flight_number},
            "crew_member": {"crew_member_id": crew_member_id},
            "assigned_role": assigned_role
        }
        assigns.append(rec)
        return _j(rec)

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"create_crew_assignment",
            "description":"Create a flight crew assignment with deterministic ID (AS###).",
            "parameters":{"type":"object","properties":{
                "flight_number":{"type":"string"},
                "crew_member_id":{"type":"string"},
                "assigned_role":{"type":"string"}
            },"required":["flight_number","crew_member_id","assigned_role"]}
        }}