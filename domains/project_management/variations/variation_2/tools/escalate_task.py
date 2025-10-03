from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class EscalateTask(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, escalate_to: str = None) -> str:
        if not all([task_id, escalate_to]):
            payload = {"error": "task_id  and escalate_to are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])
        escalations = data.get("escalations", [])

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out

        if task.get("escalated"):
            payload = {
                    "success": True,
                    "already_escalated": True,
                    "message": f"Task '{task_id}' is already escalated",
                    "existing_escalation_id": task.get("escalation_id"),
                    #"new_escalation_created": False,
                }
            out = json.dumps(
                payload)
            return out

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
        payload = {
                "success": True,
                "escalation": escalation,
                "task_priority": task["priority"],
                #"new_escalation_created": True,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EscalateTask",
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
