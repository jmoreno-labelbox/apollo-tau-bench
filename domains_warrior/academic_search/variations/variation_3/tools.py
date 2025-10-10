import json
from typing import Any, Dict
from datetime import datetime

from domains.dto import Tool

class LocatePapers(Tool):
    """Tool to search for academic articles by topic, title, or year."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        topic,title,year = kwargs.get('topic'),kwargs.get('title'),kwargs.get('year')
        articles: list = data.get('articles', [])
        results = []
        for article in articles:
            match = True
            if kwargs.get('article_id') and kwargs['article_id'] != article.get('article_id'): match = False
            if topic and topic.lower() not in article.get('topic', '').lower(): match = False
            if title and title.lower() not in article.get('title', '').lower(): match = False
            if year and year != article.get('publication_year'): match = False
            if match: results.append(article)
        return json.dumps(results, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "locate_papers","description": "Searches for academic articles by ID, topic, title, or publication year.","parameters": {"type": "object","properties": {"article_id": {"type": "string","description": "The unique ID of the article."}, "topic": {"type": "string","description": "A topic to search for (e.g., 'AI', 'Biology')."},"title": {"type": "string","description": "A keyword or phrase from the article title."},"year": {"type": "integer","description": "A specific publication year to filter by."}},"required": []}}}

class SummarizeAbstract(Tool):
    """Tool to generate a summary of an article's abstract."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        articles = data.get('articles', [])
        for article in articles:
            if article.get('article_id') == article_id:
                summary = f"The article '{article.get('title')}' discusses {article.get('topic')}. The abstract focuses on {article.get('abstract')}"
                return json.dumps({"summary": summary})

        return json.dumps({"error": f"Article with ID '{article_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "summarize_abstract","description": "Generates a brief summary of an article's abstract.","parameters": {"type": "object","properties": {"article_id": {"type": "string","description": "The unique ID of the article to summarize."}},"required": ["article_id"]}}}

class ExtractKeywords(Tool):
    """Tool to extract keywords from an article's abstract."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        articles = data.get('articles', [])
        for article in articles:
            if article.get('article_id') == article_id:
                abstract = article.get('abstract', '').lower()
                potential_keywords = ["transformer", "crispr-cas9", "biomarkers", "dark matter", "quantum computing", "gene therapy"]
                found_keywords = [kw for kw in potential_keywords if kw in abstract]
                return json.dumps(found_keywords)

        return json.dumps({"error": f"Article with ID '{article_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "extract_keywords","description": "Extracts a list of pre-defined keywords from an article's abstract.","parameters": {"type": "object","properties": {"article_id": {"type": "string","description": "The unique ID of the article to extract keywords from."}},"required": ["article_id"]}}}

class FindUsersByCriteria(Tool):
    """Tool to find users by various criteria."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        users = data.get('users', [])
        results = []
        for user in users:
            match = True
            if kwargs.get('user_id') and kwargs['user_id'] != user.get('user_id'): match = False
            if kwargs.get('name') and kwargs['name'].lower() not in user.get('name', '').lower(): match = False
            if kwargs.get('research_field') and kwargs['research_field'].lower() not in user.get('research_field', '').lower(): match = False
            if kwargs.get('availability') and kwargs['availability'] != user.get('availability'): match = False
            if kwargs.get('institution') and kwargs.get('institution') == user.get('institution'): match = False
            if match:
                results.append(user)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_users_by_criteria", "description": "Finds researchers by ID, name, research field, availability, or to exclude an institution.", "parameters": {"type": "object", "properties": {
            "user_id": {"type": "string", "description": "The unique ID of the user."},
            "name": {"type": "string", "description": "The name of the user."},
            "research_field": {"type": "string", "description": "A research field to filter by."},
            "availability": {"type": "string", "description": "The availability status (e.g., 'available')."},
            "institution": {"type": "string", "description": "Excludes users who belong to this institution."}
        }, "required": []}}}

