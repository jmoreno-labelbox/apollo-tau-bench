import json
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional

from domains.dto import Tool

class FindUsers(Tool):
    """
    Tool to search for users by name or research field, OR to get a single user's details by their ID.
    This tool replaces GetUserDetails.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        name = kwargs.get('name')
        research_field = kwargs.get('research_field')

        users = data.get('users', [])

        if user_id:
            for user in users:
                if user.get('user_id') == user_id:
                    return json.dumps(user, indent=2)
            return json.dumps({"error": f"User with ID '{user_id}' not found."})

        if not name and not research_field:
            return json.dumps({"error": "For a general search, 'name' or 'research_field' is required."})

        results = [
            user for user in users
            if (not name or name.lower() in user.get('name', '').lower())
            and (not research_field or research_field.lower() in user.get('research_field', '').lower())
        ]

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_users",
                "description": "Searches for users by name or research field, or retrieves a single user by their specific ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The specific ID of the user to retrieve."},
                        "name": {"type": "string", "description": "The name of the user to search for."},
                        "research_field": {"type": "string", "description": "The research field of the user."}
                    }
                }
            }
        }

class LaunchProject(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_name = kwargs.get('project_name')
        lead_researcher_id = kwargs.get('lead_researcher_id')
        funding_source_id = kwargs.get('funding_source_id')
        project_id_override = kwargs.get('project_id_override') # New parameter

        project_id = project_id_override if project_id_override else f"proj_{uuid.uuid4().hex[:4]}"

        new_project = {"project_id": project_id,"project_name": project_name,"lead_researcher_id": lead_researcher_id,"status": "proposed","start_date": datetime.now().strftime('%Y-%m-%d'),"end_date": None,"linked_articles": [], "funding_source_id": funding_source_id}
        data['projects'].append(new_project)
        return json.dumps({"success": True, "project": new_project})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "launch_project","description": "Creates a new research project.","parameters": {"type": "object","properties": {"project_name": {"type": "string","description": "The name of the new project."},"lead_researcher_id": {"type": "string","description": "The user ID of the lead researcher."},"funding_source_id": {"type": "string","description": "The ID of the project's funding source."},"project_id_override": {"type": "string", "description": "Optional. A specific ID to assign to the new project for predictable referencing."}},"required": ["project_name", "lead_researcher_id", "funding_source_id"]}}}

class ModifySubmissionStatus(Tool):
    """Tool to update the status of a submission."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        new_status = kwargs.get('new_status')
        if not submission_id or not new_status:
            return json.dumps({"error": "submission_id and new_status are required."})

        submissions = data.get('submissions', [])
        for submission in submissions:
            if submission.get('submission_id') == submission_id:
                submission['status'] = new_status
                return json.dumps({"success": True, "submission_id": submission_id, "new_status": new_status})
        return json.dumps({"error": "Submission not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_submission_status",
                "description": "Updates the status of a submission (e.g., 'under_review', 'accepted', 'rejected').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string", "description": "The ID of the submission to update."},
                        "new_status": {"type": "string", "description": "The new status for the submission."}
                    },
                    "required": ["submission_id", "new_status"]
                }
            }
        }

