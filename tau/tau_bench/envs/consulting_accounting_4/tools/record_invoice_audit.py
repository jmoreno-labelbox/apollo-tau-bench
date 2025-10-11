# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso




def _fixed_now_iso() -> str:
    return "2025-08-20T00:00:00Z"

class RecordInvoiceAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], event_type, invoice_id, invoice_number, notes) -> str:
        audits = data.get("invoice_audit", [])
        prefix = "AUD"
        max_num = 0
        for audit in audits:
            audit_id_str = str(audit.get("audit_id", ""))
            if audit_id_str.startswith(prefix):
                numeric_part = audit_id_str[len(prefix):]
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
            "notes": notes
        }
        audits.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"record_invoice_audit",
            "description":"Append an InvoiceAudit event (generated, emailed, etc.).",
            "parameters":{"type":"object","properties":{
                "invoice_id":{"type":"string"},"invoice_number":{"type":"string"},
                "event_type":{"type":"string"},"notes":{"type":"string"}
            },"required":["event_type"]}
        }}