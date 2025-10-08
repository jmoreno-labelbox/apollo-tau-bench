from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class SearchJobPostings(Tool):
    """Provide job postings that align with specified keywords and location."""

    @staticmethod
    def invoke(data: dict[str, Any], skill_keywords: list[str] = None, location: str = None) -> str:
        if skill_keywords is None:
            skill_keywords = []
        res = [
            p
            for p in data.get("job_postings", [])
            if (not location or location.lower() in p.get("location", ""))
            and all(kw.lower() in json.dumps(p).lower() for kw in skill_keywords)
        ]
        payload = res
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchJobPostings",
                "description": "Search postings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "skill_keywords": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "location": {"type": "string"},
                    },
                    "required": ["skill_keywords"],
                },
            },
        }
