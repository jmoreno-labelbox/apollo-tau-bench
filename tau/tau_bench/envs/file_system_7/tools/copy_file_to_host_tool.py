# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CopyFileToHostTool(Tool):
    """Simulates copying a file (and its checksum) from remote to host using scp."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "copy_file_to_host",
                "description": "Simulates copying a log and its checksum file from a remote source to the local host.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "The name of the log file to copy.",
                        }
                    },
                    "required": ["log_name"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], log_name) -> str:
        checksum_name = f"{log_name}.sha256"
        if log_name not in data or checksum_name not in data:
            return json.dumps({"error": "Log or checksum not found for copying."})

        local_log_name = f"local_{log_name}"
        local_checksum_name = f"local_{checksum_name}"

        data[local_log_name] = data[log_name]
        data[local_checksum_name] = data[checksum_name]
        return json.dumps(
            {"status": "success", "copied_files": [local_log_name, local_checksum_name]}
        )
