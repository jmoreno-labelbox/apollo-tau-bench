# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetClientPreferences(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get("client_id")
        if client_id is None:
            return json.dumps({"error": "client_id is required"}, indent=2)
        prefs = next((p for p in data.get("client_preferences", []) if p.get("client_id") == client_id), None)
        if not prefs:
            return json.dumps({"error": f"No preferences found for client_id={client_id}"}, indent=2)
        return json.dumps(prefs, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_client_preferences",
            "description":"Get preferences for a specific client.",
            "parameters":{"type":"object","properties":{"client_id":{"type":"integer"}},"required":["client_id"]}
        }}
