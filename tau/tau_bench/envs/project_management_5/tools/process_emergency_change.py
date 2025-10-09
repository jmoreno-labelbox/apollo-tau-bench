from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta
from typing import Any

class ProcessEmergencyChange(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cr_id: str,
        authorized_by: str,
        emergency_type: str,
        justification: str,
        log_id: str = None
    ) -> str:
        if not all([cr_id, authorized_by, emergency_type, justification]):
            payload = {
                "error": "cr_id, authorized_by, emergency_type, and justification are required"
            }
            out = json.dumps(payload)
            return out

        change_requests = data.get("change_requests", [])
        emergency_logs = data.get("emergency_logs", [])
        approval_workflows = data.get("approval_workflows", [])
        stakeholders = data.get("stakeholders", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            payload = {"error": f"Change request '{cr_id}' not found"}
            out = json.dumps(payload)
            return out

        authorizer = next(
            (s for s in stakeholders if s.get("stakeholder_id") == authorized_by), None
        )
        if not authorizer or "emergency" not in str(
            authorizer.get("approval_authority", [])
        ):
            if not authorizer or authorizer.get("role") not in [
                "executive_sponsor",
                "pmo_director",
            ]:
                payload = {"error": "Authorizer does not have emergency approval authority"}
                out = json.dumps(payload)
                return out

        current_time = datetime.now()
        documentation_deadline = (current_time + timedelta(hours=24)).isoformat()
        retroactive_approval_deadline = (current_time + timedelta(hours=48)).isoformat()

        log_id = log_id or f"elog_{uuid.uuid4().hex[:8]}"

        emergency_log = {
            "log_id": log_id,
            "cr_id": cr_id,
            "authorized_by": authorized_by,
            "emergency_type": emergency_type,
            "justification": justification,
            "timestamp": current_time.isoformat(),
            "documentation_deadline": documentation_deadline,
            "retroactive_approval_deadline": retroactive_approval_deadline,
            "retroactive_status": "pending",
            "retroactive_approvers": [],
            "requires_automatic_rollback": True,
        }

        emergency_logs.append(emergency_log)

        cr["status"] = "approved"
        cr["approval_date"] = current_time.isoformat()
        cr["requires_emergency_approval"] = True
        cr["emergency_log_id"] = log_id
        cr["emergency_documentation_deadline"] = documentation_deadline
        cr["emergency_retroactive_deadline"] = retroactive_approval_deadline

        workflow_id = f"wf_{uuid.uuid4().hex[:8]}"

        emergency_workflow = {
            "workflow_id": workflow_id,
            "cr_id": cr_id,
            "workflow_type": "emergency",
            "steps": [
                {
                    "step_number": 1,
                    "approval_level": "emergency_approver",
                    "approver_id": authorized_by,
                    "status": "approved",
                    "required": True,
                    "can_delegate": False,
                    "action_date": current_time.isoformat(),
                }
            ],
            "current_step": 1,
            "status": "completed",
            "created_date": current_time.isoformat(),
            "retroactive_approval_required": True,
            "retroactive_deadline": retroactive_approval_deadline,
        }

        approval_workflows.append(emergency_workflow)
        payload = {
            "success": True,
            "emergency_approval": {
                "cr_id": cr_id,
                "log_id": log_id,
                "status": "approved",
                "requires_retroactive_approval": True,
                "documentation_deadline": documentation_deadline,
                "retroactive_approval_deadline": retroactive_approval_deadline,
                "warning": "Must be documented within 24 hours and receive retroactive approval within 48 hours or automatic rollback will be triggered",
            },
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessEmergencyChange",
                "description": "Process an emergency change request with expedited approval",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "log_id": {"type": "string", "description": "Log ID"},
                        "authorized_by": {
                            "type": "string",
                            "description": "Emergency authorizer ID",
                        },
                        "emergency_type": {
                            "type": "string",
                            "description": "Type: production_fix, security_patch, compliance_requirement, data_integrity",
                        },
                        "justification": {
                            "type": "string",
                            "description": "Emergency justification",
                        },
                    },
                    "required": [
                        "cr_id",
                        "authorized_by",
                        "emergency_type",
                        "justification",
                    ],
                },
            },
        }
