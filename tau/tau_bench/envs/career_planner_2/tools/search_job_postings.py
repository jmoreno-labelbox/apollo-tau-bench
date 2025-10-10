# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchJobPostings(Tool):
    """Return job postings matching keywords and location."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        kws = kwargs.get("skill_keywords", [])
        loc = kwargs.get("location")
        res = [
            p
            for p in data.get("job_postings", [])
            if (not loc or loc.lower() in p.get("location", ""))
            and all(kw.lower() in json.dumps(p).lower() for kw in kws)
        ]
        return json.dumps(res, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_job_postings",
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
