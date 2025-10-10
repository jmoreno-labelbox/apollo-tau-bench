# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EscalateChangeRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cr_id, escalate_to_level, escalated_by) -> str:

        if not all([cr_id, escalate_to_level, escalated_by]):
            return json.dumps(
                {
                    "error": "cr_id, escalate_to_level, and escalated_by are required"
                }
            )

        change_requests = list(data.get("change_requests", {}).values())
        approval_workflows = list(data.get("approval_workflows", {}).values())
        change_history = list(data.get("change_history", {}).values())

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

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
                for w in approval_workflows
                if w.get("cr_id") == cr_id and w.get("status") == "active"
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
        change_history.append(history_entry)

        return json.dumps(
            {
                "success": True,
                "escalation": {
                    "cr_id": cr_id,
                    "escalated_to": escalate_to_level,
                    "new_priority": cr.get("priority"),
                    "workflow_updated": workflow is not None,
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "escalate_change_request",
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
