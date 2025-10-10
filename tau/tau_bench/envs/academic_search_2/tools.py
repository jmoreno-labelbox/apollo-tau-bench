import json
import uuid
from datetime import datetime
from collections import Counter
from typing import Any, Dict

from domains.dto import Tool

class FindResearcherProfiles(Tool):
    """Searches for users by their name, research field, or user_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name, research_field, user_id = kwargs.get('name'), kwargs.get('research_field'), kwargs.get('user_id')
        if not any([name, research_field, user_id]):
            return json.dumps(data.get('users', []), indent=2)

        users = data.get('users', [])
        results = [
            user for user in users if
            (not name or name.lower() in user.get('name', '').lower()) and
            (not research_field or research_field.lower() in user.get('research_field', '').lower()) and
            (not user_id or user.get('user_id') == user_id)
        ]
        return json.dumps(results, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_researcher_profiles", "description": "Searches for users by their name, research field, or user_id.", "parameters": {"type": "object", "properties": {"name": {"type": "string"}, "research_field": {"type": "string"}, "user_id": {"type": "string"}}}}}

class RetrievePapers(Tool):
    """Searches for academic articles by ID, topic, title, year, or author name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        articles: list = data.get('articles', [])

        if article_id:
            for article in articles:
                if article.get('article_id') == article_id:
                    return json.dumps([article], indent=2)
            return json.dumps([])

        topic, title, year, author_name = kwargs.get('topic'), kwargs.get('title'), kwargs.get('year'), kwargs.get('author_name')

        results = [
            a for a in articles if
            (not topic or topic.lower() in a.get('topic', '').lower()) and
            (not title or title.lower() in a.get('title', '').lower()) and
            (not year or year == a.get('publication_year')) and
            (not author_name or any(author_name.lower() in author.lower() for author in a.get('authors', [])))
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "retrieve_papers", "description": "Searches for academic articles by ID, topic, title, publication year, or author name.", "parameters": {"type": "object", "properties": {"article_id": {"type": "string"}, "topic": {"type": "string"}, "title": {"type": "string"}, "year": {"type": "integer"}, "author_name": {"type": "string"}}}}}

