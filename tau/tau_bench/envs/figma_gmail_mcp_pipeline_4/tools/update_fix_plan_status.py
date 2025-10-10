# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateFixPlanStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates fix plan status and manages fix plan lifecycle workflow.
        """
        plan_id = kwargs.get('plan_id')
        new_status = kwargs.get('new_status')
        owner_email = kwargs.get('owner_email')
        delivery_method = kwargs.get('delivery_method')
        delivery_notes = kwargs.get('delivery_notes', '')

        if not all([plan_id, new_status]):
            return json.dumps({"error": "plan_id and new_status are required."})

        # Check validity of status values.
        valid_statuses = ['DRAFTED', 'IN_PROGRESS', 'DELIVERED', 'ARCHIVED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        # Check the delivery method if it has been specified.
        valid_delivery_methods = ['COMMENTS', 'TICKETS', 'PDF']
        if delivery_method and delivery_method not in valid_delivery_methods:
            return json.dumps({"error": f"Invalid delivery_method. Must be one of: {', '.join(valid_delivery_methods)}"})

        fix_plans = data.get('fix_plans', [])

        # Determine the solution strategy.
        plan_found = False
        for plan in fix_plans:
            if plan.get('plan_id') == plan_id:
                plan_found = True
                old_status = plan.get('status')

                # Revise the status of the plan.
                plan['status'] = new_status
                plan['last_updated'] = datetime.now().isoformat()

                # Modify owner if supplied.
                if owner_email:
                    plan['owner_email'] = owner_email

                # Modify the delivery method if available.
                if delivery_method:
                    plan['delivery_method'] = delivery_method

                # Manage logic based on status conditions.
                if new_status == 'DELIVERED':
                    plan['delivered_at'] = datetime.now().isoformat()
                    if delivery_notes:
                        plan['delivery_notes'] = delivery_notes

                elif new_status == 'ARCHIVED':
                    plan['archived_at'] = datetime.now().isoformat()
                    if delivery_notes:
                        plan['archive_reason'] = delivery_notes

                # Record the status update.
                if 'status_history' not in plan:
                    plan['status_history'] = []
                plan['status_history'].append({
                    "from_status": old_status,
                    "to_status": new_status,
                    "changed_at": datetime.now().isoformat(),
                    "notes": delivery_notes,
                    "delivery_method": delivery_method
                })

                break

        if not plan_found:
            return json.dumps({"error": f"Fix plan with ID '{plan_id}' not found."})

        return json.dumps({
            "success": True,
            "plan_id": plan_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_fix_plan_status",
                "description": "Updates fix plan status and manages fix plan lifecycle workflow including delivery method and ownership tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string", "description": "The ID of the fix plan to update."},
                        "new_status": {"type": "string", "description": "The new status for the fix plan. Must be one of: DRAFTED, IN_PROGRESS, DELIVERED, ARCHIVED."},
                        "owner_email": {"type": "string", "description": "Optional updated owner email address."},
                        "delivery_method": {"type": "string", "description": "Optional delivery method. Must be one of: COMMENTS, TICKETS, PDF."},
                        "delivery_notes": {"type": "string", "description": "Optional notes about the delivery or status change."}
                    },
                    "required": ["plan_id", "new_status"]
                }
            }
        }
