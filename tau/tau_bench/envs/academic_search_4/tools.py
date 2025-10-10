import json
import uuid
from datetime import datetime
from typing import Any, Dict
from collections import Counter
import re

from domains.dto import Tool

class FetchArticles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        topic = kwargs.get('topic')
        title = kwargs.get('title')
        year = kwargs.get('year')
        author_name = kwargs.get('author_name')

        articles: list = data.get('articles', [])

        if article_id:
            for article in articles:
                if article.get('article_id') == article_id:
                    return json.dumps([article], indent=2) # Return list with one item for consistency
            return json.dumps([]) # Return empty list if not found

        results = []
        for article in articles:
            match = True
            if topic and topic.lower() not in article.get('topic', '').lower(): match = False
            if title and title.lower() not in article.get('title', '').lower(): match = False
            if author_name and author_name.lower() not in article.get('author_name', '').lower(): match = False
            if year and year != article.get('publication_year'): match = False
            if match: results.append(article)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "fetch_articles","description": "Searches for academic articles by ID, topic, title, or publication year.","parameters": {"type": "object","properties": {"article_id": {"type": "string","description": "The unique ID of the article."}, "topic": {"type": "string","description": "A topic to search for (e.g., 'AI', 'Biology')."},"title": {"type": "string","description": "A keyword or phrase from the article title."},"year": {"type": "integer","description": "A specific publication year to filter by."}},"required": []}}}

