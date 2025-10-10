import json
import uuid
from datetime import datetime
from typing import Any, Dict
from domains.dto import Tool

class SearchUsers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Executes user search.
        - If 'user_id' is provided, returns the details of that specific user.
        - Otherwise, filters users by 'name' and/or 'research_field'.
        - If no parameters are provided, returns all users.
        """
        user_id = kwargs.get('user_id')
        name = kwargs.get('name')
        research_field = kwargs.get('research_field')

        users = data.get('users', [])

        # If a user_id is provided, it has priority and returns a single user.
        if user_id:
            for user in users:
                if user.get('user_id') == user_id:
                    return json.dumps(user, indent=2)
            return json.dumps({"error": f"User with ID '{user_id}' not found."})

        # If user_id is not provided, executes the search by other fields and returns a list.
        if not name and not research_field:
            return json.dumps(users, indent=2)

        results = [
            user for user in users
            if (not name or name.lower() in user.get('name', '').lower()) and
               (not research_field or research_field.lower() in user.get('research_field', '').lower())
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """
        Returns the function schema to be used by the language model.
        """
        return {
            "type": "function",
            "function": {
                "name": "search_users",
                "description": "Searches for users by ID, name, or research field. If a user_id is provided, returns the details of that user. Otherwise, returns a list of users that match the other criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user to retrieve details for."},
                        "name": {"type": "string", "description": "The name of the user to search for."},
                        "research_field": {"type": "string", "description": "The research field of the user."}
                    }
                }
            }
        }

class CreateLogEntry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id,article_id,notes,relevance,log_id_override = kwargs.get('user_id'),kwargs.get('article_id'),kwargs.get('notes'),kwargs.get('relevance', 'medium'),kwargs.get('log_id_override')

        if not all([user_id, notes]):
            return json.dumps({"error": "user_id and notes are required."})
        users, articles, logs = data.get('users', []), data.get('articles', []), data.get('research_logs', [])
        if not any(u['user_id'] == user_id for u in users):
            return json.dumps({"error": f"User with ID '{user_id}' not found."})

        if article_id:
            if not any(a['article_id'] == article_id for a in articles):
                return json.dumps({"error": f"Article with ID '{article_id}' not found."})
        new_log_id = log_id_override if log_id_override else f"log_{uuid.uuid4().hex[:4]}"
        if log_id_override and any(log['log_id'] == log_id_override for log in logs):
            return json.dumps({"error": f"A log entry with the override ID '{log_id_override}' already exists."})
        new_log_entry = {"log_id": new_log_id, "researcher_id": user_id, "article_id": article_id, "entry_date": datetime.now().strftime('%Y-%m-%d'), "notes": notes, "relevance": relevance}
        logs.append(new_log_entry)

        if article_id:
            for user in users:
                if user['user_id'] == user_id and article_id not in user['logged_articles']:
                    user['logged_articles'].append(article_id)
                    break
        return json.dumps({"success": True, "log_entry": new_log_entry})
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {"type": "function", "function": {"name": "create_log_entry", "description": "Creates a new entry in the research log for a specific user and optionally for an article.", "parameters": {"type": "object", "properties": {"user_id": {"type": "string", "description": "The ID of the researcher creating the log."}, "article_id": {"type": "string", "description": "The ID of the article being logged. This is optional."}, "notes": {"type": "string", "description": "The personal notes about the article or task."}, "relevance": {"type": "string", "description": "The relevance of the entry. E.g., 'high', 'medium', 'low'. Defaults to 'medium'."}, "log_id_override": {"type": "string", "description": "Optional. A specific ID to assign to the new log entry for predictable referencing."}}, "required": ["user_id", "notes"]}}}

class UpdateLogNotes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        log_id,new_notes = kwargs.get('log_id'),kwargs.get('new_notes')
        if not all([log_id, new_notes]):
            return json.dumps({"error": "log_id and new_notes are required."})
        for log in data.get('research_logs', []):
            if log['log_id'] == log_id:
                log['notes'] += f"\n[UPDATE]: {new_notes}"
                return json.dumps({"success": True, "log_entry": log})
        return json.dumps({"error": f"Log entry with ID '{log_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_log_notes", "description": "Appends new notes to an existing research log entry.", "parameters": {"type": "object", "properties": {"log_id": {"type": "string", "description": "The ID of the log entry to update."}, "new_notes": {"type": "string", "description": "The new notes to append to the existing log."}}, "required": ["log_id", "new_notes"]}}}

class GetLogDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        log_id = kwargs.get('log_id')
        if not log_id:
            return json.dumps({"error": "log_id is required."})
        for log in data.get('research_logs', []):
            if log['log_id'] == log_id:
                return log.get('notes', '')
        return json.dumps({"error": f"Log entry with ID '{log_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_log_details", "description": "Retrieves just the notes from a single log entry by its unique ID.", "parameters": {"type": "object", "properties": {"log_id": {"type": "string", "description": "The unique ID of the log entry to retrieve."}}, "required": ["log_id"]}}}

class UpdateArticleDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id, new_topic, new_status = kwargs.get('article_id'), kwargs.get('new_topic'), kwargs.get('new_status')
        if not article_id or (not new_topic and not new_status):
            return json.dumps({"error": "article_id and either new_topic or new_status are required."})
        for article in data.get('articles', []):
            if article['article_id'] == article_id:
                if new_topic:
                    article['topic'] = new_topic
                if new_status:
                    article['status'] = new_status
                return json.dumps({"success": True, "article": article})
        return json.dumps({"error": f"Article with ID '{article_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "update_article_details","description": "Updates the details (e.g., topic, status) of an article.","parameters": {"type": "object","properties": {"article_id": {"type": "string","description": "The ID of the article to update."},"new_topic": {"type": "string","description": "The new topic for the article."},"new_status": {"type": "string","description": "The new status for the article (e.g., 'new', 'processing', 'archived')."}},"required": ["article_id"]}}}

class GetSubmissionByArticle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        submissions = data.get('submissions', [])
        for submission in submissions:
            if submission.get('article_id') == article_id:
                return json.dumps(submission, indent=2)

        return json.dumps({"error": f"No submission found for article_id '{article_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_submission_by_article",
                "description": "Retrieves a submission's details using the ID of the article that was submitted.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string", "description": "The unique ID of the article to find the submission for."}
                    },
                    "required": ["article_id"]
                }
            }
        }

class SearchProjects(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Searches for research projects.
        - Filters by 'project_name' and/or 'funding_source_id'.
        - If no parameters are provided, returns all projects.
        """
        project_name = kwargs.get('project_name')
        funding_source_id = kwargs.get('funding_source_id')

        projects = data.get('projects', [])

        if not project_name and not funding_source_id:
            return json.dumps(projects, indent=2)

        results = [
            p for p in projects
            if (not project_name or project_name.lower() in p.get('project_name', '').lower()) and
               (not funding_source_id or p.get('funding_source_id') == funding_source_id)
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """
        Returns the function schema to be used by the language model.
        """
        return {
            "type": "function",
            "function": {
                "name": "search_projects",
                "description": "Searches for research projects by name or funding source ID. If no parameters are provided, returns all projects.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string", "description": "The name of the project to search for."},
                        "funding_source_id": {"type": "string", "description": "The ID of the funding source to filter projects."}
                    }
                }
            }
        }

