# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ConnectRevisedVersion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        revised_article_id = kwargs.get('revised_article_id')

        if not all([submission_id, revised_article_id]):
            return json.dumps({"error": "submission_id and revised_article_id are required."})

        submissions = list(data.get('submissions', {}).values())
        for sub in submissions:
            if sub.get('submission_id') == submission_id:
                sub['revised_version_article_id'] = revised_article_id
                return json.dumps({"success": True, "submission": sub})
        return json.dumps({"error": f"Submission with ID '{submission_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "connect_revised_version", "description": "Connects a revised version of an article to an original submission record.", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string", "description": "The ID of the original submission."}, "revised_article_id": {"type": "string", "description": "The article ID of the new, revised version."}}, "required": ["submission_id", "revised_article_id"]}}}