class FetchUsers(Tool):
    """Tool to search for users by ID, name, or research field."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        name = kwargs.get('name')
        research_field = kwargs.get('research_field')

        users = data.get('users', [])

        if user_id:
            for user in users:
                if user.get('user_id') == user_id:
                    return json.dumps([user], indent=2)
            return json.dumps([])

        if not name and not research_field:
            return json.dumps({"error": "Either user_id, name, or research_field is required."})

        results = []
        for user in users:
            match = True
            if name and name.lower() not in user.get('name', '').lower():
                match = False
            if research_field and research_field.lower() not in user.get('research_field', '').lower():
                match = False
            if match:
                results.append(user)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "fetch_users","description": "Searches for users by their name or research field.","parameters": {"type": "object","properties": {"name": {"type": "string", "description": "The name of the user to search for."}, "research_field": {"type": "string", "description": "The research field of the user."}}}}}

class CreateReviewSubmission(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        author_user_id,article_id = kwargs.get('author_user_id'),kwargs.get('article_id')
        submission_id_override = kwargs.get('submission_id_override')

        if not author_user_id or not article_id:
            return json.dumps({"error": "author_user_id and article_id are required."})
        if not any(u['user_id'] == author_user_id for u in data.get('users', [])):
            return json.dumps({"error": f"Author with ID '{author_user_id}' not found."})
        if not any(a['article_id'] == article_id for a in data.get('articles', [])):
            return json.dumps({"error": f"Article with ID '{article_id}' not found."})

        new_submission_id = submission_id_override if submission_id_override else f"sub_{uuid.uuid4().hex[:4]}"

        new_submission = {"submission_id": new_submission_id,"article_id": article_id,"author_user_id": author_user_id,"submission_date": datetime.now().strftime('%Y-%m-%d'),"status": "submitted","assigned_reviewers": []}
        data['submissions'].append(new_submission)
        return json.dumps({"success": True, "submission": new_submission})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "create_review_submission","description": "Submits an author's article to the peer review system.","parameters": {"type": "object","properties": {"author_user_id": {"type": "string", "description": "The user ID of the author."}, "article_id": {"type": "string", "description": "The ID of the article being submitted."}, "submission_id_override": {"type": "string", "description": "Optional. A specific ID to assign to the new submission."}},"required": ["author_user_id", "article_id"]}}}

class AssignReviewer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        reviewer_user_id = kwargs.get('reviewer_user_id')
        overwrite = kwargs.get('overwrite', False)

        submissions = data.get('submissions', [])
        for sub in submissions:
            if sub['submission_id'] == submission_id:
                if overwrite:
                    sub['assigned_reviewers'] = [reviewer_user_id]
                else:
                    if reviewer_user_id not in sub['assigned_reviewers']:
                        sub['assigned_reviewers'].append(reviewer_user_id)

                sub['status'] = 'under_review'
                return json.dumps({"success": True, "submission": sub})
        return json.dumps({"error": f"Submission with ID '{submission_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "assign_reviewer","description": "Assigns a reviewer to an article submission, with an option to overwrite the existing list.","parameters": {"type": "object","properties": {"submission_id": {"type": "string", "description": "The ID of the submission."}, "reviewer_user_id": {"type": "string", "description": "The user ID of the person assigned to review."}, "overwrite": {"type": "boolean", "description": "If true, replaces the reviewer list. Defaults to false (append)."}},"required": ["submission_id", "reviewer_user_id"]}}}

class FetchSubmissionInfo(Tool):
    """Tool to get submission details for an article or by submission ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        submission_id = kwargs.get('submission_id')

        if not article_id and not submission_id:
            return json.dumps({"error": "Either article_id or submission_id is required."})

        submissions = data.get('submissions', [])
        for sub in submissions:
            if (article_id and sub.get('article_id') == article_id) or \
               (submission_id and sub.get('submission_id') == submission_id):
                return json.dumps(sub, indent=2)

        if article_id:
            return json.dumps({"error": f"No submission found for article ID '{article_id}'."})
        else:
            return json.dumps({"error": f"No submission found for submission ID '{submission_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "fetch_submission_info","description": "Gets the submission details for a given article ID or submission ID.","parameters": {"type": "object","properties": {"article_id": {"type": "string", "description": "The ID of the article to find the submission for."}, "submission_id": {"type": "string", "description": "The ID of the submission to find."}}}}}

class IdentifyPotentialReviewers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        exclude_user_ids = kwargs.get('exclude_user_ids', [])

        if not article_id:
            return json.dumps({"error": "article_id is required."})

        articles = data.get('articles', [])
        target_article = next((a for a in articles if a.get('article_id') == article_id), None)
        if not target_article:
            return json.dumps({"error": f"Article with ID '{article_id}' not found."})

        article_topic = target_article.get('topic')
        if not article_topic:
            return json.dumps({"error": f"Article with ID '{article_id}' has no topic specified."})

        users = data.get('users', [])
        potential_reviewers = [
            user for user in users
            if user.get('research_field') == article_topic and user.get('user_id') not in exclude_user_ids
        ]

        return json.dumps(potential_reviewers, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "identify_potential_reviewers", "description": "Identifies potential reviewers for an article based on matching research fields.", "parameters": {"type": "object", "properties": {"article_id": {"type": "string", "description": "The ID of the article needing reviewers."}, "exclude_user_ids": {"type": "array", "items": {"type": "string"}, "description": "A list of user IDs to exclude from the suggestions (e.g., the authors)."}},"required": ["article_id"]}}}

class PostNewReview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        reviewer_user_id = kwargs.get('reviewer_user_id')
        recommendation = kwargs.get('recommendation')
        comments = kwargs.get('comments')

        if not all([submission_id, reviewer_user_id, recommendation, comments]):
            return json.dumps({"error": "submission_id, reviewer_user_id, recommendation, and comments are required."})

        new_review = {"review_id": f"rev_{uuid.uuid4().hex[:4]}", "submission_id": submission_id, "reviewer_user_id": reviewer_user_id, "recommendation": recommendation, "review_content": comments, "review_date": datetime.now().strftime('%Y-%m-%d')}
        data['reviews'].append(new_review)
        return json.dumps({"success": True, "review": new_review})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "post_new_review", "description": "Posts a new peer review for a submission.", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string", "description": "The ID of the submission being reviewed."}, "reviewer_user_id": {"type": "string", "description": "The user ID of the reviewer."}, "recommendation": {"type": "string", "description": "The recommendation (e.g., 'accept', 'minor_revisions', 'reject')."}, "comments": {"type": "string", "description": "The detailed comments of the review."}}, "required": ["submission_id", "reviewer_user_id", "recommendation", "comments"]}}}

class SetSubmissionOutcome(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        new_status = kwargs.get('new_status')

        if not all([submission_id, new_status]):
            return json.dumps({"error": "submission_id and new_status are required."})

        submissions = data.get('submissions', [])
        for sub in submissions:
            if sub.get('submission_id') == submission_id:
                sub['status'] = new_status
                return json.dumps({"success": True, "submission": sub})
        return json.dumps({"error": f"Submission with ID '{submission_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_submission_outcome", "description": "Sets the outcome or status for a submission (e.g., 'accepted', 'rejected').", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string", "description": "The ID of the submission to update."}, "new_status": {"type": "string", "description": "The new status to set for the submission."}}, "required": ["submission_id", "new_status"]}}}

class ConnectRevisedVersion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        revised_article_id = kwargs.get('revised_article_id')

        if not all([submission_id, revised_article_id]):
            return json.dumps({"error": "submission_id and revised_article_id are required."})

        submissions = data.get('submissions', [])
        for sub in submissions:
            if sub.get('submission_id') == submission_id:
                sub['revised_version_article_id'] = revised_article_id
                return json.dumps({"success": True, "submission": sub})
        return json.dumps({"error": f"Submission with ID '{submission_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "connect_revised_version", "description": "Connects a revised version of an article to an original submission record.", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string", "description": "The ID of the original submission."}, "revised_article_id": {"type": "string", "description": "The article ID of the new, revised version."}}, "required": ["submission_id", "revised_article_id"]}}}

class AlertUser(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        recipient_user_id = kwargs.get('recipient_user_id')
        message = kwargs.get('message')
        sender_user_id = kwargs.get('sender_user_id', 'system')

        if not all([recipient_user_id, message]):
            return json.dumps({"error": "recipient_user_id and message are required."})

        new_notification = {"notification_id": f"notif_{uuid.uuid4().hex[:4]}", "recipient_user_id": recipient_user_id, "sender_user_id": sender_user_id, "message_content": message, "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'), "status": "unread"}
        data['notifications'].append(new_notification)
        return json.dumps({"success": True, "notification": new_notification})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "alert_user", "description": "Sends a direct alert message to a user.", "parameters": {"type": "object", "properties": {"recipient_user_id": {"type": "string", "description": "The ID of the user to receive the alert."}, "message": {"type": "string", "description": "The content of the alert message."}, "sender_user_id": {"type": "string", "description": "Optional. The user ID of the sender. Defaults to 'system'."}}, "required": ["recipient_user_id", "message"]}}}

class AdjustUserSettings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        if not user_id:
            return json.dumps({"error": "user_id is required."})

        notification_channel = kwargs.get('notification_channel')
        ui_theme = kwargs.get('ui_theme')
        research_field = kwargs.get('research_field')

        if not notification_channel and not ui_theme and not research_field:
            return json.dumps({"error": "At least one setting (notification_channel, ui_theme, or research_field) must be provided."})

        preferences = data.get('user_preferences', [])

        pref_found = False
        for pref in preferences:
            if pref.get('user_id') == user_id:
                if notification_channel:
                    pref['notification_channel'] = notification_channel
                if ui_theme:
                    pref['ui_theme'] = ui_theme
                pref_found = True
                break

        if not pref_found:
            new_pref = {
                "preference_id": f"pref_{uuid.uuid4().hex[:4]}",
                "user_id": user_id,
                "notification_channel": notification_channel if notification_channel else "none", # Default value
                "preferred_email": "", # Assuming an empty default
                "ui_theme": ui_theme if ui_theme else "light" # Default value
            }
            data['user_preferences'].append(new_pref)
            pref = new_pref
            pref_found = True

        user_obj = None
        for user in data.get('users', []):
            if user.get('user_id') == user_id:
                if research_field:
                    user['research_field'] = research_field
                user_obj = user
                break

        if pref_found or user_obj:
            if research_field and user_obj: # Se research_field foi modificado, retorna o objeto user
                return json.dumps({"success": True, "user": user_obj})
            elif pref_found: # Senão, retorna as preferências (se foram modificadas/criadas)
                return json.dumps({"success": True, "settings": pref})

        return json.dumps({"error": f"Settings for user ID '{user_id}' not found and could not be created."})


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "adjust_user_settings","description": "Adjusts a user's personal settings.","parameters": {"type": "object","properties": {"user_id": {"type": "string","description": "The user ID for whom to adjust settings."}, "notification_channel": {"type": "string","description": "The new notification channel (e.g., 'email', 'in_app', 'none')."}, "ui_theme": {"type": "string","description": "The new UI theme (e.g., 'dark', 'light')."}, "research_field": {"type": "string", "description": "The new primary research field for the user."}},"required": ["user_id"]}}}

