# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMortgageProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], client_id) -> str:
        profiles = data.get("mortgage_profiles") or data.get("mortage_profiles") or []  
        prof = next((m for m in profiles if m.get("client_id") == client_id), None)
        if not prof:
            return json.dumps({"error": f"No mortgage profile for client_id={client_id}"}, indent=2)
        return json.dumps(prof, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_mortgage_profile",
            "description":"Fetch the mortgage profile for a client.",
            "parameters":{"type":"object","properties":{"client_id":{"type":"integer"}},"required":["client_id"]}
        }}
