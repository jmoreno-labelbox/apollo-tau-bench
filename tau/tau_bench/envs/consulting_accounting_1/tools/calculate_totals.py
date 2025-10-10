# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTotals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hst_rate = float(kwargs.get("hst_rate", 0.13))
        invoice_lines = kwargs.get("invoice_lines", [])
        if isinstance(invoice_lines, list) and invoice_lines and isinstance(invoice_lines[0], dict):
            subtotal = sum(float(l.get("line_amount", 0.0)) for l in invoice_lines)
        else:
            subtotal = 0.0
            lines_index = {l["invoice_line_id"]: l for l in data.get("invoice_lines", [])}
            for lid in invoice_lines:
                line = lines_index.get(lid)
                if line:
                    subtotal += float(line.get("line_amount", 0.0))
        hst_amount = round(subtotal * hst_rate, 2)
        total_due = round(subtotal + hst_amount, 2)
        return json.dumps({"subtotal": round(subtotal, 2),"hst_amount": hst_amount,"total_due": total_due}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "calculate_totals","description": "Calculate subtotal, HST and total due based on provided invoice lines.","parameters": {"type": "object","properties": {"invoice_lines": {"type": "array","items": {"anyOf": [{"type": "string"},{"type": "object"}]}},"hst_rate": {"type": "number"}},"required": ["invoice_lines"]}}}
