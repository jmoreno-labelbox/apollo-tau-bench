# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_similar_incidents(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], issue_signature: str) -> str:
        incidents = data.get("incident_history", [])
        hits = [i for i in incidents if i.get("issue_signature") == issue_signature]
        return json.dumps({"count": len(hits), "results": hits}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "find_similar_incidents", "description": "Finds past incidents with a similar issue signature.", "parameters": { "type": "object", "properties": { "issue_signature": { "type": "string" } }, "required": ["issue_signature"] } } }
