import json
import uuid
from datetime import datetime
from typing import Any

from domains.dto import Tool


class FindUsers(Tool):
    """
    Utility for finding users by name or research area, or retrieving details of a specific user by their ID.
    This utility supersedes GetUserDetails.
    """

    @staticmethod
    def invoke(data: dict[str, Any], *, user_id: Any = None, name: Any = None, research_field: Any = None, availability: Any = None, institution: Any = None) -> str:
        user_id = user_id
        name = name
        research_field = research_field

        users = data.get("users", [])

        if user_id:
            for user in users:
                if user.get("person_id") == user_id:
                    payload = user
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"User with ID '{user_id}' not found."}
            out = json.dumps(payload)
            return out

        if not name and not research_field:
            payload = {
                    "error": "For a general search, 'name' or 'research_field' is required."
                }
            out = json.dumps(
                payload)
            return out

        results = [
            user
            for user in users
            if (not name or name.lower() in user.get("name", "").lower())
            and (
                not research_field
                or research_field.lower() in user.get("research_field", "").lower()
            )
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindUsers",
                "description": "Searches for users by name or research field, or retrieves a single user by their specific ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The specific ID of the user to retrieve.",
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


class LaunchProject(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_name: Any = None, lead_researcher_id: Any = None, funding_source_id: Any = None, project_id_override: Any = None) -> str:
        project_name = project_name
        lead_researcher_id = lead_researcher_id
        funding_source_id = funding_source_id
        project_id_override = project_id_override  # Additional parameter

        project_id = (
            project_id_override
            if project_id_override
            else f"proj_{uuid.uuid4().hex[:4]}"
        )

        new_project = {
            "project_id": project_id,
            "project_name": project_name,
            "lead_researcher_id": lead_researcher_id,
            "status": "proposed",
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "end_date": None,
            "linked_articles": [],
            "funding_source_id": funding_source_id,
        }
        data["projects"].append(new_project)
        payload = {"success": True, "project": new_project}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "LaunchProject",
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
                        "funding_source_id": {
                            "type": "string",
                            "description": "The ID of the project's funding source.",
                        },
                        "project_id_override": {
                            "type": "string",
                            "description": "Optional. A specific ID to assign to the new project for predictable referencing.",
                        },
                    },
                    "required": [
                        "project_name",
                        "lead_researcher_id",
                        "funding_source_id",
                    ],
                },
            },
        }


