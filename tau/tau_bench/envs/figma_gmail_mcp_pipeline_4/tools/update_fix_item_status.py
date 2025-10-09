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

class UpdateFixItemStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        fix_item_id: str,
        new_status: str,
        assignee_id: str = None,
        implementation_notes: str = "",
        completion_date: str = None,
        updated_by: str = None,
        notes: str = None
    ) -> str:
        # Support updated_by as alternative to assignee_id
        if updated_by is not None:
            assignee_id = updated_by
        # Support notes as alternative to implementation_notes
        if notes is not None:
            implementation_notes = notes
        """
        Modifies the status of a fix item and oversees the lifecycle of the fix plan.
        """
        if not all([fix_item_id, new_status]):
            payload = {"error": "fix_item_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Check the correctness of status values
        valid_statuses = ["PENDING", "IN_PROGRESS", "APPLIED", "DEFERRED", "VERIFIED"]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        fix_items = data.get("fix_items", [])
        fix_plans = data.get("fix_plans", [])

        # Locate the fix item
        item_found = False
        for item in fix_items:
            if item.get("item_id") == fix_item_id:
                item_found = True
                old_status = item.get("status")

                # Change the status of the item
                item["status"] = new_status
                item["last_updated"] = datetime.now().isoformat()

                # Manage logic based on status
                if new_status == "IN_PROGRESS" and assignee_id:
                    item["assignee_id"] = assignee_id
                    item["started_at"] = datetime.now().isoformat()

                elif new_status == "APPLIED":
                    item["completion_date"] = (
                        completion_date or datetime.now().isoformat()
                    )
                    if implementation_notes:
                        item["implementation_notes"] = implementation_notes

                elif new_status == "DEFERRED":
                    item["deferred_at"] = datetime.now().isoformat()
                    if implementation_notes:
                        item["deferral_reason"] = implementation_notes

                elif new_status == "VERIFIED":
                    item["verified_at"] = datetime.now().isoformat()
                    if implementation_notes:
                        item["verification_notes"] = implementation_notes

                # Modify the progress of the fix plan
                plan_id = item.get("plan_id")
                if plan_id:
                    for plan in fix_plans:
                        if plan.get("plan_id") == plan_id:
                            # Reassess the completion percentage
                            plan_items = [
                                i for i in fix_items if i.get("plan_id") == plan_id
                            ]
                            completed_items = [
                                i
                                for i in plan_items
                                if i.get("status") in ["APPLIED", "VERIFIED"]
                            ]
                            completion_percentage = (
                                (len(completed_items) / len(plan_items)) * 100
                                if plan_items
                                else 0
                            )

                            plan["completion_percentage"] = round(
                                completion_percentage, 2
                            )
                            plan["last_updated"] = datetime.now().isoformat()

                            # Change the plan status if all items are finished
                            if completion_percentage == 100:
                                plan["status"] = "COMPLETED"
                                plan["completed_at"] = datetime.now().isoformat()
                            elif completion_percentage > 0:
                                plan["status"] = "IN_PROGRESS"

                            break

                # Document the change in status
                if "status_history" not in item:
                    item["status_history"] = []
                item["status_history"].append(
                    {
                        "from_status": old_status,
                        "to_status": new_status,
                        "changed_by": assignee_id,
                        "changed_at": datetime.now().isoformat(),
                        "notes": implementation_notes,
                    }
                )

                break

        if not item_found:
            payload = {"error": f"Fix item with ID '{fix_item_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "fix_item_id": fix_item_id,
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
                "name": "UpdateFixItemStatus",
                "description": "Updates the status of a fix item and manages the fix plan lifecycle, including assignment, implementation, and verification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "fix_item_id": {
                            "type": "string",
                            "description": "The ID of the fix item to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the fix item. Must be one of: PENDING, IN_PROGRESS, APPLIED, DEFERRED, VERIFIED.",
                        },
                        "assignee_id": {
                            "type": "string",
                            "description": "The ID of the person assigned to work on the fix item.",
                        },
                        "implementation_notes": {
                            "type": "string",
                            "description": "Optional notes about the implementation, deferral reason, or verification.",
                        },
                        "completion_date": {
                            "type": "string",
                            "description": "Optional completion date in ISO format. If not provided, current timestamp will be used.",
                        },
                    },
                    "required": ["fix_item_id", "new_status"],
                },
            },
        }
