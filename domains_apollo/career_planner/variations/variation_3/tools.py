import json
from typing import Any

from domains.dto import Tool


class GetUserId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_name: str = None) -> str:
        users = data.get("users", [])

        for user in users:
            if user.get("name") == user_name:
                payload = {"user_id": user.get("user_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetUserId",
                "description": "Search for user by name",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_name": {
                            "type": "string",
                            "description": "The full name of the user.",
                        }
                    },
                    "required": ["user_name"],
                },
            },
        }


class GetUserGoals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        goals = data.get("goals", [])
        result = [g for g in goals if g["user_id"] == user_id]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserGoals",
                "description": "Retrieves the active career goals for a given user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class GetRoleRequirements(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_name: str = None) -> str:
        role_catalog = data.get("role_skill_catalog", [])
        result = [r for r in role_catalog if r["role"] == role_name]

        if not result:
            payload = {
                    "error": "Role not found",
                    "role_name": role_name,
                    "available_roles": [r["role"] for r in role_catalog],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = result[0]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getRoleRequirements",
                "description": "Retrieves the required skills and certifications for a given role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {
                            "type": "string",
                            "description": "The name of the target role.",
                        }
                    },
                    "required": ["role_name"],
                },
            },
        }


class GetUserSkillGap(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, target_role: str = None) -> str:
        gaps = data.get("skill_gap_analysis", [])
        result = [
            g
            for g in gaps
            if g["user_id"] == user_id and g["target_role"] == target_role
        ]

        if not result:
            payload = {
                    "error": "No skill gap found",
                    "user_id": user_id,
                    "target_role": target_role,
                    "available_analyses": [
                        f"{g['user_id']} -> {g['target_role']}" for g in gaps
                    ],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = result[0]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserSkillGap",
                "description": "Gets the skill gap for a user targeting a specific role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        },
                        "target_role": {
                            "type": "string",
                            "description": "The role the user wants to target.",
                        },
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }


class RecommendCourseForGap(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, target_role: str = None) -> str:
        gaps = data.get("skill_gap_analysis", [])
        user_gaps = [
            g
            for g in gaps
            if g["user_id"] == user_id and g["target_role"] == target_role
        ]

        if not user_gaps:
            payload = {"error": "No gap found."}
            out = json.dumps(payload, indent=2)
            return out

        # Identify the most critical skill gap along with the courses that are offered
        skill_gaps = user_gaps[0].get("skill_gaps", [])
        highest_priority_gap = None

        # Arrange by priority (High to Low) and severity of the gap (High to Low)
        priority_order = {"High": 3, "Medium": 2, "Low": 1}
        severity_order = {"High": 3, "Medium": 2, "Low": 1}

        for skill_gap in skill_gaps:
            if skill_gap.get("recommended_courses"):
                if not highest_priority_gap:
                    highest_priority_gap = skill_gap
                else:
                    # Evaluate based on priority initially, followed by severity
                    current_priority = priority_order.get(
                        skill_gap.get("priority", "Low"), 1
                    )
                    current_severity = severity_order.get(
                        skill_gap.get("gap_severity", "Low"), 1
                    )

                    best_priority = priority_order.get(
                        highest_priority_gap.get("priority", "Low"), 1
                    )
                    best_severity = severity_order.get(
                        highest_priority_gap.get("gap_severity", "Low"), 1
                    )

                    if current_priority > best_priority or (
                        current_priority == best_priority
                        and current_severity > best_severity
                    ):
                        highest_priority_gap = skill_gap

        if highest_priority_gap:
            payload = {
                "recommended_course": highest_priority_gap.get(
                    "recommended_courses"
                )[0],
                "skill": highest_priority_gap.get("skill_name"),
                "priority": highest_priority_gap.get("priority"),
                "gap_severity": highest_priority_gap.get("gap_severity"),
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"error": "No suitable course found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecommendCourseForGap",
                "description": "Recommends the highest priority course from the catalog to close a user's skill gap for a target role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        },
                        "target_role": {
                            "type": "string",
                            "description": "The role the user is targeting.",
                        },
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }


