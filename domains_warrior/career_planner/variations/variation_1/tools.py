import json
from datetime import datetime
from typing import Any, Dict, List
from domains.dto import Tool


class GetJobPosting(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        job_id = kwargs.get("job_id")
        postings = data.get("job_postings", [])
        for post in postings:
            if post.get("job_id") == job_id:
                return str(post)
        return f"Job posting with ID {job_id} not found."

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_job_posting",
                "description": "Retrieve details of a specific job posting by job ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {
                            "type": "string",
                            "description": "The job ID to retrieve.",
                        }
                    },
                    "required": ["job_id"],
                },
            },
        }


class GetRoleSkills(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role = kwargs.get("role")
        catalog = data.get("role_skill_catalog", [])

        # Debug: Check if catalog is loaded
        if not catalog:
            return json.dumps({"error": "Role catalog not loaded"}, indent=2)

        # Try exact match first
        for entry in catalog:
            if entry.get("role") == role:
                skills = entry.get("required_skills", [])
                if not skills:
                    return json.dumps(
                        {"error": f"No skills found for role '{role}'"}, indent=2
                    )

                # Ensure we return a list of strings, not dictionaries
                skill_names = []
                for skill in skills:
                    if isinstance(skill, str):
                        skill_names.append(skill)
                    elif isinstance(skill, dict) and skill.get("skill"):
                        skill_names.append(skill.get("skill"))

                return json.dumps(skill_names, indent=2)

                # Try partial match for common role variations
        role_mapping = {
            "AI Researcher": "Senior Data Scientist",
            "Security Analyst": "Cloud Security Specialist",
            "Marketing Specialist": "Product Marketing Specialist",
            "Senior Data Scientist": "Senior Data Scientist",
            "UX Design Lead": "UX Designer",
            "Cloud Security Compliance Specialist": "Cloud Security Specialist",
            "Product Marketing Specialist": "Product Marketing Specialist",
            "DevOps Engineer": "DevOps Engineer",
            "Data Scientist": "Data Scientist",
            "Data Analyst": "Senior Data Scientist",
        }

        mapped_role = role_mapping.get(role)
        if mapped_role:
            for entry in catalog:
                if entry.get("role") == mapped_role:
                    skills = entry.get("required_skills", [])
                    if not skills:
                        return json.dumps(
                            {
                                "error": f"No skills found for mapped role '{mapped_role}'"
                            },
                            indent=2,
                        )

                    # Ensure we return a list of strings, not dictionaries
                    skill_names = []
                    for skill in skills:
                        if isinstance(skill, str):
                            skill_names.append(skill)
                        elif isinstance(skill, dict) and skill.get("skill"):
                            skill_names.append(skill.get("skill"))

                    return json.dumps(skill_names, indent=2)

        # List available roles for debugging
        available_roles = [entry.get("role") for entry in catalog]
        return json.dumps(
            {"error": f"Role '{role}' not found", "available_roles": available_roles},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_skills",
                "description": "Get required skills for a specific role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role": {
                            "type": "string",
                            "description": "Role title to lookup skills for.",
                        }
                    },
                    "required": ["role"],
                },
            },
        }


