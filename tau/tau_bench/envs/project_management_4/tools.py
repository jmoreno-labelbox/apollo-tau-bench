import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class GetMilestoneDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], milestone_id: str = None) -> str:
        if not milestone_id:
            payload = {"error": "milestone_id is required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()
        for milestone in milestones.values():
            if milestone.get("milestone_id") == milestone_id:
                payload = milestone
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Milestone '{milestone_id}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMilestoneDetails",
                "description": "Get detailed information about a specific milestone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "The milestone ID",
                        }
                    },
                    "required": ["milestone_id"],
                },
            },
        }


class CreateMilestone(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        milestone_name: str,
        target_date: str,
        owner_id: str,
        milestone_type: str = "standard",
        description: str = None,
        deliverables: list = None,
        gate_criteria: list = None,
        milestone_id: str = None,
        start_date: str = None
    ) -> str:
        if deliverables is None:
            deliverables = []
        if gate_criteria is None:
            gate_criteria = []
        if milestone_id is None:
            milestone_id = f"ms_{uuid.uuid4().hex[:8]}"

        if not all([project_id, milestone_name, target_date, owner_id]):
            payload = {
                "error": "project_id, milestone_name, target_date, and owner_id are required"
            }
            out = json.dumps(payload)
            return out

        if milestone_type == "major" and not gate_criteria:
            payload = {"error": "Major milestones must have defined gate criteria"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()

        if not start_date:
            target_dt = datetime.fromisoformat(target_date.replace("Z", "+00:00"))
            start_dt = target_dt - timedelta(days=30)
            start_date = start_dt.isoformat()

        start_dt = datetime.fromisoformat(start_date.replace("Z", "+00:00"))
        target_dt = datetime.fromisoformat(target_date.replace("Z", "+00:00"))

        if start_dt >= target_dt:
            payload = {"error": "Start date must be before target date"}
            out = json.dumps(payload)
            return out

        new_milestone = {
            "milestone_id": milestone_id,
            "project_id": project_id,
            "milestone_name": milestone_name,
            "milestone_type": milestone_type,
            "start_date": start_date,
            "target_date": target_date,
            "description": description,
            "deliverables": deliverables,
            "gate_criteria": gate_criteria,
            "owner_id": owner_id,
            "status": "not_started",
            "health": "green",
            "progress_percentage": 0,
            "float_days": 0,
            "is_critical_path": False,
            "buffer_consumed": 0,
            "created_date": datetime.now(timezone.utc).isoformat(),
            "baseline_start": start_date,
            "baseline_target": target_date,
            "resource_allocation": 100,
        }

        data["milestones"][milestone_id] = new_milestone
        payload = {"success": True, "milestone": new_milestone}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMilestone",
                "description": "Create a new project milestone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "milestone_name": {
                            "type": "string",
                            "description": "Name of the milestone",
                        },
                        "milestone_type": {
                            "type": "string",
                            "description": "Type: standard, major, phase_gate",
                        },
                        "target_date": {
                            "type": "string",
                            "description": "Target completion date (ISO format)",
                        },
                        "description": {
                            "type": "string",
                            "description": "Milestone description",
                        },
                        "deliverables": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of deliverables",
                        },
                        "owner_id": {
                            "type": "string",
                            "description": "Owner employee ID",
                        },
                        "gate_criteria": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Gate review criteria (required for major milestones)",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Optional start date",
                        },
                    },
                    "required": [
                        "project_id",
                        "milestone_name",
                        "target_date",
                        "owner_id",
                    ],
                },
            },
        }


class UpdateMilestoneStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        milestone_id: str = None,
        new_status: str = None,
        progress_percentage: int = None,
        health: str = None,
        deliverables_completed: list = None,
        status_notes: str = ""
    ) -> str:
        if deliverables_completed is None:
            deliverables_completed = []

        if not all([milestone_id, new_status]):
            payload = {"error": "milestone_id and new_status are required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()
        milestone_updates = data.get("milestone_updates", {}).values()

        for milestone in milestones.values():
            if milestone.get("milestone_id") == milestone_id:
                milestone.get("status")
                old_health = milestone.get("health")

                if new_status == "completed":
                    start_date = datetime.fromisoformat(
                        milestone.get("start_date").replace("Z", "+00:00")
                    )
                    current_date = datetime.now(timezone.utc)

                    if current_date < start_date:
                        payload = {
                            "error": "Cannot mark milestone as completed before its start date"
                        }
                        out = json.dumps(payload)
                        return out

                    total_deliverables = len(milestone.get("deliverables", []))
                    if total_deliverables > 0:
                        if len(deliverables_completed) < total_deliverables:
                            payload = {
                                "error": f"All {total_deliverables} deliverables must be completed before marking milestone as completed. Only {len(deliverables_completed)} completed."
                            }
                            out = json.dumps(payload)
                            return out

                    milestone["actual_completion_date"] = datetime.now(
                        timezone.utc
                    ).isoformat()
                    milestone["progress_percentage"] = 100
                else:
                    if progress_percentage is not None:
                        milestone["progress_percentage"] = progress_percentage

                milestone["status"] = new_status
                if health:
                    milestone["health"] = health

                update_id = f"upd_{uuid.uuid4().hex[:8]}"
                update_record = {
                    "update_id": update_id,
                    "milestone_id": milestone_id,
                    "progress_percentage": milestone["progress_percentage"],
                    "status": new_status,
                    "status_notes": status_notes,
                    "deliverables_completed": deliverables_completed,
                    "health_change": f"{old_health} -> {milestone['health']}",
                    "updated_date": datetime.now(timezone.utc).isoformat(),
                }
                data["milestone_updates"][update_record["milestone_update_id"]] = update_record
                payload = {"success": True, "milestone": milestone, "update": update_record}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Milestone '{milestone_id}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateMilestoneStatus",
                "description": "Update milestone status, progress, and health",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status: not_started, in_progress, completed, delayed",
                        },
                        "progress_percentage": {
                            "type": "number",
                            "description": "Progress percentage (0-100)",
                        },
                        "health": {
                            "type": "string",
                            "description": "Health status: green, yellow, red",
                        },
                        "status_notes": {
                            "type": "string",
                            "description": "Notes about the update",
                        },
                        "deliverables_completed": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of completed deliverables (required for completion)",
                        },
                    },
                    "required": ["milestone_id", "new_status"],
                },
            },
        }


