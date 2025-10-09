from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateQCFigures(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        figure_type: str = "overview",
        processed_csv_path: str = None
    ) -> str:
        qc_fig_id = "QC_FIG_001"
        figures = {
            "qc_figure_id": qc_fig_id,
            "source": processed_csv_path,
            "figure_paths": [f"/figures/qc_{figure_type}.png", "/figures/qc_gaps.png"],
        }
        data.setdefault("qc_figures.json", []).append(figures)
        payload = figures
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createQcfigures",
                "parameters": {
                    "type": "object",
                    "properties": {"processed_csv_path": {"type": "string"}},
                    "required": ["processed_csv_path"],
                },
            },
        }