class SearchExternalCandidatesBySkills(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required_skills_raw = kwargs.get("required_skills", [])

        # Safely extract skill names from potentially mixed data
        required = set()
        for skill_item in required_skills_raw:
            if isinstance(skill_item, str):
                required.add(skill_item)
            elif isinstance(skill_item, dict) and skill_item.get("skill"):
                required.add(skill_item.get("skill"))

        talent_network = data.get("talent_network", [])

        # Debug: Check if talent network is loaded
        if not talent_network:
            return json.dumps(
                {"error": "Talent network not loaded", "matches": []}, indent=2
            )

        matches = []
        for c in talent_network:
            # Extract skill names from candidate skills - handle both formats
            candidate_skills = set()
            cand_skills = c.get("skills", [])

            if isinstance(cand_skills, list):
                for skill in cand_skills:
                    if isinstance(skill, str):
                        candidate_skills.add(skill)
                    elif isinstance(skill, dict) and skill.get("skill"):
                        candidate_skills.add(skill.get("skill"))

            # Check for matches - handle both direct matches and hierarchical skills
            has_match = False

            # First check direct intersection
            if required.intersection(candidate_skills):
                has_match = True
            else:
                # Check hierarchical matches by expanding required skills
                expanded_required = set()
                for req_skill in required:
                    expanded_required.add(req_skill)
                    # Find this skill in the role catalog to get specific skills
                    for role_entry in data.get("role_skill_catalog", []):
                        for skill_category in role_entry.get("required_skills", []):
                            if (
                                isinstance(skill_category, dict)
                                and skill_category.get("skill") == req_skill
                            ):
                                specific_skills = skill_category.get(
                                    "specific_skills", []
                                )
                                expanded_required.update(specific_skills)

                if expanded_required.intersection(candidate_skills):
                    has_match = True

            if has_match:
                matches.append(c)

        # Return just the matches for compatibility
        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_external_candidates_by_skills",
                "description": "Search talent network candidates by skill match.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "required_skills": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of skills required for the role",
                        }
                    },
                    "required": ["required_skills"],
                },
            },
        }


class ShortlistExternalCandidate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        job_id = kwargs.get("job_id")
        recruiter_id = kwargs.get("recruiter_id")

        # Assign recruiter deterministically if not provided
        if not recruiter_id:
            if job_id in ["J001", "J002"]:
                recruiter_id = "U301"
            elif job_id in ["J003", "J004"]:
                recruiter_id = "U304"
            else:
                recruiter_id = "U312"

        # Create shortlist entry with only essential data
        entry = {
            "candidate_id": candidate_id,
            "recruiter_id": recruiter_id,
            "job_id": job_id,
            "timestamp": datetime.now().isoformat(),
        }

        if "shortlisted_candidates" not in data:
            data["shortlisted_candidates"] = []
        data["shortlisted_candidates"].append(entry)
        return f"External candidate {candidate_id} shortlisted for job {job_id}."

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "shortlist_external_candidate",
                "description": "Add external candidate to shortlist for a given job. Recruiter is assigned deterministically based on job_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {
                            "type": "string",
                            "description": "ID of the external candidate",
                        },
                        "job_id": {
                            "type": "string",
                            "description": "ID of the job posting",
                        },
                    },
                    "required": ["candidate_id", "job_id"],
                },
            },
        }


class GetJobApplications(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        job_id = kwargs.get("job_id")
        apps = [
            app
            for app in data.get("job_applications", [])
            if app.get("job_id") == job_id
        ]
        return json.dumps(apps, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_job_applications",
                "description": "Returns all applications for a given job ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {
                            "type": "string",
                            "description": "Job ID to fetch applications for",
                        }
                    },
                    "required": ["job_id"],
                },
            },
        }


