# Copyright © Sierra

from .create_change_request import CreateChangeRequest
from .perform_impact_assessment import PerformImpactAssessment
from .update_change_request_status import UpdateChangeRequestStatus
from .process_emergency_change import ProcessEmergencyChange
from .record_retroactive_approval import RecordRetroactiveApproval
from .check_change_conflicts import CheckChangeConflicts
from .save_change_requests_conflicts import SaveChangeRequestsConflicts
from .validate_change_compliance import ValidateChangeCompliance
from .create_approval_workflow import CreateApprovalWorkflow
from .check_workflow_exists_for_change_request import CheckWorkflowExistsForChangeRequest
from .record_approval_decision import RecordApprovalDecision
from .search_change_requests import SearchChangeRequests
from .track_artifact_updates import TrackArtifactUpdates
from .create_scope_baseline import CreateScopeBaseline
from .compare_against_baseline import CompareAgainstBaseline
from .schedule_change_review import ScheduleChangeReview
from .calculate_cumulative_impact import CalculateCumulativeImpact
from .generate_change_report import GenerateChangeReport
from .create_risk_assessment import CreateRiskAssessment
from .link_change_to_milestone import LinkChangeToMilestone
from .approve_baseline_update import ApproveBaselineUpdate
from .escalate_change_request import EscalateChangeRequest
from .merge_change_requests import MergeChangeRequests
from .archive_changes import ArchiveChanges
from .create_change_template import CreateChangeTemplate
from .bulk_update_change_status import BulkUpdateChangeStatus
from .calculate_change_roi import CalculateChangeROI
from .track_change_dependencies import TrackChangeDependencies
from .generate_audit_trail import GenerateAuditTrail

ALL_TOOLS = [
    CreateChangeRequest,
    PerformImpactAssessment,
    UpdateChangeRequestStatus,
    ProcessEmergencyChange,
    RecordRetroactiveApproval,
    CheckChangeConflicts,
    SaveChangeRequestsConflicts,
    ValidateChangeCompliance,
    CreateApprovalWorkflow,
    CheckWorkflowExistsForChangeRequest,
    RecordApprovalDecision,
    SearchChangeRequests,
    TrackArtifactUpdates,
    CreateScopeBaseline,
    CompareAgainstBaseline,
    ScheduleChangeReview,
    CalculateCumulativeImpact,
    GenerateChangeReport,
    CreateRiskAssessment,
    LinkChangeToMilestone,
    ApproveBaselineUpdate,
    EscalateChangeRequest,
    MergeChangeRequests,
    ArchiveChanges,
    CreateChangeTemplate,
    BulkUpdateChangeStatus,
    CalculateChangeROI,
    TrackChangeDependencies,
    GenerateAuditTrail,
]
