import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


#Fundamental utility functions
class GetTodayDate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = {"today": "2025-10-02"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getTodayDate",
                "description": "Get today's date",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class GetUserIdFromName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], first_name: str, last_name: str) -> str:
        users = data.get("users", {}).values()
        full_name = f"{first_name} {last_name}"
        for user in users.values():
            if user.get("name") == full_name:
                payload = {"user_id": user["user_id"]}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getUserIdFromName",
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


class GetCourseIdByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], course_name: str) -> str:
        _course_nameL = course_name or ''.lower()
        pass
        courses = data.get("course_catalog", {}).values()
        # Locate a course whose name includes the specified string (case-insensitive)
        course = next(
            (c for c in courses.values() if course_name.lower() in c.get("name", "").lower()),
            None,
        )
        if course:
            payload = {"course_id": course["course_id"]}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Course with name containing '{course_name}' not found"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getCourseIdByName",
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


class GetGoalIdByDescription(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, keyword: str) -> str:
        _keywordL = keyword or ''.lower()
        pass
        goals_data = data.get("goals", {}).values()
        user_goals_obj = next(
            (g for g in goals_data.values() if g.get("user_id") == user_id), None
        )
        if user_goals_obj:
            # Identify a goal with a description that includes the keyword (case-insensitive)
            goal = next(
                (
                    g
                    for g in user_goals_obj.get("goals", [])
                    if keyword.lower() in g.get("goal_description", "").lower()
                ),
                None,
            )
            if goal:
                payload = {"goal_id": goal["goal_id"]}
                out = json.dumps(payload, indent=2)
                return out
        payload = {
            "error": f"Goal for user {user_id} containing keyword '{keyword}' not found"
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getGoalIdByDescription",
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


class GetTeamIdByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_name: str) -> str:
        _team_nameL = team_name or ''.lower()
        pass
        teams = data.get("teams", {}).values()
        team = next(
            (t for t in teams.values() if t.get("team_name", "").lower() == team_name.lower()),
            None,
        )
        if team:
            payload = {"team_id": team["team_id"]}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Team with name '{team_name}' not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getTeamIdByName",
                "description": "Find a team ID by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_name": {"type": "string"}},
                    "required": ["team_name"],
                },
            },
        }


class FindHrWorkflowForUser(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: Any = None
    ) -> str:
        hr_workflows = data.get("hr_workflows", {}).values()
        # A user may serve as the main employee or a candidate within a workflow
        workflow = next(
            (
                w
                for w in hr_workflows.values() if w.get("employee_id") == user_id
                or user_id in [c.get("employee_id") for c in w.get("candidates", [])]
            ),
            None,
        )
        if workflow:
            payload = {"workflow_id": workflow["workflow_id"]}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Workflow for user {user_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "findHrWorkflowForUser",
                "description": "Find an HR workflow associated with a specific user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class SearchUsers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], filters: dict = None) -> str:
        users = data.get("users", {}).values()
        if filters and "user_id" in filters:
            user = next(
                (u for u in users.values() if u.get("user_id") == filters["user_id"]), None
            )
            return (
                json.dumps(user, indent=2)
                if user
                else json.dumps({"error": "User not found"}, indent=2)
            )
        payload = {"users": users}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "searchUsers",
                "description": "Search for users by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }


class GetCourse(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], course_id: str) -> str:
        courses = data.get("course_catalog", {}).values()
        course = next((c for c in courses.values() if c.get("course_id") == course_id), None)
        return (
            json.dumps(course, indent=2)
            if course
            else json.dumps({"error": "Course not found"}, indent=2)
        )
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getCourse",
                "description": "Get course details by course ID",
                "parameters": {
                    "type": "object",
                    "properties": {"course_id": {"type": "string"}},
                    "required": ["course_id"],
                },
            },
        }


