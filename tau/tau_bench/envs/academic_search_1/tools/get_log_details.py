# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLogDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        log_id = kwargs.get('log_id')
        if not log_id:
            return json.dumps({"error": "log_id is required."})
        for log in list(data.get('research_logs', {}).values()):
            if log['log_id'] == log_id:
                return log.get('notes', '')
        return json.dumps({"error": f"Log entry with ID '{log_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_log_details", "description": "Retrieves just the notes from a single log entry by its unique ID.", "parameters": {"type": "object", "properties": {"log_id": {"type": "string", "description": "The unique ID of the log entry to retrieve."}}, "required": ["log_id"]}}}
