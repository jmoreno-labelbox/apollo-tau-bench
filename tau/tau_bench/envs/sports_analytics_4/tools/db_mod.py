# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DbMod(Tool):
    @staticmethod
        # primary call function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # return outcome
        return json.dumps({"dbt_run_status": "success"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # output result
        return {"type": "function", "function": {"name": "dbMod", "description": "Executes dbt models for analysis.", "parameters": {"type": "object", "properties": {"tags": {"type": "array", "items": {"type": "string"}}, "date": {"type": "string"}}, "required": ["date"]}}}
