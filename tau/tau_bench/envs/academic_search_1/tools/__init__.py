# Copyright Sierra

from .search_users import SearchUsers
from .create_log_entry import CreateLogEntry
from .update_log_notes import UpdateLogNotes
from .get_log_details import GetLogDetails
from .update_article_details import UpdateArticleDetails
from .get_submission_by_article import GetSubmissionByArticle
from .search_projects import SearchProjects
from .search_funding_sources import SearchFundingSources
from .get_review_by_submission import GetReviewBySubmission
from .get_project_details import GetProjectDetails
from .assign_reviewer_to_submission import AssignReviewerToSubmission
from .create_project import CreateProject
from .get_citation_details import GetCitationDetails
from .update_project_links import UpdateProjectLinks
from .update_submission_status import UpdateSubmissionStatus
from .get_submission_details import GetSubmissionDetails
from .update_project_status import UpdateProjectStatus
from .create_citation import CreateCitation
from .search_citations import SearchCitations
from .manage_user_subscriptions import ManageUserSubscriptions
from .send_notification import SendNotification
from .search_articles import SearchArticles
from .summarize_article import SummarizeArticle

ALL_TOOLS = [
    SearchUsers,
    CreateLogEntry,
    UpdateLogNotes,
    GetLogDetails,
    UpdateArticleDetails,
    GetSubmissionByArticle,
    SearchProjects,
    SearchFundingSources,
    GetReviewBySubmission,
    GetProjectDetails,
    AssignReviewerToSubmission,
    CreateProject,
    GetCitationDetails,
    UpdateProjectLinks,
    UpdateSubmissionStatus,
    GetSubmissionDetails,
    UpdateProjectStatus,
    CreateCitation,
    SearchCitations,
    ManageUserSubscriptions,
    SendNotification,
    SearchArticles,
    SummarizeArticle,
]