class CreateMilestoneDependency(Tool):
    @staticmethod
    def _check_circular_dependency(
        data: dict[str, Any], predecessor_id: str, successor_id: str
    ) -> bool:
        """Verify whether including this dependency would result in a circular dependency"""
        pass
        dependencies = data.get("milestone_dependencies", {}).values()

        graph = {}
        for dep in dependencies.values():
            pred = dep.get("predecessor_id")
            succ = dep.get("successor_id")
            if pred not in graph:
                graph[pred] = []
            graph[pred].append(succ)

        if predecessor_id not in graph:
            graph[predecessor_id] = []
        graph[predecessor_id].append(successor_id)

        def has_cycle(node, visited, rec_stack):
            pass
            visited.add(node)
            rec_stack.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if has_cycle(neighbor, visited, rec_stack):
                        return True
                elif neighbor in rec_stack:
                    return True

            rec_stack.remove(node)
            return False

        visited = set()
        for node in graph:
            if node not in visited:
                if has_cycle(node, visited, set()):
                    return True
        return False

    @staticmethod
    def invoke(
        data: dict[str, Any],
        predecessor_id: str,
        successor_id: str,
        dependency_type: str = "finish_to_start",
        lag_days: int = 0,
        is_mandatory: bool = True,
        notes: str = "",
        zero_lag: bool = False
    ) -> str:
        if not all([predecessor_id, successor_id]):
            payload = {"error": "predecessor_id and successor_id are required"}
            out = json.dumps(payload)
            return out

        if predecessor_id == successor_id:
            payload = {"error": "Milestone cannot depend on itself"}
            out = json.dumps(payload)
            return out

        if CreateMilestoneDependency._check_circular_dependency(
            data, predecessor_id, successor_id
        ):
            payload = {"error": "This dependency would create a circular dependency"}
            out = json.dumps(payload)
            return out

        if dependency_type == "finish_to_start" and not zero_lag and lag_days < 1:
            lag_days = 1

        if dependency_type in ["start_to_start", "finish_to_finish"] and not notes:
            payload = {
                    "error": f"{dependency_type} dependencies require justification in the notes field"
                }
            out = json.dumps(payload)
            return out

        milestone_dependencies = data.get("milestone_dependencies", {}).values()
        milestones = data.get("milestones", {}).values()

        pred_exists = any(m.get("milestone_id") == predecessor_id for m in milestones.values())
        succ_exists = any(m.get("milestone_id") == successor_id for m in milestones.values())

        if not pred_exists or not succ_exists:
            payload = {"error": "One or both milestones not found"}
            out = json.dumps(payload)
            return out

        existing = any(
            d.get("predecessor_id") == predecessor_id
            and d.get("successor_id") == successor_id
            for d in milestone_dependencies.values()
        )

        if existing:
            payload = {"error": "Dependency already exists"}
            out = json.dumps(payload)
            return out

        dependency_id = f"dep_{uuid.uuid4().hex[:8]}"

        new_dependency = {
            "dependency_id": dependency_id,
            "predecessor_id": predecessor_id,
            "successor_id": successor_id,
            "dependency_type": dependency_type,
            "lag_days": lag_days,
            "is_mandatory": is_mandatory,
            "notes": notes,
            "zero_lag": zero_lag,
            "created_date": datetime.now(timezone.utc).isoformat(),
        }

        data["milestone_dependencies"][new_dependency["milestone_dependencie_id"]] = new_dependency

        for milestone in milestones.values():
            if milestone.get("milestone_id") == successor_id:
                milestone["is_critical_path"] = True
                break

        project_id = next(
            (
                m.get("project_id")
                for m in milestones.values() if m.get("milestone_id") == predecessor_id
            ),
            None,
        )

        result = {
            "success": True,
            "dependency": new_dependency,
            "critical_path_update_required": True,
            "project_id": project_id,
        }
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMilestoneDependency",
                "description": "Create a dependency between two milestones",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "predecessor_id": {
                            "type": "string",
                            "description": "Predecessor milestone ID",
                        },
                        "successor_id": {
                            "type": "string",
                            "description": "Successor milestone ID",
                        },
                        "dependency_type": {
                            "type": "string",
                            "description": "Dependency type: finish_to_start, start_to_start, finish_to_finish, start_to_finish",
                        },
                        "lag_days": {
                            "type": "number",
                            "description": "Lag time in days (min 1 for F-S unless zero_lag=True)",
                        },
                        "is_mandatory": {
                            "type": "boolean",
                            "description": "Is this a mandatory dependency",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Notes (required for S-S and F-F dependencies)",
                        },
                        "zero_lag": {
                            "type": "boolean",
                            "description": "Allow zero lag for F-S dependencies",
                        },
                    },
                    "required": ["predecessor_id", "successor_id"],
                },
            },
        }


class CalculateCriticalPath(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()
        data.get("milestone_dependencies", {}).values()
        critical_paths = data.get("critical_paths", {}).values()

        project_milestones = [
            m for m in milestones.values() if m.get("project_id") == project_id
        ]

        if not project_milestones:
            payload = {"error": f"No milestones found for project '{project_id}'"}
            out = json.dumps(
                payload)
            return out

        critical_milestone_ids = []
        total_duration = 0

        for milestone in project_milestones.values():
            if milestone.get("float_days", 0) == 0:
                critical_milestone_ids.append(milestone.get("milestone_id"))

                start = datetime.fromisoformat(
                    milestone.get("start_date").replace("Z", "+00:00")
                )
                target = datetime.fromisoformat(
                    milestone.get("target_date").replace("Z", "+00:00")
                )
                duration = (target - start).days
                total_duration = max(total_duration, duration)

            if (
                milestone.get("is_critical_path")
                and milestone.get("is_critical_path") is True
            ):
                critical_milestone_ids.append(milestone.get("milestone_id"))

                start = datetime.fromisoformat(
                    milestone.get("start_date").replace("Z", "+00:00")
                )
                target = datetime.fromisoformat(
                    milestone.get("target_date").replace("Z", "+00:00")
                )
                duration = (target - start).days
                total_duration = max(total_duration, duration)

        path_id = f"cp_{uuid.uuid4().hex[:8]}"
        existing_path = next(
            (cp for cp in critical_paths.values() if cp.get("project_id") == project_id), None
        )

        if existing_path:
            existing_path["critical_tasks"] = critical_milestone_ids
            existing_path["total_duration_days"] = total_duration
            existing_path["last_calculated"] = datetime.now(timezone.utc).isoformat()
            result = existing_path
        else:
            new_path = {
                "path_id": path_id,
                "project_id": project_id,
                "critical_tasks": critical_milestone_ids,
                "total_duration_days": total_duration,
                "slack_time": 0,
                "last_calculated": datetime.now(timezone.utc).isoformat(),
            }
            data["critical_paths"][new_path["critical_path_id"]] = new_path
            result = new_path
        payload = {
                "success": True,
                "critical_path": result,
                "critical_milestones_count": len(critical_milestone_ids),
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateCriticalPath",
                "description": "Calculate and update the critical path for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"}
                    },
                    "required": ["project_id"],
                },
            },
        }


