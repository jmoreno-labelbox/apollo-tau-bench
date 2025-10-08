import json
from datetime import datetime
from typing import Any

from domains.dto import Tool


#Tools that are read-only
class GetUserProfile(Tool):
    """Retrieve an employee's profile using their ID."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        uid = user_id
        for u in data.get("users", []):
            if u.get("user_id") == uid:
                payload = u
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserProfile",
                "description": "Fetch user profile.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class GetSkillGap(Tool):
    """Identify skills that a user lacks compared to the target role."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, target_role: str = None) -> str:
        for g in data.get("skill_gap_analysis", []):
            if g.get("user_id") == user_id and g.get("target_role") == target_role:
                payload = g.get("skill_gaps", [])
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Gap data not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSkillGap",
                "description": "Retrieve missing skills.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "target_role": {"type": "string"},
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }


class GetPerformanceReview(Tool):
    """Retrieve performance review workflows for a specific user and time frame."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, period: str = None) -> str:
        reviews = [
            wf
            for wf in data.get("hr_workflows", [])
            if wf.get("workflow_type") == "Performance Review"
            and wf.get("employee_id") == user_id
            and wf.get("review_period") == period
        ]
        payload = reviews
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPerformanceReview",
                "description": "Get performance review by period.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "period": {"type": "string"},
                    },
                    "required": ["user_id", "period"],
                },
            },
        }


class GetCourseProgress(Tool):
    """Check the enrollment progress for a particular course."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, course_id: str = None) -> str:
        for rec in data.get("user_course_progress", []):
            if rec.get("user_id") == user_id and rec.get("course_id") == course_id:
                payload = rec
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Progress record not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCourseProgress",
                "description": "Fetch course progress.",
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


class GetUserCourseProgress(Tool):
    """Retrieve the complete course progress for a user."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        uid = user_id
        progress = [
            rec
            for rec in data.get("user_course_progress", [])
            if rec.get("user_id") == uid
        ]
        payload = progress
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserCourseProgress",
                "description": "Get all course progress for user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class SearchCourses(Tool):
    """Look for courses based on skill."""

    @staticmethod
    def invoke(data: dict[str, Any], skill: str) -> str:
        skill_query = skill
        # Adjusted to look for 'related_skills' and conduct a case-insensitive check
        courses = [
            c
            for c in data.get("course_catalog", [])
            if skill_query.lower() in [s.lower() for s in c.get("related_skills", [])]
        ]
        payload = courses
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchCourses",
                "description": "Search for courses by skill.",
                "parameters": {
                    "type": "object",
                    "properties": {"skill": {"type": "string"}},
                    "required": ["skill"],
                },
            },
        }


class SearchJobPostings(Tool):
    """Provide job postings that align with specified keywords and location."""

    @staticmethod
    def invoke(data: dict[str, Any], skill_keywords: list[str] = None, location: str = None) -> str:
        if skill_keywords is None:
            skill_keywords = []
        res = [
            p
            for p in data.get("job_postings", [])
            if (not location or location.lower() in p.get("location", ""))
            and all(kw.lower() in json.dumps(p).lower() for kw in skill_keywords)
        ]
        payload = res
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchJobPostings",
                "description": "Search postings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "skill_keywords": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "location": {"type": "string"},
                    },
                    "required": ["skill_keywords"],
                },
            },
        }


class GetJobApplication(Tool):
    """Retrieve a job application record using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], application_id: str = None) -> str:
        aid = application_id
        for a in data.get("job_applications", []):
            if a.get("application_id") == aid:
                payload = a
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Application not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetJobApplication",
                "description": "Get job application.",
                "parameters": {
                    "type": "object",
                    "properties": {"application_id": {"type": "string"}},
                    "required": ["application_id"],
                },
            },
        }


class ShortlistCandidate(Tool):
    """Include a candidate in the shortlist for a job posting."""

    @staticmethod
    def invoke(data: dict[str, Any], job_id: str = None, candidate_id: str = None) -> str:
        jid = job_id
        cid = candidate_id
        for p in data.get("job_postings", []):
            if p.get("job_id") == jid:
                sl = p.setdefault("shortlist", [])
                if cid not in sl:
                    sl.append(cid)
                payload = {"success": f"{cid} shortlisted for {jid}"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Job not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ShortlistCandidate",
                "description": "Shortlist candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {"type": "string"},
                        "candidate_id": {"type": "string"},
                    },
                    "required": ["job_id", "candidate_id"],
                },
            },
        }


class UpdateApplicationStatus(Tool):
    """Update the status of a job application."""

    @staticmethod
    def invoke(data: dict[str, Any], application_id: str = None, status: str = None) -> str:
        for a in data.get("job_applications", []):
            if a.get("application_id") == application_id:
                a["status"] = status
                a["last_updated"] = datetime.utcnow().date().isoformat()
                payload = {"success": f"{application_id} status {status}"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Application not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateApplicationStatus",
                "description": "Update app status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "application_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["application_id", "status"],
                },
            },
        }


