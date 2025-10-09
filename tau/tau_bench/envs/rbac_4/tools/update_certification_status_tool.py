from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateCertificationStatusTool(Tool):
    """Revise the status of a certification review (write operation)."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None, status: str = None, completed_on: str = None) -> str:
        certs = data.get("certifications", [])

        if not isinstance(certification_id, str):
            payload = {"error": "certification_id must be provided"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(status, str):
            payload = {"error": "status must be provided"}
            out = json.dumps(payload, indent=2)
            return out

        for c in certs:
            if c.get("certification_id") == certification_id:
                c["status"] = status
                if completed_on:
                    c["completed_on"] = completed_on
                payload = {"success": f"Certification {certification_id} updated", "certification": c}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": f"Certification {certification_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCertificationStatus",
                "description": "Update the status of a certification review.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "Unique ID of the certification",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status (e.g., PENDING, IN_PROGRESS, COMPLETED)",
                        },
                        "completed_on": {
                            "type": "string",
                            "description": "Optional ISO8601 timestamp when completed",
                        },
                    },
                    "required": ["certification_id", "status"],
                },
            },
        }
