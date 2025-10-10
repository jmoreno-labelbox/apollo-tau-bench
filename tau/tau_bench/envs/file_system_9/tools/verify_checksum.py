# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class VerifyChecksum(Tool):
    """Verifies the checksum of a file against its original record in file_lists.json."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_id = kwargs.get("file_id")
        filepath = kwargs.get("filepath")
        
        original_checksum = None
        for record in data.get("file_lists", []):
            if record.get("file_id") == file_id:
                original_checksum = record.get("checksum")
                break
        
        if not original_checksum:
            return json.dumps({"error": f"File record not found for file_id: {file_id}"})

        try:
            dest_hostname, dest_path = filepath.split(":", 1)
        except ValueError:
            return json.dumps({"error": "Invalid filepath format. Expected 'hostname:/path/to/file'"})

        actual_checksum = None
        file_found = False
        for server in data.get("file_system", []):
            if server.get("hostname") == dest_hostname:
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if f"{directory.get('path')}/{file.get('filename')}" == dest_path:
                            actual_checksum = file.get("checksum")
                            file_found = True
                            break
                    if file_found: break
                if file_found: break

        if not file_found:
            return json.dumps({"error": f"File not found at path: {filepath}"})

        match = (original_checksum == actual_checksum)
        
        return json.dumps({"match": match, "original_checksum": original_checksum, "actual_checksum": actual_checksum})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_checksum",
                "description": "Verifies the checksum of a file against its original record in file_lists.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_id": {"type": "string", "description": "The ID of the file record in file_lists.json."},
                        "filepath": {"type": "string", "description": "The full path of the file to verify, in 'hostname:/path/to/file' format."}
                    },
                    "required": ["file_id", "filepath"],
                },
            },
        }
