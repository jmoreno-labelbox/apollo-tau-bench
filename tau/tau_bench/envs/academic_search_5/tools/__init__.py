# Copyright Sierra

from .find_users import FindUsers
from .launch_project import LaunchProject
from .modify_submission_status import ModifySubmissionStatus
from .appoint_reviewer import AppointReviewer
from .submit_review import SubmitReview
from .get_reviews_for_submission import GetReviewsForSubmission
from .modify_project_status import ModifyProjectStatus
from .link_article_to_project import LinkArticleToProject
from .find_grants import FindGrants
from .assign_funding_to_project import AssignFundingToProject
from .add_researcher_to_project_team import AddResearcherToProjectTeam
from .create_research_log import CreateResearchLog
from .search_research_logs import SearchResearchLogs
from .get_user_subscriptions import GetUserSubscriptions
from .update_user_subscriptions import UpdateUserSubscriptions
from .update_user_preferences import UpdateUserPreferences
from .notify_user import NotifyUser
from .find_publications import FindPublications
from .summarize_article_text import SummarizeArticleText
from .find_references import FindReferences
from .find_projects import FindProjects
from .get_user_preferences import GetUserPreferences
from .lookup_submissions import LookupSubmissions

ALL_TOOLS = [
    FindUsers,
    LaunchProject,
    ModifySubmissionStatus,
    AppointReviewer,
    SubmitReview,
    GetReviewsForSubmission,
    ModifyProjectStatus,
    LinkArticleToProject,
    FindGrants,
    AssignFundingToProject,
    AddResearcherToProjectTeam,
    CreateResearchLog,
    SearchResearchLogs,
    GetUserSubscriptions,
    UpdateUserSubscriptions,
    UpdateUserPreferences,
    NotifyUser,
    FindPublications,
    SummarizeArticleText,
    FindReferences,
    FindProjects,
    GetUserPreferences,
    LookupSubmissions,
]