class SearchFundingSources(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        source_name = kwargs.get('source_name')
        focus_area = kwargs.get('focus_area')
        status = kwargs.get('status')
        sources = data.get('funding_sources', [])

        if not source_name and not focus_area and not status:
            return json.dumps(sources, indent=2)

        results = [
            s for s in sources
            if (not source_name or source_name.lower() in s.get('source_name', '').lower()) and
               (not focus_area or s.get('focus_area', '').lower() == focus_area.lower()) and
               (not status or s.get('status', '').lower() == status.lower())
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_funding_sources",
                "description": "Searches for funding sources by name, focus area, or status. If no parameters are provided, it returns all sources.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {"type": "string", "description": "The name of the funding source to search for."},
                        "focus_area": {"type": "string", "description": "The focus area of the funding source (e.g., 'AI', 'Biomedicine')."},
                        "status": {"type": "string", "description": "The status of the funding source (e.g., 'available', 'depleted')."}
                    }
                }
            }
        }
class GetReviewBySubmission(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        if not submission_id:
            return json.dumps({"error": "submission_id is required."})

        reviews = data.get('reviews', [])
        for review in reviews:
            if review.get('submission_id') == submission_id:
                return json.dumps(review, indent=2)

        return json.dumps({"error": f"No review found for submission_id '{submission_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_review_by_submission", "description": "Retrieves a review's details using the ID of the submission.", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string", "description": "The unique ID of the submission to find the review for."}}, "required": ["submission_id"]}}}

class GetProjectDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get('project_id')
        if not project_id:
            return json.dumps({"error": "project_id is required."})

        projects = data.get('projects', [])
        for p in projects:
            if p.get('project_id') == project_id:
                return json.dumps(p, indent=2)

        return json.dumps({"error": f"Project with ID '{project_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_project_details", "description": "Retrieves the full details for a single project by its unique ID.", "parameters": {"type": "object", "properties": {"project_id": {"type": "string", "description": "The unique ID of the project to retrieve."}}, "required": ["project_id"]}}}

class AssignReviewerToSubmission(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        reviewer_user_id = kwargs.get('reviewer_user_id')
        if not all([submission_id, reviewer_user_id]):
            return json.dumps({"error": "submission_id and reviewer_user_id are required."})

        for sub in data.get('submissions', []):
            if sub['submission_id'] == submission_id:
                if reviewer_user_id not in sub['assigned_reviewers']:
                    sub['assigned_reviewers'].append(reviewer_user_id)
                return json.dumps({"success": True, "submission": sub})

        return json.dumps({"error": f"Submission with ID '{submission_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "assign_reviewer_to_submission", "description": "Assigns a reviewer to a submission.", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string", "description": "The ID of the submission to update."}, "reviewer_user_id": {"type": "string", "description": "The user ID of the reviewer to assign."}}, "required": ["submission_id", "reviewer_user_id"]}}}

class CreateProject(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_name = kwargs.get('project_name')
        lead_researcher_id = kwargs.get('lead_researcher_id')
        if not all([project_name, lead_researcher_id]):
            return json.dumps({"error": "project_name and lead_researcher_id are required."})

        project_id_override = kwargs.get('project_id_override')
        new_id = project_id_override if project_id_override else f"proj_{uuid.uuid4().hex[:4]}"

        if any(p['project_id'] == new_id for p in data.get('projects', [])):
            return json.dumps({"error": f"Project with ID '{new_id}' already exists."})

        new_project = {
            "project_id": new_id,
            "project_name": project_name,
            "lead_researcher_id": lead_researcher_id,
            "status": "active",
            "start_date": datetime.now().strftime('%Y-%m-%d'),
            "end_date": None,
            "linked_articles": kwargs.get('linked_articles', []),
            "funding_source_id": kwargs.get('funding_source_id')
        }
        data['projects'].append(new_project)
        return json.dumps({"success": True, "project": new_project})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_project", "description": "Creates a new research project.", "parameters": {"type": "object", "properties": {"project_name": {"type": "string", "description": "The name of the new project."}, "lead_researcher_id": {"type": "string", "description": "The user ID of the lead researcher."}, "project_id_override": {"type": "string", "description": "Optional. A specific ID to assign to the new project."}, "linked_articles": {"type": "array", "items": {"type": "string"}, "description": "Optional. A list of article IDs to link to the project."}, "funding_source_id": {"type": "string", "description": "Optional. The ID of the funding source for the project."}}, "required": ["project_name", "lead_researcher_id"]}}}

class GetCitationDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        citation_id = kwargs.get('citation_id')
        if not citation_id:
            return json.dumps({"error": "citation_id is required."})

        for citation in data.get('citations', []):
            if citation.get('citation_id') == citation_id:
                return json.dumps(citation, indent=2)

        return json.dumps({"error": f"Citation with ID '{citation_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_citation_details", "description": "Retrieves the full details for a single citation by its unique ID.", "parameters": {"type": "object", "properties": {"citation_id": {"type": "string", "description": "The unique ID of the citation to retrieve."}}, "required": ["citation_id"]}}}

class UpdateProjectLinks(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get('project_id')
        add_article_id = kwargs.get('add_article_id')
        if not all([project_id, add_article_id]):
            return json.dumps({"error": "project_id and add_article_id are required."})

        for project in data.get('projects', []):
            if project['project_id'] == project_id:
                if add_article_id not in project.get('linked_articles', []):
                    project['linked_articles'].append(add_article_id)
                return json.dumps({"success": True, "project": project})

        return json.dumps({"error": f"Project with ID '{project_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_project_links", "description": "Links an additional article to an existing project.", "parameters": {"type": "object", "properties": {"project_id": {"type": "string", "description": "The ID of the project to update."}, "add_article_id": {"type": "string", "description": "The ID of the article to link to the project."}}, "required": ["project_id", "add_article_id"]}}}

class UpdateSubmissionStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        new_status = kwargs.get('new_status')
        if not all([submission_id, new_status]):
            return json.dumps({"error": "submission_id and new_status are required."})

        for sub in data.get('submissions', []):
            if sub['submission_id'] == submission_id:
                sub['status'] = new_status
                return json.dumps({"success": True, "submission": sub})

        return json.dumps({"error": f"Submission with ID '{submission_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_submission_status", "description": "Updates the status of a submission (e.g., 'under_review', 'revising').", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string", "description": "The ID of the submission to update."}, "new_status": {"type": "string", "description": "The new status to set for the submission."}}, "required": ["submission_id", "new_status"]}}}

class GetSubmissionDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        if not submission_id:
            return json.dumps({"error": "submission_id is required."})

        submissions = data.get('submissions', [])
        for sub in submissions:
            if sub.get('submission_id') == submission_id:
                return json.dumps(sub, indent=2)

        return json.dumps({"error": f"Submission with ID '{submission_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_submission_details",
                "description": "Retrieves the full details for a single submission by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string", "description": "The unique ID of the submission to retrieve."}
                    },
                    "required": ["submission_id"]
                }
            }
        }

class UpdateProjectStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get('project_id')
        new_status = kwargs.get('new_status')
        new_end_date = kwargs.get('new_end_date')

        if not project_id or not new_status:
            return json.dumps({"error": "project_id and new_status are required."})

        for project in data.get('projects', []):
            if project['project_id'] == project_id:
                project['status'] = new_status
                if new_end_date is not None:
                    project['end_date'] = new_end_date
                else:
                    project['end_date'] = None
                return json.dumps({"success": True, "project": project})
        return json.dumps({"error": f"Project with ID '{project_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_project_status",
                "description": "Updates the status of a project (e.g., 'active', 'completed') and can optionally update its end date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "The ID of the project to update."},
                        "new_status": {"type": "string", "description": "The new status to set for the project."},
                        "new_end_date": {"type": "string", "description": "Optional. The new end date for the project in YYYY-MM-DD format."}
                    },
                    "required": ["project_id", "new_status"]
                }
            }
        }

