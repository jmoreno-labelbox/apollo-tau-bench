from tau_bench.envs.tool import Tool
import json
from typing import Any

class RecordStakeholderOutputs(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        generated_ts: str = None,
        metrics_summary_csv_path: str = None,
        predictions_final_csv_path: str = None
    ) -> str:
        err = _require(
            {"predictions_final_csv_path": predictions_final_csv_path, "metrics_summary_csv_path": metrics_summary_csv_path}, 
            ["predictions_final_csv_path", "metrics_summary_csv_path"]
        )
        if err:
            return err
        row = {
            "predictions_final_csv_path": predictions_final_csv_path,
            "metrics_summary_csv_path": metrics_summary_csv_path,
            "generated_ts": generated_ts,
        }
        payload = _append(data.setdefault("stakeholder_outputs", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordStakeholderOutputs",
                "description": "Registers links to final predictions/metrics artifacts for stakeholders.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "predictions_final_csv_path": {"type": "string"},
                        "metrics_summary_csv_path": {"type": "string"},
                        "generated_ts": {"type": "string"},
                    },
                    "required": [
                        "predictions_final_csv_path",
                        "metrics_summary_csv_path",
                    ],
                },
            },
        }