class AppointReviewer(Tool):
    """Tool to assign a reviewer to a submission."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        reviewer_user_id = kwargs.get('reviewer_user_id')
        if not submission_id or not reviewer_user_id:
            return json.dumps({"error": "submission_id and reviewer_user_id are required."})

        submissions = data.get('submissions', [])
        for submission in submissions:
            if submission.get('submission_id') == submission_id:
                if 'assigned_reviewers' not in submission:
                    submission['assigned_reviewers'] = []
                if reviewer_user_id not in submission['assigned_reviewers']:
                    submission['assigned_reviewers'].append(reviewer_user_id)
                    return json.dumps({"success": True, "submission_id": submission_id, "reviewer_id": reviewer_user_id})
                else:
                    return json.dumps({"error": "Reviewer already assigned to this submission."})
        return json.dumps({"error": "Submission not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "appoint_reviewer",
                "description": "Assigns a researcher to review a submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string", "description": "The ID of the submission."},
                        "reviewer_user_id": {"type": "string", "description": "The user ID of the reviewer to assign."}
                    },
                    "required": ["submission_id", "reviewer_user_id"]
                }
            }
        }

class SubmitReview(Tool):
    """Tool to create a new review for a submission."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        reviewer_user_id = kwargs.get('reviewer_user_id')
        review_content = kwargs.get('review_content')
        recommendation = kwargs.get('recommendation')

        if not all([submission_id, reviewer_user_id, review_content, recommendation]):
            return json.dumps({"error": "submission_id, reviewer_user_id, review_content, and recommendation are required."})

        new_review = {
            "review_id": f"rev_{uuid.uuid4().hex[:4]}",
            "submission_id": submission_id,
            "reviewer_user_id": reviewer_user_id,
            "review_content": review_content,
            "recommendation": recommendation,
            "review_date": datetime.now().strftime('%Y-%m-%d')
        }
        data['reviews'].append(new_review)
        return json.dumps({"success": True, "review": new_review})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "submit_review",
                "description": "Creates a new review for a submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string", "description": "The ID of the submission being reviewed."},
                        "reviewer_user_id": {"type": "string", "description": "The user ID of the reviewer."},
                        "review_content": {"type": "string", "description": "The text content of the review."},
                        "recommendation": {"type": "string", "description": "The recommendation (e.g., 'accept', 'minor_revisions')."}
                    },
                    "required": ["submission_id", "reviewer_user_id", "review_content", "recommendation"]
                }
            }
        }

class GetReviewsForSubmission(Tool):
    """Tool to retrieve all reviews for a specific submission."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        if not submission_id:
            return json.dumps({"error": "submission_id is required."})

        reviews = data.get('reviews', [])
        submission_reviews = [review for review in reviews if review.get('submission_id') == submission_id]
        return json.dumps(submission_reviews, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_reviews_for_submission",
                "description": "Gets all reviews associated with a single submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string", "description": "The ID of the submission to get reviews for."}
                    },
                    "required": ["submission_id"]
                }
            }
        }

class ModifyProjectStatus(Tool):

    """Tool to update the status and/or end date of a research project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get('project_id')
        new_status = kwargs.get('new_status')
        end_date = kwargs.get('end_date') # Read the new optional parameter

        if not project_id or not (new_status or end_date):
            return json.dumps({"error": "project_id and either new_status or end_date are required."})

        projects = data.get('projects', [])
        for project in projects:
            if project.get('project_id') == project_id:
                if new_status:
                    project['status'] = new_status
                if end_date: # If end_date is provided, update it
                    project['end_date'] = end_date
                return json.dumps({"success": True, "project_id": project_id, "updated_fields": kwargs})
        return json.dumps({"error": "Project not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_project_status",
                "description": "Updates the status and/or end date of a research project (e.g., 'active', 'completed', 'on_hold').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "The ID of the project to update."},
                        "new_status": {"type": "string", "description": "The new status for the project."},
                        # Add end_date to the schema
                        "end_date": {"type": "string", "description": "The new end date for the project (e.g., 'YYYY-MM-DD')."}
                    },
                    "required": ["project_id"]
                }
            }
        }

class LinkArticleToProject(Tool):
    """Tool to link an article to a research project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get('project_id')
        article_id = kwargs.get('article_id')
        if not project_id or not article_id:
            return json.dumps({"error": "project_id and article_id are required."})

        projects = data.get('projects', [])
        for project in projects:
            if project.get('project_id') == project_id:
                if 'linked_articles' not in project:
                    project['linked_articles'] = []
                if article_id not in project['linked_articles']:
                    project['linked_articles'].append(article_id)
                    return json.dumps({"success": True, "project_id": project_id, "article_id": article_id})
                else:
                    return json.dumps({"error": "Article already linked to this project."})
        return json.dumps({"error": "Project not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_article_to_project",
                "description": "Links an existing article to a research project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "The ID of the project."},
                        "article_id": {"type": "string", "description": "The ID of the article to link."}
                    },
                    "required": ["project_id", "article_id"]
                }
            }
        }

class FindGrants(Tool):
    """
    Tool to search for funding sources by various criteria, OR to get a single source's details by its ID.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        funding_source_id = kwargs.get('funding_source_id')
        focus_area = kwargs.get('focus_area')
        status = kwargs.get('status')
        min_grant_amount = kwargs.get('min_grant_amount')

        sources = data.get('funding_sources', [])

        if funding_source_id:
            for source in sources:
                if source.get('funding_source_id') == funding_source_id:
                    return json.dumps(source, indent=2)
            return json.dumps({"error": f"Funding source with ID '{funding_source_id}' not found."})

        results = []
        for source in sources:
            area_match = not focus_area or focus_area.lower() in source.get('focus_area', '').lower()
            status_match = not status or status.lower() == source.get('status', '').lower()
            amount_match = not min_grant_amount or source.get('grant_amount', 0) >= int(min_grant_amount)

            if area_match and status_match and amount_match:
                results.append(source)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_grants",
                "description": "Searches for funding sources by criteria (focus area, status, amount), or retrieves a single source by its specific ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "funding_source_id": {"type": "string", "description": "The specific ID of the funding source to retrieve."},
                        "focus_area": {"type": "string", "description": "The research area the funding supports (e.g., 'AI')."},
                        "status": {"type": "string", "description": "The current status of the grant (e.g., 'available')."},
                        "min_grant_amount": {"type": "integer", "description": "The minimum amount of funding required."}
                    }
                }
            }
        }

