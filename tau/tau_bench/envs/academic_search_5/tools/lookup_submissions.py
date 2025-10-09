from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class LookupSubmissions(Tool):
    """
    Utility for searching submissions using various criteria or retrieving a specific one by ID.
    """

    @staticmethod
    def invoke(data: dict[str, Any], *, submission_id: Any = None, article_id: Any = None, author_user_id: Any = None, status: Any = None) -> str:
        submissions = data.get("submissions", {}).values()

        if submission_id:
            for sub in submissions.values():
                if sub.get("submission_id") == submission_id:
                    payload = sub
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Submission with ID '{submission_id}' not found."}
            out = json.dumps(payload)
            return out

        if article_id:
            for sub in submissions.values():
                if sub.get("article_id") == article_id:
                    payload = sub
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"No submission found for article ID '{article_id}'."}
            out = json.dumps(payload)
            return out

        if not any([author_user_id, status]):
            payload = submissions
            out = json.dumps(payload, indent=2)
            return out

        results = []
        for sub in submissions.values():
            author_match = not author_user_id or author_user_id == sub.get("author_user_id")
            status_match = not status or status.lower() == sub.get("status", "").lower()

            if author_match and status_match:
                results.append(sub)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LookupSubmissions",
                "description": "Searches for submissions by various criteria, or retrieves a single submission by its specific ID or associated article ID. Returns all submissions if no criteria are given.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The specific ID of the submission to retrieve.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to find the submission for.",
                        },
                        "author_user_id": {
                            "type": "string",
                            "description": "The user ID of the submission's author.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the submission (e.g., 'under_review').",
                        },
                    },
                },
            },
        }
