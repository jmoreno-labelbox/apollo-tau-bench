# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

class UpdateCrewMemberStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], crew_member_id: str, new_status: str) -> str:
        for c in list(data.get("crew_members", {}).values()):
            if c.get("crew_member_id") == crew_member_id:
                c["status"] = new_status
                return _j(c)
        return _j({"error":"crew_member_not_found","crew_member_id":crew_member_id})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"update_crew_member_status",
            "description":"Set status on a crew member deterministically.",
            "parameters":{"type":"object","properties":{
                "crew_member_id":{"type":"string"},
                "new_status":{"type":"string"}
            },"required":["crew_member_id","new_status"]}
        }}