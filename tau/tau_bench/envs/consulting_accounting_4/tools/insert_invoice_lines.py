# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertInvoiceLines(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], invoice_id, invoice_number, lines) -> str:
        invoice_lines = data.get("invoice_lines", [])
        invs = data.get("invoices", [])
        if invoice_id is None and invoice_number:
            inv = next((i for i in invs if i.get("invoice_number")==invoice_number), None)
            if inv:
                invoice_id = inv.get("invoice_id")
        if invoice_id is None:
            return json.dumps({"error":"invoice_id or invoice_number required"}, indent=2)
        lines = lines or []
        new_ids = []
        
        max_line_id = 0
        for line in invoice_lines:
            try:
                line_id_val = int(line.get("invoice_line_id", 0))
                if line_id_val > max_line_id:
                    max_line_id = line_id_val
            except (ValueError, TypeError):
                continue
        
        for ln in lines:
            max_line_id += 1
            lid = max_line_id
            invoice_lines.append({
                "invoice_line_id": lid,
                "invoice_id": invoice_id,
                "project_id": ln.get("project_id"),
                "isbn": ln.get("isbn"),
                "hours_billed": ln.get("hours"),
                "hourly_rate": ln.get("rate"),
                "line_amount": round(float(ln.get("hours",0))*float(ln.get("rate",0)), 2)
            })
            new_ids.append(lid)
        return json.dumps({"invoice_id": invoice_id, "inserted_line_ids": new_ids}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"insert_invoice_lines",
            "description":"Insert invoice lines for an invoice.",
            "parameters":{"type":"object","properties":{
                "invoice_id":{"type":"string"},
                "invoice_number":{"type":"string"},
                "lines":{"type":"array","items":{"type":"object"}}
            },"required":["lines"]}
        }}
