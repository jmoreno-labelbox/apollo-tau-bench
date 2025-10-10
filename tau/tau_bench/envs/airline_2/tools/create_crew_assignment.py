# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