class CreateScheduleBaseline(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        baseline_name: str,
        baseline_type: str = "initial",
        pmo_approval: bool = False,
        baseline_id: str = None,
        create_date: str = None,
        approval_ref: str = None,
        executive_approval: bool = False,
        notes: str = ""
    ) -> str:
        if not all([project_id, baseline_name]):
            payload = {"error": "project_id and baseline_name are required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()
        schedule_baselines = data.get("schedule_baselines", {}).values()

        current_quarter = (datetime.now(timezone.utc).month - 1) // 3 + 1
        current_year = datetime.now(timezone.utc).year

        quarterly_baselines = [
            b
            for b in schedule_baselines.values() if b.get("project_id") == project_id
            and b.get("year") == current_year
            and b.get("quarter") == current_quarter
            and b.get("baseline_type") != "initial"
        ]

        if len(quarterly_baselines) >= 1 and not pmo_approval:
            payload = {
                "error": "Only one baseline update allowed per quarter without PMO approval. Set pmo_approval=True if approved."
            }
            out = json.dumps(payload)
            return out

        project_milestones = [
            m for m in milestones.values() if m.get("project_id") == project_id
        ]

        if not project_milestones:
            payload = {"error": f"No milestones found for project '{project_id}'"}
            out = json.dumps(payload)
            return out

        baseline_id = baseline_id or f"base_{uuid.uuid4().hex[:8]}"
        create_date = create_date or datetime.now(timezone.utc).isoformat()

        downstream_impacts = []
        for milestone in project_milestones.values():
            deps = data.get("milestone_dependencies", {}).values()
            successors = [
                d.get("successor_id")
                for d in deps.values() if d.get("predecessor_id") == milestone.get("milestone_id")
            ]

            if successors:
                downstream_impacts.append(
                    {
                        "milestone_id": milestone.get("milestone_id"),
                        "milestone_name": milestone.get("milestone_name"),
                        "downstream_count": len(successors),
                        "downstream_milestones": successors,
                    }
                )

        milestone_snapshots = []
        max_variance = 0

        for milestone in project_milestones.values():
            original_baseline_start = milestone.get(
                "original_baseline_start",
                milestone.get("baseline_start", milestone.get("start_date")),
            )
            original_baseline_target = milestone.get(
                "original_baseline_target",
                milestone.get("baseline_target", milestone.get("target_date")),
            )

            snapshot = {
                "milestone_id": milestone.get("milestone_id"),
                "milestone_name": milestone.get("milestone_name"),
                "baseline_start": milestone.get("start_date"),
                "baseline_target": milestone.get("target_date"),
                "current_start": milestone.get("start_date"),
                "current_target": milestone.get("target_date"),
                "original_baseline_start": original_baseline_start,
                "original_baseline_target": original_baseline_target,
                "variance_days": 0,
            }

            orig_target = datetime.fromisoformat(
                original_baseline_target.replace("Z", "+00:00")
            )
            curr_target = datetime.fromisoformat(
                milestone.get("target_date").replace("Z", "+00:00")
            )
            variance_days = (curr_target - orig_target).days
            variance_percentage = (
                abs(variance_days)
                / max((orig_target - datetime.now(timezone.utc)).days, 1)
                * 100
            )

            snapshot["variance_from_original_days"] = variance_days
            snapshot["variance_from_original_percentage"] = round(
                variance_percentage, 1
            )

            milestone_snapshots.append(snapshot)

            if variance_percentage > 20 and not executive_approval:
                payload = {
                    "error": f"Milestone '{milestone.get('milestone_name')}' has {variance_percentage:.1f}% variance from original baseline. Executive approval required."
                }
                out = json.dumps(payload)
                return out

        new_baseline = {
            "baseline_id": baseline_id,
            "project_id": project_id,
            "baseline_name": baseline_name,
            "baseline_type": baseline_type,
            "approval_ref": approval_ref,
            "pmo_approval": pmo_approval,
            "executive_approval": executive_approval,
            "notes": notes,
            "milestone_count": len(milestone_snapshots),
            "max_variance_days": max_variance,
            "variance_percentage": 0,
            "milestone_snapshots": milestone_snapshots,
            "downstream_impacts": downstream_impacts,
            "created_date": create_date,
            "year": datetime.fromisoformat(create_date.replace("Z", "+00:00")).year,
            "quarter": (datetime.now(timezone.utc).month - 1) // 3 + 1,
        }

        data["schedule_baselines"][new_baseline["schedule_baseline_id"]] = new_baseline

        for milestone in project_milestones.values():
            if "original_baseline_start" not in milestone:
                milestone["original_baseline_start"] = milestone.get(
                    "baseline_start", milestone.get("start_date")
                )
            if "original_baseline_target" not in milestone:
                milestone["original_baseline_target"] = milestone.get(
                    "baseline_target", milestone.get("target_date")
                )

            milestone["baseline_start"] = milestone.get("start_date")
            milestone["baseline_target"] = milestone.get("target_date")
        payload = {"success": True, "baseline": new_baseline}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateScheduleBaseline",
                "description": "Create a schedule baseline for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "baseline_id": {"type": "string", "description": "Baseline ID"},
                        "create_date": {"type": "string", "description": "Creation date"},
                        "baseline_name": {
                            "type": "string",
                            "description": "Name of the baseline",
                        },
                        "baseline_type": {
                            "type": "string",
                            "description": "Type: initial, quarterly, rebaseline",
                        },
                        "approval_ref": {
                            "type": "string",
                            "description": "Approval reference number",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Notes about the baseline",
                        },
                        "pmo_approval": {
                            "type": "boolean",
                            "description": "PMO approval for multiple quarterly updates",
                        },
                        "executive_approval": {
                            "type": "boolean",
                            "description": "Executive approval for >20% variance",
                        },
                    },
                    "required": ["project_id", "baseline_name"],
                },
            },
        }


class UpdateMilestoneDates(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        milestone_id: str = None, 
        new_start_date: str = None, 
        new_target_date: str = None
    ) -> str:
        if not milestone_id or not (new_start_date or new_target_date):
            payload = {"error": "milestone_id, and at least one date are required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()
        schedule_changes = data.get("schedule_changes", {}).values()
        milestone_dependencies = data.get("milestone_dependencies", {}).values()

        milestone = next(
            (m for m in milestones.values() if m.get("milestone_id") == milestone_id), None
        )
        if not milestone:
            payload = {"error": f"Milestone '{milestone_id}' not found"}
            out = json.dumps(payload)
            return out

        old_start = milestone.get("start_date")
        old_target = milestone.get("target_date")

        is_critical = milestone.get("is_critical_path", False)
        if is_critical and new_target_date:
            old_target_dt = datetime.fromisoformat(old_target.replace("Z", "+00:00"))
            new_target_dt = datetime.fromisoformat(
                new_target_date.replace("Z", "+00:00")
            )
            slippage_days = (new_target_dt - old_target_dt).days

            if slippage_days > 5:
                schedule_impact_analyses = data.get("schedule_impact_analyses", {}).values()
                analysis_id = f"sia_{uuid.uuid4().hex[:8]}"

                downstream_milestones = []
                for dep in milestone_dependencies.values():
                    if dep.get("predecessor_id") == milestone_id:
                        succ_milestone = next(
                            (
                                m
                                for m in milestones.values() if m.get("milestone_id") == dep.get("successor_id")
                            ),
                            None,
                        )
                        if succ_milestone:
                            downstream_milestones.append(
                                {
                                    "milestone_id": succ_milestone.get("milestone_id"),
                                    "milestone_name": succ_milestone.get(
                                        "milestone_name"
                                    ),
                                    "expected_impact_days": slippage_days,
                                }
                            )

                impact_analysis = {
                    "analysis_id": analysis_id,
                    "milestone_id": milestone_id,
                    "slippage_days": slippage_days,
                    "downstream_impacts": downstream_milestones,
                    "critical_path_extension": slippage_days,
                    "created_date": datetime.now(timezone.utc).isoformat(),
                    "status": "mandatory_review_required",
                }

                data["schedule_impact_analyses"][impact_analysis["schedule_impact_analyse_id"]] = impact_analysis
                payload = {
                    "error": f"Critical path milestone slippage of {slippage_days} days exceeds 5-day threshold. Mandatory schedule impact analysis created.",
                    "impact_analysis": impact_analysis,
                }
                out = json.dumps(payload)
                return out

        impacted_milestones = []
        for dep in milestone_dependencies.values():
            if dep.get("predecessor_id") == milestone_id:
                impacted_milestones.append(dep.get("successor_id"))

        change_id = f"chg_{uuid.uuid4().hex[:8]}"
        change_record = {
            "change_id": change_id,
            "milestone_id": milestone_id,
            "old_start_date": old_start,
            "old_target_date": old_target,
            "new_start_date": new_start_date or old_start,
            "new_target_date": new_target_date or old_target,
            "impacted_milestones": impacted_milestones,
            "is_critical_path": is_critical,
            "change_date": datetime.now(timezone.utc).isoformat(),
        }
        schedule_data["changes"][change_id] = change_record

        if new_start_date:
            milestone["start_date"] = new_start_date
        if new_target_date:
            milestone["target_date"] = new_target_date

        if milestone.get("baseline_target"):
            baseline = datetime.fromisoformat(
                milestone["baseline_target"].replace("Z", "+00:00")
            )
            new_target = datetime.fromisoformat(
                milestone["target_date"].replace("Z", "+00:00")
            )
            milestone["float_days"] = (new_target - baseline).days

        result = {
            "success": True,
            "milestone": milestone,
            "change_record": change_record,
            "impacted_count": len(impacted_milestones),
            "critical_path_update_required": len(impacted_milestones) > 0,
        }
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateMilestoneDates",
                "description": "Update milestone start and/or target dates",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "new_start_date": {
                            "type": "string",
                            "description": "New start date (ISO format)",
                        },
                        "new_target_date": {
                            "type": "string",
                            "description": "New target date (ISO format)",
                        },
                    },
                    "required": ["milestone_id"],
                },
            },
        }