class SetTopicInterest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id, topic, action = kwargs.get('user_id'), kwargs.get('topic'), kwargs.get('action')
        if not all([user_id, topic, action]):
            return json.dumps({"error": "user_id, topic, and action are required."})

        subscriptions = data.get('subscriptions', [])
        if action.lower() == 'add':
            if any(s.get('user_id') == user_id and s.get('topic') == topic for s in subscriptions):
                return json.dumps({"success": False, "message": "User is already subscribed to this topic."})
            new_sub = {"subscription_id": f"sub_topic_{uuid.uuid4().hex[:4]}", "user_id": user_id, "topic": topic}
            subscriptions.append(new_sub)
            return json.dumps({"success": True, "subscription": new_sub})
        elif action.lower() == 'remove':
            initial_count = len(subscriptions)
            data['subscriptions'] = [s for s in subscriptions if not (s.get('user_id') == user_id and s.get('topic') == topic)]
            if len(data['subscriptions']) < initial_count:
                return json.dumps({"success": True, "message": f"Subscription to topic '{topic}' removed."})
            else:
                return json.dumps({"error": "Subscription not found to remove."})
        else:
            return json.dumps({"error": "Invalid action. Must be 'add' or 'remove'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_topic_interest", "description": "Sets a user's interest in a topic by adding or removing a subscription.", "parameters": {"type": "object", "properties": {"user_id": {"type": "string", "description": "The user ID."}, "topic": {"type": "string", "description": "The research topic."}, "action": {"type": "string", "enum": ["add", "remove"], "description": "The action to perform."}}, "required": ["user_id", "topic", "action"]}}}

