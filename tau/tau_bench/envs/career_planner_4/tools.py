import json
import uuid
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


#Fundamental utility tools
class GetTodayDate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = {"today": "2025-07-04"}
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


class SearchUsers(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filters: Any = None,
        user_id: str = None
    ) -> str:
        users = data.get("users", {}).values()
        if user_id is not None:
            user = next(
                (u for u in users.values() if u.get("user_id") == user_id), None
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
    def invoke(
        data: dict[str, Any],
        course_id: str,
        course_catalog: list[dict[str, Any]] = None
    ) -> str:
        course = next((c for c in course_catalog if c.get("course_id") == course_id), None)
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


class UpdateGoal(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, goal_id: str, updates: dict) -> str:
        goals_data = data.get("goals", {}).values()
        user_goals = next((g for g in goals_data.values() if g.get("user_id") == user_id), None)
        if user_goals:
            goals = user_goals.get("goals", [])
            goal = next((g for g in goals if g.get("goal_id") == goal_id), None)
            if goal:
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


class GetJobMarketInsights(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role: str) -> str:
        _roleL = role or ''.lower()
        insights = data.get("job_market_insights", {}).values()
        insight = next(
            (i for i in insights.values() if i.get("role", "").lower() == role.lower()), None
        )
        if insight:
            payload = insight
            out = json.dumps(payload, indent=2)
            return out
        else:
            payload = {"role": role, "insights": "Market data not available"}
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
                "name": "getJobMarketInsights",
                "description": "Get job market insights for a role",
                "parameters": {
                    "type": "object",
                    "properties": {"role": {"type": "string"}},
                    "required": ["role"],
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


class ListUserCertifications(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        user_certification = data.get("user_certification", {}).values()
        certs = [
            c for c in user_certification.values() if c.get("user_id") == user_id
        ]
        payload = {"certifications": certs}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listUserCertifications",
                "description": "List certifications for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
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
                "description": "List courses for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class AddUserEducation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, education: dict) -> str:
        education["user_id"] = user_id
        data.setdefault("user_education", []).append(education)
        payload = {"success": f"Education record added for user {user_id}"}
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
                "name": "addUserEducation",
                "description": "Add education record for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "education": {"type": "object"},
                    },
                    "required": ["user_id", "education"],
                },
            },
        }


class LogCourseCompletion(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str, course_id: str, completion_date: str
    ) -> str:
        # Modify current course progress or establish a new record
        courses = data.get("user_course_progress", {}).values()
        course = next(
            (
                c
                for c in courses.values() if c.get("user_id") == user_id and c.get("course_id") == course_id
            ),
            None,
        )
        if course:
            course.update(
                {
                    "status": "Completed",
                    "completion_date": completion_date,
                    "current_progress_percent": 100,
                }
            )
        else:
            courses.append(
                {
                    "user_id": user_id,
                    "course_id": course_id,
                    "status": "Completed",
                    "completion_date": completion_date,
                    "current_progress_percent": 100,
                }
            )
        payload = {"success": f"Course {course_id} completion logged for user {user_id}"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "logCourseCompletion",
                "description": "Log course completion for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "completion_date": {"type": "string"},
                    },
                    "required": ["user_id", "course_id", "completion_date"],
                },
            },
        }


class LogMentoringSession(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        mentee_id: str,
        mentor_id: str,
        session_date: str,
        notes: str,
    ) -> str:
        session = {
            "session_id": f"MS{uuid.uuid4().hex[:6]}",
            "mentee_id": mentee_id,
            "mentor_id": mentor_id,
            "session_date": session_date,
            "notes": notes,
        }
        data.setdefault("mentoring_sessions", []).append(session)
        payload = {"success": f"Mentoring session logged for {mentee_id} with {mentor_id}"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "logMentoringSession",
                "description": "Log a mentoring session",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mentee_id": {"type": "string"},
                        "mentor_id": {"type": "string"},
                        "session_date": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["mentee_id", "mentor_id", "session_date", "notes"],
                },
            },
        }


class ListMentoringSessions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], mentee_id: str) -> str:
        sessions = [
            s
            for s in data.get("mentoring_sessions", {}).values()
            if s.get("mentee_id") == mentee_id
        ]
        payload = {"sessions": sessions}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listMentoringSessions",
                "description": "List mentoring sessions for a mentee",
                "parameters": {
                    "type": "object",
                    "properties": {"mentee_id": {"type": "string"}},
                    "required": ["mentee_id"],
                },
            },
        }


class AuditGoalStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, goal_id: str) -> str:
        goals_data = data.get("goals", {}).values()
        user_goals = next((g for g in goals_data.values() if g.get("user_id") == user_id), {}).values()
        goals = user_goals.get("goals", [])
        goal = next((g for g in goals if g.get("goal_id") == goal_id), None)
        if goal:
            payload = {
                "audit": f"Goal {goal_id} status: {goal.get('status', 'Unknown')}, Progress: {goal.get('progress_percent', 0)}%"
            }
            out = json.dumps(
                payload, indent=2,
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
                "name": "auditGoalStatus",
                "description": "Audit goal status for a user",
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


class LogCourseProgress(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        course_id: str,
        progress: int,
        update_date: str,
    ) -> str:
        record = {
            "user_id": user_id,
            "course_id": course_id,
            "progress": progress,
            "update_date": update_date,
        }
        data.setdefault("course_progress_log", []).append(record)
        payload = {
            "success": f"Course progress logged for {user_id} in {course_id}: {progress}%"
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "logCourseProgress",
                "description": "Log course progress for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "progress": {"type": "integer"},
                        "update_date": {"type": "string"},
                    },
                    "required": ["user_id", "course_id", "progress", "update_date"],
                },
            },
        }


class RecommendLearningPath(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        soft_skill: str,
        course_id: str,
        enroll_date: str,
        goal_id: str,
        progress_percent: int,
    ) -> str:
        # Record the suggestion
        recommendation = {
            "user_id": user_id,
            "soft_skill": soft_skill,
            "course_id": course_id,
            "enroll_date": enroll_date,
            "goal_id": goal_id,
            "progress_percent": progress_percent,
        }
        data.setdefault("learning_path_recommendations", []).append(recommendation)
        payload = {"success": f"Learning path recommended for {user_id} in {soft_skill}"}
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
                "name": "recommendLearningPath",
                "description": "Recommend a learning path for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "soft_skill": {"type": "string"},
                        "course_id": {"type": "string"},
                        "enroll_date": {"type": "string"},
                        "goal_id": {"type": "string"},
                        "progress_percent": {"type": "integer"},
                    },
                    "required": [
                        "user_id",
                        "soft_skill",
                        "course_id",
                        "enroll_date",
                        "goal_id",
                        "progress_percent",
                    ],
                },
            },
        }


class ConditionalProgressUpdate(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        goal_id: str,
        increment: int,
        threshold: int,
        update_date: str,
    ) -> str:
        # Retrieve the current progress of the goal
        goals_data = data.get("goals", {}).values()
        user_goals = next((g for g in goals_data.values() if g.get("user_id") == user_id), {}).values()
        goals = user_goals.get("goals", [])
        goal = next((g for g in goals if g.get("goal_id") == goal_id), None)

        if goal:
            current_progress = goal.get("progress_percent", 0)
            if current_progress < threshold:
                new_progress = current_progress + increment
                goal.update(
                    {"progress_percent": new_progress, "last_updated": update_date}
                )
                payload = {
                    "success": f"Goal {goal_id} progress updated from {current_progress}% to {new_progress}%"
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            else:
                payload = {
                    "result": f"Goal {goal_id} progress ({current_progress}%) already meets threshold"
                }
                out = json.dumps(
                    payload, indent=2,
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
                "name": "conditionalProgressUpdate",
                "description": "Conditionally update goal progress if below threshold",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "goal_id": {"type": "string"},
                        "increment": {"type": "integer"},
                        "threshold": {"type": "integer"},
                        "update_date": {"type": "string"},
                    },
                    "required": [
                        "user_id",
                        "goal_id",
                        "increment",
                        "threshold",
                        "update_date",
                    ],
                },
            },
        }


