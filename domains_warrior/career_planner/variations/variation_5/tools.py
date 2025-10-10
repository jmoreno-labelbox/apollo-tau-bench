import json
from typing import Any, Dict, List
from domains.dto import Tool


# Basic utility tools
class get_today_date(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        return json.dumps({"today": "2025-10-02"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_today_date",
                "description": "Get today's date",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class get_user_id_from_name(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], first_name: str, last_name: str) -> str:
        users = data.get("users", [])
        full_name = f"{first_name} {last_name}"
        for user in users:
            if user.get("name") == full_name:
                return json.dumps({"user_id": user["user_id"]}, indent=2)
        return json.dumps({"error": "User not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_user_id_from_name",
                "description": "Get user ID from first and last name",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                    },
                    "required": ["first_name", "last_name"],
                },
            },
        }


class get_course_id_by_name(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], course_name: str) -> str:
        courses = data.get("course_catalog", [])
        # Find a course where the name contains the provided string (case-insensitive)
        course = next(
            (c for c in courses if course_name.lower() in c.get("name", "").lower()),
            None,
        )
        if course:
            return json.dumps({"course_id": course["course_id"]}, indent=2)
        return json.dumps(
            {"error": f"Course with name containing '{course_name}' not found"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_course_id_by_name",
                "description": "Find a course ID by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "course_name": {
                            "type": "string",
                            "description": "The name or partial name of the course to find.",
                        }
                    },
                    "required": ["course_name"],
                },
            },
        }


class get_goal_id_by_description(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, keyword: str) -> str:
        goals_data = data.get("goals", [])
        user_goals_obj = next(
            (g for g in goals_data if g.get("user_id") == user_id), None
        )
        if user_goals_obj:
            # Find a goal where the description contains the keyword (case-insensitive)
            goal = next(
                (
                    g
                    for g in user_goals_obj.get("goals", [])
                    if keyword.lower() in g.get("goal_description", "").lower()
                ),
                None,
            )
            if goal:
                return json.dumps({"goal_id": goal["goal_id"]}, indent=2)
        return json.dumps(
            {
                "error": f"Goal for user {user_id} containing keyword '{keyword}' not found"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_goal_id_by_description",
                "description": "Find a user's goal ID by searching for a keyword in the goal's description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "keyword": {
                            "type": "string",
                            "description": "A keyword to search for in the goal descriptions.",
                        },
                    },
                    "required": ["user_id", "keyword"],
                },
            },
        }


class get_team_id_by_name(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_name: str) -> str:
        teams = data.get("teams", [])
        team = next(
            (t for t in teams if t.get("team_name", "").lower() == team_name.lower()),
            None,
        )
        if team:
            return json.dumps({"team_id": team["team_id"]}, indent=2)
        return json.dumps(
            {"error": f"Team with name '{team_name}' not found"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_team_id_by_name",
                "description": "Find a team ID by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_name": {"type": "string"}},
                    "required": ["team_name"],
                },
            },
        }


class find_hr_workflow_for_user(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        workflows = data.get("hr_workflows", [])
        # A user can be the primary employee or a candidate in a workflow
        workflow = next(
            (
                w
                for w in workflows
                if w.get("employee_id") == user_id
                or user_id in [c.get("employee_id") for c in w.get("candidates", [])]
            ),
            None,
        )
        if workflow:
            return json.dumps({"workflow_id": workflow["workflow_id"]}, indent=2)
        return json.dumps({"error": f"Workflow for user {user_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "find_hr_workflow_for_user",
                "description": "Find an HR workflow associated with a specific user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class search_users(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], filters: dict) -> str:
        users = data.get("users", [])
        if "user_id" in filters:
            user = next(
                (u for u in users if u.get("user_id") == filters["user_id"]), None
            )
            return (
                json.dumps(user, indent=2)
                if user
                else json.dumps({"error": "User not found"}, indent=2)
            )
        return json.dumps({"users": users}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "search_users",
                "description": "Search for users by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }


class get_course(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], course_id: str) -> str:
        courses = data.get("course_catalog", [])
        course = next((c for c in courses if c.get("course_id") == course_id), None)
        return (
            json.dumps(course, indent=2)
            if course
            else json.dumps({"error": "Course not found"}, indent=2)
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_course",
                "description": "Get course details by course ID",
                "parameters": {
                    "type": "object",
                    "properties": {"course_id": {"type": "string"}},
                    "required": ["course_id"],
                },
            },
        }


class enroll_in_course(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], user_id: str, course_id: str, enroll_date: str
    ) -> str:
        enrollment = {
            "user_id": user_id,
            "course_id": course_id,
            "status": "Enrolled",
            "start_date": enroll_date,
            "completion_date": None,
            "current_progress_percent": 0,
        }
        data.setdefault("user_course_progress", []).append(enrollment)
        return json.dumps(
            {"success": f"User {user_id} enrolled in course {course_id}"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "enroll_in_course",
                "description": "Enroll a user in a course",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "enroll_date": {"type": "string"},
                    },
                    "required": ["user_id", "course_id", "enroll_date"],
                },
            },
        }


