from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateFixPlanStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        plan_id: str = None,
        new_status: str = None,
        owner_email: str = None,
        delivery_method: str = None,
        delivery_notes: str = "",
        notes: str = None
    ) -> str:
        # Support notes as alternative to delivery_notes
        if notes is not None:
            delivery_notes = notes
        """
        Changes fix plan status and oversees the lifecycle workflow of the fix plan.
        """
        if not all([plan_id, new_status]):
            payload = {"error": "plan_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Check the validity of status values
        valid_statuses = ["DRAFTED", "IN_PROGRESS", "DELIVERED", "ARCHIVED"]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        # Check the correctness of delivery method if specified
        valid_delivery_methods = ["COMMENTS", "TICKETS", "PDF"]
        if delivery_method and delivery_method not in valid_delivery_methods:
            payload = {
                "error": f"Invalid delivery_method. Must be one of: {', '.join(valid_delivery_methods)}"
            }
            out = json.dumps(payload)
            return out

        fix_plans = data.get("fix_plans", [])

        # Locate the fix plan
        plan_found = False
        for plan in fix_plans:
            if plan.get("plan_id") == plan_id:
                plan_found = True
                old_status = plan.get("status")

                # Change the status of the plan
                plan["status"] = new_status
                plan["last_updated"] = datetime.now().isoformat()

                # Revise owner if specified
                if owner_email:
                    plan["owner_email"] = owner_email

                # Change delivery method if supplied
                if delivery_method:
                    plan["delivery_method"] = delivery_method

                # Manage logic based on status
                if new_status == "DELIVERED":
                    plan["delivered_at"] = datetime.now().isoformat()
                    if delivery_notes:
                        plan["delivery_notes"] = delivery_notes

                elif new_status == "ARCHIVED":
                    plan["archived_at"] = datetime.now().isoformat()
                    if delivery_notes:
                        plan["archive_reason"] = delivery_notes

                # Document the change in status
                if "status_history" not in plan:
                    plan["status_history"] = []
                plan["status_history"].append(
                    {
                        "from_status": old_status,
                        "to_status": new_status,
                        "changed_at": datetime.now().isoformat(),
                        "notes": delivery_notes,
                        "delivery_method": delivery_method,
                    }
                )

                break

        if not plan_found:
            payload = {"error": f"Fix plan with ID '{plan_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "plan_id": plan_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFixPlanStatus",
                "description": "Updates fix plan status and manages fix plan lifecycle workflow including delivery method and ownership tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The ID of the fix plan to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the fix plan. Must be one of: DRAFTED, IN_PROGRESS, DELIVERED, ARCHIVED.",
                        },
                        "owner_email": {
                            "type": "string",
                            "description": "Optional updated owner email address.",
                        },
                        "delivery_method": {
                            "type": "string",
                            "description": "Optional delivery method. Must be one of: COMMENTS, TICKETS, PDF.",
                        },
                        "delivery_notes": {
                            "type": "string",
                            "description": "Optional notes about the delivery or status change.",
                        },
                    },
                    "required": ["plan_id", "new_status"],
                },
            },
        }