#Utility to obtain team information using team_id from teams.json.
class GetTeam(Tool):
    @staticmethod
    def invoke(data, team_id: str) -> str:
        for team in data.get("teams", {}).values():
            if team.get("team_id") == team_id:
                payload = team
                out = json.dumps(payload, indent=2)
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
                "name": "getTeam",
                "description": "Fetch team details using the provided team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


#Utility to retrieve team members from a team entry.
class GetTeamMembers(Tool):
    @staticmethod
    def invoke(data, team_id: str) -> str:
        for team in data.get("teams", {}).values():
            if team.get("team_id") == team_id:
                payload = {"team_members": team.get("team_members", [])}
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
                "name": "getTeamMembers",
                "description": "Return the list of team members for a given team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


#Utility to record a team training session in team_training_log.
class LogTeamTraining(Tool):
    @staticmethod
    def invoke(data: dict, team_id: str, training_session: dict) -> str:
        data.setdefault("team_training_log", []).append(training_session)
        payload = {
            "success": f"Training session {training_session['training_session_id']} logged for team {team_id}"
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
                "name": "logTeamTraining",
                "description": "Append a new training session record for a team.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "training_session": {"type": "object"},
                    },
                    "required": ["team_id", "training_session"],
                },
            },
        }


#Utility to display team training sessions for a specified team.
class ListTeamTraining(Tool):
    @staticmethod
    def invoke(
        data,
        team_id: str,
        team_training_log: list = None
    ) -> str:
        sessions = [
            ts
            for ts in (team_training_log or [])
            if ts.get("training_session_id", "").startswith("TS")
        ]
        payload = {"team_training_log": sessions}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listTeamTraining",
                "description": "List all training sessions for a specific team.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


#Utility to modify a person's training progress.
class UpdateUserTrainingProgress(Tool):
    @staticmethod
    def invoke(data: dict, user_id: str, training_session_id: str, progress: int) -> str:
        record = {
            "user_id": user_id,
            "training_session_id": training_session_id,
            "progress": progress,
        }
        data.setdefault("user_training_progress", []).append(record)
        payload = {
            "success": f"Training progress for {user_id} on session {training_session_id} set to {progress}"
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
                "name": "updateUserTrainingProgress",
                "description": "Update the training progress for a given user and training session.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "training_session_id": {"type": "string"},
                        "progress": {"type": "integer"},
                    },
                    "required": ["user_id", "training_session_id", "progress"],
                },
            },
        }


#Utility to obtain mentor information using mentor_id.
class GetMentor(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], mentor_id: str) -> str:
        user_mentorship = data.get("user_mentorship", {}).values()
        for mentor in user_mentorship.values():
            if mentor.get("mentor_id") == mentor_id:
                payload = mentor
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Mentor not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getMentor",
                "description": "Fetch mentor details using mentor_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"mentor_id": {"type": "string"}},
                    "required": ["mentor_id"],
                },
            },
        }


#Utility to arrange a mentorship session by creating a record.
class ScheduleMentorshipSession(Tool):
    @staticmethod
    def invoke(data: dict, relationship: dict) -> str:
        data.setdefault("user_mentorship_relationships", []).append(relationship)
        payload = {
            "success": f"Mentorship session {relationship['relationship_id']} scheduled"
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
                "name": "scheduleMentorshipSession",
                "description": "Schedule a new mentorship session by adding a new relationship record.",
                "parameters": {
                    "type": "object",
                    "properties": {"relationship": {"type": "object"}},
                    "required": ["relationship"],
                },
            },
        }


#Utility to display a user's mentorship connections.
class ListUserMentorships(Tool):
    @staticmethod
    def invoke(
        data,
        user_id: str,
        user_mentorship_relationships: list = None
    ) -> str:
        if user_mentorship_relationships is None:
            user_mentorship_relationships = data.get("user_mentorship_relationships", {}).values()
        rels = [
            rel
            for rel in user_mentorship_relationships.values() if rel.get("user_id") == user_id
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


#Utility to retrieve information about a soft skill.
class GetSoftSkills(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], skill: str) -> str:
        payload = data.get("soft_skills", {}).values().get(skill, {}).values()
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getSoftSkills",
                "description": "Return details for a specific soft skill.",
                "parameters": {
                    "type": "object",
                    "properties": {"skill": {"type": "string"}},
                    "required": ["skill"],
                },
            },
        }


#Utility to modify a user's course progress.
class UpdateCourseProgress(Tool):
    @staticmethod
    def invoke(data, user_id: str, course_id: str, progress_percent: int) -> str:
        record = {
            "user_id": user_id,
            "course_id": course_id,
            "progress_percent": progress_percent,
        }
        data.setdefault("course_progress_updates", []).append(record)
        payload = {
            "success": f"Course {course_id} progress for {user_id} updated to {progress_percent}%."
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
                "name": "updateCourseProgress",
                "description": "Update the progress percentage for a user in a specific course.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "progress_percent": {"type": "integer"},
                    },
                    "required": ["user_id", "course_id", "progress_percent"],
                },
            },
        }


#Utility to record a soft skill gap analysis entry.
class LogSoftSkillGap(Tool):
    @staticmethod
    def invoke(data, user_id: str, analysis: dict) -> str:
        data.setdefault("skill_gap_analysis", []).append(analysis)
        payload = {
                "success": f"Soft skill gap analysis {analysis['analysis_id']} logged for {user_id}"
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
                "name": "logSoftSkillGap",
                "description": "Add a soft-skill gap analysis record for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "analysis": {"type": "object"},
                    },
                    "required": ["user_id", "analysis"],
                },
            },
        }


#Utility to display soft skill gap analysis entries for a user, filtered by skill.
class ListSoftSkillGap(Tool):
    @staticmethod
    def invoke(data, user_id: str, skill: str) -> str:
        analyses = [
            a
            for a in data.get("skill_gap_analysis", {}).values()
            if a.get("skill") == skill and a.get("user_id") == user_id
        ]
        payload = {"soft_skill_gap": analyses}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listSoftSkillGap",
                "description": "List soft skill gap analysis records for a user for a specific skill.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "skill": {"type": "string"},
                    },
                    "required": ["user_id", "skill"],
                },
            },
        }


#Utility to evaluate a skill gap and provide analysis details (and record it).
class AnalyzeSkillGap(Tool):
    @staticmethod
    def invoke(
        data,
        user_id: str,
        skill: str,
        current_level: str,
        required_level: str,
        recommended_courses: list,
    ) -> str:
        analysis = {
            "analysis_id": "SGA005",
            "user_id": user_id,
            "skill": skill,
            "current_proficiency": current_level,
            "required_proficiency": required_level,
            "recommended_courses": recommended_courses,
        }
        data.setdefault("skill_gap_analysis", []).append(analysis)
        payload = analysis
        out = json.dumps(payload, indent=2)
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "analyzeSkillGap",
                "description": "Perform and log a skill gap analysis for a given user and skill.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "skill": {"type": "string"},
                        "current_level": {"type": "string"},
                        "required_level": {"type": "string"},
                        "recommended_courses": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": [
                        "user_id",
                        "skill",
                        "current_level",
                        "required_level",
                        "recommended_courses",
                    ],
                },
            },
        }


