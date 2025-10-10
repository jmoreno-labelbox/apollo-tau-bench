# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateLifecycleQueueStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], lifecycle_id, status) -> str:
        queue = list(data.get("lifecycle_queue", {}).values())
        entry = next((e for e in queue if e.get("lifecycle_id") == lifecycle_id), None)
        if not entry:
            return json.dumps({"error": f"Lifecycle entry {lifecycle_id} not found."}, indent=2)
        entry["status"] = status
        return json.dumps(entry, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_lifecycle_queue_status", "description": "Updates the status of an event in the lifecycle queue (e.g., to 'completed').", "parameters": {"type": "object", "properties": {"lifecycle_id": {"type": "string"}, "status": {"type": "string"}}, "required": ["lifecycle_id", "status"]}}}
