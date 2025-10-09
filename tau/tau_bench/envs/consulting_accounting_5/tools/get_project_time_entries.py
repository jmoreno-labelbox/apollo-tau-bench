from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class GetProjectTimeEntries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id: int) -> str:
        entries = [te['hours_worked'] for te in data["time_entries"].values() if te["project_id"] == project_id]
        return json.dumps({'project_id': project_id, 'hours': sum(entries)})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectTimeEntries",
                "description": "Retrieve all time_entry_ids for a given project_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID to fetch time entries for"}
                    },
                    "required": ["project_id"],
                },
            },
        }
