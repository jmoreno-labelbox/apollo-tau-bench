import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class FetchArticles(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, article_id: Any = None, topic: Any = None, title: Any = None, year: Any = None, author_name: Any = None) -> str:
        articles: list = data.get("articles", {}).values()

        if article_id:
            for article in articles.values():
                if article.get("article_id") == article_id:
                    payload = [article]
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
            payload = []
            out = json.dumps(payload)
            return out

        results = []
        for article in articles.values():
            match = True
            if topic and topic.lower() not in article.get("topic", "").lower():
                match = False
            if title and title.lower() not in article.get("title", "").lower():
                match = False
            if (
                author_name
                and author_name.lower() not in article.get("author_name", "").lower()
            ):
                match = False
            if year and year != article.get("publication_year"):
                match = False
            if match:
                results.append(article)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchArticles",
                "description": "Searches for academic articles by ID, topic, title, or publication year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The unique ID of the article.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "A topic to search for (e.g., 'AI', 'Biology').",
                        },
                        "title": {
                            "type": "string",
                            "description": "A keyword or phrase from the article title.",
                        },
                        "year": {
                            "type": "integer",
                            "description": "A specific publication year to filter by.",
                        },
                    },
                    "required": [],
                },
            },
        }


class FetchUsers(Tool):
    """Utility for locating users by their ID, name, or research area."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: Any = None, name: Any = None, research_field: Any = None, availability: Any = None, institution: Any = None) -> str:
        user_id = user_id
        name = name
        research_field = research_field

        users = data.get("users", {}).values()

        if user_id:
            for user in users.values():
                if user.get("person_id") == user_id:
                    payload = [user]
                    out = json.dumps(payload, indent=2)
                    return out
            payload = []
            out = json.dumps(payload)
            return out

        if not name and not research_field:
            payload = {"error": "Either user_id, name, or research_field is required."}
            out = json.dumps(
                payload)
            return out

        results = []
        for user in users.values():
            match = True
            if name and name.lower() not in user.get("name", "").lower():
                match = False
            if (
                research_field
                and research_field.lower() not in user.get("research_field", "").lower()
            ):
                match = False
            if match:
                results.append(user)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchUsers",
                "description": "Searches for users by their name or research field.",
                "parameters": {
                    "type": "object",
                    "properties": {
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


class CreateReviewSubmission(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], author_user_id: Any = None, submission_id_override: Any = None, article_id: Any = None) -> str:
        author_user_id, article_id = author_user_id, article_id
        submission_id_override = submission_id_override

        if not author_user_id or not article_id:
            payload = {"error": "author_user_id and article_id are required."}
            out = json.dumps(payload)
            return out
        if not any(u["person_id"] == author_user_id for u in data.get("users", {}).values():
            payload = {"error": f"Author with ID '{author_user_id}' not found."}
            out = json.dumps(payload)
            return out
        if not any(a.get("article_id") == article_id or a.get("paper_id") == article_id for a in data.get("articles", {}).values():
            payload = {"error": f"Article with ID '{article_id}' not found."}
            out = json.dumps(payload)
            return out

        new_submission_id = (
            submission_id_override
            if submission_id_override
            else f"sub_{uuid.uuid4().hex[:4]}"
        )

        new_submission = {
            "submission_id": new_submission_id,
            "article_id": article_id,
            "author_user_id": author_user_id,
            "submission_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "submitted",
            "assigned_reviewers": [],
        }
        if "submissions" not in data:
            data["submissions"] = []
        data["submissions"][submission_id] = new_submission
        payload = {"success": True, "submission": new_submission}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReviewSubmission",
                "description": "Submits an author's article to the peer review system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "author_user_id": {
                            "type": "string",
                            "description": "The user ID of the author.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article being submitted.",
                        },
                        "submission_id_override": {
                            "type": "string",
                            "description": "Optional. A specific ID to assign to the new submission.",
                        },
                    },
                    "required": ["author_user_id", "article_id"],
                },
            },
        }


class AssignReviewer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, reviewer_user_id: Any = None, overwrite: Any = None) -> str:
        submissions = data.get("submissions", {}).values()
        for sub in submissions.values():
            if sub.get("submission_id") == submission_id or sub.get("proposal_id") == submission_id:
                if overwrite:
                    sub["allocated_evaluators"] = [reviewer_user_id]
                else:
                    if "allocated_evaluators" not in sub:
                        sub["allocated_evaluators"] = []
                    if reviewer_user_id not in sub["allocated_evaluators"]:
                        sub["allocated_evaluators"].append(reviewer_user_id)

                sub["status"] = "under_review"
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
                "name": "AssignReviewer",
                "description": "Assigns a reviewer to an article submission, with an option to overwrite the existing list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission.",
                        },
                        "reviewer_user_id": {
                            "type": "string",
                            "description": "The user ID of the person assigned to review.",
                        },
                        "overwrite": {
                            "type": "boolean",
                            "description": "If true, replaces the reviewer list. Defaults to false (append).",
                        },
                    },
                    "required": ["submission_id", "reviewer_user_id"],
                },
            },
        }


class FetchSubmissionInfo(Tool):
    """Utility to retrieve submission information for an article or based on submission ID."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, submission_id: Any = None) -> str:
        if not article_id and not submission_id:
            payload = {"error": "Either article_id or submission_id is required."}
            out = json.dumps(payload)
            return out

        submissions = data.get("submissions", {}).values()
        for sub in submissions.values():
            if (article_id and sub.get("article_id") == article_id) or (
                submission_id and sub.get("submission_id") == submission_id
            ):
                payload = sub
                out = json.dumps(payload, indent=2)
                return out

        if article_id:
            payload = {"error": f"No submission found for article ID '{article_id}'."}
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": f"No submission found for submission ID '{submission_id}'."}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchSubmissionInfo",
                "description": "Gets the submission details for a given article ID or submission ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to find the submission for.",
                        },
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to find.",
                        },
                    },
                },
            },
        }


class IdentifyPotentialReviewers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, exclude_user_ids: Any = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        articles = data.get("articles", {}).values()
        target_article = next(
            (a for a in articles.values() if a.get("article_id") == article_id), None
        )
        if not target_article:
            payload = {"error": f"Article with ID '{article_id}' not found."}
            out = json.dumps(payload)
            return out

        article_topic = target_article.get("topic")
        if not article_topic:
            payload = {"error": f"Article with ID '{article_id}' has no topic specified."}
            out = json.dumps(payload)
            return out

        users = data.get("users", {}).values()
        potential_reviewers = [
            user
            for user in users.values() if user.get("research_field") == article_topic
            and user.get("person_id") not in exclude_user_ids
        ]
        payload = potential_reviewers
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "IdentifyPotentialReviewers",
                "description": "Identifies potential reviewers for an article based on matching research fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article needing reviewers.",
                        },
                        "exclude_user_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of user IDs to exclude from the suggestions (e.g., the authors).",
                        },
                    },
                    "required": ["article_id"],
                },
            },
        }


class PostNewReview(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, reviewer_user_id: Any = None, recommendation: Any = None, comments: Any = None) -> str:
        if not all([submission_id, reviewer_user_id, recommendation, comments]):
            payload = {
                "error": "submission_id, reviewer_user_id, recommendation, and comments are required."
            }
            out = json.dumps(payload)
            return out

        new_review = {
            "review_id": f"rev_{uuid.uuid4().hex[:4]}",
            "submission_id": submission_id,
            "reviewer_user_id": reviewer_user_id,
            "recommendation": recommendation,
            "review_content": comments,
            "review_date": datetime.now().strftime("%Y-%m-%d"),
        }
        if "reviews" not in data:
            data["reviews"] = []
        data["reviews"][review_id] = new_review
        payload = {"success": True, "review": new_review}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PostNewReview",
                "description": "Posts a new peer review for a submission.",
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
                        "recommendation": {
                            "type": "string",
                            "description": "The recommendation (e.g., 'accept', 'minor_revisions', 'reject').",
                        },
                        "comments": {
                            "type": "string",
                            "description": "The detailed comments of the review.",
                        },
                    },
                    "required": [
                        "submission_id",
                        "reviewer_user_id",
                        "recommendation",
                        "comments",
                    ],
                },
            },
        }