class AnalyzeApplicantSkillFit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("applicant_id")
        role = kwargs.get("role")

        # Get user skills - handle actual data structure
        user_skill_names = set()

        # Find the user in the users data
        user = next((u for u in data.get("users", []) if u.get("user_id") == uid), {})
        if user:
            # Check skills_current field (actual data structure)
            user_skills = user.get("skills_current", [])
            if isinstance(user_skills, list):
                for skill_obj in user_skills:
                    if isinstance(skill_obj, dict) and skill_obj.get("skill"):
                        user_skill_names.add(skill_obj.get("skill"))

            # Also check if there's a legacy "skills" field
            if not user_skill_names:
                user_skills = user.get("skills", [])
                if isinstance(user_skills, list):
                    for skill in user_skills:
                        if isinstance(skill, str):
                            user_skill_names.add(skill)
                        elif isinstance(skill, dict) and skill.get("skill"):
                            user_skill_names.add(skill.get("skill"))

        # Try user_skills table as fallback
        if not user_skill_names:
            user_skills_entry = next(
                (u for u in data.get("user_skills", []) if u.get("user_id") == uid), {}
            )
            if user_skills_entry:
                skills = user_skills_entry.get("skills", [])
                if isinstance(skills, list):
                    for skill in skills:
                        if isinstance(skill, str):
                            user_skill_names.add(skill)
                        elif isinstance(skill, dict) and skill.get("skill"):
                            user_skill_names.add(skill.get("skill"))

        # Debug: Check if user was found
        if not user_skill_names:
            return f"Error: No skills found for user {uid}"

        # Get role skills with mapping support
        role_mapping = {
            "AI Researcher": "Senior Data Scientist",
            "Security Analyst": "Cloud Security Specialist",
            "Marketing Specialist": "Product Marketing Specialist",
            "Senior Data Scientist": "Senior Data Scientist",
            "UX Design Lead": "UX Designer",
            "Cloud Security Compliance Specialist": "Cloud Security Specialist",
            "Product Marketing Specialist": "Product Marketing Specialist",
            "DevOps Engineer": "DevOps Engineer",
            "Data Scientist": "Data Scientist",
            "Data Analyst": "Senior Data Scientist",
        }

        target_role = role_mapping.get(role, role)
        role_rec = next(
            (
                r
                for r in data.get("role_skill_catalog", [])
                if r.get("role") == target_role
            ),
            {},
        )
        role_skills_raw = role_rec.get("required_skills", [])

        # Safely extract skill names from potentially mixed data
        role_skill_names = set()
        for skill_item in role_skills_raw:
            if isinstance(skill_item, str):
                role_skill_names.add(skill_item)
            elif isinstance(skill_item, dict) and skill_item.get("skill"):
                role_skill_names.add(skill_item.get("skill"))

        # Find matches - handle both direct matches and hierarchical skills
        matched = []
        missing = []

        # Check each role skill requirement
        for role_skill in role_skill_names:
            # Check for direct match first
            if role_skill in user_skill_names:
                matched.append(role_skill)
            else:
                # Check if any user skill matches this role requirement
                skill_matched = False

                # Get the specific skills for this role requirement from catalog
                role_rec = next(
                    (
                        r
                        for r in data.get("role_skill_catalog", [])
                        if r.get("role") == target_role
                    ),
                    {},
                )
                for skill_category in role_rec.get("required_skills", []):
                    if (
                        isinstance(skill_category, dict)
                        and skill_category.get("skill") == role_skill
                    ):
                        specific_skills = skill_category.get("specific_skills", [])
                        # Check if user has any of the specific skills in this category
                        for user_skill in user_skill_names:
                            if user_skill in specific_skills:
                                matched.append(role_skill)
                                skill_matched = True
                                break
                        if skill_matched:
                            break

                if not skill_matched:
                    missing.append(role_skill)

        # Format response
        match_count = len(matched)
        skill_percentage = (
            round((match_count / len(role_skill_names)) * 100)
            if role_skill_names
            else 0
        )

        return f"Skills match: {match_count}/{len(role_skill_names)} ({skill_percentage}%)\nMatched: {matched}\nMissing: {missing}"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyze_applicant_skill_fit",
                "description": "Analyze how well an internal applicant's skills match a target role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "applicant_id": {
                            "type": "string",
                            "description": "User ID of applicant",
                        },
                        "role": {"type": "string", "description": "Target role title"},
                    },
                    "required": ["applicant_id", "role"],
                },
            },
        }


class UpdateApplicationStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        app_id = kwargs.get("application_id")
        new_status = kwargs.get("new_status")
        for app in data.get("job_applications", []):
            if app["application_id"] == app_id:
                app["status"] = new_status
                app["last_updated"] = datetime.now().isoformat()
                return f"{app_id} {new_status}"
        return "Application not found"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_application_status",
                "description": "Updates the status of a job application.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "application_id": {
                            "type": "string",
                            "description": "Application to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status label",
                        },
                    },
                    "required": ["application_id", "new_status"],
                },
            },
        }


