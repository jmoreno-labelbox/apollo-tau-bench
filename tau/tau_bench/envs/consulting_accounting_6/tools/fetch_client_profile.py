# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchClientProfile(Tool):
    """Read a client/publisher row by publisher_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pid = kwargs.get("publisher_id")
        row = next((p for p in data.get("publishers", []) if p.get("publisher_id") == pid), None)
        if not row:
            return json.dumps({"error": f"publisher_id '{pid}' not found"}, indent=2)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "fetch_client_profile",
            "description": "Fetch a client/publisher record.",
            "parameters": {"type": "object", "properties": {"publisher_id": {"type": "string"}}, "required": ["publisher_id"]}
        }}