class GetTeamMembers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None) -> str:
        teams = data.get("teams", [])

        for t in teams:
            if t["team_id"] == team_id:
                payload = {"user_ids": t.get("team_members", [])}
                out = json.dumps(payload, indent=2)
                return out
        payload = {
                "error": "Team not found",
                "team_id": team_id,
                "available_teams": [t["team_id"] for t in teams],
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
                "name": "GetTeamMembers",
                "description": "Returns a list of user IDs belonging to a specific team.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {
                            "type": "string",
                            "description": "The team ID to search for.",
                        }
                    },
                    "required": ["team_id"],
                },
            },
        }


class GetUsersWithLeadershipGoals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_ids: list[int] = None) -> str:
        if user_ids is None:
            user_ids = []
        goals = data.get("goals", [])
        leadership_users = []

        for g in goals:
            if g["user_id"] in user_ids:
                for goal in g.get("goals", []):
                    goal_desc = goal.get("goal_description", "").lower()
                    goal_type = goal.get("goal_type", "").lower()
                    target_role = goal.get("target_role", "").lower()

                    # Look for signs of leadership
                    leadership_indicators = [
                        "leadership",
                        "lead",
                        "manager",
                        "director",
                        "senior",
                        "principal",
                        "staff",
                    ]
                    if (
                        any(
                            indicator in goal_desc
                            for indicator in leadership_indicators
                        )
                        or any(
                            indicator in goal_type
                            for indicator in leadership_indicators
                        )
                        or any(
                            indicator in target_role
                            for indicator in leadership_indicators
                        )
                    ):
                        if g["user_id"] not in leadership_users:
                            leadership_users.append(g["user_id"])
                        break
        payload = leadership_users
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUsersWithLeadershipGoals",
                "description": "Filters users by whether they have a leadership-oriented goal.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of user IDs to evaluate.",
                        }
                    },
                    "required": ["user_ids"],
                },
            },
        }


class AssessSoftSkillAlignment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, target_role: str = None) -> str:
        soft_skills = data.get("soft_skills", [])

        # Identify relevant soft skills for the desired position
        applicable_skills = []
        for s in soft_skills:
            if target_role in s.get("applicable_roles", []):
                applicable_skills.append(s["skill"])

        if applicable_skills:
            aligned = {
                "user_id": user_id,
                "role": target_role,
                "required_soft_skills": applicable_skills,
            }
            payload = aligned
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "No soft skills found for role."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssessSoftSkillAlignment",
                "description": "Gets soft skill expectations for a role and compares them to user development plans.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user being evaluated.",
                        },
                        "target_role": {
                            "type": "string",
                            "description": "The target role for soft skill comparison.",
                        },
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }


class ShortlistSuccessorCandidate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, target_role: str) -> str:
        # Create a consistent date derived from user_id and target_role
        import hashlib

        hash_input = f"{user_id}_{target_role}"
        hash_value = int(hashlib.md5(hash_input.encode()).hexdigest()[:8], 16)
        days_offset = hash_value % 30  # A range of 0 to 29 days from the reference date

        # Employ a constant base date to ensure consistent outcomes
        base_date = "2025-06-01"
        from datetime import datetime, timedelta

        base_dt = datetime.strptime(base_date, "%Y-%m-%d")
        shortlist_date = (base_dt + timedelta(days=days_offset)).strftime("%Y-%m-%d")

        entry = {
            "user_id": user_id,
            "target_role": target_role,
            "status": "shortlisted",
            "shortlist_date": shortlist_date,
        }
        data.setdefault("hr_workflows", []).append(entry)
        payload = {"message": "Candidate shortlisted.", "record": entry}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ShortlistSuccessorCandidate",
                "description": "Marks a user as a shortlisted candidate for succession into a target role with deterministic date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user being shortlisted.",
                        },
                        "target_role": {
                            "type": "string",
                            "description": "The target role under consideration.",
                        },
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }


class GetUserTargetRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        goals_data = data.get("goals", [])

        user_goals = [g for g in goals_data if g.get("user_id") == user_id]

        if not user_goals:
            payload = {"error": f"No goals found for user {user_id}."}
            out = json.dumps(payload)
            return out

        # Locate the initial goal categorized as "Role Transition"
        for goal in user_goals[0].get("goals", []):
            if goal.get("goal_type") == "Role Transition" and "target_role" in goal:
                payload = {"target_role": goal.get("target_role")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"No 'Role Transition' goal found for user {user_id}."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserTargetRole",
                "description": "Retrieves the formal target role from a user's 'Role Transition' career goal.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class AssignCourseToUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, course_id: str) -> str:
        # Create a consistent date based on user_id and course_id
        import hashlib

        hash_input = f"{user_id}_{course_id}"
        hash_value = int(hashlib.md5(hash_input.encode()).hexdigest()[:8], 16)
        days_offset = hash_value % 30  # A span of 0 to 29 days from the reference date

        # Utilize a stable base date for reliable results
        base_date = "2025-07-01"
        from datetime import datetime, timedelta

        base_dt = datetime.strptime(base_date, "%Y-%m-%d")
        assigned_date = (base_dt + timedelta(days=days_offset)).strftime("%Y-%m-%d")

        progress_entry = {
            "user_id": user_id,
            "course_id": course_id,
            "status": "assigned",
            "assigned_date": assigned_date,
        }

        data.setdefault("user_course_progress", []).append(progress_entry)
        payload = {"message": "Course assigned to user.", "entry": progress_entry}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignCourseToUser",
                "description": "Assigns a course to a user and logs it in course progress with deterministic date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user receiving the course assignment.",
                        },
                        "course_id": {
                            "type": "string",
                            "description": "The ID of the course to assign.",
                        },
                    },
                    "required": ["user_id", "course_id"],
                },
            },
        }


class ValidateUserGoalAlignment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, target_role: str = None) -> str:
        goals = data.get("goals", [])
        user_goals = [g for g in goals if g["user_id"] == user_id]

        if not user_goals:
            payload = {"valid": False, "reason": "No goals found for user"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        for goal_group in user_goals:
            for goal in goal_group.get("goals", []):
                goal_desc = goal.get("goal_description", "").lower()
                goal_target_role = goal.get("target_role", "").lower()

                if (
                    target_role.lower() in goal_desc
                    or target_role.lower() in goal_target_role
                    or goal_target_role == target_role.lower()
                ):
                    payload = {"valid": True, "goal_id": goal.get("goal_id")}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
        payload = {"valid": False, "reason": "No goals found for target role"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateUserGoalAlignment",
                "description": "Validates that a user has goals aligned with a target role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user to validate.",
                        },
                        "target_role": {
                            "type": "string",
                            "description": "The target role to check alignment with.",
                        },
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }


class CheckTrainingNeeded(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, target_role: str = None) -> str:
        gaps = data.get("skill_gap_analysis", [])
        user_gaps = [
            g
            for g in gaps
            if g["user_id"] == user_id and g["target_role"] == target_role
        ]

        if not user_gaps:
            payload = {"training_needed": False, "reason": "No skill gap analysis found"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        gap = user_gaps[0]
        readiness_score = gap.get("overall_readiness_score", 0)

        if readiness_score < 70:
            payload = {
                    "training_needed": True,
                    "readiness_score": readiness_score,
                    "reason": f"Readiness score {readiness_score} is below threshold of 70",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {
                "training_needed": False,
                "readiness_score": readiness_score,
                "reason": f"Readiness score {readiness_score} meets threshold",
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
                "name": "CheckTrainingNeeded",
                "description": "Checks if training is needed for a user targeting a specific role based on readiness score.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user to check.",
                        },
                        "target_role": {
                            "type": "string",
                            "description": "The target role to evaluate.",
                        },
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }


class ValidateTeamMembership(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, team_id: str = None) -> str:
        teams = data.get("teams", [])

        for team in teams:
            if team["team_id"] == team_id:
                members = team.get("team_members", [])
                if user_id in members:
                    payload = {"valid": True, "team_name": team.get("team_name")}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                else:
                    payload = {"valid": False, "reason": "User not in team"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
        payload = {"valid": False, "reason": "Team not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateTeamMembership",
                "description": "Validates that a user is a member of a specific team.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user to validate.",
                        },
                        "team_id": {
                            "type": "string",
                            "description": "The team to check membership in.",
                        },
                    },
                    "required": ["user_id", "team_id"],
                },
            },
        }


