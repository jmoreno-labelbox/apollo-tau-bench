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


class SearchUsers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, user_id: Any = None, name: Any = None, research_field: Any = None, availability: Any = None, institution: Any = None) -> str:
        """
        Conducts a user search.
        - If 'user_id' is supplied, it returns the information for that particular user.
        - If not, it filters users based on 'name' and/or 'research_field'.
        - If no arguments are given, it returns all users.
        """
        users = data.get("users", {}).values()

        # When a user_id is given, it takes precedence and retrieves a specific user.
        if user_id:
            for user in users.values():
                if user.get("person_id") == user_id:
                    payload = user
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"User with ID '{user_id}' not found."}
            out = json.dumps(payload)
            return out

        # In the absence of a user_id, it performs a search using other criteria and returns a collection.
        if not name and not research_field:
            payload = users
            out = json.dumps(payload, indent=2)
            return out

        results = [
            user
            for user in users.values()
            if (not name or name.lower() in user.get("label", "").lower())
            and (
                not research_field
                or research_field.lower() in user.get("study_field", "").lower()
            )
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
        
    @staticmethod
    def get_info() -> dict[str, Any]:
        """
        Provides the function schema intended for use by the language model.
        """
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchUsers",
                "description": "Searches for users by ID, name, or research field. If a user_id is provided, returns the details of that user. Otherwise, returns a list of users that match the other criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user to retrieve details for.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the user to search for.",
                        },
                        "research_field": {
                            "type": "string",
                            "description": "The research field of the user.",
                        },
                    },
                },
            },
        }


class CreateLogEntry(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        article_id: str = None,
        notes: str = None,
        relevance: str = "medium",
        log_id_override: str = None
    ) -> str:
        if not all([user_id, notes]):
            payload = {"error": "user_id and notes are required."}
            out = json.dumps(payload)
            return out
        users, articles, logs = (
            data.get("users", {}).values(),
            data.get("articles", {}).values(),
            data.get("research_logs", {}).values(),
        )
        if not any(u["person_id"] == user_id for u in users.values()):
            payload = {"error": f"User with ID '{user_id}' not found."}
            out = json.dumps(payload)
            return out

        if article_id:
            if not any(a["paper_id"] == article_id for a in articles.values()):
                payload = {"error": f"Article with ID '{article_id}' not found."}
                out = json.dumps(payload)
                return out
        new_log_id = (
            log_id_override if log_id_override else f"log_{uuid.uuid4().hex[:4]}"
        )
        if log_id_override and any(log["record_log_id"] == log_id_override for log in logs.values()):
            payload = {
                "error": f"A log entry with the override ID '{log_id_override}' already exists."
            }
            out = json.dumps(payload)
            return out
        new_log_entry = {
            "record_log_id": new_log_id,
            "investigator_id": user_id,
            "paper_id": article_id,
            "recorded_date": datetime.now().strftime("%Y-%m-%d"),
            "annotations": notes,
            "significance": relevance,
        }
        data["research_logs"][new_log_id] = new_log_entry

        if article_id:
            for user in users.values():
                if (
                    user["person_id"] == user_id
                    and article_id not in user["recorded_papers"]
                ):
                    user["recorded_papers"].append(article_id)
                    break
        payload = {"success": True, "log_entry": new_log_entry}
        out = json.dumps(payload)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "CreateLogEntry",
                "description": "Creates a new entry in the research log for a specific user and optionally for an article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the researcher creating the log.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article being logged. This is optional.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "The personal notes about the article or task.",
                        },
                        "relevance": {
                            "type": "string",
                            "description": "The relevance of the entry. E.g., 'high', 'medium', 'low'. Defaults to 'medium'.",
                        },
                        "log_id_override": {
                            "type": "string",
                            "description": "Optional. A specific ID to assign to the new log entry for predictable referencing.",
                        },
                    },
                    "required": ["user_id", "notes"],
                },
            },
        }


class UpdateLogNotes(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], log_id: Any = None, new_notes: str = None) -> str:
        if not all([log_id, new_notes]):
            payload = {"error": "log_id and new_notes are required."}
            out = json.dumps(payload)
            return out
        for log in data.get("research_logs", {}).values():
            if log["record_log_id"] == log_id:
                log["annotations"] += f"\n[UPDATE]: {new_notes}"
                payload = {"success": True, "log_entry": log}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Log entry with ID '{log_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateLogNotes",
                "description": "Appends new notes to an existing research log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_id": {
                            "type": "string",
                            "description": "The ID of the log entry to update.",
                        },
                        "new_notes": {
                            "type": "string",
                            "description": "The new notes to append to the existing log.",
                        },
                    },
                    "required": ["log_id", "new_notes"],
                },
            },
        }


class GetLogDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], log_id: Any = None) -> str:
        log_id = log_id
        if not log_id:
            payload = {"error": "log_id is required."}
            out = json.dumps(payload)
            return out
        for log in data.get("research_logs", {}).values():
            if log["record_log_id"] == log_id:
                return log.get("annotations", "")
        payload = {"error": f"Log entry with ID '{log_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLogDetails",
                "description": "Retrieves just the notes from a single log entry by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_id": {
                            "type": "string",
                            "description": "The unique ID of the log entry to retrieve.",
                        }
                    },
                    "required": ["log_id"],
                },
            },
        }


class UpdateArticleDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], article_id: str = None, new_topic: str = None, new_status: str = None) -> str:
        if not article_id or (not new_topic and not new_status):
            payload = {"error": "article_id and either new_topic or new_status are required."}
            out = json.dumps(payload)
            return out
        for article in data.get("articles", {}).values():
            if article["paper_id"] == article_id:
                if new_topic:
                    article["subject"] = new_topic
                if new_status:
                    article["state"] = new_status
                payload = {"success": True, "article": article}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Article with ID '{article_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateArticleDetails",
                "description": "Updates the details (e.g., topic, status) of an article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to update.",
                        },
                        "new_topic": {
                            "type": "string",
                            "description": "The new topic for the article.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the article (e.g., 'new', 'processing', 'archived').",
                        },
                    },
                    "required": ["article_id"],
                },
            },
        }


class GetSubmissionByArticle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        submissions = data.get("submissions", {}).values()
        for submission in submissions.values():
            if submission.get("paper_id") == article_id:
                payload = submission
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No submission found for article_id '{article_id}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSubmissionByArticle",
                "description": "Retrieves a submission's details using the ID of the article that was submitted.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The unique ID of the article to find the submission for.",
                        }
                    },
                    "required": ["article_id"],
                },
            },
        }


class SearchProjects(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, project_name: Any = None, funding_source_id: Any = None, chief_researcher_id: Any = None) -> str:
        """
        Looks for research projects.
        - Filters based on 'project_name', 'funding_source_id', and/or 'chief_researcher_id'.
        - If no parameters are supplied, it returns all projects.
        """
        projects = data.get("projects", {}).values()

        if not project_name and not funding_source_id and not chief_researcher_id:
            payload = projects
            out = json.dumps(payload, indent=2)
            return out

        results = [
            p
            for p in projects.values()
            if (
                not project_name
                or project_name.lower() in p.get("project_name", "").lower()
            )
            and (
                not funding_source_id or p.get("funding_source_id") == funding_source_id
            )
            and (
                not chief_researcher_id or p.get("chief_researcher_id") == chief_researcher_id
            )
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """
        Delivers the function schema for the language model's use.
        """
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchProjects",
                "description": "Searches for research projects by name, funding source ID, or chief researcher ID. If no parameters are provided, returns all projects.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {
                            "type": "string",
                            "description": "The name of the project to search for.",
                        },
                        "funding_source_id": {
                            "type": "string",
                            "description": "The ID of the funding source to filter projects.",
                        },
                        "chief_researcher_id": {
                            "type": "string",
                            "description": "The ID of the chief researcher to filter projects.",
                        },
                    },
                },
            },
        }


class SearchFundingSources(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], source_name: Any = None, focus_area: Any = None, status: Any = None, funding_source_id: Any = None) -> str:
        sources = data.get("funding_sources", {}).values()

        if not source_name and not focus_area and not status and not funding_source_id:
            payload = sources
            out = json.dumps(payload, indent=2)
            return out

        results = [
            s
            for s in sources.values()
            if (
                not source_name
                or source_name.lower() in s.get("source_name", "").lower()
            )
            and (
                not focus_area or s.get("focus_area", "").lower() == focus_area.lower()
            )
            and (not status or s.get("status", "").lower() == status.lower())
            and (not funding_source_id or s.get("sponsor_id") == funding_source_id)
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchFundingSources",
                "description": "Searches for funding sources by name, focus area, status, or funding source ID. If no parameters are provided, it returns all sources.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {
                            "type": "string",
                            "description": "The name of the funding source to search for.",
                        },
                        "focus_area": {
                            "type": "string",
                            "description": "The focus area of the funding source (e.g., 'AI', 'Biomedicine').",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the funding source (e.g., 'available', 'depleted').",
                        },
                        "funding_source_id": {
                            "type": "string",
                            "description": "The ID of the funding source to search for.",
                        },
                    },
                },
            },
        }


