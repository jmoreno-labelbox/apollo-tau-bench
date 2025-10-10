# Copyright Sierra

from .set_candidate_fields import SetCandidateFields
from .update_asset_request import UpdateAssetRequest
from .assign_inventory_asset import AssignInventoryAsset
from .release_inventory_asset import ReleaseInventoryAsset
from .upsert_onboarding_file import UpsertOnboardingFile
from .create_or_get_email_label import CreateOrGetEmailLabel
from .insert_email import InsertEmail
from .add_labels_to_email import AddLabelsToEmail
from .insert_access_check import InsertAccessCheck
from .update_checklist_item import UpdateChecklistItem
from .insert_terminal_log import InsertTerminalLog
from .record_mcp_tool_call import RecordMcpToolCall
from .insert_attachment_record import InsertAttachmentRecord
from .label_email_by_name import LabelEmailByName
from .update_email_metadata import UpdateEmailMetadata
from .reserve_inventory_asset import ReserveInventoryAsset
from .set_inventory_asset_fields import SetInventoryAssetFields
from .link_asset_request_to_candidate import LinkAssetRequestToCandidate
from .bulk_update_checklist_items import BulkUpdateChecklistItems
from .create_orientation_invite_email import CreateOrientationInviteEmail
from .create_manager_intro_email import CreateManagerIntroEmail
from .upsert_json_artifact import UpsertJsonArtifact
from .create_access_gap_summary_file import CreateAccessGapSummaryFile
from .set_candidate_timestamps import SetCandidateTimestamps
from .update_candidate_email_pointers import UpdateCandidateEmailPointers
from .bulk_add_labels_to_emails import BulkAddLabelsToEmails

ALL_TOOLS = [
    SetCandidateFields,
    UpdateAssetRequest,
    AssignInventoryAsset,
    ReleaseInventoryAsset,
    UpsertOnboardingFile,
    CreateOrGetEmailLabel,
    InsertEmail,
    AddLabelsToEmail,
    InsertAccessCheck,
    UpdateChecklistItem,
    InsertTerminalLog,
    RecordMcpToolCall,
    InsertAttachmentRecord,
    LabelEmailByName,
    UpdateEmailMetadata,
    ReserveInventoryAsset,
    SetInventoryAssetFields,
    LinkAssetRequestToCandidate,
    BulkUpdateChecklistItems,
    CreateOrientationInviteEmail,
    CreateManagerIntroEmail,
    UpsertJsonArtifact,
    CreateAccessGapSummaryFile,
    SetCandidateTimestamps,
    UpdateCandidateEmailPointers,
    BulkAddLabelsToEmails,
]
