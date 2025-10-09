from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class PublishStakeholderOutputs(Tool):
    """Generates a stakeholder_outputs record after confirming that referenced predictions and metrics are present."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        predictions_final_csv_path: str,
        metrics_summary_csv_path: str,
        generated_ts: str,
    ) -> str:
        preds_ok = False
        for r in data.get("predictions", {}).values():
            if r.get("predictions_csv_path") == predictions_final_csv_path:
                preds_ok = True
                break
        metrics_ok = False
        for r in data.get("metrics", {}).values():
            if r.get("metrics_csv_path") == metrics_summary_csv_path:
                metrics_ok = True
                break
        if not preds_ok or not metrics_ok:
            payload = {
                "error": "referenced artifacts not found",
                "predictions_ok": preds_ok,
                "metrics_ok": metrics_ok,
            }
            out = json.dumps(payload)
            return out
        rec = {
            "predictions_final_csv_path": predictions_final_csv_path,
            "metrics_summary_csv_path": metrics_summary_csv_path,
            "generated_ts": generated_ts,
        }
        data.setdefault("stakeholder_outputs", []).append(rec)
        payload = {"status": "inserted", "record": rec}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PublishStakeholderOutputs",
                "description": "Creates a stakeholder_outputs record after verifying predictions and metrics exist.",
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
                        "generated_ts",
                    ],
                },
            },
        }
