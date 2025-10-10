# Copyright owned by Sierra

from .list_candidate_emails import ListCandidateEmails
from .mark_checklist_items_reminded import MarkChecklistItemsReminded
from .get_or_create_email_label import GetOrCreateEmailLabel
from .search_attachments_by_filename import SearchAttachmentsByFilename
from .find_candidate_by_email import FindCandidateByEmail
from .generate_and_send_email import GenerateAndSendEmail
from .allocate_first_available_asset import AllocateFirstAvailableAsset
from .write_onboarding_file import WriteOnboardingFile
from .update_candidate_status_fields import UpdateCandidateStatusFields
from .get_candidate_details import GetCandidateDetails
from .update_candidate_invite_timestamps import UpdateCandidateInviteTimestamps
from .record_access_checks_and_notify_gaps import RecordAccessChecksAndNotifyGaps
from .reply_to_email_thread import ReplyToEmailThread
from .write_asset_request_file import WriteAssetRequestFile
from .read_asset_request import ReadAssetRequest
from .assign_asset_to_candidate import AssignAssetToCandidate
from .record_access_checks import RecordAccessChecks
from .render_onboarding_welcome import RenderOnboardingWelcome
from .create_asset_request import CreateAssetRequest
from .write_pending_tasks_file import WritePendingTasksFile
from .upsert_candidate_record import UpsertCandidateRecord
from .update_asset_request_status import UpdateAssetRequestStatus
from .read_onboarding_file import ReadOnboardingFile
from .search_checklist_items import SearchChecklistItems
from .modify_email_labels import ModifyEmailLabels
from .audit_attachments_for_email import AuditAttachmentsForEmail
from .close_completed_checklist_items import CloseCompletedChecklistItems
from .summarize_access_checks import SummarizeAccessChecks
from .create_candidate import CreateCandidate
from .add_checklist_item_for_candidate import AddChecklistItemForCandidate
from .create_onboarding_file import CreateOnboardingFile

ALL_TOOLS = [
    ListCandidateEmails,
    MarkChecklistItemsReminded,
    GetOrCreateEmailLabel,
    SearchAttachmentsByFilename,
    FindCandidateByEmail,
    GenerateAndSendEmail,
    AllocateFirstAvailableAsset,
    WriteOnboardingFile,
    UpdateCandidateStatusFields,
    GetCandidateDetails,
    UpdateCandidateInviteTimestamps,
    RecordAccessChecksAndNotifyGaps,
    ReplyToEmailThread,
    WriteAssetRequestFile,
    ReadAssetRequest,
    AssignAssetToCandidate,
    RecordAccessChecks,
    RenderOnboardingWelcome,
    CreateAssetRequest,
    WritePendingTasksFile,
    UpsertCandidateRecord,
    UpdateAssetRequestStatus,
    ReadOnboardingFile,
    SearchChecklistItems,
    ModifyEmailLabels,
    AuditAttachmentsForEmail,
    CloseCompletedChecklistItems,
    SummarizeAccessChecks,
    CreateCandidate,
    AddChecklistItemForCandidate,
    CreateOnboardingFile,
]
