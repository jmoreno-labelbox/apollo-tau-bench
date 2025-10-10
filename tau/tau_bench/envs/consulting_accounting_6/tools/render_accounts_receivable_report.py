# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RenderAccountsReceivableReport(Tool):
    """Return a PDF path for the Accounts Receivable Aging report."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        period_label = kwargs.get("period_label")
        pdf_path = f"https://test.storage.com/reports/accounts_receivable_{period_label}.pdf"
        return json.dumps({"pdf_path": pdf_path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "render_accounts_receivable_report",
            "description": "Export an Accounts Receivable Aging report and return the PDF path.",
            "parameters": {"type": "object", "properties": {
                "period_label": {"type": "string"}
            }, "required": ["period_label"]}
        }}
