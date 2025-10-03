import json
import uuid
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool


class SearchTasks(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        task_id: str = None, 
        title: str = None, 
        status: str = None, 
        assignee_id: str = None, 
        sprint_id: str = None, 
        priority: str = None
    ) -> str:
        tasks = data.get("tasks", [])

        if task_id:
            for task in tasks:
                if task.get("task_id") == task_id:
                    payload = task
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Task with ID '{task_id}' not found"}
            out = json.dumps(payload)
            return out

        results = []
        for task in tasks:
            match = True

            if title and title.lower() not in task.get("title", "").lower():
                match = False
            if status and task.get("status") != status:
                match = False
            if assignee_id and task.get("assignee_id") != assignee_id:
                match = False
            if sprint_id and task.get("sprint_id") != sprint_id:
                match = False
            if priority and task.get("priority") != priority:
                match = False

            if match:
                results.append(task)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchTasks",
                "description": "Search for tasks by various criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "Specific task ID to retrieve",
                        },
                        "title": {
                            "type": "string",
                            "description": "Search by task title",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by status: todo, in_progress, blocked, done",
                        },
                        "assignee_id": {
                            "type": "string",
                            "description": "Filter by assigned employee ID",
                        },
                        "sprint_id": {
                            "type": "string",
                            "description": "Filter by sprint ID",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Filter by priority: low, medium, high, critical",
                        },
                    },
                },
            },
        }


class CreateTask(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        new_task_id: str = None,
        title: str = None,
        description: str = None,
        assignee_id: str = None,
        priority: str = "medium",
        story_points: int = 3,
        sprint_id: str = None,
        dependencies: list = None,
    ) -> str:
        if dependencies is None:
            dependencies = []

        if not all([title, assignee_id]):
            payload = {"error": "title and assignee_id are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])
        employees = data.get("employees", [])
        sprints = data.get("sprints", [])

        assignee = next(
            (emp for emp in employees if emp.get("employee_id") == assignee_id), None
        )
        if not assignee:
            payload = {"error": f"Employee '{assignee_id}' not found"}
            out = json.dumps(payload)
            return out

        if priority == "critical":
            is_senior = any(
                skill.get("proficiency", 0) >= 4 for skill in assignee.get("skills", [])
            )
            if not is_senior:
                senior_members = [
                    emp
                    for emp in employees
                    if any(
                        skill.get("proficiency", 0) >= 4
                        for skill in emp.get("skills", [])
                    )
                ]
                if senior_members:
                    payload = {
                        "error": "Critical tasks must be assigned to senior team members (proficiency 4+)",
                        "available_seniors": [
                            {"id": emp["employee_id"], "name": emp["name"]}
                            for emp in senior_members[:5]
                        ],
                    }
                    out = json.dumps(payload)
                    return out

        if sprint_id:
            sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)
            if sprint and sprint.get("status") == "active":
                assignee_tasks = [
                    t
                    for t in tasks
                    if t.get("assignee_id") == assignee_id
                    and t.get("sprint_id") == sprint_id
                    and t.get("status") != "done"
                ]
                current_points = sum(t.get("story_points", 0) for t in assignee_tasks)

                if current_points + story_points > 25:
                    payload = {
                        "error": f"Cannot assign task. Would exceed 25 story point limit for {assignee_id}",
                        "current_points": current_points,
                        "new_task_points": story_points,
                        "total_would_be": current_points + story_points,
                    }
                    out = json.dumps(payload)
                    return out

        for dep_id in dependencies:
            if not any(task.get("task_id") == dep_id for task in tasks):
                payload = {"error": f"Dependency task '{dep_id}' not found"}
                out = json.dumps(payload)
                return out

        task_id = f"task_{uuid.uuid4().hex[:8]}"

        if new_task_id:
            for t in tasks:
                if t.get("task_id") == new_task_id:
                    payload = {
                        "error": f"new_task_id {new_task_id} exists. Please enter a unique task_id."
                    }
                    out = json.dumps(payload)
                    return out
            task_id = new_task_id

        new_task = {
            "task_id": task_id,
            "title": title,
            "description": description,
            "assignee_id": assignee_id,
            "status": "todo",
            "priority": priority,
            "story_points": story_points,
            "sprint_id": sprint_id,
            "dependencies": dependencies,
            "blocked_by": [],
            "created_date": datetime.now().isoformat(),
            "updated_date": datetime.now().isoformat(),
            "completed_date": None,
            "time_logged": 0,
        }

        tasks.append(new_task)
        payload = {"success": True, "task": new_task}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTask",
                "description": "Create a new task with optional dependencies",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "Task title"},
                        "description": {
                            "type": "string",
                            "description": "Detailed task description",
                        },
                        "assignee_id": {
                            "type": "string",
                            "description": "Employee ID to assign the task to",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Priority level: low, medium, high, critical",
                        },
                        "story_points": {
                            "type": "integer",
                            "description": "Estimated story points (1-13)",
                        },
                        "sprint_id": {
                            "type": "string",
                            "description": "Sprint to assign task to (optional)",
                        },
                        "dependencies": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of task IDs this task depends on",
                        },
                    },
                    "required": ["title", "assignee_id"],
                },
            },
        }


class GetTaskDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None) -> str:
        tasks = data.get("tasks", [])

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out

        time_logs = data.get("time_logs", [])
        task_history = data.get("task_history", [])

        task_time_logs = [log for log in time_logs if log.get("task_id") == task_id]
        #total_hours_logged = sum(log.get("hours", 0) for log in task_time_logs)

        history_entries = [h for h in task_history if h.get("task_id") == task_id]

        task_details = {
            "task_id": task.get("task_id"),
            "title": task.get("title"),
            "description": task.get("description"),
            "status": task.get("status"),
            "assignee_id": task.get("assignee_id"),
            "priority": task.get("priority"),
            "story_points": task.get("story_points"),
            "sprint_id": task.get("sprint_id"),
            "created_date": task.get("created_date"),
            "updated_date": task.get("updated_date"),
            "completed_date": task.get("completed_date"),
            "dependencies": task.get("dependencies", []),
            "blocked_by": task.get("blocked_by", []),
            "blocks": [],
            "time_logged": task.get("time_logged", 0),
            #"total_hours_logged": total_hours_logged,
            "last_time_logged": task.get("last_time_logged"),
            "blocked_date": task.get("blocked_date"),
            "escalated": task.get("escalated", False),
            "escalation_id": task.get("escalation_id"),
            "previous_priority": task.get("previous_priority"),
            "cloned_from": task.get("cloned_from"),
            "history_count": len(history_entries),
        }

        for other_task in tasks:
            if task_id in other_task.get("dependencies", []):
                task_details["blocks"].append(other_task.get("task_id"))

        dependency_details = []
        for dep_id in task.get("dependencies", []):
            dep_task = next((t for t in tasks if t.get("task_id") == dep_id), None)
            if dep_task:
                dependency_details.append(
                    {
                        "task_id": dep_task.get("task_id"),
                        "title": dep_task.get("title"),
                        "status": dep_task.get("status"),
                        "assignee_id": dep_task.get("assignee_id"),
                    }
                )
        task_details["dependency_details"] = dependency_details

        blocked_by_details = []
        for block_id in task.get("blocked_by", []):
            block_task = next((t for t in tasks if t.get("task_id") == block_id), None)
            if block_task:
                blocked_by_details.append(
                    {
                        "task_id": block_task.get("task_id"),
                        "title": block_task.get("title"),
                        "status": block_task.get("status"),
                    }
                )
        task_details["blocked_by_details"] = blocked_by_details
        payload = task_details
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTaskDetails",
                "description": "Get comprehensive details for a specific task including dependencies",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to get details for",
                        }
                    },
                    "required": ["task_id"],
                },
            },
        }


class UpdateTaskStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, new_status: str = None) -> str:
        if not all([task_id, new_status]):
            payload = {"error": "task_id and new_status are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])

        for task in tasks:
            if task.get("task_id") == task_id:
                old_status = task.get("status")

                if new_status == "in_progress" and old_status == "todo":
                    dependencies = task.get("dependencies", [])
                    unresolved_deps = []
                    for dep_id in dependencies:
                        dep_task = next(
                            (t for t in tasks if t.get("task_id") == dep_id), None
                        )
                        if dep_task and dep_task.get("status") != "done":
                            unresolved_deps.append(dep_id)
                            task["blocked_by"].append(dep_id)

                    if unresolved_deps:
                        payload = {
                                "error": "Cannot start task. Dependencies not completed",
                                "unresolved_dependencies": unresolved_deps,
                                "blocked_by": unresolved_deps,
                            }
                        out = json.dumps(
                            payload)
                        return out

                task["status"] = new_status
                task["updated_date"] = datetime.now().isoformat()

                if new_status == "blocked":
                    task["blocked_date"] = datetime.now().isoformat()
                elif new_status == "done":
                    task["completed_date"] = datetime.now().isoformat()
                payload = {"success": True, "task": task}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Task '{task_id}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTaskStatus",
                "description": "Update the status of a task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status: todo, in_progress, blocked, done",
                        },
                    },
                    "required": ["task_id", "new_status"],
                },
            },
        }


class CreateSprint(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None, sprint_name: str = None, start_date: str = None, end_date: str = None, sprint_goal: str = None, team_id: str = None) -> str:
        if not all([sprint_name, start_date, end_date, team_id]):
            payload = {"error": "sprint_name, start_date, end_date, and team_id are required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", [])
        teams = data.get("teams", [])

        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": f"Team '{team_id}' not found"}
            out = json.dumps(payload)
            return out

        for s in sprints:
            if s.get("sprint_id") == sprint_id:
                payload = {
                    "error": f"sprint_id {sprint_id} exists. Please enter a unique sprint_id.",
                }
                out = json.dumps(payload)
                return out

        new_sprint = {
            "sprint_id": sprint_id,
            "sprint_name": sprint_name,
            "start_date": start_date,
            "end_date": end_date,
            "sprint_goal": sprint_goal,
            "team_id": team_id,
            "status": "planning",
            "planned_story_points": 0,
            "completed_story_points": 0,
            "velocity": 0,
        }

        sprints.append(new_sprint)
        payload = {"success": True, "sprint": new_sprint}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSprint",
                "description": "Create a new sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_name": {
                            "type": "string",
                            "description": "Name of the sprint",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Sprint start date (YYYY-MM-DD)",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "Sprint end date (YYYY-MM-DD)",
                        },
                        "sprint_goal": {
                            "type": "string",
                            "description": "Main goal for the sprint",
                        },
                        "team_id": {
                            "type": "string",
                            "description": "Team assigned to this sprint",
                        },
                    },
                    "required": ["sprint_name", "start_date", "end_date", "team_id"],
                },
            },
        }


class MarkSprintAsReviewed(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None) -> str:
        if not sprint_id:
            payload = {"error": "sprint_id is a required parameter"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", [])

        for sprint in sprints:
            if sprint.get("sprint_id") == sprint_id:
                sprint["reviewed"] = "True"
                payload = {"success": True}
                out = json.dumps(payload)
                return out
        payload = {"error": f"It wasn't found any sprint with the if {sprint_id}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MarkSprintAsReviewed",
                "description": "Mark sprint as reviewed",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {
                            "type": "string",
                            "description": "Id of the sprint",
                        },
                    },
                    "required": [
                        "sprint_id",
                    ],
                },
            },
        }


class AssignTaskToSprint(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, sprint_id: str = None) -> str:
        if not all([task_id, sprint_id]):
            payload = {"error": "task_id and sprint_id are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])
        sprints = data.get("sprints", [])
        teams = data.get("teams", [])

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)

        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out
        if not sprint:
            payload = {"error": f"Sprint '{sprint_id}' not found"}
            out = json.dumps(payload)
            return out

        if sprint.get("status") not in ["planning", "active"]:
            payload = {
                    "error": f"Cannot add tasks to sprint in '{sprint.get('status')}' status"
                }
            out = json.dumps(
                payload)
            return out

        if sprint.get("status") == "active" and task.get("priority") != "critical":
            payload = {
                    "error": "Cannot add non-critical tasks to active sprint",
                }
            out = json.dumps(
                payload)
            return out

        team = next(
            (t for t in teams if t.get("team_id") == sprint.get("team_id")), None
        )
        if team:

            team_members = team.get("members", [])

            completed_sprints = [
                s
                for s in sprints
                if s.get("team_id") == team.get("team_id")
                and s.get("status") == "completed"
            ]

            if len(completed_sprints) >= 3:

                recent_sprints = sorted(
                    completed_sprints, key=lambda x: x.get("end_date", ""), reverse=True
                )[:3]
                avg_velocity = sum(s.get("velocity", 0) for s in recent_sprints) / 3
                capacity_limit = avg_velocity * 0.8
            else:

                capacity_limit = len(team_members) * 20

            sprint_tasks = [t for t in tasks if t.get("sprint_id") == sprint_id]
            current_points = sum(t.get("story_points", 0) for t in sprint_tasks)
            new_total = current_points + task.get("story_points", 0)

            if new_total > capacity_limit:
                payload = {
                        "error": "Adding task would exceed sprint capacity limit",
                        "current_points": current_points,
                        "task_points": task.get("story_points", 0),
                        "total_would_be": new_total,
                        "capacity_limit": capacity_limit,
                    }
                out = json.dumps(
                    payload)
                return out

            assignee_sprint_tasks = [
                t
                for t in sprint_tasks
                if t.get("assignee_id") == task.get("assignee_id")
            ]
            assignee_points = sum(
                t.get("story_points", 0) for t in assignee_sprint_tasks
            )

            if assignee_points + task.get("story_points", 0) > 25:
                payload = {
                        "error": f"Cannot assign task. Would exceed 25 story point limit for {task.get('assignee_id')}",
                        "current_points": assignee_points,
                        "task_points": task.get("story_points", 0),
                        "total_would_be": assignee_points + task.get("story_points", 0),
                    }
                out = json.dumps(
                    payload)
                return out

        task["sprint_id"] = sprint_id
        task["updated_date"] = datetime.now().isoformat()

        sprint["planned_story_points"] = sprint.get(
            "planned_story_points", 0
        ) + task.get("story_points", 0)
        payload = {
                "success": True,
                "task": task,
                "sprint_planned_points": sprint["planned_story_points"],
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignTaskToSprint",
                "description": "Assign a task to a sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to assign",
                        },
                        "sprint_id": {
                            "type": "string",
                            "description": "The sprint ID to assign to",
                        },
                    },
                    "required": ["task_id", "sprint_id"],
                },
            },
        }


class GetSprintDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None) -> str:
        if not sprint_id:
            payload = {"error": "sprint_id is required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", [])

        for sprint in sprints:
            if sprint.get("sprint_id") == sprint_id:
                payload = sprint
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Sprint '{sprint_id}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSprintDetails",
                "description": "Get details of a specific sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {"type": "string", "description": "The sprint ID"}
                    },
                    "required": ["sprint_id"],
                },
            },
        }


