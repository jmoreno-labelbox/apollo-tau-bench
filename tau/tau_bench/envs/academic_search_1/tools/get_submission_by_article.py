# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSubmissionByArticle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], article_id) -> str:
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        submissions = list(data.get('submissions', {}).values())
        for submission in submissions:
            if submission.get('article_id') == article_id:
                return json.dumps(submission, indent=2)

        return json.dumps({"error": f"No submission found for article_id '{article_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_submission_by_article",
                "description": "Retrieves a submission's details using the ID of the article that was submitted.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string", "description": "The unique ID of the article to find the submission for."}
                    },
                    "required": ["article_id"]
                }
            }
        }
