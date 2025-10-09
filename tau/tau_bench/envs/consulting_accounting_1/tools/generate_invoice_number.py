from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GenerateInvoiceNumber(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], year: str = None) -> str:
        if not year:
            payload = {"error": "year is required"}
            out = json.dumps(payload, indent=2)
            return out
        existing = [
            i.get("invoice_number")
            for i in data.get("invoices", {}).values()
            if str(i.get("invoice_number", "")).startswith(f"{year}-")
        ]
        seqs = []
        for num in existing:
            try:
                seqs.append(int(str(num).split("-")[-1]))
            except Exception:
                continue
        next_seq = (max(seqs) + 1) if seqs else 1
        inv_number = f"{year}-{next_seq:03d}"
        payload = {"invoice_number": inv_number}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateInvoiceNumber",
                "description": "Generate the next sequential invoice number for a given year (format: INV-YYYY-XXX equivalent backbone).",
                "parameters": {
                    "type": "object",
                    "properties": {"year": {"type": "integer"}},
                    "required": ["year"],
                },
            },
        }