class CalculateSprintBurndown(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None) -> str:
        if not sprint_id:
            payload = {"error": "sprint_id is required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", [])
        tasks = data.get("tasks", [])

        sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            payload = {"error": f"Sprint '{sprint_id}' not found"}
            out = json.dumps(payload)
            return out

        sprint_tasks = [t for t in tasks if t.get("sprint_id") == sprint_id]

        total_points = sum(t.get("story_points", 0) for t in sprint_tasks)
        completed_points = sum(
            t.get("story_points", 0) for t in sprint_tasks if t.get("status") == "done"
        )
        remaining_points = total_points - completed_points

        in_progress_points = sum(
            t.get("story_points", 0)
            for t in sprint_tasks
            if t.get("status") == "in_progress"
        )
        blocked_points = sum(
            t.get("story_points", 0)
            for t in sprint_tasks
            if t.get("status") == "blocked"
        )
        blocked_tasks = [t for t in sprint_tasks if t.get("status") == "blocked"]

        completion_percentage = (
            round((completed_points / total_points * 100), 1) if total_points > 0 else 0
        )

        if (
            sprint.get("status") == "active"
            and sprint.get("start_date")
            and sprint.get("end_date")
        ):
            try:
                start_date = datetime.fromisoformat(
                    sprint["start_date"].replace("Z", "+00:00")
                )
                end_date = datetime.fromisoformat(
                    sprint["end_date"].replace("Z", "+00:00")
                )
                current_date = datetime.now()

                total_days = (end_date - start_date).days
                elapsed_days = (current_date - start_date).days
                expected_progress = (
                    (elapsed_days / total_days * 100) if total_days > 0 else 0
                )

                behind_schedule = completion_percentage < (expected_progress - 20)
            except:
                behind_schedule = False
                expected_progress = None
        else:
            behind_schedule = False
            expected_progress = None

        burndown_data = {
            "sprint_id": sprint_id,
            "completion_percentage": completion_percentage,
            "total_story_points": total_points,
            "completed_story_points": completed_points,
            "remaining_story_points": remaining_points,
            "in_progress_points": in_progress_points,
            "blocked_points": blocked_points,
            "expected_progress": expected_progress,
            "behind_schedule": behind_schedule,
            "task_breakdown": {
                "total_tasks": len(sprint_tasks),
                "completed_tasks": len(
                    [t for t in sprint_tasks if t.get("status") == "done"]
                ),
                "in_progress_tasks": len(
                    [t for t in sprint_tasks if t.get("status") == "in_progress"]
                ),
                "blocked_tasks": len(blocked_tasks),
                "todo_tasks": len(
                    [t for t in sprint_tasks if t.get("status") == "todo"]
                ),
            },
        }

        if behind_schedule:
            burndown_data["alert"] = "Sprint is behind schedule by more than 20%"
            burndown_data["blocked_task_details"] = [
                {
                    "task_id": t.get("task_id"),
                    "title": t.get("title"),
                    "story_points": t.get("story_points", 0),
                }
                for t in blocked_tasks
            ]
        payload = burndown_data
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateSprintBurndown",
                "description": "Calculate burndown metrics for a sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {
                            "type": "string",
                            "description": "The sprint ID to calculate burndown for",
                        }
                    },
                    "required": ["sprint_id"],
                },
            },
        }


class ReassignTask(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, new_assignee_id: str = None) -> str:
        if not all([task_id, new_assignee_id]):
            payload = {"error": "task_id and new_assignee_id are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])
        employees = data.get("employees", [])
        task_history = data.get("task_history", [])
        sprints = data.get("sprints", [])

        new_assignee = next(
            (emp for emp in employees if emp.get("employee_id") == new_assignee_id),
            None,
        )
        if not new_assignee:
            payload = {"error": f"Employee '{new_assignee_id}' not found"}
            out = json.dumps(payload)
            return out

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out

        if task.get("priority") == "critical":
            is_senior = any(
                skill.get("proficiency", 0) >= 4
                for skill in new_assignee.get("skills", [])
            )
            if not is_senior:
                senior_members = [
                    emp
                    for emp in employees
                    if any(
                        skill.get("proficiency", 0) >= 4
                        for skill in emp.get("skills", [])
                    )
                ]
                if senior_members:
                    payload = {
                            "error": "Critical tasks must be assigned to senior team members (proficiency 4+)",
                            "available_seniors": [
                                {"id": emp["employee_id"], "name": emp["name"]}
                                for emp in senior_members[:5]
                            ],
                        }
                    out = json.dumps(
                        payload)
                    return out

        if task.get("sprint_id"):
            sprint = next(
                (s for s in sprints if s.get("sprint_id") == task["sprint_id"]), None
            )
            if sprint and sprint.get("status") == "active":
                assignee_tasks = [
                    t
                    for t in tasks
                    if t.get("assignee_id") == new_assignee_id
                    and t.get("sprint_id") == task["sprint_id"]
                    and t.get("status") != "done"
                    and t.get("task_id") != task_id
                ]
                current_points = sum(t.get("story_points", 0) for t in assignee_tasks)

                if current_points + task.get("story_points", 0) > 25:
                    payload = {
                            "error": f"Cannot reassign. Would exceed 25 story point limit for {new_assignee_id}",
                            "current_points": current_points,
                            "task_points": task.get("story_points", 0),
                            "total_would_be": current_points
                            + task.get("story_points", 0),
                        }
                    out = json.dumps(
                        payload)
                    return out

        reassignment_count = len(
            [
                h
                for h in task_history
                if h.get("task_id") == task_id and h.get("action") == "reassigned"
            ]
        )
        if reassignment_count >= 2:
            payload = {
                    "error": "Task has already been reassigned twice",
                    "reassignment_count": reassignment_count,
                }
            out = json.dumps(
                payload)
            return out

        old_assignee = task.get("assignee_id")

        history_entry = {
            "history_id": f"hist_{uuid.uuid4().hex[:8]}",
            "task_id": task_id,
            "action": "reassigned",
            "from_assignee": old_assignee,
            "to_assignee": new_assignee_id,
            "timestamp": datetime.now().isoformat(),
        }
        task_history.append(history_entry)

        task["assignee_id"] = new_assignee_id
        task["updated_date"] = datetime.now().isoformat()
        payload = {"success": True, "task": task, "history": history_entry}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReassignTask",
                "description": "Reassign a task to a different team member",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to reassign",
                        },
                        "new_assignee_id": {
                            "type": "string",
                            "description": "The new assignee's employee ID",
                        },
                    },
                    "required": ["task_id", "new_assignee_id"],
                },
            },
        }


class UpdateSprintStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None, new_status: str = None) -> str:
        if not all([sprint_id, new_status]):
            payload = {"error": "sprint_id and new_status are required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", [])
        tasks = data.get("tasks", [])
        teams = data.get("teams", [])

        sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            payload = {"error": f"Sprint '{sprint_id}' not found"}
            out = json.dumps(payload)
            return out

        old_status = sprint.get("status")

        valid_transitions = {
            "planning": ["active"],
            "active": ["completed"],
            "completed": ["completed"],
        }

        if new_status not in valid_transitions.get(old_status, []):
            payload = {
                "error": f"Invalid status transition from '{old_status}' to '{new_status}'",
            }
            out = json.dumps(payload)
            return out

        if new_status == "active":
            team_id = sprint.get("team_id")

            team = next((t for t in teams if t.get("team_id") == team_id), None)
            if team:
                team_members = team.get("members", [])

                completed_sprints = [
                    s
                    for s in sprints
                    if s.get("team_id") == team_id and s.get("status") == "completed"
                ]

                if len(completed_sprints) >= 3:
                    recent_sprints = sorted(
                        completed_sprints,
                        key=lambda x: x.get("end_date", ""),
                        reverse=True,
                    )[:3]
                    avg_velocity = sum(s.get("velocity", 0) for s in recent_sprints) / 3
                    capacity_limit = avg_velocity * 0.8
                else:
                    capacity_limit = len(team_members) * 20

                if sprint.get("planned_story_points", 0) > capacity_limit:
                    payload = {
                        "error": "Cannot activate sprint. Planned points exceed capacity",
                        "planned_points": sprint.get("planned_story_points", 0),
                        "capacity_limit": capacity_limit,
                    }
                    out = json.dumps(payload)
                    return out

        if new_status == "completed":
            sprint_tasks = [t for t in tasks if t.get("sprint_id") == sprint_id]
            incomplete_tasks = [
                t for t in sprint_tasks if t.get("status") not in ["done"]
            ]

            if incomplete_tasks:
                payload = {
                    "error": "Cannot complete sprint with incomplete tasks",
                    "incomplete_tasks": len(incomplete_tasks),
                }
                out = json.dumps(payload)
                return out

            completed_points = sum(
                t.get("story_points", 0)
                for t in sprint_tasks
                if t.get("status") == "done"
            )
            sprint["completed_story_points"] = completed_points
            sprint["velocity"] = completed_points
            sprint["completed_date"] = datetime.now().isoformat()

        sprint["status"] = new_status
        payload = {"success": True, "sprint": sprint}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSprintStatus",
                "description": "Update the status of a sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {
                            "type": "string",
                            "description": "The sprint ID to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status: planning, active, completed",
                        },
                    },
                    "required": ["sprint_id", "new_status"],
                },
            },
        }


