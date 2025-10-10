# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckSshConnectionTool(Tool):
    """Simulates checking SSH connectivity to a remote server."""

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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps(
            {"status": "connected", "remote_address": kwargs["remote_address"]}
        )
