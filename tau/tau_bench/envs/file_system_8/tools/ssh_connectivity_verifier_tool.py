from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class SshConnectivityVerifierTool(Tool):
    """Utility for verifying SSH access to target servers."""

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
    def invoke(data: dict[str, Any], remote_address: str) -> str:
        server_address = remote_address

        # Consistently returns a successful connection for simulation
        response_data = {"status": "connected", "remote_address": server_address}
        payload = response_data
        out = json.dumps(payload)
        return out
