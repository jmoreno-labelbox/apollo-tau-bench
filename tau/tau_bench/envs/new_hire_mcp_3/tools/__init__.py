# Copyright owned by Sierra.


# Utility function
from datetime import datetime

def _fixed_now_iso():
    """Return current time in ISO format."""
    return datetime.now().isoformat()

from .modify_candidate import ModifyCandidate
from .add_candidate import AddCandidate
from .remove_candidate import RemoveCandidate
from .modify_asset_request import ModifyAssetRequest
from .add_asset_request import AddAssetRequest
from .remove_asset_request import RemoveAssetRequest
from .modify_access_check import ModifyAccessCheck
from .add_access_check import AddAccessCheck
from .remove_access_check import RemoveAccessCheck
from .modify_checklist_item import ModifyChecklistItem
from .add_checklist_item import AddChecklistItem
from .remove_checklist_item import RemoveChecklistItem
from .modify_attachment import ModifyAttachment
from .add_attachment import AddAttachment
from .remove_attachment import RemoveAttachment
from .modify_email_label import ModifyEmailLabel
from .add_email_label import AddEmailLabel
from .remove_email_label import RemoveEmailLabel
from .modify_email import ModifyEmail
from .send_email import SendEmail
from .delete_email import DeleteEmail
from .modify_asset import ModifyAsset
from .assign_asset import AssignAsset
from .release_asset import ReleaseAsset
from .modify_onboarding_file import ModifyOnboardingFile
from .add_onboarding_file import AddOnboardingFile
from .remove_onboarding_file import RemoveOnboardingFile
from .record_terminal_log import RecordTerminalLog
from .apply_label_to_email import ApplyLabelToEmail

ALL_TOOLS = [
    ModifyCandidate,
    AddCandidate,
    RemoveCandidate,
    ModifyAssetRequest,
    AddAssetRequest,
    RemoveAssetRequest,
    ModifyAccessCheck,
    AddAccessCheck,
    RemoveAccessCheck,
    ModifyChecklistItem,
    AddChecklistItem,
    RemoveChecklistItem,
    ModifyAttachment,
    AddAttachment,
    RemoveAttachment,
    ModifyEmailLabel,
    AddEmailLabel,
    RemoveEmailLabel,
    ModifyEmail,
    SendEmail,
    DeleteEmail,
    ModifyAsset,
    AssignAsset,
    ReleaseAsset,
    ModifyOnboardingFile,
    AddOnboardingFile,
    RemoveOnboardingFile,
    RecordTerminalLog,
    ApplyLabelToEmail,
]
