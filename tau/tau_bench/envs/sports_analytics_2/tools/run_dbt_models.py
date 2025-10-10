# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RunDbtModels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"dbt_run_status": "success"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "run_dbt_models", "description": "Executes dbt models for analysis.", "parameters": {"type": "object", "properties": {"tags": {"type": "array", "items": {"type": "string"}}, "date": {"type": "string"}}, "required": ["date"]}}}
