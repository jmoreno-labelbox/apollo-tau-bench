# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveCandidate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        candidates = list(data.get("candidates", {}).values())
        data["candidates"] = [c for c in candidates if c.get("candidate_id") != candidate_id]
        return json.dumps({"removed_candidate_id": candidate_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"remove_candidate",
                "description":"Remove a candidate by ID.",
                "parameters":{"type":"object","properties":{"candidate_id":{"type":"string"}},"required":["candidate_id"]}
            }
        }