class RegisterNewArticle(Tool):
    """Registers a new article manuscript in the system."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        title = kwargs.get('title')
        authors = kwargs.get('authors')
        topic = kwargs.get('topic')
        abstract = kwargs.get('abstract')
        article_id_override = kwargs.get('article_id_override')

        if not all([title, authors, topic, abstract]):
            return json.dumps({"error": "title, authors, topic, and abstract are required."})

        new_article_id = article_id_override if article_id_override else f"art_{uuid.uuid4().hex[:4]}"

        new_article = {
            "article_id": new_article_id,
            "title": title,
            "authors": authors,
            "publication_year": datetime.now().year,
            "topic": topic,
            "abstract": abstract,
            "status": "draft",
            "full_text": kwargs.get('full_text', '')
        }
        data['articles'].append(new_article)
        return json.dumps({"success": True, "article": new_article})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "register_new_article", "description": "Registers a new article manuscript in the system.", "parameters": {"type": "object", "properties": {"title": {"type": "string"}, "authors": {"type": "array", "items": {"type": "string"}}, "topic": {"type": "string"}, "abstract": {"type": "string"}, "article_id_override": {"type": "string", "description": "Optional. A specific ID to assign to the new article for predictable referencing."}}, "required": ["title", "authors", "topic", "abstract"]}}}

class ReviseArticleDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        article = next((a for a in data.get('articles', []) if a.get('article_id') == article_id), None)
        if not article:
            return json.dumps({"error": f"Article with ID '{article_id}' not found."})

        updatable_fields = ['title', 'abstract', 'topic', 'status']
        for key, value in kwargs.items():
            if key in updatable_fields:
                article[key] = value

        return json.dumps({"success": True, "article": article})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "revise_article_details", "description": "Revises details of an existing article, such as its abstract or status.", "parameters": {"type": "object", "properties": {"article_id": {"type": "string", "description": "The ID of the article to revise."}, "title": {"type": "string", "description": "The new title for the article."}, "abstract": {"type": "string", "description": "The new abstract for the article."}, "topic": {"type": "string", "description": "The new topic for the article."}, "status": {"type": "string", "description": "The new status for the article."}}, "required": ["article_id"]}}}

class ListReviewsForSubmission(Tool):
    """Lista todas as avaliações submetidas para uma submissão específica."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        if not submission_id:
            return json.dumps({"error": "submission_id is required."})

        reviews = data.get('reviews', [])
        submission_reviews = [r for r in reviews if r.get('submission_id') == submission_id]

        return json.dumps(submission_reviews, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_reviews_for_submission", "description": "Lists all submitted reviews for a specific submission ID.", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string", "description": "The ID of the submission to get reviews for."}}, "required": ["submission_id"]}}}

