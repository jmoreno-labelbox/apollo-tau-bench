import json
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


class FindResearcherProfiles(Tool):
    """Looks for users based on their name, research area, user_id, or institution."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, research_field: str = None, user_id: str = None, institution: str = None) -> str:
        if not any([name, research_field, user_id, institution]):
            payload = data.get("users", {}).values()
            out = json.dumps(payload, indent=2)
            return out

        users = data.get("users", {}).values()
        results = [
            user
            for user in users.values()
            if (not name or name.lower() in user.get("name", "").lower())
            and (
                not research_field
                or research_field.lower() in user.get("research_field", "").lower()
            )
            and (not user_id or user.get("person_id") == user_id)
            and (not institution or institution.lower() in user.get("organization", "").lower())
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindResearcherProfiles",
                "description": "Searches for users by their name, research field, user_id, or institution.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "research_field": {"type": "string"},
                        "user_id": {"type": "string"},
                        "institution": {"type": "string"},
                    },
                },
            },
        }


class RetrievePapers(Tool):
    """Seeks academic articles using ID, subject, title, year, or author name."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        *, 
        article_id: Any = None, 
        topic: str = None, 
        title: str = None, 
        year: int = None, 
        publication_year: int = None,
        author_name: str = None
    ) -> str:
        articles: list = data.get("articles", {}).values()

        if article_id:
            for article in articles.values():
                if article.get("article_id") == article_id:
                    payload = [article]
                    out = json.dumps(payload, indent=2)
                    return out
            payload = []
            out = json.dumps(payload)
            return out

        # Use publication_year if provided, otherwise fall back to year
        search_year = publication_year if publication_year is not None else year
        
        results = [
            a
            for a in articles.values()
            if (not topic or topic.lower() in a.get("topic", "").lower())
            and (not title or title.lower() in a.get("title", "").lower())
            and (not search_year or search_year == a.get("publication_year"))
            and (
                not author_name
                or any(
                    author_name.lower() in author.lower()
                    for author in a.get("authors", [])
                )
            )
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RetrievePapers",
                "description": "Searches for academic articles by ID, topic, title, publication year, or author name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string"},
                        "topic": {"type": "string"},
                        "title": {"type": "string"},
                        "year": {"type": "integer"},
                        "publication_year": {"type": "integer"},
                        "author_name": {"type": "string"},
                    },
                },
            },
        }


class SearchSubmissions(Tool):
    """Finds submissions using submission_id, article_id, or a specific review_id."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: str = None, article_id: str = None, review_id: str = None) -> str:
        # Functionality derived from the previous SearchReviews tool
        if review_id:
            reviews = data.get("reviews", {}).values()
            target_review = next(
                (r for r in reviews.values() if r.get("review_id") == review_id), None
            )
            if not target_review:
                payload = []
                out = json.dumps(payload)
                return out

            # Utilize the submission_id from the review to locate the submission
            submission_id_from_review = target_review.get("submission_id")
            submissions = data.get("submissions", {}).values()
            results = [
                s
                for s in submissions.values()
                if s.get("submission_id") == submission_id_from_review
            ]

            if results:
                results[0][
                    "review_details"
                ] = target_review  # Include the complete review object
            payload = results
            out = json.dumps(payload, indent=2)
            return out

        if not submission_id and not article_id:
            payload = data.get("submissions", {}).values()
            out = json.dumps(payload, indent=2)
            return out

        submissions = data.get("submissions", {}).values()
        results = [
            s
            for s in submissions.values()
            if (not submission_id or s.get("submission_id") == submission_id)
            and (not article_id or s.get("article_id") == article_id)
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchSubmissions",
                "description": "Searches for submissions by submission_id, article_id, or indirectly via a review_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string"},
                        "article_id": {"type": "string"},
                        "review_id": {
                            "type": "string",
                            "description": "If provided, finds the submission associated with this review.",
                        },
                    },
                },
            },
        }


class GetProjectDetails(Tool):
    """Looks for projects using project_name, linked_article_id, or project_id."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        project_name: str = None, 
        linked_article_id: str = None, 
        project_id: str = None
    ) -> str:
        if not any([project_name, linked_article_id, project_id]):
            payload = data.get("projects", {}).values()
            out = json.dumps(payload, indent=2)
            return out
        projects = data.get("projects", {}).values()
        results = [
            p
            for p in projects.values()
            if (
                not project_name
                or project_name.lower() in p.get("project_name", "").lower()
            )
            and (
                not linked_article_id
                or linked_article_id in p.get("linked_articles", [])
            )
            and (not project_id or p.get("project_id") == project_id)
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectDetails",
                "description": "Searches for projects by project_name, linked_article_id, or project_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string"},
                        "linked_article_id": {"type": "string"},
                        "project_id": {"type": "string"},
                    },
                },
            },
        }


