# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordQcReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        figs = data.get("qc_figures", [])
        max_id = 0
        for f in figs:
            try:
                fid = int(f.get("figure_id", 0))
                if fid > max_id:
                    max_id = fid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "figure_id": new_id,
            "figure_label": kwargs.get("figure_label"),
            "figure_path": kwargs.get("figure_path"),
            "artifact_type": kwargs.get("artifact_type"),
            "related_model_name": kwargs.get("related_model_name"),
            "created_at": _now_iso_fixed(),
        }
        figs.append(row)
        return json.dumps({"figure_id": new_id, "figure_label": row["figure_label"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "record_qc_report",
            "description": "Insert a QC report metadata row.",
            "parameters": {"type": "object", "properties": {
                "figure_label": {"type": "string"},
                "figure_path": {"type": "string"},
                "artifact_type": {"type": "string"},
                "related_model_name": {"type": ["string", "null"]}
            }, "required": ["figure_label", "figure_path", "artifact_type"]}
        }}
