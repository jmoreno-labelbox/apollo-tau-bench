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

class BulkUpdateChangeStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cr_ids: list = None, new_status: str = None, updated_by: str = None) -> str:
        if cr_ids is None:
            cr_ids = []

        if not all([cr_ids, new_status, updated_by]):
            payload = {"error": "cr_ids, new_status, and updated_by are required"}
            out = json.dumps(
                payload)
            return out

        change_requests = data.get("change_requests", {}).values()
        change_history = data.get("change_history", {}).values()

        results = {"successful": [], "failed": []}

        for cr_id in cr_ids:
            cr = next((c for c in change_requests.values() if c.get("cr_id") == cr_id), None)
            if not cr:
                results["failed"].append({"cr_id": cr_id})
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
            data["change_history"][history_entry["change_history_id"]] = history_entry

            results["successful"].append(
                {"cr_id": cr_id, "old_status": old_status, "new_status": new_status}
            )
        payload = {
                "success": len(results["successful"]) > 0,
                "summary": {
                    "total_requested": len(cr_ids),
                    "successful": len(results["successful"]),
                    "failed": len(results["failed"]),
                },
                "results": results,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BulkUpdateChangeStatus",
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
