from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ScanRemoteDirectory(Tool):
    """Examines a directory on a remote server and returns files that meet the criteria."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        directory: Any = None,
        directory_path: str = None,
        hostname: str = None
    ) -> str:
        # Support 'directory' as an alias for 'directory_path'
        if directory is not None:
            directory_path = directory
        found_files = []
        for server in data.get("file_system", []):
            if server.get("hostname") == hostname:
                for directory in server.get("directories", []):
                    if directory.get("path") == directory_path:
                        # This represents a basic simulation
                        found_files.extend(directory.get("files", []))
        payload = {"files_found": found_files, "count": len(found_files)}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ScanRemoteDirectory",
                "description": "Performs a scan of a remote directory to find files matching specific criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {"type": "string"},
                        "directory": {"type": "string"},
                        "last_access_days": {"type": "integer"},
                        "max_size_bytes": {"type": "integer"},
                        "owner": {"type": "string"},
                    },
                    "required": ["hostname", "directory"],
                },
            },
        }