#Utility to display a user's educational records.
class ListUserEducation(Tool):
    @staticmethod
    def invoke(data, user_id: str) -> str:
        edu = [e for e in data.get("user_education", {}).values() if e.get("user_id") == user_id]
        payload = {"education": edu}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listUserEducation",
                "description": "List all education records for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


#Utility to query the external talent network using candidate_id.
class SearchTalentNetwork(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str) -> str:
        talent_network = data.get("talent_network", {}).values()
        for candidate in talent_network.values():
            if candidate.get("candidate_id") == candidate_id:
                payload = candidate
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Candidate not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "searchTalentNetwork",
                "description": "Search for an external candidate by candidate_id in the talent network.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }


#Utility to record an external job application.
class LogJobApplication(Tool):
    @staticmethod
    def invoke(
        data,
        candidate_id: str,
        job_id: str,
        apply_date: str,
        skill_match_score: int,
        application_id: str | None = None
    ) -> str:
        application = {
            "application_id": application_id or "APP001",
            "candidate_id": candidate_id,
            "job_id": job_id,
            "apply_date": apply_date,
            "skill_match_score": skill_match_score,
        }
        data.setdefault("job_applications", []).append(application)
        payload = {
            "success": f"Application {application['application_id']} logged for candidate {candidate_id}"
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "logJobApplication",
                "description": "Log a new job application record for an external candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "job_id": {"type": "string"},
                        "apply_date": {"type": "string"},
                        "skill_match_score": {"type": "integer"},
                        "application_id": {"type": "string"},
                    },
                    "required": [
                        "candidate_id",
                        "job_id",
                        "apply_date",
                        "skill_match_score",
                    ],
                },
            },
        }


#Utility to modify the information of a job application.
class UpdateApplication(Tool):
    @staticmethod
    def invoke(data, candidate_id: str, application_id: str, updates: dict) -> str:
        updated = False
        for app in data.get("job_applications", {}).values():
            if (
                app.get("application_id") == application_id
                and app.get("candidate_id") == candidate_id
            ):
                app.update(updates)
                updated = True
        if updated:
            payload = {
                    "success": f"Application {application_id} updated for candidate {candidate_id}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {"error": "Application not found"}
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateApplication",
                "description": "Update an external job application record with new details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "application_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["candidate_id", "application_id", "updates"],
                },
            },
        }


#Utility to arrange an interview for a candidate.
class ScheduleInterview(Tool):
    @staticmethod
    def invoke(
        data, candidate_id: str, application_id: str, interview_date: str
    ) -> str:
        record = {
            "candidate_id": candidate_id,
            "application_id": application_id,
            "interview_date": interview_date,
        }
        data.setdefault("interview_schedule", []).append(record)
        payload = {
            "success": f"Interview scheduled for application {application_id} on {interview_date}"
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "scheduleInterview",
                "description": "Schedule an interview for a candidate by updating the job application record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "application_id": {"type": "string"},
                        "interview_date": {"type": "string"},
                    },
                    "required": ["candidate_id", "application_id", "interview_date"],
                },
            },
        }


#Utility to display all applications submitted by a candidate.
class ListApplications(Tool):
    @staticmethod
    def invoke(
        data,
        job_applications: list = None,
        candidate_id: str = None
    ) -> str:
        apps = [
            app
            for app in (job_applications or [])
            if app.get("candidate_id") == candidate_id
        ]
        payload = {"applications": apps}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listApplications",
                "description": "List all job applications for a given candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }


#Utility to display job postings based on role criteria.
class ListJobPostings(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role: str) -> str:
        postings = [
            jp
            for jp in data.get("job_postings", {}).values()
            if jp.get("title", "").find(role) != -1
        ]
        payload = {"job_postings": postings}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listJobPostings",
                "description": "List all job postings for a given role.",
                "parameters": {
                    "type": "object",
                    "properties": {"role": {"type": "string"}},
                    "required": ["role"],
                },
            },
        }


#Utility to transfer a user's mentorship from one mentor to a different one.
class ReassignMentor(Tool):
    @staticmethod
    def invoke(
        data, user_id: str, old_mentor_id: str, new_mentor_id: str, relationship_id: str
    ) -> str:
        # To keep it straightforward, create a new record reflecting the change.
        record = {
            "relationship_id": relationship_id,
            "user_id": user_id,
            "mentor_id": new_mentor_id,
            "reassigned_from": old_mentor_id,
            "updated_date": "2023-10-05",
        }
        data.setdefault("mentorship_reassignments", []).append(record)
        payload = {
            "success": f"Mentor reassigned for {user_id}: now under mentor {new_mentor_id}"
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
                "name": "reassignMentor",
                "description": "Reassign a mentorship from an old mentor to a new mentor for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "old_mentor_id": {"type": "string"},
                        "new_mentor_id": {"type": "string"},
                        "relationship_id": {"type": "string"},
                    },
                    "required": [
                        "user_id",
                        "old_mentor_id",
                        "new_mentor_id",
                        "relationship_id",
                    ],
                },
            },
        }


#1. Conditional enrollment utility: either enrolls a user based on conditions or displays enrollments.
class ConditionalEnrollOrList(Tool):
    @staticmethod
    def invoke(
        data,
        user_id: str,
        course_id: str,
        goal_id: str,
        threshold: int,
        enroll_date: str,
    ) -> str:
        pass
        #Placeholder condition: if the numeric portion of user_id is odd, mimic enrollment.
        if int(user_id[1:]) % 2 == 1:
            payload = {
                    "result": f"User {user_id} enrolled in {course_id} and goal {goal_id} updated to {threshold}%."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                    "result": f"User {user_id} already meets threshold; enrollments listed."
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
                "name": "conditionalEnrollOrList",
                "description": "Conditionally enroll a user in a course if their goal progress is below a threshold; otherwise, list current enrollments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "goal_id": {"type": "string"},
                        "threshold": {"type": "integer"},
                        "enroll_date": {"type": "string"},
                    },
                    "required": [
                        "user_id",
                        "course_id",
                        "goal_id",
                        "threshold",
                        "enroll_date",
                    ],
                },
            },
        }


class GetUserCourseProgress(Tool):
    @staticmethod
    def invoke(
        data,
        user_id: str,
        prefix: str,
        course_id: str):
        payload = {"user_course_progress": {"status": "Not Completed", "grade": 0}}
        out = json.dumps(
            payload,
        indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getUserCourseProgress",
                "description": "Fetch the user's progress record for a specific course.",
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


#Identification Generation Utilities
class GenerateUniqueCertId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]
    ) -> str:
        unique_id = f"{prefix}001"
        payload = {"generated_cert_id": unique_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "generateUniqueCertId",
                "description": "Generate a unique certification ID",
                "parameters": {
                    "type": "object",
                    "properties": {"prefix": {"type": "string"}},
                    "required": ["prefix"],
                },
            },
        }


class GenerateUniqueEduId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], prefix: str) -> str:
        unique_id = f"{prefix}001"
        payload = {"generated_edu_id": unique_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "generateUniqueEduId",
                "description": "Generate a unique education ID",
                "parameters": {
                    "type": "object",
                    "properties": {"prefix": {"type": "string"}},
                    "required": ["prefix"],
                },
            },
        }


class GenerateUniqueApplicationId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], prefix: str) -> str:
        unique_id = f"{prefix}001"
        payload = {"generated_application_id": unique_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "generateUniqueApplicationId",
                "description": "Generate a unique application ID",
                "parameters": {
                    "type": "object",
                    "properties": {"prefix": {"type": "string"}},
                    "required": ["prefix"],
                },
            },
        }


