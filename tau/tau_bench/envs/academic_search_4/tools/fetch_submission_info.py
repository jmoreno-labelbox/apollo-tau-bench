# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchSubmissionInfo(Tool):
    """Tool to get submission details for an article or by submission ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], article_id, submission_id) -> str:

        if not article_id and not submission_id:
            return json.dumps({"error": "Either article_id or submission_id is required."})

        submissions = list(data.get('submissions', {}).values())
        for sub in submissions:
            if (article_id and sub.get('article_id') == article_id) or \
               (submission_id and sub.get('submission_id') == submission_id):
                return json.dumps(sub, indent=2)

        if article_id:
            return json.dumps({"error": f"No submission found for article ID '{article_id}'."})
        else:
            return json.dumps({"error": f"No submission found for submission ID '{submission_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "fetch_submission_info","description": "Gets the submission details for a given article ID or submission ID.","parameters": {"type": "object","properties": {"article_id": {"type": "string", "description": "The ID of the article to find the submission for."}, "submission_id": {"type": "string", "description": "The ID of the submission to find."}}}}}