class ValidateCourseSkillMapping(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], course_id: str = None, skill_name: str = None) -> str:
        courses = data.get("course_catalog", [])

        course = None
        for c in courses:
            if c["course_id"] == course_id:
                course = c
                break

        if not course:
            payload = {"valid": False, "error": "Course not found", "course_id": course_id}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Verify whether the course includes the skill
        skills_covered = []
        for skill_imparted in course.get("skills_imparted", []):
            skills_covered.append(skill_imparted.get("skill", ""))

        if skill_name in skills_covered:
            payload = {
                    "valid": True,
                    "course_id": course_id,
                    "skill_name": skill_name,
                    "course_name": course.get("name", ""),
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {
                "valid": False,
                "error": "Skill not covered by course",
                "course_id": course_id,
                "skill_name": skill_name,
                "skills_covered": skills_covered,
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
                "name": "ValidateCourseSkillMapping",
                "description": "Validates that a course covers a specific skill.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "course_id": {
                            "type": "string",
                            "description": "The ID of the course to validate.",
                        },
                        "skill_name": {
                            "type": "string",
                            "description": "The skill to check coverage for.",
                        },
                    },
                    "required": ["course_id", "skill_name"],
                },
            },
        }


class GetUserPreferences(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        preferences = data.get("user_preferences", [])

        for pref in preferences:
            if pref.get("user_id") == user_id:
                payload = pref
                out = json.dumps(payload, indent=2)
                return out
        payload = {
                "error": "User preferences not found",
                "user_id": user_id,
                "available_users_with_prefs": [p.get("user_id") for p in preferences],
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
                "name": "getUserPreferences",
                "description": "Retrieves the career and learning preferences for a given user, such as preferred industries, work style, and learning formats.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class GetUserCourseProgress(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        progress_data = data.get("user_course_progress", [])

        user_progress = [p for p in progress_data if p.get("user_id") == user_id]
        payload = user_progress
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUserCourseProgress",
                "description": "Retrieves the course progress for a given user, including completed, in-progress, and assigned courses.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class LogTeamTraining(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, course_id: str, skill_name: str) -> str:
        # Create a consistent date derived from user_id and course_id

        # Develop a straightforward hash-based method for date generation to ensure uniformity
        import hashlib

        hash_input = f"{user_id}_{course_id}"
        hash_value = int(hashlib.md5(hash_input.encode()).hexdigest()[:8], 16)
        days_offset = hash_value % 30  # A duration of 0 to 29 days from the reference date

        # Adopt a constant base date for predictable outcomes
        base_date = "2025-07-01"
        from datetime import datetime, timedelta

        base_dt = datetime.strptime(base_date, "%Y-%m-%d")
        log_date = (base_dt + timedelta(days=days_offset)).strftime("%Y-%m-%d")

        entry = {
            "user_id": user_id,
            "skill_name": skill_name,
            "course_id": course_id,
            "log_date": log_date,
        }
        # This line locates the 'team_training_log' array in the data and appends the new entry.
        # If the array is absent, it initializes it first.
        data.setdefault("team_training_log", []).append(entry)
        payload = {"message": "Training logged.", "entry": entry}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogTeamTraining",
                "description": "Logs a course training entry for a user for a specific skill with deterministic date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the employee.",
                        },
                        "skill_name": {
                            "type": "string",
                            "description": "The skill being trained.",
                        },
                        "course_id": {
                            "type": "string",
                            "description": "The ID of the course used.",
                        },
                    },
                    "required": ["user_id", "skill_name", "course_id"],
                },
            },
        }


class GetUserProfile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        users = data.get("users", [])

        for user in users:
            if user.get("user_id") == user_id:
                profile_data = {
                    "user_id": user.get("user_id"),
                    "name": user.get("name"),
                    "current_role": user.get("current_role"),
                    "department": user.get("department"),
                    "team_id": user.get("team_id"),
                }
                payload = profile_data
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"User profile not found for {user_id}."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserProfile",
                "description": "Retrieves key profile information for a user, such as their current role and department.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


TOOLS = [
    GetUserId(),
    GetUserGoals(),
    GetRoleRequirements(),
    GetUserSkillGap(),
    RecommendCourseForGap(),
    GetTeamMembers(),
    GetUsersWithLeadershipGoals(),
    AssessSoftSkillAlignment(),
    ShortlistSuccessorCandidate(),
    AssignCourseToUser(),
    ValidateUserGoalAlignment(),
    CheckTrainingNeeded(),
    ValidateTeamMembership(),
    ValidateCourseSkillMapping(),
    GetUserPreferences(),
    GetUserCourseProgress(),
    LogTeamTraining(),
    GetUserTargetRole(),
    GetUserProfile(),
]