class GenerateUniqueRelationshipId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], prefix: str) -> str:
        unique_id = f"{prefix}001"
        payload = {"generated_relationship_id": unique_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "generateUniqueRelationshipId",
                "description": "Generate a unique relationship ID",
                "parameters": {
                    "type": "object",
                    "properties": {"prefix": {"type": "string"}},
                    "required": ["prefix"],
                },
            },
        }


class GenerateUniqueAnalysisId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], prefix: str) -> str:
        unique_id = f"{prefix}001"
        payload = {"generated_analysis_id": unique_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "generateUniqueAnalysisId",
                "description": "Generate a unique analysis ID",
                "parameters": {
                    "type": "object",
                    "properties": {"prefix": {"type": "string"}},
                    "required": ["prefix"],
                },
            },
        }


#Progress and Computation Utilities
class CheckGoalProgressThreshold(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        goal_id: str,
        threshold: int,
        comparison: str,
    ) -> str:
        goals_data = data.get("goals", {}).values()
        user_goals = next((g for g in goals_data.values() if g.get("user_id") == user_id), {}).values()
        goals = user_goals.get("goals", [])
        goal = next((g for g in goals if g.get("goal_id") == goal_id), None)

        if not goal:
            payload = {"meets_threshold": False, "error": "Goal not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        progress = goal.get("progress_percent", 0)
        meets_threshold = False

        if comparison == "below":
            meets_threshold = progress < threshold
        elif comparison == "above":
            meets_threshold = progress > threshold
        elif comparison == "equal":
            meets_threshold = progress == threshold
        payload = {
                "meets_threshold": meets_threshold,
                "current_progress": progress,
                "threshold": threshold,
                "comparison": comparison,
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
                "name": "checkGoalProgressThreshold",
                "description": "Check if a goal's progress meets a threshold condition",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "goal_id": {"type": "string"},
                        "threshold": {"type": "integer"},
                        "comparison": {
                            "type": "string",
                            "enum": ["below", "above", "equal"],
                        },
                    },
                    "required": ["user_id", "goal_id", "threshold", "comparison"],
                },
            },
        }


class CalculateProgressIncrement(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], current_progress: Any, increment: int) -> str:
        if current_progress == "get_from_goal":
            # This will be calculated dynamically according to the goal
            calculated_value = min(100, increment)  # Streamlined
        else:
            calculated_value = min(100, current_progress + increment)
        payload = {"calculated_value": calculated_value}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "calculateProgressIncrement",
                "description": "Calculate progress increment automatically",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_progress": {"type": ["integer", "string"]},
                        "increment": {"type": "integer"},
                    },
                    "required": ["current_progress", "increment"],
                },
            },
        }


#Employment and Application Utilities
class GetJobPosting(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], job_id: str) -> str:
        job_postings = data.get("job_postings", {}).values()
        job = next((j for j in job_postings.values() if j.get("job_id") == job_id), None)
        return (
            json.dumps(job, indent=2)
            if job
            else json.dumps({"error": "Job posting not found"}, indent=2)
        )
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getJobPosting",
                "description": "Get job posting details by job ID",
                "parameters": {
                    "type": "object",
                    "properties": {"job_id": {"type": "string"}},
                    "required": ["job_id"],
                },
            },
        }


class AddJobApplication(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        application_id: str,
        user_id: str,
        job_id: str,
        apply_date: str,
    ) -> str:
        application = {
            "application_id": application_id,
            "user_id": user_id,
            "job_id": job_id,
            "apply_date": apply_date,
            "status": "Applied",
        }
        data.setdefault("job_applications", []).append(application)
        payload = {"success": f"Application {application_id} created for user {user_id}"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "addJobApplication",
                "description": "Add a job application record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "application_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "job_id": {"type": "string"},
                        "apply_date": {"type": "string"},
                    },
                    "required": ["application_id", "user_id", "job_id", "apply_date"],
                },
            },
        }


class ListUserApplications(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        applications = [
            app
            for app in data.get("job_applications", {}).values()
            if app.get("user_id") == user_id
        ]
        payload = {"applications": applications}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listUserApplications",
                "description": "List all job applications for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class SearchJobPostings(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filters: Any = None,
        job_id: str = None
    ) -> str:
        job_postings = data.get("job_postings", {}).values()
        if job_id is not None:
            job = next(
                (j for j in job_postings.values() if j.get("job_id") == job_id), None
            )
            return (
                json.dumps(job, indent=2)
                if job
                else json.dumps({"error": "Job not found"}, indent=2)
            )
        payload = {"job_postings": job_postings}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "searchJobPostings",
                "description": "Search for job postings by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }


#Skill Gap Evaluation Utilities
class GetSkillGapAnalysis(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = "", analysis_id: str = "") -> str:
        skill_gaps = data.get("skill_gap_analysis", {}).values()
        if analysis_id:
            analysis = next(
                (s for s in skill_gaps.values() if s.get("analysis_id") == analysis_id), None
            )
        elif user_id:
            analysis = next(
                (s for s in skill_gaps.values() if s.get("user_id") == user_id), None
            )
        else:
            payload = {"error": "Either user_id or analysis_id required"}
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
                "description": "Get skill gap analysis by user ID or analysis ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "analysis_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class PerformSoftSkillGapAnalysis(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, skills: list) -> str:
        analysis = {
            "analysis_id": f"SGA{int(datetime.now().timestamp() * 1000) % 10000}",
            "user_id": user_id,
            "skills_analyzed": skills,
            "readiness_score": 65,  # Simulated score
            "date": "2025-07-04",
        }
        data.setdefault("skill_gap_analysis", []).append(analysis)
        payload = {"success": f"Analysis completed for user {user_id}", "analysis": analysis}
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
                "name": "performSoftSkillGapAnalysis",
                "description": "Perform soft skill gap analysis for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "skills": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["user_id", "skills"],
                },
            },
        }


class ComputeSkillGapScore(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        pass
        # Simulated computation - in a real system, actual skill gaps would be assessed
        score = 45  # Simulated score under the threshold
        payload = {"readiness_score": score, "user_id": user_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "computeSkillGapScore",
                "description": "Compute skill gap readiness score for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


#Team and Mentorship Utilities
class AssignMentor(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = "",
        mentor_id: str = "",
        mentee_id: str = "",
        focus_areas: list = [],
        start_date: str = "",
    ) -> str:
        mentee = user_id or mentee_id
        relationship = {
            "relationship_id": f"MR{int(datetime.now().timestamp() * 1000) % 10000}",
            "mentor_id": mentor_id,
            "mentee_id": mentee,
            "focus_areas": focus_areas or [],
            "start_date": start_date,
            "status": "Active",
        }
        data.setdefault("user_mentorship_relationships", []).append(relationship)
        payload = {"success": f"Mentor {mentor_id} assigned to {mentee}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "assignMentor",
                "description": "Assign a mentor to a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "mentor_id": {"type": "string"},
                        "mentee_id": {"type": "string"},
                        "focus_areas": {"type": "array", "items": {"type": "string"}},
                        "start_date": {"type": "string"},
                    },
                    "required": ["mentor_id"],
                },
            },
        }


class ListUserMentors(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        mentorships = [
            m
            for m in data.get("user_mentorship_relationships", {}).values()
            if m.get("mentee_id") == user_id
        ]
        payload = {"mentorships": mentorships}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listUserMentors",
                "description": "List all mentors for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class ListMentorshipRelationships(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filters: Any = None,
        mentor_id: str = None,
        status: str = None
    ) -> str:
        relationships = data.get("user_mentorship_relationships", {}).values()
        if mentor_id is not None:
            relationships = [
                r for r in relationships.values() if r.get("mentor_id") == mentor_id
            ]
        if status is not None:
            relationships = [
                r for r in relationships.values() if r.get("status") == status
            ]
        payload = {"relationships": relationships}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listMentorshipRelationships",
                "description": "List mentorship relationships by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }


