# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindMentor(Tool):
    """Find an available mentor by expertise."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        expertise = kwargs.get("expertise")
        mentors = data.get("user_mentorship", [])
        # Deterministic selection: first mentor in the list that matches all expertise areas and has capacity.
        for m in sorted(mentors, key=lambda x: x["mentor_id"]):  # Sort for determinism
            if m.get("availability") != "Full" and all(
                e.lower() in [exp.lower() for exp in m.get("expertise", [])]
                for e in expertise
            ):
                return json.dumps({"mentor_id": m.get("mentor_id")})
        return json.dumps({"error": "No suitable mentor found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_mentor",
                "description": "Find an available mentor by expertise.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expertise": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["expertise"],
                },
            },
        }
