# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRemoteFileChecksum(Tool):
    """Calculates the checksum (e.g., SHA256) of a file on a remote server."""
    @staticmethod
    def invoke(data: Dict[str, Any], filepath, hostname) -> str:
        for server in data.get('file_system', []):
            if server.get('hostname') == hostname:
                for directory in server.get('directories', []):
                    for file in directory.get('files', []):
                        if f"{directory.get('path')}/{file.get('filename')}" == filepath:
                             return json.dumps({"filepath": filepath, "checksum": file.get("checksum")})
        return json.dumps({"error": f"File '{filepath}' not found on '{hostname}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_remote_file_checksum", "description": "Calculates and retrieves the checksum of a specific file on a remote server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}, "filepath": {"type": "string"}}, "required": ["hostname", "filepath"]}}}
