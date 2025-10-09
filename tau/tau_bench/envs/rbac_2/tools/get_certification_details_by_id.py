from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCertificationDetailsById(Tool):
    """Obtain the complete details of a specific access certification campaign by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None,
    user_id: Any = None,
    ) -> str:
        try:
            certifications = data.get("certifications", [])
        except:
            certifications = []

        for cert in certifications:
            if cert.get("certification_id") == certification_id:
                payload = cert
                out = json.dumps(payload)
                return out
        payload = {"error": f"Certification with ID '{certification_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCertificationDetailsById",
                "description": "Retrieves the full details of a specific access certification campaign using its unique ID (e.g., 'C-005').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "The unique ID of the certification campaign to retrieve.",
                        }
                    },
                    "required": ["certification_id"],
                },
            },
        }