class ModifySubmissionStatus(Tool):
    """Utility for modifying the status of a submission."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, new_status: Any = None) -> str:
        if not submission_id or not new_status:
            payload = {"error": "submission_id and new_status are required."}
            out = json.dumps(payload)
            return out

        submissions = data.get("submissions", [])
        for submission in submissions:
            if submission.get("submission_id") == submission_id:
                submission["status"] = new_status
                payload = {
                    "success": True,
                    "submission_id": submission_id,
                    "new_status": new_status,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Submission not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "ModifySubmissionStatus",
                "description": "Updates the status of a submission (e.g., 'under_review', 'accepted', 'rejected').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the submission.",
                        },
                    },
                    "required": ["submission_id", "new_status"],
                },
            },
        }


class AppointReviewer(Tool):
    """Utility for designating a reviewer for a submission."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, reviewer_user_id: Any = None) -> str:
        if not submission_id or not reviewer_user_id:
            payload = {"error": "submission_id and reviewer_user_id are required."}
            out = json.dumps(payload)
            return out

        submissions = data.get("submissions", [])
        for submission in submissions:
            if submission.get("submission_id") == submission_id:
                if "assigned_reviewers" not in submission:
                    submission["assigned_reviewers"] = []
                if reviewer_user_id not in submission["assigned_reviewers"]:
                    submission["assigned_reviewers"].append(reviewer_user_id)
                    payload = {
                        "success": True,
                        "submission_id": submission_id,
                        "reviewer_id": reviewer_user_id,
                    }
                    out = json.dumps(payload)
                    return out
                else:
                    payload = {"error": "Reviewer already assigned to this submission."}
                    out = json.dumps(payload)
                    return out
        payload = {"error": "Submission not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "AppointReviewer",
                "description": "Assigns a researcher to review a submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission.",
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


class SubmitReview(Tool):
    """Utility for generating a new review for a submission."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, reviewer_user_id: Any = None, review_content: Any = None, recommendation: Any = None) -> str:
        if not all([submission_id, reviewer_user_id, review_content, recommendation]):
            payload = {
                "error": "submission_id, reviewer_user_id, review_content, and recommendation are required."
            }
            out = json.dumps(payload)
            return out

        new_review = {
            "review_id": f"rev_{uuid.uuid4().hex[:4]}",
            "submission_id": submission_id,
            "reviewer_user_id": reviewer_user_id,
            "review_content": review_content,
            "recommendation": recommendation,
            "review_date": datetime.now().strftime("%Y-%m-%d"),
        }
        data["reviews"].append(new_review)
        payload = {"success": True, "review": new_review}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "SubmitReview",
                "description": "Creates a new review for a submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission being reviewed.",
                        },
                        "reviewer_user_id": {
                            "type": "string",
                            "description": "The user ID of the reviewer.",
                        },
                        "review_content": {
                            "type": "string",
                            "description": "The text content of the review.",
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "The recommendation (e.g., 'accept', 'minor_revisions').",
                        },
                    },
                    "required": [
                        "submission_id",
                        "reviewer_user_id",
                        "review_content",
                        "recommendation",
                    ],
                },
            },
        }


class GetReviewsForSubmission(Tool):
    """Utility for fetching all reviews related to a particular submission."""

    @staticmethod
    def invoke(data: dict[str, Any], *, submission_id: Any = None) -> str:
        if not submission_id:
            payload = {"error": "submission_id is required."}
            out = json.dumps(payload)
            return out

        reviews = data.get("reviews", [])
        submission_reviews = [
            review for review in reviews if review.get("submission_id") == submission_id
        ]
        payload = submission_reviews
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetReviewsForSubmission",
                "description": "Gets all reviews associated with a single submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to get reviews for.",
                        }
                    },
                    "required": ["submission_id"],
                },
            },
        }


class ModifyProjectStatus(Tool):
    """Utility for modifying the status and/or end date of a research project."""

    @staticmethod
    def invoke(data: dict[str, Any], *, project_id: Any = None, new_status: Any = None, end_date: Any = None) -> str:
        project_id = project_id
        new_status = new_status
        end_date = end_date  # Access the newly added optional parameter

        if not project_id or not (new_status or end_date):
            payload = {"error": "project_id and either new_status or end_date are required."}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", [])
        for project in projects:
            if project.get("project_id") == project_id:
                if new_status:
                    project["status"] = new_status
                if end_date:  # Update if an end_date is supplied
                    project["end_date"] = end_date
                updated_fields = {}
                if new_status:
                    updated_fields["new_status"] = new_status
                if end_date:
                    updated_fields["end_date"] = end_date
                payload = {
                    "success": True,
                    "project_id": project_id,
                    "updated_fields": updated_fields,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Project not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "ModifyProjectStatus",
                "description": "Updates the status and/or end date of a research project (e.g., 'active', 'completed', 'on_hold').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the project.",
                        },
                        #Incorporate end_date into the schema
                        "end_date": {
                            "type": "string",
                            "description": "The new end date for the project (e.g., 'YYYY-MM-DD').",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }


class LinkArticleToProject(Tool):
    """Utility for associating an article with a research project."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: Any = None, article_id: Any = None) -> str:
        project_id = project_id
        article_id = article_id
        if not project_id or not article_id:
            payload = {"error": "project_id and article_id are required."}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", [])
        for project in projects:
            if project.get("project_id") == project_id:
                if "linked_articles" not in project:
                    project["linked_articles"] = []
                if article_id not in project["linked_articles"]:
                    project["linked_articles"].append(article_id)
                    payload = {
                            "success": True,
                            "project_id": project_id,
                            "article_id": article_id,
                        }
                    out = json.dumps(
                        payload)
                    return out
                else:
                    payload = {"error": "Article already linked to this project."}
                    out = json.dumps(
                        payload)
                    return out
        payload = {"error": "Project not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "LinkArticleToProject",
                "description": "Links an existing article to a research project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to link.",
                        },
                    },
                    "required": ["project_id", "article_id"],
                },
            },
        }


