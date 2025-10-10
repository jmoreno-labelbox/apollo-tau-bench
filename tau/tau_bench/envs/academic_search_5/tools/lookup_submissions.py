# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LookupSubmissions(Tool):
    """
    Tool to search for submissions based on various criteria OR retrieve a single one by ID.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        article_id = kwargs.get('article_id')
        author_user_id = kwargs.get('author_user_id')
        status = kwargs.get('status')

        submissions = list(data.get('submissions', {}).values())

        if submission_id:
            for sub in submissions:
                if sub.get('submission_id') == submission_id:
                    return json.dumps(sub, indent=2)
            return json.dumps({"error": f"Submission with ID '{submission_id}' not found."})

        if article_id:
            for sub in submissions:
                if sub.get('article_id') == article_id:
                    return json.dumps(sub, indent=2)
            return json.dumps({"error": f"No submission found for article ID '{article_id}'."})

        if not any([author_user_id, status]):
            return json.dumps(submissions, indent=2)

        results = []
        for sub in submissions:
            author_match = not author_user_id or author_user_id == sub.get('author_user_id')
            status_match = not status or status.lower() == sub.get('status', '').lower()

            if author_match and status_match:
                results.append(sub)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "lookup_submissions",
                "description": "Searches for submissions by various criteria, or retrieves a single submission by its specific ID or associated article ID. Returns all submissions if no criteria are given.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string", "description": "The specific ID of the submission to retrieve."},
                        "article_id": {"type": "string", "description": "The ID of the article to find the submission for."},
                        "author_user_id": {"type": "string", "description": "The user ID of the submission's author."},
                        "status": {"type": "string", "description": "The current status of the submission (e.g., 'under_review')."}
                    }
                }
            }
        }
