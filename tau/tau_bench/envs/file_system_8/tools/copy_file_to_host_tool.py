from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class CopyFileToHostTool(Tool):
    """Emulates transferring a file (along with its checksum) from remote to host via scp."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CopyFileToHost",
                "description": "Simulates copying a log and its checksum file from a remote source to the local host.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "The name of the log file to copy.",
                        }
                    },
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], log_name: str) -> str:
        checksum_name = f"{log_name}.sha256"
        if log_name not in data or checksum_name not in data:
            payload = {"error": "Log or checksum not found for copying."}
            out = json.dumps(payload)
            return out

        local_log_name = f"local_{log_name}"
        local_checksum_name = f"local_{checksum_name}"

        data[local_log_name] = data[log_name]
        data[local_checksum_name] = data[checksum_name]
        payload = {"status": "success", "copied_files": [local_log_name, local_checksum_name]}
        out = json.dumps(payload)
        return out
