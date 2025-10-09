from tau_bench.envs.tool import Tool
import json
from typing import Any

class CompleteCertificationTool(Tool):
    """Designate a certification as complete."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None, completed_on: str = None) -> str:
        for c in data.get("certifications", []):
            if c["certification_id"] == certification_id:
                c["status"] = "COMPLETED"
                c["completed_on"] = completed_on
                payload = {"success": f"Certification {certification_id} completed"}
                out = json.dumps(
                    payload, indent=2
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
                "name": "CompleteCertification",
                "description": "Mark a certification as completed",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"},
                        "completed_on": {"type": "string"},
                    },
                    "required": ["certification_id", "completed_on"],
                },
            },
        }
