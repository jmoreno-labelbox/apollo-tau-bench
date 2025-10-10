# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateRecoveryPlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        milestone_id = kwargs.get("milestone_id")
        recovery_actions = kwargs.get("recovery_actions", [])
        additional_resources = kwargs.get("additional_resources", [])

        if not all([milestone_id, recovery_actions]):
            return json.dumps(
                {"error": "milestone_id and recovery_actions are required"}
            )

        milestones = list(data.get("milestones", {}).values())
        recovery_plans = data.get("recovery_plans", [])

        milestone = next(
            (m for m in milestones if m.get("milestone_id") == milestone_id), None
        )
        if not milestone:
            return json.dumps({"error": f"Milestone '{milestone_id}' not found"})

        if milestone.get("is_critical_path"):
            for resource_id in additional_resources:

                if milestone.get("resource_allocation", 100) < 100:
                    return json.dumps(
                        {
                            "error": "Cannot reduce resource allocation below 100% for critical path tasks"
                        }
                    )

        total_impact_days = sum(
            action.get("impact_days", 0) for action in recovery_actions
        )

        current_target = datetime.fromisoformat(
            milestone.get("target_date").replace("Z", "+00:00")
        )
        recovery_target = current_target - timedelta(days=total_impact_days)

        plan_id = f"recovery_{uuid.uuid4().hex[:8]}"

        created_within_48hrs = (
            milestone.get("status") == "delayed" and milestone.get("health") == "red"
        )

        new_plan = {
            "plan_id": plan_id,
            "milestone_id": milestone_id,
            "milestone_name": milestone.get("milestone_name"),
            "current_target_date": milestone.get("target_date"),
            "recovery_target_date": recovery_target.isoformat(),
            "recovery_days": total_impact_days,
            "recovery_actions": recovery_actions,
            "additional_resources": additional_resources,
            "risk_mitigation": kwargs.get("risk_mitigation", []),
            "total_impact_days": total_impact_days,
            "feasibility": kwargs.get("feasibility", "medium"),
            "created_date": datetime.now(timezone.utc).isoformat(),
            "status": "pending_approval",
            "created_within_48hrs": created_within_48hrs,
            "is_critical_path": milestone.get("is_critical_path", False),
        }

        recovery_plans.append(new_plan)

        return json.dumps(
            {
                "success": True,
                "recovery_plan": new_plan,
                "days_recovered": total_impact_days,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_recovery_plan",
                "description": "Create a recovery plan for a delayed milestone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "recovery_actions": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "type": {
                                        "type": "string",
                                        "description": "Action type: crashing, fast_tracking, resource_addition, scope_reduction",
                                    },
                                    "description": {
                                        "type": "string",
                                        "description": "Action description",
                                    },
                                    "impact_days": {
                                        "type": "number",
                                        "description": "Days recovered",
                                    },
                                },
                            },
                            "description": "List of recovery actions",
                        },
                        "additional_resources": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Additional resource IDs needed",
                        },
                        "risk_mitigation": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Risk mitigation strategies",
                        },
                        "feasibility": {
                            "type": "string",
                            "description": "Feasibility: low, medium, high",
                        },
                    },
                    "required": ["milestone_id", "recovery_actions"],
                },
            },
        }
