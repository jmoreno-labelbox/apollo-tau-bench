# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateSummaryPlots(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        predictions_id = kwargs.get("predictions_id")
        model_id = kwargs.get("model_id")

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

        return json.dumps(qc_figure_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSummaryPlots",
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
