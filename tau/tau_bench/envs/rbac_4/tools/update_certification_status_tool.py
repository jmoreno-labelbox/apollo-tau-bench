# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCertificationStatusTool(Tool):
    """Update the status of a certification review (write operation)."""

    @staticmethod
    def invoke(data: Dict[str, Any], certification_id, completed_on, status) -> str:
        certs = data.get("certifications", [])
        cert_id = certification_id
        new_status = status

        if not isinstance(cert_id, str):
            return json.dumps({"error": "certification_id must be provided"}, indent=2)
        if not isinstance(new_status, str):
            return json.dumps({"error": "status must be provided"}, indent=2)

        for c in certs:
            if c.get("certification_id") == cert_id:
                c["status"] = new_status
                if completed_on:
                    c["completed_on"] = completed_on
                return json.dumps({"success": f"Certification {cert_id} updated", "certification": c}, indent=2)

        return json.dumps({"error": f"Certification {cert_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_certification_status",
                "description": "Update the status of a certification review.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string", "description": "Unique ID of the certification"},
                        "status": {"type": "string", "description": "New status (e.g., PENDING, IN_PROGRESS, COMPLETED)"},
                        "completed_on": {"type": "string", "description": "Optional ISO8601 timestamp when completed"}
                    },
                    "required": ["certification_id", "status"]
                }
            }
        }