class QuerySubmissions(Tool):
    """Tool to query submissions by article or status."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submissions = data.get('submissions', [])
        results = []
        for sub in submissions:
            match = True
            if kwargs.get('submission_id') and kwargs['submission_id'] != sub.get('submission_id'): match = False
            if kwargs.get('article_id') and kwargs['article_id'] != sub.get('article_id'): match = False
            if kwargs.get('status') and kwargs['status'] != sub.get('status'): match = False
            if match:
                results.append(sub)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "query_submissions", "description": "Queries article submissions by submission ID, article ID or status.", "parameters": {"type": "object", "properties": {
            "submission_id": {"type": "string", "description": "The unique ID of the submission."},
            "article_id": {"type": "string", "description": "The associated article's ID."},
            "status": {"type": "string", "description": "The current status of the submission (e.g., 'pending', 'under review')."}
        }, "required": []}}}

class GenerateNewReview(Tool):
    """Tool to generate a new review entry for a submission."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        review_id = f"rev_{len(data.get('reviews', [])) + 1:02d}"
        new_review = {
            "review_id": review_id,
            "submission_id": kwargs.get('submission_id'),
            "reviewer_user_id": kwargs.get('reviewer_user_id'),
            "score": kwargs.get('score'),
            "comments": kwargs.get('comments'),
            "review_date": datetime.now().strftime('%Y-%m-%d')
        }
        data.get('reviews', []).append(new_review)
        return json.dumps(new_review, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "generate_new_review", "description": "Generates a new review for a submission.", "parameters": {"type": "object", "properties": {
            "submission_id": {"type": "string", "description": "The ID of the submission to be reviewed."},
            "reviewer_user_id": {"type": "string", "description": "The ID of the reviewing user."},
            "score": {"type": "integer", "description": "The review score (1-10)."},
            "comments": {"type": "string", "description": "Detailed comments for the review."}
        }, "required": ["submission_id", "reviewer_user_id", "score", "comments"]}}}

class SearchReviews(Tool):
    """Tool to search for reviews by submission and reviewer."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        reviews = data.get('reviews', [])
        results = [r for r in reviews if r.get('submission_id') == kwargs.get('submission_id') and r.get('reviewer_user_id') == kwargs.get('reviewer_user_id')]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "search_reviews", "description": "Searches for specific reviews by submission and reviewer ID.", "parameters": {"type": "object", "properties": {
            "submission_id": {"type": "string", "description": "The submission's ID."},
            "reviewer_user_id": {"type": "string", "description": "The reviewer's ID."}
        }, "required": ["submission_id", "reviewer_user_id"]}}}

class QueryProjects(Tool):
    """Tool to query projects by ID or name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        projects = data.get('projects', [])
        results = []
        for proj in projects:
            match = True
            if kwargs.get('project_id') and kwargs['project_id'] != proj.get('project_id'): match = False
            if kwargs.get('project_name') and kwargs['project_name'].lower() not in proj.get('project_name', '').lower(): match = False
            if match:
                results.append(proj)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "query_projects", "description": "Queries research projects by ID or name.", "parameters": {"type": "object", "properties": {
            "project_id": {"type": "string", "description": "The project's ID."},
            "project_name": {"type": "string", "description": "The project's name."}
        }, "required": []}}}

class LocateFundingSources(Tool):
    """Tool to locate funding sources by research area and availability status."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sources = data.get('funding_sources', [])
        results = []
        area = kwargs.get('area', '').lower()
        status = kwargs.get('status', '').lower()

        for s in sources:
            match_area = area in s.get('focus_area', '').lower()
            match_status = True
            if status:
                match_status = status == s.get('status', '').lower()

            if match_area and match_status:
                results.append(s)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "locate_funding_sources", "description": "Locates funding sources by research area and availability.", "parameters": {"type": "object", "properties": {
            "area": {"type": "string", "description": "The research area (e.g., 'AI', 'Medical Research')."},
            "status": {"type": "string", "description": "The availability status of the grant (e.g., 'available')."}
        }, "required": []}}}

class AddEntryToLog(Tool):
    """Tool to add a log note to a user, project, submission or article."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        notes = kwargs.get('notes')
        target_list = None
        target_id_key = None
        target_id_value = None

        if 'user_id' in kwargs:
            target_list = data.get('users', [])
            target_id_key = 'user_id'
            target_id_value = kwargs['user_id']
        elif 'project_id' in kwargs:
            target_list = data.get('projects', [])
            target_id_key = 'project_id'
            target_id_value = kwargs['project_id']
        elif 'submission_id' in kwargs:
            target_list = data.get('submissions', [])
            target_id_key = 'submission_id'
            target_id_value = kwargs['submission_id']
        elif 'article_id' in kwargs:
            target_list = data.get('articles', [])
            target_id_key = 'article_id'
            target_id_value = kwargs['article_id']
        else:
            return json.dumps({"error": "Either user_id, project_id, submission_id, or article_id is required."}, indent=2)

        for item in target_list:
            if item.get(target_id_key) == target_id_value:
                if 'logs' not in item:
                    item['logs'] = []
                item['logs'].append(notes)
                return json.dumps(item, indent=2)

        return json.dumps({"error": f"Item with ID '{target_id_value}' not found in the specified table."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "add_entry_to_log", "description": "Adds a log entry for a user, project, submission, or article.", "parameters": {"type": "object", "properties": {
            "user_id": {"type": "string", "description": "The ID of the user to add the log to."},
            "project_id": {"type": "string", "description": "The ID of the project to add the log to."},
            "submission_id": {"type": "string", "description": "The ID of the submission to add the log to."},
            "article_id": {"type": "string", "description": "The ID of the article to add the log to."},
            "notes": {"type": "string", "description": "The content of the log note."}
        }, "required": ["notes"]}}}

class DeleteCitation(Tool):
    """Tool to delete a citation record."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        citation_id = kwargs.get('citation_id')
        citations = data.get('citations', [])
        original_count = len(citations)
        data['citations'] = [c for c in citations if c.get('citation_id') != citation_id]
        if len(data['citations']) < original_count:
            return json.dumps({"status": "success", "citation_id": citation_id, "message": "Citation deleted."})
        else:
            return json.dumps({"error": f"Citation with ID {citation_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "delete_citation", "description": "Deletes a specific citation record by its ID.", "parameters": {"type": "object", "properties": {
            "citation_id": {"type": "string", "description": "The unique ID of the citation to delete."}
        }, "required": ["citation_id"]}}}

class QueryCitationConnections(Tool):
    """Tool to search for citations related to an article."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        citations = data.get('citations', [])
        results = []
        direction = kwargs.get('direction', 'from') # 'from' or 'to'

        if direction == 'from' and 'source_article_id' in kwargs:
            source_id = kwargs['source_article_id']
            results = [c for c in citations if c.get('source_article_id') == source_id]

        elif direction == 'to' and 'cited_article_id' in kwargs:
            cited_id = kwargs['cited_article_id']
            results = [c for c in citations if c.get('cited_article_id') == cited_id]

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "query_citation_connections", "description": "Searches for citations, either from a source article or to a cited article.", "parameters": {"type": "object", "properties": {
            "source_article_id": {"type": "string", "description": "The ID of the article that made the citation."},
            "cited_article_id": {"type": "string", "description": "The ID of the article that received the citation."},
            "direction": {"type": "string", "enum": ["from", "to"], "description": "The direction of the citation search."}
        }, "required": ["direction"]}}}

