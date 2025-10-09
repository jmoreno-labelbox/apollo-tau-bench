from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class TransferArchiveRsyncTool(Tool):
    """Emulates the transfer of an archive to a remote location using rsync."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transferArchiveRsync",
                "description": "Transfers the created archive file to a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_name": {"type": "string"},
                        "remote_address": {"type": "string"},
                        "destination_path": {"type": "string"},
                    },
                    "required": ["archive_name", "remote_address", "destination_path"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], destination_path: str, archive_name: str, remote_address: str) -> str:
        if "remote_storage" not in data:
            data["remote_storage"] = []
        remote_file = {
            "path": f"{destination_path}/{archive_name}",
            "remote_address": remote_address,
        }
        data["remote_storage"].append(remote_file)
        payload = {"status": "success", "transferred_file": remote_file}
        out = json.dumps(payload)
        return out
