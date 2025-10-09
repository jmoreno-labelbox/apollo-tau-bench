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

class MergeChangeRequests(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], primary_cr_id: str = None, secondary_cr_ids: list = None, merged_by: str = None) -> str:
        if secondary_cr_ids is None:
            secondary_cr_ids = []

        if not all([primary_cr_id, secondary_cr_ids, merged_by]):
            payload = {"error": "primary_cr_id, secondary_cr_ids, and merged_by are required"}
            out = json.dumps(
                payload)
            return out

        change_requests = data.get("change_requests", {}).values()
        change_history = data.get("change_history", {}).values()

        primary_cr = next(
            (c for c in change_requests.values() if c.get("cr_id") == primary_cr_id), None
        )
        if not primary_cr:
            payload = {"error": f"Primary change request '{primary_cr_id}' not found"}
            out = json.dumps(
                payload)
            return out

        project_id = primary_cr.get("project_id")
        merged_deliverables = set(primary_cr.get("affected_deliverables", []))
        merged_justifications = [primary_cr.get("business_justification")]

        for cr_id in secondary_cr_ids:
            secondary_cr = next(
                (c for c in change_requests.values() if c.get("cr_id") == cr_id), None
            )
            if not secondary_cr:
                payload = {"error": f"Secondary change request '{cr_id}' not found"}
                out = json.dumps(
                    payload)
                return out

            if secondary_cr.get("project_id") != project_id:
                payload = {"error": "All change requests must be for the same project"}
                out = json.dumps(
                    payload)
                return out

            merged_deliverables.update(secondary_cr.get("affected_deliverables", []))
            merged_justifications.append(secondary_cr.get("business_justification"))

            secondary_cr["status"] = "merged"
            secondary_cr["merged_into"] = primary_cr_id
            secondary_cr["merge_date"] = datetime.now().isoformat()

            history_entry = {
                "history_id": f"hist_ch_{uuid.uuid4().hex[:8]}",
                "cr_id": cr_id,
                "action": "merged",
                "merged_into": primary_cr_id,
                "performed_by": merged_by,
                "timestamp": datetime.now().isoformat(),
            }
            data["change_history"][history_entry["change_history_id"]] = history_entry

        primary_cr["affected_deliverables"] = list(merged_deliverables)
        primary_cr["business_justification"] = (
            f"{primary_cr.get('business_justification')}. MERGED: {'; '.join(merged_justifications[1:])}"
        )
        primary_cr["merged_from"] = secondary_cr_ids
        primary_cr["merge_date"] = datetime.now().isoformat()

        if len(secondary_cr_ids) >= 2 and primary_cr.get("priority") == "medium":
            primary_cr["priority"] = "high"
        payload = {
                "success": True,
                "merge_result": {
                    "primary_cr": primary_cr_id,
                    "merged_crs": secondary_cr_ids,
                    "total_affected_deliverables": len(merged_deliverables),
                    "new_priority": primary_cr.get("priority"),
                },
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MergeChangeRequests",
                "description": "Merge duplicate or related change requests",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "primary_cr_id": {
                            "type": "string",
                            "description": "Primary CR to merge into",
                        },
                        "secondary_cr_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "CRs to merge into primary",
                        },
                        "merged_by": {
                            "type": "string",
                            "description": "Person performing the merge",
                        },
                    },
                    "required": [
                        "primary_cr_id",
                        "secondary_cr_ids",
                        "merged_by",
                    ],
                },
            },
        }
