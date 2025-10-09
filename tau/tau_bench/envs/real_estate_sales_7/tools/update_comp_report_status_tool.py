from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateCompReportStatusTool(Tool):
    """Modifies the status field in the comp_reports table."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: int = None, new_status: str = None, actor_id: int = None) -> str:
        if report_id is None or not new_status or actor_id is None:
            return _err("report_id, new_status, and actor_id are required")

        rows = data.get("comp_reports", [])
        rec = next(
            (r for r in rows if int(r.get("report_id", -1)) == int(report_id)), None
        )
        if not rec:
            return _err(f"report_id {report_id} not found")

        prev = rec.get("status")
        rec["status"] = new_status
        rec["updated_at"] = HARD_TS

        #--- Generate Audit Event Entry ---
        audit_rows = data.setdefault("audit_events", [])
        audit_event_id = _next_int_id(audit_rows, "event_id")
        audit_rec = {
            "event_id": audit_event_id,
            "actor_id": int(actor_id),
            "action": "updated_status",
            "entity_type": "comp_report",
            "entity_id": str(report_id),
            "occurred_at": HARD_TS,
            "metadata_json": {"new_status": new_status, "previous_status": prev},
        }
        audit_rows.append(audit_rec)
        payload = {
                "report_id": int(report_id),
                "previous_status": prev,
                "new_status": new_status,
                "updated_at": HARD_TS,
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
                "name": "UpdateCompReportStatus",
                "description": "Updates status field in comp_reports table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
                        "new_status": {
                            "type": "string",
                            "enum": ["draft", "sent_to_broker", "sent_to_client"],
                        },
                        "actor_id": {"type": "integer"},
                    },
                    "required": ["report_id", "new_status", "actor_id"],
                },
            },
        }
