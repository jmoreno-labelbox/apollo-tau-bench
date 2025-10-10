# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CompleteCertification(Tool):
    """
    Complete a certification by setting status to COMPLETED and completed_on to deterministic timestamp.

    kwargs:
      certification_id: str (required)
      reviewer_id: str (required)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        certification_id = kwargs.get("certification_id", "")
        reviewer_id = kwargs.get("reviewer_id", "")

        certs = data.get("certifications", [])
        cert = _find_by_id(certs, "certification_id", certification_id)
        if not cert:
            return json.dumps({"error": f"certification_id {certification_id} not found"})

        if cert.get("reviewer_id") != reviewer_id:
            return json.dumps({"error": f"reviewer_id {reviewer_id} does not match certification reviewer"})

        if cert.get("status") not in ("PENDING", "IN_PROGRESS"):
            # The idempotent completion provides the current value.
            if cert.get("status") == "COMPLETED":
                return json.dumps({"ok": True, "certification": cert})
            return json.dumps({"error": f"certification {certification_id} not completable from status {cert.get('status')}"})

        updated = dict(cert)
        updated.update({
            "status": "COMPLETED",
            "completed_on": get_current_timestamp(),
        })

        for i, c in enumerate(certs):
            if c.get("certification_id") == certification_id:
                data["certifications"][i] = updated
                break

        return json.dumps({"ok": True, "certification": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "complete_certification",
                "description": "Complete a certification with deterministic completion timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string", "description": "Certification id (C-###)."},
                        "reviewer_id": {"type": "string", "description": "Reviewer user_id."}
                    },
                    "required": ["certification_id", "reviewer_id"],
                    "additionalProperties": False
                }
            }
        }
