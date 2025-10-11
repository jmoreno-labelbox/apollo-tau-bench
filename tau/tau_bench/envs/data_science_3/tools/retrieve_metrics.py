# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RetrieveMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], dataset_split, metric_name, model_name) -> str:
        metrics = data.get("metrics", []) or []
        rows = [m for m in metrics if (not model_name or m.get("model_name")==model_name)
                and (not metric_name or m.get("metric_name")==metric_name)
                and (not dataset_split or m.get("dataset_split")==dataset_split)]
        return json.dumps({"metrics": rows}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_metrics",
            "description":"List metrics (filter by model_name, metric_name, dataset_split).",
            "parameters":{"type":"object","properties":{
                "model_name":{"type":"string"},
                "metric_name":{"type":"string"},
                "dataset_split":{"type":"string"}
            },"required":[]}
        }}