class AssignFundingToProject(Tool):
    """Tool to assign a funding source to a project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get('project_id')
        funding_source_id = kwargs.get('funding_source_id')
        if not project_id or not funding_source_id:
            return json.dumps({"error": "project_id and funding_source_id are required."})

        projects = data.get('projects', [])
        for project in projects:
            if project.get('project_id') == project_id:
                project['funding_source_id'] = funding_source_id
                return json.dumps({"success": True, "project_id": project_id, "funding_source_id": funding_source_id})
        return json.dumps({"error": "Project not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_funding_to_project",
                "description": "Assigns a funding source to a research project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "The ID of the project to be funded."},
                        "funding_source_id": {"type": "string", "description": "The ID of the funding source."}
                    },
                    "required": ["project_id", "funding_source_id"]
                }
            }
        }

class AddResearcherToProjectTeam(Tool):
    """Tool to add a researcher to a project's team."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get('project_id')
        user_id = kwargs.get('user_id')
        if not project_id or not user_id:
            return json.dumps({"error": "project_id and user_id are required."})

        projects = data.get('projects', [])
        for project in projects:
            if project.get('project_id') == project_id:
                # This assumes the data model can be extended with a 'team_members' list.
                if 'team_members' not in project:
                    project['team_members'] = []
                if user_id not in project['team_members'] and user_id != project.get('lead_researcher_id'):
                    project['team_members'].append(user_id)
                    return json.dumps({"success": True, "message": f"User {user_id} added to project {project_id}."})
                else:
                    return json.dumps({"error": "User is already on the team or is the lead researcher."})
        return json.dumps({"error": "Project not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_researcher_to_project_team",
                "description": "Adds a researcher to the team of an existing project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "The ID of the project."},
                        "user_id": {"type": "string", "description": "The user ID of the researcher to add."}
                    },
                    "required": ["project_id", "user_id"]
                }
            }
        }

class CreateResearchLog(Tool):
    """Tool to create a research log entry for a researcher about an article."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        researcher_id = kwargs.get('researcher_id')
        article_id = kwargs.get('article_id')
        notes = kwargs.get('notes')
        relevance = kwargs.get('relevance')
        log_id_override = kwargs.get('log_id_override')

        if not all([researcher_id, article_id, notes, relevance]):
            return json.dumps({"error": "researcher_id, article_id, notes, and relevance are required."})

        log_id = log_id_override if log_id_override else f"log_{uuid.uuid4().hex[:4]}"
        new_log = {
            "log_id": log_id,
            "researcher_id": researcher_id,
            "article_id": article_id,
            "entry_date": datetime.now().strftime('%Y-%m-%d'),
            "notes": notes,
            "relevance": relevance
        }
        data['research_logs'].append(new_log)
        return json.dumps({"success": True, "log_entry": new_log})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_research_log",
                "description": "Creates a personal research log or note for a researcher about a specific article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "researcher_id": {"type": "string", "description": "The user ID of the researcher creating the log."},
                        "article_id": {"type": "string", "description": "The ID of the article the log is about."},
                        "notes": {"type": "string", "description": "The content of the research note."},
                        "relevance": {"type": "string", "description": "A relevance score (e.g., 'high', 'medium', 'low')."},
                        "log_id_override": {"type": "string", "description": "Optional specific ID for the log entry."}
                    },
                    "required": ["researcher_id", "article_id", "notes", "relevance"]
                }
            }
        }

class SearchResearchLogs(Tool):
    """Tool to search research logs."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        researcher_id = kwargs.get('researcher_id')
        article_id = kwargs.get('article_id')

        if not researcher_id and not article_id:
            return json.dumps({"error": "Either researcher_id or article_id is required."})

        logs = data.get('research_logs', [])
        results = [
            log for log in logs
            if (not researcher_id or log.get('researcher_id') == researcher_id)
            and (not article_id or log.get('article_id') == article_id)
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_research_logs",
                "description": "Searches research logs by researcher or article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "researcher_id": {"type": "string", "description": "The user ID of the researcher."},
                        "article_id": {"type": "string", "description": "The ID of the article."}
                    }
                }
            }
        }

