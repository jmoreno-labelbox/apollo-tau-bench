# Copyright Sierra

import datetime, uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyResourceLeveling(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id, priority_method = "critical_path", resource_constraints = {}) -> str:

        if not all([project_id, resource_constraints]):
            return json.dumps(
                {"error": "project_id and resource_constraints are required"}
            )

        milestones = list(data.get("milestones", {}).values())
        leveling_results = data.get("leveling_results", [])

        project_milestones = [
            m for m in milestones if m.get("project_id") == project_id
        ]

        if not project_milestones:
            return json.dumps(
                {"error": f"No milestones found for project '{project_id}'"}
            )

        result_id = f"level_{uuid.uuid4().hex[:8]}"

        conflicts_found = 0
        milestones_shifted = 0
        total_extension_days = 0
        leveling_changes = []

        if priority_method == "critical_path":
            project_milestones.sort(
                key=lambda x: (
                    not x.get("is_critical_path", False),
                    x.get("start_date"),
                )
            )
        else:
            project_milestones.sort(key=lambda x: x.get("start_date"))

        for i, milestone in enumerate(project_milestones):

            if (
                milestone.get("is_critical_path")
                and milestone.get("resource_allocation", 100) < 100
            ):
                return json.dumps(
                    {
                        "error": f"Critical path milestone '{milestone.get('milestone_name')}' cannot have resource allocation below 100%"
                    }
                )

            if i % 3 == 0 and milestones_shifted < 3:

                if (
                    milestone.get("is_critical_path")
                    and priority_method == "critical_path"
                ):
                    continue

                conflicts_found += 1
                shift_days = 7 * (milestones_shifted + 1)

                old_start = datetime.fromisoformat(
                    milestone.get("start_date").replace("Z", "+00:00")
                )
                old_end = datetime.fromisoformat(
                    milestone.get("target_date").replace("Z", "+00:00")
                )

                new_start = old_start + timedelta(days=shift_days)
                new_end = old_end + timedelta(days=shift_days)

                leveling_changes.append(
                    {
                        "milestone_id": milestone.get("milestone_id"),
                        "milestone_name": milestone.get("milestone_name"),
                        "original_start": milestone.get("start_date"),
                        "original_end": milestone.get("target_date"),
                        "new_start": new_start.isoformat(),
                        "new_end": new_end.isoformat(),
                        "shift_days": shift_days,
                        "is_critical_path": milestone.get("is_critical_path", False),
                    }
                )

                milestones_shifted += 1
                total_extension_days = max(total_extension_days, shift_days)

        project_duration = 180
        extension_percentage = (total_extension_days / project_duration) * 100

        requires_approval = extension_percentage > 10 or total_extension_days > 30

        new_result = {
            "extension_percentage": round(extension_percentage, 1),
            "result_id": result_id,
            "project_id": project_id,
            "resource_constraints": resource_constraints,
            "priority_method": priority_method,
            "conflicts_found": conflicts_found,
            "milestones_shifted": milestones_shifted,
            "total_extension_days": total_extension_days,
            "extension_percentage": round(extension_percentage, 1),
            "requires_approval": requires_approval,
            "leveling_changes": leveling_changes,
            "created_date": datetime.now(timezone.utc).isoformat(),
        }

        leveling_results.append(new_result)

        return json.dumps(
            {
                "success": True,
                "leveling_result": new_result,
                "requires_approval": requires_approval,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_resource_leveling",
                "description": "Apply resource leveling to resolve resource conflicts",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "resource_constraints": {
                            "type": "object",
                            "description": "Resource constraints (e.g., {'Senior Developer': 2})",
                        },
                        "priority_method": {
                            "type": "string",
                            "description": "Priority method: critical_path, business_value",
                        },
                    },
                    "required": ["project_id", "resource_constraints"],
                },
            },
        }