class GetReviewBySubmission(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, submission_id: Any = None) -> str:
        submission_id = submission_id
        if not submission_id:
            payload = {"error": "submission_id is required."}
            out = json.dumps(payload)
            return out

        reviews = data.get("reviews", {}).values()
        for review in reviews.values():
            if review.get("proposal_id") == submission_id:
                payload = review
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No review found for submission_id '{submission_id}'."}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReviewBySubmission",
                "description": "Retrieves a review's details using the ID of the submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The unique ID of the submission to find the review for.",
                        }
                    },
                    "required": ["submission_id"],
                },
            },
        }


class GetProjectDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, project_id: Any = None) -> str:
        project_id = project_id
        if not project_id:
            payload = {"error": "project_id is required."}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", {}).values()
        for p in projects.values():
            if p.get("study_id") == project_id:
                payload = p
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Project with ID '{project_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectDetails",
                "description": "Retrieves the full details for a single project by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The unique ID of the project to retrieve.",
                        }
                    },
                    "required": ["project_id"],
                },
            },
        }


class AssignReviewerToSubmission(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, reviewer_user_id: Any = None) -> str:
        if not all([submission_id, reviewer_user_id]):
            payload = {"error": "submission_id and reviewer_user_id are required."}
            out = json.dumps(payload)
            return out

        for sub in data.get("submissions", {}).values():
            if sub["proposal_id"] == submission_id:
                if reviewer_user_id not in sub["allocated_evaluators"]:
                    sub["allocated_evaluators"].append(reviewer_user_id)
                payload = {"success": True, "submission": sub}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Submission with ID '{submission_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignReviewerToSubmission",
                "description": "Assigns a reviewer to a submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to update.",
                        },
                        "reviewer_user_id": {
                            "type": "string",
                            "description": "The user ID of the reviewer to assign.",
                        },
                    },
                    "required": ["submission_id", "reviewer_user_id"],
                },
            },
        }


class CreateProject(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, project_name: Any = None, lead_researcher_id: Any = None, project_id_override: Any = None, linked_articles: list = None, funding_source_id: Any = None) -> str:
        project_name = project_name
        lead_researcher_id = lead_researcher_id
        if not all([project_name, lead_researcher_id]):
            payload = {"error": "project_name and lead_researcher_id are required."}
            out = json.dumps(
                payload)
            return out

        project_id_override = project_id_override
        new_id = (
            project_id_override
            if project_id_override
            else f"proj_{uuid.uuid4().hex[:4]}"
        )

        if any(p["study_id"] == new_id for p in data.get("projects", {}).values():
            payload = {"error": f"Project with ID '{new_id}' already exists."}
            out = json.dumps(payload)
            return out

        new_project = {
            "study_id": new_id,
            "study_name": project_name,
            "chief_researcher_id": lead_researcher_id,
            "state": "active",
            "begin_date": datetime.now().strftime("%Y-%m-%d"),
            "finish_date": None,
            "connected_papers": linked_articles or [],
            "sponsor_id": funding_source_id,
        }
        data["projects"][project_id] = new_project
        payload = {"success": True, "project": new_project}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateProject",
                "description": "Creates a new research project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {
                            "type": "string",
                            "description": "The name of the new project.",
                        },
                        "lead_researcher_id": {
                            "type": "string",
                            "description": "The user ID of the lead researcher.",
                        },
                        "project_id_override": {
                            "type": "string",
                            "description": "Optional. A specific ID to assign to the new project.",
                        },
                        "linked_articles": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional. A list of article IDs to link to the project.",
                        },
                        "funding_source_id": {
                            "type": "string",
                            "description": "Optional. The ID of the funding source for the project.",
                        },
                    },
                    "required": ["project_name", "lead_researcher_id"],
                },
            },
        }


class GetCitationDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], citation_id: Any = None) -> str:
        citation_id = citation_id
        if not citation_id:
            payload = {"error": "citation_id is required."}
            out = json.dumps(payload)
            return out

        for citation in data.get("citations", {}).values():
            if citation.get("reference_id") == citation_id:
                payload = citation
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Citation with ID '{citation_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCitationDetails",
                "description": "Retrieves the full details for a single citation by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "citation_id": {
                            "type": "string",
                            "description": "The unique ID of the citation to retrieve.",
                        }
                    },
                    "required": ["citation_id"],
                },
            },
        }


