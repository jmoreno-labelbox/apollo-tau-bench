# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCrewCertifications(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], crew_member_id: str, certification_code: Optional[str]=None) -> str:
        out = []
        for c in data.get("crew_certifications", []):
            cmid = (c.get("crew_member") or {}).get("crew_member_id")
            if cmid != crew_member_id:
                continue
            if certification_code:
                code = (c.get("certification") or {}).get("certification_code")
                if code != certification_code:
                    continue
            out.append(c)
        return _j(out)

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_crew_certifications",
            "description":"List certifications for a crew member; optionally filter by certification_code.",
            "parameters":{"type":"object","properties":{
                "crew_member_id":{"type":"string"},
                "certification_code":{"type":"string"}
            },"required":["crew_member_id"]}
        }}