class GetCitationGraph(Tool):
    """
    Retrieves the citation graph for a particular article.
    If a second article ID is supplied through 'compare_with_article_id', it identifies the shared citations between both.
    """

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, compare_with_article_id: Any = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        citations = data.get("citations", {}).values()

        # Functionality taken from the previous FindCommonCitations tool
        if compare_with_article_id:
            cites1 = {
                c["referenced_paper_id"]
                for c in citations.values()
                if c.get("origin_paper_id") == article_id
            }
            cites2 = {
                c["referenced_paper_id"]
                for c in citations.values()
                if c.get("origin_paper_id") == compare_with_article_id
            }
            common_citations = list(cites1.intersection(cites2))
            payload = {
                "article1_id": article_id,
                "article2_id": compare_with_article_id,
                "common_citations": common_citations,
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Initial logic of GetCitationGraph
        else:
            cited_by = [
                c["origin_paper_id"]
                for c in citations.values()
                if c.get("referenced_paper_id") == article_id
            ]
            cites = [
                c["referenced_paper_id"]
                for c in citations.values()
                if c.get("origin_paper_id") == article_id
            ]
            result = {"article_id": article_id, "cited_by": cited_by, "cites": cites}
            payload = result
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCitationGraph",
                "description": "Gets the citation graph for an article, or finds common citations between two articles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string"},
                        "compare_with_article_id": {
                            "type": "string",
                            "description": "If provided, finds common articles cited by both this article and the main article_id.",
                        },
                    },
                    "required": ["article_id"],
                },
            },
        }


class FindCollaborationNetwork(Tool):
    """
    Identifies the collaboration network for a specified author.
    Can be limited to examine only a particular list of possible collaborators.
    """

    @staticmethod
    def invoke(data: dict[str, Any], author_name: Any = None, authors_to_check: Any = None) -> str:
        author_name = author_name
        authors_to_check = authors_to_check
        if not author_name:
            payload = {"error": "author_name is required."}
            out = json.dumps(payload)
            return out

        # Retrieve all articles authored by the primary author
        articles = [
            a for a in data.get("articles", {}).values() if author_name in a.get("authors", [])
        ]

        # Tally all collaborators associated with those articles
        all_collaborators = Counter()
        for article in articles.values()):
            for author in article.get("authors", []):
                if author != author_name:
                    all_collaborators[author] += 1

        # If a designated list of authors is given, refine the results
        if authors_to_check:
            final_counts = {
                author: all_collaborators.get(author, 0) for author in authors_to_check
            }
            payload = final_counts
            out = json.dumps(payload, indent=2)
            return out
        payload = dict(all_collaborators)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCollaborationNetwork",
                "description": "Finds the collaboration network for an author, optionally checking against a specific list of names.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "author_name": {"type": "string"},
                        "authors_to_check": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["author_name"],
                },
            },
        }


class AddCitation(Tool):
    """Inserts a new citation."""

    @staticmethod
    def invoke(data: dict[str, Any], source_article_id: str = None, cited_article_id: str = None, context: str = None) -> str:
        if not all([source_article_id, cited_article_id]):
            payload = {"error": "source_article_id and cited_article_id are required."}
            out = json.dumps(
                payload)
            return out
        new_citation = {
            "citation_id": f"cit_{uuid.uuid4().hex[:4]}",
            "source_article_id": source_article_id,
            "cited_article_id": cited_article_id,
            "citation_context": context,
        }
        data["citations"][new_citation["citation_id"]] = new_citation
        payload = {"success": True, "citation": new_citation}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddCitation",
                "description": "Adds a new citation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_article_id": {"type": "string"},
                        "cited_article_id": {"type": "string"},
                        "context": {"type": "string"},
                    },
                    "required": ["source_article_id", "cited_article_id"],
                },
            },
        }


