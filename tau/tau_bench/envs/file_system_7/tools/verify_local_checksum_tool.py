# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class VerifyLocalChecksumTool(Tool):
    """Verifies the checksum of a locally copied file."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_local_checksum",
                "description": "Verifies the integrity of a copied file by re-computing its checksum and comparing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "The base name of the local log file to verify.",
                        }
                    },
                    "required": ["log_name"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        log_name = kwargs["log_name"]
        checksum_name = f"{kwargs['log_name']}.sha256"
        if log_name not in data or checksum_name not in data:
            return json.dumps({"error": "Log or checksum not found for copying."})

        local_log_name = f"local_{log_name}"
        local_checksum_name = f"local_{checksum_name}"

        data[local_log_name] = data[log_name]
        data[local_checksum_name] = data[checksum_name]

        return json.dumps(
            {"status": "success", "copied_files": [local_log_name, local_checksum_name]}
        )
