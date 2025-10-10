# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DbMod(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # return result
        return json.dumps({"dbt_run_status": "success"}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {"type": "function", "function": {"name": "dbMod", "description": "Executes dbt models for analysis.", "parameters": {"type": "object", "properties": {"tags": {"type": "array", "items": {"type": "string"}}, "date": {"type": "string"}}, "required": ["date"]}}}
