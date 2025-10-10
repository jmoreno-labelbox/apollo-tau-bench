# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MergeChangeRequests(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        primary_cr_id = kwargs.get("primary_cr_id")
        secondary_cr_ids = kwargs.get("secondary_cr_ids", [])
        merged_by = kwargs.get("merged_by")

        if not all([primary_cr_id, secondary_cr_ids, merged_by]):
            return json.dumps(
                {
                    "error": "primary_cr_id, secondary_cr_ids, and merged_by are required"
                }
            )

        change_requests = data.get("change_requests", [])
        change_history = data.get("change_history", [])

        primary_cr = next(
            (c for c in change_requests if c.get("cr_id") == primary_cr_id), None
        )
        if not primary_cr:
            return json.dumps(
                {"error": f"Primary change request '{primary_cr_id}' not found"}
            )

        project_id = primary_cr.get("project_id")
        merged_deliverables = set(primary_cr.get("affected_deliverables", []))
        merged_justifications = [primary_cr.get("business_justification")]

        for cr_id in secondary_cr_ids:
            secondary_cr = next(
                (c for c in change_requests if c.get("cr_id") == cr_id), None
            )
            if not secondary_cr:
                return json.dumps(
                    {"error": f"Secondary change request '{cr_id}' not found"}
                )

            if secondary_cr.get("project_id") != project_id:
                return json.dumps(
                    {"error": "All change requests must be for the same project"}
                )

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
            change_history.append(history_entry)

        primary_cr["affected_deliverables"] = list(merged_deliverables)
        primary_cr[
            "business_justification"
        ] = f"{primary_cr.get('business_justification')}. MERGED: {'; '.join(merged_justifications[1:])}"
        primary_cr["merged_from"] = secondary_cr_ids
        primary_cr["merge_date"] = datetime.now().isoformat()

        if len(secondary_cr_ids) >= 2 and primary_cr.get("priority") == "medium":
            primary_cr["priority"] = "high"

        return json.dumps(
            {
                "success": True,
                "merge_result": {
                    "primary_cr": primary_cr_id,
                    "merged_crs": secondary_cr_ids,
                    "total_affected_deliverables": len(merged_deliverables),
                    "new_priority": primary_cr.get("priority"),
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "merge_change_requests",
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
