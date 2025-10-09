from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class StartCertificationTool(Tool):
    """StartCertification"""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str, reviewer_id: str = None) -> str:
        cert_id = certification_id
        reviewer_id = reviewer_id
        certs = data.get("certifications", [])
        c = None
        for x in certs:
            if x.get("certification_id") == cert_id:
                c = x
                break
        c["status"] = "IN_PROGRESS"
        c["completed_on"] = None
        if reviewer_id:
            c["reviewer_id"] = reviewer_id
        payload = c
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StartCertification",
                "description": "Set a certification status to IN_PROGRESS.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"},
                        "reviewer_id": {
                            "type": "string",
                            "description": (
                                "Optional reviewer ID to reassign certification (e.g., U-005)"
                            ),
                        },
                    },
                    "required": ["certification_id"],
                },
            },
        }
