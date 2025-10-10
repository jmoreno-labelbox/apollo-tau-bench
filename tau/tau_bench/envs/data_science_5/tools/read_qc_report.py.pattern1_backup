# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadQcReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        figs = data.get("qc_figures", []) or []
        fid = kwargs.get("figure_id")
        label = kwargs.get("figure_label")
        row = None
        if fid is not None:
            row = next((f for f in figs if str(f.get("figure_id")) == str(fid)), None)
        elif label:
            row = next((f for f in figs if f.get("figure_label") == label), None)
        return json.dumps(row or {"error": "QC figure not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_qc_report",
            "description": "Read QC report metadata by id or label.",
            "parameters": {"type": "object", "properties": {
                "figure_id": {"type": "string"},
                "figure_label": {"type": "string"}
            }, "required": []}
        }}
