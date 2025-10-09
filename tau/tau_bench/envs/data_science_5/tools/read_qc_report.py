from tau_bench.envs.tool import Tool
import json
from typing import Any

class ReadQcReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], figure_id: str = None, figure_label: str = None) -> str:
        figs = data.get("qc_figures", []) or []
        fid = figure_id
        label = figure_label
        row = None
        if fid is not None:
            row = next((f for f in figs if str(f.get("figure_id")) == str(fid)), None)
        elif label:
            row = next((f for f in figs if f.get("figure_label") == label), None)
        payload = row or {"error": "QC figure not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadQcReport",
                "description": "Read QC report metadata by id or label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "figure_id": {"type": "string"},
                        "figure_label": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
