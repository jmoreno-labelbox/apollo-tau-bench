# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ScanRemoteDirectory(Tool):
    """Scans a directory on a remote server and returns files matching the criteria."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hostname = kwargs.get("hostname")
        directory_path = kwargs.get("directory")
        found_files = []
        for server in data.get('file_system', []):
            if server.get('hostname') == hostname:
                for directory in server.get('directories', []):
                    if directory.get('path') == directory_path:
                        # This is a simplified simulation
                        found_files.extend(directory.get('files', []))
        return json.dumps({"files_found": found_files, "count": len(found_files)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "scan_remote_directory", "description": "Performs a scan of a remote directory to find files matching specific criteria.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}, "directory": {"type": "string"}, "last_access_days": {"type": "integer"}, "max_size_bytes": {"type": "integer"}, "owner": {"type": "string"}}, "required": ["hostname", "directory"]}}}
