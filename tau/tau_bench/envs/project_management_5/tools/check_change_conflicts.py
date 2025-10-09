from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta
from typing import Any

class CheckChangeConflicts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cr_id: str = None, compare_to_cr_id: str = None) -> str:
        if not cr_id:
            payload = {"error": "cr_id is required"}
            out = json.dumps(payload)
            return out

        change_requests = data.get("change_requests", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            payload = {"error": f"Change request '{cr_id}' not found"}
            out = json.dumps(payload)
            return out

        project_id = cr.get("project_id")
        conflicts = []

        if compare_to_cr_id:
            active_crs = [
                c
                for c in change_requests
                if c.get("project_id") == project_id
                and c.get("cr_id") == compare_to_cr_id
                and c.get("status")
                in ["pending_approval", "in_review", "approved", "draft"]
            ]
        else:
            active_crs = [
                c
                for c in change_requests
                if c.get("project_id") == project_id
                and c.get("cr_id") != cr_id
                and c.get("status")
                in ["pending_approval", "in_review", "approved", "draft"]
            ]

        cr_deliverables = set(cr.get("affected_deliverables", []))
        for other_cr in active_crs:
            other_deliverables = set(other_cr.get("affected_deliverables", []))
            if overlap := cr_deliverables.intersection(other_deliverables):
                conflicts.append(
                    {
                        "type": "deliverable_conflict",
                        "conflicting_cr": other_cr.get("cr_id"),
                        "conflicting_deliverables": list(overlap),
                        "severity": "critical",
                        "rule_violation": "Multiple change requests affecting the same deliverable must be consolidated",
                        "action_required": "Merge with existing CR or wait for completion",
                    }
                )

        if impact := cr.get("impact_assessment"):
            cr_resources = {
                r.get("employee_id") for r in impact.get("resource_requirements", [])
            }

            for other_cr in active_crs:
                if other_impact := other_cr.get("impact_assessment"):
                    other_resources = {
                        r.get("employee_id")
                        for r in other_impact.get("resource_requirements", [])
                    }
                    if resource_overlap := cr_resources.intersection(other_resources):
                        conflicts.append(
                            {
                                "type": "resource_conflict",
                                "conflicting_cr": other_cr.get("cr_id"),
                                "conflicting_resources": list(resource_overlap),
                                "severity": "medium",
                            }
                        )

        if cr.get("change_type") == "schedule_change":
            for other_cr in active_crs:
                if other_cr.get("change_type") == "schedule_change":
                    conflicts.append(
                        {
                            "type": "schedule_conflict",
                            "conflicting_cr": other_cr.get("cr_id"),
                            "description": "Multiple schedule changes pending",
                            "severity": "high",
                        }
                    )

        if cr.get("change_type") in ["scope_addition", "scope_reduction"]:
            opposite_type = (
                "scope_reduction"
                if cr.get("change_type") == "scope_addition"
                else "scope_addition"
            )
            for other_cr in active_crs:
                if other_cr.get("change_type") == opposite_type:
                    conflicts.append(
                        {
                            "type": "scope_conflict",
                            "conflicting_cr": other_cr.get("cr_id"),
                            "description": "Conflicting scope changes (addition vs reduction)",
                            "severity": "critical",
                        }
                    )

        has_rule_violations = any(c.get("rule_violation") for c in conflicts)
        payload = {
                "cr_id": cr_id,
                "conflicts_found": len(conflicts),
                "has_rule_violations": has_rule_violations,
                "conflicts": conflicts,
                "recommendation": (
                    "Cannot proceed - consolidate with conflicting CRs"
                    if has_rule_violations
                    else (
                        "Coordinate with conflicting CRs"
                        if conflicts
                        else "No conflicts found"
                    )
                ),
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
                "name": "CheckChangeConflicts",
                "description": "Check for conflicts with other change requests",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {
                            "type": "string",
                            "description": "Change request ID to check",
                        },
                        "compare_to_cr_id": {
                            "type": "string",
                            "description": "Change request ID to compare with cr_id",
                        },
                    },
                    "required": ["cr_id"],
                },
            },
        }
