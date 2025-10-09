from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetServerResourceUsage(Tool):
    """Fetches the real-time CPU, memory, and disk utilization of a server."""

    @staticmethod
    def invoke(data: dict[str, Any], hostname: str = None) -> str:
        for server in data.get("system_resources", []):
            if server.get("hostname") == hostname:
                payload = server
                out = json.dumps(payload)
                return out
        payload = {"error": f"Resource usage for server '{hostname}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetServerResourceUsage",
                "description": "Retrieves current CPU, memory, and disk usage for a specific server.",
                "parameters": {
                    "type": "object",
                    "properties": {"hostname": {"type": "string"}},
                    "required": ["hostname"],
                },
            },
        }
