from tau_bench.envs.tool import Tool
import json
from typing import Any

class GenerateHealthReportPDF(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], kpis: dict[str, Any] = None) -> str:
        if not all(k in kpis for k in ["total_open", "avg_age_open_hours"]):
            payload = {
                "status": "failed",
                "reason": "KPI data is incomplete",
                "missing_fields": [
                    k for k in ["total_open", "avg_age_open_hours"] if k not in kpis
                ],
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        report_path = f"\\\\IT\\Reports\\DailyReports\\{FIXED_NOW.split('T')[0]}\\ServiceDesk_Health_Report.pdf"
        payload = {"report_path": report_path, "status": "generated"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateHealthReportPdf",
                "description": "Generates a PDF health report from calculated KPI data.",
                "parameters": {
                    "type": "object",
                    "properties": {"kpis": {"type": "object"}},
                    "required": ["kpis"],
                },
            },
        }
