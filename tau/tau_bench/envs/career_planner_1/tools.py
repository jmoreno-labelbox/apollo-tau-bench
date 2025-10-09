import json
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


class GetJobPosting(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], job_id: str = None) -> str:
        postings = data.get("job_postings", {}).values()
        for post in postings.values():
            if post.get("job_id") == job_id:
                return str(post)
        return f"Job posting with ID {job_id} not found."
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetJobPosting",
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
    def invoke(data: dict[str, Any], role: str = None) -> str:
        catalog = data.get("role_skill_catalog", {}).values()

        # Debug: Verify if the catalog is loaded
        if not catalog:
            payload = {"error": "Role catalog not loaded"}
            out = json.dumps(payload, indent=2)
            return out

        # Attempt an exact match initially
        for entry in catalog.values():
            if entry.get("role") == role:
                skills = entry.get("required_skills", [])
                if not skills:
                    payload = {"error": f"No skills found for role '{role}'"}
                    out = json.dumps(payload, indent=2)
                    return out

                # Make sure to return a list of strings instead of dictionaries
                skill_names = []
                for skill in skills:
                    if isinstance(skill, str):
                        skill_names.append(skill)
                    elif isinstance(skill, dict) and skill.get("skill"):
                        skill_names.append(skill.get("skill"))
                payload = skill_names
                out = json.dumps(payload, indent=2)
                return out

        # Attempt a partial match for typical role variations
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
            for entry in catalog.values():
                if entry.get("role") == mapped_role:
                    skills = entry.get("required_skills", [])
                    if not skills:
                        payload = {
                            "error": f"No skills found for mapped role '{mapped_role}'"
                        }
                        out = json.dumps(payload, indent=2)
                        return out

                    # Confirm that we return a list of strings rather than dictionaries
                    skill_names = []
                    for skill in skills:
                        if isinstance(skill, str):
                            skill_names.append(skill)
                        elif isinstance(skill, dict) and skill.get("skill"):
                            skill_names.append(skill.get("skill"))
                    payload = skill_names
                    out = json.dumps(payload, indent=2)
                    return out

        # Display available roles for debugging purposes
        available_roles = [entry.get("role") for entry in catalog.values()]
        payload = {"error": f"Role '{role}' not found", "available_roles": available_roles}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRoleSkills",
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
    def invoke(data: dict[str, Any], required_skills: list = None) -> str:
        required_skills_raw = required_skills if required_skills is not None else []

        # Carefully extract skill names from possibly mixed data
        required = set()
        for skill_item in required_skills_raw:
            if isinstance(skill_item, str):
                required.add(skill_item)
            elif isinstance(skill_item, dict) and skill_item.get("skill"):
                required.add(skill_item.get("skill"))

        talent_network = data.get("talent_network", {}).values()

        # Debug: Confirm if the talent network is loaded
        if not talent_network:
            payload = {"error": "Talent network not loaded", "matches": []}
            out = json.dumps(
                payload, indent=2
            )
            return out

        matches = []
        for c in talent_network.values():
            # Retrieve skill names from candidate skills - accommodate both formats
            candidate_skills = set()
            cand_skills = c.get("skills", [])

            if isinstance(cand_skills, list):
                for skill in cand_skills:
                    if isinstance(skill, str):
                        candidate_skills.add(skill)
                    elif isinstance(skill, dict) and skill.get("skill"):
                        candidate_skills.add(skill.get("skill"))

            # Verify matches - manage both direct matches and hierarchical skills
            has_match = False

            # Initially check for direct intersection
            if required.intersection(candidate_skills):
                has_match = True
            else:
                # Examine hierarchical matches by broadening required skills
                expanded_required = set()
                for req_skill in required:
                    expanded_required.add(req_skill)
                    # Locate this skill in the role catalog to obtain specific skills
                    for role_entry in data.get("role_skill_catalog", {}).values():
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
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchExternalCandidatesBySkills",
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
    def invoke(data: dict[str, Any], candidate_id: str = None, job_id: str = None, recruiter_id: str = None) -> str:
        # Assign a recruiter in a deterministic manner if not specified
        if not recruiter_id:
            if job_id in ["J001", "J002"]:
                recruiter_id = "U301"
            elif job_id in ["J003", "J004"]:
                recruiter_id = "U304"
            else:
                recruiter_id = "U312"

        # Generate a shortlist entry containing only necessary data
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
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ShortlistExternalCandidate",
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
    def invoke(data: dict[str, Any], job_id: str = None) -> str:
        apps = [
            app
            for app in data.get("job_applications", {}).values()
            if app.get("job_id") == job_id
        ]
        payload = apps
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetJobApplications",
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
    def invoke(data: dict[str, Any], applicant_id: str = None, role: str = None) -> str:
        # Retrieve user skills - manage the actual data structure
        user_skill_names = set()

        # Locate the user within the users data
        user = next((u for u in data.get("users", {}).values() if u.get("user_id") == applicant_id), {}).values()
        if user:
            # Examine the skills_current field (actual data structure)
            user_skills = user.get("skills_current", [])
            if isinstance(user_skills, list):
                for skill_obj in user_skills:
                    if isinstance(skill_obj, dict) and skill_obj.get("skill"):
                        user_skill_names.add(skill_obj.get("skill"))

            # Additionally verify if a legacy "skills" field exists
            if not user_skill_names:
                user_skills = user.get("skills", [])
                if isinstance(user_skills, list):
                    for skill in user_skills:
                        if isinstance(skill, str):
                            user_skill_names.add(skill)
                        elif isinstance(skill, dict) and skill.get("skill"):
                            user_skill_names.add(skill.get("skill"))

        # Attempt to use the user_skills table as a backup
        if not user_skill_names:
            user_skills_entry = next(
                (u for u in data.get("user_skills", {}).values() if u.get("user_id") == applicant_id), {}
            )
            if user_skills_entry:
                skills = user_skills_entry.get("skills", [])
                if isinstance(skills, list):
                    for skill in skills:
                        if isinstance(skill, str):
                            user_skill_names.add(skill)
                        elif isinstance(skill, dict) and skill.get("skill"):
                            user_skill_names.add(skill.get("skill"))

        # Debug: Verify if the user was located
        if not user_skill_names:
            return f"Error: No skills found for user {applicant_id}"

        # Retrieve role skills with mapping assistance
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
                for r in data.get("role_skill_catalog", {}).values()
                if r.get("role") == target_role
            ),
            {},
        )
        role_skills_raw = role_rec.get("required_skills", [])

        # Carefully extract skill names from possibly mixed data
        role_skill_names = set()
        for skill_item in role_skills_raw:
            if isinstance(skill_item, str):
                role_skill_names.add(skill_item)
            elif isinstance(skill_item, dict) and skill_item.get("skill"):
                role_skill_names.add(skill_item.get("skill"))

        # Identify matches - manage both direct matches and hierarchical skills
        matched = []
        missing = []

        # Examine each skill requirement for the role
        for role_skill in role_skill_names:
            # Verify for a direct match initially
            if role_skill in user_skill_names:
                matched.append(role_skill)
            else:
                # Determine if any user skill aligns with this role requirement
                skill_matched = False

                # Retrieve the specific skills for this role requirement from the catalog
                role_rec = next(
                    (
                        r
                        for r in data.get("role_skill_catalog", {}).values()
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
                        # Verify if the user possesses any of the specific skills in this category
                        for user_skill in user_skill_names:
                            if user_skill in specific_skills:
                                matched.append(role_skill)
                                skill_matched = True
                                break
                        if skill_matched:
                            break

                if not skill_matched:
                    missing.append(role_skill)

        # Structure the response
        match_count = len(matched)
        skill_percentage = (
            round((match_count / len(role_skill_names)) * 100)
            if role_skill_names
            else 0
        )

        return f"Skills match: {match_count}/{len(role_skill_names)} ({skill_percentage}%)\nMatched: {matched}\nMissing: {missing}"
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AnalyzeApplicantSkillFit",
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
    def invoke(data: dict[str, Any], application_id: str = None, new_status: str = None) -> str:
        for app in data.get("job_applications", {}).values():
            if app["application_id"] == application_id:
                app["status"] = new_status
                app["last_updated"] = datetime.now().isoformat()
                return f"{application_id} {new_status}"
        return "Application not found"
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateApplicationStatus",
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
    def invoke(data: dict[str, Any], application_id: str) -> str:
        # Generate an interview record containing only vital data
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
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ScheduleTechnicalInterview",
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
    def invoke(data: dict[str, Any], candidate_id: str = None, role: str = None) -> str:
        # Collect candidate skills - accommodate both formats
        cand = next(
            (
                c
                for c in data.get("talent_network", {}).values()
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

        # Debug: Confirm if the candidate was located
        if not cand_skill_names:
            return f"Error: No skills found for candidate {candidate_id}"

        # Collect role skills with mapping assistance
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
                for r in data.get("role_skill_catalog", {}).values()
                if r.get("role") == target_role
            ),
            {},
        )
        role_skills_raw = role_rec.get("required_skills", [])

        # Carefully extract skill names from possibly mixed data
        role_skill_names = set()
        for skill_item in role_skills_raw:
            if isinstance(skill_item, str):
                role_skill_names.add(skill_item)
            elif isinstance(skill_item, dict) and skill_item.get("skill"):
                role_skill_names.add(skill_item.get("skill"))

        # Calculate matches - manage both direct matches and hierarchical skills
        matched = []
        missing = []

        # Examine each skill requirement for the role
        for role_skill in role_skill_names:
            # Verify for a direct match initially
            if role_skill in cand_skill_names:
                matched.append(role_skill)
            else:
                # Determine if any candidate skill aligns with this role requirement
                skill_matched = False

                # Retrieve the specific skills for this role requirement from the catalog
                role_rec = next(
                    (
                        r
                        for r in data.get("role_skill_catalog", {}).values()
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
                        # Verify if the candidate possesses any of the specific skills in this category
                        for cand_skill in cand_skill_names:
                            if cand_skill in specific_skills:
                                matched.append(role_skill)
                                skill_matched = True
                                break
                        if skill_matched:
                            break

                if not skill_matched:
                    missing.append(role_skill)

        # structure the response
        match_count = len(matched)
        skill_percentage = (
            round((match_count / len(role_skill_names)) * 100)
            if role_skill_names
            else 0
        )

        return f"Skills match: {match_count}/{len(role_skill_names)} ({skill_percentage}%)\nMatched: {matched}\nMissing: {missing}"
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AnalyzeExternalCandidateSkillFit",
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
    def invoke(data: dict[str, Any], user_id: str = None, skill: str = None) -> str:
        # Confirm that the skill is pertinent to available roles
        valid_skills = set()
        for role_entry in data.get("role_skill_catalog", {}).values():
            skills = role_entry.get("required_skills", [])
            if isinstance(skills, list):
                for skill_item in skills:
                    if isinstance(skill_item, str):
                        valid_skills.add(skill_item)
                    elif isinstance(skill_item, dict) and skill_item.get("skill"):
                        valid_skills.add(skill_item.get("skill"))

        # If the skill is absent from the catalog, omit the recommendation
        if skill not in valid_skills:
            return f"Skill '{skill}' not found in catalog - no training recommendation made"

        # Generate a training recommendation containing only necessary data
        recommendation = {
            "user_id": user_id,
            "skill": skill,
            "timestamp": datetime.now().isoformat(),
        }
        table = data.setdefault("training_recommendations", {})
        key = f"{len(table)}"
        table[key] = recommendation
        return f"{user_id} needs {skill} training"
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecommendSkillTraining",
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
                "name": "GetUserIdFromName",
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
        # Locate a course whose name includes the provided string (case-insensitive)
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
                "name": "GetCourseIdByName",
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
                "name": "GetTodayDate",
                "description": "Get today's date",
                "parameters": {"type": "object", "properties": {}, "required": []},
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
                "name": "ListUserGoals",
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
        data: dict[str, Any],
        user_id: str,
        goal_id: str,
        last_updated_date: str,
        status: str = None,
        progress_percent: int = None,
        notes_to_append: str = None,
    ) -> str:
        goals_data = data.get("goals", {}).values()
        user_goals_obj = next(
            (g for g in goals_data.values() if g.get("user_id") == user_id), None
        )
        if not user_goals_obj:
            payload = {"error": f"User {user_id} not found in goals data"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        goal_to_update = next(
            (g for g in user_goals_obj.get("goals", []) if g.get("goal_id") == goal_id),
            None,
        )

        if not goal_to_update:
            payload = {"error": f"Goal {goal_id} not found for user {user_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Implement updates if supplied
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

        # Assign the last_updated date based on the supplied parameter
        goal_to_update["last_updated"] = last_updated_date
        payload = {"success": f"Goal {goal_id} updated for user {user_id}"}
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
                "name": "UpdateGoal",
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
                "name": "GetTeam",
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
        table = data.setdefault("user_course_progress", {})
        key = f"{len(table)}"
        table[key] = enrollment
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
                "name": "EnrollInCourse",
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
                "name": "ListUserCourses",
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

        #--- Logic for auto-generating relationship_id ---
        if not relationships:
            new_id_num = 1
        else:
            #Identify the highest existing ID number to prevent collisions
            max_id = 0
            for rel in relationships:
                try:
                    num = int(rel["relationship_id"][2:])  #Presumes the format MR###
                    if num > max_id:
                        max_id = num
                except (ValueError, IndexError):
                    continue  #Ignore incorrectly formatted IDs
            new_id_num = max_id + 1

        new_relationship_id = f"MR{new_id_num:03d}"  #Formats as MR001, MR015, and so on.

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
                "name": "AddMentorshipRelationship",
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

        #--- SIMPLIFIED LOGIC ---
        #The tool now solely executes a direct update.
        rel.update(updates)
        payload = {"success": f"relationship {relationship_id} updated"}
        out = json.dumps(payload)
        return out


        #--- SIMPLIFIED LOGIC ---
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
                "name": "UpdateMentorshipRelationship",
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
                "name": "ListUserMentorships",
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
                "name": "ScheduleMentorshipSession",
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
    def invoke(data: dict[str, Any], job_title: str) -> str:
        _job_titleL = job_title or ''.lower()
        pass
        postings = data.get("job_postings", {}).values()
        # Utilize a case-insensitive partial match for reliability
        posting = next(
            (p for p in postings.values() if job_title.lower() in p.get("title", "").lower()),
            None,
        )
        if posting:
            payload = {"job_id": posting["job_id"]}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Job posting with title containing '{job_title}' not found"}
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
                "name": "GetJobIdByTitle",
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
    def invoke(data: dict[str, Any], user_id: str, goal: dict[str, Any]) -> str:
        """Add a new goal to a user's record."""
        for entry in data.get("goals", {}).values():
            if entry["user_id"] == user_id:
                entry["goals"].append(goal)
                break
        else:  # no current goal list for this user
            data.setdefault("goals", []).append({"user_id": user_id, "goals": [goal]})
        payload = {"success": f"goal {goal['goal_id']} added for {user_id}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddGoal",
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
    def invoke(data: dict[str, Any], mentee_id: str, focus_areas: list[str]) -> str:
        pass
        mentors = data.get("user_mentorship", {}).values()

        # Adopt a wider definition of expertise, encompassing roles and general knowledge
        def get_mentor_expertise_set(mentor):
            pass
            expertise = set(mentor.get("expertise", []))
            roles = set(mentor.get("mentoring_roles", []))
            return expertise.union(roles)

        # Identify mentors whose expertise/roles intersect with the focus areas
        # and who are clearly suitable for the mentee.
        matches = []
        focus_set = set(focus_areas)
        for mentor in mentors.values():
            if mentor.get("availability") == "Full":
                continue

            # Verify compatibility
            if mentee_id not in mentor.get("compatible_user_ids", []):
                continue

            # Examine for overlap in expertise
            mentor_expertise = get_mentor_expertise_set(mentor)
            if focus_set.intersection(mentor_expertise):
                matches.append(
                    {
                        "mentor_id": mentor.get("mentor_id"),
                        "name": mentor.get("name"),
                        "expertise": list(mentor_expertise),
                    }
                )
        payload = {"mentors": matches}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindMentors",
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
    def invoke(data: dict[str, Any], user_id: str) -> str:
        """Fetch the complete profile for a specified user ID."""
        users = data.get("users", {}).values()
        user_profile = next((u for u in users.values() if u.get("user_id") == user_id), None)

        if user_profile:
            payload = user_profile
            out = json.dumps(payload, indent=2)
            return out
        else:
            payload = {"error": f"User with ID {user_id} not found."}
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetUserProfile",
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
