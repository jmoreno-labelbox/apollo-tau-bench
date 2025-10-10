# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class StartCertificationTool(Tool):
    """start_certification"""

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
        c["status"] = "IN_PROGRESS"
        c["completed_on"] = None
        if reviewer_id:
            c["reviewer_id"] = reviewer_id
        return json.dumps(c, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "start_certification",
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
