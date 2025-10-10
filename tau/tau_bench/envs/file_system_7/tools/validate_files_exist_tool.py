# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateFilesExistTool(Tool):
    """Checks if all specified files for archiving exist."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "validate_files_exist", "description": "Validates that all file paths in a list exist in the system.", "parameters": { "type": "object", "properties": { "file_paths": {"type": "array", "items": {"type": "string"}}}, "required": ["file_paths"]}}}

    @staticmethod
    def invoke(data: Dict[str, Any], file_paths) -> str:
        existing_paths = {f["path"] for f in data.get("remote_files", [])}
        missing_files = [p for p in file_paths if p not in existing_paths]
        if missing_files: return json.dumps({"status": "failed", "missing_files": missing_files})
        return json.dumps({"status": "success", "all_files_exist": True})
