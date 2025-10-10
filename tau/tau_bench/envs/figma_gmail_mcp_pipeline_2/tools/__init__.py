# Copyright © Sierra


def get_next_asset_id(data, prefix='asset'):
    """Generate next asset ID."""
    assets = data.get('assets', {})
    if isinstance(assets, dict):
        assets = list(assets.values())
    
    max_num = 0
    for asset in assets:
        asset_id = str(asset.get('asset_id', ''))
        if asset_id.startswith(prefix + '_'):
            try:
                num = int(asset_id.split('_')[-1])
                max_num = max(max_num, num)
            except (ValueError, IndexError):
                pass
    
    return f"{prefix}_{max_num + 1}"


from .get_artifact_with_id import GetArtifactWithId
from .get_all_artifacts_of_type_with_tags_and_email import GetAllArtifactsOfTypeWithTagsAndEmail
from .create_new_artifact import CreateNewArtifact
from .get_artifacts_with_file_id import GetArtifactsWithFileId
from .get_asset_by_id import GetAssetById
from .get_assets_by_artifact_id import GetAssetsByArtifactId
from .create_new_asset import CreateNewAsset
from .create_new_cycle import CreateNewCycle
from .update_cycle_status import UpdateCycleStatus
from .get_cycle_by_artifact_and_thread import GetCycleByArtifactAndThread
from .get_cycle_by_id import GetCycleById
from .start_email_thread import StartEmailThread
from .send_email_in_thread import SendEmailInThread
from .get_complete_email_thread import GetCompleteEmailThread
from .get_thread_by_subject import GetThreadBySubject
from .add_comment import AddComment
from .approve_review import ApproveReview
from .get_release_details_by_name import GetReleaseDetailsByName
from .create_new_release import CreateNewRelease
from .get_release_by_id import GetReleaseById
from .create_release_diff import CreateReleaseDiff
from .get_release_diff_by_release_id import GetReleaseDiffByReleaseId
from .compare_before_after_visuals import CompareBeforeAfterVisuals
from .notify_stakeholders import NotifyStakeholders
from .create_new_audit import CreateNewAudit
from .record_audit_findings import RecordAuditFindings
from .generate_audit_report_asset import GenerateAuditReportAsset
from .complete_audit import CompleteAudit

ALL_TOOLS = [
    GetArtifactWithId,
    GetAllArtifactsOfTypeWithTagsAndEmail,
    CreateNewArtifact,
    GetArtifactsWithFileId,
    GetAssetById,
    GetAssetsByArtifactId,
    CreateNewAsset,
    CreateNewCycle,
    UpdateCycleStatus,
    GetCycleByArtifactAndThread,
    GetCycleById,
    StartEmailThread,
    SendEmailInThread,
    GetCompleteEmailThread,
    GetThreadBySubject,
    AddComment,
    ApproveReview,
    GetReleaseDetailsByName,
    CreateNewRelease,
    GetReleaseById,
    CreateReleaseDiff,
    GetReleaseDiffByReleaseId,
    CompareBeforeAfterVisuals,
    NotifyStakeholders,
    CreateNewAudit,
    RecordAuditFindings,
    GenerateAuditReportAsset,
    CompleteAudit,
]
