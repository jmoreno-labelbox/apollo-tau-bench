# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class IdentifyPotentialReviewers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        exclude_user_ids = kwargs.get('exclude_user_ids', [])

        if not article_id:
            return json.dumps({"error": "article_id is required."})

        articles = list(data.get('articles', {}).values())
        target_article = next((a for a in articles if a.get('article_id') == article_id), None)
        if not target_article:
            return json.dumps({"error": f"Article with ID '{article_id}' not found."})

        article_topic = target_article.get('topic')
        if not article_topic:
            return json.dumps({"error": f"Article with ID '{article_id}' has no topic specified."})

        users = list(data.get('users', {}).values())
        potential_reviewers = [
            user for user in users
            if user.get('research_field') == article_topic and user.get('user_id') not in exclude_user_ids
        ]

        return json.dumps(potential_reviewers, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "identify_potential_reviewers", "description": "Identifies potential reviewers for an article based on matching research fields.", "parameters": {"type": "object", "properties": {"article_id": {"type": "string", "description": "The ID of the article needing reviewers."}, "exclude_user_ids": {"type": "array", "items": {"type": "string"}, "description": "A list of user IDs to exclude from the suggestions (e.g., the authors)."}},"required": ["article_id"]}}}
