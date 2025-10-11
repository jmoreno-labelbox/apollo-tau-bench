# Copyright Sierra

from .get_milestone_details import GetMilestoneDetails
from .create_milestone import CreateMilestone
from .update_milestone_status import UpdateMilestoneStatus
from .create_milestone_dependency import CreateMilestoneDependency
from .calculate_critical_path import CalculateCriticalPath
from .create_schedule_baseline import CreateScheduleBaseline
from .update_milestone_dates import UpdateMilestoneDates
from .create_gate_review import CreateGateReview
from .add_external_dependency import AddExternalDependency
from .create_recovery_plan import CreateRecoveryPlan
from .analyze_schedule_compression import AnalyzeScheduleCompression
from .update_buffer_consumption import UpdateBufferConsumption
from .get_milestone_dependencies import GetMilestoneDependencies
from .check_milestone_float import CheckMilestoneFloat
from .apply_resource_leveling import ApplyResourceLeveling
from .get_project_timeline import GetProjectTimeline
from .update_external_dependency_status import UpdateExternalDependencyStatus
from .create_milestone_from_template import CreateMilestoneFromTemplate
from .archive_milestone import ArchiveMilestone
from .get_delayed_milestones import GetDelayedMilestones
from .validate_milestone_readiness import ValidateMilestoneReadiness
from .get_schedule_variance import GetScheduleVariance
from .approve_recovery_plan import ApproveRecoveryPlan

ALL_TOOLS = [
    GetMilestoneDetails,
    CreateMilestone,
    UpdateMilestoneStatus,
    CreateMilestoneDependency,
    CalculateCriticalPath,
    CreateScheduleBaseline,
    UpdateMilestoneDates,
    CreateGateReview,
    AddExternalDependency,
    CreateRecoveryPlan,
    AnalyzeScheduleCompression,
    UpdateBufferConsumption,
    GetMilestoneDependencies,
    CheckMilestoneFloat,
    ApplyResourceLeveling,
    GetProjectTimeline,
    UpdateExternalDependencyStatus,
    CreateMilestoneFromTemplate,
    ArchiveMilestone,
    GetDelayedMilestones,
    ValidateMilestoneReadiness,
    GetScheduleVariance,
    ApproveRecoveryPlan,
]