class UpdateProjectLinks(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: Any = None, add_article_id: Any = None) -> str:
        project_id = project_id
        add_article_id = add_article_id
        if not all([project_id, add_article_id]):
            payload = {"error": "project_id and add_article_id are required."}
            out = json.dumps(payload)
            return out

        for project in data.get("projects", {}).values():
            if project["study_id"] == project_id:
                if add_article_id not in project.get("connected_papers", []):
                    project["connected_papers"].append(add_article_id)
                payload = {"success": True, "project": project}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Project with ID '{project_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProjectLinks",
                "description": "Links an additional article to an existing project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project to update.",
                        },
                        "add_article_id": {
                            "type": "string",
                            "description": "The ID of the article to link to the project.",
                        },
                    },
                    "required": ["project_id", "add_article_id"],
                },
            },
        }


class UpdateSubmissionStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, new_status: Any = None) -> str:
        if not all([submission_id, new_status]):
            payload = {"error": "submission_id and new_status are required."}
            out = json.dumps(payload)
            return out

        for sub in data.get("submissions", {}).values():
            if sub["proposal_id"] == submission_id:
                sub["state"] = new_status
                payload = {"success": True, "submission": sub}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Submission with ID '{submission_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSubmissionStatus",
                "description": "Updates the status of a submission (e.g., 'under_review', 'revising').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status to set for the submission.",
                        },
                    },
                    "required": ["submission_id", "new_status"],
                },
            },
        }


class GetSubmissionDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None) -> str:
        if not submission_id:
            payload = {"error": "submission_id is required."}
            out = json.dumps(payload)
            return out

        submissions = data.get("submissions", {}).values()
        for sub in submissions.values():
            if sub.get("proposal_id") == submission_id:
                payload = sub
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Submission with ID '{submission_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSubmissionDetails",
                "description": "Retrieves the full details for a single submission by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The unique ID of the submission to retrieve.",
                        }
                    },
                    "required": ["submission_id"],
                },
            },
        }


class UpdateProjectStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: Any = None, new_status: Any = None, new_end_date: Any = None) -> str:
        if not project_id or not new_status:
            payload = {"error": "project_id and new_status are required."}
            out = json.dumps(payload)
            return out

        for project in data.get("projects", {}).values():
            if project["study_id"] == project_id:
                project["state"] = new_status
                if new_end_date is not None:
                    project["finish_date"] = new_end_date
                else:
                    project["finish_date"] = None
                payload = {"success": True, "project": project}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Project with ID '{project_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProjectStatus",
                "description": "Updates the status of a project (e.g., 'active', 'completed') and can optionally update its end date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status to set for the project.",
                        },
                        "new_end_date": {
                            "type": "string",
                            "description": "Optional. The new end date for the project in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["project_id", "new_status"],
                },
            },
        }


class CreateCitation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], source_article_id: Any = None, cited_article_id: Any = None, citation_context: Any = None) -> str:
        source_article_id = source_article_id
        cited_article_id = cited_article_id
        context = citation_context
        if not all([source_article_id, cited_article_id]):
            payload = {"error": "source_article_id and cited_article_id are required."}
            out = json.dumps(payload)
            return out

        new_id = f"cit_{uuid.uuid4().hex[:4]}"
        new_citation = {
            "reference_id": new_id,
            "origin_paper_id": source_article_id,
            "referenced_paper_id": cited_article_id,
            "reference_context": context,
        }
        data["citations"][citation_id] = new_citation
        payload = {"success": True, "citation": new_citation}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCitation",
                "description": "Creates a new citation, linking a source article to a cited article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_article_id": {
                            "type": "string",
                            "description": "The ID of the article making the citation.",
                        },
                        "cited_article_id": {
                            "type": "string",
                            "description": "The ID of the article being cited.",
                        },
                        "citation_context": {
                            "type": "string",
                            "description": "The sentence or context in which the citation is made.",
                        },
                    },
                    "required": ["source_article_id", "cited_article_id"],
                },
            },
        }