class CreateGateReview(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        milestone_id: str,
        review_date: str,
        criteria_results: dict[str, str] = {},
        reviewers: list[str] = [],
        conditional_pass: bool = False,
        review_notes: str = "",
        action_items: list[str] = []
    ) -> str:
        if not all([milestone_id, review_date, criteria_results, reviewers]):
            payload = {
                "error": "milestone_id, review_date, criteria_results, and reviewers are required"
            }
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()
        gate_reviews = data.get("gate_reviews", {}).values()

        milestone = next(
            (m for m in milestones.values() if m.get("milestone_id") == milestone_id), None
        )
        if not milestone:
            payload = {"error": f"Milestone '{milestone_id}' not found"}
            out = json.dumps(payload)
            return out

        if milestone.get("milestone_type") not in ["phase_gate", "major"]:
            payload = {"error": "Gate reviews are only for phase_gate or major milestones"}
            out = json.dumps(payload)
            return out

        start_date = datetime.fromisoformat(
            milestone.get("start_date").replace("Z", "+00:00")
        )
        review_dt = datetime.fromisoformat(review_date.replace("Z", "+00:00"))

        if not milestone.get("gate_criteria") and review_dt >= start_date:
            payload = {"error": "Gate criteria must be defined before milestone start date"}
            out = json.dumps(payload)
            return out

        failed_criteria = [k for k, v in criteria_results.items() if v == "fail"]
        overall_decision = "fail" if failed_criteria else "pass"

        if failed_criteria and conditional_pass:
            overall_decision = "conditional_pass"

        review_id = f"gate_{uuid.uuid4().hex[:8]}"

        previous_reviews = [
            r for r in gate_reviews.values() if r.get("milestone_id") == milestone_id
        ]
        consecutive_failures = 0

        if previous_reviews and overall_decision == "fail":
            previous_reviews.sort(key=lambda x: x.get("created_date"), reverse=True)

            for review in previous_reviews:
                if review.get("overall_decision") == "fail":
                    consecutive_failures += 1
                else:
                    break

        new_review = {
            "review_id": review_id,
            "milestone_id": milestone_id,
            "review_date": review_date,
            "criteria_results": criteria_results,
            "overall_decision": overall_decision,
            "review_notes": review_notes,
            "reviewers": reviewers,
            "action_items": action_items,
            "consecutive_failures": consecutive_failures
            + (1 if overall_decision == "fail" else 0),
            "created_date": datetime.now(timezone.utc).isoformat(),
        }

        gate_data["reviews"][review_id] = new_review

        if overall_decision == "pass":
            milestone["gate_passed"] = True
        elif overall_decision == "fail":
            milestone["health"] = "red"
            milestone["status"] = "delayed"

            current_target = datetime.fromisoformat(
                milestone.get("target_date").replace("Z", "+00:00")
            )
            new_target = current_target + timedelta(days=10)
            milestone["target_date"] = new_target.isoformat()
            milestone["remediation_period"] = True

            if new_review["consecutive_failures"] >= 3:
                escalations = data.get("escalations", {}).values()
                escalation_id = f"esc_{uuid.uuid4().hex[:8]}"
                escalations.append(
                    {
                        "escalation_id": escalation_id,
                        "milestone_id": milestone_id,
                        "escalation_level": "steering_committee",
                        "created_date": datetime.now(timezone.utc).isoformat(),
                    }
                )

                new_review["escalated_to_steering"] = True
        payload = {
            "success": True,
            "gate_review": new_review,
            "decision": overall_decision,
            "failed_criteria": failed_criteria,
            "consecutive_failures": new_review["consecutive_failures"],
            "escalated": new_review.get("escalated_to_steering", False),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateGateReview",
                "description": "Create a gate review for a milestone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "review_date": {
                            "type": "string",
                            "description": "Review date (ISO format)",
                        },
                        "criteria_results": {
                            "type": "object",
                            "description": "Dictionary of criteria names to results (pass/fail)",
                        },
                        "reviewers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of reviewer employee IDs",
                        },
                        "review_notes": {
                            "type": "string",
                            "description": "Review notes",
                        },
                        "action_items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Action items from the review",
                        },
                        "conditional_pass": {
                            "type": "boolean",
                            "description": "Allow conditional pass despite failures",
                        },
                    },
                    "required": [
                        "milestone_id",
                        "review_date",
                        "criteria_results",
                        "reviewers",
                    ],
                },
            },
        }


class AddExternalDependency(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        milestone_id: str,
        dependency_name: str,
        provider: str,
        expected_delivery_date: str,
        criticality: str = "medium",
        dependency_id: str = None,
        confirmed: bool = False,
        contact_info: dict = None,
        contingency_days: int = 0,
        notice_days: int = 30
    ) -> str:
        if not all([milestone_id, dependency_name, provider, expected_delivery_date]):
            payload = {
                "error": "milestone_id, dependency_name, provider, and expected_delivery_date are required"
            }
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()
        external_dependencies = data.get("external_dependencies", {}).values()

        milestone = next(
            (m for m in milestones.values() if m.get("milestone_id") == milestone_id), None
        )
        if not milestone:
            payload = {"error": f"Milestone '{milestone_id}' not found"}
            out = json.dumps(payload)
            return out

        if dependency_id is None:
            dependency_id = f"ext_{uuid.uuid4().hex[:8]}"
        if contact_info is None:
            contact_info = {}

        new_dependency = {
            "dependency_id": dependency_id,
            "milestone_id": milestone_id,
            "dependency_name": dependency_name,
            "provider": provider,
            "expected_delivery_date": expected_delivery_date,
            "confirmed": confirmed,
            "contact_info": contact_info,
            "criticality": criticality,
            "contingency_days": contingency_days,
            "notice_days": notice_days,
            "created_date": datetime.now(timezone.utc).isoformat(),
            "status": "pending",
        }

        data["external_dependencies"][new_dependency["external_dependencie_id"]] = new_dependency

        if criticality == "critical" and not new_dependency["confirmed"]:
            milestone["health"] = (
                "yellow"
                if milestone.get("health") == "green"
                else milestone.get("health")
            )
        payload = {"success": True, "external_dependency": new_dependency}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddExternalDependency",
                "description": "Add an external dependency to a milestone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "dependency_name": {
                            "type": "string",
                            "description": "Name of the dependency",
                        },
                        "provider": {
                            "type": "string",
                            "description": "External provider name",
                        },
                        "expected_delivery_date": {
                            "type": "string",
                            "description": "Expected delivery date",
                        },
                        "criticality": {
                            "type": "string",
                            "description": "Criticality: low, medium, high, critical",
                        },
                        "confirmed": {
                            "type": "boolean",
                            "description": "Is delivery confirmed",
                        },
                        "contact_info": {
                            "type": "object",
                            "description": "Contact information for provider",
                        },
                        "contingency_days": {
                            "type": "number",
                            "description": "Contingency buffer days",
                        },
                        "notice_days": {
                            "type": "number",
                            "description": "Notice period required",
                        },
                        "dependency_id": {
                            "type": "string",
                            "description": "External dependency ID",
                        },
                    },
                    "required": [
                        "milestone_id",
                        "dependency_name",
                        "provider",
                        "expected_delivery_date",
                    ],
                },
            },
        }