class EnrollInCourse(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str, course_id: str, enroll_date: str
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
        payload = {"success": f"User {user_id} enrolled in course {course_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out


    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "enrollInCourse",
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


class ListUserCourses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        courses = [
            c
            for c in data.get("user_course_progress", {}).values()
            if c.get("user_id") == user_id
        ]
        payload = {"courses": courses}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listUserCourses",
                "description": "List all courses for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class GetUserCourseProgress(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, course_id: str) -> str:
        progress = next(
            (
                p
                for p in data.get("user_course_progress", {}).values()
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
        pass
        return {
            "type": "function",
            "function": {
                "name": "getUserCourseProgress",
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


class UpdateUserCourseProgress(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str, course_id: str, updates: dict[str, Any]
    ) -> str:
        rec = next(
            (
                r
                for r in data.get("user_course_progress", {}).values()
                if r["user_id"] == user_id and r["course_id"] == course_id
            ),
            None,
        )
        if rec:
            rec.update(updates)
            payload = {"success": "course progress updated"}
            out = json.dumps(payload)
            return out
        payload = {"error": "course enrollment not found"}
        out = json.dumps(payload)
        return out


    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateUserCourseProgress",
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


class ComputeAverageProgress(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        """Provide the average completion rate for all courses associated with a user."""
        records = [
            rec
            for rec in data.get("user_course_progress", {}).values()
            if rec["user_id"] == user_id
        ]
        if not records:
            payload = {"average_progress": 0}
            out = json.dumps(payload)
            return out
        total, count = 0, 0
        for rec in records:
            if rec.get("status") == "Completed":
                total += 100
            else:
                total += rec.get("current_progress_percent", 0)
            count += 1
        avg = round(total / count, 2)
        payload = {"average_progress": avg}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "computeAverageProgress",
                "description": "Calculate a user's average course completion percentage across all enrollments.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class ListUserGoals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        goals_data = data.get("goals", {}).values()
        user_goals = next((g for g in goals_data.values() if g.get("user_id") == user_id), {}).values()
        goals = user_goals.get("goals", [])
        payload = {"user_id": user_id, "goals": goals}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listUserGoals",
                "description": "List all goals for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class GetGoal(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, goal_id: str) -> str:
        goals_data = data.get("goals", {}).values()
        user_goals = next((g for g in goals_data.values() if g.get("user_id") == user_id), {}).values()
        goals = user_goals.get("goals", [])
        goal = next((g for g in goals if g.get("goal_id") == goal_id), None)
        return (
            json.dumps(goal, indent=2)
            if goal
            else json.dumps({"error": "Goal not found"}, indent=2)
        )
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getGoal",
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


class AddGoal(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, goal: dict[str, Any]) -> str:
        """Add a new goal to a user's profile."""
        for entry in data.get("goals", {}).values():
            if entry["user_id"] == user_id:
                entry["goals"].append(goal)
                break
        else:  # no current goal list available for this user
            data.setdefault("goals", []).append({"user_id": user_id, "goals": [goal]})
        payload = {"success": f"goal {goal['goal_id']} added for {user_id}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addGoal",
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


class UpdateGoal(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, goal_id: str, updates: dict) -> str:
        goals_data = data.get("goals", {}).values()
        user_goals = next((g for g in goals_data.values() if g.get("user_id") == user_id), None)
        if user_goals:
            goals = user_goals.get("goals", [])
            goal = next((g for g in goals if g.get("goal_id") == goal_id), None)
            if goal:
                if "notes_append" in updates:
                    goal["notes"] = (
                        goal.get("notes", "") + " " + updates.pop("notes_append")
                    )
                goal.update(updates)
                payload = {"success": f"Goal {goal_id} updated for user {user_id}"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": "Goal not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateGoal",
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


class GetTeam(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str) -> str:
        teams = data.get("teams", {}).values()
        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        return (
            json.dumps(team, indent=2)
            if team
            else json.dumps({"error": "Team not found"}, indent=2)
        )
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getTeam",
                "description": "Get team details by team ID",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class AddTeamMember(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str, user_id: str) -> str:
        teams = data.get("teams", {}).values()
        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        if team:
            team_members = team.setdefault("team_members", [])
            if user_id not in team_members:
                team_members.append(user_id)
                payload = {"success": f"User {user_id} added to team {team_id}"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            else:
                payload = {"success": f"User {user_id} already in team {team_id}"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": "Team not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "addTeamMember",
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


class GetSkillGapAnalysis(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], analysis_id: str = "", user_id: str = "") -> str:
        analyses = data.get("skill_gap_analysis", {}).values()
        if analysis_id:
            analysis = next(
                (a for a in analyses.values() if a.get("analysis_id") == analysis_id), None
            )
        elif user_id:
            analysis = next((a for a in analyses.values() if a.get("user_id") == user_id), None)
        else:
            payload = {"error": "Must provide either analysis_id or user_id"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        return (
            json.dumps(analysis, indent=2)
            if analysis
            else json.dumps({"error": "Analysis not found"}, indent=2)
        )
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getSkillGapAnalysis",
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


class ListUserMentorships(Tool):
    @staticmethod
    def invoke(data, user_id: str, user_mentorship_relationships: list = None) -> str:
        if user_mentorship_relationships is None:
            user_mentorship_relationships = data.get("user_mentorship_relationships", {}).values()
        rels = [
            rel
            for rel in user_mentorship_relationships.values() if rel.get("mentee_id") == user_id
        ]
        payload = {"mentorships": rels}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listUserMentorships",
                "description": "List all mentorship relationships for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class AddMentorshipRelationship(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        mentor_id: str,
        mentee_id: str,
        start_date: str,
        status: str,
        focus_areas: list[str],
    ) -> str:
        relationships = data.setdefault("user_mentorship_relationships", [])

        #--- Logic for automatic generation of relationship_id ---
        if not relationships:
            new_id_num = 1
        else:
            #Identify the highest current ID number to prevent conflicts
            max_id = 0
            for rel in relationships:
                try:
                    num = int(rel["relationship_id"][2:])  #Expects format MR###
                    if num > max_id:
                        max_id = num
                except (ValueError, IndexError):
                    continue  #Ignore incorrectly formatted IDs
            new_id_num = max_id + 1

        new_relationship_id = f"MR{new_id_num:03d}"  #Formats like MR001, MR015, and so on.

        new_relationship = {
            "relationship_id": new_relationship_id,
            "mentor_id": mentor_id,
            "mentee_id": mentee_id,
            "start_date": start_date,
            "status": status,
            "focus_areas": focus_areas,
        }

        relationships.append(new_relationship)
        payload = {
                "success": f"Mentorship relationship {new_relationship_id} created",
                "relationship_id": new_relationship_id,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out


    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "addMentorshipRelationship",
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


class UpdateMentorshipRelationship(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], relationship_id: str, updates: dict[str, Any]
    ) -> str:
        rel = next(
            (
                r
                for r in data.get("user_mentorship_relationships", {}).values()
                if r["relationship_id"] == relationship_id
            ),
            None,
        )
        if not rel:
            payload = {"error": "relationship not found"}
            out = json.dumps(payload)
            return out

        #--- EASED LOGIC ---
        #The tool now solely executes a direct update.
        rel.update(updates)
        payload = {"success": f"relationship {relationship_id} updated"}
        out = json.dumps(payload)
        return out


    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateMentorshipRelationship",
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


class ScheduleMentorshipSession(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], relationship_id: str, session_date: str) -> str:
        sessions = data.setdefault("scheduled_mentorship_sessions", [])
        sessions.append(
            {
                "relationship_id": relationship_id,
                "session_date": session_date,
                "status": "Scheduled",
            }
        )
        payload = {"scheduled_for": session_date}
        out = json.dumps(payload)
        return out
        
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "scheduleMentorshipSession",
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


class ComputeMentorLoad(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], mentor_id: str) -> str:
        """Calculate the number of active mentees for a mentor."""
        count = sum(
            1
            for rel in data.get("user_mentorship_relationships", {}).values()
            if rel["mentor_id"] == mentor_id and rel["status"] == "Active"
        )
        payload = {"current_mentees": count}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "computeMentorLoad",
                "description": "Return the number of active mentees a mentor currently has.",
                "parameters": {
                    "type": "object",
                    "properties": {"mentor_id": {"type": "string"}},
                    "required": ["mentor_id"],
                },
            },
        }


class GetHrWorkflow(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], workflow_id: str) -> str:
        workflow = next(
            (
                w
                for w in data.get("hr_workflows", {}).values()
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
        pass
        return {
            "type": "function",
            "function": {
                "name": "getHrWorkflow",
                "description": "Get HR workflow details by workflow ID",
                "parameters": {
                    "type": "object",
                    "properties": {"workflow_id": {"type": "string"}},
                    "required": ["workflow_id"],
                },
            },
        }


class UpdateHrWorkflow(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], workflow_id: str, updates: dict[str, Any]) -> str:
        wf = next(
            (
                w
                for w in data.get("hr_workflows", {}).values()
                if w["workflow_id"] == workflow_id
            ),
            None,
        )
        if not wf:
            payload = {"error": "workflow not found"}
            out = json.dumps(payload)
            return out

        if "notes_append" in updates:
            wf["notes"] = wf.get("notes", "") + " " + updates.pop("notes_append")

        wf.update(updates)
        payload = {"success": f"workflow {workflow_id} updated"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateHrWorkflow",
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


class AddUserCertification(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, cert: dict) -> str:
        cert["user_id"] = user_id
        data.setdefault("user_certification", []).append(cert)
        payload = {"success": f"Certification {cert['cert_name']} added for user {user_id}"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "addUserCertification",
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


class NotifyHr(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message: str) -> str:
        data.setdefault("hr_notifications", []).append({"message": message})
        payload = {"notified": "HR", "message": message}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "notifyHr",
                "description": "Send an informational notification to the HR team.",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }


class NotifyUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, message: str) -> str:
        data.setdefault("user_notifications", []).append(
            {"user_id": user_id, "message": message}
        )
        payload = {"notified_user": user_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "notifyUser",
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


#Complete tools registry
TOOLS = [
    GetTodayDate(),
    GetUserIdFromName(),
    GetCourseIdByName(),
    GetGoalIdByDescription(),
    GetTeamIdByName(),
    FindHrWorkflowForUser(),
    SearchUsers(),
    GetCourse(),
    EnrollInCourse(),
    ListUserCourses(),
    GetUserCourseProgress(),
    UpdateUserCourseProgress(),
    ComputeAverageProgress(),
    ListUserGoals(),
    GetGoal(),
    AddGoal(),
    UpdateGoal(),
    GetTeam(),
    AddTeamMember(),
    GetSkillGapAnalysis(),
    ListUserMentorships(),
    AddMentorshipRelationship(),
    UpdateMentorshipRelationship(),
    ScheduleMentorshipSession(),
    ComputeMentorLoad(),
    GetHrWorkflow(),
    UpdateHrWorkflow(),
    AddUserCertification(),
    NotifyHr(),
    NotifyUser(),
]