class GetUserSubscriptions(Tool):
    """Tool to get a user's topic subscriptions."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        if not user_id:
            return json.dumps({"error": "user_id is required."})

        subscriptions = data.get('subscriptions', [])
        user_subs = [sub for sub in subscriptions if sub.get('user_id') == user_id]
        return json.dumps(user_subs, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_subscriptions",
                "description": "Retrieves the list of topics a specific user is subscribed to.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user whose subscriptions to retrieve."}
                    },
                    "required": ["user_id"]
                }
            }
        }

class UpdateUserSubscriptions(Tool):
    """Tool to add or remove a topic subscription for a user."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        topic = kwargs.get('topic')
        action = kwargs.get('action', 'add')  # 'add' or 'remove'
        if not user_id or not topic:
            return json.dumps({"error": "user_id and topic are required."})

        subscriptions = data.get('subscriptions', [])
        if action.lower() == 'add':
            # Check if subscription already exists
            for sub in subscriptions:
                if sub.get('user_id') == user_id and sub.get('topic', '').lower() == topic.lower():
                    return json.dumps({"success": True, "message": "User is already subscribed to this topic."})
            new_sub = {
                "subscription_id": f"sub_topic_{uuid.uuid4().hex[:4]}",
                "user_id": user_id,
                "topic": topic
            }
            subscriptions.append(new_sub)
            return json.dumps({"success": True, "subscription": new_sub})
        elif action.lower() == 'remove':
            initial_len = len(subscriptions)
            data['subscriptions'] = [
                sub for sub in subscriptions
                if not (sub.get('user_id') == user_id and sub.get('topic', '').lower() == topic.lower())
            ]
            if len(data['subscriptions']) < initial_len:
                return json.dumps({"success": True, "message": f"Subscription to topic '{topic}' removed for user {user_id}."})
            else:
                return json.dumps({"error": "Subscription not found."})
        else:
            return json.dumps({"error": "Invalid action. Must be 'add' or 'remove'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_subscriptions",
                "description": "Adds or removes a topic subscription for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to update."},
                        "topic": {"type": "string", "description": "The topic to subscribe or unsubscribe from (e.g., 'AI')."},
                        "action": {"type": "string", "description": "The action to perform: 'add' or 'remove'. Defaults to 'add'."}
                    },
                    "required": ["user_id", "topic"]
                }
            }
        }