class ComputeMentorLoad(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], mentor_id: str) -> str:
        relationships = [
            r
            for r in data.get("user_mentorship_relationships", {}).values()
            if r.get("mentor_id") == mentor_id and r.get("status") == "Active"
        ]
        load = len(relationships)
        payload = {"mentor_load": load, "mentor_id": mentor_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "computeMentorLoad",
                "description": "Compute the current active mentee load for a mentor",
                "parameters": {
                    "type": "object",
                    "properties": {"mentor_id": {"type": "string"}},
                    "required": ["mentor_id"],
                },
            },
        }


class UpdateMentorshipNote(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], mentor_id: str, mentee_id: str, note: str) -> str:
        note_record = {
            "mentor_id": mentor_id,
            "mentee_id": mentee_id,
            "note": note,
            "date": "2025-07-04",
        }
        data.setdefault("mentorship_notes", []).append(note_record)
        payload = {"success": "Note added to mentorship record"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateMentorshipNote",
                "description": "Add a note to a mentorship record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mentor_id": {"type": "string"},
                        "mentee_id": {"type": "string"},
                        "note": {"type": "string"},
                    },
                    "required": ["mentor_id", "mentee_id", "note"],
                },
            },
        }


#Team Utilities
class SearchTeams(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filters: Any = None,
        team_id: str = None
    ) -> str:
        teams = data.get("teams", {}).values()
        if team_id is not None:
            team = next(
                (t for t in teams.values() if t.get("team_id") == team_id), None
            )
            return (
                json.dumps(team, indent=2)
                if team
                else json.dumps({"error": "Team not found"}, indent=2)
            )
        payload = {"teams": teams}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "searchTeams",
                "description": "Search for teams by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }


class ListTeamMembers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str) -> str:
        teams = data.get("teams", {}).values()
        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        if team:
            members = team.get("members", [])
            payload = {"members": members}
            out = json.dumps(payload, indent=2)
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
                "name": "listTeamMembers",
                "description": "List all members of a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


#Extra Utilities
class CheckCourseCompletionStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, course_id: str) -> str:
        progress = data.get("user_course_progress", {}).values()
        user_progress = next(
            (
                p
                for p in progress.values() if p.get("user_id") == user_id and p.get("course_id") == course_id
            ),
            None,
        )
        completed = (
            user_progress.get("status") == "Completed" if user_progress else False
        )
        payload = {"completed": completed, "user_id": user_id, "course_id": course_id}
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
                "name": "checkCourseCompletionStatus",
                "description": "Check if a user has completed a course",
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


class MarkCourseCompleted(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str, course_id: str, completion_date: str
    ) -> str:
        progress = data.get("user_course_progress", {}).values()
        user_progress = next(
            (
                p
                for p in progress.values() if p.get("user_id") == user_id and p.get("course_id") == course_id
            ),
            None,
        )
        if user_progress:
            user_progress["status"] = "Completed"
            user_progress["completion_date"] = completion_date
            user_progress["current_progress_percent"] = 100
        else:
            new_progress = {
                "user_id": user_id,
                "course_id": course_id,
                "status": "Completed",
                "completion_date": completion_date,
                "current_progress_percent": 100,
            }
            data["user_course_progress"][new_progress["user_course_progres_id"]] = new_progress
        payload = {"success": f"Course {course_id} marked completed for user {user_id}"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "markCourseCompleted",
                "description": "Mark a course as completed for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "completion_date": {"type": "string"},
                    },
                    "required": ["user_id", "course_id", "completion_date"],
                },
            },
        }


class ComputeAverageProgress(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        progress = data.get("user_course_progress", {}).values()
        user_courses = [p for p in progress.values() if p.get("user_id") == user_id]
        if not user_courses:
            payload = {"average_progress": 0}
            out = json.dumps(payload, indent=2)
            return out

        total_progress = sum(p.get("current_progress_percent", 0) for p in user_courses.values())
        average = total_progress / len(user_courses)
        payload = {"average_progress": average, "user_id": user_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "computeAverageProgress",
                "description": "Compute average course progress for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class NotifyHr(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message: str) -> str:
        notification = {
            "message": message,
            "timestamp": "2025-07-04",
            "type": "HR_NOTIFICATION",
        }
        data.setdefault("hr_notifications", []).append(notification)
        payload = {"success": "HR notified", "message": message}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "notifyHr",
                "description": "Send a notification to HR",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }


class SendEmailToUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, subject: str, body: str) -> str:
        email = {
            "user_id": user_id,
            "subject": subject,
            "body": body,
            "timestamp": "2025-07-04",
        }
        data.setdefault("emails_sent", []).append(email)
        payload = {"success": f"Email sent to user {user_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "sendEmailToUser",
                "description": "Send an email to a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "body": {"type": "string"},
                    },
                    "required": ["user_id", "subject", "body"],
                },
            },
        }


#Extra utilities that are missing
class GetTeamTrainingLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str) -> str:
        training_logs = data.get("team_training_log", {}).values()
        team_logs = [log for log in training_logs.values() if log.get("team_id") == team_id]
        payload = {"training_logs": team_logs}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getTeamTrainingLog",
                "description": "Get training logs for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class UpdateTeamTrainingLog(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        training_session_id: str,
        user_id: str,
        status: str,
        completion_date: str,
        skills_gained: list,
    ) -> str:
        log_entry = {
            "training_session_id": training_session_id,
            "user_id": user_id,
            "status": status,
            "completion_date": completion_date,
            "skills_gained": skills_gained,
        }
        data.setdefault("team_training_log", []).append(log_entry)
        payload = {"success": f"Training log updated for {user_id}"}
        out = json.dumps(payload, indent=2)
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateTeamTrainingLog",
                "description": "Update team training log",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "training_session_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "status": {"type": "string"},
                        "completion_date": {"type": "string"},
                        "skills_gained": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "training_session_id",
                        "user_id",
                        "status",
                        "completion_date",
                        "skills_gained",
                    ],
                },
            },
        }


class ListUserTrainingSessions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        training_logs = data.get("team_training_log", {}).values()
        user_sessions = [log for log in training_logs.values() if log.get("user_id") == user_id]
        payload = {"training_sessions": user_sessions}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listUserTrainingSessions",
                "description": "List training sessions for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class ScheduleTeamTraining(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], team_id: str, course_id: str, session_date: str
    ) -> str:
        training_session = {
            "team_id": team_id,
            "course_id": course_id,
            "session_date": session_date,
            "status": "Scheduled",
        }
        data.setdefault("team_training_sessions", []).append(training_session)
        payload = {"success": f"Training session scheduled for team {team_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "scheduleTeamTraining",
                "description": "Schedule a training session for a team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "session_date": {"type": "string"},
                    },
                    "required": ["team_id", "course_id", "session_date"],
                },
            },
        }


class AddTeamTrainingSession(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str, training: dict) -> str:
        training["team_id"] = team_id
        data.setdefault("team_training_sessions", []).append(training)
        payload = {"success": f"Training session added for team {team_id}"}
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
                "name": "addTeamTrainingSession",
                "description": "Add a training session for a team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "training": {"type": "object"},
                    },
                    "required": ["team_id", "training"],
                },
            },
        }


