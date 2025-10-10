# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateAttachCompReportDocumentTool(Tool):
    """Generate comp_###.pdf URI from report_id, update comp_reports.doc_uri, and insert documents row."""

    @staticmethod
    def invoke(data: Dict[str, Any], created_by, doc_type, report_id) -> str:
        report_id = _as_int(report_id)
        created_by = _as_int(created_by)
        doc_type = (doc_type or "comp_report").strip()
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
        docs.append(doc_row)

        # --- Generate Audit Event Record ---
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
        audit_rows.append(audit_rec)

        return json.dumps(
            {
                "document_uri": uri,
                "report": {
                    "report_id": report_id,
                    "doc_uri": uri,
                    "updated_at": HARD_TS,
                },
                "document_entry": doc_row,
                "audit_event": audit_rec,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_attach_comp_report_document",
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
