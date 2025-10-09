from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCertificationTool(Tool):
    """Provide a single certification record using certification_id (read operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None) -> str:
        certifications = data.get("certifications", [])
        if not isinstance(certifications, list):
            payload = {"error": "certifications must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(certification_id, str) or not certification_id.strip():
            payload = {"error": "certification_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        for c in certifications:
            if c.get("certification_id") == certification_id:
                payload = c
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Certification {certification_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCertification",
                "description": "Retrieve a certification by certification_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"certification_id": {"type": "string"}},
                    "required": ["certification_id"],
                },
            },
        }
