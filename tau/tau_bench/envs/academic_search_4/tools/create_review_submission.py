# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
import uuid
from datetime import datetime


class CreateReviewSubmission(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        author_user_id,article_id = kwargs.get('author_user_id'),kwargs.get('article_id')
        submission_id_override = kwargs.get('submission_id_override')

        if not author_user_id or not article_id:
            return json.dumps({"error": "author_user_id and article_id are required."})
        if not any(u['user_id'] == author_user_id for u in list(data.get('users', {}).values())):
            return json.dumps({"error": f"Author with ID '{author_user_id}' not found."})
        if not any(a['article_id'] == article_id for a in list(data.get('articles', {}).values())):
            return json.dumps({"error": f"Article with ID '{article_id}' not found."})

        new_submission_id = submission_id_override if submission_id_override else f"sub_{uuid.uuid4().hex[:4]}"

        new_submission = {"submission_id": new_submission_id,"article_id": article_id,"author_user_id": author_user_id,"submission_date": datetime.now().strftime('%Y-%m-%d'),"status": "submitted","assigned_reviewers": []}
        data['submissions'].append(new_submission)
        return json.dumps({"success": True, "submission": new_submission})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "create_review_submission","description": "Submits an author's article to the peer review system.","parameters": {"type": "object","properties": {"author_user_id": {"type": "string", "description": "The user ID of the author."}, "article_id": {"type": "string", "description": "The ID of the article being submitted."}, "submission_id_override": {"type": "string", "description": "Optional. A specific ID to assign to the new submission."}},"required": ["author_user_id", "article_id"]}}}
