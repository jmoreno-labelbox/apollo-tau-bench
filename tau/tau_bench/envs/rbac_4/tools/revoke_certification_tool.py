from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RevokeCertificationTool(Tool):
    """Remove an existing certification from a user (write operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str, expires_on: str = None) -> str:
        certifications = data.get("certifications", {}).values()
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
        if expires_on is not None and not isinstance(expires_on, str):
            payload = {"error": "expires_on must be a string if provided"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        cert = next(
            (
                c
                for c in certifications.values() if c.get("certification_id") == certification_id
            ),
            None,
        )
        if not cert:
            payload = {"error": f"Certification {certification_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        cert["status"] = "REVOKED"
        #Reset completion if available
        if "completed_on" in cert:
            cert["completed_on"] = None
        #Optionally mark an end using a pre-existing field name utilized in other datasets
        if expires_on:
            cert["expires_on"] = expires_on
        payload = {"success": f"Certification {certification_id} revoked"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokeCertification",
                "description": "Revoke a certification by certification_id; clears completed_on and can set expires_on.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"},
                        "expires_on": {
                            "type": "string",
                            "description": "Optional deterministic end timestamp",
                        },
                    },
                    "required": ["certification_id"],
                },
            },
        }