class FindGrants(Tool):
    """
    Utility for locating funding sources based on different criteria, or obtaining details of a specific source by its ID.
    """

    @staticmethod
    def invoke(data: dict[str, Any], funding_source_id: Any = None, focus_area: Any = None, status: Any = None, min_grant_amount: Any = None, source_name: Any = None) -> str:
        funding_source_id = funding_source_id
        focus_area = focus_area
        status = status
        min_grant_amount = min_grant_amount

        sources = data.get("funding_sources", [])

        if funding_source_id:
            for source in sources:
                if source.get("funding_source_id") == funding_source_id:
                    payload = source
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Funding source with ID '{funding_source_id}' not found."}
            out = json.dumps(
                payload)
            return out

        results = []
        for source in sources:
            area_match = (
                not focus_area
                or focus_area.lower() in source.get("focus_area", "").lower()
            )
            status_match = (
                not status or status.lower() == source.get("status", "").lower()
            )
            amount_match = not min_grant_amount or source.get("grant_amount", 0) >= int(
                min_grant_amount
            )

            if area_match and status_match and amount_match:
                results.append(source)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindGrants",
                "description": "Searches for funding sources by criteria (focus area, status, amount), or retrieves a single source by its specific ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "funding_source_id": {
                            "type": "string",
                            "description": "The specific ID of the funding source to retrieve.",
                        },
                        "focus_area": {
                            "type": "string",
                            "description": "The research area the funding supports (e.g., 'AI').",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the grant (e.g., 'available').",
                        },
                        "min_grant_amount": {
                            "type": "integer",
                            "description": "The minimum amount of funding required.",
                        },
                    },
                },
            },
        }


class AssignFundingToProject(Tool):
    """Utility for allocating a funding source to a project."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: Any = None, funding_source_id: Any = None) -> str:
        if not project_id or not funding_source_id:
            payload = {"error": "project_id and funding_source_id are required."}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", [])
        for project in projects:
            if project.get("project_id") == project_id:
                project["funding_source_id"] = funding_source_id
                payload = {
                    "success": True,
                    "project_id": project_id,
                    "funding_source_id": funding_source_id,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Project not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "AssignFundingToProject",
                "description": "Assigns a funding source to a research project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project to be funded.",
                        },
                        "funding_source_id": {
                            "type": "string",
                            "description": "The ID of the funding source.",
                        },
                    },
                    "required": ["project_id", "funding_source_id"],
                },
            },
        }


class AddResearcherToProjectTeam(Tool):
    """Utility for including a researcher in a project's team."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: Any = None, user_id: Any = None) -> str:
        project_id = project_id
        user_id = user_id
        if not project_id or not user_id:
            payload = {"error": "project_id and user_id are required."}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", [])
        for project in projects:
            if project.get("project_id") == project_id:
                # This presumes the data model can be enhanced with a 'team_members' list.
                if "team_members" not in project:
                    project["team_members"] = []
                if user_id not in project["team_members"] and user_id != project.get(
                    "lead_researcher_id"
                ):
                    project["team_members"].append(user_id)
                    payload = {
                        "success": True,
                        "message": f"User {user_id} added to project {project_id}.",
                    }
                    out = json.dumps(payload)
                    return out
                else:
                    payload = {
                        "error": "User is already on the team or is the lead researcher."
                    }
                    out = json.dumps(payload)
                    return out
        payload = {"error": "Project not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddResearcherToProjectTeam",
                "description": "Adds a researcher to the team of an existing project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project.",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "The user ID of the researcher to add.",
                        },
                    },
                    "required": ["project_id", "user_id"],
                },
            },
        }