class UpdateUserPreferences(Tool):
    """Tool to update a user's preferences."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        notification_channel = kwargs.get('notification_channel')
        ui_theme = kwargs.get('ui_theme')
        if not user_id or not (notification_channel or ui_theme):
            return json.dumps({"error": "user_id and at least one preference to update are required."})

        preferences = data.get('user_preferences', [])
        for pref in preferences:
            if pref.get('user_id') == user_id:
                if notification_channel:
                    pref['notification_channel'] = notification_channel
                if ui_theme:
                    pref['ui_theme'] = ui_theme
                return json.dumps({"success": True, "updated_preferences": pref})

        # If no preferences found, create one
        new_pref = {"preference_id": f"pref_{uuid.uuid4().hex[:4]}", "user_id": user_id}
        if notification_channel:
            new_pref['notification_channel'] = notification_channel
        if ui_theme:
            new_pref['ui_theme'] = ui_theme
        preferences.append(new_pref)
        return json.dumps({"success": True, "created_preferences": new_pref})


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_preferences",
                "description": "Updates a user's preferences, such as notification channel or UI theme.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID whose preferences to update."},
                        "notification_channel": {"type": "string", "description": "The preferred notification channel (e.g., 'email', 'in_app', 'none')."},
                        "ui_theme": {"type": "string", "description": "The preferred UI theme (e.g., 'light', 'dark')."}
                    },
                    "required": ["user_id"]
                }
            }
        }

class NotifyUser(Tool):
    """Tool to send a notification to a user."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        recipient_user_id = kwargs.get('recipient_user_id')
        message_content = kwargs.get('message_content')
        sender_user_id = kwargs.get('sender_user_id', 'system')
        if not recipient_user_id or not message_content:
            return json.dumps({"error": "recipient_user_id and message_content are required."})

        new_notification = {
            "notification_id": f"notif_{uuid.uuid4().hex[:4]}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message_content,
            "timestamp": datetime.now().isoformat() + "Z",
            "status": "unread"
        }
        data['notifications'].append(new_notification)
        return json.dumps({"success": True, "notification": new_notification})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "notify_user",
                "description": "Sends a notification to a user within the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {"type": "string", "description": "The user ID of the recipient."},
                        "message_content": {"type": "string", "description": "The content of the notification message."},
                        "sender_user_id": {"type": "string", "description": "The user ID of the sender. Defaults to 'system'."}
                    },
                    "required": ["recipient_user_id", "message_content"]
                }
            }
        }

class FindPublications(Tool):
    """Tool to search for articles based on various criteria."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        title = kwargs.get('title')
        author_name = kwargs.get('author_name')
        topic = kwargs.get('topic')
        publication_year = kwargs.get('publication_year')
        article_id = kwargs.get('article_id')

        if not any([title, author_name, topic, publication_year, article_id]):
            return json.dumps({"error": "At least one search parameter is required."})

        articles = data.get('articles', [])
        results = []
        for article in articles:
            title_match = not title or title.lower() in article.get('title', '').lower()
            author_match = not author_name or any(author_name.lower() in author.lower() for author in article.get('authors', []))
            topic_match = not topic or topic.lower() == article.get('topic', '').lower()
            year_match = not publication_year or str(publication_year) == str(article.get('publication_year'))
            id_match = not article_id or article_id == article.get('article_id')

            if all([title_match, author_match, topic_match, year_match, id_match]):
                results.append(article)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_publications",
                "description": "Searches for articles by title, author, topic, or publication year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "The title or a keyword from the title of the article."},
                        "author_name": {"type": "string", "description": "The name of one of the authors."},
                        "topic": {"type": "string", "description": "The main topic of the article (e.g., 'AI', 'Biomedicine')."},
                        "publication_year": {"type": "integer", "description": "The year the article was published."},
                        "article_id": {"type": "string", "description": "The exact ID of the article."}
                    }
                }
            }
        }

class SummarizeArticleText(Tool):
    """Tool to get a summary of an article."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        articles = data.get('articles', [])
        for article in articles:
            if article.get('article_id') == article_id:
                # This is a mock summary tool. In a real system, this would involve NLP.
                # Here, we just return the abstract, or a truncated part of the full text.
                summary = article.get('abstract', 'No abstract available.')
                if 'full_text' in article and len(summary) < 20:
                    summary = article['full_text'][:200] + "..."
                return json.dumps({"article_id": article_id, "summary": summary})
        return json.dumps({"error": "Article not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_article_text",
                "description": "Provides a concise summary of a given article's content.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string", "description": "The ID of the article to summarize."}
                    },
                    "required": ["article_id"]
                }
            }
        }

