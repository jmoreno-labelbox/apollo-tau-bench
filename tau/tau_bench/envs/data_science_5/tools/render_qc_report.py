# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RenderQcReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        label = kwargs.get("figure_label")
        pdf_path = f"https://storage.example.com/reports/{label}.pdf"
        return json.dumps({"figure_path": pdf_path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "render_qc_report",
            "description": "Return deterministic PDF path for a QC report.",
            "parameters": {"type": "object", "properties": {"figure_label": {"type": "string"}},
                           "required": ["figure_label"]}
        }}
