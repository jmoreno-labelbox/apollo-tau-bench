from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListCertificationsForReviewerTool(Tool):
    """Display all certifications allocated to a specific reviewer (read operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], reviewer_id: str = None) -> str:
        certifications = data.get("certifications", {}).values()
        if not isinstance(certifications, list):
            payload = {"error": "certifications must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(reviewer_id, str) or not reviewer_id.strip():
            payload = {"error": "reviewer_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        results = [c for c in certifications.values() if c.get("reviewer_id") == reviewer_id]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListCertificationsForReviewer",
                "description": "List all certifications assigned to a specific reviewer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reviewer_id": {
                            "type": "string",
                            "description": "The reviewer’s user_id",
                        }
                    },
                    "required": ["reviewer_id"],
                },
            },
        }
