from tau_bench.envs.tool import Tool
import json
from typing import Any

class DeleteFileOnRemote(Tool):
    """Imitates the removal of a file from a remote server."""

    @staticmethod
    def invoke(data: dict[str, Any], filepath: str = None, hostname: str = None) -> str:
        payload = {
            "status": "success",
            "message": f"Deleted {filepath} from {hostname}.",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteFileOnRemote",
                "description": "Deletes a specified file from a remote server.",
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
