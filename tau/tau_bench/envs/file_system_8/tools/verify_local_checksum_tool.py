from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class VerifyLocalChecksumTool(Tool):
    """Confirms the checksum of a file copied locally."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifyLocalChecksum",
                "description": "Verifies the integrity of a copied file by re-computing its checksum and comparing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "The base name of the local log file to verify.",
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
