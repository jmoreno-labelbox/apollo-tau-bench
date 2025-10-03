from tau_bench.envs.tool import Tool
import json
from typing import Any

class GenerateQCFigure(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], figure_label: str = None) -> str:
        label = figure_label
        pdf_path = f"https://storage.example.com/reports/{label}.pdf"
        payload = {"figure_path": pdf_path}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportQcFigure",
                "description": "Export a QC figure/report and return its deterministic pdf path.",
                "parameters": {
                    "type": "object",
                    "properties": {"figure_label": {"type": "string"}},
                    "required": ["figure_label"],
                },
            },
        }
