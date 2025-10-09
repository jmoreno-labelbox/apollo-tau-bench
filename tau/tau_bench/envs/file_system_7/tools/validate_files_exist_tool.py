from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ValidateFilesExistTool(Tool):
    """Verifies the existence of all specified files intended for archiving."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateFilesExist",
                "description": "Validates that all file paths in a list exist in the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_paths": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["file_paths"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], file_paths: list[str], minimum_size_bytes: Any = None, check_permissions: Any = None, validate_format: Any = None) -> str:
        existing_paths = {f["path"] for f in data.get("remote_files", {}).values()}
        missing_files = [p for p in file_paths.values() if p not in existing_paths]
        if missing_files:
            payload = {"status": "failed", "missing_files": missing_files}
            out = json.dumps(payload)
            return out
        payload = {"status": "success", "all_files_exist": True}
        out = json.dumps(payload)
        return out