class CreateResearchLog(Tool):
    """Utility for generating a research log entry for a researcher regarding an article."""

    @staticmethod
    def invoke(data: dict[str, Any], researcher_id: Any = None, article_id: Any = None, notes: Any = None, relevance: Any = None, log_id_override: Any = None) -> str:
        if not all([researcher_id, article_id, notes, relevance]):
            payload = {
                    "error": "researcher_id, article_id, notes, and relevance are required."
                }
            out = json.dumps(
                payload)
            return out

        log_id = log_id_override if log_id_override else f"log_{uuid.uuid4().hex[:4]}"
        new_log = {
            "log_id": log_id,
            "researcher_id": researcher_id,
            "article_id": article_id,
            "entry_date": datetime.now().strftime("%Y-%m-%d"),
            "notes": notes,
            "relevance": relevance,
        }
        data["research_logs"].append(new_log)
        payload = {"success": True, "log_entry": new_log}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateResearchLog",
                "description": "Creates a personal research log or note for a researcher about a specific article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "researcher_id": {
                            "type": "string",
                            "description": "The user ID of the researcher creating the log.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article the log is about.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "The content of the research note.",
                        },
                        "relevance": {
                            "type": "string",
                            "description": "A relevance score (e.g., 'high', 'medium', 'low').",
                        },
                        "log_id_override": {
                            "type": "string",
                            "description": "Optional specific ID for the log entry.",
                        },
                    },
                    "required": ["researcher_id", "article_id", "notes", "relevance"],
                },
            },
        }


class SearchResearchLogs(Tool):
    """Utility for querying research logs."""

    @staticmethod
    def invoke(data: dict[str, Any], researcher_id: Any = None, article_id: Any = None) -> str:
        researcher_id = researcher_id
        article_id = article_id

        if not researcher_id and not article_id:
            payload = {"error": "Either researcher_id or article_id is required."}
            out = json.dumps(
                payload)
            return out

        logs = data.get("research_logs", [])
        results = [
            log
            for log in logs
            if (not researcher_id or log.get("researcher_id") == researcher_id)
            and (not article_id or log.get("article_id") == article_id)
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchResearchLogs",
                "description": "Searches research logs by researcher or article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "researcher_id": {
                            "type": "string",
                            "description": "The user ID of the researcher.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article.",
                        },
                    },
                },
            },
        }


class GetUserSubscriptions(Tool):
    """Utility for retrieving a user's topic subscriptions."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: Any = None) -> str:
        if not user_id:
            payload = {"error": "user_id is required."}
            out = json.dumps(payload)
            return out

        subscriptions = data.get("subscriptions", [])
        user_subs = [sub for sub in subscriptions if sub.get("user_id") == user_id]
        payload = user_subs
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetUserSubscriptions",
                "description": "Retrieves the list of topics a specific user is subscribed to.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user whose subscriptions to retrieve.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class UpdateUserSubscriptions(Tool):
    """Utility for adding or deleting a topic subscription for a user."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: Any = None, topic: Any = None, action: Any = None) -> str:
        user_id = user_id
        topic = topic
        action = action  #'add' or 'delete'
        if not user_id or not topic:
            payload = {"error": "user_id and topic are required."}
            out = json.dumps(payload)
            return out

        subscriptions = data.get("subscriptions", [])
        if action.lower() == "add":
            # Verify if the subscription is already present
            for sub in subscriptions:
                if (
                    sub.get("user_id") == user_id
                    and sub.get("topic", "").lower() == topic.lower()
                ):
                    payload = {
                        "success": True,
                        "message": "User is already subscribed to this topic.",
                    }
                    out = json.dumps(payload)
                    return out
            new_sub = {
                "subscription_id": f"sub_topic_{uuid.uuid4().hex[:4]}",
                "user_id": user_id,
                "topic": topic,
            }
            subscriptions.append(new_sub)
            payload = {"success": True, "subscription": new_sub}
            out = json.dumps(payload)
            return out
        elif action.lower() == "remove":
            initial_len = len(subscriptions)
            data["subscriptions"] = [
                sub
                for sub in subscriptions
                if not (
                    sub.get("user_id") == user_id
                    and sub.get("topic", "").lower() == topic.lower()
                )
            ]
            if len(data["subscriptions"]) < initial_len:
                payload = {
                    "success": True,
                    "message": f"Subscription to topic '{topic}' removed for user {user_id}.",
                }
                out = json.dumps(payload)
                return out
            else:
                payload = {"error": "Subscription not found."}
                out = json.dumps(payload)
                return out
        else:
            payload = {"error": "Invalid action. Must be 'add' or 'remove'."}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserSubscriptions",
                "description": "Adds or removes a topic subscription for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID to update.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "The topic to subscribe or unsubscribe from (e.g., 'AI').",
                        },
                        "action": {
                            "type": "string",
                            "description": "The action to perform: 'add' or 'remove'. Defaults to 'add'.",
                        },
                    },
                    "required": ["user_id", "topic"],
                },
            },
        }


