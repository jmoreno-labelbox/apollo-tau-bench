# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class VerifySpaceRequirementsTool(Tool):
    """Compares total file size against available disk space to ensure sufficient space."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_space_requirements",
                "description": "Compares the total size of files to be moved against available disk space at the destination to ensure the operation can proceed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_path": {
                            "type": "string",
                            "description": "The destination path to check space for.",
                        }
                    },
                    "required": ["destination_path"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], destination_path) -> str:

        # Obtain the cumulative size from the previous calculation.
        total_size = data.get("last_total_size", 0)

        # Retrieve the available storage for the target location.
        disk_space_key = f"disk_space_{destination_path.replace('/', '_')}"
        available_space = data.get(
            disk_space_key, 10**12
        )  # Use 1TB as the default value if not specified.

        if total_size <= available_space:
            return json.dumps(
                {
                    "status": "sufficient_space",
                    "total_size": total_size,
                    "available_space": available_space,
                    "space_check": "passed",
                }
            )
        else:
            return json.dumps(
                {
                    "status": "insufficient_space",
                    "total_size": total_size,
                    "available_space": available_space,
                    "space_check": "failed",
                    "error": f"Insufficient disk space. Need {total_size} bytes but only {available_space} bytes available.",
                }
            )
