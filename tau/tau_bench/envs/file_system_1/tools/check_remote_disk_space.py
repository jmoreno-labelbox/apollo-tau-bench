from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CheckRemoteDiskSpace(Tool):
    """Verifies the available disk space on the filesystem of a remote server."""

    @staticmethod
    def invoke(data: dict[str, Any], hostname: str = None) -> str:
        for server_resources in data.get("system_resources", []):
            if server_resources.get("hostname") == hostname:
                disk_info = server_resources.get("disk", {})
                payload = {
                    "hostname": hostname,
                    "available_gb": disk_info.get("available_gb"),
                    "total_gb": disk_info.get("total_gb"),
                    "usage_percent": disk_info.get("usage_percent"),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Resource information for server '{hostname}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckRemoteDiskSpace",
                "description": "Checks the available disk space on a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {
                            "type": "string",
                            "description": "The hostname of the server to check.",
                        }
                    },
                    "required": ["hostname"],
                },
            },
        }
