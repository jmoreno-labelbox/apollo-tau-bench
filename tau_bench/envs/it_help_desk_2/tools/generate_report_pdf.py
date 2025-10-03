from tau_bench.envs.tool import Tool
import json
from typing import Any

class GenerateReportPDF(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], kpi_data_path: str = None, template_path: str = None, output_path: str = None) -> str:
        payload = {"status": "generated", "output_path": output_path}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateReportPdf",
                "description": "Generate a PDF report from KPI data using a template.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kpi_data_path": {"type": "string"},
                        "template_path": {"type": "string"},
                        "output_path": {"type": "string"},
                    },
                    "required": ["kpi_data_path", "template_path", "output_path"],
                },
            },
        }
