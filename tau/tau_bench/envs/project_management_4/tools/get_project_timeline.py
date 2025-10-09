from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

class GetProjectTimeline(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        include_dependencies: bool = True
    ) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", [])
        milestone_dependencies = data.get("milestone_dependencies", [])
        projects = data.get("projects", [])

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project '{project_id}' not found"}
            out = json.dumps(payload)
            return out

        project_milestones = [
            m for m in milestones if m.get("project_id") == project_id
        ]

        project_milestones.sort(key=lambda x: x.get("start_date"))

        timeline = {
            "project_id": project_id,
            "project_name": project.get("name"),
            "project_start": project.get("start_date"),
            "project_end": project.get("end_date"),
            "milestones": [],
        }

        for milestone in project_milestones:
            milestone_info = {
                "milestone_id": milestone.get("milestone_id"),
                "milestone_name": milestone.get("milestone_name"),
                "type": milestone.get("milestone_type"),
                "start_date": milestone.get("start_date"),
                "target_date": milestone.get("target_date"),
                "status": milestone.get("status"),
                "health": milestone.get("health"),
                "progress": milestone.get("progress_percentage"),
                "is_critical_path": milestone.get("is_critical_path"),
                "resource_allocation": milestone.get("resource_allocation", 100),
                "gate_criteria_defined": (
                    bool(milestone.get("gate_criteria"))
                    if milestone.get("milestone_type") == "major"
                    else None
                ),
            }

            if include_dependencies:
                deps = []
                for dep in milestone_dependencies:
                    if dep.get("successor_id") == milestone.get("milestone_id"):
                        deps.append(
                            {
                                "predecessor_id": dep.get("predecessor_id"),
                                "type": dep.get("dependency_type"),
                                "lag_days": dep.get("lag_days"),
                                "zero_lag": dep.get("zero_lag", False),
                            }
                        )
                milestone_info["dependencies"] = deps

            timeline["milestones"].append(milestone_info)

        if project_milestones:
            earliest_start = min(m.get("start_date") for m in project_milestones)
            latest_end = max(m.get("target_date") for m in project_milestones)

            timeline["timeline_metrics"] = {
                "total_milestones": len(project_milestones),
                "completed": len(
                    [m for m in project_milestones if m.get("status") == "completed"]
                ),
                "in_progress": len(
                    [m for m in project_milestones if m.get("status") == "in_progress"]
                ),
                "delayed": len(
                    [m for m in project_milestones if m.get("status") == "delayed"]
                ),
                "critical_path_count": len(
                    [m for m in project_milestones if m.get("is_critical_path")]
                ),
                "timeline_span": f"{earliest_start} to {latest_end}",
                "major_milestones_without_criteria": len(
                    [
                        m
                        for m in project_milestones
                        if m.get("milestone_type") == "major"
                        and not m.get("gate_criteria")
                    ]
                ),
            }
        payload = timeline
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectTimeline",
                "description": "Get complete timeline view of a project with all milestones",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "include_dependencies": {
                            "type": "boolean",
                            "description": "Include dependency information",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }
