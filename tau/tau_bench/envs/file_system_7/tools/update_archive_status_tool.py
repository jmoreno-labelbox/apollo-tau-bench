# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateArchiveStatusTool(Tool):
    """Updates the status of a task in the archive_instructions database."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_archive_status",
                "description": "Finds an archive instruction by its 'archive_id' and updates its 'status' field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_id": {"type": "string", "description": "The ID of the archive task to update (e.g., 'arch_001')."},
                        "status": {"type": "string", "description": "The new status to set (e.g., 'completed', 'failed')."}
                    },
                    "required": ["archive_id", "status"]
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], archive_id, status) -> str:
        archive_task = next((t for t in data.get("archive_instructions", []) if t.get("archive_id") == archive_id), None)
        if archive_task:
            archive_task["status"] = status
            return json.dumps({"status": "success", "archive_id": archive_id, "new_status": status})
        return json.dumps({"error": f"Archive ID {archive_id} not found."})
