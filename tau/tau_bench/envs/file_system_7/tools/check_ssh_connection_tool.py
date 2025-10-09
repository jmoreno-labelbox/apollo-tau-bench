from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class CheckSshConnectionTool(Tool):
    """Emulates the process of verifying SSH connectivity to a remote server."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckSshConnection",
                "description": "Verifies that a remote address is accessible. For simulation, this always succeeds.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "remote_address": {
                            "type": "string",
                            "description": "The address of the remote server.",
                        }
                    },
                    "required": ["remote_address"],
                },
            },
        }

    @staticmethod

    def invoke(data: dict[str, Any], remote_address: str = None) -> str:
        payload = {"status": "connected", "remote_address": remote_address}
        out = json.dumps(payload)
        return out