class CreateRecoveryPlan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        milestone_id: str,
        recovery_actions: list[dict[str, Any]],
        additional_resources: list[str] = [],
        risk_mitigation: list[str] = [],
        feasibility: str = "medium"
    ) -> str:
        milestone_id = milestone_id
        recovery_actions = recovery_actions
        additional_resources = additional_resources

        if not all([milestone_id, recovery_actions]):
            payload = {"error": "milestone_id and recovery_actions are required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()
        recovery_plans = data.get("recovery_plans", {}).values()

        milestone = next(
            (m for m in milestones.values() if m.get("milestone_id") == milestone_id), None
        )
        if not milestone:
            payload = {"error": f"Milestone '{milestone_id}' not found"}
            out = json.dumps(payload)
            return out

        if milestone.get("is_critical_path"):
            for resource_id in additional_resources:
                if milestone.get("resource_allocation", 100) < 100:
                    payload = {
                        "error": "Cannot reduce resource allocation below 100% for critical path tasks"
                    }
                    out = json.dumps(payload)
                    return out

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
            "risk_mitigation": risk_mitigation,
            "total_impact_days": total_impact_days,
            "feasibility": feasibility,
            "created_date": datetime.now(timezone.utc).isoformat(),
            "status": "pending_approval",
            "created_within_48hrs": created_within_48hrs,
            "is_critical_path": milestone.get("is_critical_path", False),
        }

        data["recovery_plans"][new_plan["recovery_plan_id"]] = new_plan
        payload = {
            "success": True,
            "recovery_plan": new_plan,
            "days_recovered": total_impact_days,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRecoveryPlan",
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


class AnalyzeScheduleCompression(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        target_reduction: int,
        compression_type: str = "crashing"
    ) -> str:
        if not all([project_id, target_reduction]):
            payload = {"error": "project_id and target_reduction are required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()
        compression_analyses = data.get("compression_analyses", {}).values()

        project_milestones = [
            m for m in milestones.values() if m.get("project_id") == project_id
        ]

        if not project_milestones:
            payload = {"error": f"No milestones found for project '{project_id}'"}
            out = json.dumps(
                payload)
            return out

        analysis_id = f"comp_{uuid.uuid4().hex[:8]}"

        compression_results = []
        achieved_reduction = 0
        total_cost = 0
        affected_milestones = 0

        for milestone in project_milestones.values():
            if achieved_reduction >= target_reduction:
                break

            if (
                milestone.get("is_critical_path")
                and compression_type == "resource_reduction"
            ):
                continue

            if milestone.get("float_days", 0) > 0 or milestone.get("is_critical_path"):
                start_date = datetime.fromisoformat(
                    milestone.get("start_date").replace("Z", "+00:00")
                )
                target_date = datetime.fromisoformat(
                    milestone.get("target_date").replace("Z", "+00:00")
                )
                duration = (target_date - start_date).days

                if compression_type == "crashing":

                    max_reduction = int(duration * 0.2)
                    reduction = min(
                        max_reduction, target_reduction - achieved_reduction
                    )
                    cost = reduction * 500
                    risk_multiplier = 1.0
                else:

                    max_reduction = int(duration * 0.3)
                    reduction = min(
                        max_reduction, target_reduction - achieved_reduction
                    )
                    cost = 0
                    risk_multiplier = 2.0

                if reduction > 0:
                    compression_results.append(
                        {
                            "milestone_id": milestone.get("milestone_id"),
                            "milestone_name": milestone.get("milestone_name"),
                            "compression_type": compression_type,
                            "original_duration": duration,
                            "reduction_days": reduction,
                            "new_duration": duration - reduction,
                            "cost": cost,
                            "risk_multiplier": risk_multiplier,
                            "is_critical_path": milestone.get(
                                "is_critical_path", False
                            ),
                        }
                    )

                    achieved_reduction += reduction
                    total_cost += cost
                    affected_milestones += 1

        cost_benefit_ratio = (
            total_cost / achieved_reduction if achieved_reduction > 0 else 0
        )

        new_analysis = {
            "analysis_id": analysis_id,
            "project_id": project_id,
            "compression_type": compression_type,
            "target_reduction": target_reduction,
            "achieved_reduction": achieved_reduction,
            "total_cost": total_cost,
            "risk_multiplier": 2.0 if compression_type == "fast_tracking" else 1.0,
            "affected_milestones": affected_milestones,
            "compression_results": compression_results,
            "cost_benefit_ratio": cost_benefit_ratio,
            "created_date": datetime.now(timezone.utc).isoformat(),
        }

        data["compression_analyses"][new_analysis["compression_analyse_id"]] = new_analysis
        payload = {
                "success": True,
                "analysis": new_analysis,
                "feasible": achieved_reduction >= target_reduction * 0.8,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AnalyzeScheduleCompression",
                "description": "Analyze schedule compression options for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "target_reduction": {
                            "type": "number",
                            "description": "Target reduction in days",
                        },
                        "compression_type": {
                            "type": "string",
                            "description": "Type: crashing, fast_tracking",
                        },
                    },
                    "required": ["project_id", "target_reduction"],
                },
            },
        }


class UpdateBufferConsumption(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        buffer_type: str,
        days_consumed: int,
        milestone_id: str = None,
        scope: str = "false",
        change_request_id: str = None
    ) -> str:
        if not all([project_id, buffer_type, days_consumed]):
            payload = {"error": "project_id, buffer_type and days_consumed are required"}
            out = json.dumps(payload)
            return out

        if scope.lower() == "true" and not change_request_id:
            payload = {
                "error": "Buffer cannot be consumed for scope additions without change request approval. Provide change_request_id."
            }
            out = json.dumps(payload)
            return out

        schedule_buffers = data.get("schedule_buffers", {}).values()

        buffer = next(
            (b for b in schedule_buffers.values() if b.get("project_id") == project_id), None
        )
        if not buffer:
            total_project_days = 180
            buffer = {
                "project_id": project_id,
                "total_buffer": int(total_project_days * 0.3),
                "project_buffer": int(total_project_days * 0.3 * 0.5),
                "phase_gate_buffer": int(total_project_days * 0.3 * 0.3),
                "integration_buffer": int(total_project_days * 0.3 * 0.2),
                "project_consumed": 0,
                "phase_gate_consumed": 0,
                "integration_consumed": 0,
                "buffer_history": [],
            }
            data["schedule_buffers"][buffer["schedule_buffer_id"]] = buffer

        if buffer_type == "project":
            buffer["project_consumed"] = (
                buffer.get("project_consumed", 0) + days_consumed
            )
            consumption_percentage = (
                buffer["project_consumed"] / buffer["project_buffer"]
            ) * 100
        elif buffer_type == "phase_gate":
            buffer["phase_gate_consumed"] = (
                buffer.get("phase_gate_consumed", 0) + days_consumed
            )
            consumption_percentage = (
                buffer["phase_gate_consumed"] / buffer["phase_gate_buffer"]
            ) * 100
        elif buffer_type == "integration":
            buffer["integration_consumed"] = (
                buffer.get("integration_consumed", 0) + days_consumed
            )
            consumption_percentage = (
                buffer["integration_consumed"] / buffer["integration_buffer"]
            ) * 100
        else:
            payload = {
                "error": "Invalid buffer_type. Must be: project, phase_gate, or integration"
            }
            out = json.dumps(payload)
            return out

        if "buffer_history" not in buffer:
            buffer["buffer_history"] = []

        history_entry = {
            "change_id": f"buf_{uuid.uuid4().hex[:8]}",
            "buffer_type": buffer_type,
            "action": "consume",
            "days": days_consumed,
            "milestone_id": milestone_id,
            "scope": scope,
            "change_request_id": change_request_id,
            "consumption_percentage": consumption_percentage,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        buffer["buffer_history"].append(history_entry)

        total_consumed = (
            buffer.get("project_consumed", 0)
            + buffer.get("phase_gate_consumed", 0)
            + buffer.get("integration_consumed", 0)
        )
        total_buffer = buffer.get("total_buffer", 0)
        remaining_buffer = total_buffer - total_consumed
        total_consumption_percentage = (
            (total_consumed / total_buffer * 100) if total_buffer > 0 else 0
        )

        risk_review_required = total_consumption_percentage > 60

        if risk_review_required:
            risk_reviews = data.get("risk_reviews", {}).values()
            review_id = f"risk_{uuid.uuid4().hex[:8]}"
            risk_reviews.append(
                {
                    "review_id": review_id,
                    "project_id": project_id,
                    "trigger": "buffer_consumption_exceeded_60",
                    "consumption_percentage": total_consumption_percentage,
                    "status": "pending",
                    "created_date": datetime.now(timezone.utc).isoformat(),
                }
            )
        payload = {
            "success": True,
            "buffer_status": {
                "project_id": project_id,
                "total_buffer": total_buffer,
                "total_consumed": total_consumed,
                "remaining_buffer": remaining_buffer,
                "consumption_percentage": round(total_consumption_percentage, 1),
                "buffer_type_consumed": {
                    "project": buffer.get("project_consumed", 0),
                    "phase_gate": buffer.get("phase_gate_consumed", 0),
                    "integration": buffer.get("integration_consumed", 0),
                },
                "risk_review_required": risk_review_required,
            },
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateBufferConsumption",
                "description": "Update buffer consumption for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "buffer_type": {
                            "type": "string",
                            "description": "Buffer type: project, phase_gate, integration",
                        },
                        "days_consumed": {
                            "type": "number",
                            "description": "Number of days consumed",
                        },
                        "milestone_id": {
                            "type": "string",
                            "description": "Related milestone ID",
                        },
                        "escope": {
                            "type": "boolean",
                            "description": "Flag to indicate if consumption is scope-related",
                        },
                        "change_request_id": {
                            "type": "string",
                            "description": "Change request ID (required for scope additions)",
                        },
                    },
                    "required": [
                        "project_id",
                        "buffer_type",
                        "days_consumed",
                    ],
                },
            },
        }


