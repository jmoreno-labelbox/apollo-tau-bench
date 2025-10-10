# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateInvoiceNumber(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        year = kwargs.get("year")
        if not year:
            return json.dumps({"error": "year is required"}, indent=2)
        existing = [i.get("invoice_number") for i in list(data.get("invoices", {}).values()) if str(i.get("invoice_number", "")).startswith(f"{year}-")]
        seqs = []
        for num in existing:
            try:
                seqs.append(int(str(num).split("-")[-1]))
            except Exception:
                continue
        next_seq = (max(seqs) + 1) if seqs else 1
        inv_number = f"{year}-{next_seq:03d}"
        return json.dumps({"invoice_number": inv_number}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "generate_invoice_number","description": "Generate the next sequential invoice number for a given year (format: INV-YYYY-XXX equivalent backbone).","parameters": {"type": "object","properties": {"year": {"type": "integer"}},"required": ["year"]}}}
