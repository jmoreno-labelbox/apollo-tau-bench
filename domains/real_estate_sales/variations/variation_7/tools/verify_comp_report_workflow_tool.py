from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class VerifyCompReportWorkflowTool(Tool):
    """Confirms that the entire comparable analysis workflow was performed accurately."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: int = None) -> str:
        if report_id is None:
            return _err("report_id is required")

        reports = {
            int(r.get("report_id")): r
            for r in data.get("comp_reports", [])
            if r.get("report_id") is not None
        }
        r = reports.get(int(report_id))
        exists = r is not None
        status = r.get("status") if r else None
        document_generated = bool(r and r.get("doc_uri"))

        comps = [
            c
            for c in data.get("comparables", [])
            if int(c.get("report_id", -1)) == int(report_id)
        ]
        comparables_count = len(comps)

        emails = data.get("emails", [])
        emails_sent = sum(
            1
            for e in emails
            if r and int(e.get("client_id", -1)) == int(r.get("client_id", -2))
        )

        audits = [
            a
            for a in data.get("audit_events", [])
            if a.get("entity_type") == "comp_report"
            and str(a.get("entity_id")) == str(report_id)
        ]
        audit_trail_complete = len(audits) >= 1

        compliance_verified = bool(document_generated and audit_trail_complete)
        workflow_complete = bool(
            exists
            and status == "sent_to_client"
            and document_generated
            and comparables_count >= 1
            and emails_sent >= 1
            and audit_trail_complete
        )

        out = {
            "workflow_verification": {
                "report_id": int(report_id),
                "report_exists": bool(exists),
                "status_current": status,
                "document_generated": bool(document_generated),
                "comparables_count": int(comparables_count),
                "emails_sent": int(emails_sent),
                "audit_trail_complete": bool(audit_trail_complete),
                "compliance_verified": bool(compliance_verified),
                "workflow_complete": bool(workflow_complete),
            }
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verifyCompReportWorkflow",
                "description": "Verify comparable analysis workflow end state.",
                "parameters": {
                    "type": "object",
                    "properties": {"report_id": {"type": "integer"}},
                    "required": ["report_id"],
                },
            },
        }