class SetSubmissionOutcome(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, new_status: Any = None) -> str:
        if not all([submission_id, new_status]):
            payload = {"error": "submission_id and new_status are required."}
            out = json.dumps(payload)
            return out

        submissions = data.get("submissions", {}).values()
        for sub in submissions.values():
            if sub.get("submission_id") == submission_id:
                sub["status"] = new_status
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
                "name": "SetSubmissionOutcome",
                "description": "Sets the outcome or status for a submission (e.g., 'accepted', 'rejected').",
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


class ConnectRevisedVersion(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, revised_article_id: Any = None) -> str:
        if not all([submission_id, revised_article_id]):
            payload = {"error": "submission_id and revised_article_id are required."}
            out = json.dumps(payload)
            return out

        submissions = data.get("submissions", {}).values()
        for sub in submissions.values():
            if sub.get("submission_id") == submission_id:
                sub["revised_version_article_id"] = revised_article_id
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
                "name": "ConnectRevisedVersion",
                "description": "Connects a revised version of an article to an original submission record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the original submission.",
                        },
                        "revised_article_id": {
                            "type": "string",
                            "description": "The article ID of the new, revised version.",
                        },
                    },
                    "required": ["submission_id", "revised_article_id"],
                },
            },
        }


class AlertUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipient_user_id: Any = None, message: Any = None, sender_user_id: Any = None) -> str:
        if not all([recipient_user_id, message]):
            payload = {"error": "recipient_user_id and message are required."}
            out = json.dumps(payload)
            return out

        new_notification = {
            "notification_id": f"notif_{uuid.uuid4().hex[:4]}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message,
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "status": "unread",
        }
        if "notifications" not in data:
            data["notifications"] = []
        data["notifications"][notification_id] = new_notification
        payload = {"success": True, "notification": new_notification}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AlertUser",
                "description": "Sends a direct alert message to a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {
                            "type": "string",
                            "description": "The ID of the user to receive the alert.",
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the alert message.",
                        },
                        "sender_user_id": {
                            "type": "string",
                            "description": "Optional. The user ID of the sender. Defaults to 'system'.",
                        },
                    },
                    "required": ["recipient_user_id", "message"],
                },
            },
        }


class AdjustUserSettings(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, user_id: Any = None, notification_channel: Any = None, ui_theme: Any = None, research_field: Any = None) -> str:
        user_id = user_id
        if not user_id:
            payload = {"error": "user_id is required."}
            out = json.dumps(payload)
            return out

        notification_channel = notification_channel
        ui_theme = ui_theme
        research_field = research_field

        if not notification_channel and not ui_theme and not research_field:
            payload = {
                    "error": "At least one setting (notification_channel, ui_theme, or research_field) must be provided."
                }
            out = json.dumps(
                payload)
            return out

        preferences = data.get("user_preferences", {}).values()

        pref_found = False
        for pref in preferences.values():
            if pref.get("person_id") == user_id:
                if notification_channel:
                    pref["notification_channel"] = notification_channel
                if ui_theme:
                    pref["ui_theme"] = ui_theme
                pref_found = True
                break

        if not pref_found:
            new_pref = {
                "preference_id": f"pref_{uuid.uuid4().hex[:4]}",
                "user_id": user_id,
                "notification_channel": (
                    notification_channel if notification_channel else "none"
                ),  #Initial value
                "preferred_email": "",  #Presuming a blank default
                "ui_theme": ui_theme if ui_theme else "light",  #Initial value
            }
            if "user_preferences" not in data:
                data["user_preferences"] = []
            data["user_preferences"][user_preference_id] = new_pref
            pref = new_pref
            pref_found = True

        user_obj = None
        for user in data.get("users", {}).values():
            if user.get("person_id") == user_id:
                if research_field:
                    user["research_field"] = research_field
                user_obj = user
                break

        if pref_found or user_obj:
            if (
                research_field and user_obj
            ):  #If research_field has been changed, return the user object
                payload = {"success": True, "user": user_obj}
                out = json.dumps(payload)
                return out
            elif (
                pref_found
            ):  #Otherwise, return the preferences (if they have been altered/created)
                payload = {"success": True, "settings": pref}
                out = json.dumps(payload)
                return out
        payload = {
                "error": f"Settings for user ID '{user_id}' not found and could not be created."
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AdjustUserSettings",
                "description": "Adjusts a user's personal settings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID for whom to adjust settings.",
                        },
                        "notification_channel": {
                            "type": "string",
                            "description": "The new notification channel (e.g., 'email', 'in_app', 'none').",
                        },
                        "ui_theme": {
                            "type": "string",
                            "description": "The new UI theme (e.g., 'dark', 'light').",
                        },
                        "research_field": {
                            "type": "string",
                            "description": "The new primary research field for the user.",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }


