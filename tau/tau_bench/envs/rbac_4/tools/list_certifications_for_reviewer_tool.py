# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCertificationsForReviewerTool(Tool):
    """List all certifications assigned to a given reviewer (read operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        reviewer_id = kwargs.get("reviewer_id")
        certifications = data.get("certifications", [])
        if not isinstance(certifications, list):
            return json.dumps({"error": "certifications must be a list"}, indent=2)

        if not isinstance(reviewer_id, str) or not reviewer_id.strip():
            return json.dumps({"error": "reviewer_id must be a non-empty string"}, indent=2)

        results = [c for c in certifications if c.get("reviewer_id") == reviewer_id]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_certifications_for_reviewer",
                "description": "List all certifications assigned to a specific reviewer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reviewer_id": {"type": "string", "description": "The reviewer’s user_id"}
                    },
                    "required": ["reviewer_id"]
                }
            }
        }