class SearchSubmissions(Tool):
    """Searches for submissions by submission_id, article_id, or by a specific review_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id, article_id, review_id = kwargs.get('submission_id'), kwargs.get('article_id'), kwargs.get('review_id')

        # Logic from the old SearchReviews tool
        if review_id:
            reviews = data.get('reviews', [])
            target_review = next((r for r in reviews if r.get('review_id') == review_id), None)
            if not target_review:
                return json.dumps([]) # Return empty list if review not found

            # Use the submission_id from the review to find the submission
            submission_id_from_review = target_review.get('submission_id')
            submissions = data.get('submissions', [])
            results = [s for s in submissions if s.get('submission_id') == submission_id_from_review]

            if results:
                results[0]['review_details'] = target_review # Attach the entire review object
            return json.dumps(results, indent=2)

        if not submission_id and not article_id:
            return json.dumps(data.get('submissions', []), indent=2)

        submissions = data.get('submissions', [])
        results = [
            s for s in submissions if
            (not submission_id or s.get('submission_id') == submission_id) and
            (not article_id or s.get('article_id') == article_id)
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_submissions",
                "description": "Searches for submissions by submission_id, article_id, or indirectly via a review_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string"},
                        "article_id": {"type": "string"},
                        "review_id": {"type": "string", "description": "If provided, finds the submission associated with this review."}
                    }
                }
            }
        }

class GetProjectDetails(Tool):
    """Searches for projects by project_name, linked_article_id, or project_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_name, linked_article_id, project_id = kwargs.get('project_name'), kwargs.get('linked_article_id'), kwargs.get('project_id')
        if not any([project_name, linked_article_id, project_id]):
            return json.dumps(data.get('projects', []), indent=2)
        projects = data.get('projects', [])
        results = [
            p for p in projects if
            (not project_name or project_name.lower() in p.get('project_name', '').lower()) and
            (not linked_article_id or linked_article_id in p.get('linked_articles', [])) and
            (not project_id or p.get('project_id') == project_id)
        ]
        return json.dumps(results, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_project_details", "description": "Searches for projects by project_name, linked_article_id, or project_id.", "parameters": {"type": "object", "properties": {"project_name": {"type": "string"}, "linked_article_id": {"type": "string"}, "project_id": {"type": "string"}}}}}

class GetCitationGraph(Tool):
    """
    Gets the citation graph for a specific article.
    If a second article ID is provided via 'compare_with_article_id', it finds the common citations between the two.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        compare_with_article_id = kwargs.get('compare_with_article_id')

        if not article_id:
            return json.dumps({"error": "article_id is required."})

        citations = data.get('citations', [])

        # Logic from the old FindCommonCitations tool
        if compare_with_article_id:
            cites1 = {c['cited_article_id'] for c in citations if c.get('source_article_id') == article_id}
            cites2 = {c['cited_article_id'] for c in citations if c.get('source_article_id') == compare_with_article_id}
            common_citations = list(cites1.intersection(cites2))
            return json.dumps({"article1_id": article_id, "article2_id": compare_with_article_id, "common_citations": common_citations}, indent=2)

        # Original logic of GetCitationGraph
        else:
            cited_by = [c['source_article_id'] for c in citations if c.get('cited_article_id') == article_id]
            cites = [c['cited_article_id'] for c in citations if c.get('source_article_id') == article_id]
            result = {"article_id": article_id, "cited_by": cited_by, "cites": cites}
            return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_citation_graph",
                "description": "Gets the citation graph for an article, or finds common citations between two articles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string"},
                        "compare_with_article_id": {"type": "string", "description": "If provided, finds common articles cited by both this article and the main article_id."}
                    },
                    "required": ["article_id"]
                }
            }
        }

class FindCollaborationNetwork(Tool):
    """
    Finds the collaboration network for a given author.
    Can be constrained to check only against a specific list of potential collaborators.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        author_name = kwargs.get('author_name')
        authors_to_check = kwargs.get('authors_to_check')
        if not author_name:
            return json.dumps({"error": "author_name is required."})

        # Find all articles by the main author
        articles = [a for a in data.get('articles', []) if author_name in a.get('authors', [])]

        # Count all collaborators from those articles
        all_collaborators = Counter()
        for article in articles:
            for author in article.get('authors', []):
                if author != author_name:
                    all_collaborators[author] += 1

        # If a specific list of authors is provided, filter the results
        if authors_to_check:
            final_counts = {author: all_collaborators.get(author, 0) for author in authors_to_check}
            return json.dumps(final_counts, indent=2)

        return json.dumps(dict(all_collaborators), indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_collaboration_network", "description": "Finds the collaboration network for an author, optionally checking against a specific list of names.", "parameters": {"type": "object", "properties": {"author_name": {"type": "string"}, "authors_to_check": {"type": "array", "items": {"type": "string"}}}, "required": ["author_name"]}}}

class AddCitation(Tool):
    """Adds a new citation."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        source_article_id, cited_article_id, context = kwargs.get('source_article_id'), kwargs.get('cited_article_id'), kwargs.get('context')
        if not all([source_article_id, cited_article_id]):
            return json.dumps({"error": "source_article_id and cited_article_id are required."})
        new_citation = {"citation_id": f"cit_{uuid.uuid4().hex[:4]}", "source_article_id": source_article_id, "cited_article_id": cited_article_id, "citation_context": context}
        data.get('citations', []).append(new_citation)
        return json.dumps({"success": True, "citation": new_citation}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "add_citation", "description": "Adds a new citation.", "parameters": {"type": "object", "properties": {"source_article_id": {"type": "string"}, "cited_article_id": {"type": "string"}, "context": {"type": "string"}}, "required": ["source_article_id", "cited_article_id"]}}}

class UpdateArticleMetadata(Tool):
    """Updates article metadata for specified fields."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        if not article_id:
            return json.dumps({"error": "article_id is required."})
        article = next((a for a in data.get('articles', []) if a.get('article_id') == article_id), None)
        if not article:
            return json.dumps({"error": "Article not found."})

        updatable_fields = ['title', 'authors', 'publication_year', 'topic', 'abstract', 'status', 'keywords']
        for key, value in kwargs.items():
            if key in updatable_fields and key != 'article_id':
                article[key] = value
        return json.dumps({"success": True, "article": article}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_article_metadata", "description": "Updates article metadata (e.g., topic, status, keywords).", "parameters": {"type": "object", "properties": {"article_id": {"type": "string"}, "topic": {"type": "string"}, "status": {"type": "string"}, "keywords": {"type": "array", "items": {"type": "string"}}}, "required": ["article_id"]}}}

class GetAuthorMetrics(Tool):
    """Gets multiple metrics for an author."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        author_name = kwargs.get('author_name')
        if not author_name:
            return json.dumps({"error": "author_name is required."})
        articles = [a for a in data.get('articles', []) if author_name in a.get('authors', [])]
        if not articles:
            return json.dumps({"total_publications": 0, "total_citations": 0, "h_index": 0})
        citations = data.get('citations', [])
        total_citations = 0
        citation_counts = []
        for article in articles:
            count = len([c for c in citations if c.get('cited_article_id') == article['article_id']])
            total_citations += count
            citation_counts.append(count)
        citation_counts.sort(reverse=True)
        h_index = 0
        for i, count in enumerate(citation_counts):
            if count >= i + 1: h_index = i + 1
            else: break
        return json.dumps({"total_publications": len(articles), "total_citations": total_citations, "h_index": h_index}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_author_metrics", "description": "Gets multiple metrics for an author.", "parameters": {"type": "object", "properties": {"author_name": {"type": "string"}}, "required": ["author_name"]}}}

class SuggestReviewers(Tool):
    """Suggests potential reviewers for an article, with an option to exclude certain authors."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        exclude_authors = kwargs.get('exclude_authors', [])
        if not article_id:
            return json.dumps({"error": "article_id is required."})
        article = next((a for a in data.get('articles', []) if a.get('article_id') == article_id), None)
        if not article:
            return json.dumps({"error": "Article not found."})
        topic = article.get('topic')
        authors = [a.get('authors') for a in data.get('articles', []) if a.get('topic') == topic and a.get('article_id') != article_id]
        authors = [author for sublist in authors for author in sublist]
        authors = [author for author in dict.fromkeys(authors) if author not in exclude_authors]
        return json.dumps({"suggested_reviewers": authors}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "suggest_reviewers", "description": "Suggests potential reviewers for an article.", "parameters": {"type": "object", "properties": {"article_id": {"type": "string"}, "exclude_authors": {"type": "array", "items": {"type": "string"}}}, "required": ["article_id"]}}}

class GetMostCitedArticles(Tool):
    """Tool to get a list of the most cited articles."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        citations = data.get('citations', [])
        cited_ids = [c['cited_article_id'] for c in citations]
        citation_counts = Counter(cited_ids)
        sorted_articles = sorted(citation_counts.items(), key=lambda item: item[1], reverse=True)
        result = [{"article_id": article_id, "citation_count": count} for article_id, count in sorted_articles]
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "get_most_cited_articles","description": "Returns a list of articles sorted by how many times they have been cited.","parameters": {"type": "object", "properties": {}}}}

class FindCommonCollaborators(Tool):
    """Finds common collaborators between two authors."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        author1_name, author2_name = kwargs.get('author1_name'), kwargs.get('author2_name')
        if not all([author1_name, author2_name]):
            return json.dumps({"error": "author1_name and author2_name are required."})
        articles1 = [a for a in data.get('articles', []) if author1_name in a.get('authors', [])]
        collaborators1 = {author for article in articles1 for author in article.get('authors', []) if author != author1_name}
        articles2 = [a for a in data.get('articles', []) if author2_name in a.get('authors', [])]
        collaborators2 = {author for article in articles2 for author in article.get('authors', []) if author != author2_name}
        common_collaborators = list(collaborators1.intersection(collaborators2))
        return json.dumps({"common_collaborators": common_collaborators}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_common_collaborators", "description": "Finds common collaborators between two authors.", "parameters": {"type": "object", "properties": {"author1_name": {"type": "string"}, "author2_name": {"type": "string"}}, "required": ["author1_name", "author2_name"]}}}

class UpdateSubmission(Tool):
    """Updates a submission's status or overwrites its list of reviewers."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        if not submission_id:
            return json.dumps({"error": "submission_id is required."})

        submission = next((s for s in data.get('submissions', []) if s.get('submission_id') == submission_id), None)
        if not submission: return json.dumps({"error": "Submission not found."})

        if 'reviewers' in kwargs:
            provided_reviewers = kwargs.get('reviewers', [])
            users = data.get('users', [])

            valid_reviewer_ids = []
            for reviewer_item in provided_reviewers:
                if any(u['user_id'] == reviewer_item for u in users):
                    valid_reviewer_ids.append(reviewer_item)
                else:
                    found_user = next((u for u in users if u['name'] == reviewer_item), None)
                    if found_user:
                        valid_reviewer_ids.append(found_user['user_id'])

            submission['assigned_reviewers'] = sorted(list(set(valid_reviewer_ids)))

        if 'status' in kwargs:
            submission['status'] = kwargs['status']

        return json.dumps({"success": True, "submission": submission}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_submission", "description": "Updates a submission's status or overwrites its list of reviewers.", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string"}, "reviewers": {"type": "array", "items": {"type": "string", "description": "List of reviewer user_ids or names to assign."}}, "status": {"type": "string"}}, "required": ["submission_id"]}}}

class RegisterProject(Tool):
    """Creates a new research project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_name, lead_researcher_id, linked_article_id = kwargs.get('project_name'), kwargs.get('lead_researcher_id'), kwargs.get('linked_article_id')
        project_id_override = kwargs.get('project_id_override')
        if not all([project_name, lead_researcher_id, linked_article_id]):
            return json.dumps({"error": "project_name, lead_researcher_id, and linked_article_id are required."})
        new_project = {
            "project_id": project_id_override if project_id_override else f"proj_{uuid.uuid4().hex[:4]}",
            "project_name": project_name,
            "lead_researcher_id": lead_researcher_id,
            "status": "active",
            "start_date": "2025-06-24",
            "end_date": None,
            "linked_articles": [linked_article_id],
            "funding_source_id": None
        }
        data.get('projects', []).append(new_project)
        return json.dumps({"success": True, "project": new_project}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "register_project", "description": "Creates a new research project.", "parameters": {"type": "object", "properties": {"project_name": {"type": "string"}, "lead_researcher_id": {"type": "string"}, "linked_article_id": {"type": "string"}, "project_id_override": {"type": "string"}}, "required": ["project_name", "lead_researcher_id", "linked_article_id"]}}}

class CreateSubmission(Tool):
    """Creates a new article submission."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id, author_user_id = kwargs.get('article_id'), kwargs.get('author_user_id')
        submission_id_override = kwargs.get('submission_id_override')
        if not all([article_id, author_user_id]):
            return json.dumps({"error": "article_id and author_user_id are required."})
        new_submission = {
            "submission_id": submission_id_override if submission_id_override else f"sub_{uuid.uuid4().hex[:4]}",
            "article_id": article_id,
            "author_user_id": author_user_id,
            "submission_date": "2025-06-24",
            "status": "submitted",
            "assigned_reviewers": []
        }
        data.get('submissions', []).append(new_submission)
        return json.dumps({"success": True, "submission": new_submission}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_submission", "description": "Creates a new article submission.", "parameters": {"type": "object", "properties": {"article_id": {"type": "string"}, "author_user_id": {"type": "string"}, "submission_id_override": {"type": "string"}}, "required": ["article_id", "author_user_id"]}}}

class AddResearchNote(Tool):
    """Creates a new entry in the research_logs."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        researcher_id, article_id, notes = kwargs.get('researcher_id'), kwargs.get('article_id'), kwargs.get('notes')
        log_id_override = kwargs.get('log_id_override')
        if not all([researcher_id, article_id, notes]):
            return json.dumps({"error": "researcher_id, article_id, and notes are required."})
        new_log = {
            "log_id": log_id_override if log_id_override else f"log_{uuid.uuid4().hex[:4]}",
            "researcher_id": researcher_id,
            "article_id": article_id,
            "entry_date": "2025-06-24",
            "notes": notes,
            "relevance": kwargs.get('relevance', 'medium')
        }
        data.get('research_logs', []).append(new_log)
        return json.dumps({"success": True, "log_entry": new_log}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "add_research_note", "description": "Creates a new entry in the research_logs.", "parameters": {"type": "object", "properties": {"researcher_id": {"type": "string"}, "article_id": {"type": "string"}, "notes": {"type": "string"}, "relevance": {"type": "string"}, "log_id_override": {"type": "string"}}, "required": ["researcher_id", "article_id", "notes"]}}}

class UpdateProject(Tool):
    """Updates an existing project's status, collaborators, linked articles, or funding source."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get('project_id')
        if not project_id: return json.dumps({"error": "project_id is required."})
        project = next((p for p in data.get('projects', []) if p.get('project_id') == project_id), None)
        if not project: return json.dumps({"error": "Project not found."})

        standard_updatable_fields = ['project_name', 'status', 'end_date', 'funding_source_id']
        for key, value in kwargs.items():
            if key in standard_updatable_fields:
                project[key] = value

        if 'linked_articles' in kwargs:
            project['linked_articles'] = kwargs['linked_articles']

        if 'add_collaborators' in kwargs:
            if 'collaborators' not in project:
                project['collaborators'] = []

            provided_collaborators = kwargs.get('add_collaborators', [])
            users = data.get('users', [])

            valid_collaborator_ids = []
            for collab_item in provided_collaborators:
                # Check if the item is already a valid user_id
                if any(u['user_id'] == collab_item for u in users):
                    valid_collaborator_ids.append(collab_item)
                # Otherwise, try to find by name
                else:
                    found_user = next((u for u in users if u['name'] == collab_item), None)
                    if found_user:
                        valid_collaborator_ids.append(found_user['user_id'])

            existing_collaborators = set(project.get('collaborators', []))
            updated_collaborators = sorted(list(existing_collaborators.union(set(valid_collaborator_ids))))
            project['collaborators'] = updated_collaborators

        return json.dumps({"success": True, "project": project}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_project", "description": "Updates a project's details, such as status, collaborators, linked articles, or funding.", "parameters": {"type": "object", "properties": {"project_id": {"type": "string"}, "status": {"type": "string"}, "project_name": {"type": "string"}, "add_collaborators": {"type": "array", "items": {"type": "string"}}, "funding_source_id": {"type": "string"}, "linked_articles": {"type": "array", "items": {"type": "string"}}}, "required": ["project_id"]}}}

class RetrieveFundingInfo(Tool):
    """Searches for funding sources by source_name or funding_source_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        source_name, funding_source_id = kwargs.get('source_name'), kwargs.get('funding_source_id')
        if not source_name and not funding_source_id:
            return json.dumps(data.get('funding_sources', []), indent=2)

        funding_sources = data.get('funding_sources', [])
        results = [
            fs for fs in funding_sources if
            (not source_name or source_name.lower() in fs.get('source_name', '').lower()) and
            (not funding_source_id or fs.get('funding_source_id') == funding_source_id)
        ]
        return json.dumps(results, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "retrieve_funding_info", "description": "Searches for funding sources by name or ID.", "parameters": {"type": "object", "properties": {"source_name": {"type": "string"}, "funding_source_id": {"type": "string"}}}}}