class GetTeamVelocity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str, last_n_sprints: int = 3) -> str:
        if not team_id:
            payload = {"error": "team_id is required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", [])

        team_sprints = [
            s
            for s in sprints
            if s.get("team_id") == team_id and s.get("status") == "completed"
        ]

        team_sprints.sort(key=lambda x: x.get("end_date", ""), reverse=True)

        recent_sprints = team_sprints[:last_n_sprints]

        if not recent_sprints:
            payload = {
                    "team_id": team_id,
                    "average_velocity": 0,
                    "sprints_analyzed": 0,
                    "message": "No completed sprints found for this team",
                }
            out = json.dumps(
                payload)
            return out

        velocities = [s.get("velocity", 0) for s in recent_sprints]
        average_velocity = sum(velocities) / len(velocities) if velocities else 0
        payload = {
                "team_id": team_id,
                "average_velocity": round(average_velocity, 1),
                "sprints_analyzed": len(recent_sprints),
                "individual_velocities": velocities,
                "trend": (
                    "improving"
                    if len(velocities) > 1 and velocities[0] > velocities[-1]
                    else "stable"
                ),
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamVelocity",
                "description": "Calculate team velocity based on completed sprints",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string", "description": "The team ID"},
                        "last_n_sprints": {
                            "type": "integer",
                            "description": "Number of recent sprints to analyze (default: 3)",
                        },
                    },
                    "required": ["team_id"],
                },
            },
        }


class CreateTaskDependency(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, depends_on_task_id: str = None, block_task: bool = False) -> str:
        if not all([task_id, depends_on_task_id]):
            payload = {"error": "task_id and depends_on_task_id are required"}
            out = json.dumps(payload)
            return out

        if task_id == depends_on_task_id:
            payload = {"error": "Task cannot depend on itself"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        dependency_task = next(
            (t for t in tasks if t.get("task_id") == depends_on_task_id), None
        )

        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out
        if not dependency_task:
            payload = {"error": f"Dependency task '{depends_on_task_id}' not found"}
            out = json.dumps(payload)
            return out

        def has_circular_dependency(start_id, check_id, visited=None):
            if visited is None:
                visited = set()
            if start_id in visited:
                return True
            visited.add(start_id)

            task_to_check = next(
                (t for t in tasks if t.get("task_id") == start_id), None
            )
            if not task_to_check:
                return False

            for dep_id in task_to_check.get("dependencies", []):
                if dep_id == check_id:
                    return True
                if has_circular_dependency(dep_id, check_id, visited):
                    return True
            return False

        if has_circular_dependency(depends_on_task_id, task_id):
            payload = {"error": "Creating this dependency would create a circular dependency"}
            out = json.dumps(payload)
            return out

        if depends_on_task_id not in task.get("dependencies", []):
            if "dependencies" not in task:
                task["dependencies"] = []
            task["dependencies"].append(depends_on_task_id)
            task["updated_date"] = datetime.now().isoformat()

        if block_task or (
            task.get("status") == "in_progress"
            and dependency_task.get("status") != "done"
        ):
            task["status"] = "todo"
            if "blocked_by" not in task:
                task["blocked_by"] = []
            task["blocked_by"].append(depends_on_task_id)
        payload = {"success": True, "task": task}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTaskDependency",
                "description": "Create a dependency between two tasks",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task that will depend on another",
                        },
                        "depends_on_task_id": {
                            "type": "string",
                            "description": "The task that must be completed first",
                        },
                    },
                    "required": ["task_id", "depends_on_task_id"],
                },
            },
        }


class GetBacklogTasks(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], priority: str = None, max_story_points: int = None) -> str:
        tasks = data.get("tasks", [])

        backlog_tasks = [
            t for t in tasks if not t.get("sprint_id") and t.get("status") != "done"
        ]

        if priority:
            backlog_tasks = [t for t in backlog_tasks if t.get("priority") == priority]

        if max_story_points:
            backlog_tasks = [
                t for t in backlog_tasks if t.get("story_points", 0) <= max_story_points
            ]

        priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        backlog_tasks.sort(
            key=lambda x: (
                priority_order.get(x.get("priority", "medium"), 2),
                x.get("story_points", 0),
            )
        )
        payload = {
            "backlog_size": len(backlog_tasks),
            "total_story_points": sum(
                t.get("story_points", 0) for t in backlog_tasks
            ),
            "tasks": backlog_tasks,
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
                "name": "GetBacklogTasks",
                "description": "Get tasks in the backlog (not assigned to any sprint)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "priority": {
                            "type": "string",
                            "description": "Filter by priority: low, medium, high, critical",
                        },
                        "max_story_points": {
                            "type": "integer",
                            "description": "Maximum story points to filter by",
                        },
                    },
                },
            },
        }


class LogTimeOnTask(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, hours_logged: float = None, employee_id: str = None, notes: str = "") -> str:
        tasks = data.get("tasks", [])
        time_logs = data.get("time_logs", [])

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out

        if task.get("assignee_id") != employee_id:
            payload = {"error": f"Employee '{employee_id}' is not assigned to this task"}
            out = json.dumps(payload)
            return out

        log_entry = {
            "log_id": f"time_{uuid.uuid4().hex[:8]}",
            "task_id": task_id,
            "employee_id": employee_id,
            "hours": hours_logged,
            "notes": notes,
            "logged_date": datetime.now().isoformat(),
        }
        time_logs.append(log_entry)

        task["time_logged"] = task.get("time_logged", 0) + hours_logged
        task["updated_date"] = datetime.now().isoformat()
        task["last_time_logged"] = datetime.now().isoformat()
        payload = {
            "success": True,
            "time_log": log_entry,
            # "total_time_logged": task["time_logged"],
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogTimeOnTask",
                "description": "Log time spent on a task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to log time for",
                        },
                        "hours_logged": {
                            "type": "number",
                            "description": "Number of hours to log",
                        },
                        "employee_id": {
                            "type": "string",
                            "description": "Employee logging the time",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about work done",
                        },
                    },
                    "required": ["task_id", "hours_logged", "employee_id"],
                },
            },
        }


