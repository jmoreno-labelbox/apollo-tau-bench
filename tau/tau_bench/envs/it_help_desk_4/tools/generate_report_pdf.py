# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateReportPDF(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], kpi_data_path, output_path, template_path) -> str:
        return json.dumps({"status": "generated", "output_path": output_path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "generate_report_pdf", "description": "Generate a PDF report from KPI data using a template.", "parameters": {"type": "object", "properties": {"kpi_data_path": {"type": "string"}, "template_path": {"type": "string"}, "output_path": {"type": "string"}}, "required": ["kpi_data_path", "template_path", "output_path"]}}}
