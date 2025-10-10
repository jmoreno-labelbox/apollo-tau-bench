# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDiskSpaceTool(Tool):
    """Simulates checking available disk space."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_disk_space",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        path = kwargs["path"]
        available_space = 10**12  # 1 Terabyte
        data[f"disk_space_{path.replace('/', '_')}"] = available_space
        return json.dumps({"available_space": available_space, "path": path})