class GetMilestoneDependencies(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], milestone_id: str = None) -> str:
        if not milestone_id:
            payload = {"error": "milestone_id is required"}
            out = json.dumps(payload)
            return out

        milestone_dependencies = data.get("milestone_dependencies", {}).values()
        milestones = data.get("milestones", {}).values()

        predecessors = []
        successors = []

        for dep in milestone_dependencies.values():
            if dep.get("successor_id") == milestone_id:
                pred_milestone = next(
                    (
                        m
                        for m in milestones.values() if m.get("milestone_id") == dep.get("predecessor_id")
                    ),
                    None,
                )
                if pred_milestone:
                    predecessors.append(
                        {
                            "dependency_id": dep.get("dependency_id"),
                            "milestone_id": pred_milestone.get("milestone_id"),
                            "milestone_name": pred_milestone.get("milestone_name"),
                            "status": pred_milestone.get("status"),
                            "target_date": pred_milestone.get("target_date"),
                            "dependency_type": dep.get("dependency_type"),
                            "lag_days": dep.get("lag_days"),
                            "is_mandatory": dep.get("is_mandatory"),
                            "zero_lag": dep.get("zero_lag", False),
                        }
                    )

            if dep.get("predecessor_id") == milestone_id:
                succ_milestone = next(
                    (
                        m
                        for m in milestones.values() if m.get("milestone_id") == dep.get("successor_id")
                    ),
                    None,
                )
                if succ_milestone:
                    successors.append(
                        {
                            "dependency_id": dep.get("dependency_id"),
                            "milestone_id": succ_milestone.get("milestone_id"),
                            "milestone_name": succ_milestone.get("milestone_name"),
                            "status": succ_milestone.get("status"),
                            "target_date": succ_milestone.get("target_date"),
                            "dependency_type": dep.get("dependency_type"),
                            "lag_days": dep.get("lag_days"),
                            "is_mandatory": dep.get("is_mandatory"),
                            "zero_lag": dep.get("zero_lag", False),
                        }
                    )
        payload = {
                "milestone_id": milestone_id,
                "predecessors": predecessors,
                "successors": successors,
                "total_dependencies": len(predecessors) + len(successors),
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
                "name": "GetMilestoneDependencies",
                "description": "Get all dependencies (predecessors and successors) for a milestone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        }
                    },
                    "required": ["milestone_id"],
                },
            },
        }


class CheckMilestoneFloat(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()
        project_milestones = [
            m for m in milestones.values() if m.get("project_id") == project_id
        ]

        float_analysis = []

        for milestone in project_milestones.values():
            float_days = milestone.get("float_days", 0)
            is_critical = milestone.get("is_critical_path", False)

            if float_days < 0:
                float_status = "negative"
                risk_level = "critical"
            elif float_days == 0:
                float_status = "zero"
                risk_level = "high"
            elif float_days <= 5:
                float_status = "low"
                risk_level = "medium"
            else:
                float_status = "comfortable"
                risk_level = "low"

            float_analysis.append(
                {
                    "milestone_id": milestone.get("milestone_id"),
                    "milestone_name": milestone.get("milestone_name"),
                    "float_days": float_days,
                    "float_status": float_status,
                    "risk_level": risk_level,
                    "is_critical_path": is_critical,
                    "target_date": milestone.get("target_date"),
                    "status": milestone.get("status"),
                    "resource_allocation": milestone.get("resource_allocation", 100),
                }
            )

        float_analysis.sort(key=lambda x: x["float_days"])

        summary = {
            "negative_float": len(
                [f for f in float_analysis.values() if f["float_status"] == "negative"]
            ),
            "zero_float": len(
                [f for f in float_analysis.values() if f["float_status"] == "zero"]
            ),
            "low_float": len([f for f in float_analysis.values() if f["float_status"] == "low"]),
            "comfortable_float": len(
                [f for f in float_analysis.values() if f["float_status"] == "comfortable"]
            ),
            "critical_path_count": len(
                [f for f in float_analysis.values() if f["is_critical_path"]]
            ),
        }
        payload = {
                "project_id": project_id,
                "float_analysis": float_analysis,
                "summary": summary,
                "total_milestones": len(float_analysis),
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
                "name": "CheckMilestoneFloat",
                "description": "Check float/slack time for all project milestones",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"}
                    },
                    "required": ["project_id"],
                },
            },
        }


class ApplyResourceLeveling(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        resource_constraints: dict = {},
        priority_method: str = "critical_path"
    ) -> str:
        if not all([project_id, resource_constraints]):
            payload = {"error": "project_id and resource_constraints are required"}
            out = json.dumps(
                payload)
            return out

        milestones = data.get("milestones", {}).values()
        leveling_results = data.get("leveling_results", {}).values()

        project_milestones = [
            m for m in milestones.values() if m.get("project_id") == project_id
        ]

        if not project_milestones:
            payload = {"error": f"No milestones found for project '{project_id}'"}
            out = json.dumps(
                payload)
            return out

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
                payload = {
                        "error": f"Critical path milestone '{milestone.get('milestone_name')}' cannot have resource allocation below 100%"
                    }
                out = json.dumps(
                    payload)
                return out

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

        data["leveling_results"][new_result["leveling_result_id"]] = new_result
        payload = {
                "success": True,
                "leveling_result": new_result,
                "requires_approval": requires_approval,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyResourceLeveling",
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

        milestones = data.get("milestones", {}).values()
        milestone_dependencies = data.get("milestone_dependencies", {}).values()
        projects = data.get("projects", {}).values()

        project = next((p for p in projects.values() if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project '{project_id}' not found"}
            out = json.dumps(payload)
            return out

        project_milestones = [
            m for m in milestones.values() if m.get("project_id") == project_id
        ]

        project_milestones.sort(key=lambda x: x.get("start_date"))

        timeline = {
            "project_id": project_id,
            "project_name": project.get("name"),
            "project_start": project.get("start_date"),
            "project_end": project.get("end_date"),
            "milestones": [],
        }

        for milestone in project_milestones.values():
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
                for dep in milestone_dependencies.values():
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
            earliest_start = min(m.get("start_date") for m in project_milestones.values())
            latest_end = max(m.get("target_date") for m in project_milestones.values())

            timeline["timeline_metrics"] = {
                "total_milestones": len(project_milestones),
                "completed": len(
                    [m for m in project_milestones.values() if m.get("status") == "completed"]
                ),
                "in_progress": len(
                    [m for m in project_milestones.values() if m.get("status") == "in_progress"]
                ),
                "delayed": len(
                    [m for m in project_milestones.values() if m.get("status") == "delayed"]
                ),
                "critical_path_count": len(
                    [m for m in project_milestones.values() if m.get("is_critical_path")]
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


class UpdateExternalDependencyStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], dependency_id: str = None, new_status: str = None, actual_delivery_date: str = None) -> str:
        if not all([dependency_id, new_status]):
            payload = {"error": "dependency_id and new_status are required"}
            out = json.dumps(payload)
            return out

        external_dependencies = data.get("external_dependencies", {}).values()
        milestones = data.get("milestones", {}).values()

        dependency = next(
            (
                d
                for d in external_dependencies.values() if d.get("dependency_id") == dependency_id
            ),
            None,
        )
        if not dependency:
            payload = {"error": f"External dependency '{dependency_id}' not found"}
            out = json.dumps(
                payload)
            return out

        old_status = dependency.get("status")
        dependency["status"] = new_status

        if new_status == "delivered" and actual_delivery_date:
            dependency["actual_delivery_date"] = actual_delivery_date

            expected = datetime.fromisoformat(
                dependency.get("expected_delivery_date").replace("Z", "+00:00")
            )
            actual = datetime.fromisoformat(actual_delivery_date.replace("Z", "+00:00"))

            if actual > expected:
                days_late = (actual - expected).days
                dependency["days_late"] = days_late

                milestone = next(
                    (
                        m
                        for m in milestones.values() if m.get("milestone_id") == dependency.get("milestone_id")
                    ),
                    None,
                )
                if milestone and dependency.get("criticality") in ["high", "critical"]:
                    milestone["health"] = "yellow" if days_late < 7 else "red"

        elif new_status == "delayed":

            milestone = next(
                (
                    m
                    for m in milestones.values() if m.get("milestone_id") == dependency.get("milestone_id")
                ),
                None,
            )
            if milestone:
                milestone["health"] = (
                    "yellow" if milestone.get("health") == "green" else "red"
                )
        payload = {
                "success": True,
                "dependency": dependency,
                "status_change": f"{old_status} -> {new_status}",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateExternalDependencyStatus",
                "description": "Update the status of an external dependency",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dependency_id": {
                            "type": "string",
                            "description": "External dependency ID",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status: pending, confirmed, delayed, delivered, cancelled",
                        },
                        "actual_delivery_date": {
                            "type": "string",
                            "description": "Actual delivery date (for delivered status)",
                        },
                    },
                    "required": ["dependency_id", "new_status"],
                },
            },
        }


