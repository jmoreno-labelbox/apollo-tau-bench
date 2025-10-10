# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BulkUpdateChangeStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_status, updated_by, cr_ids = []) -> str:

        if not all([cr_ids, new_status, updated_by]):
            return json.dumps(
                {"error": "cr_ids, new_status, and updated_by are required"}
            )

        change_requests = list(data.get("change_requests", {}).values())
        change_history = list(data.get("change_history", {}).values())

        results = {"successful": [], "failed": []}

        for cr_id in cr_ids:
            cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
            if not cr:
                results["failed"].append(
                    {"cr_id": cr_id}
                )
                continue

            old_status = cr.get("status")

            valid_bulk_transitions = {
                "draft": ["cancelled"],
                "in_review": ["cancelled"],
                "pending_approval": ["on_hold", "cancelled"],
                "on_hold": ["cancelled"],
                "approved": ["in_implementation", "completed"],
                "in_implementation": ["completed"],
            }

            if new_status not in valid_bulk_transitions.get(old_status, []):
                results["failed"].append(
                    {
                        "cr_id": cr_id,
                    }
                )
                continue

            cr["status"] = new_status
            cr["updated_date"] = datetime.now().isoformat()
            cr["bulk_update"] = True

            history_entry = {
                "history_id": f"hist_ch_{uuid.uuid4().hex[:8]}",
                "cr_id": cr_id,
                "action": "bulk_status_change",
                "from_status": old_status,
                "to_status": new_status,
                "performed_by": updated_by,
                "timestamp": datetime.now().isoformat(),
            }
            change_history.append(history_entry)

            results["successful"].append(
                {"cr_id": cr_id, "old_status": old_status, "new_status": new_status}
            )

        return json.dumps(
            {
                "success": len(results["successful"]) > 0,
                "summary": {
                    "total_requested": len(cr_ids),
                    "successful": len(results["successful"]),
                    "failed": len(results["failed"]),
                },
                "results": results,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "bulk_update_change_status",
                "description": "Update status for multiple change requests at once",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of change request IDs",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status to apply",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Person performing the update",
                        },
                    },
                    "required": ["cr_ids", "new_status", "updated_by"],
                },
            },
        }