#Tools for writing
class AssignCourse(Tool):
    """Register a user in a course."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, course_id: str = None) -> str:
        uid = user_id
        cid = course_id
        log = data.setdefault("user_course_progress", [])
        log[:] = [r for r in log if not (r["user_id"] == uid and r["course_id"] == cid)]
        log.append(
            {
                "user_id": uid,
                "course_id": cid,
                "enrolled_date": datetime.utcnow().date().isoformat(),
                "progress_percent": 0,
            }
        )
        payload = {"success": f"{uid} enrolled in {cid}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignCourse",
                "description": "Enroll user in course.",
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


class LinkMentor(Tool):
    """Connect a mentor with a mentee."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, mentor_id: str = None) -> str:
        uid = user_id
        mid = mentor_id
        rel = data.setdefault("user_mentorship_relationships", [])
        rel[:] = [
            r for r in rel if not (r["mentee_id"] == uid and r["mentor_id"] == mid)
        ]
        rel.append(
            {
                "mentee_id": uid,
                "mentor_id": mid,
                "start_date": datetime.utcnow().date().isoformat(),
                "status": "Active",
            }
        )
        payload = {"success": f"Mentor {mid} -> {uid}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkMentor",
                "description": "Link mentor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "mentor_id": {"type": "string"},
                    },
                    "required": ["user_id", "mentor_id"],
                },
            },
        }


class UpdateWorkflowStage(Tool):
    """Revise the status of the HR workflow stage."""

    @staticmethod
    def invoke(data: dict[str, Any], workflow_id: str = None, stage: str = None, status: str = None) -> str:
        wid = workflow_id
        stg = stage
        st = status
        for wf in data.get("hr_workflows", []):
            if wf.get("workflow_id") == wid:
                for s in wf.get("workflow_stages", []):
                    if s.get("stage") == stg:
                        s["status"] = st
                        s["date"] = datetime.utcnow().date().isoformat()
                        payload = {"success": f"{stg} -> {st}"}
                        out = json.dumps(payload, indent=2)
                        return out
        payload = {"error": "Not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateWorkflowStage",
                "description": "Update stage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "workflow_id": {"type": "string"},
                        "stage": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["workflow_id", "stage", "status"],
                },
            },
        }


class SetPerformanceGoal(Tool):
    """Introduce a performance objective."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, goal: str = None) -> str:
        tbl = data.setdefault("goals", [])
        tbl.append({"user_id": user_id, "goals": [goal]})
        payload = {"success": f"Goal set for {user_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetPerformanceGoal",
                "description": "Set performance goal.",
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


class UpdateSkillProficiency(Tool):
    """Revise the proficiency level of a user's skills."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, skill: str = None, new_level: int = None) -> str:
        uid = user_id
        skill = skill
        level = new_level
        skills = data.setdefault("user_skills", [])
        skills[:] = [
            s for s in skills if not (s["user_id"] == uid and s["skill"] == skill)
        ]
        skills.append(
            {
                "user_id": uid,
                "skill": skill,
                "proficiency_level": level,
                "updated_date": datetime.utcnow().date().isoformat(),
            }
        )
        payload = {"success": f"{uid} {skill} -> {level}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSkillProficiency",
                "description": "Update skill level.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "skill": {"type": "string"},
                        "new_level": {"type": "string"},
                    },
                    "required": ["user_id", "skill", "new_level"],
                },
            },
        }


class GetTeamTrainingLog(Tool):
    """Retrieve entries from the team training log."""

    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None) -> str:
        logs = [
            log
            for log in data.get("team_training_logs", [])
            if log.get("team_id") == team_id
        ]
        payload = logs
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamTrainingLog",
                "description": "Get team training log.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class UpdateTeamTrainingLog(Tool):
    """Insert an entry into the team training log."""

    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None, entry: str = None) -> str:
        logs = data.setdefault("team_training_logs", [])
        logs.append(
            {
                "team_id": team_id,
                "entry": entry,
                "date": datetime.utcnow().date().isoformat(),
            }
        )
        payload = {"success": f"Log entry added for {team_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTeamTrainingLog",
                "description": "Add training log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "entry": {"type": "string"},
                    },
                    "required": ["team_id", "entry"],
                },
            },
        }


class GetUserCertification(Tool):
    """Retrieve certifications held by a user."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        uid = user_id
        certs = [
            c for c in data.get("user_certifications", []) if c.get("user_id") == uid
        ]
        payload = certs
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserCertification",
                "description": "Get user certifications.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class UpdateUserCertification(Tool):
    """Revise a user's certification."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, certification: str = None) -> str:
        uid = user_id
        cert = certification
        certs = data.setdefault("user_certifications", [])
        certs[:] = [
            c for c in certs if not (c["user_id"] == uid and c["certification"] == cert)
        ]
        certs.append(
            {
                "user_id": uid,
                "certification": cert,
                "date_earned": datetime.utcnow().date().isoformat(),
            }
        )
        payload = {"success": f"{uid} earned {cert}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateUserCertification",
                "description": "Update user certification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "certification": {"type": "string"},
                    },
                    "required": ["user_id", "certification"],
                },
            },
        }


