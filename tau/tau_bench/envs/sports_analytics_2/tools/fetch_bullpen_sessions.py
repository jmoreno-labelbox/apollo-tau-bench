# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchBullpenSessions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        date_range = kwargs.get("date_range")
        normalize_metrics = kwargs.get("normalize_metrics", True)
        return json.dumps({"bullpen_session_data": f"sessions_{date_range}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "fetch_bullpen_sessions", "description": "Fetches recent bullpen session data.", "parameters": {"type": "object", "properties": {"date_range": {"type": "string"}, "normalize_metrics": {"type": "boolean"}}, "required": ["date_range"]}}}
