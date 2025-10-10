# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogModelMetric(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], dataset_split, metric_name, model_name, value) -> str:
        metrics = list(data.get("metrics", {}).values())
        max_id = 0
        for m in metrics:
            try:
                mid = int(m.get("metric_id", 0))
                if mid > max_id:
                    max_id = mid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "metric_id": new_id,
            "model_name": model_name,
            "metric_name": metric_name,
            "value": value,
            "dataset_split": dataset_split,
            "timestamp": _fixed_now_iso(),
        }
        metrics.append(row)
        return json.dumps({"metric_id": new_id, "model_name": row["model_name"], "metric_name": row["metric_name"]},
                          indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "log_model_metric",
            "description": "Insert a metric row for a model+split.",
            "parameters": {"type": "object", "properties": {
                "model_name": {"type": "string"},
                "metric_name": {"type": "string"},
                "value": {"type": "number"},
                "dataset_split": {"type": "string"}
            }, "required": ["model_name", "metric_name", "value", "dataset_split"]}
        }}