class ScheduleTechnicalInterview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        application_id = kwargs.get("application_id")

        # Create interview record with only essential data
        interview = {
            "application_id": application_id,
            "status": "scheduled",
            "created_at": datetime.now().isoformat(),
        }

        if "technical_interviews" not in data:
            data["technical_interviews"] = []
        data["technical_interviews"].append(interview)
        return f"Technical interview scheduled for application {application_id}."

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_technical_interview",
                "description": "Schedules a technical interview for a job application.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "application_id": {
                            "type": "string",
                            "description": "ID of the job application",
                        }
                    },
                    "required": ["application_id"],
                },
            },
        }


class AnalyzeExternalCandidateSkillFit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        role = kwargs.get("role")

        # gather candidate skills - handle both formats
        cand = next(
            (
                c
                for c in data.get("talent_network", [])
                if c.get("candidate_id") == candidate_id
            ),
            {},
        )
        cand_skill_names = set()

        if cand:
            cand_skills = cand.get("skills", [])
            if isinstance(cand_skills, list):
                for skill in cand_skills:
                    if isinstance(skill, str):
                        cand_skill_names.add(skill)
                    elif isinstance(skill, dict) and skill.get("skill"):
                        cand_skill_names.add(skill.get("skill"))

        # Debug: Check if candidate was found
        if not cand_skill_names:
            return f"Error: No skills found for candidate {candidate_id}"

        # gather role skills with mapping support
        role_mapping = {
            "AI Researcher": "Senior Data Scientist",
            "Security Analyst": "Cloud Security Specialist",
            "Marketing Specialist": "Product Marketing Specialist",
            "Senior Data Scientist": "Senior Data Scientist",
            "UX Design Lead": "UX Designer",
            "Cloud Security Compliance Specialist": "Cloud Security Specialist",
            "Product Marketing Specialist": "Product Marketing Specialist",
            "DevOps Engineer": "DevOps Engineer",
            "Data Scientist": "Data Scientist",
            "Data Analyst": "Senior Data Scientist",
        }

        target_role = role_mapping.get(role, role)
        role_rec = next(
            (
                r
                for r in data.get("role_skill_catalog", [])
                if r.get("role") == target_role
            ),
            {},
        )
        role_skills_raw = role_rec.get("required_skills", [])

        # Safely extract skill names from potentially mixed data
        role_skill_names = set()
        for skill_item in role_skills_raw:
            if isinstance(skill_item, str):
                role_skill_names.add(skill_item)
            elif isinstance(skill_item, dict) and skill_item.get("skill"):
                role_skill_names.add(skill_item.get("skill"))

        # compute matches - handle both direct matches and hierarchical skills
        matched = []
        missing = []

        # Check each role skill requirement
        for role_skill in role_skill_names:
            # Check for direct match first
            if role_skill in cand_skill_names:
                matched.append(role_skill)
            else:
                # Check if any candidate skill matches this role requirement
                skill_matched = False

                # Get the specific skills for this role requirement from catalog
                role_rec = next(
                    (
                        r
                        for r in data.get("role_skill_catalog", [])
                        if r.get("role") == target_role
                    ),
                    {},
                )
                for skill_category in role_rec.get("required_skills", []):
                    if (
                        isinstance(skill_category, dict)
                        and skill_category.get("skill") == role_skill
                    ):
                        specific_skills = skill_category.get("specific_skills", [])
                        # Check if candidate has any of the specific skills in this category
                        for cand_skill in cand_skill_names:
                            if cand_skill in specific_skills:
                                matched.append(role_skill)
                                skill_matched = True
                                break
                        if skill_matched:
                            break

                if not skill_matched:
                    missing.append(role_skill)

        # format response
        match_count = len(matched)
        skill_percentage = (
            round((match_count / len(role_skill_names)) * 100)
            if role_skill_names
            else 0
        )

        return f"Skills match: {match_count}/{len(role_skill_names)} ({skill_percentage}%)\nMatched: {matched}\nMissing: {missing}"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyze_external_candidate_skill_fit",
                "description": "Compare external candidate skills to target role requirements.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {
                            "type": "string",
                            "description": "ID of candidate in talent_network.json",
                        },
                        "role": {
                            "type": "string",
                            "description": "Target role title (must exist in role_skill_catalog.json)",
                        },
                    },
                    "required": ["candidate_id", "role"],
                },
            },
        }


