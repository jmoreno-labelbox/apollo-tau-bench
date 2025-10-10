from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class FindMentor(Tool):
    """Identify an available mentor based on expertise."""

    @staticmethod
    def invoke(data: dict[str, Any], expertise: list[str] = None) -> str:
        mentors = data.get("user_mentorship", {}).values()
        # Deterministic selection: the initial mentor from the list who satisfies all expertise requirements and is accessible.
        for m in sorted(mentors, key=lambda x: x["mentor_id"]):  # Sort to guarantee consistent results.
            if m.get("availability") != "Full" and all(
                e.lower() in [exp.lower() for exp in m.get("expertise", [])]
                for e in expertise
            ):
                payload = {"mentor_id": m.get("mentor_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": "No suitable mentor found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindMentor",
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
