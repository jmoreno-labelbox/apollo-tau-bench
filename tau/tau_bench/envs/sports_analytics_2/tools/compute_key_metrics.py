# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeKeyMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"metrics_table": "key_metrics"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "compute_key_metrics", "description": "Computes key pitcher metrics.", "parameters": {"type": "object", "properties": {"source_table": {"type": "string"}}}, "required": []}}
