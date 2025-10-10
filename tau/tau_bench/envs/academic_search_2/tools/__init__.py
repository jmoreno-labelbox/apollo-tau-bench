# Copyright Sierra

from .find_researcher_profiles import FindResearcherProfiles
from .retrieve_papers import RetrievePapers
from .search_submissions import SearchSubmissions
from .get_project_details import GetProjectDetails
from .get_citation_graph import GetCitationGraph
from .find_collaboration_network import FindCollaborationNetwork
from .add_citation import AddCitation
from .update_article_metadata import UpdateArticleMetadata
from .get_author_metrics import GetAuthorMetrics
from .suggest_reviewers import SuggestReviewers
from .get_most_cited_articles import GetMostCitedArticles
from .find_common_collaborators import FindCommonCollaborators
from .update_submission import UpdateSubmission
from .register_project import RegisterProject
from .create_submission import CreateSubmission
from .add_research_note import AddResearchNote
from .update_project import UpdateProject
from .retrieve_funding_info import RetrieveFundingInfo
from .create_review import CreateReview
from .create_article import CreateArticle
from .configure_profile_settings import ConfigureProfileSettings
from .update_topic_subscription import UpdateTopicSubscription
from .dispatch_user_alert import DispatchUserAlert

ALL_TOOLS = [
    FindResearcherProfiles,
    RetrievePapers,
    SearchSubmissions,
    GetProjectDetails,
    GetCitationGraph,
    FindCollaborationNetwork,
    AddCitation,
    UpdateArticleMetadata,
    GetAuthorMetrics,
    SuggestReviewers,
    GetMostCitedArticles,
    FindCommonCollaborators,
    UpdateSubmission,
    RegisterProject,
    CreateSubmission,
    AddResearchNote,
    UpdateProject,
    RetrieveFundingInfo,
    CreateReview,
    CreateArticle,
    ConfigureProfileSettings,
    UpdateTopicSubscription,
    DispatchUserAlert,
]
