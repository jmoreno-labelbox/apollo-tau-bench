# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPendingFileChecks(Tool):
    """Retrieves pending file check tasks."""
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        pending_tasks = [task for task in list(data.get("file_check_db", {}).values()) if not task.get("completed")]
        return json.dumps({"pending_tasks": pending_tasks})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pending_file_checks",
                "description": "Retrieves pending file check tasks.",
                "parameters": {},
            },
        }
