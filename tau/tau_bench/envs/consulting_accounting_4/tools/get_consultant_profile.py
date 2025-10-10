# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetConsultantProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], consultant_id) -> str:
        cid = consultant_id
        row = next((c for c in data.get("consultants", []) if c.get("consultant_id") == cid), None)
        if not row:
            return json.dumps({"error": f"Consultant '{cid}' not found"}, indent=2)
        return json.dumps(row, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_consultant_profile",
            "description":"Fetch the consultant profile row.",
            "parameters":{"type":"object","properties":{"consultant_id":{"type":"string"}},"required":["consultant_id"]}
        }}
