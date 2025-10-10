# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TriggerRecountIfNeeded(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"recount_triggered": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "trigger_recount_if_needed", "parameters": {"store_id": {"type": "string"}, "sku": {"type": "string"}, "discrepancy_threshold": {"type": "number"}}, "required": ["store_id", "sku", "discrepancy_threshold"]}}
