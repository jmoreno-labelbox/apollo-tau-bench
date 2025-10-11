# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class QuerySubmissions(Tool):
    """Tool to query submissions by article or status."""
    @staticmethod
    def invoke(data: Dict[str, Any], article_id, status, submission_id) -> str:
        submissions = list(data.get('submissions', {}).values())
        results = []
        for sub in submissions:
            match = True
            if submission_id and submission_id != sub.get('submission_id'): match = False
            if article_id and article_id != sub.get('article_id'): match = False
            if status and status != sub.get('status'): match = False
            if match:
                results.append(sub)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "query_submissions", "description": "Queries article submissions by submission ID, article ID or status.", "parameters": {"type": "object", "properties": {
            "submission_id": {"type": "string", "description": "The unique ID of the submission."},
            "article_id": {"type": "string", "description": "The associated article's ID."},
            "status": {"type": "string", "description": "The current status of the submission (e.g., 'pending', 'under review')."}
        }, "required": []}}}