class CreateReview(Tool):
    """Creates a new review for a submission."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id, reviewer_user_id, content, recommendation = kwargs.get('submission_id'), kwargs.get('reviewer_user_id'), kwargs.get('content'), kwargs.get('recommendation')
        review_id_override = kwargs.get('review_id_override')
        if not all([submission_id, reviewer_user_id, content, recommendation]):
            return json.dumps({"error": "submission_id, reviewer_user_id, content, and recommendation are required."})

        new_review = {
            "review_id": review_id_override if review_id_override else f"rev_{uuid.uuid4().hex[:4]}",
            "submission_id": submission_id,
            "reviewer_user_id": reviewer_user_id,
            "review_content": content,
            "recommendation": recommendation,
            "review_date": "2025-06-24"
        }
        data.get('reviews', []).append(new_review)
        return json.dumps({"success": True, "review": new_review}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_review", "description": "Creates a new review for a submission.", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string"}, "reviewer_user_id": {"type": "string"}, "content": {"type": "string"}, "recommendation": {"type": "string"}, "review_id_override": {"type": "string"}}, "required": ["submission_id", "reviewer_user_id", "content", "recommendation"]}}}

class CreateArticle(Tool):
    """Creates a new article record."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Extract parameters for the new article
        title = kwargs.get('title')
        authors = kwargs.get('authors')
        topic = kwargs.get('topic')
        publication_year = kwargs.get('publication_year')
        article_id_override = kwargs.get('article_id_override')

        if not all([title, authors, topic, publication_year]):
            return json.dumps({"error": "title, authors, topic, and publication_year are required."})

        new_article = {
            "article_id": article_id_override if article_id_override else f"art_{uuid.uuid4().hex[:4]}",
            "title": title,
            "authors": authors,
            "publication_year": publication_year,
            "topic": topic,
            "abstract": kwargs.get('abstract', '...'),
            "status": "new"
        }
        data.get('articles', []).append(new_article)
        return json.dumps({"success": True, "article": new_article}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_article", "description": "Creates a new article record.", "parameters": {"type": "object", "properties": {"title": {"type": "string"}, "authors": {"type": "array", "items": {"type": "string"}}, "topic": {"type": "string"}, "publication_year": {"type": "integer"}, "abstract": {"type": "string"}, "article_id_override": {"type": "string"}}, "required": ["title", "authors", "topic", "publication_year"]}}}

class ConfigureProfileSettings(Tool):
    """Configures a user's profile settings."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        notification_channel = kwargs.get('notification_channel')
        ui_theme = kwargs.get('ui_theme')

        if not user_id:
            return json.dumps({"error": "user_id is required to configure settings."})

        if not notification_channel and not ui_theme:
            return json.dumps({"error": "At least one setting (notification_channel or ui_theme) must be provided."})

        preferences = data.get('user_preferences', [])

        user_pref = next((pref for pref in preferences if pref.get('user_id') == user_id), None)

        if user_pref:
            if notification_channel:
                user_pref['notification_channel'] = notification_channel
            if ui_theme:
                user_pref['ui_theme'] = ui_theme
            return json.dumps({"success": True, "configured_settings": user_pref})
        else:
            new_pref = {
                "preference_id": f"pref_{uuid.uuid4().hex[:4]}", # Gera um ID único
                "user_id": user_id,
                "notification_channel": notification_channel,
                "ui_theme": ui_theme
            }
            if not notification_channel:
                del new_pref['notification_channel']
            if not ui_theme:
                del new_pref['ui_theme']

            preferences.append(new_pref)
            data['user_preferences'] = preferences # Garante que a lista atualizada seja salva de volta no 'data'
            return json.dumps({"success": True, "configured_settings": new_pref})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "configure_profile_settings",
                "description": "Configures a user's profile settings, such as notification channel or UI theme. Creates a new preference entry if one does not exist for the user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user whose settings are being configured."},
                        "notification_channel": {"type": "string", "description": "The new notification channel (e.g., 'email', 'in_app')."},
                        "ui_theme": {"type": "string", "description": "The new UI theme (e.g., 'dark', 'light')."}
                    },
                    "required": ["user_id"]
                }
            }
        }

class UpdateTopicSubscription(Tool):
    """Updates a user's subscription to a research topic."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        topic = kwargs.get('topic')
        action = kwargs.get('action')

        if not all([user_id, topic, action]):
            return json.dumps({"error": "user_id, topic, and action are required."})

        subscriptions = data.get('subscriptions', [])

        if action.lower() == 'add':
            if any(sub.get('user_id') == user_id and sub.get('topic') == topic for sub in subscriptions):
                return json.dumps({"success": False, "message": "User is already subscribed to this topic."})

            new_sub_id = f"sub_topic_{uuid.uuid4().hex[:6]}"
            new_subscription = {"subscription_id": new_sub_id, "user_id": user_id, "topic": topic}
            subscriptions.append(new_subscription)
            return json.dumps({"success": True, "subscription": new_subscription})

        elif action.lower() == 'remove':
            initial_count = len(subscriptions)
            data['subscriptions'] = [sub for sub in subscriptions if not (sub.get('user_id') == user_id and sub.get('topic') == topic)]

            if len(data['subscriptions']) < initial_count:
                return json.dumps({"success": True, "message": f"Subscription to '{topic}' for user '{user_id}' removed."})
            else:
                return json.dumps({"error": "Subscription not found to remove."})

        else:
            return json.dumps({"error": "Invalid action. Must be 'add' or 'remove'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_topic_subscription",
                "description": "Updates a user's subscription to a research topic (adds or removes).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user."},
                        "topic": {"type": "string", "description": "The research topic to subscribe to or unsubscribe from."},
                        "action": {"type": "string", "enum": ["add", "remove"], "description": "The action to perform."}
                    },
                    "required": ["user_id", "topic", "action"]
                }
            }
        }

