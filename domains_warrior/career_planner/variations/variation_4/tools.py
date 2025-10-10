import json
import uuid
from datetime import datetime
from typing import Any, Dict, Optional
from domains.dto import Tool


# Basic utility tools
class get_today_date(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        return json.dumps({"today": "2025-07-04"}, indent=2)

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


class update_goal(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, goal_id: str, updates: dict) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), None)
        if user_goals:
            goals = user_goals.get("goals", [])
            goal = next((g for g in goals if g.get("goal_id") == goal_id), None)
            if goal:
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


class get_job_market_insights(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], role: str) -> str:
        insights = data.get("job_market_insights", [])
        insight = next(
            (i for i in insights if i.get("role", "").lower() == role.lower()), None
        )
        if insight:
            return json.dumps(insight, indent=2)
        else:
            return json.dumps(
                {"role": role, "insights": "Market data not available"}, indent=2
            )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_job_market_insights",
                "description": "Get job market insights for a role",
                "parameters": {
                    "type": "object",
                    "properties": {"role": {"type": "string"}},
                    "required": ["role"],
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


class list_user_certifications(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        certs = [
            c for c in data.get("user_certification", []) if c.get("user_id") == user_id
        ]
        return json.dumps({"certifications": certs}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_certifications",
                "description": "List certifications for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
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
                "description": "List courses for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class add_user_education(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, education: dict) -> str:
        education["user_id"] = user_id
        data.setdefault("user_education", []).append(education)
        return json.dumps(
            {"success": f"Education record added for user {user_id}"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "add_user_education",
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


class log_course_completion(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], user_id: str, course_id: str, completion_date: str
    ) -> str:
        # Update existing course progress or create new record
        courses = data.get("user_course_progress", [])
        course = next(
            (
                c
                for c in courses
                if c.get("user_id") == user_id and c.get("course_id") == course_id
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
        return json.dumps(
            {"success": f"Course {course_id} completion logged for user {user_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "log_course_completion",
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


class log_mentoring_session(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
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
        return json.dumps(
            {"success": f"Mentoring session logged for {mentee_id} with {mentor_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "log_mentoring_session",
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


class list_mentoring_sessions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], mentee_id: str) -> str:
        sessions = [
            s
            for s in data.get("mentoring_sessions", [])
            if s.get("mentee_id") == mentee_id
        ]
        return json.dumps({"sessions": sessions}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_mentoring_sessions",
                "description": "List mentoring sessions for a mentee",
                "parameters": {
                    "type": "object",
                    "properties": {"mentee_id": {"type": "string"}},
                    "required": ["mentee_id"],
                },
            },
        }


class audit_goal_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, goal_id: str) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), {})
        goals = user_goals.get("goals", [])
        goal = next((g for g in goals if g.get("goal_id") == goal_id), None)
        if goal:
            return json.dumps(
                {
                    "audit": f"Goal {goal_id} status: {goal.get('status', 'Unknown')}, Progress: {goal.get('progress_percent', 0)}%"
                },
                indent=2,
            )
        return json.dumps({"error": "Goal not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "audit_goal_status",
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


class log_course_progress(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
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
        return json.dumps(
            {
                "success": f"Course progress logged for {user_id} in {course_id}: {progress}%"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "log_course_progress",
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


class recommend_learning_path(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_id: str,
        soft_skill: str,
        course_id: str,
        enroll_date: str,
        goal_id: str,
        progress_percent: int,
    ) -> str:
        # Log the recommendation
        recommendation = {
            "user_id": user_id,
            "soft_skill": soft_skill,
            "course_id": course_id,
            "enroll_date": enroll_date,
            "goal_id": goal_id,
            "progress_percent": progress_percent,
        }
        data.setdefault("learning_path_recommendations", []).append(recommendation)
        return json.dumps(
            {"success": f"Learning path recommended for {user_id} in {soft_skill}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "recommend_learning_path",
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


class conditional_progress_update(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_id: str,
        goal_id: str,
        increment: int,
        threshold: int,
        update_date: str,
    ) -> str:
        # Get current goal progress
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), {})
        goals = user_goals.get("goals", [])
        goal = next((g for g in goals if g.get("goal_id") == goal_id), None)

        if goal:
            current_progress = goal.get("progress_percent", 0)
            if current_progress < threshold:
                new_progress = current_progress + increment
                goal.update(
                    {"progress_percent": new_progress, "last_updated": update_date}
                )
                return json.dumps(
                    {
                        "success": f"Goal {goal_id} progress updated from {current_progress}% to {new_progress}%"
                    },
                    indent=2,
                )
            else:
                return json.dumps(
                    {
                        "result": f"Goal {goal_id} progress ({current_progress}%) already meets threshold"
                    },
                    indent=2,
                )
        return json.dumps({"error": "Goal not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "conditional_progress_update",
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


# Tool to fetch team details by team_id from teams.json.
class get_team(Tool):
    @staticmethod
    def invoke(data, team_id: str) -> str:
        for team in data.get("teams", []):
            if team.get("team_id") == team_id:
                return json.dumps(team, indent=2)
        return json.dumps({"error": "Team not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_team",
                "description": "Fetch team details using the provided team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


# Tool to fetch team members from a team record.
class get_team_members(Tool):
    @staticmethod
    def invoke(data, team_id: str) -> str:
        for team in data.get("teams", []):
            if team.get("team_id") == team_id:
                return json.dumps(
                    {"team_members": team.get("team_members", [])}, indent=2
                )
        return json.dumps({"error": "Team not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_team_members",
                "description": "Return the list of team members for a given team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


# Tool to log a team training session into team_training_log.
class log_team_training(Tool):
    @staticmethod
    def invoke(data, team_id: str, training_session: dict) -> str:
        data.setdefault("team_training_log", []).append(training_session)
        return json.dumps(
            {
                "success": f"Training session {training_session['training_session_id']} logged for team {team_id}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "log_team_training",
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


# Tool to list team training sessions for a given team.
class list_team_training(Tool):
    @staticmethod
    def invoke(data, team_id: str) -> str:
        sessions = [
            ts
            for ts in data.get("team_training_log", [])
            if ts.get("training_session_id", "").startswith("TS")
        ]
        # (In a real scenario, you would filter by team_id)
        return json.dumps({"team_training_log": sessions}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_team_training",
                "description": "List all training sessions for a specific team.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


# Tool to update an individual's training progress.
class update_user_training_progress(Tool):
    @staticmethod
    def invoke(data, user_id: str, training_session_id: str, progress: int) -> str:
        record = {
            "user_id": user_id,
            "training_session_id": training_session_id,
            "progress": progress,
        }
        data.setdefault("user_training_progress", []).append(record)
        return json.dumps(
            {
                "success": f"Training progress for {user_id} on session {training_session_id} set to {progress}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "update_user_training_progress",
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


# Tool to get mentor details by mentor_id.
class get_mentor(Tool):
    @staticmethod
    def invoke(data, mentor_id: str) -> str:
        for mentor in data.get("user_mentorship", []):
            if mentor.get("mentor_id") == mentor_id:
                return json.dumps(mentor, indent=2)
        return json.dumps({"error": "Mentor not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_mentor",
                "description": "Fetch mentor details using mentor_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"mentor_id": {"type": "string"}},
                    "required": ["mentor_id"],
                },
            },
        }


# Tool to schedule a mentorship session by adding a record.
class schedule_mentorship_session(Tool):
    @staticmethod
    def invoke(data, relationship: dict) -> str:
        data.setdefault("user_mentorship_relationships", []).append(relationship)
        return json.dumps(
            {
                "success": f"Mentorship session {relationship['relationship_id']} scheduled"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "schedule_mentorship_session",
                "description": "Schedule a new mentorship session by adding a new relationship record.",
                "parameters": {
                    "type": "object",
                    "properties": {"relationship": {"type": "object"}},
                    "required": ["relationship"],
                },
            },
        }


# Tool to list a user's mentorship relationships.
class list_user_mentorships(Tool):
    @staticmethod
    def invoke(data, user_id: str) -> str:
        rels = [
            rel
            for rel in data.get("user_mentorship_relationships", [])
            if rel.get("user_id") == user_id
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


# Tool to fetch details of a soft skill.
class get_soft_skills(Tool):
    @staticmethod
    def invoke(data, skill: str) -> str:
        return json.dumps(data.get("soft_skills", {}).get(skill, {}), indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_soft_skills",
                "description": "Return details for a specific soft skill.",
                "parameters": {
                    "type": "object",
                    "properties": {"skill": {"type": "string"}},
                    "required": ["skill"],
                },
            },
        }


# Tool to update the progress of a course for a user.
class update_course_progress(Tool):
    @staticmethod
    def invoke(data, user_id: str, course_id: str, progress_percent: int) -> str:
        record = {
            "user_id": user_id,
            "course_id": course_id,
            "progress_percent": progress_percent,
        }
        data.setdefault("course_progress_updates", []).append(record)
        return json.dumps(
            {
                "success": f"Course {course_id} progress for {user_id} updated to {progress_percent}%."
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "update_course_progress",
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


# Tool to log a soft skill gap analysis record.
class log_soft_skill_gap(Tool):
    @staticmethod
    def invoke(data, user_id: str, analysis: dict) -> str:
        data.setdefault("skill_gap_analysis", []).append(analysis)
        return json.dumps(
            {
                "success": f"Soft skill gap analysis {analysis['analysis_id']} logged for {user_id}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "log_soft_skill_gap",
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


# Tool to list soft skill gap analysis records for a user filtered by skill.
class list_soft_skill_gap(Tool):
    @staticmethod
    def invoke(data, user_id: str, skill: str) -> str:
        analyses = [
            a
            for a in data.get("skill_gap_analysis", [])
            if a.get("skill") == skill and a.get("user_id", user_id) == user_id
        ]
        return json.dumps({"soft_skill_gap": analyses}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_soft_skill_gap",
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


# Tool to analyze a skill gap and return analysis details (and log it).
class analyze_skill_gap(Tool):
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
        return json.dumps(analysis, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "analyze_skill_gap",
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


# Tool to list a user's education records.
class list_user_education(Tool):
    @staticmethod
    def invoke(data, user_id: str) -> str:
        edu = [e for e in data.get("user_education", []) if e.get("user_id") == user_id]
        return json.dumps({"education": edu}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_education",
                "description": "List all education records for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


# Tool to search the external talent network by candidate_id.
class search_talent_network(Tool):
    @staticmethod
    def invoke(data, candidate_id: str) -> str:
        for candidate in data.get("talent_network", []):
            if candidate.get("candidate_id") == candidate_id:
                return json.dumps(candidate, indent=2)
        return json.dumps({"error": "Candidate not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "search_talent_network",
                "description": "Search for an external candidate by candidate_id in the talent network.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }


# Tool to log an external job application.
class log_job_application(Tool):
    @staticmethod
    def invoke(
        data,
        candidate_id: str,
        job_id: str,
        apply_date: str,
        skill_match_score: int,
        application_id: Optional[str] = None,
    ) -> str:
        application = {
            "application_id": application_id or "APP001",
            "candidate_id": candidate_id,
            "job_id": job_id,
            "apply_date": apply_date,
            "skill_match_score": skill_match_score,
        }
        data.setdefault("job_applications", []).append(application)
        return json.dumps(
            {
                "success": f"Application {application['application_id']} logged for candidate {candidate_id}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "log_job_application",
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


# Tool to update details of a job application.
class update_application(Tool):
    @staticmethod
    def invoke(data, candidate_id: str, application_id: str, updates: dict) -> str:
        updated = False
        for app in data.get("job_applications", []):
            if (
                app.get("application_id") == application_id
                and app.get("candidate_id") == candidate_id
            ):
                app.update(updates)
                updated = True
        if updated:
            return json.dumps(
                {
                    "success": f"Application {application_id} updated for candidate {candidate_id}"
                },
                indent=2,
            )
        else:
            return json.dumps({"error": "Application not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "update_application",
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


# Tool to schedule an interview for a candidate.
class schedule_interview(Tool):
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
        return json.dumps(
            {
                "success": f"Interview scheduled for application {application_id} on {interview_date}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "schedule_interview",
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


# Tool to list all applications for a candidate.
class list_applications(Tool):
    @staticmethod
    def invoke(data, candidate_id: str) -> str:
        apps = [
            app
            for app in data.get("job_applications", [])
            if app.get("candidate_id") == candidate_id
        ]
        return json.dumps({"applications": apps}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_applications",
                "description": "List all job applications for a given candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }


# Tool to list job postings filtered by role.
class list_job_postings(Tool):
    @staticmethod
    def invoke(data, role: str) -> str:
        postings = [
            jp
            for jp in data.get("job_postings", [])
            if jp.get("title", "").find(role) != -1
        ]
        return json.dumps({"job_postings": postings}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_job_postings",
                "description": "List all job postings for a given role.",
                "parameters": {
                    "type": "object",
                    "properties": {"role": {"type": "string"}},
                    "required": ["role"],
                },
            },
        }


# Tool to reassign a user's mentorship from one mentor to another.
class reassign_mentor(Tool):
    @staticmethod
    def invoke(
        data, user_id: str, old_mentor_id: str, new_mentor_id: str, relationship_id: str
    ) -> str:
        # For simplicity, add a new record indicating the change.
        record = {
            "relationship_id": relationship_id,
            "user_id": user_id,
            "mentor_id": new_mentor_id,
            "reassigned_from": old_mentor_id,
            "updated_date": "2023-10-05",
        }
        data.setdefault("mentorship_reassignments", []).append(record)
        return json.dumps(
            {
                "success": f"Mentor reassigned for {user_id}: now under mentor {new_mentor_id}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "reassign_mentor",
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


# 1. Conditional enrollment tool: conditionally enrolls a user or lists enrollments.
class conditional_enroll_or_list(Tool):
    @staticmethod
    def invoke(
        data,
        user_id: str,
        course_id: str,
        goal_id: str,
        threshold: int,
        enroll_date: str,
    ) -> str:
        # Dummy condition: if the numeric part of user_id is odd, simulate enrollment.
        if int(user_id[1:]) % 2 == 1:
            # Simulate enrolling the user and updating the goal.
            # (In a real system, we would check the current progress from data.)
            return json.dumps(
                {
                    "result": f"User {user_id} enrolled in {course_id} and goal {goal_id} updated to {threshold}%."
                },
                indent=2,
            )
        else:
            # Otherwise simulate returning a list of current enrollments.
            return json.dumps(
                {
                    "result": f"User {user_id} already meets threshold; enrollments listed."
                },
                indent=2,
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "conditional_enroll_or_list",
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


class get_user_course_progress(Tool):
    @staticmethod
    def invoke(data, user_id: str, course_id: str):
        # Minimal simulation: Return a mock object with "status" or "grade"
        # In real usage, we would look up user_course_progress in data
        return json.dumps(
            {"user_course_progress": {"status": "Not Completed", "grade": 0}}, indent=2
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_user_course_progress",
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


# ID Generation Tools
class generate_unique_cert_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], prefix: str) -> str:
        unique_id = f"{prefix}001"
        return json.dumps({"generated_cert_id": unique_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "generate_unique_cert_id",
                "description": "Generate a unique certification ID",
                "parameters": {
                    "type": "object",
                    "properties": {"prefix": {"type": "string"}},
                    "required": ["prefix"],
                },
            },
        }


class generate_unique_edu_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], prefix: str) -> str:
        unique_id = f"{prefix}001"
        return json.dumps({"generated_edu_id": unique_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "generate_unique_edu_id",
                "description": "Generate a unique education ID",
                "parameters": {
                    "type": "object",
                    "properties": {"prefix": {"type": "string"}},
                    "required": ["prefix"],
                },
            },
        }


class generate_unique_application_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], prefix: str) -> str:
        unique_id = f"{prefix}001"
        return json.dumps({"generated_application_id": unique_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "generate_unique_application_id",
                "description": "Generate a unique application ID",
                "parameters": {
                    "type": "object",
                    "properties": {"prefix": {"type": "string"}},
                    "required": ["prefix"],
                },
            },
        }


class generate_unique_relationship_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], prefix: str) -> str:
        unique_id = f"{prefix}001"
        return json.dumps({"generated_relationship_id": unique_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "generate_unique_relationship_id",
                "description": "Generate a unique relationship ID",
                "parameters": {
                    "type": "object",
                    "properties": {"prefix": {"type": "string"}},
                    "required": ["prefix"],
                },
            },
        }


class generate_unique_analysis_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], prefix: str) -> str:
        unique_id = f"{prefix}001"
        return json.dumps({"generated_analysis_id": unique_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "generate_unique_analysis_id",
                "description": "Generate a unique analysis ID",
                "parameters": {
                    "type": "object",
                    "properties": {"prefix": {"type": "string"}},
                    "required": ["prefix"],
                },
            },
        }


# Progress and Calculation Tools
class check_goal_progress_threshold(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_id: str,
        goal_id: str,
        threshold: int,
        comparison: str,
    ) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), {})
        goals = user_goals.get("goals", [])
        goal = next((g for g in goals if g.get("goal_id") == goal_id), None)

        if not goal:
            return json.dumps(
                {"meets_threshold": False, "error": "Goal not found"}, indent=2
            )

        progress = goal.get("progress_percent", 0)
        meets_threshold = False

        if comparison == "below":
            meets_threshold = progress < threshold
        elif comparison == "above":
            meets_threshold = progress > threshold
        elif comparison == "equal":
            meets_threshold = progress == threshold

        return json.dumps(
            {
                "meets_threshold": meets_threshold,
                "current_progress": progress,
                "threshold": threshold,
                "comparison": comparison,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "check_goal_progress_threshold",
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


class calculate_progress_increment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], current_progress: Any, increment: int) -> str:
        if current_progress == "get_from_goal":
            # This would be dynamically calculated based on the goal
            calculated_value = min(100, increment)  # Simplified
        else:
            calculated_value = min(100, current_progress + increment)

        return json.dumps({"calculated_value": calculated_value}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "calculate_progress_increment",
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


# Job and Application Tools
class get_job_posting(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], job_id: str) -> str:
        job_postings = data.get("job_postings", [])
        job = next((j for j in job_postings if j.get("job_id") == job_id), None)
        return (
            json.dumps(job, indent=2)
            if job
            else json.dumps({"error": "Job posting not found"}, indent=2)
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_job_posting",
                "description": "Get job posting details by job ID",
                "parameters": {
                    "type": "object",
                    "properties": {"job_id": {"type": "string"}},
                    "required": ["job_id"],
                },
            },
        }


class add_job_application(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
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
        return json.dumps(
            {"success": f"Application {application_id} created for user {user_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "add_job_application",
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


class list_user_applications(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        applications = [
            app
            for app in data.get("job_applications", [])
            if app.get("user_id") == user_id
        ]
        return json.dumps({"applications": applications}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_applications",
                "description": "List all job applications for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class search_job_postings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], filters: dict) -> str:
        job_postings = data.get("job_postings", [])
        if "job_id" in filters:
            job = next(
                (j for j in job_postings if j.get("job_id") == filters["job_id"]), None
            )
            return (
                json.dumps(job, indent=2)
                if job
                else json.dumps({"error": "Job not found"}, indent=2)
            )
        return json.dumps({"job_postings": job_postings}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "search_job_postings",
                "description": "Search for job postings by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }


# Skill Gap Analysis Tools
class get_skill_gap_analysis(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str = "", analysis_id: str = "") -> str:
        skill_gaps = data.get("skill_gap_analysis", [])
        if analysis_id:
            analysis = next(
                (s for s in skill_gaps if s.get("analysis_id") == analysis_id), None
            )
        elif user_id:
            analysis = next(
                (s for s in skill_gaps if s.get("user_id") == user_id), None
            )
        else:
            return json.dumps(
                {"error": "Either user_id or analysis_id required"}, indent=2
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


class perform_soft_skill_gap_analysis(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, skills: list) -> str:
        analysis = {
            "analysis_id": f"SGA{int(datetime.now().timestamp() * 1000) % 10000}",
            "user_id": user_id,
            "skills_analyzed": skills,
            "readiness_score": 65,  # Mock score
            "date": "2025-07-04",
        }
        data.setdefault("skill_gap_analysis", []).append(analysis)
        return json.dumps(
            {"success": f"Analysis completed for user {user_id}", "analysis": analysis},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "perform_soft_skill_gap_analysis",
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


class compute_skill_gap_score(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        # Mock computation - in real system would analyze actual skill gaps
        score = 45  # Mock score below threshold
        return json.dumps({"readiness_score": score, "user_id": user_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "compute_skill_gap_score",
                "description": "Compute skill gap readiness score for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


# Team and Mentor Tools
class assign_mentor(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
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
        return json.dumps(
            {"success": f"Mentor {mentor_id} assigned to {mentee}"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "assign_mentor",
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


class list_user_mentors(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        mentorships = [
            m
            for m in data.get("user_mentorship_relationships", [])
            if m.get("mentee_id") == user_id
        ]
        return json.dumps({"mentorships": mentorships}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_mentors",
                "description": "List all mentors for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class list_mentorship_relationships(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], filters: dict) -> str:
        relationships = data.get("user_mentorship_relationships", [])
        if "mentor_id" in filters:
            relationships = [
                r for r in relationships if r.get("mentor_id") == filters["mentor_id"]
            ]
        if "status" in filters:
            relationships = [
                r for r in relationships if r.get("status") == filters["status"]
            ]
        return json.dumps({"relationships": relationships}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_mentorship_relationships",
                "description": "List mentorship relationships by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }


class compute_mentor_load(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], mentor_id: str) -> str:
        relationships = [
            r
            for r in data.get("user_mentorship_relationships", [])
            if r.get("mentor_id") == mentor_id and r.get("status") == "Active"
        ]
        load = len(relationships)
        return json.dumps({"mentor_load": load, "mentor_id": mentor_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "compute_mentor_load",
                "description": "Compute the current active mentee load for a mentor",
                "parameters": {
                    "type": "object",
                    "properties": {"mentor_id": {"type": "string"}},
                    "required": ["mentor_id"],
                },
            },
        }


class update_mentorship_note(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], mentor_id: str, mentee_id: str, note: str) -> str:
        note_record = {
            "mentor_id": mentor_id,
            "mentee_id": mentee_id,
            "note": note,
            "date": "2025-07-04",
        }
        data.setdefault("mentorship_notes", []).append(note_record)
        return json.dumps({"success": "Note added to mentorship record"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "update_mentorship_note",
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


# Team Tools
class search_teams(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], filters: dict) -> str:
        teams = data.get("teams", [])
        if "team_id" in filters:
            team = next(
                (t for t in teams if t.get("team_id") == filters["team_id"]), None
            )
            return (
                json.dumps(team, indent=2)
                if team
                else json.dumps({"error": "Team not found"}, indent=2)
            )
        return json.dumps({"teams": teams}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "search_teams",
                "description": "Search for teams by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }


class list_team_members(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if team:
            members = team.get("members", [])
            return json.dumps({"members": members}, indent=2)
        return json.dumps({"error": "Team not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_team_members",
                "description": "List all members of a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


# Additional Tools
class check_course_completion_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, course_id: str) -> str:
        progress = data.get("user_course_progress", [])
        user_progress = next(
            (
                p
                for p in progress
                if p.get("user_id") == user_id and p.get("course_id") == course_id
            ),
            None,
        )
        completed = (
            user_progress.get("status") == "Completed" if user_progress else False
        )
        return json.dumps(
            {"completed": completed, "user_id": user_id, "course_id": course_id},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "check_course_completion_status",
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


class mark_course_completed(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], user_id: str, course_id: str, completion_date: str
    ) -> str:
        progress = data.get("user_course_progress", [])
        user_progress = next(
            (
                p
                for p in progress
                if p.get("user_id") == user_id and p.get("course_id") == course_id
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
            progress.append(new_progress)
        return json.dumps(
            {"success": f"Course {course_id} marked completed for user {user_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "mark_course_completed",
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


class compute_average_progress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        progress = data.get("user_course_progress", [])
        user_courses = [p for p in progress if p.get("user_id") == user_id]
        if not user_courses:
            return json.dumps({"average_progress": 0}, indent=2)

        total_progress = sum(p.get("current_progress_percent", 0) for p in user_courses)
        average = total_progress / len(user_courses)
        return json.dumps({"average_progress": average, "user_id": user_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "compute_average_progress",
                "description": "Compute average course progress for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class notify_hr(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], message: str) -> str:
        notification = {
            "message": message,
            "timestamp": "2025-07-04",
            "type": "HR_NOTIFICATION",
        }
        data.setdefault("hr_notifications", []).append(notification)
        return json.dumps({"success": "HR notified", "message": message}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "notify_hr",
                "description": "Send a notification to HR",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }


class send_email_to_user(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, subject: str, body: str) -> str:
        email = {
            "user_id": user_id,
            "subject": subject,
            "body": body,
            "timestamp": "2025-07-04",
        }
        data.setdefault("emails_sent", []).append(email)
        return json.dumps({"success": f"Email sent to user {user_id}"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "send_email_to_user",
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


# Additional missing tools
class get_team_training_log(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str) -> str:
        training_logs = data.get("team_training_log", [])
        team_logs = [log for log in training_logs if log.get("team_id") == team_id]
        return json.dumps({"training_logs": team_logs}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_team_training_log",
                "description": "Get training logs for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class update_team_training_log(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
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
        return json.dumps({"success": f"Training log updated for {user_id}"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "update_team_training_log",
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


class list_user_training_sessions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        training_logs = data.get("team_training_log", [])
        user_sessions = [log for log in training_logs if log.get("user_id") == user_id]
        return json.dumps({"training_sessions": user_sessions}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_training_sessions",
                "description": "List training sessions for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class schedule_team_training(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], team_id: str, course_id: str, session_date: str
    ) -> str:
        training_session = {
            "team_id": team_id,
            "course_id": course_id,
            "session_date": session_date,
            "status": "Scheduled",
        }
        data.setdefault("team_training_sessions", []).append(training_session)
        return json.dumps(
            {"success": f"Training session scheduled for team {team_id}"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "schedule_team_training",
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


class add_team_training_session(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str, training: dict) -> str:
        training["team_id"] = team_id
        data.setdefault("team_training_sessions", []).append(training)
        return json.dumps(
            {"success": f"Training session added for team {team_id}"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "add_team_training_session",
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


class compute_team_training_hours(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str, year: int = 2025) -> str:
        training_logs = data.get("team_training_log", [])
        team_logs = [log for log in training_logs if log.get("team_id") == team_id]
        total_hours = len(team_logs) * 8  # Mock calculation
        return json.dumps({"total_hours": total_hours, "team_id": team_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "compute_team_training_hours",
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


class compute_team_average_progress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

        members = team.get("members", [])
        if not members:
            return json.dumps({"average_progress": 0}, indent=2)

        total_progress = 0
        for member in members:
            user_progress = data.get("user_course_progress", [])
            user_courses = [p for p in user_progress if p.get("user_id") == member]
            if user_courses:
                avg_progress = sum(
                    p.get("current_progress_percent", 0) for p in user_courses
                ) / len(user_courses)
                total_progress += avg_progress

        team_average = total_progress / len(members) if members else 0
        return json.dumps(
            {"team_average_progress": team_average, "team_id": team_id}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "compute_team_average_progress",
                "description": "Compute average course progress for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class bulk_enroll_course(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], team_id: str, course_id: str, enroll_date: str
    ) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

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

        return json.dumps(
            {"success": f"Bulk enrolled {len(members)} members in course {course_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "bulk_enroll_course",
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


class bulk_update_goals(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], team_id: str, goal_type: str, updates: dict
    ) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

        members = team.get("members", [])
        goals_data = data.get("goals", [])

        for member in members:
            user_goals = next(
                (g for g in goals_data if g.get("user_id") == member), None
            )
            if user_goals:
                for goal in user_goals.get("goals", []):
                    if goal_type.lower() in goal.get("title", "").lower():
                        goal.update(updates)

        return json.dumps(
            {"success": f"Bulk updated goals for {len(members)} members"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "bulk_update_goals",
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


class compute_cert_expiry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, cert_id: str) -> str:
        # Mock implementation - in real system would check actual expiry dates
        return json.dumps(
            {"expiry_date": "2026-03-12", "days_until_expiry": 251}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "compute_cert_expiry",
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


class bulk_check_team_courses(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

        members = team.get("team_members", [])
        progress_data = data.get("user_course_progress", [])
        team_progress = []

        for member_id in members:
            member_courses = [p for p in progress_data if p.get("user_id") == member_id]
            avg_progress = (
                sum(c.get("current_progress_percent", 0) for c in member_courses)
                / len(member_courses)
                if member_courses
                else 0
            )
            team_progress.append(
                {"user_id": member_id, "average_progress": avg_progress}
            )

        return json.dumps(
            {"team_id": team_id, "member_progress": team_progress}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "bulk_check_team_courses",
                "description": "Check course progress for all team members",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class bulk_enroll_team(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], team_id: str, course_id: str, enroll_date: str
    ) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

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

        return json.dumps(
            {
                "success": f"Team {team_id} enrolled in course {course_id}",
                "enrolled_members": enrolled_members,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "bulk_enroll_team",
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


class bulk_update_team_goals(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], team_id: str, goal_type: str, updates: dict
    ) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

        members = team.get("team_members", [])
        goals_data = data.get("goals", [])
        updated_goals = []

        for member_id in members:
            user_goals = next(
                (g for g in goals_data if g.get("user_id") == member_id), None
            )
            if user_goals:
                goals = user_goals.get("goals", [])
                for goal in goals:
                    if goal_type.lower() in goal.get("goal_name", "").lower():
                        goal.update(updates)
                        updated_goals.append(
                            {"user_id": member_id, "goal_id": goal.get("goal_id")}
                        )

        return json.dumps(
            {
                "success": f"Team {team_id} goals updated",
                "updated_goals": updated_goals,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "bulk_update_team_goals",
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


class check_readiness_threshold(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], user_id: str, threshold: int, comparison: str
    ) -> str:
        # Mock implementation - in real system would check actual readiness scores
        readiness_score = 75  # Mock score

        if comparison == "below":
            meets_condition = readiness_score < threshold
        elif comparison == "above":
            meets_condition = readiness_score > threshold
        else:
            meets_condition = readiness_score == threshold

        return json.dumps(
            {
                "user_id": user_id,
                "readiness_score": readiness_score,
                "threshold": threshold,
                "comparison": comparison,
                "meets_condition": meets_condition,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "check_readiness_threshold",
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


class check_team_average_threshold(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], team_id: str, threshold: int, comparison: str
    ) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

        members = team.get("team_members", [])
        progress_data = data.get("user_course_progress", [])

        # Calculate team average
        total_progress = 0
        member_count = 0

        for member_id in members:
            member_courses = [p for p in progress_data if p.get("user_id") == member_id]
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

        return json.dumps(
            {
                "team_id": team_id,
                "team_average": team_average,
                "threshold": threshold,
                "comparison": comparison,
                "meets_condition": meets_condition,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "check_team_average_threshold",
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


class check_team_training_threshold(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], team_id: str, threshold: int, comparison: str
    ) -> str:
        # Mock team training hours calculation
        training_data = data.get("team_training_log", [])
        team_sessions = [t for t in training_data if t.get("team_id") == team_id]

        # Mock calculation - in real system would sum actual training hours
        total_hours = len(team_sessions) * 25  # Assume 25 hours per session

        if comparison == "below":
            condition_met = total_hours < threshold
            return json.dumps(
                {
                    "condition_met": condition_met,
                    "team_id": team_id,
                    "total_hours": total_hours,
                    "threshold": threshold,
                    "comparison": comparison,
                },
                indent=2,
            )
        else:
            condition_met = total_hours >= threshold
            return json.dumps(
                {
                    "condition_met": condition_met,
                    "team_id": team_id,
                    "total_hours": total_hours,
                    "threshold": threshold,
                    "comparison": comparison,
                },
                indent=2,
            )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "check_team_training_threshold",
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


class get_user_goals_by_type(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_id: str,
        goal_type: str = "",
        goal_description_keywords: str = "",
    ) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), {})
        goals = user_goals.get("goals", [])

        filtered_goals = goals

        # Filter by goal type if provided
        if goal_type:
            filtered_goals = [
                g
                for g in filtered_goals
                if g.get("goal_type", "").lower() == goal_type.lower()
            ]

        # Filter by keywords in goal description if provided
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

        return json.dumps(
            {
                "user_id": user_id,
                "matching_goals": filtered_goals,
                "total_goals_found": len(filtered_goals),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_user_goals_by_type",
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


class get_course_by_name(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], course_name: str) -> str:
        courses = data.get("course_catalog", [])

        # Try exact match first
        course = next(
            (c for c in courses if c.get("name", "").lower() == course_name.lower()),
            None,
        )

        # If no exact match, try partial match
        if not course:
            course = next(
                (
                    c
                    for c in courses
                    if course_name.lower() in c.get("name", "").lower()
                ),
                None,
            )

        if course:
            return json.dumps(
                {
                    "course_found": True,
                    "course_id": course.get("course_id"),
                    "course_name": course.get("name"),
                    "provider": course.get("provider"),
                    "level": course.get("level"),
                },
                indent=2,
            )
        else:
            return json.dumps(
                {
                    "course_found": False,
                    "error": f"Course '{course_name}' not found",
                    "suggestion": "Try using partial course name or check course catalog",
                },
                indent=2,
            )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_course_by_name",
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


class get_job_by_title(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], job_title: str = "", keywords: str = "") -> str:
        jobs = data.get("job_postings", [])

        search_term = job_title or keywords
        if not search_term:
            return json.dumps(
                {"error": "Either job_title or keywords must be provided"}, indent=2
            )

        # Try exact match first
        job = next(
            (j for j in jobs if j.get("title", "").lower() == search_term.lower()), None
        )

        # If no exact match, try partial match
        if not job:
            job = next(
                (j for j in jobs if search_term.lower() in j.get("title", "").lower()),
                None,
            )

        # If still no match, try matching keywords in job title
        if not job and keywords:
            keyword_list = keywords.lower().split()
            job = next(
                (
                    j
                    for j in jobs
                    if any(
                        keyword in j.get("title", "").lower()
                        for keyword in keyword_list
                    )
                ),
                None,
            )

        if job:
            return json.dumps(
                {
                    "job_found": True,
                    "job_id": job.get("job_id"),
                    "job_title": job.get("title"),
                    "department": job.get("department"),
                    "location": job.get("location"),
                    "experience_level": job.get("experience_level"),
                },
                indent=2,
            )
        else:
            return json.dumps(
                {
                    "job_found": False,
                    "error": f"Job with title/keywords '{search_term}' not found",
                    "suggestion": "Try using different keywords or check job postings",
                },
                indent=2,
            )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_job_by_title",
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


# Missing functions from tasks.py:


class get_all_goals(Tool):
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
                "name": "get_all_goals",
                "description": "Get all goals for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class generate_unique_goal_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, prefix: str) -> str:
        unique_id = f"{prefix}-001"
        return json.dumps({"generated_goal_id": unique_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "generate_unique_goal_id",
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


class add_user_goal(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, goal: dict) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), None)

        if user_goals:
            user_goals["goals"].append(goal)
        else:
            goals_data.append({"user_id": user_id, "goals": [goal]})

        return json.dumps(
            {"success": f"Goal {goal.get('goal_type')} added for user {user_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "add_user_goal",
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


class check_user_training_completion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, team_id: str) -> str:
        training_logs = data.get("team_training_log", [])
        user_training = [log for log in training_logs if log.get("user_id") == user_id]
        completed_training = [
            log for log in user_training if log.get("status") == "Completed"
        ]

        completion_rate = (
            len(completed_training) / len(user_training) if user_training else 0
        )

        return json.dumps(
            {
                "user_id": user_id,
                "team_id": team_id,
                "total_training_sessions": len(user_training),
                "completed_sessions": len(completed_training),
                "completion_rate": completion_rate,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "check_user_training_completion",
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


class assess_team_mentorship_coverage(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)

        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

        members = team.get("team_members", [])
        mentorship_relationships = data.get("user_mentorship_relationships", [])

        members_with_mentors = []
        for member in members:
            has_mentor = any(
                r.get("mentee_id") == member and r.get("status") == "Active"
                for r in mentorship_relationships
            )
            members_with_mentors.append({"user_id": member, "has_mentor": has_mentor})

        mentorship_coverage = (
            sum(1 for m in members_with_mentors if m["has_mentor"]) / len(members)
            if members
            else 0
        )

        return json.dumps(
            {
                "team_id": team_id,
                "total_members": len(members),
                "members_with_mentors": sum(
                    1 for m in members_with_mentors if m["has_mentor"]
                ),
                "mentorship_coverage": mentorship_coverage,
                "member_status": members_with_mentors,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "assess_team_mentorship_coverage",
                "description": "Assess mentorship coverage for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class evaluate_team_training_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str) -> str:
        training_logs = data.get("team_training_log", [])
        team_training = [log for log in training_logs if log.get("team_id") == team_id]

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

        return json.dumps(
            {
                "team_id": team_id,
                "total_training_sessions": total_sessions,
                "completed_sessions": completed_sessions,
                "in_progress_sessions": in_progress_sessions,
                "completion_rate": completion_rate,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "evaluate_team_training_status",
                "description": "Evaluate training status for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class check_skill_gap_severity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, skill: str) -> str:
        """
        Checks the severity of a specific skill gap for a user from their analysis report.
        """
        # Find the overall analysis report for the specified user.
        user_analysis = next(
            (
                a
                for a in data.get("skill_gap_analysis", [])
                if a.get("user_id") == user_id
            ),
            None,
        )

        if not user_analysis:
            return json.dumps(
                {"error": f"Skill gap analysis not found for user {user_id}"}, indent=2
            )

        # Within that user's report, find the specific skill gap.
        skill_gap_details = next(
            (
                g
                for g in user_analysis.get("skill_gaps", [])
                if g.get("skill_name", "").lower() == skill.lower()
            ),
            None,
        )

        if not skill_gap_details:
            return json.dumps(
                {
                    "error": f"Skill '{skill}' not found in the analysis for user {user_id}"
                },
                indent=2,
            )

        # Return the details directly from the found skill gap record.
        return json.dumps(
            {
                "user_id": user_id,
                "skill": skill_gap_details.get("skill_name"),
                "severity": skill_gap_details.get("gap_severity"),
                "current_proficiency": skill_gap_details.get("current_proficiency"),
                "required_proficiency": skill_gap_details.get("required_proficiency"),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "check_skill_gap_severity",
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


class create_skill_development_plan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, focus_areas: list) -> str:
        plan = {
            "plan_id": f"SDP{int(datetime.now().timestamp() * 1000) % 10000}",
            "user_id": user_id,
            "focus_areas": focus_areas,
            "created_date": "2025-07-04",
            "status": "Active",
        }

        data.setdefault("skill_development_plans", []).append(plan)

        return json.dumps(
            {
                "success": f"Skill development plan created for user {user_id}",
                "plan": plan,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "create_skill_development_plan",
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


# All tools registry
TOOLS = [
    get_today_date(),
    search_users(),
    get_course(),
    enroll_in_course(),
    get_goal(),
    update_goal(),
    get_job_market_insights(),
    add_user_certification(),
    list_user_certifications(),
    list_user_courses(),
    add_user_education(),
    log_course_completion(),
    log_mentoring_session(),
    list_mentoring_sessions(),
    audit_goal_status(),
    log_course_progress(),
    recommend_learning_path(),
    conditional_progress_update(),
    get_team(),
    get_team_members(),
    log_team_training(),
    list_team_training(),
    update_user_training_progress(),
    get_mentor(),
    schedule_mentorship_session(),
    list_user_mentorships(),
    get_soft_skills(),
    update_course_progress(),
    log_soft_skill_gap(),
    list_soft_skill_gap(),
    analyze_skill_gap(),
    list_user_education(),
    search_talent_network(),
    log_job_application(),
    update_application(),
    schedule_interview(),
    list_applications(),
    list_job_postings(),
    reassign_mentor(),
    conditional_enroll_or_list(),
    get_user_course_progress(),
    generate_unique_cert_id(),
    generate_unique_edu_id(),
    generate_unique_application_id(),
    generate_unique_relationship_id(),
    generate_unique_analysis_id(),
    check_goal_progress_threshold(),
    calculate_progress_increment(),
    get_job_posting(),
    add_job_application(),
    list_user_applications(),
    search_job_postings(),
    get_skill_gap_analysis(),
    perform_soft_skill_gap_analysis(),
    compute_skill_gap_score(),
    assign_mentor(),
    list_user_mentors(),
    list_mentorship_relationships(),
    compute_mentor_load(),
    update_mentorship_note(),
    search_teams(),
    list_team_members(),
    check_course_completion_status(),
    mark_course_completed(),
    compute_average_progress(),
    notify_hr(),
    send_email_to_user(),
    get_team_training_log(),
    update_team_training_log(),
    list_user_training_sessions(),
    schedule_team_training(),
    add_team_training_session(),
    compute_team_training_hours(),
    compute_team_average_progress(),
    bulk_enroll_course(),
    bulk_update_goals(),
    compute_cert_expiry(),
    get_user_id_from_name(),
    bulk_check_team_courses(),
    bulk_enroll_team(),
    bulk_update_team_goals(),
    check_readiness_threshold(),
    check_team_average_threshold(),
    check_team_training_threshold(),
    get_user_goals_by_type(),
    get_course_by_name(),
    get_job_by_title(),
    get_all_goals(),
    generate_unique_goal_id(),
    add_user_goal(),
    check_user_training_completion(),
    assess_team_mentorship_coverage(),
    evaluate_team_training_status(),
    check_skill_gap_severity(),
    create_skill_development_plan(),
]
