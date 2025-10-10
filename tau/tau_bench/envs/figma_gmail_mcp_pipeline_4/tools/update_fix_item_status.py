# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateFixItemStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates the status of a fix item and manages the fix plan lifecycle.
        """
        fix_item_id = kwargs.get('fix_item_id')
        new_status = kwargs.get('new_status')
        assignee_id = kwargs.get('assignee_id')
        implementation_notes = kwargs.get('implementation_notes', '')
        completion_date = kwargs.get('completion_date')

        if not all([fix_item_id, new_status]):
            return json.dumps({"error": "fix_item_id and new_status are required."})

        # Check the validity of status values.
        valid_statuses = ['PENDING', 'IN_PROGRESS', 'APPLIED', 'DEFERRED', 'VERIFIED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        fix_items = data.get('fix_items', [])
        fix_plans = data.get('fix_plans', [])

        # Locate the correction item.
        item_found = False
        for item in fix_items:
            if item.get('item_id') == fix_item_id:
                item_found = True
                old_status = item.get('status')

                # Modify the status of the item.
                item['status'] = new_status
                item['last_updated'] = datetime.now().isoformat()

                # Manage logic based on status conditions.
                if new_status == 'IN_PROGRESS' and assignee_id:
                    item['assignee_id'] = assignee_id
                    item['started_at'] = datetime.now().isoformat()

                elif new_status == 'APPLIED':
                    item['completion_date'] = completion_date or datetime.now().isoformat()
                    if implementation_notes:
                        item['implementation_notes'] = implementation_notes

                elif new_status == 'DEFERRED':
                    item['deferred_at'] = datetime.now().isoformat()
                    if implementation_notes:
                        item['deferral_reason'] = implementation_notes

                elif new_status == 'VERIFIED':
                    item['verified_at'] = datetime.now().isoformat()
                    if implementation_notes:
                        item['verification_notes'] = implementation_notes

                # Revise the progress of the fix plan.
                plan_id = item.get('plan_id')
                if plan_id:
                    for plan in fix_plans:
                        if plan.get('plan_id') == plan_id:
                            # Recompute the completion ratio.
                            plan_items = [i for i in fix_items if i.get('plan_id') == plan_id]
                            completed_items = [i for i in plan_items if i.get('status') in ['APPLIED', 'VERIFIED']]
                            completion_percentage = (len(completed_items) / len(plan_items)) * 100 if plan_items else 0

                            plan['completion_percentage'] = round(completion_percentage, 2)
                            plan['last_updated'] = datetime.now().isoformat()

                            # Change plan status when all items are finished.
                            if completion_percentage == 100:
                                plan['status'] = 'COMPLETED'
                                plan['completed_at'] = datetime.now().isoformat()
                            elif completion_percentage > 0:
                                plan['status'] = 'IN_PROGRESS'

                            break

                # Record the status update.
                if 'status_history' not in item:
                    item['status_history'] = []
                item['status_history'].append({
                    "from_status": old_status,
                    "to_status": new_status,
                    "changed_by": assignee_id,
                    "changed_at": datetime.now().isoformat(),
                    "notes": implementation_notes
                })

                break

        if not item_found:
            return json.dumps({"error": f"Fix item with ID '{fix_item_id}' not found."})

        return json.dumps({
            "success": True,
            "fix_item_id": fix_item_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_fix_item_status",
                "description": "Updates the status of a fix item and manages the fix plan lifecycle, including assignment, implementation, and verification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "fix_item_id": {"type": "string", "description": "The ID of the fix item to update."},
                        "new_status": {"type": "string", "description": "The new status for the fix item. Must be one of: PENDING, IN_PROGRESS, APPLIED, DEFERRED, VERIFIED."},
                        "assignee_id": {"type": "string", "description": "The ID of the person assigned to work on the fix item."},
                        "implementation_notes": {"type": "string", "description": "Optional notes about the implementation, deferral reason, or verification."},
                        "completion_date": {"type": "string", "description": "Optional completion date in ISO format. If not provided, current timestamp will be used."}
                    },
                    "required": ["fix_item_id", "new_status"]
                }
            }
        }
