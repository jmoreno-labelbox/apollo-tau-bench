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

class CreateApprovalWorkflow(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cr_id: str,
        workflow_type: str = "standard"
    ) -> str:
        if not cr_id:
            payload = {"error": "cr_id is required"}
            out = json.dumps(payload)
            return out

        change_requests = data.get("change_requests", {}).values()
        approval_workflows = data.get("approval_workflows", {}).values()
        stakeholders = data.get("stakeholders", {}).values()

        cr = next((c for c in change_requests.values() if c.get("cr_id") == cr_id), None)
        if not cr:
            payload = {"error": f"Change request '{cr_id}' not found"}
            out = json.dumps(payload)
            return out

        existing = [
            i
            for i in range(len(approval_workflows))
            if approval_workflows[i].get("cr_id") == cr_id
        ]
        for drop_index in existing:
            approval_workflows.pop(drop_index)

        steps = []
        step_number = 1

        approval_mapping = {
            "project_manager": {"role": "project_manager", "can_delegate": True},
            "technical_lead": {"role": "technical_lead", "can_delegate": True},
            "finance": {"role": "finance_director", "can_delegate": False},
            "pmo_director": {"role": "pmo_director", "can_delegate": True},
            "executive_sponsor": {"role": "executive_sponsor", "can_delegate": False},
        }

        for approval_level in cr.get("approvals_required", []):
            if approval_level in approval_mapping:
                mapping = approval_mapping[approval_level]

                approver = next(
                    (s for s in stakeholders.values() if mapping["role"] in s.get("role", "")),
                    None,
                )

                if approver:
                    steps.append(
                        {
                            "step_number": step_number,
                            "approval_level": approval_level,
                            "approver_id": approver.get("stakeholder_id"),
                            "status": "pending",
                            "required": True,
                            "can_delegate": mapping["can_delegate"],
                        }
                    )
                    step_number += 1

        workflow_id = f"wf_{uuid.uuid4().hex[:8]}"

        new_workflow = {
            "workflow_id": workflow_id,
            "cr_id": cr_id,
            "workflow_type": workflow_type,
            "steps": steps,
            "current_step": 1,
            "status": "active",
            "created_date": datetime.now().isoformat(),
        }

        data["approval_workflows"][new_workflow["approval_workflow_id"]] = new_workflow

        if cr.get("status") == "pending_approval" and not steps:
            cr["status"] = "approved"
            cr["approval_date"] = datetime.now().isoformat()
        payload = {"success": True, "workflow": new_workflow}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateApprovalWorkflow",
                "description": "Create approval workflow for a change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "workflow_type": {
                            "type": "string",
                            "description": "Workflow type: standard, expedited, emergency",
                        },
                    },
                    "required": ["cr_id"],
                },
            },
        }
