# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CompleteCertificationTool(Tool):
    """Mark a certification as complete."""

    @staticmethod
    def invoke(data: Dict[str, Any], certification_id, completed_on) -> str:
        cid = certification_id
        for c in data.get("certifications", []):
            if c["certification_id"] == cid:
                c["status"] = "COMPLETED"
                c["completed_on"] = completed_on
                return json.dumps({"success": f"Certification {cid} completed"}, indent=2)
        return json.dumps({"error": f"Certification {cid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "complete_certification",
                "description": "Mark a certification as completed",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"},
                        "completed_on": {"type": "string"},
                    },
                    "required": ["certification_id", "completed_on"]
                }
            }
        }