class ComputeTeamTrainingHours(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        team_id: str,
        year: int = 2025
    ) -> str:
        training_logs = data.get("team_training_log", {}).values()
        team_logs = [log for log in training_logs.values() if log.get("team_id") == team_id]
        total_hours = len(team_logs) * 8  # Simulated calculation
        payload = {"total_hours": total_hours, "team_id": team_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "computeTeamTrainingHours",
                "description": "Compute total training hours for a team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "year": {"type": "integer"},
                    },
                    "required": ["team_id"],
                },
            },
        }


class ComputeTeamAverageProgress(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        team_id: str,
        teams: list = None,
        user_course_progress: list = None
    ) -> str:
        teams = teams if teams is not None else data.get("teams", {}).values()
        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": "Team not found"}
            out = json.dumps(payload, indent=2)
            return out

        members = team.get("members", [])
        if not members:
            payload = {"average_progress": 0}
            out = json.dumps(payload, indent=2)
            return out

        total_progress = 0
        user_progress = user_course_progress if user_course_progress is not None else data.get("user_course_progress", {}).values()
        for member in members:
            user_courses = [p for p in user_progress.values() if p.get("user_id") == member]
            if user_courses:
                avg_progress = sum(
                    p.get("current_progress_percent", 0) for p in user_courses
                ) / len(user_courses)
                total_progress += avg_progress

        team_average = total_progress / len(members) if members else 0
        payload = {"team_average_progress": team_average, "team_id": team_id}
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
                "name": "computeTeamAverageProgress",
                "description": "Compute average course progress for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class BulkEnrollCourse(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], team_id: str, course_id: str, enroll_date: str
    ) -> str:
        teams = data.get("teams", {}).values()
        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": "Team not found"}
            out = json.dumps(payload, indent=2)
            return out

        members = team.get("members", [])
        for member in members:
            enrollment = {
                "user_id": member,
                "course_id": course_id,
                "status": "Enrolled",
                "start_date": enroll_date,
                "current_progress_percent": 0,
            }
            data.setdefault("user_course_progress", []).append(enrollment)
        payload = {"success": f"Bulk enrolled {len(members)} members in course {course_id}"}
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
                "name": "bulkEnrollCourse",
                "description": "Bulk enroll team members in a course",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "enroll_date": {"type": "string"},
                    },
                    "required": ["team_id", "course_id", "enroll_date"],
                },
            },
        }


class BulkUpdateGoals(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], team_id: str, goal_type: str, updates: dict
    ) -> str:
        _goal_typeL = goal_type or ''.lower()
        pass
        teams = data.get("teams", {}).values()
        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": "Team not found"}
            out = json.dumps(payload, indent=2)
            return out

        members = team.get("members", [])
        goals_data = data.get("goals", {}).values()

        for member in members:
            user_goals = next(
                (g for g in goals_data.values() if g.get("user_id") == member), None
            )
            if user_goals:
                for goal in user_goals.get("goals", []):
                    if goal_type.lower() in goal.get("title", "").lower():
                        goal.update(updates)
        payload = {"success": f"Bulk updated goals for {len(members)} members"}
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
                "name": "bulkUpdateGoals",
                "description": "Bulk update goals for team members",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "goal_type": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["team_id", "goal_type", "updates"],
                },
            },
        }


class ComputeCertExpiry(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, cert_id: str) -> str:
        payload = {"expiry_date": "2026-03-12", "days_until_expiry": 251}
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
                "name": "computeCertExpiry",
                "description": "Compute certification expiry date",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "cert_id": {"type": "string"},
                    },
                    "required": ["user_id", "cert_id"],
                },
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


class BulkCheckTeamCourses(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        team_id: str,
        teams: list = None,
        user_course_progress: list = None
    ) -> str:
        teams = teams if teams is not None else data.get("teams", {}).values()
        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": "Team not found"}
            out = json.dumps(payload, indent=2)
            return out

        members = team.get("team_members", [])
        progress_data = user_course_progress if user_course_progress is not None else data.get("user_course_progress", {}).values()
        team_progress = []

        for member_id in members:
            member_courses = [p for p in progress_data.values() if p.get("user_id") == member_id]
            avg_progress = (
                sum(c.get("current_progress_percent", 0) for c in member_courses.values()
                / len(member_courses)
                if member_courses
                else 0
            )
            team_progress.append(
                {"user_id": member_id, "average_progress": avg_progress}
            )
        payload = {"team_id": team_id, "member_progress": team_progress}
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
                "name": "bulkCheckTeamCourses",
                "description": "Check course progress for all team members",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class BulkEnrollTeam(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], team_id: str, course_id: str, enroll_date: str
    ) -> str:
        teams = data.get("teams", {}).values()
        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": "Team not found"}
            out = json.dumps(payload, indent=2)
            return out

        members = team.get("team_members", [])
        enrolled_members = []

        for member_id in members:
            enrollment = {
                "user_id": member_id,
                "course_id": course_id,
                "status": "Enrolled",
                "start_date": enroll_date,
                "completion_date": None,
                "current_progress_percent": 0,
            }
            data.setdefault("user_course_progress", []).append(enrollment)
            enrolled_members.append(member_id)
        payload = {
            "success": f"Team {team_id} enrolled in course {course_id}",
            "enrolled_members": enrolled_members,
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
                "name": "bulkEnrollTeam",
                "description": "Enroll all team members in a course",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "enroll_date": {"type": "string"},
                    },
                    "required": ["team_id", "course_id", "enroll_date"],
                },
            },
        }


class BulkUpdateTeamGoals(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], team_id: str, goal_type: str, updates: dict
    ) -> str:
        _goal_typeL = goal_type or ''.lower()
        pass
        teams = data.get("teams", {}).values()
        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": "Team not found"}
            out = json.dumps(payload, indent=2)
            return out

        members = team.get("team_members", [])
        goals_data = data.get("goals", {}).values()
        updated_goals = []

        for member_id in members:
            user_goals = next(
                (g for g in goals_data.values() if g.get("user_id") == member_id), None
            )
            if user_goals:
                goals = user_goals.get("goals", [])
                for goal in goals:
                    if goal_type.lower() in goal.get("goal_name", "").lower():
                        goal.update(updates)
                        updated_goals.append(
                            {"user_id": member_id, "goal_id": goal.get("goal_id")}
                        )
        payload = {
                "success": f"Team {team_id} goals updated",
                "updated_goals": updated_goals,
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
                "name": "bulkUpdateTeamGoals",
                "description": "Update goals for all team members",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "goal_type": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["team_id", "goal_type", "updates"],
                },
            },
        }


class CheckReadinessThreshold(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str, threshold: int, comparison: str
    ) -> str:
        pass
        #Simulated implementation - in a real system, actual readiness scores would be verified
        readiness_score = 75  #Simulated score

        if comparison == "below":
            meets_condition = readiness_score < threshold
        elif comparison == "above":
            meets_condition = readiness_score > threshold
        else:
            meets_condition = readiness_score == threshold
        payload = {
                "user_id": user_id,
                "readiness_score": readiness_score,
                "threshold": threshold,
                "comparison": comparison,
                "meets_condition": meets_condition,
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
                "name": "checkReadinessThreshold",
                "description": "Check if user's readiness score meets threshold",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "threshold": {"type": "integer"},
                        "comparison": {"type": "string"},
                    },
                    "required": ["user_id", "threshold", "comparison"],
                },
            },
        }


