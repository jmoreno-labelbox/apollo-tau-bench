from tau_bench.envs.tool import Tool
import json
from typing import Any

class MoveFileOnRemote(Tool):
    """Imitates transferring a file from one location to another on the same remote server."""

    @staticmethod
    def invoke(data: dict[str, Any], source_path: str = None, destination_path: str = None, hostname: str = None) -> str:
        payload = {
            "status": "success",
            "message": f"Moved {source_path} to {destination_path} on {hostname}.",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MoveFileOnRemote",
                "description": "Moves a file on a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {"type": "string"},
                        "source_path": {"type": "string"},
                        "destination_path": {"type": "string"},
                    },
                    "required": ["hostname", "source_path", "destination_path"],
                },
            },
        }
