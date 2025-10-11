# Copyright Sierra

from .fetch_articles import FetchArticles
from .fetch_users import FetchUsers
from .create_review_submission import CreateReviewSubmission
from .assign_reviewer import AssignReviewer
from .fetch_submission_info import FetchSubmissionInfo
from .identify_potential_reviewers import IdentifyPotentialReviewers
from .post_new_review import PostNewReview
from .set_submission_outcome import SetSubmissionOutcome
from .connect_revised_version import ConnectRevisedVersion
from .alert_user import AlertUser
from .adjust_user_settings import AdjustUserSettings
from .set_topic_interest import SetTopicInterest
from .register_new_article import RegisterNewArticle
from .revise_article_details import ReviseArticleDetails
from .list_reviews_for_submission import ListReviewsForSubmission
from .create_new_project import CreateNewProject
from .get_article_keywords import GetArticleKeywords
from .find_citations import FindCitations
from .update_project_details import UpdateProjectDetails
from .remove_review import RemoveReview

ALL_TOOLS = [
    FetchArticles,
    FetchUsers,
    CreateReviewSubmission,
    AssignReviewer,
    FetchSubmissionInfo,
    IdentifyPotentialReviewers,
    PostNewReview,
    SetSubmissionOutcome,
    ConnectRevisedVersion,
    AlertUser,
    AdjustUserSettings,
    SetTopicInterest,
    RegisterNewArticle,
    ReviseArticleDetails,
    ListReviewsForSubmission,
    CreateNewProject,
    GetArticleKeywords,
    FindCitations,
    UpdateProjectDetails,
    RemoveReview,
]