class EscalateTask(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, escalate_to: str = None) -> str:
        if not all([task_id, escalate_to]):
            payload = {"error": "task_id  and escalate_to are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])
        escalations = data.get("escalations", [])

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out

        if task.get("escalated"):
            payload = {
                    "success": True,
                    "already_escalated": True,
                    "message": f"Task '{task_id}' is already escalated",
                    "existing_escalation_id": task.get("escalation_id"),
                    #"new_escalation_created": False,
                }
            out = json.dumps(
                payload)
            return out

        escalation = {
            "escalation_id": f"esc_{uuid.uuid4().hex[:8]}",
            "task_id": task_id,
            "escalated_by": task.get("assignee_id"),
            "escalated_to": escalate_to,
            "previous_status": task.get("status"),
            "created_date": datetime.now().isoformat(),
            "resolved": False,
        }
        escalations.append(escalation)

        if task.get("priority") != "critical":
            task["previous_priority"] = task.get("priority")
            task["priority"] = "critical"

        task["escalated"] = True
        task["escalation_id"] = escalation["escalation_id"]
        task["updated_date"] = datetime.now().isoformat()
        payload = {
                "success": True,
                "escalation": escalation,
                "task_priority": task["priority"],
                #"new_escalation_created": True,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EscalateTask",
                "description": "Escalate a task to management",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to escalate",
                        },
                        "escalate_to": {
                            "type": "string",
                            "description": "Manager or team lead ID to escalate to",
                        },
                    },
                    "required": ["task_id", "escalate_to"],
                },
            },
        }


class CalculateTeamCapacity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None, sprint_id: str = None) -> str:
        if not team_id:
            payload = {"error": "team_id is required"}
            out = json.dumps(payload)
            return out

        teams = data.get("teams", [])
        data.get("employees", [])
        tasks = data.get("tasks", [])

        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": f"Team '{team_id}' not found"}
            out = json.dumps(payload)
            return out

        team_members = team.get("members", [])

        total_capacity_hours = len(team_members) * 6 * 10

        if sprint_id:
            sprint_tasks = [
                t
                for t in tasks
                if t.get("sprint_id") == sprint_id
                and t.get("assignee_id") in team_members
            ]

            member_loads = {}
            for member_id in team_members:
                member_tasks = [
                    t for t in sprint_tasks if t.get("assignee_id") == member_id
                ]
                member_points = sum(t.get("story_points", 0) for t in member_tasks)
                member_loads[member_id] = {
                    "story_points": member_points,
                    "task_count": len(member_tasks),
                    "utilization": round((member_points / 20) * 100, 1),
                }

            total_assigned_points = sum(
                m["story_points"] for m in member_loads.values()
            )
            payload = {
                    "team_id": team_id,
                    "sprint_id": sprint_id,
                    "team_utilization": round(
                        (total_assigned_points / (len(team_members) * 20)) * 100, 1
                    ),
                    "total_capacity_hours": total_capacity_hours,
                    "total_capacity_points": len(team_members) * 20,
                    "assigned_story_points": total_assigned_points,
                    "available_story_points": (len(team_members) * 20)
                    - total_assigned_points,
                    "member_loads": member_loads,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {
                "team_id": team_id,
                "total_capacity_hours": total_capacity_hours,
                "total_capacity_points": len(team_members) * 20,
                "team_size": len(team_members),
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
                "name": "CalculateTeamCapacity",
                "description": "Calculate team capacity for sprint planning",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string", "description": "The team ID"},
                        "sprint_id": {
                            "type": "string",
                            "description": "Optional sprint ID to check current load",
                        },
                    },
                    "required": ["team_id"],
                },
            },
        }


class CreateSprintRetrospective(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sprint_id: str,
        what_went_well: list = [],
        what_needs_improvement: list = [],
        action_items: list = []
    ) -> str:
        pass

        if not sprint_id:
            payload = {"error": "sprint_id is required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", [])
        retrospectives = data.get("retrospectives", [])

        sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            payload = {"error": f"Sprint '{sprint_id}' not found"}
            out = json.dumps(payload)
            return out

        #if sprint.get("status") != "completed":
        #return json.dumps(
        #{"error": "Retrospective can only be created for completed sprints"}
        #)

        if len(what_went_well) < 1:
            payload = {
                    "error": "Retrospective must include at least 3 items for 'what went well'",
                    "current_count": len(what_went_well),
                    "required": 3,
                }
            out = json.dumps(
                payload)
            return out

        if len(what_needs_improvement) < 1:
            payload = {
                    "error": "Retrospective must include at least 3 items for 'what needs improvement'",
                    "current_count": len(what_needs_improvement),
                    "required": 3,
                }
            out = json.dumps(
                payload)
            return out

        #if len(action_items) < 1:
        #return json.dumps(
        #{
        #"error": "Retrospective must include at least 3 action items",
        #"current_count": len(action_items),
        #"required": 3,
        #}
        #)

        if sprint.get("completed_date"):
            try:
                completed_date = datetime.fromisoformat(
                    sprint["completed_date"].replace("Z", "+00:00")
                )
                days_since_completion = (datetime.now() - completed_date).days
                if days_since_completion > 2:
                    payload = {
                            "warning": f"Retrospective is being created {days_since_completion} days after sprint completion",
                        }
                    out = json.dumps(
                        payload)
                    return out
            except:
                pass

        retro_id = f"retro_{uuid.uuid4().hex[:8]}"

        retrospective = {
            "retrospective_id": retro_id,
            "sprint_id": sprint_id,
            "what_went_well": what_went_well,
            "what_needs_improvement": what_needs_improvement,
            "action_items": action_items,
            "created_date": datetime.now().isoformat(),
            "team_id": sprint.get("team_id"),
        }

        retrospectives.append(retrospective)
        payload = {"success": True, "retrospective": retrospective}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSprintRetrospective",
                "description": "Create a retrospective for a completed sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {"type": "string", "description": "The sprint ID"},
                        "what_went_well": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of things that went well (minimum 1)",
                        },
                        "what_needs_improvement": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of areas for improvement (minimum 1)",
                        },
                        "action_items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Action items for next sprint",
                        },
                    },
                    "required": [
                        "sprint_id",
                        "what_went_well",
                        "what_needs_improvement",
                    ],
                },
            },
        }


class GetTaskHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None) -> str:
        if not task_id:
            payload = {"error": "task_id is required"}
            out = json.dumps(payload)
            return out

        task_history = data.get("task_history", [])

        history_entries = [h for h in task_history if h.get("task_id") == task_id]

        history_entries.sort(key=lambda x: x.get("timestamp", ""))
        payload = {
                "task_id": task_id,
                "history_count": len(history_entries),
                "history": history_entries,
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
                "name": "GetTaskHistory",
                "description": "Get the history of changes for a task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to get history for",
                        }
                    },
                    "required": ["task_id"],
                },
            },
        }


class UpdateTaskPriority(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, new_priority: str = None) -> str:
        if not all([task_id, new_priority]):
            payload = {"error": "task_id and new_priority are required"}
            out = json.dumps(payload)
            return out

        if new_priority not in ["low", "medium", "high", "critical"]:
            payload = {"error": "Priority must be one of: low, medium, high, critical"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])
        task_history = data.get("task_history", [])
        employees = data.get("employees", [])

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out

        old_priority = task.get("priority")

        if new_priority == "critical" and old_priority != "critical":
            assignee = next(
                (
                    emp
                    for emp in employees
                    if emp.get("employee_id") == task.get("assignee_id")
                ),
                None,
            )
            if assignee:
                is_senior = any(
                    skill.get("proficiency", 0) >= 4
                    for skill in assignee.get("skills", [])
                )
                if not is_senior:
                    senior_members = [
                        emp
                        for emp in employees
                        if any(
                            skill.get("proficiency", 0) >= 4
                            for skill in emp.get("skills", [])
                        )
                    ]
                    if senior_members:
                        payload = {
                            "error": "Critical tasks must be assigned to senior team members",
                            "current_assignee": assignee.get("name"),
                            "needs_reassignment": True,
                            "available_seniors": [
                                {"id": emp["employee_id"], "name": emp["name"]}
                                for emp in senior_members[:5]
                            ],
                        }
                        out = json.dumps(payload)
                        return out

        history_entry = {
            "history_id": f"hist_{uuid.uuid4().hex[:8]}",
            "task_id": task_id,
            "action": "priority_changed",
            "from_priority": old_priority,
            "to_priority": new_priority,
            "timestamp": datetime.now().isoformat(),
        }
        task_history.append(history_entry)

        task["priority"] = new_priority
        task["updated_date"] = datetime.now().isoformat()
        payload = {
            "success": True,
            "task": task,
            "priority_change": f"{old_priority} -> {new_priority}",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTaskPriority",
                "description": "Update the priority of a task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to update",
                        },
                        "new_priority": {
                            "type": "string",
                            "description": "New priority: low, medium, high, critical",
                        },
                    },
                    "required": ["task_id", "new_priority"],
                },
            },
        }


