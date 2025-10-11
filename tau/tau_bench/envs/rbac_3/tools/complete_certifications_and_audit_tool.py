# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




class AppendAuditLogTool(Tool):
    """append_audit_log"""

    @staticmethod
    def invoke(data: Dict[str, Any], log_id, access_request, actor_id, action_type, target_id, details = "") -> str:
        # Generate log_id if not provided
        if "log_id" not in kwargs or log_id is None:
            log_id = f"LOG-{access_request}-decision"
        else:
            pass

        entry = {
            "log_id": log_id,
            "actor_id": actor_id,
            "action_type": action_type,
            "target_id": target_id,
            "timestamp": _HARD_TS,
            "details": details,
        }
        logs = data.setdefault("audit_logs", [])
        existing = next((l for l in logs if l.get("log_id") == entry["log_id"]), None)
        if existing is None:
            logs.append(entry)
            out = entry
        else:
            out = existing
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_audit_log",
                "description": "Append an audit log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_id": {"type": "string"},
                        "access_request": {"type": "string"},
                        "actor_id": {"type": "string"},
                        "action_type": {"type": "string"},
                        "target_id": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "details": {"type": "string"},
                    },
                    "required": [
                        "access_request",
                        "actor_id",
                        "action_type",
                        "target_id",
                        "timestamp",
                    ],
                },
            },
        }

class CompleteCertificationsAndAuditTool(Tool):
    """
    complete_certifications_and_audit
    Complete all IN_PROGRESS certifications and write a single audit log.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], actor_id, details, log_id, target_id) -> str:
        log_id = log_id or "LOG-CERT-CLOSE"
        target_id = target_id or "CERT:ALL"
        details = details or "Certifications completed."
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