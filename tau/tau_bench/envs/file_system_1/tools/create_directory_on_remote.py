from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateDirectoryOnRemote(Tool):
    """Imitates the creation of a directory on a remote server."""

    @staticmethod
    def invoke(data: dict[str, Any], directory_path: str = None, hostname: str = None) -> str:
        payload = {
            "status": "success",
            "message": f"Directory '{directory_path}' created on {hostname}.",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDirectoryOnRemote",
                "description": "Creates a new directory at the specified path on a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {"type": "string"},
                        "directory_path": {"type": "string"},
                    },
                    "required": ["hostname", "directory_path"],
                },
            },
        }
