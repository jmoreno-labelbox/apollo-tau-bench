import json
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class LocatePapers(Tool):
    """Utility for finding academic papers based on topic, title, or year."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        topic: str = None, 
        title: str = None, 
        year: int = None, 
        article_id: str = None
    ) -> str:
        articles: list = data.get("articles", {}).values()
        results = []
        for article in articles.values():
            match = True
            if article_id and article_id != article.get("article_id"):
                match = False
            if topic and topic.lower() not in article.get("topic", "").lower():
                match = False
            if title and title.lower() not in article.get("title", "").lower():
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
                "name": "LocatePapers",
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


class SummarizeAbstract(Tool):
    """Utility for creating a summary of an article's abstract."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        articles = data.get("articles", {}).values()
        for article in articles.values():
            if article.get("article_id") == article_id:
                summary = f"The article '{article.get('title')}' discusses {article.get('topic')}. The abstract focuses on {article.get('abstract')}"
                payload = {"summary": summary}
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
                "name": "SummarizeAbstract",
                "description": "Generates a brief summary of an article's abstract.",
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


class ExtractKeywords(Tool):
    """Utility for retrieving keywords from an article's abstract."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        articles = data.get("articles", {}).values()
        for article in articles.values():
            if article.get("article_id") == article_id:
                abstract = article.get("abstract", "").lower()
                potential_keywords = [
                    "transformer",
                    "crispr-cas9",
                    "biomarkers",
                    "dark matter",
                    "quantum computing",
                    "gene therapy",
                ]
                found_keywords = [kw for kw in potential_keywords.values() if kw in abstract]
                payload = found_keywords
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
                "name": "ExtractKeywords",
                "description": "Extracts a list of pre-defined keywords from an article's abstract.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The unique ID of the article to extract keywords from.",
                        }
                    },
                    "required": ["article_id"],
                },
            },
        }


class FindUsersByCriteria(Tool):
    """Utility for locating users based on different criteria."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: Any = None, name: Any = None, research_field: Any = None, availability: Any = None, institution: Any = None) -> str:
        users = data.get("users", {}).values()
        results = []
        for user in users.values():
            match = True
            if user_id and user_id != user.get("person_id"):
                match = False
            if name and name.lower() not in user.get("name", "").lower():
                match = False
            if research_field and research_field.lower() not in user.get("research_field", "").lower():
                match = False
            if availability and availability != user.get("availability"):
                match = False
            if institution and institution == user.get("institution"):
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
                "name": "FindUsersByCriteria",
                "description": "Finds researchers by ID, name, research field, availability, or to exclude an institution.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the user.",
                        },
                        "research_field": {
                            "type": "string",
                            "description": "A research field to filter by.",
                        },
                        "availability": {
                            "type": "string",
                            "description": "The availability status (e.g., 'available').",
                        },
                        "institution": {
                            "type": "string",
                            "description": "Excludes users who belong to this institution.",
                        },
                    },
                    "required": [],
                },
            },
        }


class QuerySubmissions(Tool):
    """Utility for querying submissions based on article or status."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: str = None, article_id: str = None, status: str = None) -> str:
        submissions = data.get("submissions", {}).values()
        results = []
        for sub in submissions.values():
            match = True
            if submission_id and submission_id != sub.get("submission_id"):
                match = False
            if article_id and article_id != sub.get("article_id"):
                match = False
            if status and status != sub.get("status"):
                match = False
            if match:
                results.append(sub)
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "QuerySubmissions",
                "description": "Queries article submissions by submission ID, article ID or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The unique ID of the submission.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The associated article's ID.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the submission (e.g., 'pending', 'under review').",
                        },
                    },
                    "required": [],
                },
            },
        }


class GenerateNewReview(Tool):
    """Utility for creating a new review entry for a submission."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: str = None, reviewer_user_id: str = None, score: int = None, comments: str = None) -> str:
        review_id = f"rev_{len(data.get('reviews', {})) + 1:02d}"
        new_review = {
            "review_id": review_id,
            "submission_id": submission_id,
            "reviewer_user_id": reviewer_user_id,
            "score": score,
            "comments": comments,
            "review_date": datetime.now().strftime("%Y-%m-%d"),
        }
        data["reviews"][new_review["review_id"]] = new_review
        payload = new_review
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateNewReview",
                "description": "Generates a new review for a submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to be reviewed.",
                        },
                        "reviewer_user_id": {
                            "type": "string",
                            "description": "The ID of the reviewing user.",
                        },
                        "score": {
                            "type": "integer",
                            "description": "The review score (1-10).",
                        },
                        "comments": {
                            "type": "string",
                            "description": "Detailed comments for the review.",
                        },
                    },
                    "required": [
                        "submission_id",
                        "reviewer_user_id",
                        "score",
                        "comments",
                    ],
                },
            },
        }


