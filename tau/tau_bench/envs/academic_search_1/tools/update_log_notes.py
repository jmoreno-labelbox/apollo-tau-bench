# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateLogNotes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], log_id, new_notes) -> str:
        log_id,new_notes = log_id,new_notes
        if not all([log_id, new_notes]):
            return json.dumps({"error": "log_id and new_notes are required."})
        for log in list(data.get('research_logs', {}).values()):
            if log['log_id'] == log_id:
                log['notes'] += f"\n[UPDATE]: {new_notes}"
                return json.dumps({"success": True, "log_entry": log})
        return json.dumps({"error": f"Log entry with ID '{log_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_log_notes", "description": "Appends new notes to an existing research log entry.", "parameters": {"type": "object", "properties": {"log_id": {"type": "string", "description": "The ID of the log entry to update."}, "new_notes": {"type": "string", "description": "The new notes to append to the existing log."}}, "required": ["log_id", "new_notes"]}}}
