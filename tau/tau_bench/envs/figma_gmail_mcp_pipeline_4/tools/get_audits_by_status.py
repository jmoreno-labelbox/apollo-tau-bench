from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAuditsByStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str = None,
        status: str = None,
        audit_type: str = None,
        artifact_id: str = None,
        created_after: str = None,
        created_before: str = None
    ) -> str:
        """
        Obtains audits filtered by status, type, and additional criteria.
        """
        audits = data.get("audits", {}).values()

        # Return the specific audit if audit_id is supplied
        if audit_id:
            for audit in audits.values():
                if audit.get("audit_id") == audit_id:
                    payload = audit
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Audit with ID '{audit_id}' not found."}
            out = json.dumps(payload)
            return out

        # Sort audits based on specified criteria
        results = []
        for audit in audits.values():
            # Implement filters
            if status:
                if audit.get("status") != status:
                    continue

            if audit_type:
                if audit.get("audit_type") != audit_type:
                    continue

            if artifact_id:
                if audit.get("artifact_id") != artifact_id:
                    continue

            # Enforce date filters
            if created_after:
                audit_created = audit.get("created_ts", "")
                if audit_created < created_after:
                    continue

            if created_before:
                audit_created = audit.get("created_ts", "")
                if audit_created > created_before:
                    continue

            results.append(audit)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuditsByStatus",
                "description": "Retrieves audits filtered by status, type, artifact association, and date ranges for comprehensive audit management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of a specific audit to retrieve.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter audits by status (e.g., 'RUNNING', 'COMPLETED', 'FAILED').",
                        },
                        "audit_type": {
                            "type": "string",
                            "description": "Filter audits by type (e.g., 'COMBINED_DS_A11Y', 'A11Y', 'DS').",
                        },
                        "artifact_id": {
                            "type": "string",
                            "description": "Filter audits by associated artifact ID.",
                        },
                        "created_after": {
                            "type": "string",
                            "description": "Filter audits created after this ISO timestamp.",
                        },
                        "created_before": {
                            "type": "string",
                            "description": "Filter audits created before this ISO timestamp.",
                        },
                    },
                },
            },
        }
