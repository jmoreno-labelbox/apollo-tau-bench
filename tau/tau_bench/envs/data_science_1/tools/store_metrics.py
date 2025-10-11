# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require






def _require(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return json.dumps({"error": f"Missing required arguments: {', '.join(missing)}"}, indent=2)
    return None

def _append(table: List[Dict[str, Any]], row: Dict[str, Any]) -> Dict[str, Any]:
    table.append(row)
    return row

class StoreMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], accuracy_nullable, auc_nullable, generated_ts, metrics_csv_path, model_name, rmse_nullable) -> str:
        err = _require(kwargs, ["model_name", "metrics_csv_path"])
        if err: return err
        row = {"model_name": model_name, "metrics_csv_path": metrics_csv_path,
               "auc_nullable": auc_nullable, "accuracy_nullable": accuracy_nullable,
               "rmse_nullable": rmse_nullable, "generated_ts": generated_ts}
        return json.dumps(_append(data.setdefault("metrics", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_metrics",
            "description": "Stores metrics for a model (AUC/accuracy/RMSE).",
            "parameters": {"type": "object", "properties": {
                "model_name": {"type": "string"}, "metrics_csv_path": {"type": "string"},
                "auc_nullable": {"type": "number"}, "accuracy_nullable": {"type": "number"},
                "rmse_nullable": {"type": "number"}, "generated_ts": {"type": "string"}},
                "required": ["model_name", "metrics_csv_path"]}}}