# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAuditsByStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves audits filtered by status, type, and other criteria.
        """
        audit_id = kwargs.get('audit_id')
        status = kwargs.get('status')
        audit_type = kwargs.get('audit_type')
        artifact_id = kwargs.get('artifact_id')
        created_after = kwargs.get('created_after')
        created_before = kwargs.get('created_before')

        audits = data.get('audits', [])

        # If audit_id is provided, return specific audit
        if audit_id:
            for audit in audits:
                if audit.get('audit_id') == audit_id:
                    return json.dumps(audit, indent=2)
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found."})

        # Filter audits by criteria
        results = []
        for audit in audits:
            # Apply filters
            if status:
                if audit.get('status') != status:
                    continue

            if audit_type:
                if audit.get('audit_type') != audit_type:
                    continue

            if artifact_id:
                if audit.get('artifact_id') != artifact_id:
                    continue

            # Apply date filters
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
