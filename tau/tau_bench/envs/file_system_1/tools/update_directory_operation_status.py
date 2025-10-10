# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateDirectoryOperationStatus(Tool):
    """Updates the status of a single file in a file organization task."""
    @staticmethod
    def invoke(data: Dict[str, Any], file_id, status) -> str:
        new_status = status
        for file in data.get('file_lists', []):
            if file.get('file_id') == file_id:
                file['status'] = new_status
                return json.dumps({"status": "success", "updated_file": file})
        return json.dumps({"status": "failure", "error": f"File ID '{file_id}' not found in any directory operation."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_directory_operation_status", "description": "Updates the status of an individual file within a file organization task.", "parameters": {"type": "object", "properties": {"file_id": {"type": "string"}, "status": {"type": "string", "enum": ["completed", "failed", "in_progress"]}}, "required": ["file_id", "status"]}}}
