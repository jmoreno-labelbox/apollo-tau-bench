from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class EscalateChangeRequest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cr_id: str = None, escalate_to_level: str = None, escalated_by: str = None) -> str:
        if not all([cr_id, escalate_to_level, escalated_by]):
            payload = {"error": "cr_id, escalate_to_level, and escalated_by are required"}
            out = json.dumps(payload)
            return out

        change_requests = data.get("change_requests", {}).values()
        approval_workflows = data.get("approval_workflows", {}).values()
        change_history = data.get("change_history", {}).values()

        cr = next((c for c in change_requests.values() if c.get("cr_id") == cr_id), None)
        if not cr:
            payload = {"error": f"Change request '{cr_id}' not found"}
            out = json.dumps(payload)
            return out

        old_priority = cr.get("priority")
        if escalate_to_level in ["executive", "critical"]:
            cr["priority"] = "critical"
        elif old_priority != "critical":
            cr["priority"] = "high"

        cr["escalated"] = True
        cr["escalation_date"] = datetime.now().isoformat()
        cr["escalated_to"] = escalate_to_level

        workflow = next(
            (
                w
                for w in approval_workflows.values() if w.get("cr_id") == cr_id and w.get("status") == "active"
            ),
            None,
        )
        if workflow:
            if escalate_to_level == "executive":
                new_step = {
                    "step_number": len(workflow.get("steps", [])) + 1,
                    "approval_level": "executive_sponsor",
                    "approver_id": None,
                    "status": "pending",
                    "required": True,
                    "can_delegate": False,
                    "escalated": True,
                }
                workflow["steps"].append(new_step)

                if "executive_sponsor" not in cr.get("approvals_required", []):
                    cr["approvals_required"].append("executive_sponsor")

        history_entry = {
            "history_id": f"hist_ch_{uuid.uuid4().hex[:8]}",
            "cr_id": cr_id,
            "action": "escalated",
            "performed_by": escalated_by,
            "escalation_level": escalate_to_level,
            "priority_change": f"{old_priority} -> {cr.get('priority')}",
            "timestamp": datetime.now().isoformat(),
        }
        data["change_history"][history_entry["change_history_id"]] = history_entry
        payload = {
            "success": True,
            "escalation": {
                "cr_id": cr_id,
                "escalated_to": escalate_to_level,
                "new_priority": cr.get("priority"),
                "workflow_updated": workflow is not None,
            },
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EscalateChangeRequest",
                "description": "Escalate a change request to higher management",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "escalate_to_level": {
                            "type": "string",
                            "description": "Level to escalate to: senior_management, executive, critical",
                        },
                        "escalated_by": {
                            "type": "string",
                            "description": "Person escalating the request",
                        },
                    },
                    "required": [
                        "cr_id",
                        "escalate_to_level",
                        "escalated_by",
                    ],
                },
            },
        }