class CreateMilestoneFromTemplate(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        template_id: str,
        project_id: str,
        milestone_name: str,
        target_date: str,
        owner_id: str,
        milestone_id: str = None
    ) -> str:
        if not all([template_id, project_id, milestone_name, target_date, owner_id]):
            payload = {
                "error": "template_id, project_id, milestone_name, target_date, and owner_id are required"
            }
            out = json.dumps(payload)
            return out

        milestone_templates = data.get("milestone_templates", {}).values()
        milestones = data.get("milestones", {}).values()

        template = next(
            (t for t in milestone_templates.values() if t.get("template_id") == template_id),
            None,
        )
        if not template:
            payload = {"error": f"Template '{template_id}' not found"}
            out = json.dumps(payload)
            return out

        if template.get("template_type") == "major" and not template.get(
            "gate_criteria"
        ):
            payload = {"error": "Major milestone templates must include gate criteria"}
            out = json.dumps(payload)
            return out

        milestone_id = milestone_id or f"ms_{uuid.uuid4().hex[:8]}"

        target_dt = datetime.fromisoformat(target_date.replace("Z", "+00:00"))
        duration_days = template.get("duration_days", 30)
        start_dt = target_dt - timedelta(days=duration_days)

        buffer_days = int(duration_days * (template.get("buffer_percentage", 0) / 100))

        new_milestone = {
            "milestone_id": milestone_id,
            "project_id": project_id,
            "milestone_name": milestone_name,
            "milestone_type": template.get("template_type"),
            "start_date": start_dt.isoformat(),
            "target_date": target_date,
            "description": f"Created from template: {template.get('template_name')}",
            "deliverables": template.get("deliverables", []),
            "gate_criteria": template.get("gate_criteria", []),
            "owner_id": owner_id,
            "status": "not_started",
            "health": "green",
            "progress_percentage": 0,
            "float_days": buffer_days,
            "is_critical_path": template.get("is_critical_path_candidate", False),
            "buffer_consumed": 0,
            "created_date": datetime.now(timezone.utc).isoformat(),
            "baseline_start": start_dt.isoformat(),
            "baseline_target": target_date,
            "original_baseline_start": start_dt.isoformat(),
            "original_baseline_target": target_date,
            "template_id": template_id,
            "resource_allocation": 100,
        }

        data["milestones"][milestone_id] = new_milestone
        payload = {
            "success": True,
            "milestone": new_milestone,
            "template_used": template.get("template_name"),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMilestoneFromTemplate",
                "description": "Create a new milestone from a predefined template",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "template_id": {"type": "string", "description": "Template ID"},
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "project_id": {"type": "string", "description": "Project ID"},
                        "milestone_name": {
                            "type": "string",
                            "description": "Name for the new milestone",
                        },
                        "target_date": {
                            "type": "string",
                            "description": "Target completion date",
                        },
                        "owner_id": {
                            "type": "string",
                            "description": "Owner employee ID",
                        },
                    },
                    "required": [
                        "template_id",
                        "project_id",
                        "milestone_name",
                        "target_date",
                        "owner_id",
                    ],
                },
            },
        }


class ArchiveMilestone(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], milestone_id: str = None) -> str:
        if not milestone_id:
            payload = {"error": "milestone_id is required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()
        archived_milestones = data.get("archived_milestones", {}).values()

        milestone_index = None
        milestone_to_archive = None
        for i, milestone in enumerate(milestones.values()):
            if milestone.get("milestone_id") == milestone_id:
                milestone_index = i
                milestone_to_archive = milestone
                break

        if not milestone_to_archive:
            payload = {"error": f"Milestone '{milestone_id}' not found"}
            out = json.dumps(payload)
            return out

        if milestone_to_archive.get("status") != "completed":
            payload = {"error": "Only completed milestones can be archived"}
            out = json.dumps(payload)
            return out

        milestones.pop(milestone_index)

        milestone_to_archive["archived_date"] = datetime.now(timezone.utc).isoformat()
        archived_data["milestones"][milestone_id] = milestone_to_archive
        payload = {
                "success": True,
                "archived_milestone": {
                    "milestone_id": milestone_to_archive.get("milestone_id"),
                    "milestone_name": milestone_to_archive.get("milestone_name"),
                    "archived_date": milestone_to_archive.get("archived_date"),
                },
            }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ArchiveMilestone",
                "description": "Archive a completed milestone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID to archive",
                        },
                    },
                    "required": ["milestone_id"],
                },
            },
        }


class GetDelayedMilestones(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None, include_recovery_plans: bool = False) -> str:
        milestones = data.get("milestones", {}).values()
        recovery_plans = data.get("recovery_plans", {}).values()

        if project_id:
            project_milestones = [
                m for m in milestones.values() if m.get("project_id") == project_id
            ]
        else:
            project_milestones = milestones

        delayed_milestones = []

        for milestone in project_milestones.values():

            is_delayed = (
                milestone.get("float_days", 0) < 0
                or milestone.get("health") == "red"
                or milestone.get("status") == "delayed"
            )

            if is_delayed:
                delayed_info = {
                    "milestone_id": milestone.get("milestone_id"),
                    "milestone_name": milestone.get("milestone_name"),
                    "project_id": milestone.get("project_id"),
                    "target_date": milestone.get("target_date"),
                    "float_days": milestone.get("float_days", 0),
                    "health": milestone.get("health"),
                    "status": milestone.get("status"),
                    "owner_id": milestone.get("owner_id"),
                    "is_critical_path": milestone.get("is_critical_path"),
                    "resource_allocation": milestone.get("resource_allocation", 100),
                }

                if include_recovery_plans:

                    milestone_recovery_plans = [
                        rp
                        for rp in recovery_plans.values() if rp.get("milestone_id") == milestone.get("milestone_id")
                    ]
                    delayed_info["recovery_plans"] = milestone_recovery_plans
                    delayed_info["has_recovery_plan"] = (
                        len(milestone_recovery_plans) > 0
                    )

                delayed_data["milestones"][milestone_id] = delayed_info

        delayed_milestones.sort(key=lambda x: x["float_days"])

        critical_delays_over_5 = [
            m
            for m in delayed_milestones
            if m["is_critical_path"] and m["float_days"] < -5
        ]
        payload = {
                "delayed_count": len(delayed_milestones),
                "delayed_milestones": delayed_milestones,
                "critical_delays": len(
                    [m for m in delayed_milestones.values() if m["is_critical_path"]]
                ),
                "critical_delays_requiring_impact_analysis": len(
                    critical_delays_over_5
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
                "name": "GetDelayedMilestones",
                "description": "Get all delayed milestones with optional recovery plan information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "Filter by project ID (optional)",
                        },
                        "include_recovery_plans": {
                            "type": "boolean",
                            "description": "Include recovery plan information",
                        },
                    },
                },
            },
        }


