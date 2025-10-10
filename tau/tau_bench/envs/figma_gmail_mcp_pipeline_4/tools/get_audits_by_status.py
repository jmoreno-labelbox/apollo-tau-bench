# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAuditsByStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], artifact_id, audit_id, audit_type, created_after, created_before, status) -> str:
        """
        Retrieves audits filtered by status, type, and other criteria.
        """

        audits = data.get('audits', [])

        # Return the specific audit if an audit_id is given.
        if audit_id:
            for audit in audits:
                if audit.get('audit_id') == audit_id:
                    return json.dumps(audit, indent=2)
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found."})

        # Apply criteria to filter audits.
        results = []
        for audit in audits:
            # Implement filters
            if status:
                if audit.get('status') != status:
                    continue

            if audit_type:
                if audit.get('audit_type') != audit_type:
                    continue

            if artifact_id:
                if audit.get('artifact_id') != artifact_id:
                    continue

            # Implement date constraints.
            if created_after:
                audit_created = audit.get('created_ts', '')
                if audit_created < created_after:
                    continue

            if created_before:
                audit_created = audit.get('created_ts', '')
                if audit_created > created_before:
                    continue

            results.append(audit)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_audits_by_status",
                "description": "Retrieves audits filtered by status, type, artifact association, and date ranges for comprehensive audit management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of a specific audit to retrieve."},
                        "status": {"type": "string", "description": "Filter audits by status (e.g., 'RUNNING', 'COMPLETED', 'FAILED')."},
                        "audit_type": {"type": "string", "description": "Filter audits by type (e.g., 'COMBINED_DS_A11Y', 'A11Y', 'DS')."},
                        "artifact_id": {"type": "string", "description": "Filter audits by associated artifact ID."},
                        "created_after": {"type": "string", "description": "Filter audits created after this ISO timestamp."},
                        "created_before": {"type": "string", "description": "Filter audits created before this ISO timestamp."}
                    }
                }
            }
        }
