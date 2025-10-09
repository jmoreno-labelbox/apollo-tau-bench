from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class ComputeChecksumTool(Tool):
    """Calculates a sha256sum for a data object, emulating checksum creation."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeChecksum",
                "description": "Computes and returns a sha256 checksum for a given log file.",
                "parameters": {
                    "type": "object",
                    "properties": {"log_name": {"type": "string"}},
                    "required": ["log_name"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], log_name: str) -> str:
        if log_name not in data:
            payload = {"error": f"Log '{log_name}' not found."}
            out = json.dumps(payload)
            return out
        content_str = json.dumps(data[log_name], sort_keys=True)
        checksum = hashlib.sha256(content_str.encode()).hexdigest()
        #store checksum using a deterministic key '<log_name>.sha256'.
        data[f"{log_name}.sha256"] = checksum
        payload = {"log_name": log_name, "checksum": checksum}
        out = json.dumps(payload)
        return out
