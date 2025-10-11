# Copyright Sierra

import datetime, uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateMilestoneDependency(Tool):
    @staticmethod
    def _check_circular_dependency(
        data: Dict[str, Any], predecessor_id: str, successor_id: str
    ) -> bool:
        """Check if adding this dependency would create a circular dependency"""
        dependencies = data.get("milestone_dependencies", [])

        graph = {}
        for dep in dependencies:
            pred = dep.get("predecessor_id")
            succ = dep.get("successor_id")
            if pred not in graph:
                graph[pred] = []
            graph[pred].append(succ)

        if predecessor_id not in graph:
            graph[predecessor_id] = []
        graph[predecessor_id].append(successor_id)

        def has_cycle(node, visited, rec_stack):
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
    def invoke(data: Dict[str, Any], predecessor_id, successor_id, dependency_type = "finish_to_start", is_mandatory = True, lag_days = 0, notes = "", zero_lag = False) -> str:

        if not all([predecessor_id, successor_id]):
            return json.dumps({"error": "predecessor_id and successor_id are required"})

        if predecessor_id == successor_id:
            return json.dumps({"error": "Milestone cannot depend on itself"})

        if CreateMilestoneDependency._check_circular_dependency(
            data, predecessor_id, successor_id
        ):
            return json.dumps(
                {"error": "This dependency would create a circular dependency"}
            )

        if dependency_type == "finish_to_start" and not zero_lag and lag_days < 1:
            lag_days = 1

        if dependency_type in ["start_to_start", "finish_to_finish"] and not notes:
            return json.dumps(
                {
                    "error": f"{dependency_type} dependencies require justification in the notes field"
                }
            )

        milestone_dependencies = data.get("milestone_dependencies", [])
        milestones = list(data.get("milestones", {}).values())

        pred_exists = any(m.get("milestone_id") == predecessor_id for m in milestones)
        succ_exists = any(m.get("milestone_id") == successor_id for m in milestones)

        if not pred_exists or not succ_exists:
            return json.dumps({"error": "One or both milestones not found"})

        existing = any(
            d.get("predecessor_id") == predecessor_id
            and d.get("successor_id") == successor_id
            for d in milestone_dependencies
        )

        if existing:
            return json.dumps({"error": "Dependency already exists"})

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

        milestone_dependencies.append(new_dependency)

        for milestone in milestones:
            if milestone.get("milestone_id") == successor_id:
                milestone["is_critical_path"] = True
                break

        project_id = next(
            (
                m.get("project_id")
                for m in milestones
                if m.get("milestone_id") == predecessor_id
            ),
            None,
        )

        result = {
            "success": True,
            "dependency": new_dependency,
            "critical_path_update_required": True,
            "project_id": project_id,
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_milestone_dependency",
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
