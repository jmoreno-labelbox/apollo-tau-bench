# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateMilestoneReadiness(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], milestone_id) -> str:

        if not milestone_id:
            return json.dumps({"error": "milestone_id is required"})

        milestones = list(data.get("milestones", {}).values())
        milestone_dependencies = data.get("milestone_dependencies", [])
        external_dependencies = data.get("external_dependencies", [])

        milestone = next(
            (m for m in milestones if m.get("milestone_id") == milestone_id), None
        )
        if not milestone:
            return json.dumps({"error": f"Milestone '{milestone_id}' not found"})

        readiness_issues = []

        if milestone.get("milestone_type") == "major":
            if not milestone.get("gate_criteria"):
                readiness_issues.append(
                    {
                        "type": "missing_gate_criteria",
                        "message": "Major milestones must have defined gate criteria before start date",
                    }
                )
            else:

                start_date = datetime.fromisoformat(
                    milestone.get("start_date").replace("Z", "+00:00")
                )
                if datetime.now(timezone.utc) >= start_date and not milestone.get(
                    "gate_criteria"
                ):
                    readiness_issues.append(
                        {
                            "type": "late_gate_criteria",
                            "message": "Gate criteria must be defined before milestone start date",
                        }
                    )

        predecessor_deps = [
            d for d in milestone_dependencies if d.get("successor_id") == milestone_id
        ]
        for dep in predecessor_deps:
            if dep.get("is_mandatory"):
                pred_milestone = next(
                    (
                        m
                        for m in milestones
                        if m.get("milestone_id") == dep.get("predecessor_id")
                    ),
                    None,
                )
                if pred_milestone and pred_milestone.get("status") != "completed":
                    readiness_issues.append(
                        {
                            "type": "incomplete_predecessor",
                            "milestone_id": pred_milestone.get("milestone_id"),
                            "milestone_name": pred_milestone.get("milestone_name"),
                            "status": pred_milestone.get("status"),
                        }
                    )

        ext_deps = [
            d for d in external_dependencies if d.get("milestone_id") == milestone_id
        ]
        for ext_dep in ext_deps:
            if ext_dep.get("status") not in ["delivered", "confirmed"]:
                readiness_issues.append(
                    {
                        "type": "pending_external_dependency",
                        "dependency_name": ext_dep.get("dependency_name"),
                        "provider": ext_dep.get("provider"),
                        "status": ext_dep.get("status"),
                        "expected_date": ext_dep.get("expected_delivery_date"),
                    }
                )

        deliverables = milestone.get("deliverables", [])
        if deliverables and milestone.get("progress_percentage", 0) < 90:
            readiness_issues.append(
                {
                    "type": "incomplete_deliverables",
                    "progress_percentage": milestone.get("progress_percentage"),
                    "deliverables_count": len(deliverables),
                }
            )

        if milestone.get("status") == "not_started" and milestone.get("owner_id"):
            if (
                milestone.get("is_critical_path")
                and milestone.get("resource_allocation", 100) < 100
            ):
                readiness_issues.append(
                    {
                        "type": "insufficient_resource_allocation",
                        "current_allocation": milestone.get("resource_allocation"),
                        "message": "Critical path tasks require 100% resource allocation",
                    }
                )

        is_ready = len(readiness_issues) == 0

        return json.dumps(
            {
                "milestone_id": milestone_id,
                "milestone_name": milestone.get("milestone_name"),
                "milestone_type": milestone.get("milestone_type"),
                "is_ready": is_ready,
                "readiness_issues": readiness_issues,
                "readiness_score": max(0, 100 - (len(readiness_issues) * 25)),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_milestone_readiness",
                "description": "Validate if a milestone is ready to start based on dependencies and prerequisites",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID to validate",
                        }
                    },
                    "required": ["milestone_id"],
                },
            },
        }
