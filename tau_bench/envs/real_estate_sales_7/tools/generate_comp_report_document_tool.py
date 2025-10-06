from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class GenerateCompReportDocumentTool(Tool):
    """Creates a PDF report for comparable analysis."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        report_id: int = None,
        subject_property_data: dict = None,
        comparable_data: list = None,
        market_analysis: dict = None,
        mortgage_calculations: dict = None
    ) -> str:
        if report_id is None:
            return _err("report_id is required")

        # Deterministic URI derived from report_id
        uri = f"https://storage.example.com/reports/comp_{int(report_id):03d}.pdf"
        out = {
            "document_uri": uri,
            "document_type": "comparable_analysis_report",
            "pages_generated": 8,
            "sections": [
                "executive_summary",
                "property_details",
                "comparables_analysis",
                "market_context",
                "financial_analysis",
                "recommendations",
            ],
            "generation_timestamp": HARD_TS,
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateCompReportDocument",
                "description": "Generate PDF comparable analysis report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
                        "subject_property_data": {"type": "object"},
                        "comparable_data": {"type": "array", "items": {"type": "object"}},
                        "market_analysis": {"type": "object"},
                        "mortgage_calculations": {"type": "object"},
                    },
                    "required": ["report_id"],
                },
            },
        }
