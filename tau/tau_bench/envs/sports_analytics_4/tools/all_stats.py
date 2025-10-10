# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AllStats(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # return output
        return json.dumps({"metrics_table": "key_metrics"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return output
        return {"type": "function", "function": {"name": "getStats", "description": "Computes key pitcher metrics.", "parameters": {"type": "object", "properties": {"source_table": {"type": "string"}}}, "required": []}}
