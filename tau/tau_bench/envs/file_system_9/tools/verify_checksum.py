from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class VerifyChecksum(Tool):
    """Confirms the checksum of a file against its initial record in file_lists.json."""

    @staticmethod
    def invoke(data: dict[str, Any], file_id: str = None, filepath: str = None) -> str:
        original_checksum = None
        for record in data.get("file_lists", []):
            if record.get("file_id") == file_id:
                original_checksum = record.get("checksum")
                break

        if not original_checksum:
            payload = {"error": f"File record not found for file_id: {file_id}"}
            out = json.dumps(payload)
            return out

        try:
            dest_hostname, dest_path = filepath.split(":", 1)
        except ValueError:
            payload = {"error": "Invalid filepath format. Expected 'hostname:/path/to/file'"}
            out = json.dumps(payload)
            return out

        actual_checksum = None
        file_found = False
        for server in data.get("file_system", []):
            if server.get("hostname") == dest_hostname:
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if (
                            f"{directory.get('path')}/{file.get('filename')}"
                            == dest_path
                        ):
                            actual_checksum = file.get("checksum")
                            file_found = True
                            break
                    if file_found:
                        break
                if file_found:
                    break

        if not file_found:
            payload = {"error": f"File not found at path: {filepath}"}
            out = json.dumps(payload)
            return out

        match = original_checksum == actual_checksum
        payload = {
            "match": match,
            "original_checksum": original_checksum,
            "actual_checksum": actual_checksum,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifyChecksum",
                "description": "Verifies the checksum of a file against its original record in file_lists.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_id": {
                            "type": "string",
                            "description": "The ID of the file record in file_lists.json.",
                        },
                        "filepath": {
                            "type": "string",
                            "description": "The full path of the file to verify, in 'hostname:/path/to/file' format.",
                        },
                    },
                    "required": ["file_id", "filepath"],
                },
            },
        }
