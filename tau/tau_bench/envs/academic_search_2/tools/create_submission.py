# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateSubmission(Tool):
    """Creates a new article submission."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id, author_user_id = kwargs.get('article_id'), kwargs.get('author_user_id')
        submission_id_override = kwargs.get('submission_id_override')
        if not all([article_id, author_user_id]):
            return json.dumps({"error": "article_id and author_user_id are required."})
        new_submission = {
            "submission_id": submission_id_override if submission_id_override else f"sub_{uuid.uuid4().hex[:4]}",
            "article_id": article_id,
            "author_user_id": author_user_id,
            "submission_date": "2025-06-24",
            "status": "submitted",
            "assigned_reviewers": []
        }
        list(data.get('submissions', {}).values()).append(new_submission)
        return json.dumps({"success": True, "submission": new_submission}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_submission", "description": "Creates a new article submission.", "parameters": {"type": "object", "properties": {"article_id": {"type": "string"}, "author_user_id": {"type": "string"}, "submission_id_override": {"type": "string"}}, "required": ["article_id", "author_user_id"]}}}