class SearchReviews(Tool):
    """Utility for finding reviews based on submission and reviewer."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: str = None, reviewer_user_id: str = None) -> str:
        reviews = data.get("reviews", {}).values()
        results = [
            r
            for r in reviews.values() if r.get("submission_id") == submission_id
            and r.get("reviewer_user_id") == reviewer_user_id
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchReviews",
                "description": "Searches for specific reviews by submission and reviewer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The submission's ID.",
                        },
                        "reviewer_user_id": {
                            "type": "string",
                            "description": "The reviewer's ID.",
                        },
                    },
                    "required": ["submission_id", "reviewer_user_id"],
                },
            },
        }


class QueryProjects(Tool):
    """Utility for querying projects using ID or name."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None, project_name: str = None, funding_source_id: str = None) -> str:
        projects = data.get("projects", {}).values()
        results = []
        for proj in projects.values():
            match = True
            if project_id and project_id != proj.get("project_id"):
                match = False
            if project_name and project_name.lower() not in proj.get("project_name", "").lower():
                match = False
            if funding_source_id and funding_source_id != proj.get("funding_source_id"):
                match = False
            if match:
                results.append(proj)
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "QueryProjects",
                "description": "Queries research projects by ID, name, or funding source ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project's ID.",
                        },
                        "project_name": {
                            "type": "string",
                            "description": "The project's name.",
                        },
                        "funding_source_id": {
                            "type": "string",
                            "description": "The funding source ID to filter projects.",
                        },
                    },
                    "required": [],
                },
            },
        }


class LocateFundingSources(Tool):
    """Utility for identifying funding sources based on research area and availability."""

    @staticmethod
    def invoke(data: dict[str, Any], area: str = None, status: str = None, funding_source_id: str = None, source_name: str = None) -> str:
        sources = data.get("funding_sources", {}).values()
        results = []
        area = area.lower() if area else ""
        status = status.lower() if status else ""
        source_name = source_name.lower() if source_name else ""

        for s in sources.values():
            match_area = not area or area in s.get("focus_area", "").lower()
            match_status = not status or status == s.get("status", "").lower()
            match_id = not funding_source_id or funding_source_id == s.get("sponsor_id")
            match_name = not source_name or source_name in s.get("source_name", "").lower()

            if match_area and match_status and match_id and match_name:
                results.append(s)
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LocateFundingSources",
                "description": "Locates funding sources by research area, availability, funding source ID, or source name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "area": {
                            "type": "string",
                            "description": "The research area (e.g., 'AI', 'Medical Research').",
                        },
                        "status": {
                            "type": "string",
                            "description": "The availability status of the grant (e.g., 'available').",
                        },
                        "funding_source_id": {
                            "type": "string",
                            "description": "The ID of the funding source to search for.",
                        },
                        "source_name": {
                            "type": "string",
                            "description": "The name of the funding source to search for.",
                        },
                    },
                    "required": [],
                },
            },
        }


