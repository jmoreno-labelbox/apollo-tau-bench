# Copyright Sierra


def _next_seq(items, id_key='id'):
    """Get next sequential integer ID."""
    max_id = 0
    for item in items:
        try:
            item_id = item.get(id_key, 0)
            if isinstance(item_id, str):
                # Try to extract number from string like "123" or "ID-123"
                import re
                nums = re.findall(r'\d+', item_id)
                if nums:
                    item_id = int(nums[-1])
                else:
                    continue
            max_id = max(max_id, int(item_id))
        except (ValueError, TypeError):
            pass
    return max_id + 1


from .find_candidate_by_email import FindCandidateByEmail
from .read_asset_request import ReadAssetRequest
from .upsert_candidate_record import UpsertCandidateRecord
from .get_candidate_details import GetCandidateDetails
from .update_candidate_status_fields import UpdateCandidateStatusFields
from .search_attachments_by_filename import SearchAttachmentsByFilename
from .read_onboarding_file import ReadOnboardingFile
from .render_onboarding_welcome import RenderOnboardingWelcome
from .write_onboarding_file import WriteOnboardingFile
from .generate_and_send_email import GenerateAndSendEmail
from .get_or_create_email_label import GetOrCreateEmailLabel
from .modify_email_labels import ModifyEmailLabels
from .list_candidate_emails import ListCandidateEmails
from .create_asset_request import CreateAssetRequest
from .write_asset_request_file import WriteAssetRequestFile
from .assign_asset_to_candidate import AssignAssetToCandidate
from .record_access_checks import RecordAccessChecks
from .update_candidate_invite_timestamps import UpdateCandidateInviteTimestamps
from .search_checklist_items import SearchChecklistItems
from .write_pending_tasks_file import WritePendingTasksFile
from .mark_checklist_items_reminded import MarkChecklistItemsReminded
from .update_asset_request_status import UpdateAssetRequestStatus
from .allocate_first_available_asset import AllocateFirstAvailableAsset
from .reply_to_email_thread import ReplyToEmailThread
from .summarize_access_checks import SummarizeAccessChecks
from .audit_attachments_for_email import AuditAttachmentsForEmail
from .close_completed_checklist_items import CloseCompletedChecklistItems
from .record_access_checks_and_notify_gaps import RecordAccessChecksAndNotifyGaps

ALL_TOOLS = [
    FindCandidateByEmail,
    ReadAssetRequest,
    UpsertCandidateRecord,
    GetCandidateDetails,
    UpdateCandidateStatusFields,
    SearchAttachmentsByFilename,
    ReadOnboardingFile,
    RenderOnboardingWelcome,
    WriteOnboardingFile,
    GenerateAndSendEmail,
    GetOrCreateEmailLabel,
    ModifyEmailLabels,
    ListCandidateEmails,
    CreateAssetRequest,
    WriteAssetRequestFile,
    AssignAssetToCandidate,
    RecordAccessChecks,
    UpdateCandidateInviteTimestamps,
    SearchChecklistItems,
    WritePendingTasksFile,
    MarkChecklistItemsReminded,
    UpdateAssetRequestStatus,
    AllocateFirstAvailableAsset,
    ReplyToEmailThread,
    SummarizeAccessChecks,
    AuditAttachmentsForEmail,
    CloseCompletedChecklistItems,
    RecordAccessChecksAndNotifyGaps,
]
