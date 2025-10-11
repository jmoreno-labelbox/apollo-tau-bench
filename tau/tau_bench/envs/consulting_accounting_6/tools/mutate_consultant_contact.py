# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _now_iso() -> str:
    return "2025-08-20T00:00:00Z"

class MutateConsultantContact(Tool):
    """Update consultant contact fields."""
    @staticmethod
    def invoke(data: Dict[str, Any], consultant_id) -> str:
        cid = consultant_id
        updates = {k: v for k, v in kwargs.items() if k in {"address", "phone", "email", "gst_number"}}
        row = next((c for c in data.get("consultants", []) if c.get("consultant_id") == cid), None)
        if not row:
            return json.dumps({"error": f"consultant_id '{cid}' not found"}, indent=2)
        row.update(updates)
        row["updated_at"] = _now_iso()
        return json.dumps({"consultant_id": cid, "updated": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "mutate_consultant_contact",
            "description": "Update contact fields for a consultant.",
            "parameters": {"type": "object", "properties": {
                "consultant_id": {"type": "string"},
                "address": {"type": "string"},
                "phone": {"type": "string"},
                "email": {"type": "string"},
                "gst_number": {"type": "string"}
            }, "required": ["consultant_id"]}
        }}