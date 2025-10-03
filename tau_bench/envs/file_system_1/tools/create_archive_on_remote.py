from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateArchiveOnRemote(Tool):
    """Imitates the creation of a compressed tarball (tar.gz) on a remote server."""

    @staticmethod
    def invoke(data: dict[str, Any], hostname: str = None, archive_path: str = None, files_to_include: list = None) -> str:
        file_count = len(files_to_include or [])
        payload = {
            "status": "success",
            "hostname": hostname,
            "archive_path": archive_path,
            "message": f"Successfully created archive '{archive_path}' with {file_count} files on {hostname}.",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateArchiveOnRemote",
                "description": "Creates a compressed tar.gz archive from a list of files on a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {"type": "string"},
                        "archive_path": {"type": "string"},
                        "files_to_include": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["hostname", "archive_path", "files_to_include"],
                },
            },
        }
