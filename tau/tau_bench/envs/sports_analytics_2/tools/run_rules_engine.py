# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RunRulesEngine(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        return json.dumps({"flagged_insights_dataframe": "flags_table"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "run_rules_engine", "description": "Runs the rules engine over computed metrics.", "parameters": {"type": "object", "properties": {"dbt_output_tables": {"type": "array", "items": {"type": "string"}}}, "required": ["dbt_output_tables"]}}}
