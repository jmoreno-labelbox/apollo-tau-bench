from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateSummaryPlots(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], predictions_id: str = None, model_id: str = None) -> str:
        figure_id = "FIGURE_001"
        figure_path = f"/figures/risk_timeseries_{model_id}.png"

        qc_figure_entry = {
            "figure_id": figure_id,
            "figure_paths": [figure_path, f"/figures/summary_{model_id}.png"],
            "descriptions": [
                f"Time series summary plot showing predicted flood risk probability vs key drivers for model '{model_id}'."
            ],
            "predictions_id": predictions_id,
        }

        data.setdefault("qc_figures.json", []).append(qc_figure_entry)
        payload = qc_figure_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createSummaryPlots",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "predictions_id": {
                            "type": "string",
                            "description": "The ID of the final predictions.",
                        },
                        "metrics_id": {
                            "type": "string",
                            "description": "The ID of the final metrics.",
                        },
                    },
                    "required": [],
                },
            },
        }
