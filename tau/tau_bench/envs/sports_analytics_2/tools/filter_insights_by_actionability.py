# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterInsightsByActionability(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"filtered": True, "filtered_table": "flags_actionable"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "filter_insights_by_actionability", "description": "Filters insights by actionability.", "parameters": {"type": "object", "properties": {}}, "required": []}}
