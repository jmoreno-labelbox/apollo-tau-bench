from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetDirectoryOperationByID(Tool):
    """Fetches a file organization task (directory operation) using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], operation_id: str = None) -> str:
        for op in data.get("directories", []):
            if op.get("operation_id") == operation_id:
                payload = op
                out = json.dumps(payload)
                return out
        payload = {"error": f"Directory operation with ID '{operation_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDirectoryOperationById",
                "description": "Fetches the details for a file organization task, including source, destination, and file type mappings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "operation_id": {
                            "type": "string",
                            "description": "The unique ID of the directory operation (e.g., 'dir_op_001').",
                        }
                    },
                    "required": ["operation_id"],
                },
            },
        }