class UpdateArticleMetadata(Tool):
    """Modifies article metadata for designated fields."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        article_id: Any = None,
        title: str = None,
        authors: list[str] = None,
        publication_year: int = None,
        topic: str = None,
        abstract: str = None,
        status: str = None,
        keywords: list[str] = None
    ) -> str:
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
            payload = {"error": "Article not found."}
            out = json.dumps(payload)
            return out

        updatable_fields = [
            "title",
            "authors",
            "publication_year",
            "topic",
            "abstract",
            "status",
            "keywords",
        ]
        updates = {
            "title": title,
            "authors": authors,
            "publication_year": publication_year,
            "topic": topic,
            "abstract": abstract,
            "status": status,
            "keywords": keywords,
        }
        for key, value in updates.items():
            if key in updatable_fields and value is not None:
                article[key] = value
        payload = {"success": True, "article": article}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateArticleMetadata",
                "description": "Updates article metadata (e.g., topic, status, keywords).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string"},
                        "topic": {"type": "string"},
                        "status": {"type": "string"},
                        "keywords": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["article_id"],
                },
            },
        }


class GetAuthorMetrics(Tool):
    """Retrieves various metrics for an author."""

    @staticmethod
    def invoke(data: dict[str, Any], author_name: Any = None) -> str:
        author_name = author_name
        if not author_name:
            payload = {"error": "author_name is required."}
            out = json.dumps(payload)
            return out
        articles = [
            a for a in data.get("articles", {}).values() if author_name in a.get("authors", [])
        ]
        if not articles:
            payload = {"total_publications": 0, "total_citations": 0, "h_index": 0}
            out = json.dumps(
                payload)
            return out
        citations = data.get("citations", {}).values()
        total_citations = 0
        citation_counts = []
        for article in articles.values():
            count = len(
                [
                    c
                    for c in citations.values()
                    if c.get("referenced_paper_id") == article["paper_id"]
                ]
            )
            total_citations += count
            citation_counts.append(count)
        citation_counts.sort(reverse=True)
        h_index = 0
        for i, count in enumerate(citation_counts):
            if count >= i + 1:
                h_index = i + 1
            else:
                break
        payload = {
                "total_publications": len(articles),
                "total_citations": total_citations,
                "h_index": h_index,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuthorMetrics",
                "description": "Gets multiple metrics for an author.",
                "parameters": {
                    "type": "object",
                    "properties": {"author_name": {"type": "string"}},
                    "required": ["author_name"],
                },
            },
        }


class SuggestReviewers(Tool):
    """Recommends possible reviewers for an article, allowing for the exclusion of specific authors."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, exclude_authors: Any = None) -> str:
        article_id = article_id
        exclude_authors = exclude_authors
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out
        article = next(
            (a for a in data.get("articles", {}).values() if a.get("article_id") == article_id),
            None,
        )
        if not article:
            payload = {"error": "Article not found."}
            out = json.dumps(payload)
            return out
        topic = article.get("topic")
        authors = [
            a.get("authors")
            for a in data.get("articles", {}).values()
            if a.get("topic") == topic and a.get("article_id") != article_id
        ]
        authors = [author for sublist in authors for author in sublist]
        authors = [
            author for author in dict.fromkeys(authors) if author not in exclude_authors
        ]
        payload = {"suggested_reviewers": authors}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SuggestReviewers",
                "description": "Suggests potential reviewers for an article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string"},
                        "exclude_authors": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["article_id"],
                },
            },
        }


