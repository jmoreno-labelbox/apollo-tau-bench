from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class QuerySubmissions(Tool):
    """Utility for querying submissions based on article or status."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: str = None, article_id: str = None, status: str = None) -> str:
        submissions = data.get("submissions", [])
        results = []
        for sub in submissions:
            match = True
            if submission_id and submission_id != sub.get("submission_id"):
                match = False
            if article_id and article_id != sub.get("article_id"):
                match = False
            if status and status != sub.get("status"):
                match = False
            if match:
                results.append(sub)
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "QuerySubmissions",
                "description": "Queries article submissions by submission ID, article ID or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The unique ID of the submission.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The associated article's ID.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the submission (e.g., 'pending', 'under review').",
                        },
                    },
                    "required": [],
                },
            },
        }