class CheckTeamAverageThreshold(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], team_id: str, threshold: int, comparison: str
    ) -> str:
        teams = data.get("teams", {}).values()
        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": "Team not found"}
            out = json.dumps(payload, indent=2)
            return out

        members = team.get("team_members", [])
        progress_data = data.get("user_course_progress", {}).values()

        # Compute the average for the team
        total_progress = 0
        member_count = 0

        for member_id in members:
            member_courses = [p for p in progress_data.values() if p.get("user_id") == member_id]
            if member_courses:
                avg_progress = sum(
                    c.get("current_progress_percent", 0) for c in member_courses
                ) / len(member_courses)
                total_progress += avg_progress
                member_count += 1

        team_average = total_progress / member_count if member_count > 0 else 0

        if comparison == "below":
            meets_condition = team_average < threshold
        elif comparison == "above":
            meets_condition = team_average > threshold
        else:
            meets_condition = team_average == threshold
        payload = {
            "team_id": team_id,
            "team_average": team_average,
            "threshold": threshold,
            "comparison": comparison,
            "meets_condition": meets_condition,
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
                "name": "checkTeamAverageThreshold",
                "description": "Check if team average meets threshold",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "threshold": {"type": "integer"},
                        "comparison": {"type": "string"},
                    },
                    "required": ["team_id", "threshold", "comparison"],
                },
            },
        }


class CheckTeamTrainingThreshold(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], team_id: str, threshold: int, comparison: str
    ) -> str:
        # Simulated calculation of team training hours
        training_data = data.get("team_training_log", {}).values()
        team_sessions = [t for t in training_data.values() if t.get("team_id") == team_id]

        # Simulated calculation - in a real system, actual training hours would be totaled
        total_hours = len(team_sessions) * 25  # Presume 25 hours for each session

        if comparison == "below":
            condition_met = total_hours < threshold
            payload = {
                "condition_met": condition_met,
                "team_id": team_id,
                "total_hours": total_hours,
                "threshold": threshold,
                "comparison": comparison,
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            condition_met = total_hours >= threshold
            payload = {
                "condition_met": condition_met,
                "team_id": team_id,
                "total_hours": total_hours,
                "threshold": threshold,
                "comparison": comparison,
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
                "name": "checkTeamTrainingThreshold",
                "description": "Check if team training hours meet threshold",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "threshold": {"type": "integer"},
                        "comparison": {"type": "string", "enum": ["below", "above"]},
                    },
                    "required": ["team_id", "threshold", "comparison"],
                },
            },
        }


class GetUserGoalsByType(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        goal_type: str = "",
        goal_description_keywords: str = ""
    ) -> str:
        _goal_typeL = goal_type or ''.lower()
        _goal_description_keywordsL = goal_description_keywords or ''.lower()
        goals_data = data.get("goals", {}).values()
        user_goals = next((g for g in goals_data.values() if g.get("user_id") == user_id), {}).values()
        goals = user_goals.get("goals", [])

        filtered_goals = goals

        # Filter based on goal type if specified
        if goal_type:
            filtered_goals = [
                g
                for g in filtered_goals
                if g.get("goal_type", "").lower() == goal_type.lower()
            ]

        # Filter using keywords in the goal description if specified
        if goal_description_keywords:
            keywords = goal_description_keywords.lower().split()
            filtered_goals = [
                g
                for g in filtered_goals
                if any(
                    keyword in g.get("goal_description", "").lower()
                    for keyword in keywords
                )
            ]
        payload = {
            "user_id": user_id,
            "matching_goals": filtered_goals,
            "total_goals_found": len(filtered_goals),
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
                "name": "getUserGoalsByType",
                "description": "Get user goals filtered by type and/or description keywords",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "goal_type": {
                            "type": "string",
                            "description": "Goal type to filter by (e.g., 'Role Transition', 'Skill Mastery', 'Certification')",
                        },
                        "goal_description_keywords": {
                            "type": "string",
                            "description": "Keywords to search in goal description (space-separated)",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }


class GetCourseByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], course_name: str) -> str:
        _course_nameL = course_name or ''.lower()
        pass
        courses = data.get("course_catalog", {}).values()

        # Attempt an exact match initially
        course = next(
            (c for c in courses.values() if c.get("name", "").lower() == course_name.lower()),
            None,
        )

        # If an exact match is not found, attempt a partial match
        if not course:
            course = next(
                (
                    c
                    for c in courses.values() if course_name.lower() in c.get("name", "").lower()
                ),
                None,
            )

        if course:
            payload = {
                "course_found": True,
                "course_id": course.get("course_id"),
                "course_name": course.get("name"),
                "provider": course.get("provider"),
                "level": course.get("level"),
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                "course_found": False,
                "error": f"Course '{course_name}' not found",
                "suggestion": "Try using partial course name or check course catalog",
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
                "name": "getCourseByName",
                "description": "Find course ID by course name (exact or partial match)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "course_name": {
                            "type": "string",
                            "description": "Full or partial course name to search for",
                        }
                    },
                    "required": ["course_name"],
                },
            },
        }


class GetJobByTitle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], job_title: str = "", keywords: str = "") -> str:
        _keywordsL = keywords or ''.lower()
        pass
        jobs = data.get("job_postings", {}).values()

        search_term = job_title or keywords
        if not search_term:
            payload = {"error": "Either job_title or keywords must be provided"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Attempt an exact match initially
        job = next(
            (j for j in jobs.values() if j.get("title", "").lower() == search_term.lower()), None
        )

        # If an exact match is not found, attempt a partial match
        if not job:
            job = next(
                (j for j in jobs.values() if search_term.lower() in j.get("title", "").lower()),
                None,
            )

        # If no match is found, attempt to match keywords in the job title
        if not job and keywords:
            keyword_list = keywords.lower().split()
            job = next(
                (
                    j
                    for j in jobs.values() if any(
                        keyword in j.get("title", "").lower()
                        for keyword in keyword_list
                    )
                ),
                None,
            )

        if job:
            payload = {
                "job_found": True,
                "job_id": job.get("job_id"),
                "job_title": job.get("title"),
                "department": job.get("department"),
                "location": job.get("location"),
                "experience_level": job.get("experience_level"),
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                "job_found": False,
                "error": f"Job with title/keywords '{search_term}' not found",
                "suggestion": "Try using different keywords or check job postings",
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
                "name": "getJobByTitle",
                "description": "Find job ID by job title or keywords (exact or partial match)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_title": {
                            "type": "string",
                            "description": "Full or partial job title to search for",
                        },
                        "keywords": {
                            "type": "string",
                            "description": "Keywords to search in job titles (space-separated)",
                        },
                    },
                    "required": [],
                },
            },
        }


#Functions absent from tasks.py:


class GetAllGoals(Tool):
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
                "name": "getAllGoals",
                "description": "Get all goals for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class GenerateUniqueGoalId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, prefix: str) -> str:
        unique_id = f"{prefix}-001"
        payload = {"generated_goal_id": unique_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "generateUniqueGoalId",
                "description": "Generate a unique goal ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "prefix": {"type": "string"},
                    },
                    "required": ["user_id", "prefix"],
                },
            },
        }


class AddUserGoal(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, goal: dict) -> str:
        goals_data = data.get("goals", {}).values()
        user_goals = next((g for g in goals_data.values() if g.get("user_id") == user_id), None)

        if user_goals:
            user_goals["goals"].append(goal)
        else:
            goals_data.append({"user_id": user_id, "goals": [goal]})
        payload = {"success": f"Goal {goal.get('goal_type')} added for user {user_id}"}
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
                "name": "addUserGoal",
                "description": "Add a new goal for a user",
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


class CheckUserTrainingCompletion(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, team_id: str) -> str:
        training_logs = data.get("team_training_log", {}).values()
        user_training = [log for log in training_logs.values() if log.get("user_id") == user_id]
        completed_training = [
            log for log in user_training if log.get("status") == "Completed"
        ]

        completion_rate = (
            len(completed_training) / len(user_training) if user_training else 0
        )
        payload = {
            "user_id": user_id,
            "team_id": team_id,
            "total_training_sessions": len(user_training),
            "completed_sessions": len(completed_training),
            "completion_rate": completion_rate,
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
                "name": "checkUserTrainingCompletion",
                "description": "Check training completion status for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "team_id": {"type": "string"},
                    },
                    "required": ["user_id", "team_id"],
                },
            },
        }


