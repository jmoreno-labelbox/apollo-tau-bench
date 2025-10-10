# Copyright owned by Sierra

from .get_build_run_details import GetBuildRunDetails
from .list_failed_build_runs_by_branch import ListFailedBuildRunsByBranch
from .start_automation_run import StartAutomationRun
from .complete_automation_run import CompleteAutomationRun
from .attach_symbolicated_stack_to_run import AttachSymbolicatedStackToRun
from .map_path_to_owner import MapPathToOwner
from .set_build_triage_status import SetBuildTriageStatus
from .record_repro_command_for_run import RecordReproCommandForRun
from .set_fix_proposal_on_run import SetFixProposalOnRun
from .list_failed_tests_for_run import ListFailedTestsForRun
from .create_asset_qa_result import CreateAssetQaResult
from .promote_asset_autofix_to_pass import PromoteAssetAutofixToPass
from .update_asset_catalog_performance_rating import UpdateAssetCatalogPerformanceRating
from .update_artifact_metadata import UpdateArtifactMetadata
from .create_test_run_summary import CreateTestRunSummary
from .add_test_result_to_run import AddTestResultToRun
from .set_build_failure_categorization import SetBuildFailureCategorization
from .set_first_bad_commit_on_run import SetFirstBadCommitOnRun
from .set_bisect_result_on_run import SetBisectResultOnRun
from .append_similar_incident_to_run import AppendSimilarIncidentToRun
from .update_run_metadata import UpdateRunMetadata
from .add_run_step import AddRunStep
from .update_run_step_status import UpdateRunStepStatus
from .link_artifact_to_run import LinkArtifactToRun
from .register_symbol import RegisterSymbol
from .deprecate_symbol import DeprecateSymbol
from .register_asset_in_catalog import RegisterAssetInCatalog
from .deprecate_asset_in_catalog import DeprecateAssetInCatalog
from .persist_owner_to_run import PersistOwnerToRun
from .update_test_run_coverage import UpdateTestRunCoverage

ALL_TOOLS = [
    GetBuildRunDetails,
    ListFailedBuildRunsByBranch,
    StartAutomationRun,
    CompleteAutomationRun,
    AttachSymbolicatedStackToRun,
    MapPathToOwner,
    SetBuildTriageStatus,
    RecordReproCommandForRun,
    SetFixProposalOnRun,
    ListFailedTestsForRun,
    CreateAssetQaResult,
    PromoteAssetAutofixToPass,
    UpdateAssetCatalogPerformanceRating,
    UpdateArtifactMetadata,
    CreateTestRunSummary,
    AddTestResultToRun,
    SetBuildFailureCategorization,
    SetFirstBadCommitOnRun,
    SetBisectResultOnRun,
    AppendSimilarIncidentToRun,
    UpdateRunMetadata,
    AddRunStep,
    UpdateRunStepStatus,
    LinkArtifactToRun,
    RegisterSymbol,
    DeprecateSymbol,
    RegisterAssetInCatalog,
    DeprecateAssetInCatalog,
    PersistOwnerToRun,
    UpdateTestRunCoverage,
]
