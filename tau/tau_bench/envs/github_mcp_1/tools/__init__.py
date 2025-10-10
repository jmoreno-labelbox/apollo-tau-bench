# Copyright Sierra

from .authenticate_user import AuthenticateUser
from .get_repo_info_for_owner import GetRepoInfoForOwner
from .get_branch_content import GetBranchContent
from .delete_repository import DeleteRepository
from .create_repository import CreateRepository
from .add_new_file_in_repo import AddNewFileInRepo
from .update_file_in_repo import UpdateFileInRepo
from .delete_file_in_repo import DeleteFileInRepo
from .create_new_branch import CreateNewBranch
from .delete_branch import DeleteBranch
from .merge_branch import MergeBranch
from .initial_commit import InitialCommit
from .make_commit import MakeCommit
from .create_pull_request import CreatePullRequest
from .get_pr_details import GetPRDetails
from .list_of_pr_for_repo import ListOfPRForRepo
from .add_pull_request_comment import AddPullRequestComment
from .assign_pull_request_reviewers import AssignPullRequestReviewers
from .approve_pr import ApprovePR
from .mark_p_ras_merged import MarkPRasMerged
from .create_new_issue import CreateNewIssue
from .get_all_issues_for_repo import GetAllIssuesForRepo
from .add_comment_to_issue import AddCommentToIssue
from .close_issue import CloseIssue
from .create_code_scanning_alert import CreateCodeScanningAlert
from .get_alert_details import GetAlertDetails
from .list_open_alerts_for_repo import ListOpenAlertsForRepo
from .dismiss_alert import DismissAlert
from .list_all_terminal_message import ListAllTerminalMessage

ALL_TOOLS = [
    AuthenticateUser,
    GetRepoInfoForOwner,
    GetBranchContent,
    DeleteRepository,
    CreateRepository,
    AddNewFileInRepo,
    UpdateFileInRepo,
    DeleteFileInRepo,
    CreateNewBranch,
    DeleteBranch,
    MergeBranch,
    InitialCommit,
    MakeCommit,
    CreatePullRequest,
    GetPRDetails,
    ListOfPRForRepo,
    AddPullRequestComment,
    AssignPullRequestReviewers,
    ApprovePR,
    MarkPRasMerged,
    CreateNewIssue,
    GetAllIssuesForRepo,
    AddCommentToIssue,
    CloseIssue,
    CreateCodeScanningAlert,
    GetAlertDetails,
    ListOpenAlertsForRepo,
    DismissAlert,
    ListAllTerminalMessage,
]
