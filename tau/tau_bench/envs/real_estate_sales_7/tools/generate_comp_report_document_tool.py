# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _err(msg: str, code: str = "bad_request", ) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class GenerateCompReportDocumentTool(Tool):
    """Generates PDF comparable analysis report."""

    @staticmethod
    def invoke(data: Dict[str, Any], comparable_data, market_analysis, mortgage_calculations, report_id, subject_property_data) -> str:
        subject_property_data = subject_property_data or {}
        comparable_data = comparable_data or []
        market_analysis = market_analysis or {}
        mortgage_calculations = mortgage_calculations or {}

        if report_id is None:
            return _err("report_id is required")

        # Fixed URI determined by report_id
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
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_comp_report_document",
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