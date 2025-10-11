# Copyright Sierra

import datetime, uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EscalateTask(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], escalate_to, task_id) -> str:

        if not all([task_id, escalate_to]):
            return json.dumps(
                {"error": "task_id  and escalate_to are required"}
            )

        tasks = list(data.get("tasks", {}).values())
        escalations = list(data.get("escalations", {}).values())

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            return json.dumps({"error": f"Task '{task_id}' not found"})

        if task.get("escalated"):
            return json.dumps(
                {
                    "success": True,
                    "already_escalated": True,
                    "message": f"Task '{task_id}' is already escalated",
                    "existing_escalation_id": task.get("escalation_id"),
                    # "escalation_created": False,
                }
            )

        escalation = {
            "escalation_id": f"esc_{uuid.uuid4().hex[:8]}",
            "task_id": task_id,
            "escalated_by": task.get("assignee_id"),
            "escalated_to": escalate_to,
            "previous_status": task.get("status"),
            "created_date": datetime.now().isoformat(),
            "resolved": False,
        }
        escalations.append(escalation)

        if task.get("priority") != "critical":
            task["previous_priority"] = task.get("priority")
            task["priority"] = "critical"

        task["escalated"] = True
        task["escalation_id"] = escalation["escalation_id"]
        task["updated_date"] = datetime.now().isoformat()

        return json.dumps(
            {
                "success": True,
                "escalation": escalation,
                "task_priority": task["priority"],
                # "escalation_initiated": True,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "escalate_task",
                "description": "Escalate a task to management",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to escalate",
                        },
                        "escalate_to": {
                            "type": "string",
                            "description": "Manager or team lead ID to escalate to",
                        },
                    },
                    "required": ["task_id", "escalate_to"],
                },
            },
        }
