# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetConsultantProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], consultant_id) -> str:
        cid = consultant_id
        cons = next((c for c in list(data.get("consultants", {}).values()) if c.get("consultant_id") == cid), None)
        return json.dumps(cons or {"error": f"Consultant {cid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "get_consultant_profile","description": "Retrieve consultant master data.","parameters": {"type": "object","properties": {"consultant_id": {"type": "string"}},"required": ["consultant_id"]}}}