class SetTopicInterest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, topic: str = None, action: str = None) -> str:
        if not all([user_id, topic, action]):
            payload = {"error": "user_id, topic, and action are required."}
            out = json.dumps(payload)
            return out

        subscriptions = data.get("subscriptions", {}).values()
        if action.lower() == "add":
            if any(
                s.get("person_id") == user_id and s.get("topic") == topic
                for s in subscriptions.values()
            ):
                payload = {
                        "success": False,
                        "message": "User is already subscribed to this topic.",
                    }
                out = json.dumps(
                    payload)
                return out
            new_sub = {
                "subscription_id": f"sub_topic_{uuid.uuid4().hex[:4]}",
                "user_id": user_id,
                "topic": topic,
            }
            data["subscriptions"][subscription_id] = new_sub
            payload = {"success": True, "subscription": new_sub}
            out = json.dumps(payload)
            return out
        elif action.lower() == "remove":
            initial_count = len(subscriptions)
            data["subscriptions"] = [
                s
                for s in subscriptions.values() if not (s.get("person_id") == user_id and s.get("topic") == topic)
            ]
            if len(data["subscriptions"]) < initial_count:
                payload = {
                        "success": True,
                        "message": f"Subscription to topic '{topic}' removed.",
                    }
                out = json.dumps(
                    payload)
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
        return {
            "type": "function",
            "function": {
                "name": "SetTopicInterest",
                "description": "Sets a user's interest in a topic by adding or removing a subscription.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID."},
                        "topic": {
                            "type": "string",
                            "description": "The research topic.",
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "remove"],
                            "description": "The action to perform.",
                        },
                    },
                    "required": ["user_id", "topic", "action"],
                },
            },
        }