class FindReferences(Tool):
    """Tool to search for citations."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        direction = kwargs.get('direction', 'to')  # 'to' or 'from'
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        citations = data.get('citations', [])
        results = []
        if direction.lower() == 'to':
            # Find articles that CITED the given article_id
            results = [c for c in citations if c.get('cited_article_id') == article_id]
        elif direction.lower() == 'from':
            # Find articles that ARE CITED BY the given article_id
            results = [c for c in citations if c.get('source_article_id') == article_id]
        else:
            return json.dumps({"error": "Invalid direction. Must be 'to' or 'from'."})
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_references",
                "description": "Searches for citations. Can find which articles cited a given article, or which articles a given article cited.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string", "description": "The ID of the article to search citations for."},
                        "direction": {"type": "string", "description": "Search direction: 'to' (who cited this article) or 'from' (who did this article cite). Defaults to 'to'."}
                    },
                    "required": ["article_id"]
                }
            }
        }

class FindProjects(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get('project_id')
        if project_id:
            for project in data.get('projects', []):
                if project.get('project_id') == project_id:
                    return json.dumps(project, indent=2)
            return json.dumps({"error": f"Project with ID '{project_id}' not found."})

        project_name = kwargs.get('project_name')
        lead_researcher_id = kwargs.get('lead_researcher_id')
        status = kwargs.get('status')
        end_date_year = kwargs.get('end_date_year') # New parameter

        # Add new parameter to the validation check
        if not any([project_name, lead_researcher_id, status, end_date_year]):
            return json.dumps({"error": "At least one search parameter (project_name, lead_researcher_id, status, or end_date_year) is required for a general search."})

        projects = data.get('projects', [])
        results = []
        for project in projects:
            name_match = not project_name or project_name.lower() in project.get('project_name', '').lower()
            lead_match = not lead_researcher_id or lead_researcher_id == project.get('lead_researcher_id')
            status_match = not status or status.lower() == project.get('status', '').lower()

            # Add year matching logic
            project_end_date = project.get('end_date')
            year_match = (not end_date_year or
                          (project_end_date and project_end_date.startswith(str(end_date_year))))

            # Add year_match to the final condition
            if name_match and lead_match and status_match and year_match:
                results.append(project)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_projects",
                "description": "Searches for projects by various criteria OR retrieves a single project by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "The specific ID of the project to retrieve."},
                        "project_name": {"type": "string", "description": "The name of the project."},
                        "lead_researcher_id": {"type": "string", "description": "The user ID of the lead researcher."},
                        "status": {"type": "string", "description": "The current status of the project."},
                        # Add new parameter to the schema
                        "end_date_year": {"type": "integer", "description": "The year the project ended, to filter by completion year."}
                    }
                }
            }
        }

class GetUserPreferences(Tool):
    """Tool to retrieve the preference settings for a specific user."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        if not user_id:
            return json.dumps({"error": "user_id is required."})

        preferences = data.get('user_preferences', [])
        for pref in preferences:
            if pref.get('user_id') == user_id:
                return json.dumps(pref, indent=2)
        return json.dumps({"error": "Preferences not found for the given user ID."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_preferences",
                "description": "Retrieves the preference settings (like notification channel and UI theme) for a single user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user to retrieve preferences for."}
                    },
                    "required": ["user_id"]
                }
            }
        }

class LookupSubmissions(Tool):
    """
    Tool to search for submissions based on various criteria OR retrieve a single one by ID.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        article_id = kwargs.get('article_id')
        author_user_id = kwargs.get('author_user_id')
        status = kwargs.get('status')

        submissions = data.get('submissions', [])

        if submission_id:
            for sub in submissions:
                if sub.get('submission_id') == submission_id:
                    return json.dumps(sub, indent=2)
            return json.dumps({"error": f"Submission with ID '{submission_id}' not found."})

        if article_id:
            for sub in submissions:
                if sub.get('article_id') == article_id:
                    return json.dumps(sub, indent=2)
            return json.dumps({"error": f"No submission found for article ID '{article_id}'."})

        if not any([author_user_id, status]):
            return json.dumps(submissions, indent=2)

        results = []
        for sub in submissions:
            author_match = not author_user_id or author_user_id == sub.get('author_user_id')
            status_match = not status or status.lower() == sub.get('status', '').lower()

            if author_match and status_match:
                results.append(sub)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "lookup_submissions",
                "description": "Searches for submissions by various criteria, or retrieves a single submission by its specific ID or associated article ID. Returns all submissions if no criteria are given.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string", "description": "The specific ID of the submission to retrieve."},
                        "article_id": {"type": "string", "description": "The ID of the article to find the submission for."},
                        "author_user_id": {"type": "string", "description": "The user ID of the submission's author."},
                        "status": {"type": "string", "description": "The current status of the submission (e.g., 'under_review')."}
                    }
                }
            }
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
    LookupSubmissions()
]
