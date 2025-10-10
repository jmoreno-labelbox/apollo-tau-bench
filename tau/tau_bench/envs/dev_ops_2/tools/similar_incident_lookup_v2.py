# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SimilarIncidentLookupV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], signature: str, top_k: int = 5) -> str:
        crashes = _get_table(data, "crash_events")
        neighbors = [c for c in crashes if c.get("crash_fingerprint") == signature or c.get("fingerprint") == signature][:top_k]
        return json.dumps({"neighbors": neighbors}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "similar_incident_lookup_v2", "description": "Returns incidents matching the exact signature/fingerprint (deterministic).", "parameters": {"type": "object", "properties": {"signature": {"type": "string"}, "top_k": {"type": "integer"}}, "required": ["signature"]}}}
