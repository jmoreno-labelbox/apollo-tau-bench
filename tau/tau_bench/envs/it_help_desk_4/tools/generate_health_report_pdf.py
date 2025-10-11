# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateHealthReportPDF(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], kpis) -> str:
        if not all(k in kpis for k in ["total_open", "avg_age_open_hours"]):
            return json.dumps({"status": "failed", "reason": "KPI data is incomplete", "missing_fields": [k for k in ["total_open", "avg_age_open_hours"] if k not in kpis]}, indent=2)
        report_path = f"\\\\IT\\Reports\\DailyReports\\{FIXED_NOW.split('T')[0]}\\ServiceDesk_Health_Report.pdf"
        return json.dumps({"report_path": report_path, "status": "generated"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "generate_health_report_pdf", "description": "Generates a PDF health report from calculated KPI data.", "parameters": {"type": "object", "properties": {"kpis": {"type": "object"}}, "required": ["kpis"]}}}