class RetrieveCitationData(Tool):
    """Tool to get the full details of a specific citation."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        citation_id = kwargs.get('citation_id')
        for citation in data.get('citations', []):
            if citation.get('citation_id') == citation_id:
                return json.dumps(citation, indent=2)
        return json.dumps({"error": f"Citation with ID {citation_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "retrieve_citation_data", "description": "Retrieves the full details of a specific citation by its ID.", "parameters": {"type": "object", "properties": {
            "citation_id": {"type": "string", "description": "The unique ID of the citation."}
        }, "required": ["citation_id"]}}}

class InitiateProject(Tool):
    """Tool to create a new research project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        projects = data.get('projects', [])
        new_project = {
            "project_id": f"proj_{len(projects) + 1:02d}",
            "project_name": kwargs.get('project_name'),
            "lead_researcher_id": kwargs.get('lead_researcher_id'),
            "status": "new",
            "start_date": datetime.now().strftime('%Y-%m-%d'),
            "end_date": None,
            "linked_articles": [],
            "funding_source_id": None,
            "logs": []
        }
        projects.append(new_project)
        return json.dumps(new_project, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "initiate_project", "description": "Creates a new research project.", "parameters": {"type": "object", "properties": {
            "project_name": {"type": "string", "description": "The name of the new project."},
            "lead_researcher_id": {"type": "string", "description": "The user ID of the lead researcher."}
        }, "required": ["project_name", "lead_researcher_id"]}}}

class RegisterArticleRecord(Tool):
    """Tool to create a new article record."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        articles = data.get('articles', [])
        new_article = {
            "article_id": f"art_{len(articles) + 1:02d}",
            "title": kwargs.get('title'),
            "authors": kwargs.get('authors', []),
            "publication_year": datetime.now().year,
            "topic": kwargs.get('topic'),
            "abstract": kwargs.get('abstract'),
            "status": "draft"
        }
        articles.append(new_article)
        return json.dumps(new_article, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "register_article_record", "description": "Creates a new draft article record.", "parameters": {"type": "object", "properties": {
            "title": {"type": "string", "description": "The title of the article."},
            "authors": {"type": "array", "items": {"type": "string"}, "description": "A list of author names."},
            "topic": {"type": "string", "description": "The primary topic of the article."},
            "abstract": {"type": "string", "description": "The abstract of the article."}
        }, "required": ["title", "authors", "topic", "abstract"]}}}

class SubmitArticleForReview(Tool):
    """Tool to create a new submission for an article."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submissions = data.get('submissions', [])
        new_submission = {
            "submission_id": f"sub_{len(submissions) + 1:02d}",
            "article_id": kwargs.get('article_id'),
            "author_user_id": kwargs.get('author_user_id'),
            "submission_date": datetime.now().strftime('%Y-%m-%d'),
            "status": "submitted",
            "assigned_reviewers": []
        }
        submissions.append(new_submission)
        return json.dumps(new_submission, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "submit_article_for_review", "description": "Creates a new article submission for the review process.", "parameters": {"type": "object", "properties": {
            "article_id": {"type": "string", "description": "The ID of the article being submitted."},
            "author_user_id": {"type": "string", "description": "The ID of the submitting author."}
        }, "required": ["article_id", "author_user_id"]}}}

class LinkCitedArticle(Tool):
    """Tool to create a new citation record between two articles."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        citations = data.get('citations', [])
        new_citation_id = f"cit_{len(citations) + 1:02d}"
        new_citation = {
            "citation_id": new_citation_id,
            "source_article_id": kwargs.get('source_article_id'),
            "cited_article_id": kwargs.get('cited_article_id'),
            "citation_context": kwargs.get('citation_context', 'Citation added for reference.')
        }
        citations.append(new_citation)
        return json.dumps(new_citation, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "link_cited_article", "description": "Creates a new citation record to link a source article to a cited article.", "parameters": {"type": "object", "properties": {
            "source_article_id": {"type": "string", "description": "The ID of the article making the citation."},
            "cited_article_id": {"type": "string", "description": "The ID of the article being cited."},
            "citation_context": {"type": "string", "description": "A brief description of the citation's context."}
        }, "required": ["source_article_id", "cited_article_id"]}}}

class DeleteReview(Tool):
    """Tool to delete a review record."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        review_id = kwargs.get('review_id')
        reviews = data.get('reviews', [])
        original_count = len(reviews)
        data['reviews'] = [r for r in reviews if r.get('review_id') != review_id]
        if len(data['reviews']) < original_count:
            return json.dumps({"status": "success", "review_id": review_id, "message": "Review deleted."})
        else:
            return json.dumps({"error": f"Review with ID {review_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "delete_review", "description": "Deletes a specific review record by its ID.", "parameters": {"type": "object", "properties": {
            "review_id": {"type": "string", "description": "The unique ID of the review to delete."}
        }, "required": ["review_id"]}}}

