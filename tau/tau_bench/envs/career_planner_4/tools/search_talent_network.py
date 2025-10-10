# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class search_talent_network(Tool):
    @staticmethod
    def invoke(data, candidate_id: str) -> str:
        for candidate in data.get("talent_network", []):
            if candidate.get("candidate_id") == candidate_id:
                return json.dumps(candidate, indent=2)
        return json.dumps({"error": "Candidate not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "search_talent_network",
                "description": "Search for an external candidate by candidate_id in the talent network.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }
