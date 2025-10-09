from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCertification(Tool):
    """
    Retrieve certifications based on ID, reviewer, resource, or status.

    kwargs:
      certification_id: str (optional) - Specific certification ID to retrieve
      reviewer_id: str (optional) - Filter by the reviewer user ID
      resource_id: str (optional) - Filter by resource ID
      status: str (optional) - Filter by status (PENDING, IN_PROGRESS, COMPLETED)
    """

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None, reviewer_id: str = None, resource_id: str = None, status: str = None,
    user_id: Any = None,
    ) -> str:
        certifications = data.get("certifications", {}).values()

        # If certification_id is supplied, return the specific certification
        if certification_id:
            cert = _find_by_id(certifications, "certification_id", certification_id)
            if not cert:
                payload = {"error": f"certification_id {certification_id} not found"}
                out = json.dumps(payload)
                return out
            payload = {"ok": True, "certification": cert}
            out = json.dumps(payload)
            return out

        # Narrow down certifications according to the supplied criteria
        filtered_certifications = []
        for cert in certifications:
            if reviewer_id and cert.get("reviewer_id") != reviewer_id:
                continue
            if resource_id and cert.get("resource_id") != resource_id:
                continue
            if status and cert.get("status") != status:
                continue
            filtered_data["certifications"][certification_id] = cert
        payload = {"ok": True, "certifications": filtered_certifications}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCertification",
                "description": "Retrieve certifications by ID, reviewer, resource, or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "Specific certification ID to retrieve.",
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "Filter by reviewer user ID.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Filter by resource ID.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by status (PENDING, IN_PROGRESS, COMPLETED).",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