class AddEntryToLog(Tool):
    """Utility for appending a log note to a user, project, submission, or article."""

    @staticmethod
    def invoke(data: dict[str, Any], *, notes: Any = None, user_id: str = None, project_id: str = None, submission_id: str = None, article_id: str = None) -> str:
        target_list = None
        target_id_key = None
        target_id_value = None

        if user_id is not None:
            target_list = data.get("users", {}).values()
            target_id_key = "user_id"
            target_id_value = user_id
        elif project_id is not None:
            target_list = data.get("projects", {}).values()
            target_id_key = "project_id"
            target_id_value = project_id
        elif submission_id is not None:
            target_list = data.get("submissions", {}).values()
            target_id_key = "submission_id"
            target_id_value = submission_id
        elif article_id is not None:
            target_list = data.get("articles", {}).values()
            target_id_key = "article_id"
            target_id_value = article_id
        else:
            payload = {
                "error": "Either user_id, project_id, submission_id, or article_id is required."
            }
            out = json.dumps(payload, indent=2)
            return out

        for item in target_list.values():
            if item.get(target_id_key) == target_id_value:
                if "logs" not in item:
                    item["logs"] = []
                item["logs"].append(notes)
                payload = item
                out = json.dumps(payload, indent=2)
                return out
        payload = {
            "error": f"Item with ID '{target_id_value}' not found in the specified table."
        }
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddEntryToLog",
                "description": "Adds a log entry for a user, project, submission, or article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user to add the log to.",
                        },
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project to add the log to.",
                        },
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to add the log to.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to add the log to.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "The content of the log note.",
                        },
                    },
                    "required": ["notes"],
                },
            },
        }


class DeleteCitation(Tool):
    """Utility for removing a citation record."""

    @staticmethod
    def invoke(data: dict[str, Any], citation_id: Any = None) -> str:
        citations = data.get("citations", {}).values()
        original_count = len(citations)
        data["citations"] = [
            c for c in citations.values() if c.get("citation_id") != citation_id
        ]
        if len(data["citations"]) < original_count:
            payload = {
                "status": "success",
                "citation_id": citation_id,
                "message": "Citation deleted.",
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": f"Citation with ID {citation_id} not found."}
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteCitation",
                "description": "Deletes a specific citation record by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "citation_id": {
                            "type": "string",
                            "description": "The unique ID of the citation to delete.",
                        }
                    },
                    "required": ["citation_id"],
                },
            },
        }


class QueryCitationConnections(Tool):
    """Utility for finding citations associated with an article."""

    @staticmethod
    def invoke(data: dict[str, Any], direction: Any = None, source_article_id: str = None, cited_article_id: str = None) -> str:
        citations = data.get("citations", {}).values()
        results = []

        if direction == "from" and source_article_id is not None:
            source_id = source_article_id
            results = [c for c in citations.values() if c.get("source_article_id") == source_id]

        elif direction == "to" and cited_article_id is not None:
            cited_id = cited_article_id
            results = [c for c in citations.values() if c.get("referenced_paper_id") == cited_id]
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "QueryCitationConnections",
                "description": "Searches for citations, either from a source article or to a cited article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_article_id": {
                            "type": "string",
                            "description": "The ID of the article that made the citation.",
                        },
                        "cited_article_id": {
                            "type": "string",
                            "description": "The ID of the article that received the citation.",
                        },
                        "direction": {
                            "type": "string",
                            "enum": ["from", "to"],
                            "description": "The direction of the citation search.",
                        },
                    },
                    "required": ["direction"],
                },
            },
        }


class RetrieveCitationData(Tool):
    """Utility for retrieving complete details of a particular citation."""

    @staticmethod
    def invoke(data: dict[str, Any], citation_id: Any = None) -> str:
        for citation in data.get("citations", {}).values():
            if citation.get("citation_id") == citation_id:
                payload = citation
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Citation with ID {citation_id} not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RetrieveCitationData",
                "description": "Retrieves the full details of a specific citation by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "citation_id": {
                            "type": "string",
                            "description": "The unique ID of the citation.",
                        }
                    },
                    "required": ["citation_id"],
                },
            },
        }


class InitiateProject(Tool):
    """Utility for establishing a new research project."""

    @staticmethod
    def invoke(data: dict[str, Any], project_name: str = None, lead_researcher_id: str = None, funding_source_id: str = None) -> str:
        projects = data.get("projects", {}).values()
        new_project = {
            "project_id": f"proj_{len(projects) + 1:02d}",
            "project_name": project_name,
            "lead_researcher_id": lead_researcher_id,
            "status": "new",
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "end_date": None,
            "linked_articles": [],
            "funding_source_id": funding_source_id,
            "logs": [],
        }
        data["projects"][project_id] = new_project
        payload = new_project
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InitiateProject",
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
                            "description": "The ID of the funding source for the project.",
                        },
                    },
                    "required": ["project_name", "lead_researcher_id"],
                },
            },
        }


