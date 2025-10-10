import json
from datetime import datetime
from typing import Any, Dict, List
from domains.dto import Tool


# Read-only Tools
class GetUserProfile(Tool):
    """Fetch an employee's profile by ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        for u in data.get("users", []):
            if u.get("user_id") == uid:
                return json.dumps(u, indent=2)
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_profile",
                "description": "Fetch user profile.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class GetSkillGap(Tool):
    """List missing skills for a user vs target role."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        role = kwargs.get("target_role")
        for g in data.get("skill_gap_analysis", []):
            if g.get("user_id") == uid and g.get("target_role") == role:
                return json.dumps(g.get("skill_gaps", []), indent=2)
        return json.dumps({"error": "Gap data not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_skill_gap",
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
    """Fetch performance review workflows for a user and period."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        per = kwargs.get("period")
        reviews = [
            wf
            for wf in data.get("hr_workflows", [])
            if wf.get("workflow_type") == "Performance Review"
            and wf.get("employee_id") == uid
            and wf.get("review_period") == per
        ]
        return json.dumps(reviews, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_performance_review",
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
    """Look up enrollment progress for a course."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        cid = kwargs.get("course_id")
        for rec in data.get("user_course_progress", []):
            if rec.get("user_id") == uid and rec.get("course_id") == cid:
                return json.dumps(rec, indent=2)
        return json.dumps({"error": "Progress record not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_course_progress",
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
    """Get all course progress for a user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        progress = [
            rec
            for rec in data.get("user_course_progress", [])
            if rec.get("user_id") == uid
        ]
        return json.dumps(progress, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_course_progress",
                "description": "Get all course progress for user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class SearchCourses(Tool):
    """Search for courses by skill."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        skill_query = kwargs.get("skill")
        # Corrected to search 'related_skills' and perform a case-insensitive comparison
        courses = [
            c
            for c in data.get("course_catalog", [])
            if skill_query.lower() in [s.lower() for s in c.get("related_skills", [])]
        ]
        return json.dumps(courses, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_courses",
                "description": "Search for courses by skill.",
                "parameters": {
                    "type": "object",
                    "properties": {"skill": {"type": "string"}},
                    "required": ["skill"],
                },
            },
        }


class SearchJobPostings(Tool):
    """Return job postings matching keywords and location."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        kws = kwargs.get("skill_keywords", [])
        loc = kwargs.get("location")
        res = [
            p
            for p in data.get("job_postings", [])
            if (not loc or loc.lower() in p.get("location", ""))
            and all(kw.lower() in json.dumps(p).lower() for kw in kws)
        ]
        return json.dumps(res, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_job_postings",
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
    """Fetch a job application record by ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("application_id")
        for a in data.get("job_applications", []):
            if a.get("application_id") == aid:
                return json.dumps(a, indent=2)
        return json.dumps({"error": "Application not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_job_application",
                "description": "Get job application.",
                "parameters": {
                    "type": "object",
                    "properties": {"application_id": {"type": "string"}},
                    "required": ["application_id"],
                },
            },
        }


class ShortlistCandidate(Tool):
    """Add a candidate to a posting's shortlist."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        jid = kwargs.get("job_id")
        cid = kwargs.get("candidate_id")
        for p in data.get("job_postings", []):
            if p.get("job_id") == jid:
                sl = p.setdefault("shortlist", [])
                if cid not in sl:
                    sl.append(cid)
                return json.dumps({"success": f"{cid} shortlisted for {jid}"}, indent=2)
        return json.dumps({"error": "Job not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "shortlist_candidate",
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
    """Set a new status on a job application."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("application_id")
        st = kwargs.get("status")
        for a in data.get("job_applications", []):
            if a.get("application_id") == aid:
                a["status"] = st
                a["last_updated"] = datetime.utcnow().date().isoformat()
                return json.dumps({"success": f"{aid} status {st}"}, indent=2)
        return json.dumps({"error": "Application not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_application_status",
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


# Write Tools
class AssignCourse(Tool):
    """Enroll user in course."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        cid = kwargs.get("course_id")
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
        return json.dumps({"success": f"{uid} enrolled in {cid}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_course",
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
    """Link mentor to mentee."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        mid = kwargs.get("mentor_id")
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
        return json.dumps({"success": f"Mentor {mid} -> {uid}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_mentor",
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
    """Update HR workflow stage status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        wid = kwargs.get("workflow_id")
        stg = kwargs.get("stage")
        st = kwargs.get("status")
        for wf in data.get("hr_workflows", []):
            if wf.get("workflow_id") == wid:
                for s in wf.get("workflow_stages", []):
                    if s.get("stage") == stg:
                        s["status"] = st
                        s["date"] = datetime.utcnow().date().isoformat()
                        return json.dumps({"success": f"{stg} -> {st}"}, indent=2)
        return json.dumps({"error": "Not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_workflow_stage",
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
    """Add a performance goal."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        goal = kwargs.get("goal")
        tbl = data.setdefault("goals", [])
        tbl.append({"user_id": uid, "goals": [goal]})
        return json.dumps({"success": f"Goal set for {uid}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_performance_goal",
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
    """Update user skill proficiency level."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        skill = kwargs.get("skill")
        level = kwargs.get("new_level")
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
        return json.dumps({"success": f"{uid} {skill} -> {level}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_skill_proficiency",
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
    """Get team training log entries."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tid = kwargs.get("team_id")
        logs = [
            log
            for log in data.get("team_training_logs", [])
            if log.get("team_id") == tid
        ]
        return json.dumps(logs, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_training_log",
                "description": "Get team training log.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class UpdateTeamTrainingLog(Tool):
    """Add entry to team training log."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tid = kwargs.get("team_id")
        entry = kwargs.get("entry")
        logs = data.setdefault("team_training_logs", [])
        logs.append(
            {
                "team_id": tid,
                "entry": entry,
                "date": datetime.utcnow().date().isoformat(),
            }
        )
        return json.dumps({"success": f"Log entry added for {tid}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_team_training_log",
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
    """Get user certifications."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        certs = [
            c for c in data.get("user_certifications", []) if c.get("user_id") == uid
        ]
        return json.dumps(certs, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_certification",
                "description": "Get user certifications.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class UpdateUserCertification(Tool):
    """Update user certification."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        cert = kwargs.get("certification")
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
        return json.dumps({"success": f"{uid} earned {cert}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_certification",
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
    """Find a user's ID by their full name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        for u in data.get("users", []):
            if u.get("name").lower() == name.lower():
                return json.dumps({"user_id": u.get("user_id")})
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_user_by_name",
                "description": "Find a user's ID by their full name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class FindCourseByName(Tool):
    """Find a course's ID by its name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        for c in data.get("course_catalog", []):
            if c.get("name").lower() == name.lower():
                return json.dumps({"course_id": c.get("course_id")})
        return json.dumps({"error": "Course not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_course_by_name",
                "description": "Find a course's ID by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class FindJobByTitle(Tool):
    """Find a job posting's ID by its title."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        title = kwargs.get("title")
        for j in data.get("job_postings", []):
            if j.get("title").lower() == title.lower():
                return json.dumps({"job_id": j.get("job_id")})
        return json.dumps({"error": "Job not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_job_by_title",
                "description": "Find a job posting's ID by its title.",
                "parameters": {
                    "type": "object",
                    "properties": {"title": {"type": "string"}},
                    "required": ["title"],
                },
            },
        }


class FindApplication(Tool):
    """Find a job application ID by user ID and job ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        jid = kwargs.get("job_id")
        for a in data.get("job_applications", []):
            if a.get("applicant_id") == uid and a.get("job_id") == jid:
                return json.dumps({"application_id": a.get("application_id")})
        return json.dumps({"error": "Application not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_application",
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
    """Find an available mentor by expertise."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        expertise = kwargs.get("expertise")
        mentors = data.get("user_mentorship", [])
        # Deterministic selection: first mentor in the list that matches all expertise areas and has capacity.
        for m in sorted(mentors, key=lambda x: x["mentor_id"]):  # Sort for determinism
            if m.get("availability") != "Full" and all(
                e.lower() in [exp.lower() for exp in m.get("expertise", [])]
                for e in expertise
            ):
                return json.dumps({"mentor_id": m.get("mentor_id")})
        return json.dumps({"error": "No suitable mentor found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_mentor",
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
    """Find a workflow ID by employee ID and workflow name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("employee_id")
        name = kwargs.get("workflow_name")

        for wf in data.get("hr_workflows", []):
            # Check if the workflow name matches first
            if wf.get("workflow_name", "").lower() == name.lower():
                # Check for a top-level employee_id (e.g., Performance Review)
                if wf.get("employee_id") == uid:
                    return json.dumps({"workflow_id": wf.get("workflow_id")})

                # Check if the user is in the 'candidates' list (e.g., Succession Planning)
                if any(
                    candidate.get("employee_id") == uid
                    for candidate in wf.get("candidates", [])
                ):
                    return json.dumps({"workflow_id": wf.get("workflow_id")})

                # Check if the user is in the 'target_audience' list (e.g., Training Initiative)
                if uid in wf.get("target_audience", []):
                    return json.dumps({"workflow_id": wf.get("workflow_id")})

        return json.dumps({"error": "Workflow not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_workflow",
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
    """Fetch the full details of a specific HR workflow by its ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        wid = kwargs.get("workflow_id")
        for wf in data.get("hr_workflows", []):
            if wf.get("workflow_id") == wid:
                return json.dumps(wf, indent=2)
        return json.dumps({"error": "Workflow not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_workflow_details",
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