class GetMostCitedArticles(Tool):
    """Utility to obtain a list of the most referenced articles."""

    @staticmethod
    def invoke(data: dict[str, Any], citations: list[dict[str, Any]] = []) -> str:
        cited_ids = [c["referenced_paper_id"] for c in citations.values()]
        citation_counts = Counter(cited_ids)
        sorted_articles = sorted(
            citation_counts.items(), key=lambda item: item[1], reverse=True
        )
        result = [
            {"article_id": article_id, "citation_count": count}
            for article_id, count in sorted_articles
        ]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMostCitedArticles",
                "description": "Returns a list of articles sorted by how many times they have been cited.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class FindCommonCollaborators(Tool):
    """Identifies shared collaborators between two authors."""

    @staticmethod
    def invoke(data: dict[str, Any], author1_name: Any = None, author2_name: Any = None) -> str:
        if not all([author1_name, author2_name]):
            payload = {"error": "author1_name and author2_name are required."}
            out = json.dumps(payload)
            return out
        articles1 = [
            a for a in data.get("articles", {}).values() if author1_name in a.get("authors", [])
        ]
        collaborators1 = {
            author
            for article in articles1
            for author in article.get("authors", [])
            if author != author1_name
        }
        articles2 = [
            a for a in data.get("articles", {}).values() if author2_name in a.get("authors", [])
        ]
        collaborators2 = {
            author
            for article in articles2
            for author in article.get("authors", [])
            if author != author2_name
        }
        common_collaborators = list(collaborators1.intersection(collaborators2))
        payload = {"common_collaborators": common_collaborators}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCommonCollaborators",
                "description": "Finds common collaborators between two authors.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "author1_name": {"type": "string"},
                        "author2_name": {"type": "string"},
                    },
                    "required": ["author1_name", "author2_name"],
                },
            },
        }


class UpdateSubmission(Tool):
    """Modifies a submission's status or replaces its list of reviewers."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, reviewers: Any = None, status: str = None) -> str:
        submission_id = submission_id
        if not submission_id:
            payload = {"error": "submission_id is required."}
            out = json.dumps(payload)
            return out

        submission = next(
            (
                s
                for s in data.get("submissions", {}).values()
                if s.get("proposal_id") == submission_id
            ),
            None,
        )
        if not submission:
            payload = {"error": "Submission not found."}
            out = json.dumps(payload)
            return out

        if reviewers is not None:
            provided_reviewers = reviewers
            users = data.get("users", {}).values()

            valid_reviewer_ids = []
            for reviewer_item in provided_reviewers:
                if any(u.get("person_id") == reviewer_item for u in users.values()):
                    valid_reviewer_ids.append(reviewer_item)
                else:
                    found_user = next(
                        (u for u in users.values() if u.get("label") == reviewer_item), None
                    )
                    if found_user:
                        valid_reviewer_ids.append(found_user["person_id"])

            submission["allocated_evaluators"] = sorted(list(set(valid_reviewer_ids)))

        if status is not None:
            submission["state"] = status
        payload = {"success": True, "submission": submission}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSubmission",
                "description": "Updates a submission's status or overwrites its list of reviewers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string"},
                        "reviewers": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "description": "List of reviewer user_ids or names to assign.",
                            },
                        },
                        "status": {"type": "string"},
                    },
                    "required": ["submission_id"],
                },
            },
        }


class RegisterProject(Tool):
    """Establishes a new research project."""

    @staticmethod
    def invoke(data: dict[str, Any], project_name: str = None, lead_researcher_id: Any = None, linked_article_id: Any = None, project_id_override: Any = None) -> str:
        if not all([project_name, lead_researcher_id, linked_article_id]):
            payload = {
                    "error": "project_name, lead_researcher_id, and linked_article_id are required."
                }
            out = json.dumps(
                payload)
            return out
        new_project = {
            "project_id": (
                project_id_override
                if project_id_override
                else f"proj_{uuid.uuid4().hex[:4]}"
            ),
            "project_name": project_name,
            "lead_researcher_id": lead_researcher_id,
            "status": "active",
            "start_date": "2025-06-24",
            "end_date": None,
            "linked_articles": [linked_article_id],
            "funding_source_id": None,
        }
        data["projects"][new_project["project_id"]] = new_project
        payload = {"success": True, "project": new_project}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterProject",
                "description": "Creates a new research project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string"},
                        "lead_researcher_id": {"type": "string"},
                        "linked_article_id": {"type": "string"},
                        "project_id_override": {"type": "string"},
                    },
                    "required": [
                        "project_name",
                        "lead_researcher_id",
                        "linked_article_id",
                    ],
                },
            },
        }


class CreateSubmission(Tool):
    """Initiates a new article submission."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, submission_id_override: Any = None, author_user_id: Any = None) -> str:
        if not all([article_id, author_user_id]):
            payload = {"error": "article_id and author_user_id are required."}
            out = json.dumps(payload)
            return out
        new_submission = {
            "submission_id": (
                submission_id_override
                if submission_id_override
                else f"sub_{uuid.uuid4().hex[:4]}"
            ),
            "article_id": article_id,
            "author_user_id": author_user_id,
            "submission_date": "2025-06-24",
            "status": "submitted",
            "assigned_reviewers": [],
        }
        data["submissions"][new_submission["submission_id"]] = new_submission
        payload = {"success": True, "submission": new_submission}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSubmission",
                "description": "Creates a new article submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string"},
                        "author_user_id": {"type": "string"},
                        "submission_id_override": {"type": "string"},
                    },
                    "required": ["article_id", "author_user_id"],
                },
            },
        }