class SearchCitations(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, direction: Any = None, context_keyword: Any = None) -> str:
        """
        Looks for citations associated with a particular article.
        - The direction of the search ('to' or 'from') is necessary.
        - 'to': Locates all citations that reference the article_id.
        - 'from': Locates all citations authored by the article_id.
        """
        if not all([article_id, direction]):
            payload = {"error": "article_id and direction are required."}
            out = json.dumps(payload)
            return out

        citations = data.get("citations", {}).values()
        results = []

        if direction.lower() == "to":
            keyword = context_keyword.lower() if context_keyword else None
            results = [
                c
                for c in citations.values()
                if c.get("referenced_paper_id") == article_id
                and (not keyword or keyword in c.get("citation_context", "").lower())
            ]
        elif direction.lower() == "from":
            results = [c for c in citations.values() if c.get("source_article_id") == article_id]
        else:
            payload = {"error": "Invalid direction. Must be 'to' or 'from'."}
            out = json.dumps(payload)
            return out
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """
        Supplies the function schema for the language model's application.
        """
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchCitations",
                "description": "Searches for citations from or to an article. Use direction 'to' to find citations that an article received or 'from' to find citations that an article made.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to search for citations.",
                        },
                        "direction": {
                            "type": "string",
                            "enum": ["to", "from"],
                            "description": "The direction of the search: 'to' (for citations to the article) or 'from' (for citations from the article).",
                        },
                        "context_keyword": {
                            "type": "string",
                            "description": "Optional. A keyword to search for in the citation context (only for 'to' direction).",
                        },
                    },
                    "required": ["article_id", "direction"],
                },
            },
        }


class ManageUserSubscriptions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: Any = None, topic: Any = None, action: Any = None) -> str:
        """
        Modifies a user's subscription to a topic by adding or removing it.
        - Needs user_id, topic, and action ('add' or 'remove').
        """
        if not all([user_id, topic, action]):
            payload = {"error": "user_id, topic, and action are required."}
            out = json.dumps(payload)
            return out

        subscriptions = data.get("subscriptions", {}).values()

        if action.lower() == "add":
            already_subscribed = any(
                sub.get("person_id") == user_id and sub.get("subject") == topic
                for sub in subscriptions.values()
            )
            if already_subscribed:
                payload = {
                    "success": False,
                    "message": "User is already subscribed to this topic.",
                }
                out = json.dumps(payload)
                return out

            new_sub_id = f"sub_topic_{uuid.uuid4().hex[:6]}"
            new_subscription = {
                "membership_id": new_sub_id,
                "person_id": user_id,
                "subject": topic,
            }
            data["subscriptions"][new_subscription["subscription_id"]] = new_subscription
            payload = {"success": True, "subscription": new_subscription}
            out = json.dumps(payload)
            return out

        elif action.lower() == "remove":
            initial_count = len(subscriptions)
            # Generate a new list that omits the subscription intended for removal.
            data["subscriptions"] = [
                sub
                for sub in subscriptions.values() if not (sub.get("person_id") == user_id and sub.get("subject") == topic)
            ]

            if len(data["subscriptions"]) < initial_count:
                payload = {
                    "success": True,
                    "message": f"Subscription to topic '{topic}' for user '{user_id}' removed.",
                }
                out = json.dumps(payload)
                return out
            else:
                payload = {"error": "Subscription not found to remove."}
                out = json.dumps(payload)
                return out

        else:
            payload = {"error": "Invalid action. Must be 'add' or 'remove'."}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """
        Provides the function schema intended for the language model.
        """
        pass
        return {
            "type": "function",
            "function": {
                "name": "ManageUserSubscriptions",
                "description": "Adds or removes a user's subscription to a specific topic.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "The topic to subscribe to or unsubscribe from.",
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "remove"],
                            "description": "The action to perform: 'add' or 'remove' the subscription.",
                        },
                    },
                    "required": ["user_id", "topic", "action"],
                },
            },
        }


class SendNotification(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipient_user_id: Any = None, message_content: Any = None, sender_user_id: Any = 'system') -> str:
        """
        Generates and dispatches a new notification to a user.
        - Needs recipient_user_id and message_content.
        - sender_user_id is optional and defaults to 'system'.
        """
        if not all([recipient_user_id, message_content]):
            payload = {"error": "recipient_user_id and message_content are required."}
            out = json.dumps(payload)
            return out

        notifications = data.get("notifications", {}).values()
        new_notification = {
            "alert_id": f"notif_{uuid.uuid4().hex[:6]}",
            "receiver_person_id": recipient_user_id,
            "sender_person_id": sender_user_id,
            "note_text": message_content,
            "time_recorded": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "state": "unread",
        }
        data["notifications"][new_notification["notification_id"]] = new_notification
        payload = {"success": True, "notification": new_notification}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """
        Supplies the function schema for the language model's use.
        """
        pass
        return {
            "type": "function",
            "function": {
                "name": "SendNotification",
                "description": "Sends a direct notification to a specific user. Can be from another user or the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {
                            "type": "string",
                            "description": "The ID of the user who will receive the notification.",
                        },
                        "message_content": {
                            "type": "string",
                            "description": "The content of the notification message.",
                        },
                        "sender_user_id": {
                            "type": "string",
                            "description": "Optional. The ID of the user sending the notification. Defaults to 'system'.",
                        },
                    },
                    "required": ["recipient_user_id", "message_content"],
                },
            },
        }


