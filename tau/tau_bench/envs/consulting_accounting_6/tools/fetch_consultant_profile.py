# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchConsultantProfile(Tool):
    """Return the consultant profile row by consultant_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("consultant_id")
        row = next((c for c in data.get("consultants", []) if c.get("consultant_id") == cid), None)
        if not row:
            return json.dumps({"error": f"consultant_id '{cid}' not found"}, indent=2)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "fetch_consultant_profile",
            "description": "Fetch a consultant profile.",
            "parameters": {"type": "object", "properties": {"consultant_id": {"type": "string"}}, "required": ["consultant_id"]}
        }}