class ValidateMilestoneReadiness(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], milestone_id: str = None) -> str:
        if not milestone_id:
            payload = {"error": "milestone_id is required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()
        milestone_dependencies = data.get("milestone_dependencies", {}).values()
        external_dependencies = data.get("external_dependencies", {}).values()

        milestone = next(
            (m for m in milestones.values() if m.get("milestone_id") == milestone_id), None
        )
        if not milestone:
            payload = {"error": f"Milestone '{milestone_id}' not found"}
            out = json.dumps(payload)
            return out

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
            d for d in milestone_dependencies.values() if d.get("successor_id") == milestone_id
        ]
        for dep in predecessor_deps:
            if dep.get("is_mandatory"):
                pred_milestone = next(
                    (
                        m
                        for m in milestones.values() if m.get("milestone_id") == dep.get("predecessor_id")
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
            d for d in external_dependencies.values() if d.get("milestone_id") == milestone_id
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
        payload = {
                "milestone_id": milestone_id,
                "milestone_name": milestone.get("milestone_name"),
                "milestone_type": milestone.get("milestone_type"),
                "is_ready": is_ready,
                "readiness_issues": readiness_issues,
                "readiness_score": max(0, 100 - (len(readiness_issues) * 25)),
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
                "name": "ValidateMilestoneReadiness",
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


class GetScheduleVariance(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None, baseline_id: str = None) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", {}).values()
        schedule_baselines = data.get("schedule_baselines", {}).values()

        project_milestones = [
            m for m in milestones.values() if m.get("project_id") == project_id
        ]

        if baseline_id:
            baseline = next(
                (b for b in schedule_baselines.values() if b.get("baseline_id") == baseline_id),
                None,
            )
        else:
            project_baselines = [
                b for b in schedule_baselines.values() if b.get("project_id") == project_id
            ]
            baseline = (
                max(project_baselines, key=lambda x: x.get("created_date"))
                if project_baselines
                else None
            )

        if not baseline:
            payload = {"error": f"No baseline found for project '{project_id}'"}
            out = json.dumps(payload)
            return out

        variance_analysis = []
        total_variance_days = 0

        for milestone in project_milestones.values():
            baseline_snapshot = next(
                (
                    s
                    for s in baseline.get("milestone_snapshots", [])
                    if s.get("milestone_id") == milestone.get("milestone_id")
                ),
                None,
            )

            if baseline_snapshot:
                baseline_target = datetime.fromisoformat(
                    baseline_snapshot.get("baseline_target").replace("Z", "+00:00")
                )
                current_target = datetime.fromisoformat(
                    milestone.get("target_date").replace("Z", "+00:00")
                )

                variance_days = (current_target - baseline_target).days
                variance_percentage = (
                    variance_days
                    / max((baseline_target - datetime.now(timezone.utc)).days, 1)
                ) * 100

                original_variance_days = None
                original_variance_percentage = None
                if baseline_snapshot.get("original_baseline_target"):
                    orig_target = datetime.fromisoformat(
                        baseline_snapshot.get("original_baseline_target").replace(
                            "Z", "+00:00"
                        )
                    )
                    original_variance_days = (current_target - orig_target).days
                    original_variance_percentage = (
                        original_variance_days
                        / max((orig_target - datetime.now(timezone.utc)).days, 1)
                    ) * 100

                variance_analysis.append(
                    {
                        "milestone_id": milestone.get("milestone_id"),
                        "milestone_name": milestone.get("milestone_name"),
                        "baseline_target": baseline_snapshot.get("baseline_target"),
                        "current_target": milestone.get("target_date"),
                        "variance_days": variance_days,
                        "variance_percentage": round(variance_percentage, 1),
                        "original_baseline_target": baseline_snapshot.get(
                            "original_baseline_target"
                        ),
                        "original_variance_days": original_variance_days,
                        "original_variance_percentage": (
                            round(original_variance_percentage, 1)
                            if original_variance_percentage
                            else None
                        ),
                        "requires_executive_approval": original_variance_percentage
                        and abs(original_variance_percentage) > 20,
                        "status": milestone.get("status"),
                        "health": milestone.get("health"),
                    }
                )

                total_variance_days += abs(variance_days)

        variance_analysis.sort(key=lambda x: x["variance_days"], reverse=True)

        avg_variance = (
            total_variance_days / len(variance_analysis) if variance_analysis else 0
        )

        requiring_approval = [
            v for v in variance_analysis if v.get("requires_executive_approval", False)
        ]
        payload = {
                "delayed_milestones": len(
                    [v for v in variance_analysis.values() if v["variance_days"] > 0]
                ),
                "project_id": project_id,
                "baseline_id": baseline.get("baseline_id"),
                "baseline_name": baseline.get("baseline_name"),
                "baseline_type": baseline.get("baseline_type"),
                "variance_analysis": variance_analysis,
                "summary": {
                    "total_milestones": len(variance_analysis),
                    "delayed_milestones": len(
                        [v for v in variance_analysis.values() if v["variance_days"] > 0]
                    ),
                    "ahead_milestones": len(
                        [v for v in variance_analysis.values() if v["variance_days"] < 0]
                    ),
                    "on_track_milestones": len(
                        [v for v in variance_analysis.values() if v["variance_days"] == 0]
                    ),
                    "average_variance_days": round(avg_variance, 1),
                    "max_delay_days": max(
                        (v["variance_days"] for v in variance_analysis.values()), default=0
                    ),
                    "milestones_requiring_executive_approval": len(requiring_approval),
                },
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
                "name": "GetScheduleVariance",
                "description": "Analyze schedule variance against baseline",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "baseline_id": {
                            "type": "string",
                            "description": "Specific baseline ID (optional)",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }


class ApproveRecoveryPlan(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, decision: str = None, approver_id: str = None, approval_notes: str = "") -> str:
        if not all([plan_id, decision, approver_id]):
            payload = {"error": "plan_id, decision, and approver_id are required"}
            out = json.dumps(payload)
            return out

        recovery_plans = data.get("recovery_plans", {}).values()
        milestones = data.get("milestones", {}).values()

        plan = next((p for p in recovery_plans.values() if p.get("plan_id") == plan_id), None)
        if not plan:
            payload = {"error": f"Recovery plan '{plan_id}' not found"}
            out = json.dumps(payload)
            return out

        if plan.get("status") != "pending_approval":
            payload = {"error": "Plan is not in pending_approval status"}
            out = json.dumps(payload)
            return out

        plan["status"] = "approved" if decision == "approve" else "rejected"
        plan["approver_id"] = approver_id
        plan["approval_date"] = datetime.now(timezone.utc).isoformat()
        plan["approval_notes"] = approval_notes

        if decision == "approve":
            milestone = next(
                (
                    m
                    for m in milestones.values() if m.get("milestone_id") == plan.get("milestone_id")
                ),
                None,
            )
            if milestone:
                milestone["target_date"] = plan.get("recovery_target_date")
                milestone["has_recovery_plan"] = True
                milestone["recovery_plan_id"] = plan_id

                if plan.get("feasibility") == "high":
                    milestone["health"] = (
                        "yellow"
                        if milestone.get("health") == "red"
                        else milestone.get("health")
                    )

                if (
                    milestone.get("is_critical_path")
                    and milestone.get("resource_allocation", 100) < 100
                ):
                    payload = {
                        "error": "Cannot approve recovery plan that reduces critical path task resources below 100%"
                    }
                    out = json.dumps(payload)
                    return out

        payload = {"success": True, "recovery_plan": plan, "decision": decision}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApproveRecoveryPlan",
                "description": "Approve or reject a recovery plan",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "Recovery plan ID",
                        },
                        "decision": {
                            "type": "string",
                            "description": "Decision: approve or reject",
                        },
                        "approver_id": {
                            "type": "string",
                            "description": "Approver employee ID",
                        },
                        "approval_notes": {
                            "type": "string",
                            "description": "Approval notes",
                        },
                    },
                    "required": ["plan_id", "decision", "approver_id"],
                },
            },
        }


TOOLS = [
    GetMilestoneDetails(),
    CreateMilestone(),
    UpdateMilestoneStatus(),
    CreateMilestoneDependency(),
    CalculateCriticalPath(),
    CreateScheduleBaseline(),
    UpdateMilestoneDates(),
    CreateGateReview(),
    AddExternalDependency(),
    CreateRecoveryPlan(),
    AnalyzeScheduleCompression(),
    UpdateBufferConsumption(),
    GetMilestoneDependencies(),
    CheckMilestoneFloat(),
    ApplyResourceLeveling(),
    GetProjectTimeline(),
    UpdateExternalDependencyStatus(),
    CreateMilestoneFromTemplate(),
    ArchiveMilestone(),
    GetDelayedMilestones(),
    ValidateMilestoneReadiness(),
    GetScheduleVariance(),
    ApproveRecoveryPlan(),
]
