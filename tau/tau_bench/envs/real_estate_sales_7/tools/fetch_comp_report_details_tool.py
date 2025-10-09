from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FetchCompReportDetailsTool(Tool):
    """Fetches a comp report that includes related comparables, documents, email summaries, and audit trails."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: int = None) -> str:
        if report_id is None:
            return _err("report_id is required")

        report = next(
            (
                r
                for r in data.get("comp_reports", {}).values()
                if _as_int(r.get("report_id")) == report_id
            ),
            None,
        )
        if not report:
            return _err(f"report_id {report_id} not found", code="not_found")

        comps = [
            c
            for c in data.get("comparables", {}).values()
            if _as_int(c.get("report_id")) == report_id
        ]
        docs = [
            d
            for d in data.get("documents", {}).values()
            if d.get("entity_type") == "comp_report"
            and str(d.get("entity_id")) == str(report_id)
        ]

        #emails associated with the report's client (summary only)
        client_id = _as_int(report.get("client_id"))
        emails = [
            e
            for e in data.get("emails", {}).values()
            if _as_int(e.get("client_id")) == client_id
        ]
        emails_sorted = sorted(
            emails, key=lambda e: e.get("sent_at") or "", reverse=True
        )

        #audit trail records for this report
        audits = [
            a
            for a in data.get("audit_events", {}).values()
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchCompReportDetails",
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
