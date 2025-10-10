# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateArchiveTaskStatus(Tool):
    """Updates the status of an archive task in the instructions database."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        archive_id = kwargs.get("archive_id")
        new_status = kwargs.get("status")
        for instruction in data.get('archive_instructions', []):
            if instruction.get('archive_id') == archive_id:
                instruction['status'] = new_status
                return json.dumps({"status": "success", "updated_task": instruction})
        return json.dumps({"status": "failure", "error": f"Archive ID '{archive_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_archive_task_status", "description": "Updates the status of an archive task (e.g., 'in_progress', 'completed', 'failed').", "parameters": {"type": "object", "properties": {"archive_id": {"type": "string"}, "status": {"type": "string", "enum": ["in_progress", "completed", "failed", "verified"]}}, "required": ["archive_id", "status"]}}}