class ModifyRecord(Tool):
    """
    Tool to modify fields of any existing record, such as project, article, user, submission, or funding source.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        record_type = kwargs.pop('record_type', None)
        record_id = kwargs.pop('record_id', None)

        if not record_type or not record_id:
            return json.dumps({"error": "The parameters 'record_type' and 'record_id' are required."}, indent=2)

        table_map = {
            "article": (data.get('articles', []), 'article_id'),
            "project": (data.get('projects', []), 'project_id'),
            "user": (data.get('users', []), 'user_id'),
            "submission": (data.get('submissions', []), 'submission_id'),
            "funding_source": (data.get('funding_sources', []), 'funding_source_id'),
            "user_preference": (data.get('user_preferences', []), 'preference_id'),
            "subscription": (data.get('subscriptions', []), 'subscription_id')
        }

        if record_type not in table_map:
            return json.dumps({"error": f"Invalid record type: {record_type}"}, indent=2)

        target_list, id_key = table_map[record_type]

        for item in target_list:
            if item.get(id_key) == record_id:
                # Update the item with the remaining kwargs
                for key, value in kwargs.items():
                    item[key] = value
                return json.dumps(item, indent=2)

        return json.dumps({"error": f"Record of type '{record_type}' with ID '{record_id}' not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_record",
                "description": "Modifies fields of an existing record, such as a project, article, user, submission, or funding source.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record_type": {
                            "type": "string",
                            "description": "The type of the record to be modified.",
                            "enum": ["article", "project", "user", "submission", "funding_source", "user_preference", "subscription"]
                        },
                        "record_id": {
                            "type": "string",
                            "description": "The unique ID of the record to be modified."
                        },
                    },
                    "required": ["record_type", "record_id"]
                }
            }
        }

class DispatchSystemNotification(Tool):
    """Tool to dispatch a direct notification to a user."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        recipient_user_id = kwargs.get('recipient_user_id')
        message_content = kwargs.get('message_content')
        sender_user_id = kwargs.get('sender_user_id', 'system')

        if not all([recipient_user_id, message_content]):
            return json.dumps({"error": "recipient_user_id and message_content are required."})

        notifications = data.get('notifications', [])
        new_notification = {
            "notification_id": f"notif_{len(notifications) + 1:02d}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message_content,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "status": "unread"
        }
        notifications.append(new_notification)

        return json.dumps(new_notification, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "dispatch_system_notification",
                "description": "Dispatches a direct notification to a user, which can be from the system or another user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {"type": "string", "description": "The ID of the user who will receive the notification."},
                        "message_content": {"type": "string", "description": "The content of the notification message."},
                        "sender_user_id": {"type": "string", "description": "Optional. The user ID of the sender. Defaults to 'system'."}
                    },
                    "required": ["recipient_user_id", "message_content"]
                }
            }
        }

TOOLS = [
    LocatePapers(),
    SummarizeAbstract(),
    ExtractKeywords(),
    FindUsersByCriteria(),
    QuerySubmissions(),
    GenerateNewReview(),
    SearchReviews(),
    QueryProjects(),
    LocateFundingSources(),
    AddEntryToLog(),
    DeleteCitation(),
    QueryCitationConnections(),
    RetrieveCitationData(),
    InitiateProject(),
    RegisterArticleRecord(),
    SubmitArticleForReview(),
    LinkCitedArticle(),
    DeleteReview(),
    ModifyRecord(),
    DispatchSystemNotification()
]
