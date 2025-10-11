# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class NormalizeTicketTimestamps(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], input_path, output_path, timezone = "UTC") -> str:
        return json.dumps({"status": "normalized", "input_path": input_path, "output_path": output_path, "timezone": timezone}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "normalize_ticket_timestamps", "description": "Normalize ticket timestamps to specified timezone.", "parameters": {"type": "object", "properties": {"input_path": {"type": "string"}, "output_path": {"type": "string"}, "timezone": {"type": "string"}}, "required": ["input_path", "output_path"]}}}
