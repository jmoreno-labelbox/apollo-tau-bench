from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class ConnectRevisedVersion(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, revised_article_id: Any = None) -> str:
        if not all([submission_id, revised_article_id]):
            payload = {"error": "submission_id and revised_article_id are required."}
            out = json.dumps(payload)
            return out

        submissions = data.get("submissions", [])
        for sub in submissions:
            if sub.get("submission_id") == submission_id:
                sub["revised_version_article_id"] = revised_article_id
                payload = {"success": True, "submission": sub}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Submission with ID '{submission_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConnectRevisedVersion",
                "description": "Connects a revised version of an article to an original submission record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the original submission.",
                        },
                        "revised_article_id": {
                            "type": "string",
                            "description": "The article ID of the new, revised version.",
                        },
                    },
                    "required": ["submission_id", "revised_article_id"],
                },
            },
        }