class RegisterNewArticle(Tool):
    """Records a new manuscript for an article within the system."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        title: Any = None,
        authors: Any = None,
        topic: Any = None,
        abstract: Any = None,
        article_id_override: Any = None,
        full_text: str = ""
    ) -> str:
        title = title
        authors = authors
        topic = topic
        abstract = abstract
        article_id_override = article_id_override

        if not all([title, authors, topic, abstract]):
            payload = {"error": "title, authors, topic, and abstract are required."}
            out = json.dumps(payload)
            return out

        new_article_id = (
            article_id_override
            if article_id_override
            else f"art_{uuid.uuid4().hex[:4]}"
        )

        new_article = {
            "article_id": new_article_id,
            "title": title,
            "authors": authors,
            "publication_year": datetime.now().year,
            "topic": topic,
            "abstract": abstract,
            "status": "draft",
            "full_text": full_text,
        }
        if "articles" not in data:
            data["articles"] = []
        data["articles"][article_id] = new_article
        payload = {"success": True, "article": new_article}
        out = json.dumps(payload)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterNewArticle",
                "description": "Registers a new article manuscript in the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "authors": {"type": "array", "items": {"type": "string"}},
                        "topic": {"type": "string"},
                        "abstract": {"type": "string"},
                        "article_id_override": {
                            "type": "string",
                            "description": "Optional. A specific ID to assign to the new article for predictable referencing.",
                        },
                    },
                    "required": ["title", "authors", "topic", "abstract"],
                },
            },
        }


class ReviseArticleDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, article_id: Any = None, title: str = None, abstract: str = None, topic: str = None, status: str = None) -> str:
        article_id = article_id
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        article = next(
            (a for a in data.get("articles", {}).values() if a.get("article_id") == article_id),
            None,
        )
        if not article:
            payload = {"error": f"Article with ID '{article_id}' not found."}
            out = json.dumps(payload)
            return out

        updatable_fields = {"title": title, "abstract": abstract, "topic": topic, "status": status}
        for key, value in updatable_fields.items():
            if value is not None:
                article[key] = value
        payload = {"success": True, "article": article}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReviseArticleDetails",
                "description": "Revises details of an existing article, such as its abstract or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to revise.",
                        },
                        "title": {
                            "type": "string",
                            "description": "The new title for the article.",
                        },
                        "abstract": {
                            "type": "string",
                            "description": "The new abstract for the article.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "The new topic for the article.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status for the article.",
                        },
                    },
                    "required": ["article_id"],
                },
            },
        }


class ListReviewsForSubmission(Tool):
    """Lists all evaluations submitted for a specific submission."""
    @staticmethod
    def invoke(data: dict[str, Any], *, submission_id: Any = None) -> str:
        if not submission_id:
            payload = {"error": "submission_id is required."}
            out = json.dumps(payload)
            return out

        reviews = data.get("reviews", {}).values()
        submission_reviews = [
            r for r in reviews.values() if r.get("submission_id") == submission_id
        ]
        payload = submission_reviews
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListReviewsForSubmission",
                "description": "Lists all submitted reviews for a specific submission ID.",
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


class CreateNewProject(Tool):
    """Initiates a new research project."""

    @staticmethod
    def invoke(data: dict[str, Any], *, project_name: Any = None, lead_researcher_id: Any = None, project_id_override: Any = None, linked_article_ids: list = None) -> str:
        project_name = project_name
        lead_researcher_id = lead_researcher_id
        project_id_override = project_id_override

        if not all([project_name, lead_researcher_id]):
            payload = {"error": "project_name and lead_researcher_id are required."}
            out = json.dumps(
                payload)
            return out

        new_project_id = (
            project_id_override
            if project_id_override
            else f"proj_{uuid.uuid4().hex[:4]}"
        )

        new_project = {
            "project_id": new_project_id,
            "project_name": project_name,
            "lead_researcher_id": lead_researcher_id,
            "status": "active",
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "end_date": None,
            "linked_articles": linked_article_ids if linked_article_ids is not None else [],
        }
        if "projects" not in data:
            data["projects"] = []
        data["projects"][project_id] = new_project
        payload = {"success": True, "project": new_project}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewProject",
                "description": "Creates a new research project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string"},
                        "lead_researcher_id": {"type": "string"},
                        "linked_article_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "project_id_override": {
                            "type": "string",
                            "description": "Optional. A specific ID to assign to the new project.",
                        },
                    },
                    "required": ["project_name", "lead_researcher_id"],
                },
            },
        }


class GetArticleKeywords(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        article = next(
            (a for a in data.get("articles", {}).values() if a.get("article_id") == article_id),
            None,
        )
        if not article or not article.get("abstract"):
            payload = []
            out = json.dumps(payload)
            return out

        text = article.get("abstract", "").lower()
        words = re.findall(r"\b\w+\b", text)
        stop_words = {
            "a",
            "an",
            "the",
            "in",
            "of",
            "for",
            "is",
            "on",
            "and",
            "to",
            "with",
            "by",
            "as",
            "its",
            "we",
            "this",
        }
        meaningful_words = [
            word for word in words if word not in stop_words and not word.isdigit()
        ]

        top_keywords = [
            word for word, count in Counter(meaningful_words).most_common(5)
        ]
        payload = top_keywords
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetArticleKeywords",
                "description": "Identifies potential keywords from an article's abstract based on word frequency.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to extract keywords from.",
                        }
                    },
                    "required": ["article_id"],
                },
            },
        }


class FindCitations(Tool):
    """Identifies all articles that reference a specified article."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, citations: list = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        citations = citations or []
        citing_articles = [
            c.get("source_article_id")
            for c in citations
            if c.get("referenced_paper_id") == article_id
        ]
        payload = citing_articles
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCitations",
                "description": "Finds all articles that cite a given article ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to find citations for.",
                        }
                    },
                    "required": ["article_id"],
                },
            },
        }


