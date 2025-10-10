# Copyright © Sierra

from .who_am_i import WhoAmI
from .list_repos import ListRepos
from .create_repo import CreateRepo
from .delete_repo import DeleteRepo
from .list_branches import ListBranches
from .create_branch import CreateBranch
from .open_issue import OpenIssue
from .list_issues import ListIssues
from .set_issue_state import SetIssueState
from .comment_issue import CommentIssue
from .add_label import AddLabel
from .open_pr import OpenPR
from .list_p_rs import ListPRs
from .merge_pr import MergePR
from .submit_review import SubmitReview
from .add_commit import AddCommit
from .list_commits import ListCommits
from .search_work import SearchWork
from .list_alerts import ListAlerts
from .resolve_alert import ResolveAlert
from .activity_feed import ActivityFeed
from .append_terminal import AppendTerminal
from .list_terminal import ListTerminal
from .assign_user import AssignUser
from .set_milestone import SetMilestone
from .remove_label import RemoveLabel
from .close_pr import ClosePR
from .reopen_pr import ReopenPR
from .repo_topics import RepoTopics
from .transfer_repo import TransferRepo

ALL_TOOLS = [
    WhoAmI,
    ListRepos,
    CreateRepo,
    DeleteRepo,
    ListBranches,
    CreateBranch,
    OpenIssue,
    ListIssues,
    SetIssueState,
    CommentIssue,
    AddLabel,
    OpenPR,
    ListPRs,
    MergePR,
    SubmitReview,
    AddCommit,
    ListCommits,
    SearchWork,
    ListAlerts,
    ResolveAlert,
    ActivityFeed,
    AppendTerminal,
    ListTerminal,
    AssignUser,
    SetMilestone,
    RemoveLabel,
    ClosePR,
    ReopenPR,
    RepoTopics,
    TransferRepo,
]
