from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetServerStatusByHostname(Tool):
    """Verifies the status of a remote server (e.g., online, under maintenance)."""

    @staticmethod
    def invoke(data: dict[str, Any], hostname: str = None) -> str:
        for server in data.get("remote_servers", []):
            if server.get("hostname") == hostname:
                payload = {"hostname": hostname, "status": server.get("status")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Server with hostname '{hostname}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetServerStatusByHostname",
                "description": "Retrieves the current operational status of a server by its hostname.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {
                            "type": "string",
                            "description": "The fully qualified domain name of the server.",
                        }
                    },
                    "required": ["hostname"],
                },
            },
        }