class list_user_courses(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        courses = [
            c
            for c in data.get("user_course_progress", [])
            if c.get("user_id") == user_id
        ]
        return json.dumps({"courses": courses}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_courses",
                "description": "List all courses for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class get_user_course_progress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, course_id: str) -> str:
        progress = next(
            (
                p
                for p in data.get("user_course_progress", [])
                if p.get("user_id") == user_id and p.get("course_id") == course_id
            ),
            None,
        )
        return (
            json.dumps(progress, indent=2)
            if progress
            else json.dumps({"error": "Course progress not found"}, indent=2)
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_user_course_progress",
                "description": "Get course progress for a specific user and course",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                    },
                    "required": ["user_id", "course_id"],
                },
            },
        }


class update_user_course_progress(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], user_id: str, course_id: str, updates: Dict[str, Any]
    ) -> str:
        rec = next(
            (
                r
                for r in data.get("user_course_progress", [])
                if r["user_id"] == user_id and r["course_id"] == course_id
            ),
            None,
        )
        if rec:
            rec.update(updates)
            return json.dumps({"success": "course progress updated"})
        return json.dumps({"error": "course enrollment not found"})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_user_course_progress",
                "description": "Update an existing course-progress record for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["user_id", "course_id", "updates"],
                },
            },
        }


class compute_average_progress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        """Return the average completion percentage across all courses for a user."""
        records = [
            rec
            for rec in data.get("user_course_progress", [])
            if rec["user_id"] == user_id
        ]
        if not records:
            return json.dumps({"average_progress": 0})
        total, count = 0, 0
        for rec in records:
            if rec.get("status") == "Completed":
                total += 100
            else:
                total += rec.get("current_progress_percent", 0)
            count += 1
        avg = round(total / count, 2)
        return json.dumps({"average_progress": avg})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_average_progress",
                "description": "Calculate a user's average course completion percentage across all enrollments.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class list_user_goals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), {})
        goals = user_goals.get("goals", [])
        return json.dumps({"user_id": user_id, "goals": goals}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_goals",
                "description": "List all goals for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class get_goal(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, goal_id: str) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), {})
        goals = user_goals.get("goals", [])
        goal = next((g for g in goals if g.get("goal_id") == goal_id), None)
        return (
            json.dumps(goal, indent=2)
            if goal
            else json.dumps({"error": "Goal not found"}, indent=2)
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_goal",
                "description": "Get goal details for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "goal_id": {"type": "string"},
                    },
                    "required": ["user_id", "goal_id"],
                },
            },
        }


class add_goal(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, goal: Dict[str, Any]) -> str:
        """Append a new goal to a user's record."""
        for entry in data.get("goals", []):
            if entry["user_id"] == user_id:
                entry["goals"].append(goal)
                break
        else:  # no existing goal list for this user
            data.setdefault("goals", []).append({"user_id": user_id, "goals": [goal]})
        return json.dumps({"success": f"goal {goal['goal_id']} added for {user_id}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_goal",
                "description": "Add a new goal object to the specified user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "goal": {"type": "object"},
                    },
                    "required": ["user_id", "goal"],
                },
            },
        }


class update_goal(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, goal_id: str, updates: dict) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), None)
        if user_goals:
            goals = user_goals.get("goals", [])
            goal = next((g for g in goals if g.get("goal_id") == goal_id), None)
            if goal:
                if "notes_append" in updates:
                    goal["notes"] = (
                        goal.get("notes", "") + " " + updates.pop("notes_append")
                    )
                goal.update(updates)
                return json.dumps(
                    {"success": f"Goal {goal_id} updated for user {user_id}"}, indent=2
                )
        return json.dumps({"error": "Goal not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "update_goal",
                "description": "Update goal details for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "goal_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["user_id", "goal_id", "updates"],
                },
            },
        }


