from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any

class CompleteCertification(Tool):
    """
    Finalize a certification by changing the status to COMPLETED and setting completed_on to a consistent timestamp.

    kwargs:
      certification_id: str (mandatory)
      reviewer_id: str (mandatory)
    """

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = "", reviewer_id: str = "") -> str:
        certs = data.get("certifications", [])
        cert = _find_by_id(certs, "certification_id", certification_id)
        if not cert:
            payload = {"error": f"certification_id {certification_id} not found"}
            out = json.dumps(payload)
            return out

        if cert.get("reviewer_id") != reviewer_id:
            payload = {
                "error": f"reviewer_id {reviewer_id} does not match certification reviewer"
            }
            out = json.dumps(payload)
            return out

        if cert.get("status") not in ("PENDING", "IN_PROGRESS"):
            # Idempotent completion yields the current state
            if cert.get("status") == "COMPLETED":
                payload = {"ok": True, "certification": cert}
                out = json.dumps(payload)
                return out
            payload = {
                "error": f"certification {certification_id} not completable from status {cert.get('status')}"
            }
            out = json.dumps(payload)
            return out

        updated = dict(cert)
        updated.update(
            {
                "status": "COMPLETED",
                "completed_on": get_current_timestamp(),
            }
        )

        for i, c in enumerate(certs):
            if c.get("certification_id") == certification_id:
                data["certifications"][i] = updated
                break
        payload = {"ok": True, "certification": updated}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CompleteCertification",
                "description": "Complete a certification with deterministic completion timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "Certification id (C-###).",
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "Reviewer user_id.",
                        },
                    },
                    "required": ["certification_id", "reviewer_id"],
                    "additionalProperties": False,
                },
            },
        }
