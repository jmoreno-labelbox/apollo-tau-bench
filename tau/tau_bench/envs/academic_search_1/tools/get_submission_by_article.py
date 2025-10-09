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

class GetSubmissionByArticle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        submissions = data.get("submissions", {}).values()
        for submission in submissions.values():
            if submission.get("paper_id") == article_id:
                payload = submission
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No submission found for article_id '{article_id}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSubmissionByArticle",
                "description": "Retrieves a submission's details using the ID of the article that was submitted.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The unique ID of the article to find the submission for.",
                        }
                    },
                    "required": ["article_id"],
                },
            },
        }