class RecommendSkillTraining(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        skill = kwargs.get("skill")

        # Validate that the skill is relevant for available roles
        valid_skills = set()
        for role_entry in data.get("role_skill_catalog", []):
            skills = role_entry.get("required_skills", [])
            if isinstance(skills, list):
                for skill_item in skills:
                    if isinstance(skill_item, str):
                        valid_skills.add(skill_item)
                    elif isinstance(skill_item, dict) and skill_item.get("skill"):
                        valid_skills.add(skill_item.get("skill"))

        # If skill not in catalog, skip recommendation
        if skill not in valid_skills:
            return f"Skill '{skill}' not found in catalog - no training recommendation made"

        # Create training recommendation with only essential data
        recommendation = {
            "user_id": user_id,
            "skill": skill,
            "timestamp": datetime.now().isoformat(),
        }
        data.setdefault("training_recommendations", []).append(recommendation)
        return f"{user_id} needs {skill} training"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "recommend_skill_training",
                "description": "Adds a training recommendation for a user on a specific skill.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User receiving recommendation",
                        },
                        "skill": {"type": "string", "description": "Skill to develop"},
                    },
                    "required": ["user_id", "skill"],
                },
            },
        }


class GetUserIdFromName(Tool):
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


class GetCourseIdByName(Tool):
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


class GetTodayDate(Tool):
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


class ListUserGoals(Tool):
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


class UpdateGoal(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_id: str,
        goal_id: str,
        last_updated_date: str,
        status: str = None,
        progress_percent: int = None,
        notes_to_append: str = None,
    ) -> str:
        goals_data = data.get("goals", [])
        user_goals_obj = next(
            (g for g in goals_data if g.get("user_id") == user_id), None
        )
        if not user_goals_obj:
            return json.dumps(
                {"error": f"User {user_id} not found in goals data"}, indent=2
            )

        goal_to_update = next(
            (g for g in user_goals_obj.get("goals", []) if g.get("goal_id") == goal_id),
            None,
        )

        if not goal_to_update:
            return json.dumps(
                {"error": f"Goal {goal_id} not found for user {user_id}"}, indent=2
            )

        # Apply updates if provided
        if status is not None:
            goal_to_update["status"] = status
        if progress_percent is not None:
            goal_to_update["progress_percent"] = progress_percent
        if notes_to_append:
            existing_notes = goal_to_update.get("notes", "")
            if existing_notes:
                goal_to_update["notes"] = f"{existing_notes} {notes_to_append}".strip()
            else:
                goal_to_update["notes"] = notes_to_append.strip()

        # Set the last_updated date from the provided parameter
        goal_to_update["last_updated"] = last_updated_date

        return json.dumps(
            {"success": f"Goal {goal_id} updated for user {user_id}"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "update_goal",
                "description": "Update specific fields of a user's goal. The last_updated date must be provided.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user whose goal is to be updated.",
                        },
                        "goal_id": {
                            "type": "string",
                            "description": "The ID of the goal to update.",
                        },
                        "last_updated_date": {
                            "type": "string",
                            "description": "The date of the update in YYYY-MM-DD format. Typically sourced from the get_today_date tool.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status for the goal (e.g., 'Active', 'Completed').",
                        },
                        "progress_percent": {
                            "type": "integer",
                            "description": "The new progress percentage (0-100).",
                        },
                        "notes_to_append": {
                            "type": "string",
                            "description": "A string of text to append to the existing notes.",
                        },
                    },
                    "required": ["user_id", "goal_id", "last_updated_date"],
                },
            },
        }


class GetTeam(Tool):
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


