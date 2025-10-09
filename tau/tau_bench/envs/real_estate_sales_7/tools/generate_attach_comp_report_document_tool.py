from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class GenerateAttachCompReportDocumentTool(Tool):
    """Create comp_###.pdf URI from report_id, refresh comp_reports.doc_uri, and add a documents row."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: int = None, created_by: int = None, doc_type: str = "comp_report") -> str:
        pass
        report_id = _as_int(report_id)
        created_by = _as_int(created_by)
        doc_type = doc_type.strip()
        if report_id is None or created_by is None:
            return _err("report_id and created_by are required")

        reports = data.setdefault("comp_reports", [])
        r = next((x for x in reports if _as_int(x.get("report_id")) == report_id), None)
        if not r:
            return _err(f"report_id {report_id} not found", code="not_found")

        padded = str(report_id).zfill(3)
        uri = f"https://storage.example.com/reports/comp_{padded}.pdf"

        r["doc_uri"] = uri
        r["updated_at"] = HARD_TS

        docs = data.setdefault("documents", [])
        document_id = _next_int_id(docs, "document_id")
        doc_row = {
            "document_id": document_id,
            "entity_type": "comp_report",
            "entity_id": str(report_id),
            "doc_type": doc_type,
            "file_uri": uri,
            "created_by": created_by,
            "created_at": HARD_TS,
        }
        data["documents"][doc_row["document_id"]] = doc_row

        #--- Generate Audit Event Entry ---
        audit_rows = data.setdefault("audit_events", [])
        audit_event_id = _next_int_id(audit_rows, "event_id")
        audit_rec = {
            "event_id": audit_event_id,
            "actor_id": int(created_by),
            "action": "updated_uri",
            "entity_type": "comp_report",
            "entity_id": str(report_id),
            "occurred_at": HARD_TS,
            "metadata_json": {"new_uri": uri},
        }
        data["audit_events"][audit_rec["audit_event_id"]] = audit_rec
        payload = {
                "document_uri": uri,
                "report": {
                    "report_id": report_id,
                    "doc_uri": uri,
                    "updated_at": HARD_TS,
                },
                "document_entry": doc_row,
                "audit_event": audit_rec,
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
                "name": "GenerateAttachCompReportDocument",
                "description": (
                    "Generate PDF URI from report_id, update comp_reports.doc_uri, and insert a documents row."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
                        "created_by": {"type": "integer"},
                        "doc_type": {"type": "string", "default": "comp_report"},
                    },
                    "required": ["report_id", "created_by"],
                },
            },
        }
