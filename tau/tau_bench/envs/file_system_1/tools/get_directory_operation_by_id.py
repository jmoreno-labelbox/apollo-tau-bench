# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDirectoryOperationByID(Tool):
    """Retrieves a file organization (directory operation) task by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], operation_id) -> str:
        for op in data.get('directories', []):
            if op.get('operation_id') == operation_id:
                return json.dumps(op)
        return json.dumps({"error": f"Directory operation with ID '{operation_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_directory_operation_by_id", "description": "Fetches the details for a file organization task, including source, destination, and file type mappings.", "parameters": {"type": "object", "properties": {"operation_id": {"type": "string", "description": "The unique ID of the directory operation (e.g., 'dir_op_001')."}}, "required": ["operation_id"]}}}
