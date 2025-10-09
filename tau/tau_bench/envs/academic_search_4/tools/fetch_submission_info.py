from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FetchSubmissionInfo(Tool):
    """Utility to retrieve submission information for an article or based on submission ID."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, submission_id: Any = None) -> str:
        if not article_id and not submission_id:
            payload = {"error": "Either article_id or submission_id is required."}
            out = json.dumps(payload)
            return out

        submissions = data.get("submissions", {}).values()
        for sub in submissions.values():
            if (article_id and sub.get("article_id") == article_id) or (
                submission_id and sub.get("submission_id") == submission_id
            ):
                payload = sub
                out = json.dumps(payload, indent=2)
                return out

        if article_id:
            payload = {"error": f"No submission found for article ID '{article_id}'."}
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": f"No submission found for submission ID '{submission_id}'."}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchSubmissionInfo",
                "description": "Gets the submission details for a given article ID or submission ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to find the submission for.",
                        },
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to find.",
                        },
                    },
                },
            },
        }
