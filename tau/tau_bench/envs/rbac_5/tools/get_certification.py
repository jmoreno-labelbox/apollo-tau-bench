# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCertification(Tool):
    """
    Retrieve certifications by ID, reviewer, resource, or status.

    kwargs:
      certification_id: str (optional) - Specific certification ID to retrieve
      reviewer_id: str (optional) - Filter by reviewer user ID
      resource_id: str (optional) - Filter by resource ID
      status: str (optional) - Filter by status (PENDING, IN_PROGRESS, COMPLETED)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], certification_id, resource_id, reviewer_id, status) -> str:

        certifications = data.get("certifications", [])

        # Return a single certification if certification_id is given.
        if certification_id:
            cert = _find_by_id(certifications, "certification_id", certification_id)
            if not cert:
                return json.dumps({"error": f"certification_id {certification_id} not found"})
            return json.dumps({"ok": True, "certification": cert})

        # Narrow down certifications according to specified parameters.
        filtered_certifications = []
        for cert in certifications:
            if reviewer_id and cert.get("reviewer_id") != reviewer_id:
                continue
            if resource_id and cert.get("resource_id") != resource_id:
                continue
            if status and cert.get("status") != status:
                continue
            filtered_certifications.append(cert)

        return json.dumps({"ok": True, "certifications": filtered_certifications})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_certification",
                "description": "Retrieve certifications by ID, reviewer, resource, or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string", "description": "Specific certification ID to retrieve."},
                        "reviewer_id": {"type": "string", "description": "Filter by reviewer user ID."},
                        "resource_id": {"type": "string", "description": "Filter by resource ID."},
                        "status": {"type": "string", "description": "Filter by status (PENDING, IN_PROGRESS, COMPLETED)."}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
