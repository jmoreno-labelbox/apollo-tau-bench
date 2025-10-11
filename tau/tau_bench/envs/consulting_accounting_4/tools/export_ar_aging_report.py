# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExportARAgingReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], period_label) -> str:
        pdf_path = f"https://storage.example.com/reports/AR_Aging_{period_label}.pdf"
        return json.dumps({"report_pdf_path": pdf_path}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"export_ar_aging_report",
            "description":"Export an A/R Aging report and return pdf path.",
            "parameters":{"type":"object","properties":{"period_label":{"type":"string"}},"required":["period_label"]}
        }}
