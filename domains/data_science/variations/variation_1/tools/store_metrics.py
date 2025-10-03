from tau_bench.envs.tool import Tool
import json
from typing import Any

class StoreMetrics(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        accuracy_nullable: float = None,
        auc_nullable: float = None,
        generated_ts: str = None,
        metrics_csv_path: str = None,
        model_name: str = None,
        rmse_nullable: float = None
    ) -> str:
        err = _require({"model_name": model_name, "metrics_csv_path": metrics_csv_path}, ["model_name", "metrics_csv_path"])
        if err:
            return err
        row = {
            "model_name": model_name,
            "metrics_csv_path": metrics_csv_path,
            "auc_nullable": auc_nullable,
            "accuracy_nullable": accuracy_nullable,
            "rmse_nullable": rmse_nullable,
            "generated_ts": generated_ts,
        }
        payload = _append(data.setdefault("metrics", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StoreMetrics",
                "description": "Stores metrics for a model (AUC/accuracy/RMSE).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "metrics_csv_path": {"type": "string"},
                        "auc_nullable": {"type": "number"},
                        "accuracy_nullable": {"type": "number"},
                        "rmse_nullable": {"type": "number"},
                        "generated_ts": {"type": "string"},
                    },
                    "required": ["model_name", "metrics_csv_path"],
                },
            },
        }
