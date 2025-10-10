# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildMetricsSummaryPath(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        model_name = kwargs.get("model_name")
        end_ts = kwargs.get("end_ts")
        if not model_name or not end_ts:
            return json.dumps({"error":"Missing model_name or end_ts"})
        y1 = end_ts[:10].replace("-","")
        return json.dumps({"metrics_summary_path": f"/processed_data/metrics_summary_{model_name}_{y1}.csv"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_metrics_summary_path","description":"Builds canonical metrics summary CSV path from model_name and end_ts.","parameters":{"type":"object","properties":{"model_name":{"type":"string"},"end_ts":{"type":"string"}},"required":["model_name","end_ts"]}}}