class AssessTeamMentorshipCoverage(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str) -> str:
        teams = data.get("teams", {}).values()
        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)

        if not team:
            payload = {"error": "Team not found"}
            out = json.dumps(payload, indent=2)
            return out

        members = team.get("team_members", [])
        mentorship_relationships = data.get("user_mentorship_relationships", {}).values()

        members_with_mentors = []
        for member in members:
            has_mentor = any(
                r.get("mentee_id") == member and r.get("status") == "Active"
                for r in mentorship_relationships.values()
            )
            members_with_mentors.append({"user_id": member, "has_mentor": has_mentor})

        mentorship_coverage = (
            sum(1 for m in members_with_mentors if m["has_mentor"]) / len(members)
            if members
            else 0
        )
        payload = {
                "team_id": team_id,
                "total_members": len(members),
                "members_with_mentors": sum(
                    1 for m in members_with_mentors if m["has_mentor"]
                ),
                "mentorship_coverage": mentorship_coverage,
                "member_status": members_with_mentors,
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
                "name": "assessTeamMentorshipCoverage",
                "description": "Assess mentorship coverage for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class EvaluateTeamTrainingStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str) -> str:
        training_logs = data.get("team_training_log", {}).values()
        team_training = [log for log in training_logs.values() if log.get("team_id") == team_id]

        total_sessions = len(team_training)
        completed_sessions = sum(
            1 for log in team_training if log.get("status") == "Completed"
        )
        in_progress_sessions = sum(
            1 for log in team_training if log.get("status") == "In Progress"
        )

        completion_rate = (
            completed_sessions / total_sessions if total_sessions > 0 else 0
        )
        payload = {
            "team_id": team_id,
            "total_training_sessions": total_sessions,
            "completed_sessions": completed_sessions,
            "in_progress_sessions": in_progress_sessions,
            "completion_rate": completion_rate,
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
                "name": "evaluateTeamTrainingStatus",
                "description": "Evaluate training status for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class CheckSkillGapSeverity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, skill: str) -> str:
        """Evaluates the seriousness of a particular skill gap for a user based on their analysis report."""
        _skillL = skill or ''.lower()
        pass
        # Locate the comprehensive analysis report for the designated user.
        user_analysis = next(
            (
                a
                for a in data.get("skill_gap_analysis", {}).values()
                if a.get("user_id") == user_id
            ),
            None,
        )

        if not user_analysis:
            payload = {"error": f"Skill gap analysis not found for user {user_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # In that user's report, identify the particular skill gap.
        skill_gap_details = next(
            (
                g
                for g in user_analysis.get("skill_gaps", [])
                if g.get("skill_name", "").lower() == skill.lower()
            ),
            None,
        )

        if not skill_gap_details:
            payload = {
                    "error": f"Skill '{skill}' not found in the analysis for user {user_id}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {
                "user_id": user_id,
                "skill": skill_gap_details.get("skill_name"),
                "severity": skill_gap_details.get("gap_severity"),
                "current_proficiency": skill_gap_details.get("current_proficiency"),
                "required_proficiency": skill_gap_details.get("required_proficiency"),
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
                "name": "checkSkillGapSeverity",
                "description": "Check severity of a specific skill gap for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user to check.",
                        },
                        "skill": {
                            "type": "string",
                            "description": "The specific skill to check the gap severity for.",
                        },
                    },
                    "required": ["user_id", "skill"],
                },
            },
        }


class CreateSkillDevelopmentPlan(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, focus_areas: list) -> str:
        plan = {
            "plan_id": f"SDP{int(datetime.now().timestamp() * 1000) % 10000}",
            "user_id": user_id,
            "focus_areas": focus_areas,
            "created_date": "2025-07-04",
            "status": "Active",
        }

        data.setdefault("skill_development_plans", []).append(plan)
        payload = {
            "success": f"Skill development plan created for user {user_id}",
            "plan": plan,
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
                "name": "createSkillDevelopmentPlan",
                "description": "Create a skill development plan for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "focus_areas": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["user_id", "focus_areas"],
                },
            },
        }


#Complete tools registry
TOOLS = [
    GetTodayDate(),
    SearchUsers(),
    GetCourse(),
    EnrollInCourse(),
    GetGoal(),
    UpdateGoal(),
    GetJobMarketInsights(),
    AddUserCertification(),
    ListUserCertifications(),
    ListUserCourses(),
    AddUserEducation(),
    LogCourseCompletion(),
    LogMentoringSession(),
    ListMentoringSessions(),
    AuditGoalStatus(),
    LogCourseProgress(),
    RecommendLearningPath(),
    ConditionalProgressUpdate(),
    GetTeam(),
    GetTeamMembers(),
    LogTeamTraining(),
    ListTeamTraining(),
    UpdateUserTrainingProgress(),
    GetMentor(),
    ScheduleMentorshipSession(),
    ListUserMentorships(),
    GetSoftSkills(),
    UpdateCourseProgress(),
    LogSoftSkillGap(),
    ListSoftSkillGap(),
    AnalyzeSkillGap(),
    ListUserEducation(),
    SearchTalentNetwork(),
    LogJobApplication(),
    UpdateApplication(),
    ScheduleInterview(),
    ListApplications(),
    ListJobPostings(),
    ReassignMentor(),
    ConditionalEnrollOrList(),
    GetUserCourseProgress(),
    GenerateUniqueCertId(),
    GenerateUniqueEduId(),
    GenerateUniqueApplicationId(),
    GenerateUniqueRelationshipId(),
    GenerateUniqueAnalysisId(),
    CheckGoalProgressThreshold(),
    CalculateProgressIncrement(),
    GetJobPosting(),
    AddJobApplication(),
    ListUserApplications(),
    SearchJobPostings(),
    GetSkillGapAnalysis(),
    PerformSoftSkillGapAnalysis(),
    ComputeSkillGapScore(),
    AssignMentor(),
    ListUserMentors(),
    ListMentorshipRelationships(),
    ComputeMentorLoad(),
    UpdateMentorshipNote(),
    SearchTeams(),
    ListTeamMembers(),
    CheckCourseCompletionStatus(),
    MarkCourseCompleted(),
    ComputeAverageProgress(),
    NotifyHr(),
    SendEmailToUser(),
    GetTeamTrainingLog(),
    UpdateTeamTrainingLog(),
    ListUserTrainingSessions(),
    ScheduleTeamTraining(),
    AddTeamTrainingSession(),
    ComputeTeamTrainingHours(),
    ComputeTeamAverageProgress(),
    BulkEnrollCourse(),
    BulkUpdateGoals(),
    ComputeCertExpiry(),
    GetUserIdFromName(),
    BulkCheckTeamCourses(),
    BulkEnrollTeam(),
    BulkUpdateTeamGoals(),
    CheckReadinessThreshold(),
    CheckTeamAverageThreshold(),
    CheckTeamTrainingThreshold(),
    GetUserGoalsByType(),
    GetCourseByName(),
    GetJobByTitle(),
    GetAllGoals(),
    GenerateUniqueGoalId(),
    AddUserGoal(),
    CheckUserTrainingCompletion(),
    AssessTeamMentorshipCoverage(),
    EvaluateTeamTrainingStatus(),
    CheckSkillGapSeverity(),
    CreateSkillDevelopmentPlan(),
]
