from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ExportARAgingReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], period_label: str = None) -> str:
        pdf_path = f"https://storage.example.com/reports/AR_Aging_{period_label}.pdf"
        payload = {"report_pdf_path": pdf_path}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportArAgingReport",
                "description": "Export an A/R Aging report and return pdf path.",
                "parameters": {
                    "type": "object",
                    "properties": {"period_label": {"type": "string"}},
                    "required": ["period_label"],
                },
            },
        }