class UpdateUserPreferences(Tool):
    """Utility for modifying a user's preferences."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: Any = None, notification_channel: Any = None, ui_theme: Any = None) -> str:
        user_id = user_id
        notification_channel = notification_channel
        ui_theme = ui_theme
        if not user_id or not (notification_channel or ui_theme):
            payload = {"error": "user_id and at least one preference to update are required."}
            out = json.dumps(payload)
            return out

        preferences = data.get("user_preferences", [])
        for pref in preferences:
            if pref.get("user_id") == user_id:
                if notification_channel:
                    pref["notification_channel"] = notification_channel
                if ui_theme:
                    pref["ui_theme"] = ui_theme
                payload = {"success": True, "updated_preferences": pref}
                out = json.dumps(payload)
                return out

        # Create one if no preferences are detected
        new_pref = {"preference_id": f"pref_{uuid.uuid4().hex[:4]}", "user_id": user_id}
        if notification_channel:
            new_pref["notification_channel"] = notification_channel
        if ui_theme:
            new_pref["ui_theme"] = ui_theme
        preferences.append(new_pref)
        payload = {"success": True, "created_preferences": new_pref}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserPreferences",
                "description": "Updates a user's preferences, such as notification channel or UI theme.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID whose preferences to update.",
                        },
                        "notification_channel": {
                            "type": "string",
                            "description": "The preferred notification channel (e.g., 'email', 'in_app', 'none').",
                        },
                        "ui_theme": {
                            "type": "string",
                            "description": "The preferred UI theme (e.g., 'light', 'dark').",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }


class NotifyUser(Tool):
    """Utility for dispatching a notification to a user."""

    @staticmethod
    def invoke(data: dict[str, Any], recipient_user_id: Any = None, message_content: Any = None, sender_user_id: Any = None) -> str:
        if not recipient_user_id or not message_content:
            payload = {"error": "recipient_user_id and message_content are required."}
            out = json.dumps(payload)
            return out

        new_notification = {
            "notification_id": f"notif_{uuid.uuid4().hex[:4]}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message_content,
            "timestamp": datetime.now().isoformat() + "Z",
            "status": "unread",
        }
        data["notifications"].append(new_notification)
        payload = {"success": True, "notification": new_notification}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "NotifyUser",
                "description": "Sends a notification to a user within the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {
                            "type": "string",
                            "description": "The user ID of the recipient.",
                        },
                        "message_content": {
                            "type": "string",
                            "description": "The content of the notification message.",
                        },
                        "sender_user_id": {
                            "type": "string",
                            "description": "The user ID of the sender. Defaults to 'system'.",
                        },
                    },
                    "required": ["recipient_user_id", "message_content"],
                },
            },
        }


class FindPublications(Tool):
    """Utility for locating articles according to different criteria."""

    @staticmethod
    def invoke(data: dict[str, Any], *, title: Any = None, author_name: Any = None, topic: Any = None, publication_year: Any = None, article_id: Any = None) -> str:
        if not any([title, author_name, topic, publication_year, article_id]):
            payload = {"error": "At least one search parameter is required."}
            out = json.dumps(payload)
            return out

        articles = data.get("articles", [])
        results = []
        for article in articles:
            title_match = not title or title.lower() in article.get("title", "").lower()
            author_match = not author_name or any(
                author_name.lower() in author.lower()
                for author in article.get("authors", [])
            )
            topic_match = not topic or topic.lower() == article.get("topic", "").lower()
            year_match = not publication_year or str(publication_year) == str(
                article.get("publication_year")
            )
            id_match = not article_id or article_id == article.get("article_id")

            if all([title_match, author_match, topic_match, year_match, id_match]):
                results.append(article)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindPublications",
                "description": "Searches for articles by title, author, topic, or publication year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "The title or a keyword from the title of the article.",
                        },
                        "author_name": {
                            "type": "string",
                            "description": "The name of one of the authors.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "The main topic of the article (e.g., 'AI', 'Biomedicine').",
                        },
                        "publication_year": {
                            "type": "integer",
                            "description": "The year the article was published.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The exact ID of the article.",
                        },
                    },
                },
            },
        }


class SummarizeArticleText(Tool):
    """Utility for obtaining a summary of an article."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        articles = data.get("articles", [])
        for article in articles:
            if article.get("article_id") == article_id:
                # This serves as a mock summary tool. In an actual system, it would utilize NLP.
                # In this case, we return only the abstract or a shortened version of the complete text.
                summary = article.get("abstract", "No abstract available.")
                if "full_text" in article and len(summary) < 20:
                    summary = article["full_text"][:200] + "..."
                payload = {"article_id": article_id, "summary": summary}
                out = json.dumps(payload)
                return out
        payload = {"error": "Article not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "SummarizeArticleText",
                "description": "Provides a concise summary of a given article's content.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to summarize.",
                        }
                    },
                    "required": ["article_id"],
                },
            },
        }


