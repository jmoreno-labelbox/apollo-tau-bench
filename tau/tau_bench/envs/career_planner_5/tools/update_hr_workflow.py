# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_hr_workflow(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], workflow_id: str, updates: Dict[str, Any]) -> str:
        wf = next(
            (
                w
                for w in data.get("hr_workflows", [])
                if w["workflow_id"] == workflow_id
            ),
            None,
        )
        if not wf:
            return json.dumps({"error": "workflow not found"})

        if "notes_append" in updates:
            wf["notes"] = wf.get("notes", "") + " " + updates.pop("notes_append")

        wf.update(updates)
        return json.dumps({"success": f"workflow {workflow_id} updated"})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_hr_workflow",
                "description": "Update fields of an existing HR workflow record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "workflow_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["workflow_id", "updates"],
                },
            },
        }
