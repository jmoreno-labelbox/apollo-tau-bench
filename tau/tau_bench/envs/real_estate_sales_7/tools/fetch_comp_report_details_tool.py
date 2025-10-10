# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchCompReportDetailsTool(Tool):
    """Retrieves a comp report with related comparables, documents, emails summary, and audit trail."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = _as_int(kwargs.get("report_id"))
        if report_id is None:
            return _err("report_id is required")

        report = next(
            (
                r
                for r in data.get("comp_reports", [])
                if _as_int(r.get("report_id")) == report_id
            ),
            None,
        )
        if not report:
            return _err(f"report_id {report_id} not found", code="not_found")

        comps = [
            c
            for c in data.get("comparables", [])
            if _as_int(c.get("report_id")) == report_id
        ]
        docs = [
            d
            for d in data.get("documents", [])
            if d.get("entity_type") == "comp_report"
            and str(d.get("entity_id")) == str(report_id)
        ]

        # related emails sent to the report's client (summary only)
        client_id = _as_int(report.get("client_id"))
        emails = [
            e
            for e in data.get("emails", [])
            if _as_int(e.get("client_id")) == client_id
        ]
        emails_sorted = sorted(
            emails, key=lambda e: e.get("sent_at") or "", reverse=True
        )

        # audit trail entries for this report
        audits = [
            a
            for a in data.get("audit_events", [])
            if a.get("entity_type") == "comp_report"
            and str(a.get("entity_id")) == str(report_id)
        ]
        audits_sorted = sorted(
            audits, key=lambda a: a.get("occurred_at") or "", reverse=True
        )

        out = {
            "report": report,
            "comparables": comps,
            "documents": docs,
            "emails_summary": {
                "total": len(emails_sorted),
                "recent": emails_sorted[:5],
            },
            "audit_events": audits_sorted[:10],
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_comp_report_details",
                "description": (
                    "Retrieve a comp report and its related comparables, documents, emails summary, and audit trail."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"report_id": {"type": "integer"}},
                    "required": ["report_id"],
                },
            },
        }
