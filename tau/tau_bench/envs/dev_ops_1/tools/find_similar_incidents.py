# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindSimilarIncidents(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], signature: str, top_k: int = 5) -> str:
        crashes = _get_table(data, "crash_events")
        neighbors = [c for c in crashes if c.get("fingerprint") == signature][:top_k]
        return json.dumps({"neighbors": neighbors}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_similar_incidents", "description": "Returns prior crash/incidents with identical deterministic fingerprint (simulated semantic match).", "parameters": {"type": "object", "properties": {"signature": {"type": "string"}, "top_k": {"type": "integer"}}, "required": ["signature"]}}}
