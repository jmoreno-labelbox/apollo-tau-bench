# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCertificationsByStatusTool(Tool):
    """list_certifications_by_status"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        certification_id = kwargs.get("certification_id")

        out = [
            c
            for c in data.get("certifications", [])
            if (status is None or c.get("status") == status)
            and (
                certification_id is None
                or c.get("certification_id") == certification_id
            )
        ]
        out = sorted(out, key=lambda c: (c.get("certification_id") or ""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_certifications_by_status",
                "description": (
                    "Filter certifications by optional status and/or certification_id."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "enum": ["PENDING", "IN_PROGRESS", "COMPLETED"],
                        },
                        "certification_id": {
                            "type": "string",
                            "description": (
                                "Optional certification identifier to further filter results."
                            ),
                        },
                    },
                    "required": [],
                },
            },
        }