class AddResearchNote(Tool):
    """Adds a new record in the research_logs."""

    @staticmethod
    def invoke(data: dict[str, Any], researcher_id: str = None, article_id: str = None, notes: str = None, relevance: str = "medium", log_id_override: Any = None) -> str:
        if not all([researcher_id, article_id, notes]):
            payload = {"error": "researcher_id, article_id, and notes are required."}
            out = json.dumps(payload)
            return out
        new_log = {
            "log_id": (
                log_id_override if log_id_override else f"log_{uuid.uuid4().hex[:4]}"
            ),
            "researcher_id": researcher_id,
            "article_id": article_id,
            "entry_date": "2025-06-24",
            "notes": notes,
            "relevance": relevance,
        }
        data["research_logs"][new_log["research_log_id"]] = new_log
        payload = {"success": True, "log_entry": new_log}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddResearchNote",
                "description": "Creates a new entry in the research_logs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "researcher_id": {"type": "string"},
                        "article_id": {"type": "string"},
                        "notes": {"type": "string"},
                        "relevance": {"type": "string"},
                        "log_id_override": {"type": "string"},
                    },
                    "required": ["researcher_id", "article_id", "notes"],
                },
            },
        }


class UpdateProject(Tool):
    """Modifies the status, collaborators, linked articles, or funding source of an existing project."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        project_id: Any = None,
        project_name: str = None,
        status: str = None,
        end_date: str = None,
        funding_source_id: Any = None,
        linked_articles: Any = None,
        add_collaborators: Any = None
    ) -> str:
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
            payload = {"error": "Project not found."}
            out = json.dumps(payload)
            return out

        standard_updatable_fields = [
            "project_name",
            "status",
            "end_date",
            "funding_source_id",
        ]
        for key, value in {
            "project_name": project_name,
            "status": status,
            "end_date": end_date,
            "funding_source_id": funding_source_id,
        }.items():
            if key in standard_updatable_fields:
                project[key] = value

        if linked_articles is not None:
            project["linked_articles"] = linked_articles

        if add_collaborators is not None:
            if "collaborators" not in project:
                project["collaborators"] = []

            provided_collaborators = add_collaborators
            users = data.get("users", {}).values()

            valid_collaborator_ids = []
            for collab_item in provided_collaborators:
                # Verify if the item is a valid user_id
                if any(u["person_id"] == collab_item for u in users.values()):
                    valid_collaborator_ids.append(collab_item)
                # If not, attempt to search by name
                else:
                    found_user = next(
                        (u for u in users.values() if u["name"] == collab_item), None
                    )
                    if found_user:
                        valid_collaborator_ids.append(found_user["user_id"])

            existing_collaborators = set(project.get("collaborators", []))
            updated_collaborators = sorted(
                list(existing_collaborators.union(set(valid_collaborator_ids)))
            )
            project["collaborators"] = updated_collaborators
        payload = {"success": True, "project": project}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProject",
                "description": "Updates a project's details, such as status, collaborators, linked articles, or funding.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "status": {"type": "string"},
                        "project_name": {"type": "string"},
                        "add_collaborators": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "funding_source_id": {"type": "string"},
                        "linked_articles": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }


class RetrieveFundingInfo(Tool):
    """Looks for funding sources using source_name or funding_source_id."""

    @staticmethod
    def invoke(data: dict[str, Any], source_name: Any = None, funding_source_id: Any = None) -> str:
        if not source_name and not funding_source_id:
            payload = data.get("funding_sources", {}).values()
            out = json.dumps(payload, indent=2)
            return out

        funding_sources = data.get("funding_sources", {}).values()
        results = [
            fs
            for fs in funding_sources.values() if (
                not source_name
                or source_name.lower() in fs.get("source_name", "").lower()
            )
            and (
                not funding_source_id
                or fs.get("funding_source_id") == funding_source_id
            )
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RetrieveFundingInfo",
                "description": "Searches for funding sources by name or ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {"type": "string"},
                        "funding_source_id": {"type": "string"},
                    },
                },
            },
        }


class CreateReview(Tool):
    """Generates a new review for a submission."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        submission_id: str = None,
        reviewer_user_id: str = None,
        content: str = None,
        recommendation: str = None,
        review_id_override: Any = None
    ) -> str:
        if not all([submission_id, reviewer_user_id, content, recommendation]):
            payload = {
                "error": "submission_id, reviewer_user_id, content, and recommendation are required."
            }
            out = json.dumps(payload)
            return out

        new_review = {
            "review_id": (
                review_id_override
                if review_id_override
                else f"rev_{uuid.uuid4().hex[:4]}"
            ),
            "submission_id": submission_id,
            "reviewer_user_id": reviewer_user_id,
            "review_content": content,
            "recommendation": recommendation,
            "review_date": "2025-06-24",
        }
        data["reviews"][new_review["review_id"]] = new_review
        payload = {"success": True, "review": new_review}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReview",
                "description": "Creates a new review for a submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string"},
                        "reviewer_user_id": {"type": "string"},
                        "content": {"type": "string"},
                        "recommendation": {"type": "string"},
                        "review_id_override": {"type": "string"},
                    },
                    "required": [
                        "submission_id",
                        "reviewer_user_id",
                        "content",
                        "recommendation",
                    ],
                },
            },
        }