class RegisterArticleRecord(Tool):
    """Utility for generating a new article record."""

    @staticmethod
    def invoke(data: dict[str, Any], title: str, authors: list = None, topic: str = None, abstract: str = None) -> str:
        if authors is None:
            authors = []
        articles = data.get("articles", {}).values()
        new_article = {
            "article_id": f"art_{len(articles) + 1:02d}",
            "title": title,
            "authors": authors,
            "publication_year": datetime.now().year,
            "topic": topic,
            "abstract": abstract,
            "status": "draft",
        }
        data["articles"][article_id] = new_article
        payload = new_article
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterArticleRecord",
                "description": "Creates a new draft article record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "The title of the article.",
                        },
                        "authors": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of author names.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "The primary topic of the article.",
                        },
                        "abstract": {
                            "type": "string",
                            "description": "The abstract of the article.",
                        },
                    },
                    "required": ["title", "authors", "topic", "abstract"],
                },
            },
        }


class SubmitArticleForReview(Tool):
    """Utility for submitting a new article."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: str = None, author_user_id: str = None) -> str:
        submissions = data.get("submissions", {}).values()
        new_submission = {
            "submission_id": f"sub_{len(submissions) + 1:02d}",
            "article_id": article_id,
            "author_user_id": author_user_id,
            "submission_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "submitted",
            "assigned_reviewers": [],
        }
        data["submissions"][submission_id] = new_submission
        payload = new_submission
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SubmitArticleForReview",
                "description": "Creates a new article submission for the review process.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article being submitted.",
                        },
                        "author_user_id": {
                            "type": "string",
                            "description": "The ID of the submitting author.",
                        },
                    },
                    "required": ["article_id", "author_user_id"],
                },
            },
        }


class LinkCitedArticle(Tool):
    """Utility for establishing a new citation record linking two articles."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        source_article_id: str = None,
        cited_article_id: str = None,
        citation_context: str = "Citation added for reference."
    ) -> str:
        citations = data.get("citations", {}).values()
        new_citation_id = f"cit_{len(citations) + 1:02d}"
        new_citation = {
            "reference_id": new_citation_id,
            "origin_paper_id": source_article_id,
            "referenced_paper_id": cited_article_id,
            "reference_context": citation_context,
        }
        data["citations"][citation_id] = new_citation
        payload = new_citation
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkCitedArticle",
                "description": "Creates a new citation record to link a source article to a cited article.",
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
                            "description": "A brief description of the citation's context.",
                        },
                    },
                    "required": ["source_article_id", "cited_article_id"],
                },
            },
        }


class DeleteReview(Tool):
    """Utility for removing a review record."""

    @staticmethod
    def invoke(data: dict[str, Any], review_id: Any = None) -> str:
        reviews = data.get("reviews", {}).values()
        original_count = len(reviews)
        data["reviews"] = [r for r in reviews.values() if r.get("review_id") != review_id]
        if len(data["reviews"]) < original_count:
            payload = {
                "status": "success",
                "review_id": review_id,
                "message": "Review deleted.",
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": f"Review with ID {review_id} not found."}
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteReview",
                "description": "Deletes a specific review record by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "review_id": {
                            "type": "string",
                            "description": "The unique ID of the review to delete.",
                        }
                    },
                    "required": ["review_id"],
                },
            },
        }


