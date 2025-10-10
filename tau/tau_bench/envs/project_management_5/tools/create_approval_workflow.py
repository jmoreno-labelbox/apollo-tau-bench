# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateApprovalWorkflow(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        workflow_type = kwargs.get("workflow_type", "standard")

        if not cr_id:
            return json.dumps({"error": "cr_id is required"})

        change_requests = data.get("change_requests", [])
        approval_workflows = data.get("approval_workflows", [])
        stakeholders = data.get("stakeholders", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        existing = [i for i in range(len(approval_workflows)) if approval_workflows[i].get("cr_id") == cr_id]
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
                    (s for s in stakeholders if mapping["role"] in s.get("role", "")),
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

        approval_workflows.append(new_workflow)

        if cr.get("status") == "pending_approval" and not steps:
            cr["status"] = "approved"
            cr["approval_date"] = datetime.now().isoformat()

        return json.dumps({"success": True, "workflow": new_workflow})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_approval_workflow",
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
