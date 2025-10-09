from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class CompleteCertificationTool(Tool):
    """CompleteCertification"""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str, reviewer_id: str = None, completed_on: Any = None) -> str:
        cert_id = certification_id
        reviewer_id = reviewer_id

        certs = data.get("certifications", [])
        c = None
        for x in certs:
            if x.get("certification_id") == cert_id:
                c = x
                break
        c["status"] = "COMPLETED"
        c["completed_on"] = _HARD_TS
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
                "name": "CompleteCertification",
                "description": (
                    "Mark a certification as COMPLETED with completed_on timestamp."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"},
                        "completed_on": {"type": "string"},
                        "reviewer_id": {
                            "type": "string",
                            "description": (
                                "Optional reviewer ID to reassign certification (e.g., U-005)"
                            ),
                        },
                    },
                    "required": ["certification_id", "completed_on"],
                },
            },
        }
