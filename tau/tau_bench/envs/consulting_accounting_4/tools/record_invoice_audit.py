from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RecordInvoiceAudit(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        invoice_id: str = None,
        invoice_number: str = None,
        event_type: str = None,
        notes: str = None
    ) -> str:
        audits = data.get("invoice_audit", [])
        prefix = "AUD"
        max_num = 0
        for audit in audits:
            audit_id_str = str(audit.get("audit_id", ""))
            if audit_id_str.startswith(prefix):
                numeric_part = audit_id_str[len(prefix) :]
                try:
                    num = int(numeric_part)
                    if num > max_num:
                        max_num = num
                except ValueError:
                    continue

        new_number = max_num + 1
        new_id = f"{prefix}{new_number:03d}"

        row = {
            "audit_id": new_id,
            "invoice_id": invoice_id,
            "invoice_number": invoice_number,
            "event_type": event_type,
            "event_timestamp": _fixed_now_iso(),
            "notes": notes,
        }
        audits.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordInvoiceAudit",
                "description": "Append an InvoiceAudit event (generated, emailed, etc.).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                        "event_type": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["event_type"],
                },
            },
        }
