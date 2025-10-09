from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetRemoteFileChecksum(Tool):
    """Computes the checksum (e.g., SHA256) for a file located on a remote server."""

    @staticmethod
    def invoke(data: dict[str, Any], hostname: str = None, filepath: str = None) -> str:
        for server in data.get("file_system", []):
            if server.get("hostname") == hostname:
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if (
                            f"{directory.get('path')}/{file.get('filename')}"
                            == filepath
                        ):
                            payload = {"filepath": filepath, "checksum": file.get("checksum")}
                            out = json.dumps(
                                payload)
                            return out
        payload = {"error": f"File '{filepath}' not found on '{hostname}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRemoteFileChecksum",
                "description": "Calculates and retrieves the checksum of a specific file on a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {"type": "string"},
                        "filepath": {"type": "string"},
                    },
                    "required": ["hostname", "filepath"],
                },
            },
        }
