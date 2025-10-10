# Copyright by Sierra

from .locate_papers import LocatePapers
from .summarize_abstract import SummarizeAbstract
from .extract_keywords import ExtractKeywords
from .find_users_by_criteria import FindUsersByCriteria
from .query_submissions import QuerySubmissions
from .generate_new_review import GenerateNewReview
from .search_reviews import SearchReviews
from .query_projects import QueryProjects
from .locate_funding_sources import LocateFundingSources
from .add_entry_to_log import AddEntryToLog
from .delete_citation import DeleteCitation
from .query_citation_connections import QueryCitationConnections
from .retrieve_citation_data import RetrieveCitationData
from .initiate_project import InitiateProject
from .register_article_record import RegisterArticleRecord
from .submit_article_for_review import SubmitArticleForReview
from .link_cited_article import LinkCitedArticle
from .delete_review import DeleteReview
from .modify_record import ModifyRecord
from .dispatch_system_notification import DispatchSystemNotification

ALL_TOOLS = [
    LocatePapers,
    SummarizeAbstract,
    ExtractKeywords,
    FindUsersByCriteria,
    QuerySubmissions,
    GenerateNewReview,
    SearchReviews,
    QueryProjects,
    LocateFundingSources,
    AddEntryToLog,
    DeleteCitation,
    QueryCitationConnections,
    RetrieveCitationData,
    InitiateProject,
    RegisterArticleRecord,
    SubmitArticleForReview,
    LinkCitedArticle,
    DeleteReview,
    ModifyRecord,
    DispatchSystemNotification,
]