class DispatchUserAlert(Tool):
    """Dispatches an alert or notification to a user."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        recipient_user_id = kwargs.get('recipient_user_id')
        message_content = kwargs.get('message_content')
        sender_user_id = kwargs.get('sender_user_id', 'system')

        if not all([recipient_user_id, message_content]):
            return json.dumps({"error": "recipient_user_id and message_content are required."})

        notifications = data.get('notifications', [])
        new_alert = {
            "notification_id": f"notif_{uuid.uuid4().hex[:6]}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message_content,
            "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "status": "unread"
        }
        notifications.append(new_alert)

        return json.dumps({"success": True, "alert": new_alert})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "dispatch_user_alert",
                "description": "Dispatches an alert or notification to a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {"type": "string", "description": "The ID of the user who will receive the alert."},
                        "message_content": {"type": "string", "description": "The content of the alert message."},
                        "sender_user_id": {"type": "string", "description": "Optional. The user ID of the sender. Defaults to 'system'."}
                    },
                    "required": ["recipient_user_id", "message_content"]
                }
            }
        }

TOOLS = [
    FindResearcherProfiles(),
    RetrievePapers(),
    SearchSubmissions(),
    GetProjectDetails(),
    GetCitationGraph(),
    FindCollaborationNetwork(),
    AddCitation(),
    UpdateArticleMetadata(),
    GetAuthorMetrics(),
    SuggestReviewers(),
    GetMostCitedArticles(),
    FindCommonCollaborators(),
    UpdateSubmission(),
    RegisterProject(),
    CreateSubmission(),
    AddResearchNote(),
    UpdateProject(),
    RetrieveFundingInfo(),
    CreateReview(),
    CreateArticle(),
    ConfigureProfileSettings(),
    UpdateTopicSubscription(),
    DispatchUserAlert()
]