class CreateArticle(Tool):
    """Establishes a new article record."""

    @staticmethod
    def invoke(data: dict[str, Any], *, title: Any = None, authors: Any = None, topic: Any = None, publication_year: Any = None, article_id_override: Any = None, abstract: str = "...") -> str:
        #Retrieve parameters for the new article
        title = title
        authors = authors
        topic = topic
        publication_year = publication_year
        article_id_override = article_id_override

        if not all([title, authors, topic, publication_year]):
            payload = {"error": "title, authors, topic, and publication_year are required."}
            out = json.dumps(
                payload)
            return out

        new_article = {
            "article_id": (
                article_id_override
                if article_id_override
                else f"art_{uuid.uuid4().hex[:4]}"
            ),
            "title": title,
            "authors": authors,
            "publication_year": publication_year,
            "topic": topic,
            "abstract": abstract,
            "status": "new",
        }
        article_id = new_article["article_id"]
        data["articles"][article_id] = new_article
        payload = {"success": True, "article": new_article}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateArticle",
                "description": "Creates a new article record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "authors": {"type": "array", "items": {"type": "string"}},
                        "topic": {"type": "string"},
                        "publication_year": {"type": "integer"},
                        "abstract": {"type": "string"},
                        "article_id_override": {"type": "string"},
                    },
                    "required": ["title", "authors", "topic", "publication_year"],
                },
            },
        }