class SearchArticles(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        article_id: Any = None,
        title: Any = None,
        topic: Any = None,
        year: Any = None,
        author_name: Any = None,
        abstract_keyword: Any = None,
        full_text_keyword: Any = None
    ) -> str:
        articles = data.get("articles", {}).values()

        if article_id:
            for article in articles.values():
                if article.get("paper_id") == article_id:
                    payload = [article]
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Article with ID '{article_id}' not found."}
            out = json.dumps(payload)
            return out

        if not any(
            [title, topic, year, author_name, abstract_keyword, full_text_keyword]
        ):
            payload = articles
            out = json.dumps(payload, indent=2)
            return out

        results = [
            a
            for a in articles.values()
            if (not title or title.lower() in a.get("heading", "").lower())
            and (not topic or topic.lower() in a.get("subject", "").lower())
            and (not year or year == a.get("release_year"))
            and (
                not author_name
                or any(
                    author_name.lower() in author.lower()
                    for author in a.get("writers", [])
                )
            )
            and (
                not abstract_keyword
                or abstract_keyword.lower() in a.get("summary", "").lower()
            )
            and (
                not full_text_keyword
                or full_text_keyword.lower() in a.get("complete_text", "").lower()
            )
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        """
        Provides the function schema designated for the language model.
        """
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchArticles",
                "description": "Searches for academic articles by ID, title, topic, year, author, or keywords in the abstract or full text. If an article_id is provided, it returns the details of that specific article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to retrieve details for.",
                        },
                        "title": {
                            "type": "string",
                            "description": "A keyword or phrase from the article title.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "A topic to search for (e.g., 'IA', 'Biology').",
                        },
                        "year": {
                            "type": "integer",
                            "description": "A specific publication year to filter by.",
                        },
                        "author_name": {
                            "type": "string",
                            "description": "The name of an author to search for.",
                        },
                        "abstract_keyword": {
                            "type": "string",
                            "description": "A keyword to search for within the article's abstract.",
                        },
                        "full_text_keyword": {
                            "type": "string",
                            "description": "A keyword to search for within the article's full text.",
                        },
                    },
                },
            },
        }


class SummarizeArticle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None) -> str:
        """
        Locates an article using its ID and provides a summary of its complete text.
        The summary is created by pulling the first three sentences.
        """
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        articles = data.get("articles", {}).values()
        for article in articles.values():
            if article.get("paper_id") == article_id:
                full_text = article.get("complete_text")
                if not full_text:
                    payload = {
                        "error": f"Article with ID '{article_id}' has no full text to summarize."
                    }
                    out = json.dumps(payload)
                    return out

                # Basic summarization approach: extract the initial three sentences.
                sentences = full_text.split(".")
                summary = ". ".join(sentences[:3]).strip()
                if summary:
                    summary += "."
                payload = {"success": True, "article_id": article_id, "summary": summary}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Article with ID '{article_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """
        Delivers the function schema for the language model's application.
        """
        pass
        return {
            "type": "function",
            "function": {
                "name": "SummarizeArticle",
                "description": "Generates a concise summary of an article's full text using its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The unique ID of the article to summarize.",
                        }
                    },
                    "required": ["article_id"],
                },
            },
        }


TOOLS = [
    SearchUsers(),
    SearchArticles(),
    CreateLogEntry(),
    UpdateLogNotes(),
    GetLogDetails(),
    UpdateArticleDetails(),
    GetSubmissionByArticle(),
    SearchProjects(),
    SearchFundingSources(),
    GetReviewBySubmission(),
    GetProjectDetails(),
    AssignReviewerToSubmission(),
    CreateProject(),
    GetCitationDetails(),
    UpdateProjectLinks(),
    UpdateSubmissionStatus(),
    GetSubmissionDetails(),
    UpdateProjectStatus(),
    CreateCitation(),
    SearchCitations(),
    ManageUserSubscriptions(),
    SendNotification(),
    SummarizeArticle(),
]
