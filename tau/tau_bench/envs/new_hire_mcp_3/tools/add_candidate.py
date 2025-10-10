# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddCandidate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], candidate) -> str:
        new_candidate = candidate or {}
        candidates = list(data.get("candidates", {}).values())
        candidates.append(new_candidate)
        data["candidates"] = candidates
        return json.dumps({"added_candidate": new_candidate}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"add_candidate",
                "description":"Add a new candidate.",
                "parameters":{"type":"object","properties":{"candidate":{"type":"object"}},"required":["candidate"]}
            }
        }