class CreateCitation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        source_article_id = kwargs.get('source_article_id')
        cited_article_id = kwargs.get('cited_article_id')
        context = kwargs.get('citation_context', 'No context provided.')
        if not all([source_article_id, cited_article_id]):
            return json.dumps({"error": "source_article_id and cited_article_id are required."})

        new_id = f"cit_{uuid.uuid4().hex[:4]}"
        new_citation = {
            "citation_id": new_id,
            "source_article_id": source_article_id,
            "cited_article_id": cited_article_id,
            "citation_context": context
        }
        data['citations'].append(new_citation)
        return json.dumps({"success": True, "citation": new_citation})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_citation", "description": "Creates a new citation, linking a source article to a cited article.", "parameters": {"type": "object", "properties": {"source_article_id": {"type": "string", "description": "The ID of the article making the citation."}, "cited_article_id": {"type": "string", "description": "The ID of the article being cited."}, "citation_context": {"type": "string", "description": "The sentence or context in which the citation is made."}}, "required": ["source_article_id", "cited_article_id"]}}}

class SearchCitations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Searches for citations related to a specific article.
        - The search direction ('to' or 'from') is required.
        - 'to': Finds all citations that point TO the article_id.
        - 'from': Finds all citations made BY the article_id.
        """
        article_id = kwargs.get('article_id')
        direction = kwargs.get('direction')

        if not all([article_id, direction]):
            return json.dumps({"error": "article_id and direction are required."})

        citations = data.get('citations', [])
        results = []

        if direction.lower() == 'to':
            keyword = kwargs.get('context_keyword', '').lower()
            results = [
                c for c in citations
                if c.get('cited_article_id') == article_id and
                (not keyword or keyword in c.get('citation_context', '').lower())
            ]
        elif direction.lower() == 'from':
            results = [c for c in citations if c.get('source_article_id') == article_id]
        else:
            return json.dumps({"error": "Invalid direction. Must be 'to' or 'from'."})

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """
        Returns the function schema to be used by the language model.
        """
        return {
            "type": "function",
            "function": {
                "name": "search_citations",
                "description": "Searches for citations from or to an article. Use direction 'to' to find citations that an article received or 'from' to find citations that an article made.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string", "description": "The ID of the article to search for citations."},
                        "direction": {"type": "string", "enum": ["to", "from"], "description": "The direction of the search: 'to' (for citations to the article) or 'from' (for citations from the article)."},
                        "context_keyword": {"type": "string", "description": "Optional. A keyword to search for in the citation context (only for 'to' direction)."}
                    },
                    "required": ["article_id", "direction"]
                }
            }
        }

class ManageUserSubscriptions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Adds or removes a user's subscription to a topic.
        - Requires user_id, topic, and action ('add' or 'remove').
        """
        user_id = kwargs.get('user_id')
        topic = kwargs.get('topic')
        action = kwargs.get('action')

        if not all([user_id, topic, action]):
            return json.dumps({"error": "user_id, topic, and action are required."})

        subscriptions = data.get('subscriptions', [])

        if action.lower() == 'add':
            already_subscribed = any(sub.get('user_id') == user_id and sub.get('topic') == topic for sub in subscriptions)
            if already_subscribed:
                return json.dumps({"success": False, "message": "User is already subscribed to this topic."})

            new_sub_id = f"sub_topic_{uuid.uuid4().hex[:6]}"
            new_subscription = {
                "subscription_id": new_sub_id,
                "user_id": user_id,
                "topic": topic
            }
            subscriptions.append(new_subscription)
            return json.dumps({"success": True, "subscription": new_subscription})

        elif action.lower() == 'remove':
            initial_count = len(subscriptions)
            # Create a new list excluding the subscription to be removed
            data['subscriptions'] = [sub for sub in subscriptions if not (sub.get('user_id') == user_id and sub.get('topic') == topic)]

            if len(data['subscriptions']) < initial_count:
                return json.dumps({"success": True, "message": f"Subscription to topic '{topic}' for user '{user_id}' removed."})
            else:
                return json.dumps({"error": "Subscription not found to remove."})

        else:
            return json.dumps({"error": "Invalid action. Must be 'add' or 'remove'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """
        Returns the function schema for the language model.
        """
        return {
            "type": "function",
            "function": {
                "name": "manage_user_subscriptions",
                "description": "Adds or removes a user's subscription to a specific topic.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user."},
                        "topic": {"type": "string", "description": "The topic to subscribe to or unsubscribe from."},
                        "action": {"type": "string", "enum": ["add", "remove"], "description": "The action to perform: 'add' or 'remove' the subscription."}
                    },
                    "required": ["user_id", "topic", "action"]
                }
            }
        }

class SendNotification(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Creates and sends a new notification to a user.
        - Requires recipient_user_id and message_content.
        - sender_user_id is optional and defaults to 'system'.
        """
        recipient_user_id = kwargs.get('recipient_user_id')
        message_content = kwargs.get('message_content')
        sender_user_id = kwargs.get('sender_user_id', 'system')

        if not all([recipient_user_id, message_content]):
            return json.dumps({"error": "recipient_user_id and message_content are required."})

        notifications = data.get('notifications', [])
        new_notification = {
            "notification_id": f"notif_{uuid.uuid4().hex[:6]}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message_content,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "status": "unread"
        }
        notifications.append(new_notification)

        return json.dumps({"success": True, "notification": new_notification})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """
        Returns the function schema for the language model.
        """
        return {
            "type": "function",
            "function": {
                "name": "send_notification",
                "description": "Sends a direct notification to a specific user. Can be from another user or the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {"type": "string", "description": "The ID of the user who will receive the notification."},
                        "message_content": {"type": "string", "description": "The content of the notification message."},
                        "sender_user_id": {"type": "string", "description": "Optional. The ID of the user sending the notification. Defaults to 'system'."}
                    },
                    "required": ["recipient_user_id", "message_content"]
                }
            }
        }

