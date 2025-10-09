from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateCertificationStatus(Tool):
    """Modify the status of an access certification campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None, new_status: str = None, timestamp: str = None) -> str:
        certification_id_to_update = certification_id
        new_status = new_status
        timestamp = timestamp
        try:
            certifications = data.get("certifications", {}).values()
        except:
            certifications = []

        certification_found = False
        updated_certification = None
        for cert in certifications:
            if cert.get("certification_id") == certification_id_to_update:
                cert["status"] = new_status
                if new_status == "COMPLETED":
                    cert["completed_on"] = timestamp

                certification_found = True
                updated_certification = cert
                break

        if not certification_found:
            payload = {
                "error": f"Certification with ID '{certification_id_to_update}' not found."
            }
            out = json.dumps(payload)
            return out

        data["certifications"] = certifications
        payload = {
            "message": "Certification campaign status updated successfully.",
            "certification_details": updated_certification,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCertificationStatus",
                "description": "Updates the status of an access certification campaign (e.g., to 'COMPLETED').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "The unique ID of the certification campaign to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status to set for the campaign (e.g., 'COMPLETED').",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp to record as the completion time.",
                        },
                    },
                    "required": ["certification_id", "new_status", "timestamp"],
                },
            },
        }
