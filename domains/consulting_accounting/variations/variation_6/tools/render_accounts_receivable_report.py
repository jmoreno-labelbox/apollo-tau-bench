from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class RenderAccountsReceivableReport(Tool):
    """Provide a PDF path for the Accounts Receivable Aging report."""

    @staticmethod
    def invoke(data: dict[str, Any], period_label: str = None) -> str:
        pdf_path = (
            f"https://test.storage.com/reports/accounts_receivable_{period_label}.pdf"
        )
        payload = {"pdf_path": pdf_path}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RenderAccountsReceivableReport",
                "description": "Export an Accounts Receivable Aging report and return the PDF path.",
                "parameters": {
                    "type": "object",
                    "properties": {"period_label": {"type": "string"}},
                    "required": ["period_label"],
                },
            },
        }
