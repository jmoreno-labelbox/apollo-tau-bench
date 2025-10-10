# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso


class UpdatePublisherContact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], publisher_id) -> str:
        pid = publisher_id
        row = next((p for p in data.get("publishers", []) if p.get("publisher_id") == pid), None)
        if not row:
            return json.dumps({"error": f"Publisher '{pid}' not found"}, indent=2)
        updates = {k:v for k,v in kwargs.items() if k in {"address","contact_email","gst_number"}}
        row.update(updates)
        row["updated_at"] = _fixed_now_iso()
        return json.dumps({"publisher_id": pid, "updated": updates}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_publisher_contact",
            "description":"Update a publisher’s contact fields.",
            "parameters":{"type":"object","properties":{
                "publisher_id":{"type":"string"},
                "address":{"type":"string"},"contact_email":{"type":"string"},"gst_number":{"type":"string"}
            },"required":["publisher_id"]}
        }}
