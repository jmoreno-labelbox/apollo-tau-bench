# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CompleteCertificationTool(Tool):
    """complete_certification"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cert_id = kwargs["certification_id"]
        reviewer_id = kwargs.get("reviewer_id")

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
        return json.dumps(c, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "complete_certification",
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