class GetEmployeeWorkload(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, sprint_id: str = None, include_blocked: bool = True) -> str:
        if not employee_id:
            payload = {"error": "employee_id is required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])

        employee_tasks = [t for t in tasks if t.get("assignee_id") == employee_id]

        if sprint_id:
            employee_tasks = [
                t for t in employee_tasks if t.get("sprint_id") == sprint_id
            ]

        active_tasks = [
            t for t in employee_tasks if t.get("status") in ["in_progress", "todo"]
        ]
        if include_blocked:
            active_tasks.extend(
                [t for t in employee_tasks if t.get("status") == "blocked"]
            )

        total_story_points = sum(t.get("story_points", 0) for t in active_tasks)

        status_breakdown = {
            "todo": len([t for t in employee_tasks if t.get("status") == "todo"]),
            "in_progress": len(
                [t for t in employee_tasks if t.get("status") == "in_progress"]
            ),
            "blocked": len([t for t in employee_tasks if t.get("status") == "blocked"]),
            "done": len([t for t in employee_tasks if t.get("status") == "done"]),
        }

        priority_breakdown = {
            "critical": sum(
                t.get("story_points", 0)
                for t in active_tasks
                if t.get("priority") == "critical"
            ),
            "high": sum(
                t.get("story_points", 0)
                for t in active_tasks
                if t.get("priority") == "high"
            ),
            "medium": sum(
                t.get("story_points", 0)
                for t in active_tasks
                if t.get("priority") == "medium"
            ),
            "low": sum(
                t.get("story_points", 0)
                for t in active_tasks
                if t.get("priority") == "low"
            ),
        }
        payload = {
                "employee_id": employee_id,
                "sprint_id": sprint_id,
                "total_active_story_points": total_story_points,
                "total_tasks": len(employee_tasks),
                "active_tasks": len(active_tasks),
                "status_breakdown": status_breakdown,
                "priority_breakdown": priority_breakdown,
                "workload_rating": (
                    "overloaded"
                    if total_story_points > 25
                    else "high" if total_story_points > 20 else "normal"
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
                "name": "GetEmployeeWorkload",
                "description": "Get current workload for an employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "sprint_id": {
                            "type": "string",
                            "description": "Optional sprint ID to filter by",
                        },
                        "include_blocked": {
                            "type": "boolean",
                            "description": "Include blocked tasks in workload calculation",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }


class BulkMoveTasksToSprint(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_ids: list = None, target_sprint_id: str = None) -> str:
        if task_ids is None:
            task_ids = []

        if not all([task_ids, target_sprint_id]):
            payload = {"error": "task_ids and target_sprint_id are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])
        sprints = data.get("sprints", [])
        teams = data.get("teams", [])

        sprint = next(
            (s for s in sprints if s.get("sprint_id") == target_sprint_id), None
        )
        if not sprint:
            payload = {"error": f"Sprint '{target_sprint_id}' not found"}
            out = json.dumps(payload)
            return out

        if sprint.get("status") not in ["planning", "active"]:
            payload = {
                    "error": f"Cannot add tasks to sprint in '{sprint.get('status')}' status"
                }
            out = json.dumps(
                payload)
            return out

        team = next(
            (t for t in teams if t.get("team_id") == sprint.get("team_id")), None
        )
        if not team:
            payload = {"error": "Sprint team not found"}
            out = json.dumps(payload)
            return out

        team_members = team.get("members", [])

        completed_sprints = [
            s
            for s in sprints
            if s.get("team_id") == team.get("team_id")
            and s.get("status") == "completed"
        ]

        if len(completed_sprints) >= 3:
            recent_sprints = sorted(
                completed_sprints, key=lambda x: x.get("end_date", ""), reverse=True
            )[:3]
            avg_velocity = sum(s.get("velocity", 0) for s in recent_sprints) / 3
            capacity_limit = avg_velocity * 0.8
        else:
            capacity_limit = len(team_members) * 20

        sprint_tasks = [t for t in tasks if t.get("sprint_id") == target_sprint_id]
        current_points = sum(t.get("story_points", 0) for t in sprint_tasks)

        moved_tasks = []
        failed_tasks = []
        total_points_to_add = 0
        assignee_workloads = {}

        for member_id in team_members:
            member_tasks = [
                t for t in sprint_tasks if t.get("assignee_id") == member_id
            ]
            assignee_workloads[member_id] = sum(
                t.get("story_points", 0) for t in member_tasks
            )

        for task_id in task_ids:
            task = next((t for t in tasks if t.get("task_id") == task_id), None)
            if not task:
                failed_tasks.append({"task_id": task_id, "reason": "Task not found"})
                continue

            if task.get("status") == "done":
                failed_tasks.append(
                    {"task_id": task_id, "reason": "Cannot move completed tasks"}
                )
                continue

            if sprint.get("status") == "active" and task.get("priority") != "critical":
                failed_tasks.append(
                    {
                        "task_id": task_id,
                        "reason": "Only critical tasks can be added to active sprints",
                    }
                )
                continue

            task_points = task.get("story_points", 0)

            if current_points + total_points_to_add + task_points > capacity_limit:
                failed_tasks.append(
                    {
                        "task_id": task_id,
                        "reason": f"Would exceed sprint capacity ({capacity_limit} points)",
                    }
                )
                continue

            assignee_id = task.get("assignee_id")
            if assignee_id in assignee_workloads:
                if assignee_workloads[assignee_id] + task_points > 25:
                    failed_tasks.append(
                        {
                            "task_id": task_id,
                            "reason": f"Would exceed 25 point limit for {assignee_id}",
                        }
                    )
                    continue

            old_sprint = task.get("sprint_id")
            total_points_to_add += task_points
            if assignee_id in assignee_workloads:
                assignee_workloads[assignee_id] += task_points

            moved_tasks.append(
                {
                    "task_id": task_id,
                    "from_sprint": old_sprint,
                    "story_points": task_points,
                }
            )

            task["sprint_id"] = target_sprint_id
            task["updated_date"] = datetime.now().isoformat()

        sprint["planned_story_points"] = current_points + total_points_to_add
        payload = {
                "success": True,
                "moved_count": len(moved_tasks),
                "failed_count": len(failed_tasks),
                "total_points_added": total_points_to_add,
                "moved_tasks": moved_tasks,
                "failed_tasks": failed_tasks,
                "sprint_total_points": sprint["planned_story_points"],
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BulkMoveTasksToSprint",
                "description": "Move multiple tasks to a sprint at once",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of task IDs to move",
                        },
                        "target_sprint_id": {
                            "type": "string",
                            "description": "Target sprint ID",
                        },
                    },
                    "required": ["task_ids", "target_sprint_id"],
                },
            },
        }