class SearchArticles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        title = kwargs.get('title')
        topic = kwargs.get('topic')
        year = kwargs.get('year')
        author_name = kwargs.get('author_name')
        abstract_keyword = kwargs.get('abstract_keyword')
        full_text_keyword = kwargs.get('full_text_keyword')

        articles = data.get('articles', [])

        if article_id:
            for article in articles:
                if article.get('article_id') == article_id:
                    return json.dumps([article], indent=2)
            return json.dumps({"error": f"Article with ID '{article_id}' not found."})

        if not any([title, topic, year, author_name, abstract_keyword, full_text_keyword]):
            return json.dumps(articles, indent=2)

        results = [
            a for a in articles
            if (not title or title.lower() in a.get('title', '').lower()) and
               (not topic or topic.lower() in a.get('topic', '').lower()) and
               (not year or year == a.get('publication_year')) and
               (not author_name or any(author_name.lower() in author.lower() for author in a.get('authors', []))) and
               (not abstract_keyword or abstract_keyword.lower() in a.get('abstract', '').lower()) and
               (not full_text_keyword or full_text_keyword.lower() in a.get('full_text', '').lower())
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """
        Returns the function schema to be used by the language model.
        """
        return {
            "type": "function",
            "function": {
                "name": "search_articles",
                "description": "Searches for academic articles by ID, title, topic, year, author, or keywords in the abstract or full text. If an article_id is provided, it returns the details of that specific article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string", "description": "The ID of the article to retrieve details for."},
                        "title": {"type": "string", "description": "A keyword or phrase from the article title."},
                        "topic": {"type": "string", "description": "A topic to search for (e.g., 'IA', 'Biology')."},
                        "year": {"type": "integer", "description": "A specific publication year to filter by."},
                        "author_name": {"type": "string", "description": "The name of an author to search for."},
                        "abstract_keyword": {"type": "string", "description": "A keyword to search for within the article's abstract."},
                        "full_text_keyword": {"type": "string", "description": "A keyword to search for within the article's full text."}
                    }
                }
            }
        }

class SummarizeArticle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Finds an article by its ID and returns a summary of its full text.
        The summary is generated by extracting the first three sentences.
        """
        article_id = kwargs.get('article_id')

        if not article_id:
            return json.dumps({"error": "article_id is required."})

        articles = data.get('articles', [])
        for article in articles:
            if article.get('article_id') == article_id:
                full_text = article.get('full_text')
                if not full_text:
                    return json.dumps({"error": f"Article with ID '{article_id}' has no full text to summarize."})

                # Simple summarization logic: take the first three sentences.
                sentences = full_text.split('.')
                summary = ". ".join(sentences[:3]).strip()
                if summary:
                    summary += "."

                return json.dumps({"success": True, "article_id": article_id, "summary": summary})

        return json.dumps({"error": f"Article with ID '{article_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """
        Returns the function schema for the language model.
        """
        return {
            "type": "function",
            "function": {
                "name": "summarize_article",
                "description": "Generates a concise summary of an article's full text using its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string", "description": "The unique ID of the article to summarize."}
                    },
                    "required": ["article_id"]
                }
            }
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
    SummarizeArticle()
]
