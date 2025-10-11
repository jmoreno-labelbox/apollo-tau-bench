# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFilesForDirectoryOperation(Tool):
    """Retrieves the list of files to be moved for a file organization task."""
    @staticmethod
    def invoke(data: Dict[str, Any], operation_id) -> str:
        files = [f for f in data.get('file_lists', []) if f.get('operation_id') == operation_id]
        return json.dumps({"files": files, "count": len(files)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_files_for_directory_operation", "description": "Retrieves the manifest of files associated with a specific file organization operation.", "parameters": {"type": "object", "properties": {"operation_id": {"type": "string"}}, "required": ["operation_id"]}}}
