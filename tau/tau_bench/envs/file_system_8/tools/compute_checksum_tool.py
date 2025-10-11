# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeChecksumTool(Tool):
    """Computes a sha256sum for a data object, simulating checksum generation."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_checksum",
                "description": "Computes and returns a sha256 checksum for a given log file.",
                "parameters": {
                    "type": "object",
                    "properties": {"log_name": {"type": "string"}},
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], log_name) -> str:
        if log_name not in data:
            return json.dumps({"error": f"Log '{log_name}' not found."})
        content_str = json.dumps(data[log_name], sort_keys=True)
        checksum = hashlib.sha256(content_str.encode()).hexdigest()
        # store checksum using a consistent key '<log_name>.sha256'
        data[f"{log_name}.sha256"] = checksum
        return json.dumps({"log_name": log_name, "checksum": checksum})