class UpdateProjectDetails(Tool):
    """Modifies the information of an existing research project."""

    @staticmethod
    def invoke(data: dict[str, Any], *, project_id: Any = None, project_name: str = None, status: str = None, linked_article_ids: list = None, lead_researcher_id: str = None) -> str:
        project_id = project_id
        if not project_id:
            payload = {"error": "project_id is required."}
            out = json.dumps(payload)
            return out

        project = next(
            (p for p in data.get("projects", {}).values() if p.get("project_id") == project_id),
            None,
        )
        if not project:
            payload = {"error": f"Project with ID '{project_id}' not found."}
            out = json.dumps(payload)
            return out

        updatable_fields = ["project_name", "status", "linked_article_ids", "lead_researcher_id"]
        updates = {"project_name": project_name, "status": status, "linked_article_ids": linked_article_ids, "lead_researcher_id": lead_researcher_id}
        for key, value in updates.items():
            if key in updatable_fields and value is not None:
                project[key] = value
        payload = {"success": True, "project": project}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProjectDetails",
                "description": "Updates details of an existing project, such as its name or linked articles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project to update.",
                        },
                        "project_name": {
                            "type": "string",
                            "description": "The new name for the project.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status for the project.",
                        },
                        "linked_article_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A new list of linked article IDs.",
                        },
                        "lead_researcher_id": {
                            "type": "string",
                            "description": "The new lead researcher ID for the project.",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }


class RemoveReview(Tool):
    """Removes a review entry from the system."""

    @staticmethod
    def invoke(data: dict[str, Any], review_id: Any = None) -> str:
        review_id = review_id
        if not review_id:
            payload = {"error": "review_id is required."}
            out = json.dumps(payload)
            return out

        reviews = data.get("reviews", {}).values()
        original_count = len(reviews)
        # Reminder: In an actual database, this would perform a direct deletion. Here, we filter the array.
        data["reviews"] = [r for r in reviews.values() if r.get("review_id") != review_id]

        if len(data["reviews"]) < original_count:
            payload = {"success": True, "message": f"Review {review_id} has been deleted."}
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": f"Review with ID '{review_id}' not found."}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveReview",
                "description": "Deletes a specific review by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "review_id": {
                            "type": "string",
                            "description": "The ID of the review to delete.",
                        }
                    },
                    "required": ["review_id"],
                },
            },
        }


TOOLS = [
    FetchArticles(),
    FetchUsers(),
    CreateReviewSubmission(),
    AssignReviewer(),
    FetchSubmissionInfo(),
    IdentifyPotentialReviewers(),
    PostNewReview(),
    SetSubmissionOutcome(),
    ConnectRevisedVersion(),
    AlertUser(),
    AdjustUserSettings(),
    SetTopicInterest(),
    RegisterNewArticle(),
    ReviseArticleDetails(),
    ListReviewsForSubmission(),
    CreateNewProject(),
    GetArticleKeywords(),
    FindCitations(),
    UpdateProjectDetails(),
    RemoveReview(),
]