class get_team(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        return (
            json.dumps(team, indent=2)
            if team
            else json.dumps({"error": "Team not found"}, indent=2)
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_team",
                "description": "Get team details by team ID",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class add_team_member(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str, user_id: str) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if team:
            team_members = team.setdefault("team_members", [])
            if user_id not in team_members:
                team_members.append(user_id)
                return json.dumps(
                    {"success": f"User {user_id} added to team {team_id}"}, indent=2
                )
            else:
                return json.dumps(
                    {"success": f"User {user_id} already in team {team_id}"}, indent=2
                )
        return json.dumps({"error": "Team not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "add_team_member",
                "description": "Add a team member to a team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "user_id": {"type": "string"},
                    },
                    "required": ["team_id", "user_id"],
                },
            },
        }


class get_skill_gap_analysis(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], analysis_id: str = "", user_id: str = "") -> str:
        analyses = data.get("skill_gap_analysis", [])
        if analysis_id:
            analysis = next(
                (a for a in analyses if a.get("analysis_id") == analysis_id), None
            )
        elif user_id:
            analysis = next((a for a in analyses if a.get("user_id") == user_id), None)
        else:
            return json.dumps(
                {"error": "Must provide either analysis_id or user_id"}, indent=2
            )
        return (
            json.dumps(analysis, indent=2)
            if analysis
            else json.dumps({"error": "Analysis not found"}, indent=2)
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_skill_gap_analysis",
                "description": "Get skill gap analysis by ID or user ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "analysis_id": {"type": "string"},
                        "user_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class list_user_mentorships(Tool):
    @staticmethod
    def invoke(data, user_id: str) -> str:
        rels = [
            rel
            for rel in data.get("user_mentorship_relationships", [])
            if rel.get("mentee_id") == user_id
        ]
        return json.dumps({"mentorships": rels}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_mentorships",
                "description": "List all mentorship relationships for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class add_mentorship_relationship(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        mentor_id: str,
        mentee_id: str,
        start_date: str,
        status: str,
        focus_areas: List[str],
    ) -> str:
        relationships = data.setdefault("user_mentorship_relationships", [])

        # --- Auto-generation logic for relationship_id ---
        if not relationships:
            new_id_num = 1
        else:
            # Find the highest existing ID number to avoid collisions
            max_id = 0
            for rel in relationships:
                try:
                    num = int(rel["relationship_id"][2:])  # Assumes format MR###
                    if num > max_id:
                        max_id = num
                except (ValueError, IndexError):
                    continue  # Skip malformed IDs
            new_id_num = max_id + 1

        new_relationship_id = f"MR{new_id_num:03d}"  # Formats as MR001, MR015, etc.

        new_relationship = {
            "relationship_id": new_relationship_id,
            "mentor_id": mentor_id,
            "mentee_id": mentee_id,
            "start_date": start_date,
            "status": status,
            "focus_areas": focus_areas,
        }

        relationships.append(new_relationship)

        return json.dumps(
            {
                "success": f"Mentorship relationship {new_relationship_id} created",
                "relationship_id": new_relationship_id,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "add_mentorship_relationship",
                "description": "Create a new mentorship relationship with an auto-generated ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mentor_id": {"type": "string"},
                        "mentee_id": {"type": "string"},
                        "start_date": {"type": "string"},
                        "status": {"type": "string"},
                        "focus_areas": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "mentor_id",
                        "mentee_id",
                        "start_date",
                        "status",
                        "focus_areas",
                    ],
                },
            },
        }


class update_mentorship_relationship(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], relationship_id: str, updates: Dict[str, Any]
    ) -> str:
        rel = next(
            (
                r
                for r in data.get("user_mentorship_relationships", [])
                if r["relationship_id"] == relationship_id
            ),
            None,
        )
        if not rel:
            return json.dumps({"error": "relationship not found"})

        # --- SIMPLIFIED LOGIC ---
        # The tool now only performs a direct update.
        rel.update(updates)
        # --- END OF SIMPLIFICATION ---

        return json.dumps({"success": f"relationship {relationship_id} updated"})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_mentorship_relationship",
                "description": "Modify attributes of an existing mentorship relationship by overwriting them with new values.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "relationship_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["relationship_id", "updates"],
                },
            },
        }