class AddTeamMember(Tool):
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


class EnrollInCourse(Tool):
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


class ListUserCourses(Tool):
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


class UpdateUserCourseProgress(Tool):
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


class AddMentorshipRelationship(Tool):
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


class UpdateMentorshipRelationship(Tool):
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


class ListUserMentorships(Tool):
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


class ScheduleMentorshipSession(Tool):
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


class GetJobIdByTitle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], job_title: str) -> str:
        postings = data.get("job_postings", [])
        # Use a case-insensitive partial match for robustness
        posting = next(
            (p for p in postings if job_title.lower() in p.get("title", "").lower()),
            None,
        )
        if posting:
            return json.dumps({"job_id": posting["job_id"]}, indent=2)
        return json.dumps(
            {"error": f"Job posting with title containing '{job_title}' not found"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_job_id_by_title",
                "description": "Find a job ID by its title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_title": {
                            "type": "string",
                            "description": "The title of the job to find.",
                        }
                    },
                    "required": ["job_title"],
                },
            },
        }


class AddGoal(Tool):
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


class FindMentors(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], mentee_id: str, focus_areas: List[str]) -> str:
        mentors = data.get("user_mentorship", [])

        # Use a broader definition of expertise, including roles and general expertise
        def get_mentor_expertise_set(mentor):
            expertise = set(mentor.get("expertise", []))
            roles = set(mentor.get("mentoring_roles", []))
            return expertise.union(roles)

        # Find mentors whose expertise/roles overlap with the focus areas
        # and who are explicitly compatible with the mentee.
        matches = []
        focus_set = set(focus_areas)
        for mentor in mentors:
            if mentor.get("availability") == "Full":
                continue

            # Check for compatibility
            if mentee_id not in mentor.get("compatible_user_ids", []):
                continue

            # Check for expertise overlap
            mentor_expertise = get_mentor_expertise_set(mentor)
            if focus_set.intersection(mentor_expertise):
                matches.append(
                    {
                        "mentor_id": mentor.get("mentor_id"),
                        "name": mentor.get("name"),
                        "expertise": list(mentor_expertise),
                    }
                )

        return json.dumps({"mentors": matches}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "find_mentors",
                "description": "Finds suitable and available mentors for a mentee based on required focus areas and compatibility.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mentee_id": {
                            "type": "string",
                            "description": "The user ID of the mentee seeking mentorship.",
                        },
                        "focus_areas": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of skills or topics the mentorship should focus on.",
                        },
                    },
                    "required": ["mentee_id", "focus_areas"],
                },
            },
        }


class GetUserProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        """Retrieve the full profile for a given user ID."""
        users = data.get("users", [])
        user_profile = next((u for u in users if u.get("user_id") == user_id), None)

        if user_profile:
            return json.dumps(user_profile, indent=2)
        else:
            return json.dumps({"error": f"User with ID {user_id} not found."}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_user_profile",
                "description": "Retrieve the full profile of a user by their user ID, including their team ID, role, and manager.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID to retrieve the profile for.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


TOOLS = [
    GetJobPosting(),
    GetRoleSkills(),
    SearchExternalCandidatesBySkills(),
    ShortlistExternalCandidate(),
    GetJobApplications(),
    AnalyzeApplicantSkillFit(),
    UpdateApplicationStatus(),
    ScheduleTechnicalInterview(),
    AnalyzeExternalCandidateSkillFit(),
    RecommendSkillTraining(),
    GetUserIdFromName(),
    GetCourseIdByName(),
    GetTodayDate(),
    ListUserGoals(),
    UpdateGoal(),
    AddTeamMember(),
    GetTeam(),
    ListUserCourses(),
    EnrollInCourse(),
    UpdateUserCourseProgress(),
    AddMentorshipRelationship(),
    UpdateMentorshipRelationship(),
    ListUserMentorships(),
    ScheduleMentorshipSession(),
    GetJobIdByTitle(),
    AddGoal(),
    FindMentors(),
    GetUserProfile(),
]