class ModifyRecord(Tool):
    """Utility for updating fields of any existing record, including project, article, user, submission, or funding source."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        record_type: str = None, 
        record_id: str = None, 
        modifications: dict[str, Any] = None,
        status: str = None,
        linked_articles: list = None,
        funding_source_id: str = None,
        lead_researcher_id: Any = None,
        assigned_reviewers: list = None,
        publication_date: str = None,
        end_date: str = None,
        logs: list = None,
        institution: str = None,
        team_members: list = None
    ) -> str:
        if not record_type or not record_id:
            payload = {"error": "The parameters 'record_type' and 'record_id' are required."}
            out = json.dumps(payload, indent=2)
            return out

        table_map = {
            "article": (data.get("articles", {}).values(), "article_id"),
            "project": (data.get("projects", {}).values(), "project_id"),
            "user": (data.get("users", {}).values(), "user_id"),
            "submission": (data.get("submissions", {}).values(), "submission_id"),
            "funding_source": (data.get("funding_sources", {}).values(), "funding_source_id"),
            "user_preference": (data.get("user_preferences", {}).values(), "preference_id"),
            "subscription": (data.get("subscriptions", {}).values(), "subscription_id"),
        }

        if record_type not in table_map:
            payload = {"error": f"Invalid record type: {record_type}"}
            out = json.dumps(payload, indent=2)
            return out

        target_list, id_key = table_map[record_type]

        for item in target_list.values():
            if item.get(id_key) == record_id:
                # Apply modifications from the modifications parameter
                if modifications:
                    for key, value in modifications.items():
                        item[key] = value
                
                # Apply modifications from individual parameters
                individual_params = {
                    "status": status,
                    "linked_articles": linked_articles,
                    "funding_source_id": funding_source_id,
                    "lead_researcher_id": lead_researcher_id,
                    "assigned_reviewers": assigned_reviewers,
                    "publication_date": publication_date,
                    "end_date": end_date,
                    "logs": logs,
                    "institution": institution,
                    "team_members": team_members
                }
                
                for key, value in individual_params.items():
                    if value is not None:
                        item[key] = value
                        
                payload = item
                out = json.dumps(payload, indent=2)
                return out
        payload = {
            "error": f"Record of type '{record_type}' with ID '{record_id}' not found."
        }
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ModifyRecord",
                "description": "Modifies fields of an existing record, such as a project, article, user, submission, or funding source. Can accept individual field parameters or a modifications object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record_type": {
                            "type": "string",
                            "description": "The type of the record to be modified.",
                            "enum": [
                                "article",
                                "project",
                                "user",
                                "submission",
                                "funding_source",
                                "user_preference",
                                "subscription",
                            ],
                        },
                        "record_id": {
                            "type": "string",
                            "description": "The unique ID of the record to be modified.",
                        },
                        "modifications": {
                            "type": "object",
                            "description": "A dictionary of field modifications.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status field to update.",
                        },
                        "linked_articles": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of linked article IDs.",
                        },
                        "funding_source_id": {
                            "type": "string",
                            "description": "The funding source ID.",
                        },
                        "lead_researcher_id": {
                            "description": "The lead researcher ID (can be string or array).",
                        },
                        "assigned_reviewers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of assigned reviewer IDs.",
                        },
                        "publication_date": {
                            "type": "string",
                            "description": "The publication date.",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date.",
                        },
                        "logs": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of log entries.",
                        },
                        "institution": {
                            "type": "string",
                            "description": "The institution name.",
                        },
                        "team_members": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of team member IDs.",
                        },
                    },
                    "required": ["record_type", "record_id"],
                },
            },
        }


class DispatchSystemNotification(Tool):
    """Utility for sending a direct notification to a user."""

    @staticmethod
    def invoke(data: dict[str, Any], recipient_user_id: Any = None, message_content: Any = None, sender_user_id: Any = None) -> str:
        if not all([recipient_user_id, message_content]):
            payload = {"error": "recipient_user_id and message_content are required."}
            out = json.dumps(payload)
            return out

        notifications = data.get("notifications", {}).values()
        new_notification = {
            "notification_id": f"notif_{len(notifications) + 1:02d}",
            "recipient_user_id": recipient_user_id,
            "sender_user_id": sender_user_id,
            "message_content": message_content,
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "status": "unread",
        }
        data["notifications"][notification_id] = new_notification
        payload = new_notification
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DispatchSystemNotification",
                "description": "Dispatches a direct notification to a user, which can be from the system or another user.",
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
                            "description": "Optional. The user ID of the sender. Defaults to 'system'.",
                        },
                    },
                    "required": ["recipient_user_id", "message_content"],
                },
            },
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
    DispatchSystemNotification(),
]