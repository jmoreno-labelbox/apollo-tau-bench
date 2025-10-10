# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateQCFigures(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        processed_csv_path = kwargs.get("processed_csv_path")
        figure_type = kwargs.get("figure_type", "overview")
        qc_fig_id = "QC_FIG_001"
        figures = {
            "qc_figure_id": qc_fig_id,
            "source": processed_csv_path,
            "figure_paths": [f"/figures/qc_{figure_type}.png", "/figures/qc_gaps.png"],
        }
        data.setdefault("qc_figures.json", []).append(figures)
        return json.dumps(figures)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateQCFigures",
                "parameters": {
                    "type": "object",
                    "properties": {"processed_csv_path": {"type": "string"}},
                    "required": ["processed_csv_path"],
                },
            },
        }
