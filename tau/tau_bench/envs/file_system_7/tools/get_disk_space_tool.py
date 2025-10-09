from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class GetDiskSpaceTool(Tool):
    """Emulates the process of checking available disk space."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDiskSpace",
                "description": "Returns the available disk space. In this simulation, it returns a fixed large number for determinism.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "The path to check for disk space (unused in simulation).",
                        }
                    },
                    "required": ["path"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], path: str) -> str:
        available_space = 10**12  # 1 Terabyte.
        data[f"disk_space_{path.replace('/', '_')}"] = available_space
        payload = {"available_space": available_space, "path": path}
        out = json.dumps(payload)
        return out