class FindReferences(Tool):
    """Utility for querying citations."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, direction: Any = None) -> str:
        article_id = article_id
        direction = direction  #'to' or 'from'
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        citations = data.get("citations", [])
        results = []
        if direction.lower() == "to":
            #Locate articles that have CITED the specified article_id
            results = [c for c in citations if c.get("referenced_paper_id") == article_id]
        elif direction.lower() == "from":
            #Identify articles that are CITED BY the specified article_id
            results = [c for c in citations if c.get("source_article_id") == article_id]
        else:
            payload = {"error": "Invalid direction. Must be 'to' or 'from'."}
            out = json.dumps(payload)
            return out
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindReferences",
                "description": "Searches for citations. Can find which articles cited a given article, or which articles a given article cited.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to search citations for.",
                        },
                        "direction": {
                            "type": "string",
                            "description": "Search direction: 'to' (who cited this article) or 'from' (who did this article cite). Defaults to 'to'.",
                        },
                    },
                    "required": ["article_id"],
                },
            },
        }


class FindProjects(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: Any = None,
        project_name: Any = None,
        lead_researcher_id: Any = None,
        status: Any = None,
        end_date_year: Any = None
    ) -> str:
        project_id = project_id
        if project_id:
            for project in data.get("projects", []):
                if project.get("project_id") == project_id:
                    payload = project
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Project with ID '{project_id}' not found."}
            out = json.dumps(payload)
            return out

        project_name = project_name
        lead_researcher_id = lead_researcher_id
        status = status
        end_date_year = end_date_year  # Additional parameter

        # Incorporate the new parameter into the validation process
        if not any([project_name, lead_researcher_id, status, end_date_year]):
            payload = {
                "error": "At least one search parameter (project_name, lead_researcher_id, status, or end_date_year) is required for a general search."
            }
            out = json.dumps(payload)
            return out

        projects = data.get("projects", [])
        results = []
        for project in projects:
            name_match = (
                not project_name
                or project_name.lower() in project.get("project_name", "").lower()
            )
            lead_match = not lead_researcher_id or lead_researcher_id == project.get(
                "lead_researcher_id"
            )
            status_match = (
                not status or status.lower() == project.get("status", "").lower()
            )

            # Implement logic for year matching
            project_end_date = project.get("end_date")
            year_match = not end_date_year or (
                project_end_date and project_end_date.startswith(str(end_date_year))
            )

            # Include year_match in the concluding condition
            if name_match and lead_match and status_match and year_match:
                results.append(project)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindProjects",
                "description": "Searches for projects by various criteria OR retrieves a single project by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The specific ID of the project to retrieve.",
                        },
                        "project_name": {
                            "type": "string",
                            "description": "The name of the project.",
                        },
                        "lead_researcher_id": {
                            "type": "string",
                            "description": "The user ID of the lead researcher.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the project.",
                        },
                        #Introduce the new parameter into the schema
                        "end_date_year": {
                            "type": "integer",
                            "description": "The year the project ended, to filter by completion year.",
                        },
                    },
                },
            },
        }


class GetUserPreferences(Tool):
    """Utility for fetching the preference settings of a particular user."""

    @staticmethod
    def invoke(data: dict[str, Any], *, user_id: Any = None) -> str:
        user_id = user_id
        if not user_id:
            payload = {"error": "user_id is required."}
            out = json.dumps(payload)
            return out

        preferences = data.get("user_preferences", [])
        for pref in preferences:
            if pref.get("user_id") == user_id:
                payload = pref
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Preferences not found for the given user ID."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetUserPreferences",
                "description": "Retrieves the preference settings (like notification channel and UI theme) for a single user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user to retrieve preferences for.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class LookupSubmissions(Tool):
    """
    Utility for searching submissions using various criteria or retrieving a specific one by ID.
    """

    @staticmethod
    def invoke(data: dict[str, Any], *, submission_id: Any = None, article_id: Any = None, author_user_id: Any = None, status: Any = None) -> str:
        submissions = data.get("submissions", [])

        if submission_id:
            for sub in submissions:
                if sub.get("submission_id") == submission_id:
                    payload = sub
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Submission with ID '{submission_id}' not found."}
            out = json.dumps(payload)
            return out

        if article_id:
            for sub in submissions:
                if sub.get("article_id") == article_id:
                    payload = sub
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"No submission found for article ID '{article_id}'."}
            out = json.dumps(payload)
            return out

        if not any([author_user_id, status]):
            payload = submissions
            out = json.dumps(payload, indent=2)
            return out

        results = []
        for sub in submissions:
            author_match = not author_user_id or author_user_id == sub.get("author_user_id")
            status_match = not status or status.lower() == sub.get("status", "").lower()

            if author_match and status_match:
                results.append(sub)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "LookupSubmissions",
                "description": "Searches for submissions by various criteria, or retrieves a single submission by its specific ID or associated article ID. Returns all submissions if no criteria are given.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The specific ID of the submission to retrieve.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to find the submission for.",
                        },
                        "author_user_id": {
                            "type": "string",
                            "description": "The user ID of the submission's author.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the submission (e.g., 'under_review').",
                        },
                    },
                },
            },
        }


TOOLS = [
    FindUsers(),
    LaunchProject(),
    ModifySubmissionStatus(),
    AppointReviewer(),
    SubmitReview(),
    GetReviewsForSubmission(),
    ModifyProjectStatus(),
    LinkArticleToProject(),
    FindGrants(),
    AssignFundingToProject(),
    AddResearcherToProjectTeam(),
    CreateResearchLog(),
    SearchResearchLogs(),
    GetUserSubscriptions(),
    UpdateUserSubscriptions(),
    UpdateUserPreferences(),
    NotifyUser(),
    FindPublications(),
    SummarizeArticleText(),
    FindReferences(),
    FindProjects(),
    GetUserPreferences(),
    LookupSubmissions(),
]
