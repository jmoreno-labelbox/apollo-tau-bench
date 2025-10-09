from tau_bench.envs.tool import Tool
import json
from typing import Any

class RenderQcReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], figure_label: str = None) -> str:
        pdf_path = f"https://storage.example.com/reports/{figure_label}.pdf"
        payload = {"figure_path": pdf_path}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RenderQcReport",
                "description": "Return deterministic PDF path for a QC report.",
                "parameters": {
                    "type": "object",
                    "properties": {"figure_label": {"type": "string"}},
                    "required": ["figure_label"],
                },
            },
        }
