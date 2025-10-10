# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsightAction(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # return output
        return json.dumps({"filtered": True, "filtered_table": "flags_actionable"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return outcome
        return {"type": "function", "function": {"name": "cutOut", "description": "Selects insights by actionability.", "parameters": {"type": "object", "properties": {}}, "required": []}}