class schedule_mentorship_session(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], relationship_id: str, session_date: str) -> str:
        sessions = data.setdefault("scheduled_mentorship_sessions", [])
        sessions.append(
            {
                "relationship_id": relationship_id,
                "session_date": session_date,
                "status": "Scheduled",
            }
        )
        return json.dumps({"scheduled_for": session_date})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "schedule_mentorship_session",
                "description": "Schedule a mentorship session for an existing relationship.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "relationship_id": {"type": "string"},
                        "session_date": {"type": "string"},
                    },
                    "required": ["relationship_id", "session_date"],
                },
            },
        }


class compute_mentor_load(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], mentor_id: str) -> str:
        """Count active mentees for a mentor."""
        count = sum(
            1
            for rel in data.get("user_mentorship_relationships", [])
            if rel["mentor_id"] == mentor_id and rel["status"] == "Active"
        )
        return json.dumps({"current_mentees": count})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_mentor_load",
                "description": "Return the number of active mentees a mentor currently has.",
                "parameters": {
                    "type": "object",
                    "properties": {"mentor_id": {"type": "string"}},
                    "required": ["mentor_id"],
                },
            },
        }


class get_hr_workflow(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], workflow_id: str) -> str:
        workflow = next(
            (
                w
                for w in data.get("hr_workflows", [])
                if w.get("workflow_id") == workflow_id
            ),
            None,
        )
        return (
            json.dumps(workflow, indent=2)
            if workflow
            else json.dumps({"error": "Workflow not found"}, indent=2)
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_hr_workflow",
                "description": "Get HR workflow details by workflow ID",
                "parameters": {
                    "type": "object",
                    "properties": {"workflow_id": {"type": "string"}},
                    "required": ["workflow_id"],
                },
            },
        }


class update_hr_workflow(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], workflow_id: str, updates: Dict[str, Any]) -> str:
        wf = next(
            (
                w
                for w in data.get("hr_workflows", [])
                if w["workflow_id"] == workflow_id
            ),
            None,
        )
        if not wf:
            return json.dumps({"error": "workflow not found"})

        if "notes_append" in updates:
            wf["notes"] = wf.get("notes", "") + " " + updates.pop("notes_append")

        wf.update(updates)
        return json.dumps({"success": f"workflow {workflow_id} updated"})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_hr_workflow",
                "description": "Update fields of an existing HR workflow record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "workflow_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["workflow_id", "updates"],
                },
            },
        }


class add_user_certification(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, cert: dict) -> str:
        cert["user_id"] = user_id
        data.setdefault("user_certification", []).append(cert)
        return json.dumps(
            {"success": f"Certification {cert['cert_name']} added for user {user_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "add_user_certification",
                "description": "Add a certification for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "cert": {"type": "object"},
                    },
                    "required": ["user_id", "cert"],
                },
            },
        }


class notify_hr(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], message: str) -> str:
        data.setdefault("hr_notifications", []).append({"message": message})
        return json.dumps({"notified": "HR", "message": message})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "notify_hr",
                "description": "Send an informational notification to the HR team.",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }


class notify_user(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, message: str) -> str:
        data.setdefault("user_notifications", []).append(
            {"user_id": user_id, "message": message}
        )
        return json.dumps({"notified_user": user_id})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "notify_user",
                "description": "Push a notification message to an individual user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["user_id", "message"],
                },
            },
        }


# All tools registry
TOOLS = [
    get_today_date(),
    get_user_id_from_name(),
    get_course_id_by_name(),
    get_goal_id_by_description(),
    get_team_id_by_name(),
    find_hr_workflow_for_user(),
    search_users(),
    get_course(),
    enroll_in_course(),
    list_user_courses(),
    get_user_course_progress(),
    update_user_course_progress(),
    compute_average_progress(),
    list_user_goals(),
    get_goal(),
    add_goal(),
    update_goal(),
    get_team(),
    add_team_member(),
    get_skill_gap_analysis(),
    list_user_mentorships(),
    add_mentorship_relationship(),
    update_mentorship_relationship(),
    schedule_mentorship_session(),
    compute_mentor_load(),
    get_hr_workflow(),
    update_hr_workflow(),
    add_user_certification(),
    notify_hr(),
    notify_user(),
]
