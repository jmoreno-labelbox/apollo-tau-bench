# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PublishStakeholderOutputs(Tool):
    """
    Creates a stakeholder_outputs record after verifying referenced predictions and metrics exist.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], predictions_final_csv_path: str, metrics_summary_csv_path: str, generated_ts: str) -> str:
        preds_ok = False
        for r in data.get("predictions", []):
            if r.get("predictions_csv_path") == predictions_final_csv_path:
                preds_ok = True
                break
        metrics_ok = False
        for r in data.get("metrics", []):
            if r.get("metrics_csv_path") == metrics_summary_csv_path:
                metrics_ok = True
                break
        if not preds_ok or not metrics_ok:
            return json.dumps({"error": "referenced artifacts not found", "predictions_ok": preds_ok, "metrics_ok": metrics_ok})
        rec = {
            "predictions_final_csv_path": predictions_final_csv_path,
            "metrics_summary_csv_path": metrics_summary_csv_path,
            "generated_ts": generated_ts
        }
        data.setdefault("stakeholder_outputs", []).append(rec)
        return json.dumps({"status": "inserted", "record": rec})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "publish_stakeholder_outputs",
                "description": "Creates a stakeholder_outputs record after verifying predictions and metrics exist.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "predictions_final_csv_path": {"type": "string"},
                        "metrics_summary_csv_path": {"type": "string"},
                        "generated_ts": {"type": "string"}
                    },
                    "required": ["predictions_final_csv_path", "metrics_summary_csv_path", "generated_ts"]
                }
            }
        }