class CloneTask(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        source_task_id: str = None,
        new_title: str = None,
        new_assignee_id: str = None,
        sprint_id: str = None,
        new_task_id: str = None
    ) -> str:
        if not all([source_task_id, new_title]):
            payload = {"error": "source_task_id and new_title are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])
        employees = data.get("employees", [])
        sprints = data.get("sprints", [])

        source_task = next(
            (t for t in tasks if t.get("task_id") == source_task_id), None
        )
        if not source_task:
            payload = {"error": f"Source task '{source_task_id}' not found"}
            out = json.dumps(payload)
            return out

        assignee_id = new_assignee_id or source_task.get("assignee_id")

        assignee = next(
            (emp for emp in employees if emp.get("employee_id") == assignee_id), None
        )
        if not assignee:
            payload = {"error": f"Assignee '{assignee_id}' not found"}
            out = json.dumps(payload)
            return out

        if source_task.get("priority") == "critical":
            is_senior = any(
                skill.get("proficiency", 0) >= 4 for skill in assignee.get("skills", [])
            )
            if not is_senior:
                senior_members = [
                    emp
                    for emp in employees
                    if any(
                        skill.get("proficiency", 0) >= 4
                        for skill in emp.get("skills", [])
                    )
                ]
                if senior_members:
                    payload = {
                            "error": "Critical tasks must be assigned to senior team members",
                            "available_seniors": [
                                {"id": emp["employee_id"], "name": emp["name"]}
                                for emp in senior_members[:5]
                            ],
                        }
                    out = json.dumps(
                        payload)
                    return out

        story_points = source_task.get("story_points", 3)
        if sprint_id:
            sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)
            if sprint and sprint.get("status") == "active":
                assignee_tasks = [
                    t
                    for t in tasks
                    if t.get("assignee_id") == assignee_id
                    and t.get("sprint_id") == sprint_id
                    and t.get("status") != "done"
                ]
                current_points = sum(t.get("story_points", 0) for t in assignee_tasks)

                if current_points + story_points > 25:
                    payload = {
                            "error": "Cannot assign task. Would exceed 25 story point limit",
                            "current_points": current_points,
                            "new_task_points": story_points,
                        }
                    out = json.dumps(
                        payload)
                    return out

        task_id = f"task_{uuid.uuid4().hex[:8]}"

        if new_task_id:
            for t in tasks:
                if t.get("task_id") == new_task_id:
                    payload = {
                            "error": f"new_task_id {new_task_id} exists. Please enter a unique task_id."
                        }
                    out = json.dumps(
                        payload)
                    return out
            task_id = new_task_id

        new_task = {
            "task_id": task_id,
            "title": new_title,
            "description": source_task.get("description", ""),
            "assignee_id": assignee_id,
            "status": "todo",
            "priority": source_task.get("priority", "medium"),
            "story_points": story_points,
            "sprint_id": sprint_id,
            "dependencies": [],
            "blocked_by": [],
            "created_date": datetime.now().isoformat(),
            "updated_date": datetime.now().isoformat(),
            "completed_date": None,
            "time_logged": 0,
            "cloned_from": source_task_id,
        }

        tasks.append(new_task)
        payload = {"success": True, "new_task": new_task, "source_task_id": source_task_id}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CloneTask",
                "description": "Create a copy of an existing task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_task_id": {
                            "type": "string",
                            "description": "Task ID to clone from",
                        },
                        "new_title": {
                            "type": "string",
                            "description": "Title for the new task",
                        },
                        "new_assignee_id": {
                            "type": "string",
                            "description": "Optional new assignee (defaults to source task assignee)",
                        },
                        "sprint_id": {
                            "type": "string",
                            "description": "Optional sprint to assign to",
                        },
                        "new_task_id": {
                            "type": "string",
                            "description": "Optional task_id",
                        },
                    },
                    "required": ["source_task_id", "new_title"],
                },
            },
        }


class ResolveBlockedTask(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str, resolution: str, unblock_dependencies: bool = False) -> str:
        if not all([task_id, resolution]):
            payload = {"error": "task_id and resolution are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])
        task_history = data.get("task_history", [])

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out

        #if task.get("status") != "blocked":
        #return json.dumps({"error": "Task is not in blocked status"})

        unresolved_deps = []

        if unblock_dependencies:
            task["blocked_by"] = []
        else:
            for dep_id in task.get("dependencies", []):
                dep_task = next((t for t in tasks if t.get("task_id") == dep_id), None)

                if dep_task and dep_task.get("status") != "done":
                    unresolved_deps.append(dep_id)

        if unresolved_deps:
            payload = {
                    "error": "Cannot unblock task - dependencies not resolved",
                    "unresolved_dependencies": unresolved_deps,
                }
            out = json.dumps(
                payload)
            return out

        history_entry = {
            "history_id": f"hist_{uuid.uuid4().hex[:8]}",
            "task_id": task_id,
            "action": "unblocked",
            "resolution": resolution,
            "timestamp": datetime.now().isoformat(),
        }
        task_history.append(history_entry)

        task["status"] = "todo"
        task["blocked_date"] = None
        task["updated_date"] = datetime.now().isoformat()

        if task.get("escalated"):
            escalations = data.get("escalations", [])
            for esc in escalations:
                if esc.get("task_id") == task_id and not esc.get("resolved"):
                    esc["resolved"] = True
                    esc["resolution_date"] = datetime.now().isoformat()
                    esc["resolution"] = resolution
        payload = {"success": True, "task": task, "resolution": resolution}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ResolveBlockedTask",
                "description": "Resolve a blocked task and move it back to todo",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The blocked task ID",
                        },
                        "resolution": {
                            "type": "string",
                            "description": "How the block was resolved",
                        },
                        "unblock_dependencies": {
                            "type": "boolean",
                            "description": "Force unblock even if dependencies aren't resolved",
                        },
                    },
                    "required": ["task_id", "resolution"],
                },
            },
        }


class GenerateSprintReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None) -> str:
        if not sprint_id:
            payload = {"error": "sprint_id is required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", [])
        tasks = data.get("tasks", [])
        time_logs = data.get("time_logs", [])

        sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            payload = {"error": f"Sprint '{sprint_id}' not found"}
            out = json.dumps(payload)
            return out

        sprint_tasks = [t for t in tasks if t.get("sprint_id") == sprint_id]

        total_tasks = len(sprint_tasks)
        completed_tasks = [t for t in sprint_tasks if t.get("status") == "done"]
        blocked_tasks = [t for t in sprint_tasks if t.get("status") == "blocked"]

        sprint_time_logs = [
            log
            for log in time_logs
            if any(t.get("task_id") == log.get("task_id") for t in sprint_tasks)
        ]
        #total_hours_logged = sum(log.get("hours", 0) for log in sprint_time_logs)

        assignee_performance = {}
        for task in sprint_tasks:
            assignee = task.get("assignee_id")
            if assignee not in assignee_performance:
                assignee_performance[assignee] = {
                    "completed_points": 0,
                    "total_points": 0,
                    "completed_tasks": 0,
                    "total_tasks": 0,
                }

            assignee_performance[assignee]["total_tasks"] += 1
            assignee_performance[assignee]["total_points"] += task.get(
                "story_points", 0
            )

            if task.get("status") == "done":
                assignee_performance[assignee]["completed_tasks"] += 1
                assignee_performance[assignee]["completed_points"] += task.get(
                    "story_points", 0
                )

        compliance_issues = []

        for task in sprint_tasks:
            if task.get("status") in ["in_progress", "done"]:
                task_logs = [
                    log
                    for log in sprint_time_logs
                    if log.get("task_id") == task.get("task_id")
                ]
                if task.get("status") == "done":
                    required_hours = task.get("story_points", 0) * 2 * 0.5
                    logged_hours = sum(log.get("hours", 0) for log in task_logs)
                    if logged_hours < required_hours:
                        compliance_issues.append(
                            {
                                "type": "insufficient_time_logged",
                                "task_id": task.get("task_id"),
                                "required_hours": required_hours,
                                "logged_hours": logged_hours,
                            }
                        )

        risks = []
        if len(blocked_tasks) > total_tasks * 0.2:
            risks.append("High number of blocked tasks (>20%)")
        if (
            sprint.get("status") == "active"
            and sprint.get("completed_story_points", 0)
            < sprint.get("planned_story_points", 0) * 0.3
        ):
            risks.append("Low completion rate for active sprint")

        report = {
            "compliance_issues": compliance_issues,
            "sprint_id": sprint_id,
            "sprint_name": sprint.get("sprint_name"),
            "status": sprint.get("status"),
            "metrics": {
                "planned_story_points": sprint.get("planned_story_points", 0),
                #"total_hours_logged": total_hours_logged,
                "total_tasks": total_tasks,
                "completed_tasks": len(completed_tasks),
                "blocked_tasks": len(blocked_tasks),
                "completion_percentage": (
                    round((len(completed_tasks) / total_tasks * 100), 1)
                    if total_tasks > 0
                    else 0
                ),
                "completed_story_points": sprint.get("completed_story_points", 0),
                "velocity": sprint.get("velocity", 0),
            },
            "team_performance": assignee_performance,
            "blocked_task_details": [
                {
                    "task_id": t.get("task_id"),
                    "title": t.get("title"),
                    "assignee": t.get("assignee_id"),
                }
                for t in blocked_tasks
            ],
            "risks": risks,
            "report_generated": datetime.now().isoformat(),
        }
        payload = report
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateSprintReport",
                "description": "Generate a comprehensive report for a sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {
                            "type": "string",
                            "description": "The sprint ID to generate report for",
                        }
                    },
                    "required": ["sprint_id"],
                },
            },
        }


