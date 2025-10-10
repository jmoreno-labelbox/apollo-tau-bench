# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SshConnectivityVerifierTool(Tool):
    """Tool for validating SSH access to target servers."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_ssh_connection",
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
    def invoke(data: Dict[str, Any], remote_address) -> str:
        server_address = remote_address

        # Consistently provides a successful connection for testing scenarios.
        response_data = {
            "status": "connected",
            "remote_address": server_address
        }

        return json.dumps(response_data)