class ConfigureProfileSettings(Tool):
    """Sets up a user's profile preferences."""

    @staticmethod
    def invoke(data: dict[str, Any], *, user_id: Any = None, notification_channel: Any = None, ui_theme: Any = None) -> str:
        user_id = user_id
        notification_channel = notification_channel
        ui_theme = ui_theme

        if not user_id:
            payload = {"error": "user_id is required to configure settings."}
            out = json.dumps(payload)
            return out

        if not notification_channel and not ui_theme:
            payload = {
                    "error": "At least one setting (notification_channel or ui_theme) must be provided."
                }
            out = json.dumps(
                payload)
            return out

        preferences = data.get("user_preferences", {}).values()

        user_pref = next(
            (pref for pref in preferences.values() if pref.get("user_id") == user_id), None
        )

        if user_pref:
            if notification_channel:
                user_pref["notification_channel"] = notification_channel
            if ui_theme:
                user_pref["ui_theme"] = ui_theme
            payload = {"success": True, "configured_settings": user_pref}
            out = json.dumps(payload)
            return out
        else:
            new_pref = {
                "preference_id": f"pref_{uuid.uuid4().hex[:4]}",  #Generate a unique ID
                "user_id": user_id,
                "notification_channel": notification_channel,
                "ui_theme": ui_theme,
            }
            if not notification_channel:
                del new_pref["notification_channel"]
            if not ui_theme:
                del new_pref["ui_theme"]

            data["user_preferences"][new_pref["user_preference_id"]] = new_pref
            data["user_preferences"] = (
                preferences  #Ensures that the updated list is saved back to 'data'
            )
            payload = {"success": True, "configured_settings": new_pref}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigureProfileSettings",
                "description": "Configures a user's profile settings, such as notification channel or UI theme. Creates a new preference entry if one does not exist for the user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user whose settings are being configured.",
                        },
                        "notification_channel": {
                            "type": "string",
                            "description": "The new notification channel (e.g., 'email', 'in_app').",
                        },
                        "ui_theme": {
                            "type": "string",
                            "description": "The new UI theme (e.g., 'dark', 'light').",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }


class UpdateTopicSubscription(Tool):
    """Modifies a user's subscription to a research area."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: Any = None, topic: Any = None, action: Any = None) -> str:
        if not all([user_id, topic, action]):
            payload = {"error": "user_id, topic, and action are required."}
            out = json.dumps(payload)
            return out

        subscriptions = data.get("subscriptions", {}).values()

        if action.lower() == "add":
            if any(
                sub.get("user_id") == user_id and sub.get("topic") == topic
                for sub in subscriptions.values()
            ):
                payload = {
                    "success": False,
                    "message": "User is already subscribed to this topic.",
                }
                out = json.dumps(payload)
                return out

            new_sub_id = f"sub_topic_{uuid.uuid4().hex[:6]}"
            new_subscription = {
                "subscription_id": new_sub_id,
                "user_id": user_id,
                "topic": topic,
            }
            data["subscriptions"][subscription_id] = new_subscription
            payload = {"success": True, "subscription": new_subscription}
            out = json.dumps(payload)
            return out

        elif action.lower() == "remove":
            initial_count = len(subscriptions)
            data["subscriptions"] = [
                sub
                for sub in subscriptions.values() if not (sub.get("user_id") == user_id and sub.get("topic") == topic)
            ]

            if len(data["subscriptions"]) < initial_count:
                payload = {
                    "success": True,
                    "message": f"Subscription to '{topic}' for user '{user_id}' removed.",
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
        return {
            "type": "function",
            "function": {
                "name": "UpdateTopicSubscription",
                "description": "Updates a user's subscription to a research topic (adds or removes).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "The research topic to subscribe to or unsubscribe from.",
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


class DispatchUserAlert(Tool):
    """Sends an alert or notification to a user."""

    @staticmethod
    def invoke(data: dict[str, Any], recipient_user_id: Any = None, message_content: Any = None, sender_user_id: Any = None) -> str:
        recipient_user_id = recipient_user_id
        message_content = message_content
        sender_user_id = sender_user_id

        if not all([recipient_user_id, message_content]):
            payload = {"error": "recipient_user_id and message_content are required."}
            out = json.dumps(
                payload)
            return out

        notifications = data.get("notifications", {}).values()
        new_alert = {
            "notification_id": f"notif_{uuid.uuid4().hex[:6]}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message_content,
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "status": "unread",
        }
        data["notifications"][notification_id] = new_alert
        payload = {"success": True, "alert": new_alert}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DispatchUserAlert",
                "description": "Dispatches an alert or notification to a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_user_id": {
                            "type": "string",
                            "description": "The ID of the user who will receive the alert.",
                        },
                        "message_content": {
                            "type": "string",
                            "description": "The content of the alert message.",
                        },
                        "sender_user_id": {
                            "type": "string",
                            "description": "Optional. The user ID of the sender. Defaults to 'system'.",
                        },
                    },
                    "required": ["recipient_user_id", "message_content"],
                },
            },
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
    DispatchUserAlert(),
]