class CheckBlockedTasksForEscalation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], check_all_sprints: bool = True, sprint_id: str = None) -> str:
        tasks = data.get("tasks", [])
        task_history = data.get("task_history", [])

        if sprint_id:
            tasks_to_check = [t for t in tasks if t.get("sprint_id") == sprint_id]
        elif check_all_sprints:
            tasks_to_check = tasks
        else:
            payload = {
                "error": "Either check_all_sprints must be True or sprint_id must be provided"
            }
            out = json.dumps(payload)
            return out

        blocked_tasks = [t for t in tasks_to_check if t.get("status") == "blocked"]

        tasks_needing_escalation = []

        for task in blocked_tasks:
            if task.get("escalated", False):
                continue

            task_id = task.get("task_id")
            blocked_history = [
                h
                for h in task_history
                if h.get("task_id") == task_id
                and h.get("action") == "status_changed"
                and h.get("to_status") == "blocked"
            ]

            days_blocked = "2+"
            if blocked_history:
                blocked_history.sort(key=lambda x: x.get("timestamp", ""), reverse=True)

                days_blocked = "365+"

            tasks_needing_escalation.append(
                {
                    "task_id": task.get("task_id"),
                    "title": task.get("title"),
                    "assignee_id": task.get("assignee_id"),
                    "days_blocked": days_blocked,
                    "current_priority": task.get("priority"),
                }
            )
        payload = {
            "total_blocked_tasks": len(blocked_tasks),
            "tasks_needing_escalation": len(tasks_needing_escalation),
            "tasks": tasks_needing_escalation,
        }
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckBlockedTasksForEscalation",
                "description": "Check for blocked tasks that need escalation (blocked > 2 days)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "check_all_sprints": {
                            "type": "boolean",
                            "description": "Check all sprints (default: True)",
                        },
                        "sprint_id": {
                            "type": "string",
                            "description": "Specific sprint to check",
                        },
                    },
                },
            },
        }


class CheckTimeLoggingCompliance(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None, check_all: bool = False) -> str:
        tasks = data.get("tasks", [])
        time_logs = data.get("time_logs", [])

        if sprint_id:
            tasks_to_check = [t for t in tasks if t.get("sprint_id") == sprint_id]
        elif check_all:
            tasks_to_check = tasks
        else:
            payload = {"error": "Either sprint_id must be provided or check_all must be True"}
            out = json.dumps(payload)
            return out

        non_compliant_tasks = []

        for task in tasks_to_check:
            if task.get("status") in ["in_progress", "done"]:
                last_logged = task.get("last_time_logged")
                if last_logged:
                    try:
                        last_logged_date = datetime.fromisoformat(
                            last_logged.replace("Z", "+00:00")
                        )
                        days_since_logged = (datetime.now() - last_logged_date).days

                        if days_since_logged > 2:
                            non_compliant_tasks.append(
                                {
                                    "task_id": task.get("task_id"),
                                    "title": task.get("title"),
                                    "assignee_id": task.get("assignee_id"),
                                    "status": task.get("status"),
                                    "days_since_logged": days_since_logged,
                                    "issue": "No time logged in over 2 days",
                                }
                            )
                    except:
                        pass
                else:
                    non_compliant_tasks.append(
                        {
                            "task_id": task.get("task_id"),
                            "title": task.get("title"),
                            "assignee_id": task.get("assignee_id"),
                            "status": task.get("status"),
                            "issue": "No time ever logged",
                        }
                    )

                if task.get("status") == "done":
                    task_logs = [
                        log
                        for log in time_logs
                        if log.get("task_id") == task.get("task_id")
                    ]
                    total_hours = sum(log.get("hours", 0) for log in task_logs)
                    required_hours = task.get("story_points", 0) * 2 * 0.5

                    if total_hours < required_hours:
                        existing = next(
                            (
                                t
                                for t in non_compliant_tasks
                                if t["task_id"] == task["task_id"]
                            ),
                            None,
                        )
                        if existing:
                            existing["insufficient_hours"] = {
                                "logged": total_hours,
                                "required": required_hours,
                            }
                        else:
                            non_compliant_tasks.append(
                                {
                                    "task_id": task.get("task_id"),
                                    "title": task.get("title"),
                                    "assignee_id": task.get("assignee_id"),
                                    "status": "done",
                                    "issue": "Insufficient hours logged",
                                    "insufficient_hours": {
                                        "logged": total_hours,
                                        "required": required_hours,
                                    },
                                }
                            )
        payload = {
            "tasks_checked": len(tasks_to_check),
            "non_compliant_count": len(non_compliant_tasks),
            "non_compliant_tasks": non_compliant_tasks,
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
                "name": "CheckTimeLoggingCompliance",
                "description": "Check time logging compliance for tasks",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {
                            "type": "string",
                            "description": "Sprint ID to check",
                        },
                        "check_all": {
                            "type": "boolean",
                            "description": "Check all tasks regardless of sprint",
                        },
                    },
                },
            },
        }


TOOLS = [
    SearchTasks(),
    CreateTask(),
    GetTaskDetails(),
    UpdateTaskStatus(),
    CreateSprint(),
    AssignTaskToSprint(),
    GetSprintDetails(),
    CalculateSprintBurndown(),
    ReassignTask(),
    UpdateSprintStatus(),
    GetTeamVelocity(),
    CreateTaskDependency(),
    GetBacklogTasks(),
    LogTimeOnTask(),
    EscalateTask(),
    CalculateTeamCapacity(),
    CreateSprintRetrospective(),
    GetTaskHistory(),
    UpdateTaskPriority(),
    GetEmployeeWorkload(),
    BulkMoveTasksToSprint(),
    CloneTask(),
    ResolveBlockedTask(),
    GenerateSprintReport(),
    CheckBlockedTasksForEscalation(),
    CheckTimeLoggingCompliance(),
    MarkSprintAsReviewed(),
]
