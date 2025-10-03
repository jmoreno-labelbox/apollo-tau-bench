from tau_bench.envs.tool import Tool
import json
from typing import Any

class TransferFileToRemote(Tool):
    """Imitates the transfer of a file to a remote server, usually via SCP or rsync."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        destination_path: str = None,
        remote_address: str = None,
        source_path: str = None,
        ssh_key: Any = None
    ) -> str:
        payload = {
            "status": "success",
            "source_file": source_path,
            "destination": f"{remote_address}:{destination_path}",
            "checksum_verified": True,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TransferFileToRemote",
                "description": "Transfers a file from a source to a remote destination using a secure protocol.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_path": {"type": "string"},
                        "remote_address": {"type": "string"},
                        "destination_path": {"type": "string"},
                        "ssh_key": {"type": "string"},
                    },
                    "required": [
                        "source_path",
                        "remote_address",
                        "destination_path",
                        "ssh_key",
                    ],
                },
            },
        }