class CreateNewProject(Tool):
    """Creates a new research project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_name = kwargs.get('project_name')
        lead_researcher_id = kwargs.get('lead_researcher_id')
        project_id_override = kwargs.get('project_id_override')

        if not all([project_name, lead_researcher_id]):
            return json.dumps({"error": "project_name and lead_researcher_id are required."})

        new_project_id = project_id_override if project_id_override else f"proj_{uuid.uuid4().hex[:4]}"

        new_project = {
            "project_id": new_project_id,
            "project_name": project_name,
            "lead_researcher_id": lead_researcher_id,
            "status": "active",
            "start_date": datetime.now().strftime('%Y-%m-%d'),
            "end_date": None,
            "linked_articles": kwargs.get('linked_article_ids', [])
        }
        data['projects'].append(new_project)
        return json.dumps({"success": True, "project": new_project})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_new_project", "description": "Creates a new research project.", "parameters": {"type": "object", "properties": {"project_name": {"type": "string"}, "lead_researcher_id": {"type": "string"}, "linked_article_ids": {"type": "array", "items": {"type": "string"}}, "project_id_override": {"type": "string", "description": "Optional. A specific ID to assign to the new project."}}, "required": ["project_name", "lead_researcher_id"]}}}

class GetArticleKeywords(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        article = next((a for a in data.get('articles', []) if a.get('article_id') == article_id), None)
        if not article or not article.get('abstract'):
            return json.dumps([])

        text = article.get('abstract', '').lower()
        words = re.findall(r'\b\w+\b', text)
        stop_words = {'a', 'an', 'the', 'in', 'of', 'for', 'is', 'on', 'and', 'to', 'with', 'by', 'as', 'its', 'we', 'this'}
        meaningful_words = [word for word in words if word not in stop_words and not word.isdigit()]

        top_keywords = [word for word, count in Counter(meaningful_words).most_common(5)]

        return json.dumps(top_keywords)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_article_keywords", "description": "Identifies potential keywords from an article's abstract based on word frequency.", "parameters": {"type": "object", "properties": {"article_id": {"type": "string", "description": "The ID of the article to extract keywords from."}}, "required": ["article_id"]}}}

class FindCitations(Tool):
    """Finds all articles that cite a given article."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        citations = data.get('citations', [])
        citing_articles = [c.get('source_article_id') for c in citations if c.get('cited_article_id') == article_id]

        return json.dumps(citing_articles, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_citations", "description": "Finds all articles that cite a given article ID.", "parameters": {"type": "object", "properties": {"article_id": {"type": "string", "description": "The ID of the article to find citations for."}}, "required": ["article_id"]}}}

class UpdateProjectDetails(Tool):
    """Updates the details of an existing research project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get('project_id')
        if not project_id:
            return json.dumps({"error": "project_id is required."})

        project = next((p for p in data.get('projects', []) if p.get('project_id') == project_id), None)
        if not project:
            return json.dumps({"error": f"Project with ID '{project_id}' not found."})

        updatable_fields = ['project_name', 'status', 'linked_article_ids']
        for key, value in kwargs.items():
            if key in updatable_fields:
                project[key] = value

        return json.dumps({"success": True, "project": project})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_project_details", "description": "Updates details of an existing project, such as its name or linked articles.", "parameters": {"type": "object", "properties": {"project_id": {"type": "string", "description": "The ID of the project to update."}, "project_name": {"type": "string", "description": "The new name for the project."}, "status": {"type": "string", "description": "The new status for the project."}, "linked_article_ids": {"type": "array", "items": {"type": "string"}, "description": "A new list of linked article IDs."}}, "required": ["project_id"]}}}

class RemoveReview(Tool):
    """Deletes a review record from the system."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        review_id = kwargs.get('review_id')
        if not review_id:
            return json.dumps({"error": "review_id is required."})

        reviews = data.get('reviews', [])
        original_count = len(reviews)
        # Note: In a real DB, this would be a direct delete. Here we filter the list.
        data['reviews'] = [r for r in reviews if r.get('review_id') != review_id]

        if len(data['reviews']) < original_count:
            return json.dumps({"success": True, "message": f"Review {review_id} has been deleted."})
        else:
            return json.dumps({"error": f"Review with ID '{review_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "remove_review", "description": "Deletes a specific review by its ID.", "parameters": {"type": "object", "properties": {"review_id": {"type": "string", "description": "The ID of the review to delete."}}, "required": ["review_id"]}}}

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
    RemoveReview()
]
