# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SubmitArticleForReview(Tool):
    """Tool to create a new submission for an article."""
    @staticmethod
    def invoke(data: Dict[str, Any], article_id, author_user_id) -> str:
        submissions = list(data.get('submissions', {}).values())
        new_submission = {
            "submission_id": f"sub_{len(submissions) + 1:02d}",
            "article_id": article_id,
            "author_user_id": author_user_id,
            "submission_date": datetime.now().strftime('%Y-%m-%d'),
            "status": "submitted",
            "assigned_reviewers": []
        }
        submissions.append(new_submission)
        return json.dumps(new_submission, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "submit_article_for_review", "description": "Creates a new article submission for the review process.", "parameters": {"type": "object", "properties": {
            "article_id": {"type": "string", "description": "The ID of the article being submitted."},
            "author_user_id": {"type": "string", "description": "The ID of the submitting author."}
        }, "required": ["article_id", "author_user_id"]}}}
