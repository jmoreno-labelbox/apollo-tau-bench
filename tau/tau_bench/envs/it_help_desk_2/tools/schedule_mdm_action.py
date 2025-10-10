# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ScheduleMdmAction(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id: str, when: str, action: str, workflow_id: str) -> str:
        row = {
            "workflow_id": workflow_id,
            "employee_id": None,
            "asset_id": asset_id,
            "process": action,
            "status": "scheduled",
            "pickup_code": None,
            "created_at": when,
            "completed_at": None,
        }
        _append_row(data["device_workflow"], row)
        return json.dumps({"status": "ok", "workflow": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_mdm_action",
                "description": "Schedule an MDM action for an asset (stored as a workflow entry).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string"},
                        "when": {"type": "string"},
                        "action": {"type": "string"},
                        "workflow_id": {"type": "string"},
                    },
                    "required": ["asset_id", "when", "action", "workflow_id"],
                },
            },
        }
