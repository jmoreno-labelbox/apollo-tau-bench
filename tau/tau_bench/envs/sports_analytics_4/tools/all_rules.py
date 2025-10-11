# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AllRules(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], ) -> str:
        # return outcome
        return json.dumps({"flagged_insights_dataframe": "flags_table"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return output
        return {"type": "function", "function": {"name": "rules", "description": "Executes the rules engine over computed metrics.", "parameters": {"type": "object", "properties": {"dbt_output_tables": {"type": "array", "items": {"type": "string"}}}, "required": ["dbt_output_tables"]}}}