class FindUserByName(Tool):
    """Locate a user's ID using their full name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        for u in data.get("users", []):
            if u.get("name").lower() == name.lower():
                payload = {"user_id": u.get("user_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindUserByName",
                "description": "Find a user's ID by their full name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class FindCourseByName(Tool):
    """Identify a course's ID based on its name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        for c in data.get("course_catalog", []):
            if c.get("name").lower() == name.lower():
                payload = {"course_id": c.get("course_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": "Course not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCourseByName",
                "description": "Find a course's ID by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class FindJobByTitle(Tool):
    """Determine a job posting's ID using its title."""

    @staticmethod
    def invoke(data: dict[str, Any], title: str = None) -> str:
        for j in data.get("job_postings", []):
            if j.get("title").lower() == title.lower():
                payload = {"job_id": j.get("job_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": "Job not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindJobByTitle",
                "description": "Find a job posting's ID by its title.",
                "parameters": {
                    "type": "object",
                    "properties": {"title": {"type": "string"}},
                    "required": ["title"],
                },
            },
        }


class FindApplication(Tool):
    """Locate a job application ID using the user ID and job ID."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, job_id: str = None) -> str:
        for a in data.get("job_applications", []):
            if a.get("applicant_id") == user_id and a.get("job_id") == job_id:
                payload = {"application_id": a.get("application_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": "Application not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindApplication",
                "description": "Find a job application ID by user and job ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "job_id": {"type": "string"},
                    },
                    "required": ["user_id", "job_id"],
                },
            },
        }


class FindMentor(Tool):
    """Identify an available mentor based on expertise."""

    @staticmethod
    def invoke(data: dict[str, Any], expertise: list[str] = None) -> str:
        mentors = data.get("user_mentorship", [])
        # Deterministic choice: the first mentor from the list who meets all expertise criteria and is available.
        for m in sorted(mentors, key=lambda x: x["mentor_id"]):  # Sort to ensure determinism
            if m.get("availability") != "Full" and all(
                e.lower() in [exp.lower() for exp in m.get("expertise", [])]
                for e in expertise
            ):
                payload = {"mentor_id": m.get("mentor_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": "No suitable mentor found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindMentor",
                "description": "Find an available mentor by expertise.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expertise": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["expertise"],
                },
            },
        }


class FindWorkflow(Tool):
    """Locate a workflow ID using the employee ID and workflow name."""

    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, workflow_name: str = None) -> str:
        uid = employee_id
        name = workflow_name

        for wf in data.get("hr_workflows", []):
            # Verify if the workflow name matches initially
            if wf.get("workflow_name", "").lower() == name.lower():
                # Verify the presence of a top-level employee_id (e.g., Performance Review)
                if wf.get("employee_id") == uid:
                    payload = {"workflow_id": wf.get("workflow_id")}
                    out = json.dumps(payload)
                    return out

                # Confirm if the user is included in the 'candidates' list (e.g., Succession Planning)
                if any(
                    candidate.get("employee_id") == uid
                    for candidate in wf.get("candidates", [])
                ):
                    payload = {"workflow_id": wf.get("workflow_id")}
                    out = json.dumps(payload)
                    return out

                # Verify if the user appears in the 'target_audience' list (e.g., Training Initiative)
                if uid in wf.get("target_audience", []):
                    payload = {"workflow_id": wf.get("workflow_id")}
                    out = json.dumps(payload)
                    return out
        payload = {"error": "Workflow not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindWorkflow",
                "description": "Find a workflow ID by employee and workflow name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "workflow_name": {"type": "string"},
                    },
                    "required": ["employee_id", "workflow_name"],
                },
            },
        }


class GetWorkflowDetails(Tool):
    """Retrieve comprehensive details of a specific HR workflow using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], workflow_id: str = None) -> str:
        wid = workflow_id
        for wf in data.get("hr_workflows", []):
            if wf.get("workflow_id") == wid:
                payload = wf
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Workflow not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWorkflowDetails",
                "description": "Fetch the full details of a specific HR workflow by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"workflow_id": {"type": "string"}},
                    "required": ["workflow_id"],
                },
            },
        }


TOOLS = [
    GetUserProfile(),
    GetSkillGap(),
    GetPerformanceReview(),
    GetCourseProgress(),
    GetUserCourseProgress(),
    SearchCourses(),
    SearchJobPostings(),
    GetJobApplication(),
    ShortlistCandidate(),
    UpdateApplicationStatus(),
    AssignCourse(),
    LinkMentor(),
    UpdateWorkflowStage(),
    SetPerformanceGoal(),
    UpdateSkillProficiency(),
    GetTeamTrainingLog(),
    UpdateTeamTrainingLog(),
    GetUserCertification(),
    UpdateUserCertification(),
    FindUserByName(),
    FindCourseByName(),
    FindJobByTitle(),
    FindApplication(),
    FindMentor(),
    FindWorkflow(),
    GetWorkflowDetails(),
]
