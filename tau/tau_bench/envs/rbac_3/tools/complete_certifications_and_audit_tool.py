# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CompleteCertificationsAndAuditTool(Tool):
    """
    complete_certifications_and_audit
    Complete all IN_PROGRESS certifications and write a single audit log.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        log_id = kwargs.get("log_id") or "LOG-CERT-CLOSE"
        actor_id = kwargs.get("actor_id")
        target_id = kwargs.get("target_id") or "CERT:ALL"
        details = kwargs.get("details") or "Certifications completed."
        if not actor_id:
            return json.dumps({"error": "actor_id is required"}, indent=2)

        completed: List[str] = []
        for cert in data.get("certifications", []):
            if cert.get("status") == "IN_PROGRESS":
                cert["status"] = "COMPLETED"
                cert["completed_on"] = _HARD_TS
                completed.append(cert.get("certification_id"))

        audit = json.loads(
            AppendAuditLogTool.invoke(
                data,
                log_id=log_id,
                access_request=log_id,
                actor_id=actor_id,
                action_type="certification_close",
                target_id=target_id,
                timestamp=_HARD_TS,
                details=details,
            )
        )

        return json.dumps(
            {
                "completed_ids": completed,
                "audit_log_id": audit.get("log_id"),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "complete_certifications_and_audit",
                "description": (
                    "Complete all IN_PROGRESS certifications and write a single audit log."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_id": {"type": "string"},
                        "actor_id": {"type": "string"},
                        "target_id": {"type": "string"},
                        "details": {"type": "string"},
                    },
                    "required": ["actor_id"],
                },
            },
        }
