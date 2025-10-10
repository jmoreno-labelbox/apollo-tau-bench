# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RevokeCertificationTool(Tool):
    """Revoke an existing certification from a user (write operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], certification_id, expires_on) -> str:
        certifications = data.get("certifications", [])
        if not isinstance(certifications, list):
            return json.dumps({"error": "certifications must be a list"}, indent=2)

        if not isinstance(certification_id, str) or not certification_id.strip():
            return json.dumps({"error": "certification_id must be a non-empty string"}, indent=2)
        if expires_on is not None and not isinstance(expires_on, str):
            return json.dumps({"error": "expires_on must be a string if provided"}, indent=2)

        cert = next((c for c in certifications if c.get("certification_id") == certification_id), None)
        if not cert:
            return json.dumps({"error": f"Certification {certification_id} not found"}, indent=2)

        cert["status"] = "REVOKED"
        # Remove completion if it exists.
        if "completed_on" in cert:
            cert["completed_on"] = None
        # Optionally add an end marker utilizing a field name that is present in other datasets.
        if expires_on:
            cert["expires_on"] = expires_on

        return json.dumps({"success": f"Certification {certification_id} revoked"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revoke_certification",
                "description": "Revoke a certification by certification_id; clears completed_on and can set expires_on.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"},
                        "expires_on": {"type": "string", "description": "Optional deterministic end timestamp"}
                    },
                    "required": ["certification_id"]
                },
            },
        }
