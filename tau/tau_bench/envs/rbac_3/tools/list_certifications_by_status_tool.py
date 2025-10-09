from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class ListCertificationsByStatusTool(Tool):
    """ListCertificationsByStatus"""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None, certification_id: str = None) -> str:
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListCertificationsByStatus",
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
