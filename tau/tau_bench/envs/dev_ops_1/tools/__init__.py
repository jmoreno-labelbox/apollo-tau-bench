# Copyright Sierra

from .receive_ci_event import ReceiveCiEvent
from .attach_run_artifacts import AttachRunArtifacts
from .extract_failure_signals import ExtractFailureSignals
from .find_similar_incidents import FindSimilarIncidents
from .enumerate_suspects import EnumerateSuspects
from .run_bisect import RunBisect
from .propose_fix_patch import ProposeFixPatch
from .open_auto_branch import OpenAutoBranch
from .commit_patch_to_branch import CommitPatchToBranch
from .open_draft_pull_request import OpenDraftPullRequest
from .create_or_update_ticket import CreateOrUpdateTicket
from .run_validation_checks import RunValidationChecks
from .record_automation_run import RecordAutomationRun
from .run_dcc_validation import RunDccValidation
from .get_asset_files import GetAssetFiles
from .validate_textures import ValidateTextures
from .run_engine_budget_checks import RunEngineBudgetChecks
from .apply_asset_autofixes import ApplyAssetAutofixes
from .render_asset_previews import RenderAssetPreviews
from .upload_qa_reports import UploadQaReports
from .annotate_pr_with_qa import AnnotatePrWithQa
from .set_asset_qa_check import SetAssetQaCheck
from .persist_asset_qa_results import PersistAssetQaResults
from .receive_ticket_webhook import ReceiveTicketWebhook
from .normalize_issue import NormalizeIssue
from .summarize_issue import SummarizeIssue
from .compute_impact_score import ComputeImpactScore
from .resolve_owner_from_map import ResolveOwnerFromMap
from .link_duplicate_issue import LinkDuplicateIssue
from .update_ticket_fields import UpdateTicketFields
from .detect_changed_strings import DetectChangedStrings
from .capture_loc_context import CaptureLocContext
from .loc_lint import LocLint
from .validate_subtitle_timing import ValidateSubtitleTiming
from .write_locale_bundle import WriteLocaleBundle
from .create_tms_job import CreateTmsJob
from .return_scalar import ReturnScalar
from .get_project_key import GetProjectKey

ALL_TOOLS = [
    ReceiveCiEvent,
    AttachRunArtifacts,
    ExtractFailureSignals,
    FindSimilarIncidents,
    EnumerateSuspects,
    RunBisect,
    ProposeFixPatch,
    OpenAutoBranch,
    CommitPatchToBranch,
    OpenDraftPullRequest,
    CreateOrUpdateTicket,
    RunValidationChecks,
    RecordAutomationRun,
    RunDccValidation,
    GetAssetFiles,
    ValidateTextures,
    RunEngineBudgetChecks,
    ApplyAssetAutofixes,
    RenderAssetPreviews,
    UploadQaReports,
    AnnotatePrWithQa,
    SetAssetQaCheck,
    PersistAssetQaResults,
    ReceiveTicketWebhook,
    NormalizeIssue,
    SummarizeIssue,
    ComputeImpactScore,
    ResolveOwnerFromMap,
    LinkDuplicateIssue,
    UpdateTicketFields,
    DetectChangedStrings,
    CaptureLocContext,
    LocLint,
    ValidateSubtitleTiming,
    WriteLocaleBundle,
    CreateTmsJob,
    ReturnScalar,
    GetProjectKey,
]
