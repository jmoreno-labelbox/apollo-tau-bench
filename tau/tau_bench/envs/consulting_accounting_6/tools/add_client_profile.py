# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddClientProfile(Tool):
    """Create a new client/publisher row."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tbl = data.get("publishers", [])
        row = {
            "publisher_id": kwargs.get("publisher_id"),
            "name": kwargs.get("name"),
            "address": kwargs.get("address"),
            "contact_email": kwargs.get("contact_email"),
            "gst_number": kwargs.get("gst_number"),
            "created_at": _now_iso(),
            "updated_at": _now_iso()
        }
        tbl.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "add_client_profile",
            "description": "Create a client/publisher row.",
            "parameters": {"type": "object", "properties": {
                "publisher_id": {"type": "string"},
                "name": {"type": "string"},
                "address": {"type": "string"},
                "contact_email": {"type": "string"},
                "gst_number": {"type": "string"}
            }, "required": ["publisher_id", "name"]}
        }}
