from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CompleteCertificationsAndAuditTool(Tool):
    """
    complete_certifications_and_audit
    Finalize all IN_PROGRESS certifications and create a single audit log.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        log_id: str = "LOG-CERT-CLOSE", 
        actor_id: str = None, 
        target_id: str = "CERT:ALL", 
        details: str = "Certifications completed."
    ) -> str:
        if not actor_id:
            payload = {"error": "actor_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        completed: list[str] = []
        for cert in data.get("certifications", {}).values():
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
        payload = {
                "completed_ids": completed,
                "audit_log_id": audit.get("log_id"),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "completeCertificationsAndAudit",
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
