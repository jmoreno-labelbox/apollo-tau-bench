from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="qap_001",
        instruction=(
            "Act as the Quality Engineer & Performance Specialist addressing a Windows compile failure in build run 'run_001' for repository 'game-engine'. Take deterministic steps to ensure symbolication for module 'GameEngine.dll' from build 'build_001' on platform 'windows', log the reproducible build command 'make build-windows-x64', determine ownership for the failing source file 'src/game/engine/renderer.cpp' using the ownership map, and monitor the triage in an automation run with the key that MUST be 'AUTO::automation::build_triage::run_001::canonical' having the status 'completed'. Mark the run's triage status as 'in_progress'. Provide the updated details of 'run_001'. All parameters utilized must come from this instruction or previously obtained data."
        ),
        actions=[
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"}),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id": "run_001",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="RecordReproCommandForRun", kwargs={
                "run_id": "run_001",
                "command": "make build-windows-x64"
            }),
            Action(name="MapPathToOwner", kwargs={
                "file_path": "src/game/engine/renderer.cpp"
            }),
            Action(name="SetBuildTriageStatus", kwargs={
                "run_id": "run_001",
                "triage_status": "in_progress"
            }),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "in_progress",
                    "symbolicated_stack_uri": "https://symbols.techcorp.com/build_001/GameEngine.pdb"
                }
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="qap_002",
        instruction=(
            "As a Quality Engineer concentrating on asset validation, ensure the system is updated to reflect: a documented QA result for the texture asset located at 'assets/textures/environment/castle_tower_diffuse.png' with type 'texture', validation_status as 'failed', severity_max as 'issue', and autofix_applied as true; promote the existing QA record 'qa_004' (castle_tower.fbx) to reflect that its validation outcome now includes the auto-fix; in the asset catalog, the same PNG texture's performance_rating remains 'high'; and confirm the CI context by examining the details of build run 'run_006'. Rely solely on the exact identifiers and values provided here; default fields returned by read operations are permitted."
        ),
        actions=[
            Action(
                name="CreateAssetQaResult",
                kwargs={
                    "asset_path": "assets/textures/environment/castle_tower_diffuse.png",
                    "asset_type": "texture",
                    "validation_status": "failed",
                    "severity_max": "issue",
                    "autofix_applied": True
                }
            ),
            Action(
                name="PromoteAssetAutofixToPass",
                kwargs={"qa_id": "qa_004"}
            ),
            Action(
                name="UpdateAssetCatalogPerformanceRating",
                kwargs={
                    "asset_path": "assets/textures/environment/castle_tower_diffuse.png",
                    "performance_rating": "high"
                }
            ),
            Action(
                name="GetBuildRunDetails",
                kwargs={"run_id": "run_006"}
            )
        ],
        outputs=[
            "QA recorded for assets/textures/environment/castle_tower_diffuse.png (failed, autofix_applied=true)",
            "QA qa_004 promoted to pass",
            "Asset catalog performance_rating=high for assets/textures/environment/castle_tower_diffuse.png",
            "Build run run_006 details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_003",
        instruction=(
            "Act as a Performance Specialist overseeing Windows performance diagnosis. Guarantee the system incorporates all the ensuing details, refraining from introducing any identifiers beyond those supplied here: the pipeline 'pipeline_perf_windows' has executed a performance test with the designated id 'AUTO::test_run::pipeline_perf_windows::175', summarizing totals of total=3, failed=1, skipped=0, passed=2, and coverage_pct=0.0; that identical test_run_id encompasses precisely three results named 'FrameRateTest::SceneA' (failed, duration_ms=1200), 'MemoryUsageTest::SceneA' (passed, duration_ms=800), and 'LoadTimeTest::SceneA' (passed, duration_ms=500); artifact 'build_001' is marked with metadata perf_baseline='2025-01' and regression_flag=true; Windows symbolication for module 'GameEngine.dll' from build 'build_001' is accessible to run 'run_007'; a build-triage automation for 'run_007' exists with key 'AUTO::automation::build_triage::run_007::canonical' and with completion status 'completed'; furthermore, the specifics of 'run_007' are accessible."
        ),
        actions=[
            Action(
                name="AttachSymbolicatedStackToRun",
                kwargs={
                    "run_id": "run_007",
                    "build_id": "build_001",
                    "module_name": "GameEngine.dll",
                    "platform": "windows"
                }
            ),
            Action(
                name="CreateTestRunSummary",
                kwargs={
                    "pipeline_id": "pipeline_perf_windows",
                    "total": 3,
                    "failed": 1,
                    "skipped": 0,
                    "passed": 2,
                    "coverage_pct": 0.0
                }
            ),
            Action(
                name="AddTestResultToRun",
                kwargs={
                    "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                    "test_name": "FrameRateTest::SceneA",
                    "status": "failed",
                    "duration_ms": 1200
                }
            ),
            Action(
                name="AddTestResultToRun",
                kwargs={
                    "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                    "test_name": "MemoryUsageTest::SceneA",
                    "status": "passed",
                    "duration_ms": 800
                }
            ),
            Action(
                name="AddTestResultToRun",
                kwargs={
                    "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                    "test_name": "LoadTimeTest::SceneA",
                    "status": "passed",
                    "duration_ms": 500
                }
            ),
            Action(
                name="UpdateArtifactMetadata",
                kwargs={
                    "artifact_id": "build_001",
                    "metadata_patch": {"perf_baseline": "2025-01", "regression_flag": True}
                }
            ),
            Action(
                name="StartAutomationRun",
                kwargs={
                    "automation_type": "build_triage",
                    "input_ref": "run_007",
                    "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"
                }
            ),
            Action(
                name="CompleteAutomationRun",
                kwargs={
                    "automation_run_id": "AUTO::automation::build_triage::run_007::canonical",
                    "status": "completed",
                    "outputs_json": {
                        "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                        "regression_flag": True
                    }
                }
            ),
            Action(
                name="GetBuildRunDetails",
                kwargs={"run_id": "run_007"}
            )
        ],
        outputs=[
            "Performance test summary recorded for AUTO::test_run::pipeline_perf_windows::175 with 3 total (1 failed, 2 passed, 0 skipped, coverage 0.0)",
            "Three results appended to AUTO::test_run::pipeline_perf_windows::175",
            "Artifact build_001 metadata annotated (perf_baseline=2025-01, regression_flag=true)",
            "Windows symbols for GameEngine.dll from build_001 linked to run_007",
            "Automation AUTO::automation::build_triage::run_007::canonical completed",
            "Build run run_007 details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_004",
        instruction=(
            "Manage an integration failure on Linux for build run 'run_005'. Leverage failed test evidence from 'test_run_002' to determine the owner of 'src/game/network/multiplayer.cpp' and maintain the triage context. Log the effort in a build-triage automation whose key must be 'AUTO::automation::build_triage::run_005::canonical' and which has a completion status of 'completed'. Confirm that the reproducible command for this run is 'make test-integration-linux', set the run's triage status to 'manual_review', and provide Windows symbolication for module 'GameEngine.dll' from build 'build_001' to support cross-platform analysis. Provide the updated details of 'run_005'. All parameters must be sourced from this instruction or previous tool outputs."
        ),
        actions=[
            Action(name="ListFailedTestsForRun", kwargs={"test_run_id": "test_run_002"}),
            Action(name="MapPathToOwner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_005", "command": "make test-integration-linux"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id": "run_005",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_005",
                "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_005::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "manual_review",
                    "owner_id": "user_008",
                    "owner_path": "src/game/network/multiplayer.cpp",
                    "evidence_test_run": "test_run_002"
                }
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_005"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="qap_005",
        instruction=(
            "As the Release & Performance steward, handle the CI triage state for 'run_007' and ensure its performance signal is explicit and auditable. Upon completion: associate 'run_007' with symbolicated stacks for module 'GameEngine.dll' from 'build_001' on 'windows'; record regression_root_commit 'abc123def456789' as true in artifact 'build_001' metadata; the performance pipeline 'pipeline_perf_windows' displays test run id 'AUTO::test_run::pipeline_perf_windows::175' with totals total=3, failed=1, skipped=0, passed=2, coverage_pct=0.0, and includes exactly 'FrameRateTest::SceneA' failed (duration_ms=1200), 'MemoryUsageTest::SceneA' passed (800), and 'LoadTimeTest::SceneA' passed (500); ensure completion of a build_triage automation keyed 'AUTO::automation::build_triage::run_007::canonical' with outputs showing triage_status 'manual_review', reflecting the run's triage_status as 'manual_review'. Finally, you can request refreshed details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(
                name="AttachSymbolicatedStackToRun",
                kwargs={"run_id": "run_007", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}
            ),
            Action(
                name="UpdateArtifactMetadata",
                kwargs={"artifact_id": "build_001", "metadata_patch": {"regression_root_commit": "abc123def456789", "validated": True}}
            ),
            Action(
                name="CreateTestRunSummary",
                kwargs={"pipeline_id": "pipeline_perf_windows", "total": 3, "failed": 1, "skipped": 0, "passed": 2, "coverage_pct": 0.0}
            ),
            Action(
                name="AddTestResultToRun",
                kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "FrameRateTest::SceneA", "status": "failed", "duration_ms": 1200}
            ),
            Action(
                name="AddTestResultToRun",
                kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "MemoryUsageTest::SceneA", "status": "passed", "duration_ms": 800}
            ),
            Action(
                name="AddTestResultToRun",
                kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "LoadTimeTest::SceneA", "status": "passed", "duration_ms": 500}
            ),
            Action(
                name="StartAutomationRun",
                kwargs={"automation_type": "build_triage", "input_ref": "run_007", "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"}
            ),
            Action(
                name="CompleteAutomationRun",
                kwargs={"automation_run_id": "AUTO::automation::build_triage::run_007::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review"}}
            ),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_007", "triage_status": "manual_review"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_007"})
        ],
        outputs=[
            "Symbols attached to run_007 from build_001 (GameEngine.dll, windows)",
            "build_001 metadata updated (regression_root_commit, validated)",
            "Test run AUTO::test_run::pipeline_perf_windows::175 summary + 3 results recorded",
            "Automation AUTO::automation::build_triage::run_007::canonical completed with triage_status=manual_review",
            "Run run_007 returned with triage_status=manual_review"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_006",
        instruction=(
            "As the Reliability Engineer for the asset-validation pipeline, coordinate bringing build run 'run_006' on branch 'feature/new-assets' to a coherent triage state, including all the following achievements upon completion: failure category 'asset_validation_issue'; first bad commit 'jkl012ghi789def'; artifacts available at 'https://artifacts.techcorp.com/run_006/'; a finalized build_triage automation 'AUTO::automation::build_triage::run_006::canonical' reporting outputs as triage_status 'pending'; mark the run itself with triage_status 'pending' and metadata.triage_note='owner to review assets'; and have the run carry the repro command 'scripts/validate_assets.sh --run run_006 --branch feature/new-assets'. Request refreshed details for 'run_006'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="SetBuildFailureCategorization", kwargs={"run_id": "run_006", "category": "asset_validation_issue"}),
            Action(name="SetFirstBadCommitOnRun", kwargs={"run_id": "run_006", "commit_sha": "jkl012ghi789def"}),
            Action(name="LinkArtifactToRun", kwargs={"run_id": "run_006", "artifacts_uri": "https://artifacts.techcorp.com/run_006/"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_006", "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_006::canonical", "status": "completed", "outputs_json": {"triage_status": "pending"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_006", "triage_status": "pending"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id": "run_006", "metadata_patch": {"triage_note": "owner to review assets"}}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_006", "command": "scripts/validate_assets.sh --run run_006 --branch feature/new-assets"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_006"})
        ],
        outputs=[
            "Run run_006 categorized as asset_validation_issue with first_bad_commit=jkl012ghi789def",
            "Artifacts linked to run_006 at https://artifacts.techcorp.com/run_006/",
            "Automation AUTO::automation::build_triage::run_006::canonical completed (outputs.triage_status=pending)",
            "Run run_006 triage_status set to pending; triage_note recorded; repro command recorded; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_007",
        instruction=(
            "Handle the traceability and auditability of ownership for the Linux integration failure in run 'run_005'. Upon completion, ensure the run metadata retains owner_id 'user_008' (team 'team_003') with ownership_type 'file_owner' and a confidence_score of 0.92. Classify the run as 'integration_failure' and update the triage_status to 'manual_review'. A build_triage automation identified as 'AUTO::automation::build_triage::run_005::canonical' should have concluded, providing outputs such as triage_status 'manual_review', owner_id 'user_008', and owner_path 'src/game/network/multiplayer.cpp'. Note a similar incident reference to 'run_001' with a similarity_score of 0.92. Ensure the step 'ownership_resolution' is marked complete for provenance. Provide refreshed details for 'run_005' using only the identifiers and values stated here."
        ),
        actions=[
            Action(name="PersistOwnerToRun", kwargs={"run_id": "run_005", "owner_id": "user_008", "team_id": "team_003", "ownership_type": "file_owner", "confidence_score": 0.92}),
            Action(name="SetBuildFailureCategorization", kwargs={"run_id": "run_005", "category": "integration_failure"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "owner_id": "user_008", "owner_path": "src/game/network/multiplayer.cpp"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
            Action(name="AppendSimilarIncidentToRun", kwargs={"run_id": "run_005", "incident_run_id": "run_001", "similarity_score": 0.92}),
            Action(name="AddRunStep", kwargs={"run_id": "run_005", "step_id": "ownership_resolution", "name": "ownership_resolution", "status": "completed"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_005"})
        ],
        outputs=[
            "Owner user_008 (team_003) persisted to run_005 (ownership_type=file_owner, confidence_score=0.92)",
            "Automation AUTO::automation::build_triage::run_005::canonical completed (outputs.triage_status=manual_review, owner_id=user_008, owner_path=src/game/network/multiplayer.cpp)",
            "Run run_005 categorized as integration_failure; triage_status=manual_review; similar incident linked (run_001, similarity_score=0.92); provenance step ownership_resolution=completed; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_008",
        instruction=(
            "Coordinate the consolidation of performance signal and bisect outcome without setting specific steps. Once accomplished: for the pipeline 'pipeline_perf_windows', a test run exists with totals total=2, failed=0, skipped=0, passed=2, and initial coverage_pct=0.0, known as 'AUTO::test_run::pipeline_perf_windows::175'. This run includes successful results for 'ShaderCompile::PassA' (600 ms) and 'ShaderCompile::PassB' (550 ms); the coverage for this run is 72.5. In CI run 'run_001', bisect metadata logs first_bad_commit_sha='commit_abc123', last_good_commit_sha='commit_prev000', confidence=1.0, and ties fix_proposal_id='fix_001'. The run records a repro command 'scripts/run_smoke_tests.sh --pipeline pipeline_perf_windows --run run_001'. Lastly, return refreshed details for 'run_001'. Use precisely the given identifiers and values."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={"pipeline_id": "pipeline_perf_windows", "total": 2, "failed": 0, "skipped": 0, "passed": 2, "coverage_pct": 0.0}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "ShaderCompile::PassA", "status": "passed", "duration_ms": 600}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "ShaderCompile::PassB", "status": "passed", "duration_ms": 550}),
            Action(name="UpdateTestRunCoverage", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "coverage_pct": 72.5}),
            Action(name="SetBisectResultOnRun", kwargs={"run_id": "run_001", "first_bad_commit_sha": "commit_abc123", "last_good_commit_sha": "commit_prev000", "confidence": 1.0}),
            Action(name="SetFixProposalOnRun", kwargs={"run_id": "run_001", "fix_proposal_id": "fix_001"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_001", "command": "scripts/run_smoke_tests.sh --pipeline pipeline_perf_windows --run run_001"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Test run summary recorded for pipeline_perf_windows (total=2, failed=0, skipped=0, passed=2, coverage_pct=0.0)",
            "Result appended: ShaderCompile::PassA (passed, 600ms) to AUTO::test_run::pipeline_perf_windows::175",
            "Result appended: ShaderCompile::PassB (passed, 550ms) to AUTO::test_run::pipeline_perf_windows::175",
            "Coverage updated to 72.5 for AUTO::test_run::pipeline_perf_windows::175",
            "Bisect recorded on run_001 (first_bad_commit_sha=commit_abc123, last_good_commit_sha=commit_prev000, confidence=1.0)",
            "Fix proposal fix_001 linked to run_001; repro command recorded; build run details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_009",
        instruction=(
            "Handle 'run_001' to achieve a triage-ready state utilizing compile-failure context and symbolication. Upon completion, set the run's failure_categorization to 'compilation_issue', the first_bad_commit to 'abc123def456789', and ensure Windows symbolication for 'GameEngine.dll' from 'build_001' is linked; the run should display triage_status 'in_progress', with this status documented under the canonical automation 'AUTO::automation::build_triage::run_001::canonical'. Update the details for 'run_001'. Use strictly these identifiers and values."
        ),
        actions=[
            Action(name="SetBuildFailureCategorization", kwargs={"run_id": "run_001", "category": "compilation_issue"}),
            Action(name="SetFirstBadCommitOnRun", kwargs={"run_id": "run_001", "commit_sha": "abc123def456789"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "run_001 categorized as compilation_issue; first_bad_commit=abc123def456789; Windows symbolication attached; triage_status=in_progress captured via canonical automation; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_010",
        instruction=(
            "Coordinate to verify that the asset-intake state remains coherent with its CI triage context reliably documented. By completing this task, ensure the catalog includes 'assets/models/environment/castle_tower.fbx' classified as 'model' with validation_status 'unverified' and performance_rating 'medium'; a QA record should be available for the same asset with validation_status 'passed' and severity_max 'warning'; ensure build run 'run_006' contains artifacts at 'https://artifacts.techcorp.com/run_006/', is categorized as 'asset_validation_issue', identifies the first_bad_commit 'jkl012ghi789def', and maintains the reproducibility command 'scripts/validate_assets.sh --run run_006 --branch feature/new-assets'. Complete a build_triage automation identified by 'AUTO::automation::build_triage::run_006::canonical' with outputs stating triage_status 'pending', while the run itself shows triage_status 'pending'. For provenance, the run should display completed steps 'triage_fetch_artifacts' and 'triage_repro'. Update the information for 'run_006'. Use only the explicitly stated identifiers and values."
        ),
        actions=[
            Action(name="RegisterAssetInCatalog", kwargs={"asset_path": "assets/models/environment/castle_tower.fbx", "asset_type": "model", "validation_status": "unverified", "performance_rating": "medium"}),
            Action(name="CreateAssetQaResult", kwargs={"asset_path": "assets/models/environment/castle_tower.fbx", "asset_type": "model", "validation_status": "passed", "severity_max": "warning"}),
            Action(name="LinkArtifactToRun", kwargs={"run_id": "run_006", "artifacts_uri": "https://artifacts.techcorp.com/run_006/"}),
            Action(name="SetBuildFailureCategorization", kwargs={"run_id": "run_006", "category": "asset_validation_issue"}),
            Action(name="SetFirstBadCommitOnRun", kwargs={"run_id": "run_006", "commit_sha": "jkl012ghi789def"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_006", "command": "scripts/validate_assets.sh --run run_006 --branch feature/new-assets"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_006", "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_006::canonical", "status": "completed", "outputs_json": {"triage_status": "pending"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_006", "triage_status": "pending"}),
            Action(name="AddRunStep", kwargs={"run_id": "run_006", "step_id": "triage_fetch_artifacts", "name": "triage_fetch_artifacts", "status": "completed"}),
            Action(name="AddRunStep", kwargs={"run_id": "run_006", "step_id": "triage_repro", "name": "triage_repro", "status": "completed"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_006"})
        ],
        outputs=[
            "Catalog reflects assets/models/environment/castle_tower.fbx (type=model, validation_status=unverified, performance_rating=medium)",
            "QA recorded for assets/models/environment/castle_tower.fbx (validation_status=passed, severity_max=warning)",
            "Run run_006 linked to artifacts https://artifacts.techcorp.com/run_006/ and categorized as asset_validation_issue with first_bad_commit=jkl012ghi789def",
            "Repro command recorded; automation AUTO::automation::build_triage::run_006::canonical completed (outputs.triage_status=pending); run triage_status=pending",
            "Provenance steps recorded: triage_fetch_artifacts=completed, triage_repro=completed; details for run_006 retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_011",
        instruction=(
            "As the Quality Engineer responsible for triage clarity in build run 'run_001', ensure symbolication is accessible for the module 'GameEngine.dll' from build 'build_001' on the 'windows' platform. Document the reproducible command 'make build-windows-x64', determine ownership for 'src/game/engine/renderer.cpp', and log the activity in a build-triage automation, making sure the key is 'AUTO::automation::build_triage::run_001::canonical'. Change the run triage_status to 'manual_review' and save the owner mapping in the automation outputs. Provide the updated details of 'run_001'."
        ),
        actions=[
            Action(name="GetBuildRunDetails", kwargs={ "run_id": "run_001" }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={ "run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows" }),
            Action(name="RecordReproCommandForRun", kwargs={ "run_id": "run_001", "command": "make build-windows-x64" }),
            Action(name="MapPathToOwner", kwargs={ "file_path": "src/game/engine/renderer.cpp" }),
            Action(name="StartAutomationRun", kwargs={ "automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical" }),
            Action(name="SetBuildTriageStatus", kwargs={ "run_id": "run_001", "triage_status": "manual_review" }),
            Action(name="CompleteAutomationRun", kwargs={ "automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "owner_id": "user_001", "owner_path": "src/game/engine/renderer.cpp"} }),
            Action(name="GetBuildRunDetails", kwargs={ "run_id": "run_001" }),
        ],
        outputs=["Run run_001 updated: symbolication attached, repro recorded, triage_status=manual_review, owner persisted"],
    ),
    Task(
        annotator="0",
        user_id="qap_012",
        instruction=(
            "Gather Windows performance evidence and seamlessly associate it with triage for 'run_007'. After completion, confirm the following system updates: a fixed-id performance test run 'AUTO::test_run::pipeline_perf_windows::175' for the 'pipeline_perf_windows' pipeline with totals total=4, failed=2, skipped=0, passed=2, coverage_pct=0.0, and these exact results—'FrameRateTest::SceneB' failed (duration_ms=1100), 'MemoryUsageTest::SceneB' passed (700), 'LoadTimeTest::SceneB' passed (450), 'StutterSpikeTest::SceneB' failed (1300); the 'build_001' artifact metadata indicates perf_baseline='2025-02' and regression_flag='true'; 'run_007' associates with artifacts at 'https://artifacts.techcorp.com/run_007/', includes symbolication for module 'GameEngine.dll' from build 'build_001' on 'windows', logs a bisect outcome with first_bad_commit_sha='commit_def234', last_good_commit_sha='commit_prev111', confidence 0.97, and maintains the repro command 'make perf-benchmark-windows', showing a triage_status of 'manual_review'. Finalize the canonical build_triage automation 'AUTO::automation::build_triage::run_007::canonical', noting outputs with triage_status 'manual_review' and bisect_first_bad 'commit_def234'. For provenance, 'run_007' displays a completed step with step_id 'perf_evidence_consolidated' and name 'perf_evidence_consolidated'. Return the updated details for 'run_007'. Adhere strictly to the given identifiers and values."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={
                "pipeline_id": "pipeline_perf_windows", "total": 4, "failed": 2, "skipped": 0, "passed": 2, "coverage_pct": 0.0
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "FrameRateTest::SceneB", "status": "failed", "duration_ms": 1100
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "MemoryUsageTest::SceneB", "status": "passed", "duration_ms": 700
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "LoadTimeTest::SceneB", "status": "passed", "duration_ms": 450
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "StutterSpikeTest::SceneB", "status": "failed", "duration_ms": 1300
            }),
            Action(name="UpdateArtifactMetadata", kwargs={
                "artifact_id": "build_001", "metadata_patch": {"perf_baseline": "2025-02", "regression_flag": "true"}
            }),
            Action(name="LinkArtifactToRun", kwargs={
                "run_id": "run_007", "artifacts_uri": "https://artifacts.techcorp.com/run_007/"
            }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id": "run_007", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"
            }),
            Action(name="SetFirstBadCommitOnRun", kwargs={
                "run_id": "run_007", "commit_sha": "commit_def234"
            }),
            Action(name="SetBisectResultOnRun", kwargs={
                "run_id": "run_007",
                "first_bad_commit_sha": "commit_def234",
                "last_good_commit_sha": "commit_prev111",
                "confidence": 0.97
            }),
            Action(name="RecordReproCommandForRun", kwargs={
                "run_id": "run_007", "command": "make perf-benchmark-windows"
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_007",
                "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"
            }),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_007::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "manual_review", "bisect_first_bad": "commit_def234"}
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_007", "triage_status": "manual_review"}),
            Action(name="AddRunStep", kwargs={
                "run_id": "run_007",
                "step_id": "perf_evidence_consolidated",
                "name": "perf_evidence_consolidated",
                "status": "completed"
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_007"})
        ],
        outputs=[
            "Performance test run AUTO::test_run::pipeline_perf_windows::175 recorded with 4 results (2 failed); artifact build_001 metadata patched (perf_baseline=2025-02, regression_flag=true).",
            "Run run_007 linked to artifacts, symbolication attached, bisect recorded (first_bad=commit_def234, last_good=commit_prev111, confidence=0.97), repro command recorded, triage_status=manual_review.",
            "Automation AUTO::automation::build_triage::run_007::canonical completed (outputs.triage_status=manual_review, outputs.bisect_first_bad=commit_def234); provenance step perf_evidence_consolidated=completed; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_013",
        instruction=(
            "Handle 'run_001' to achieve a reproducible, auditable triaged condition. Once completed, ensure the run includes Windows symbolication for 'GameEngine.dll' from 'build_001', is identified as a 'compilation_issue', and has the command 'make build-windows-x64' logged as reproducible. Verify the presence of a build_triage automation with the canonical key 'AUTO::automation::build_triage::run_001::canonical' that concludes with outputs indicating triage_status 'in_progress', and ensure the run itself shows a triage_status of 'in_progress'. Finally, update and return the details for 'run_001'. Adhere strictly to the provided identifiers and values."
        ),
        actions=[
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="SetBuildFailureCategorization", kwargs={"run_id": "run_001", "category": "compilation_issue"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Symbolication attached and categorization set for run_001; repro command recorded.",
            "Automation AUTO::automation::build_triage::run_001::canonical completed (outputs.triage_status=in_progress); run triage_status=in_progress; details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_014",
        instruction=(
            "Coordinate a Linux integration failure for 'run_005'. Employ evidence from 'test_run_002' and the ownership of 'src/game/network/multiplayer.cpp' to clearly define the triage process. Guarantee symbolication for 'GameEngine.dll' from 'build_001' on the 'windows' platform, establish the reproducible command 'make test-integration-linux', and oversee a build-triage automation with the key 'AUTO::automation::build_triage::run_005::canonical' that concludes with a triage_status of 'in_progress' and reflects the allocated owner. Provide the updated details of 'run_005'."
        ),
        actions=[
            Action(name="ListFailedTestsForRun", kwargs={ "test_run_id": "test_run_002" }),
            Action(name="MapPathToOwner", kwargs={ "file_path": "src/game/network/multiplayer.cpp" }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={ "run_id": "run_005", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows" }),
            Action(name="RecordReproCommandForRun", kwargs={ "run_id": "run_005", "command": "make test-integration-linux" }),
            Action(name="StartAutomationRun", kwargs={ "automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical" }),
            Action(name="SetBuildTriageStatus", kwargs={ "run_id": "run_005", "triage_status": "in_progress" }),
            Action(name="CompleteAutomationRun", kwargs={ "automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "owner_id": "user_008", "owner_path": "src/game/network/multiplayer.cpp", "evidence_test_run": "test_run_002"} }),
            Action(name="GetBuildRunDetails", kwargs={ "run_id": "run_005" }),
        ],
        outputs=["Run run_005 updated with symbols, repro, triage_status=in_progress; owner persisted from multiplayer.cpp"],
    ),
    Task(
        annotator="0",
        user_id="qap_015",
        instruction=(
            "Handle the formalization of the fix decision for build run 'run_001' ensuring an auditable trail aligns with CI triage. Once finalized, the run retains fix_proposal_id 'fix_010' while triage_status stays 'in_progress'; the standard build_triage automation 'AUTO::automation::build_triage::run_001::canonical' concludes with outputs indicating triage_status 'in_progress' and fix_proposal_id 'fix_010'; run metadata encompasses fix_proposal_summary='fix_010 formalized' for history; and a provenance step with step_id 'fix_proposal_formalized' and name 'fix_proposal_formalized' is noted as completed. Next, offer updated details for 'run_001'. Ensure all identifiers and values are precisely used."
        ),
        actions=[
            Action(name="SetFixProposalOnRun", kwargs={"run_id": "run_001", "fix_proposal_id": "fix_010"}),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "in_progress", "fix_proposal_id": "fix_010"}
            }),
            Action(name="UpdateRunMetadata", kwargs={
                "run_id": "run_001",
                "metadata_patch": {"fix_proposal_summary": "fix_010 formalized"}
            }),
            Action(name="AddRunStep", kwargs={
                "run_id": "run_001",
                "step_id": "fix_proposal_formalized",
                "name": "fix_proposal_formalized",
                "status": "completed"
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Fix proposal fix_010 recorded on run_001; automation completed with triage_status=in_progress; "
            "provenance step fix_proposal_formalized=completed; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_016",
        instruction=(
            "Coordinate the maintenance of triage hygiene on the feature branch ensuring an auditable record is kept. Upon completion, failures on branch 'feature/new-renderer' have undergone review; run 'run_001' shows triage_status 'in_progress', connects artifacts at 'https://artifacts.techcorp.com/run_001/', includes symbolication for module 'GameEngine.dll' from build 'build_001' on platform 'windows', and upholds the reproducible command 'make build-windows-x64'. The run metadata catalogs a failure_category classified as 'render_pipeline_regression' and the first bad commit 'abc123def456789'; the incident context mentions a similar reference to 'run_007' with similarity_score 0.90; and provenance documents completed steps 'triage_fetch_artifacts' and 'triage_repro'. The standard build_triage automation for this run 'AUTO::automation::build_triage::run_001::canonical' finishes with outputs detailing triage_status 'in_progress', along with the branch, repro command, artifacts URI, and symbol module. Provide updated details for 'run_001'. Use precisely these identifiers and values."
        ),
        actions=[
            Action(name="ListFailedBuildRunsByBranch", kwargs={"branch": "feature/new-renderer"}),
            Action(name="LinkArtifactToRun", kwargs={
                "run_id": "run_001",
                "artifacts_uri": "https://artifacts.techcorp.com/run_001/"
            }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id": "run_001",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="RecordReproCommandForRun", kwargs={
                "run_id": "run_001",
                "command": "make build-windows-x64"
            }),
            Action(name="SetBuildFailureCategorization", kwargs={
                "run_id": "run_001",
                "category": "render_pipeline_regression"
            }),
            Action(name="SetFirstBadCommitOnRun", kwargs={
                "run_id": "run_001",
                "commit_sha": "abc123def456789"
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "in_progress",
                    "branch": "feature/new-renderer",
                    "repro_command": "make build-windows-x64",
                    "artifacts_uri": "https://artifacts.techcorp.com/run_001/",
                    "symbol_module": "GameEngine.dll"
                }
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="AppendSimilarIncidentToRun", kwargs={
                "run_id": "run_001",
                "incident_run_id": "run_007",
                "similarity_score": 0.90
            }),
            Action(name="AddRunStep", kwargs={
                "run_id": "run_001",
                "step_id": "triage_fetch_artifacts",
                "name": "triage_fetch_artifacts",
                "status": "completed"
            }),
            Action(name="AddRunStep", kwargs={
                "run_id": "run_001",
                "step_id": "triage_repro",
                "name": "triage_repro",
                "status": "completed"
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Branch failures reviewed; run_001 triage_status=in_progress; artifacts linked; symbolication attached; repro recorded.",
            "Metadata recorded (failure_category.category=render_pipeline_regression; first_bad_commit=abc123def456789); "
            "similar incident linked (run_007, 0.90); provenance steps completed; automation outputs captured; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_017",
        instruction=(
            "Ensure the Linux integration failure in 'run_005' is both traceable and auditable for ownership and triage. Once completed, retain the run metadata showing owner_id 'user_008' (team 'team_003') with ownership_type 'file_owner' and a confidence_score of 0.92. The run must display triage_status 'manual_review'; include Windows symbolication for 'GameEngine.dll' from 'build_001' (platform 'windows'); record the reproducible command 'make test-integration-linux'; and conclude the build_triage automation by running the key 'AUTO::automation::build_triage::run_005::canonical', yielding outputs that list triage_status 'manual_review', owner_id 'user_008', and owner_path 'src/game/network/multiplayer.cpp'. Store a reference to a similar incident, 'run_001', with a similarity_score of 0.92. Conclude by providing the updated details for 'run_005'. Use only the identifiers and values specified."
        ),
        actions=[
            Action(name="PersistOwnerToRun", kwargs={"run_id": "run_005", "owner_id": "user_008", "team_id": "team_003", "ownership_type": "file_owner", "confidence_score": 0.92}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_005", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_005", "command": "make test-integration-linux"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "owner_id": "user_008", "owner_path": "src/game/network/multiplayer.cpp"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
            Action(name="AppendSimilarIncidentToRun", kwargs={"run_id": "run_005", "incident_run_id": "run_001", "similarity_score": 0.92}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_005"})
        ],
        outputs=[
            "Owner persisted to run_005 (owner_id=user_008, team_003, ownership_type=file_owner, confidence_score=0.92); symbolication and repro recorded.",
            "Automation AUTO::automation::build_triage::run_005::canonical completed (outputs.triage_status=manual_review); run triage_status=manual_review; similar incident linked; details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_018",
        instruction=(
            "Anchor Windows shader performance signals within the triage record for 'run_001'. Upon completion, the system will show a test run with id 'AUTO::test_run::pipeline_perf_windows::175' for 'pipeline_perf_windows' (total=2, failed=1, skipped=0, passed=1, coverage_pct=0.0) that includes precisely two outcomes: 'ShaderCompile::BatchA' passed (duration_ms=300) and 'ShaderCompile::BatchB' failed (duration_ms=450). Connect 'run_001' to artifacts located at 'https://artifacts.techcorp.com/run_001/', include symbolication for 'GameEngine.dll' from build 'build_001' on 'windows'. Log within its metadata a failure_category tagged 'performance_regression', record the first bad commit 'abc123def456789', and preserve the repro command 'make test-integration-windows'. After completing a build_triage automation with 'AUTO::automation::build_triage::run_001::canonical', provide outputs indicating triage_status 'in_progress' and the same test_run_id; the run itself must show triage_status 'in_progress', integrate performance_test_run_id='AUTO::test_run::pipeline_perf_windows::175', and reference a similar incident 'run_007' with similarity_score 0.88. Finally, offer the updated details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={"pipeline_id": "pipeline_perf_windows", "total": 2, "failed": 1, "skipped": 0, "passed": 1, "coverage_pct": 0.0}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "ShaderCompile::BatchA", "status": "passed", "duration_ms": 300}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "ShaderCompile::BatchB", "status": "failed", "duration_ms": 450}),
            Action(name="LinkArtifactToRun", kwargs={"run_id": "run_001", "artifacts_uri": "https://artifacts.techcorp.com/run_001/"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="SetBuildFailureCategorization", kwargs={"run_id": "run_001", "category": "performance_regression"}),
            Action(name="SetFirstBadCommitOnRun", kwargs={"run_id": "run_001", "commit_sha": "abc123def456789"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_001", "command": "make test-integration-windows"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id": "run_001", "metadata_patch": {"performance_test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="AppendSimilarIncidentToRun", kwargs={"run_id": "run_001", "incident_run_id": "run_007", "similarity_score": 0.88}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Performance test run AUTO::test_run::pipeline_perf_windows::175 recorded (2 results) and linked; artifacts and symbolication present.",
            "Run run_001 metadata.failure_category.category=performance_regression; first_bad_commit=abc123def456789; repro recorded.",
            "Automation AUTO::automation::build_triage::run_001::canonical completed (triage_status=in_progress, test_run_id linked); run triage_status=in_progress; metadata updated; similar incident run_007 noted; details retrieved"
        ]
    ),


    Task(
        annotator="0",
        user_id="qap_019",
        instruction=(
            "Enhance the triage context for 'run_001'. Upon completion, ensure the run has Windows symbolication connected for 'GameEngine.dll' from 'build_001'; the artifacts are accessible at 'https://artifacts.techcorp.com/run_001/'; its metadata should be updated to {'stability': 'review'}; finalize a build_triage automation with the canonical key 'AUTO::automation::build_triage::run_001::canonical' and outputs indicating triage_status 'manual_review'; and the run itself should reflect triage_status 'manual_review'. Conclude by presenting updated details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="LinkArtifactToRun", kwargs={"run_id": "run_001", "artifacts_uri": "https://artifacts.techcorp.com/run_001/"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id": "run_001", "metadata_patch": {"stability": "review"}}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "manual_review"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Symbolication and artifacts linked for run_001; metadata updated to stability=review.",
            "Automation AUTO::automation::build_triage::run_001::canonical completed (outputs.triage_status=manual_review); run triage_status=manual_review; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_020",
        instruction=(
            "Organize a performance triage record for 'run_007' aligning with real CI practice. By the end, ensure the run shows triage_status 'in_progress'; symbolication is available for 'GameEngine.dll' from build 'build_001' on 'windows'; artifacts can be accessed at 'https://artifacts.techcorp.com/run_007/'; the reproducible command is 'make performance-test-windows'; metadata should record a failure_category with category 'performance_regression' and the first bad commit 'abc123def456789'; complete the canonical build_triage automation 'AUTO::automation::build_triage::run_007::canonical' with outputs showing triage_status 'in_progress'; the incident context must be stored under run.metadata.similar_incidents as precisely one item {incident_run_id='run_001', similarity_score=0.90} (make no changes to any other similarly named fields); and provenance should include completed steps 'triage_fetch_artifacts' and 'triage_repro'. Finish by returning updated details for 'run_007'. Use exactly these identifiers and values."
        ),
        actions=[
            Action(
                name="LinkArtifactToRun",
                kwargs={
                    "run_id": "run_007",
                    "artifacts_uri": "https://artifacts.techcorp.com/run_007/"
                }
            ),
            Action(
                name="AttachSymbolicatedStackToRun",
                kwargs={
                    "run_id": "run_007",
                    "build_id": "build_001",
                    "module_name": "GameEngine.dll",
                    "platform": "windows"
                }
            ),
            Action(
                name="RecordReproCommandForRun",
                kwargs={
                    "run_id": "run_007",
                    "command": "make performance-test-windows"
                }
            ),
            Action(
                name="SetBuildFailureCategorization",
                kwargs={
                    "run_id": "run_007",
                    "category": "performance_regression"
                }
            ),
            Action(
                name="SetFirstBadCommitOnRun",
                kwargs={
                    "run_id": "run_007",
                    "commit_sha": "abc123def456789"
                }
            ),
            Action(
                name="StartAutomationRun",
                kwargs={
                    "automation_type": "build_triage",
                    "input_ref": "run_007",
                    "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"
                }
            ),
            Action(
                name="CompleteAutomationRun",
                kwargs={
                    "automation_run_id": "AUTO::automation::build_triage::run_007::canonical",
                    "status": "completed",
                    "outputs_json": {"triage_status": "in_progress"}
                }
            ),
            Action(
                name="SetBuildTriageStatus",
                kwargs={
                    "run_id": "run_007",
                    "triage_status": "in_progress"
                }
            ),
            Action(
                name="AddRunStep",
                kwargs={
                    "run_id": "run_007",
                    "step_id": "triage_fetch_artifacts",
                    "name": "triage_fetch_artifacts",
                    "status": "completed"
                }
            ),
            Action(
                name="AddRunStep",
                kwargs={
                    "run_id": "run_007",
                    "step_id": "triage_repro",
                    "name": "triage_repro",
                    "status": "completed"
                }
            ),
            Action(
                name="UpdateRunMetadata",
                kwargs={
                    "run_id": "run_007",
                    "metadata_patch": {
                        "similar_incidents": [
                            {"incident_run_id": "run_001", "similarity_score": 0.90}
                        ]
                    }
                }
            ),
            Action(
                name="GetBuildRunDetails",
                kwargs={"run_id": "run_007"}
            )
        ],
        outputs=[
            "Run run_007 prepared for performance triage (triage_status=in_progress) with artifacts and symbolication; repro recorded.",
            "Metadata: failure_category.category=performance_regression; first_bad_commit=abc123def456789; metadata.similar_incidents=[run_001 (0.90)]; provenance steps recorded; automation completed; details retrieved"
        ]
    ),
Task(
        annotator="0",
        user_id="qap_021",
        instruction=(
            "Handle the updating of the Windows performance baseline, linking it to the triage context. Once finished, the system shows the fixed test run id 'AUTO::test_run::pipeline_perf_windows::175' for pipeline 'pipeline_perf_windows' with totals of total=3, failed=0, skipped=1, passed=2, coverage_pct=0.0 and exactly two results - 'LoadTimeTest::LevelX' passed (duration_ms=600) and 'FrameRateTest::LevelX' passed (duration_ms=900); The artifact 'build_001' metadata reflects perf_baseline='2025-03' and regression_flag='false'; the build run 'run_007' displays triage_status 'in_progress', its metadata includes performance_test_run_id='AUTO::test_run::pipeline_perf_windows::175', and provenance indicates a completed 'perf_baseline_updated' step; The canonical build_triage automation 'AUTO::automation::build_triage::run_007::canonical' concludes with outputs that contain triage_status 'in_progress' and the test_run_id. Return with updated details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={"pipeline_id": "pipeline_perf_windows", "total": 3, "failed": 0, "skipped": 1, "passed": 2, "coverage_pct": 0.0}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "LoadTimeTest::LevelX", "status": "passed", "duration_ms": 600}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "FrameRateTest::LevelX", "status": "passed", "duration_ms": 900}),
            Action(name="UpdateArtifactMetadata", kwargs={"artifact_id": "build_001", "metadata_patch": {"perf_baseline": "2025-03", "regression_flag": "false"}}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_007", "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_007::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_007", "triage_status": "in_progress"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id": "run_007", "metadata_patch": {"performance_test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="AddRunStep", kwargs={"run_id": "run_007", "step_id": "perf_baseline_updated", "name": "perf_baseline_updated", "status": "completed"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_007"})
        ],
        outputs=[
            "Performance summary and 2 results recorded for AUTO::test_run::pipeline_perf_windows::175; build_001 patched (perf_baseline=2025-03, regression_flag=false).",
            "run_007 triage_status=in_progress; metadata performance_test_run_id set; provenance step perf_baseline_updated=completed; automation outputs captured; details retrieved."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_022",
        instruction=(
            "Ensure the ownership of the networking failure on 'run_005' is auditable and retained. Upon completion, failures from 'test_run_002' serve as evidence; the path 'src/game/network/multiplayer.cpp' is linked to owner_id 'user_008' (team 'team_003') and this ownership is retained on the run as ownership_type 'file_owner' with a confidence_score of 0.92; the run indicates triage_status 'manual_review' and the canonical build_triage automation for this run ('AUTO::automation::build_triage::run_005::canonical') concludes with outputs that provide triage_status 'manual_review', owner_id 'user_008', owner_path 'src/game/network/multiplayer.cpp', and evidence_test_run 'test_run_002'. The run's provenance notes a completed 'owner_asserted' step. Provide updated details for 'run_005'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="ListFailedTestsForRun", kwargs={"test_run_id": "test_run_002"}),
            Action(name="MapPathToOwner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="PersistOwnerToRun", kwargs={"run_id": "run_005", "owner_id": "user_008", "team_id": "team_003", "ownership_type": "file_owner", "confidence_score": 0.92}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "owner_id": "user_008", "owner_path": "src/game/network/multiplayer.cpp", "evidence_test_run": "test_run_002"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
            Action(name="AddRunStep", kwargs={"run_id": "run_005", "step_id": "owner_asserted", "name": "owner_asserted", "status": "completed"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_005"})
        ],
        outputs=[
            "Ownership persisted for src/game/network/multiplayer.cpp to user_008 (team_003, file_owner, confidence_score=0.92).",
            "run_005 triage_status=manual_review recorded via automation with evidence test_run_002; provenance step owner_asserted=completed; details retrieved."
        ]
    ),


    Task(
        annotator="0",
        user_id="qap_023",
        instruction=(
            "Handle the cataloging and quality-gating of a VFX texture while anchoring its CI triage context. Upon finishing: the catalog should include 'assets/vfx/explosion/explosion_sparks.png' with type 'texture' and name 'Explosion Sparks'; a passed QA is present with severity_max 'warning' and autofix_applied true; the catalog performance_rating is 'medium'; build run 'run_006' links to artifacts at 'https://artifacts.techcorp.com/run_006/', containing symbolication for module 'GameEngine.dll' from build 'build_001' on 'windows', and retains the reproducibility command 'scripts/validate_assets.sh --asset assets/vfx/explosion/explosion_sparks.png --run run_006', displays triage_status 'in_progress', and is marked as 'asset_validation_issue'. The canonical build_triage automation 'AUTO::automation::build_triage::run_006::canonical' concludes with outputs reflecting triage_status 'in_progress'. For provenance, the run confirms a completed step 'vfx_texture_gated'. Provide updated details for 'run_006'. Use only the identifiers and values provided."
        ),
        actions=[
        Action(name="RegisterAssetInCatalog", kwargs={"asset_path": "assets/vfx/explosion/explosion_sparks.png", "asset_type": "texture", "asset_name": "Explosion Sparks"}),
        Action(name="CreateAssetQaResult", kwargs={"asset_path": "assets/vfx/explosion/explosion_sparks.png", "asset_type": "texture", "validation_status": "passed", "severity_max": "warning", "autofix_applied": True}),
        Action(name="UpdateAssetCatalogPerformanceRating", kwargs={"asset_path": "assets/vfx/explosion/explosion_sparks.png", "performance_rating": "medium"}),
        Action(name="LinkArtifactToRun", kwargs={"run_id": "run_006", "artifacts_uri": "https://artifacts.techcorp.com/run_006/"}),
        Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_006", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
        Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_006", "command": "scripts/validate_assets.sh --asset assets/vfx/explosion/explosion_sparks.png --run run_006"}),
        Action(name="SetBuildFailureCategorization", kwargs={"run_id": "run_006", "category": "asset_validation_issue"}),
        Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_006", "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"}),
        Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_006::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
        Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_006", "triage_status": "in_progress"}),
        Action(name="AddRunStep", kwargs={"run_id": "run_006", "step_id": "vfx_texture_gated", "name": "vfx_texture_gated", "status": "completed"}),
        Action(name="GetBuildRunDetails", kwargs={"run_id": "run_006"})
        ],
        outputs=[
        "VFX texture cataloged ('Explosion Sparks'); QA passed (severity_max=warning, autofix_applied=true); performance_rating=medium.",
        "Run run_006 triage enriched: artifacts linked, symbolication attached, category=asset_validation_issue, repro command recorded, triage_status=in_progress.",
        "Automation AUTO::automation::build_triage::run_006::canonical completed (outputs.triage_status=in_progress); provenance step vfx_texture_gated=completed; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_024",
        instruction=(
            "Coordinate the progression of the render regression investigation for 'run_001' while ensuring an audit trail is maintained. When completed: symbolication is appended for 'GameEngine.dll' from 'build_001' on 'windows'; the run notes triage_status 'in_progress'; the reproducible command 'make build-windows-x64' is maintained; the canonical build_triage automation 'AUTO::automation::build_triage::run_001::canonical' concludes with outputs showing triage_status 'in_progress' and symbol_module 'GameEngine.dll'; and provenance indicates a completed step 'symbols_attached'. Subsequently, return updated details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "symbol_module": "GameEngine.dll"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="AddRunStep", kwargs={"run_id": "run_001", "step_id": "symbols_attached", "name": "symbols_attached", "status": "completed"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Symbolication linked (GameEngine.dll, windows); repro command recorded; run_001 triage_status=in_progress; automation outputs captured; provenance step symbols_attached=completed; details retrieved."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_025",
        instruction=(
            "You stabilize the CI context for 'run_001' by ensuring owner accountability, reproducibility, and symbol awareness. Once completed, failed test evidence from 'test_run_002' is referenced; the code path 'src/game/engine/renderer.cpp' is designated for ownership; attach symbolication for module 'GameEngine.dll' from build 'build_001' on platform 'windows' to the run; the run indicates triage_status 'in_progress' and retains the reproducible command 'make build-windows-x64'; meanwhile, finalize the canonical build_triage automation for this run 'AUTO::automation::build_triage::run_001::canonical' with outputs that include triage_status 'in_progress', owner_id 'user_001', owner_path 'src/game/engine/renderer.cpp', and evidence_test_run 'test_run_002'. You then provide updated details for 'run_001'. Utilize only the specified identifiers and values."
        ),
        actions=[
            Action(name="ListFailedTestsForRun", kwargs={"test_run_id": "test_run_002"}),
            Action(name="MapPathToOwner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(
                name="AttachSymbolicatedStackToRun",
                kwargs={
                    "run_id": "run_001",
                    "build_id": "build_001",
                    "module_name": "GameEngine.dll",
                    "platform": "windows"
                }
            ),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(
                name="StartAutomationRun",
                kwargs={
                    "automation_type": "build_triage",
                    "input_ref": "run_001",
                    "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
                }
            ),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(
                name="CompleteAutomationRun",
                kwargs={
                    "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                    "status": "completed",
                    "outputs_json": {
                        "triage_status": "in_progress",
                        "owner_id": "user_001",
                        "owner_path": "src/game/engine/renderer.cpp",
                        "evidence_test_run": "test_run_002"
                    }
                }
            ),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Triage recorded: in_progress for run_001 with evidence test_run_002; ownership mapped for src/game/engine/renderer.cpp; symbolication attached; repro recorded; details retrieved."
        ]
    ),


    Task(
        annotator="0",
        user_id="qap_026",
        instruction=(
            "You organize asset intake, catalog, and CI triage for a hero model with an auditable trail. Upon completion, the system will reflect all of the following: a passed QA check for 'assets/characters/hero/hero_body.fbx' (type 'model', severity_max 'info', autofix_applied true); the registering of the same path in the catalog as 'Hero Body' with performance_rating 'high'; build run 'run_006' connects artifacts at 'https://artifacts.techcorp.com/run_006/', includes symbolication for module 'GameEngine.dll' from build 'build_001' on platform 'windows', is branded as 'asset_validation_issue', retains the reproducibility command 'scripts/validate_assets.sh --asset assets/characters/hero/hero_body.fbx --run run_006', and signifies triage_status 'manual_review'. Conclude the canonical build_triage automation 'AUTO::automation::build_triage::run_006::canonical' with outputs comprising triage_status 'manual_review' and asset_path 'assets/characters/hero/hero_body.fbx'. For provenance, the run will display completed steps 'triage_fetch_artifacts' and 'asset_intake_validated'. Provide updated details for 'run_006'. Use solely the identifiers and values listed here."
        ),
        actions=[
        Action(name="CreateAssetQaResult", kwargs={"asset_path": "assets/characters/hero/hero_body.fbx", "asset_type": "model", "validation_status": "passed", "severity_max": "info", "autofix_applied": True}),
        Action(name="RegisterAssetInCatalog", kwargs={"asset_path": "assets/characters/hero/hero_body.fbx", "asset_type": "model", "asset_name": "Hero Body"}),
        Action(name="UpdateAssetCatalogPerformanceRating", kwargs={"asset_path": "assets/characters/hero/hero_body.fbx", "performance_rating": "high"}),
        Action(name="LinkArtifactToRun", kwargs={"run_id": "run_006", "artifacts_uri": "https://artifacts.techcorp.com/run_006/"}),
        Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_006", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
        Action(name="SetBuildFailureCategorization", kwargs={"run_id": "run_006", "category": "asset_validation_issue"}),
        Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_006", "command": "scripts/validate_assets.sh --asset assets/characters/hero/hero_body.fbx --run run_006"}),
        Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_006", "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"}),
        Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_006::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "asset_path": "assets/characters/hero/hero_body.fbx"}}),
        Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_006", "triage_status": "manual_review"}),
        Action(name="AddRunStep", kwargs={"run_id": "run_006", "step_id": "triage_fetch_artifacts", "name": "triage_fetch_artifacts", "status": "completed"}),
        Action(name="AddRunStep", kwargs={"run_id": "run_006", "step_id": "asset_intake_validated", "name": "asset_intake_validated", "status": "completed"}),
        Action(name="GetBuildRunDetails", kwargs={"run_id": "run_006"})
        ],
        outputs=[
        "QA recorded for assets/characters/hero/hero_body.fbx (passed, severity_max=info, autofix_applied=true); catalog 'Hero Body' with performance_rating=high.",
        "Run run_006 linked to artifacts, symbolication attached, category=asset_validation_issue, repro command recorded, triage_status=manual_review.",
        "Automation AUTO::automation::build_triage::run_006::canonical completed (outputs include triage_status=manual_review, asset_path set); provenance steps recorded; details retrieved."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_027",
        instruction=(
            "Handle the documentation of a targeted fix proposal regarding a shader compile issue on 'run_001', ensuring traceability. Once finalized, the run displays fix_proposal_id 'fix_shader_001', and triage_status stays 'in_progress'. The canonical automation 'AUTO::automation::build_triage::run_001::canonical' concludes with outputs showing triage_status 'in_progress' and fix_proposal_id 'fix_shader_001'. Provenance indicates a finished step 'fix_proposal_documented', and the incident context references 'run_007' with a similarity_score of 0.85. Provide updated information for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="SetFixProposalOnRun", kwargs={"run_id": "run_001", "fix_proposal_id": "fix_shader_001"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "fix_proposal_id": "fix_shader_001"}}),
            Action(name="AppendSimilarIncidentToRun", kwargs={"run_id": "run_001", "incident_run_id": "run_007", "similarity_score": 0.85}),
            Action(name="AddRunStep", kwargs={"run_id": "run_001", "step_id": "fix_proposal_documented", "name": "fix_proposal_documented", "status": "completed"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Fix proposal fix_shader_001 recorded; run_001 triage_status=in_progress; automation outputs captured; similar incident run_007 (0.85) noted; provenance step fix_proposal_documented=completed; details retrieved."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_028",
        instruction=(
            "Coordinate a consolidated Windows performance snapshot and associate it with the triage record for 'run_001', ensuring reproducibility and provenance. By the end, the system indicates a fixed-id performance test run 'AUTO::test_run::pipeline_perf_windows::175' for pipeline 'pipeline_perf_windows' with totals total=2, failed=0, skipped=0, passed=2, coverage_pct=0.0. Two results are observed: 'StreamingIO::ChunkLoad' passed (duration_ms=250) and 'Serialization::SaveGame' passed (duration_ms=380). 'run_001' links artifacts at 'https://artifacts.techcorp.com/run_001/', includes Windows symbolication for 'GameEngine.dll' from build 'build_001', logs the initial bad commit 'abc123def456789', maintains the reproducible command 'make perf-benchmark-windows', and shows triage_status 'in_progress'. The canonical build_triage automation 'AUTO::automation::build_triage::run_001::canonical' is finished, with outputs including triage_status 'in_progress' and test_run_id 'AUTO::test_run::pipeline_perf_windows::175'. Run metadata lists performance_test_run_id='AUTO::test_run::pipeline_perf_windows::175'. The incident context notes a similar point of reference to 'run_007' with a similarity_score of 0.88, and provenance confirms a finished step 'perf_snapshot_curated'. Provide refreshed details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={"pipeline_id": "pipeline_perf_windows", "total": 2, "failed": 0, "skipped": 0, "passed": 2, "coverage_pct": 0.0}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "StreamingIO::ChunkLoad", "status": "passed", "duration_ms": 250}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "Serialization::SaveGame", "status": "passed", "duration_ms": 380}),
            Action(name="LinkArtifactToRun", kwargs={"run_id": "run_001", "artifacts_uri": "https://artifacts.techcorp.com/run_001/"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="SetFirstBadCommitOnRun", kwargs={"run_id": "run_001", "commit_sha": "abc123def456789"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_001", "command": "make perf-benchmark-windows"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id": "run_001", "metadata_patch": {"performance_test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="AppendSimilarIncidentToRun", kwargs={"run_id": "run_001", "incident_run_id": "run_007", "similarity_score": 0.88}),
            Action(name="AddRunStep", kwargs={"run_id": "run_001", "step_id": "perf_snapshot_curated", "name": "perf_snapshot_curated", "status": "completed"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Performance test run AUTO::test_run::pipeline_perf_windows::175 recorded (2 passing) and linked in run_001 metadata.",
            "Run run_001 enriched: artifacts linked, symbolication attached, first_bad_commit=abc123def456789, repro recorded, triage_status=in_progress.",
            "Automation AUTO::automation::build_triage::run_001::canonical completed (outputs include triage_status=in_progress and test_run_id); similar incident run_007 (0.88) noted; provenance step perf_snapshot_curated=completed; details retrieved."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_029",
        instruction=(
            "Handle the validation and cataloging of the texture, recording the asset decision in the CI record. Upon finalizing, 'assets/textures/environment/castle_tower_diffuse.png' (type 'texture') should have a QA result documented with validation_status 'failed', severity_max 'issue', and autofix_applied true; QA 'qa_004' is upgraded to pass; the catalog performance_rating for that asset remains 'high'; and execute the canonical build_triage automation for 'run_006' ('AUTO::automation::build_triage::run_006::canonical') to completion with outputs indicating asset_path 'assets/textures/environment/castle_tower_diffuse.png', validation_status 'failed', and performance_rating 'high'. Ensure to utilize only these specific identifiers and values."
        ),
        actions=[
            Action(name="CreateAssetQaResult", kwargs={"asset_path": "assets/textures/environment/castle_tower_diffuse.png", "asset_type": "texture", "validation_status": "failed", "severity_max": "issue", "autofix_applied": True}),
            Action(name="PromoteAssetAutofixToPass", kwargs={"qa_id": "qa_004"}),
            Action(name="UpdateAssetCatalogPerformanceRating", kwargs={"asset_path": "assets/textures/environment/castle_tower_diffuse.png", "performance_rating": "high"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_006", "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_006::canonical", "status": "completed", "outputs_json": {"asset_path": "assets/textures/environment/castle_tower_diffuse.png", "validation_status": "failed", "performance_rating": "high"}})
        ],
        outputs=[
            "Asset castle_tower_diffuse.png QA recorded (failed, issue, autofix_applied=true), promoted qa_004 to pass; catalog performance_rating=high; automation recorded asset decision."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_030",
        instruction=(
            "Coordinate the establishment of symbol availability over two runs within an auditable context. Once finished, both 'run_005' and 'run_007' should include symbolication for module 'GameEngine.dll' from build 'build_001' on 'windows' while maintaining triage_status at 'in_progress'; finalize the canonical build_triage automation for each run ('AUTO::automation::build_triage::run_005::canonical' and 'AUTO::automation::build_triage::run_007::canonical') with outputs featuring triage_status 'in_progress'; and confirm provenance shows a finished step 'symbols_verified' for each. Adhere strictly to these identifiers and values."
        ),
        actions=[
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_005", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_007", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_005", "triage_status": "in_progress"}),
            Action(name="AddRunStep", kwargs={"run_id": "run_005", "step_id": "symbols_verified", "name": "symbols_verified", "status": "completed"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_007", "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_007::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_007", "triage_status": "in_progress"}),
            Action(name="AddRunStep", kwargs={"run_id": "run_007", "step_id": "symbols_verified", "name": "symbols_verified", "status": "completed"})
        ],
        outputs=[
            "Symbolication attached and triage_status=in_progress for run_005 and run_007; automation outputs captured; provenance steps symbols_verified=completed for both."
        ]
    ),
        Task(
        annotator="0",
        user_id="qap_031",
        instruction=(
            "Handle publishing an AI behavior performance snapshot and associate it with CI triage. Upon completion, the system logs a test run 'AUTO::test_run::pipeline_perf_windows::175' for 'pipeline_perf_windows', including totals: total=2, failed=1, skipped=0, passed=1, and coverage_pct=0.0. Specifically, 'AI::PathfindingNavmesh' failed (duration_ms=980), while 'AI::DecisionTreeTick' passed (410). The artifact 'build_001' metadata notes ai_profile='aggressive'. Build run 'run_007' shows triage_status 'in_progress', a finalized canonical build_triage automation 'AUTO::automation::build_triage::run_007::canonical', with outcomes listing ai_test_run_id 'AUTO::test_run::pipeline_perf_windows::175', and the run metadata holds ai_perf_test_run_id='AUTO::test_run::pipeline_perf_windows::175'. Coordinate the return of updated details for 'run_007'. Ensure only these identifiers and values are utilized."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={"pipeline_id":"pipeline_perf_windows","total":2,"failed":1,"skipped":0,"passed":1,"coverage_pct":0.0}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"AI::PathfindingNavmesh","status":"failed","duration_ms":980}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"AI::DecisionTreeTick","status":"passed","duration_ms":410}),
            Action(name="UpdateArtifactMetadata", kwargs={"artifact_id":"build_001","metadata_patch":{"ai_profile":"aggressive"}}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"ai_test_run_id":"AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id":"run_007","metadata_patch":{"ai_perf_test_run_id":"AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "AI perf run AUTO::test_run::pipeline_perf_windows::175 recorded (1 failed) and linked to run_007; build_001 ai_profile=aggressive.",
            "Automation AUTO::automation::build_triage::run_007::canonical completed (outputs.ai_test_run_id set); run_007 triage_status=in_progress; metadata linked; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_032",
        instruction=(
            "Coordinate the creation of a performance-triage evidence bundle for 'run_006', ensuring a clear audit trail. After finalization, the metadata for run_006 indicates priority='high'; the command 'make perf-benchmark-windows' for reproducibility is documented; symbolication for 'GameEngine.dll' from 'build_001' on 'windows' is included; 'run_007' is referenced as a similar incident with a similarity_score of 0.87; and the run displays a triage_status of 'manual_review' via a completed canonical build_triage automation 'AUTO::automation::build_triage::run_006::canonical', producing outputs that report triage_status 'manual_review'. Provenance confirms the completion of the steps 'triage_fetch_artifacts' and 'triage_repro'. Facilitate the return of updated details for 'run_006'. Use exclusively these identifiers and values."
        ),
        actions=[
            Action(name="UpdateRunMetadata", kwargs={"run_id":"run_006","metadata_patch":{"priority":"high"}}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id":"run_006","command":"make perf-benchmark-windows"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id":"run_006","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="AppendSimilarIncidentToRun", kwargs={"run_id":"run_006","incident_run_id":"run_007","similarity_score":0.87}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_006","automation_run_id":"AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_006","step_id":"triage_fetch_artifacts","name":"triage_fetch_artifacts","status":"completed"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_006","step_id":"triage_repro","name":"triage_repro","status":"completed"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed","outputs_json":{"triage_status":"manual_review"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_006"})
        ],
        outputs=[
            "run_006 priority=high; repro recorded; symbolication attached; similar incident run_007 (0.87); steps triage_fetch_artifacts & triage_repro=completed.",
            "Automation AUTO::automation::build_triage::run_006::canonical completed with triage_status=manual_review; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_033",
        instruction=(
            "Handle cataloging and quality control for the UI audio click while presenting its CI context. Upon completion, ensure the catalog lists 'assets/audio/ui/click.wav' as 'audio' with asset_name 'UI Click'; verify a QA record exists with validation_status 'passed', severity_max 'info', and autofix_applied marked as false; confirm the catalog performance_rating is noted as 'high'; track build run 'run_006' under the ongoing canonical build_triage automation 'AUTO::automation::build_triage::run_006::canonical' with triage_status of 'in_progress'; include Windows symbolication for 'GameEngine.dll' from 'build_001' on 'windows'; establish provenance showing 'audio_asset_evidence_ingest' has completed; and ensure run metadata contains audio_asset_path='assets/audio/ui/click.wav'. Provide updated details for 'run_006'. Utilize only the given identifiers and values."
        ),
        actions=[
            Action(name="RegisterAssetInCatalog", kwargs={
                "asset_path":"assets/audio/ui/click.wav","asset_type":"audio","asset_name":"UI Click"
            }),
            Action(name="CreateAssetQaResult", kwargs={
                "asset_path":"assets/audio/ui/click.wav","asset_type":"audio",
                "validation_status":"passed","severity_max":"info","autofix_applied":False
            }),
            Action(name="UpdateAssetCatalogPerformanceRating", kwargs={
                "asset_path":"assets/audio/ui/click.wav","performance_rating":"high"
            }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id":"run_006","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type":"build_triage","input_ref":"run_006",
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_006","triage_status":"in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical",
                "status":"completed","outputs_json":{"triage_status":"in_progress"}
            }),
            Action(name="AddRunStep", kwargs={
                "run_id":"run_006","step_id":"audio_asset_evidence_ingest","name":"audio_asset_evidence_ingest","status":"completed"
            }),
            Action(name="UpdateRunMetadata", kwargs={
                "run_id":"run_006","metadata_patch":{"audio_asset_path":"assets/audio/ui/click.wav"}
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_006"})
        ],
        outputs=[
            "Audio asset cataloged and QA recorded; performance_rating=high; symbolication attached; "
            "triage_status=in_progress with evidence step completed; audio_asset_path stored; details retrieved."
        ]
    ),


    Task(
        annotator="0",
        user_id="qap_034",
        instruction=(
            "Coordinate making 'run_007' reproducible and symbol-aware for performance triage with incident correlation. At the end, ensure the run includes the command 'make performance-test-windows'; carries symbolication for 'GameEngine.dll' from 'build_001' on 'windows'; reflects a triage_status of 'manual_review' within a completed canonical build_triage automation 'AUTO::automation::build_triage::run_007::canonical'; includes in the provenance a completed step 'triage_repro'; and logs an incident similar to 'run_006' with similarity_score 0.83. Return updated information for 'run_007'. Use exclusively these identifiers and values."
        ),
        actions=[
            Action(name="RecordReproCommandForRun", kwargs={"run_id":"run_007","command":"make performance-test-windows"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id":"run_007","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="AppendSimilarIncidentToRun", kwargs={"run_id":"run_007","incident_run_id":"run_006","similarity_score":0.83}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_007","triage_status":"manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"triage_status":"manual_review"}}),
            Action(name="AddRunStep", kwargs={"run_id":"run_007","step_id":"triage_repro","name":"triage_repro","status":"completed"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "Repro recorded and symbolication attached; similar incident run_006 (0.83) noted; provenance step triage_repro=completed.",
            "Automation completed with triage_status=manual_review; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_035",
        instruction=(
            "Administer a memory-profiling snapshot and link it to CI triage for 'run_007'. Once completed, the system retains test run 'AUTO::test_run::pipeline_perf_windows::175' for 'pipeline_perf_windows', with summaries showing total=2, failed=0, skipped=0, passed=2, and coverage_pct=0.0, and precisely two results—'Memory::PeakUsageSceneA' succeeded (820) and 'Memory::PeakUsageSceneB' succeeded (910); artifact 'build_001' metadata records specifying memory_sampling='heap_only'; symbolication associated with 'GameEngine.dll' from 'build_001' on 'windows' is incorporated into the run; 'run_007' indicates triage_status 'in_progress'; the standard build_triage automation 'AUTO::automation::build_triage::run_007::canonical' is finalized with outputs including performance_test_run_id 'AUTO::test_run::pipeline_perf_windows::175' and triage_status 'in_progress'; run metadata records performance_test_run_id='AUTO::test_run::pipeline_perf_windows::175'; and provenance marks a completed step 'perf_snapshot_curated'. Refine and provide updated details for 'run_007'. Only utilize these identifiers and values."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={"pipeline_id":"pipeline_perf_windows","total":2,"failed":0,"skipped":0,"passed":2,"coverage_pct":0.0}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"Memory::PeakUsageSceneA","status":"passed","duration_ms":820}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"Memory::PeakUsageSceneB","status":"passed","duration_ms":910}),
            Action(name="UpdateArtifactMetadata", kwargs={"artifact_id":"build_001","metadata_patch":{"memory_sampling":"heap_only"}}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id":"run_007","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"performance_test_run_id":"AUTO::test_run::pipeline_perf_windows::175","triage_status":"in_progress"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id":"run_007","metadata_patch":{"performance_test_run_id":"AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="AddRunStep", kwargs={"run_id":"run_007","step_id":"perf_snapshot_curated","name":"perf_snapshot_curated","status":"completed"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "Memory snapshot AUTO::test_run::pipeline_perf_windows::175 recorded (2 passing); build_001 memory_sampling=heap_only; symbolication attached.",
            "Automation completed (outputs.performance_test_run_id and triage_status=in_progress); run_007 triage_status=in_progress; metadata linked; provenance step perf_snapshot_curated=completed; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_036",
        instruction=(
            "Gather reproducibility and evidence for 'run_008' to bolster manual triage. Upon conclusion, the run archives reproducible command 'make test-windows-x64'; includes symbolication for 'GameEngine.dll' from 'build_001' on 'windows'; metadata documents repro_env='windows_x64_ci'; provenance lists completed steps 'triage_repro' and 'evidence_bundle'; a related incident points to 'run_006' with similarity_score 0.82; and the run manifests triage_status 'manual_review' under a completed conventional build_triage automation 'AUTO::automation::build_triage::run_008::canonical' whose outputs reveal triage_status 'manual_review'. Provide updated details for 'run_008'. Use solely these identifiers and values."
        ),
        actions=[
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_008","automation_run_id":"AUTO::automation::build_triage::run_008::canonical"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id":"run_008","command":"make test-windows-x64"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id":"run_008","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id":"run_008","metadata_patch":{"repro_env":"windows_x64_ci"}}),
            Action(name="AddRunStep", kwargs={"run_id":"run_008","step_id":"triage_repro","name":"triage_repro","status":"completed"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_008","step_id":"evidence_bundle","name":"evidence_bundle","status":"completed"}),
            Action(name="AppendSimilarIncidentToRun", kwargs={"run_id":"run_008","incident_run_id":"run_006","similarity_score":0.82}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_008","triage_status":"manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_008::canonical","status":"completed","outputs_json":{"triage_status":"manual_review"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_008"})
        ],
        outputs=[
            "Repro recorded; symbolication attached; metadata.repro_env=windows_x64_ci; steps triage_repro & evidence_bundle=completed; similar incident run_006 (0.82).",
            "Automation AUTO::automation::build_triage::run_008::canonical completed with triage_status=manual_review; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_037",
        instruction=(
            "Register and verify the UI texture while highlighting its CI context. Upon completion, the catalog includes 'assets/textures/ui/health_bar.png' typed as 'texture' with the name 'Health Bar'; a QA record is present for that texture with validation_status 'failed', severity_max 'warning', autofix_applied true; the catalog performance_rating is 'medium'; symbolication for 'GameEngine.dll' from 'build_001' on 'windows' is attached; and build run 'run_006' reflects triage_status 'manual_review' under a completed canonical build_triage automation 'AUTO::automation::build_triage::run_006::canonical'. Provide updated details for 'run_006'. Use only the given identifiers and values."
        ),
        actions=[
            Action(name="RegisterAssetInCatalog", kwargs={"asset_path":"assets/textures/ui/health_bar.png","asset_type":"texture","asset_name":"Health Bar"}),
            Action(name="CreateAssetQaResult", kwargs={"asset_path":"assets/textures/ui/health_bar.png","asset_type":"texture","validation_status":"failed","severity_max":"warning","autofix_applied":True}),
            Action(name="UpdateAssetCatalogPerformanceRating", kwargs={"asset_path":"assets/textures/ui/health_bar.png","performance_rating":"medium"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id":"run_006","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_006","automation_run_id":"AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed","outputs_json":{"triage_status":"manual_review"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_006"})
        ],
        outputs=[
            "Texture registered; QA recorded (failed, severity_max=warning, autofix_applied=true); performance_rating=medium; symbolication attached.",
            "Run run_006 triage_status=manual_review; automation completed; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_038",
        instruction=(
            "Set up a deterministic performance record and connect it to triage for 'run_007'. By the end, the system contains fixed test_run 'AUTO::test_run::pipeline_perf_windows::175' for 'pipeline_perf_windows' with totals total=3, failed=1, skipped=0, passed=2, coverage_pct=78.3 and exactly three results—'FrameRateTest::SceneB' failed (1300), 'MemoryUsageTest::SceneB' passed (780), 'LoadTimeTest::SceneB' passed (520); artifact 'build_002' metadata records perf_baseline='2025-02' and regression_flag=true; 'run_007' reflects triage_status 'in_progress', a completed canonical build_triage automation 'AUTO::automation::build_triage::run_007::canonical' whose outputs include test_run_id 'AUTO::test_run::pipeline_perf_windows::175', and run metadata stores performance_test_run_id='AUTO::test_run::pipeline_perf_windows::175'; and provenance shows a completed step 'triage_fetch_artifacts'. Return updated details for 'run_007'. Use only the specified identifiers and values."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={"pipeline_id":"pipeline_perf_windows","total":3,"failed":1,"skipped":0,"passed":2,"coverage_pct":78.3}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"FrameRateTest::SceneB","status":"failed","duration_ms":1300}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"MemoryUsageTest::SceneB","status":"passed","duration_ms":780}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"LoadTimeTest::SceneB","status":"passed","duration_ms":520}),
            Action(name="UpdateArtifactMetadata", kwargs={"artifact_id":"build_002","metadata_patch":{"perf_baseline":"2025-02","regression_flag":True}}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"test_run_id":"AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id":"run_007","metadata_patch":{"performance_test_run_id":"AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="AddRunStep", kwargs={"run_id":"run_007","step_id":"triage_fetch_artifacts","name":"triage_fetch_artifacts","status":"completed"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "Performance test run AUTO::test_run::pipeline_perf_windows::175 recorded with 3 results; build_002 metadata patched.",
            "Automation completed (outputs.test_run_id set); run_007 triage_status=in_progress; metadata linked; provenance triage_fetch_artifacts=completed; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_039",
        instruction=(
            "Ensure the networking failure on 'run_005' is fully auditable, providing clear ownership and context. Upon completion, the ownership resolved from 'src/game/network/multiplayer.cpp' is saved to the run as owner_id 'user_008', team 'team_003', ownership_type 'file_owner', with a confidence_score of 0.92; the run logs repro command 'make test-networking-lan'; includes symbolication for 'GameEngine.dll' from 'build_001' on 'windows'; provenance lists steps 'triage_fetch_artifacts' and 'owner_resolution' as completed; a related incident references 'run_004' with a similarity_score of 0.83; and the run indicates triage_status 'manual_review' after a completed canonical build_triage automation 'AUTO::automation::build_triage::run_005::canonical' which outputs report triage_status 'manual_review' and owner_path 'src/game/network/multiplayer.cpp'. Provide updated details for 'run_005'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="PersistOwnerToRun", kwargs={"run_id":"run_005","owner_id":"user_008","team_id":"team_003","ownership_type":"file_owner","confidence_score":0.92}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id":"run_005","command":"make test-networking-lan"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id":"run_005","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_005","automation_run_id":"AUTO::automation::build_triage::run_005::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_005","triage_status":"manual_review"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_005","step_id":"triage_fetch_artifacts","name":"triage_fetch_artifacts","status":"completed"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_005","step_id":"owner_resolution","name":"owner_resolution","status":"completed"}),
            Action(name="AppendSimilarIncidentToRun", kwargs={"run_id":"run_005","incident_run_id":"run_004","similarity_score":0.83}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_005::canonical","status":"completed","outputs_json":{"triage_status":"manual_review","owner_id":"user_008","owner_path":"src/game/network/multiplayer.cpp"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_005"})
        ],
        outputs=[
            "Ownership persisted to user_008 (team_003, file_owner, confidence=0.92); repro recorded; symbolication attached; steps triage_fetch_artifacts & owner_resolution=completed; similar incident run_004 (0.83).",
            "Automation AUTO::automation::build_triage::run_005::canonical completed with triage_status=manual_review; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_040",
        instruction=(
            "Organize symbol availability and root‑cause context for build run 'run_001'. When completed, symbols for the module 'GameEngine.dll' from 'build_001' on 'windows' are recorded and linked to the run; the failure is categorized as a 'compilation_issue'; the first_bad_commit is 'abc123def456789'; and the canonical build_triage automation 'AUTO::automation::build_triage::run_001::canonical' concludes with outputs indicating triage_status 'in_progress', while the run itself indicates triage_status 'in_progress'. Provide updated details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="RegisterSymbol", kwargs={"build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id":"run_001","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="SetBuildFailureCategorization", kwargs={"run_id":"run_001","category":"compilation_issue"}),
            Action(name="SetFirstBadCommitOnRun", kwargs={"run_id":"run_001","commit_sha":"abc123def456789"}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_001","automation_run_id":"AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_001","triage_status":"in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_001::canonical","status":"completed","outputs_json":{"triage_status":"in_progress"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_001"})
        ],
        outputs=[
            "Symbols registered and attached; run_001 categorized as compilation_issue with first_bad_commit=abc123def456789.",
            "Automation completed with triage_status=in_progress; run triage_status=in_progress; details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_041",
        instruction=(
            "Handle 'run_007' to ensure it is auditable with a distinct classification snapshot and reproducibility context. Upon completion, ensure the run's metadata includes failure_category as 'test_failure'; first_bad_commit as 'abc123def456789'; note the repro command 'make test-windows-x64'; set triage_status to 'in_progress' within the finalized canonical automation 'AUTO::automation::build_triage::run_007::canonical', which outputs include triage_status 'in_progress' and failure_categorization 'test_failure'; and ensure provenance indicates a step 'triage_classified' as completed. Provide the updated details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id":"run_007","command":"make test-windows-x64"}),
            Action(name="SetFirstBadCommitOnRun", kwargs={"run_id":"run_007","commit_sha":"abc123def456789"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_007","step_id":"triage_classified","name":"triage_classified","status":"completed"}),
            Action(name="SetBuildFailureCategorization", kwargs={"run_id":"run_007","category":"test_failure"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"triage_status":"in_progress","failure_categorization":"test_failure"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "run_007: failure_categorization remained 'performance_regression'; metadata.failure_category stored as {category:'test_failure'}; first_bad_commit=abc123def456789; repro preserved; triage_status=in_progress via automation; step triage_classified=completed; details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_042",
        instruction=(
            "Coordinate owner responsibility for 'run_005'. Upon finishing, make sure the run's metadata retains owner_id 'user_001' and owner_path 'src/game/engine/renderer.cpp'; attach symbolication for 'GameEngine.dll' from 'build_001' on 'windows'; and set triage_status to 'manual_review' within the finalized canonical automation 'AUTO::automation::build_triage::run_005::canonical' showing that status. Provide the updated details for 'run_005'. Use only these identifiers and values."
        ),
        actions=[
        Action(name="MapPathToOwner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
        Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_005", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
        Action(name="UpdateRunMetadata", kwargs={"run_id": "run_005", "metadata_patch": {"owner_id": "user_001", "owner_path": "src/game/engine/renderer.cpp"}}),
        Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
        Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
        Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "owner_id": "user_001", "owner_path": "src/game/engine/renderer.cpp"}}),
        Action(name="GetBuildRunDetails", kwargs={"run_id": "run_005"})
        ],
        outputs=[
        "Ownership persisted (user_001 for src/game/engine/renderer.cpp); symbolication attached; triage_status=manual_review captured via automation; run_005 details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_043",
        instruction=(
            "Handle the enrichment of incident context for 'run_005'. Once finished, the run includes a reference to a similar incident 'run_003' with a similarity_score of 0.84; a bisect outcome identifies the first_bad_commit 'commit_def456' and the last_good_commit 'commit_prev111' with a confidence of 0.95; metadata identifies owner_team as 'networking'; and triage_status is noted as 'manual_review' with completion of the canonical automation 'AUTO::automation::build_triage::run_005::canonical'. Return the updated details for 'run_005'."
        ),
        actions=[
        Action(name="AppendSimilarIncidentToRun", kwargs={"run_id": "run_005", "incident_run_id": "run_003", "similarity_score": 0.84}),
        Action(name="SetBisectResultOnRun", kwargs={"run_id": "run_005", "first_bad_commit_sha": "commit_def456", "last_good_commit_sha": "commit_prev111", "confidence": 0.95}),
        Action(name="UpdateRunMetadata", kwargs={"run_id": "run_005", "metadata_patch": {"owner_team": "networking"}}),
        Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
        Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
        Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "bisect_first_bad": "commit_def456"}}),
        Action(name="GetBuildRunDetails", kwargs={"run_id": "run_005"})
        ],
        outputs=[
        "Similar incident run_003 (0.84) recorded; bisect first_bad=commit_def456 last_good=commit_prev111 (0.95); metadata updated; triage_status=manual_review recorded; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_044",
        instruction=(
            "Coordinate the provision of symbol context for 'run_001'. At the conclusion, symbols for 'AudioEngine.dll' sourced from 'build_003' on 'windows' are documented, and the symbolicated stack is linked to the run; triage_status is set to 'in_progress' with the completion of the canonical automation 'AUTO::automation::build_triage::run_001::canonical' capturing this status. Return the updated details for 'run_001'."
        ),
        actions=[
        Action(name="RegisterSymbol", kwargs={"build_id": "build_003", "module_name": "AudioEngine.dll", "platform": "windows"}),
        Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_001", "build_id": "build_003", "module_name": "AudioEngine.dll", "platform": "windows"}),
        Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
        Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
        Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
        Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
        "Symbols registered and attached (AudioEngine.dll build_003/windows); triage_status=in_progress recorded; run_001 details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_045",
        instruction=(
            "Handle the consolidation of a reproducible triage dossier for 'run_001' which links evidence, ownership, and artifact context. Upon finished execution, ensure that the run maintains the reproducible command 'make build-windows-x64'; incorporates Windows symbolication for 'GameEngine.dll' from 'build_001'; connects with artifact 'build_002', where the metadata shows hotfix_candidate=true and perf_baseline='2025-03'; an evidence test run 'AUTO::test_run::pipeline_perf_windows::175' should exist, featuring totals total=2, failed=1, skipped=0, passed=1, coverage_pct=78.0, with exactly two outcomes—'FrameRateTest::SceneC' failed (1250) and 'MemoryUsageTest::SceneC' passed (810); ownership is recorded as owner_id 'user_001' for owner_path 'src/game/engine/renderer.cpp' with ownership_type 'file_owner' and confidence_score 0.9; a similar incident is linked to 'run_006' with similarity_score 0.88; provenance should reveal completed steps 'triage_fetch_artifacts' and 'owner_resolution'; triage status is noted as 'in_progress' under the completed canonical build_triage automation 'AUTO::automation::build_triage::run_001::canonical'; and run metadata contains {'evidence_test_run':'AUTO::test_run::pipeline_perf_windows::175','linked_artifact':'build_002'}. Present updated details for 'run_001'. Utilize only these identifiers and values."
        ),
        actions=[
            Action(name="RecordReproCommandForRun", kwargs={"run_id":"run_001","command":"make build-windows-x64"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id":"run_001","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"
            }),
            Action(name="LinkArtifactToRun", kwargs={"run_id":"run_001","artifact_id":"build_002"}),
            Action(name="UpdateArtifactMetadata", kwargs={
                "artifact_id":"build_002","metadata_patch":{"hotfix_candidate":True,"perf_baseline":"2025-03"}
            }),
            Action(name="CreateTestRunSummary", kwargs={
                "pipeline_id":"pipeline_perf_windows","total":2,"failed":1,"skipped":0,"passed":1,"coverage_pct":78.0
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"FrameRateTest::SceneC",
                "status":"failed","duration_ms":1250
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"MemoryUsageTest::SceneC",
                "status":"passed","duration_ms":810
            }),
            Action(name="UpdateRunMetadata", kwargs={
                "run_id":"run_001",
                "metadata_patch":{"evidence_test_run":"AUTO::test_run::pipeline_perf_windows::175","linked_artifact":"build_002"}
            }),
            Action(name="PersistOwnerToRun", kwargs={
                "run_id":"run_001","owner_id":"user_001","owner_path":"src/game/engine/renderer.cpp",
                "ownership_type":"file_owner","confidence_score":0.9
            }),
            Action(name="AppendSimilarIncidentToRun", kwargs={
                "run_id":"run_001","incident_run_id":"run_006","similarity_score":0.88
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type":"build_triage","input_ref":"run_001",
                "automation_run_id":"AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_001","triage_status":"in_progress"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_001","step_id":"triage_fetch_artifacts","name":"triage_fetch_artifacts","status":"completed"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_001","step_id":"owner_resolution","name":"owner_resolution","status":"completed"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_001::canonical","status":"completed",
                "outputs_json":{
                    "triage_status":"in_progress","artifact_id":"build_002",
                    "owner_id":"user_001","owner_path":"src/game/engine/renderer.cpp",
                    "evidence_test_run":"AUTO::test_run::pipeline_perf_windows::175"
                }
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_001"})
        ],
        outputs=[
            "Repro preserved; symbolication attached; build_002 linked (hotfix_candidate=true, perf_baseline=2025-03); "
            "evidence test run AUTO::test_run::pipeline_perf_windows::175 recorded with 2 results (coverage_pct=78.0); "
            "ownership persisted (user_001 for src/game/engine/renderer.cpp, confidence=0.9); similar incident run_006 (0.88) noted; "
            "provenance steps completed; triage_status=in_progress; run metadata updated; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_046",
        instruction=(
            "Coordinate the publication of a deterministic unit‑test snapshot, associating it with triage on 'run_002'. Upon completion, ensure the system includes a test run identified by 'AUTO::test_run::pipeline_unit_tests::001' within 'pipeline_unit_tests', with computed totals of total=2, failed=1, skipped=0, passed=1 and coverage_pct=85.5; ensures exactly two results are in place—'PhysicsUnitTest::VectorMath' passed (75) and 'PhysicsUnitTest::Collision' failed (210). Ensure the build run 'run_002' displays triage_status 'in_progress' under the finalized canonical automation 'AUTO::automation::build_triage::run_002::canonical' with outputs including test_run_id 'AUTO::test_run::pipeline_unit_tests::001', and that run metadata stores unit_test_run_id='AUTO::test_run::pipeline_unit_tests::001'. Provide updated details for 'run_002'. Employ only these identifiers and values."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={"pipeline_id":"pipeline_unit_tests","total":2,"failed":1,"skipped":0,"passed":1,"coverage_pct":85.5}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_unit_tests::001","test_name":"PhysicsUnitTest::VectorMath","status":"passed","duration_ms":75}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_unit_tests::001","test_name":"PhysicsUnitTest::Collision","status":"failed","duration_ms":210}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_002","automation_run_id":"AUTO::automation::build_triage::run_002::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_002","triage_status":"in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_002::canonical","status":"completed","outputs_json":{"triage_status":"in_progress","test_run_id":"AUTO::test_run::pipeline_unit_tests::001"}}),
            Action(name="AddRunStep", kwargs={"run_id":"run_002","step_id":"unit_test_evidence_ingest","name":"unit_test_evidence_ingest","status":"completed"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id":"run_002","metadata_patch":{"unit_test_run_id":"AUTO::test_run::pipeline_unit_tests::001"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_002"})
        ],
        outputs=[
            "Unit test run AUTO::test_run::pipeline_unit_tests::001 recorded with 2 results (85.5%); run_002 triage_status=in_progress; evidence ingested; metadata linked; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_047",
        instruction=(
            "Advance the performance investigation for 'run_007'. Once finished, the incident context should include a single reference similar to 'run_008' with a similarity_score of 0.92; this run is associated with artifact 'build_002' (also labeled hotfix_candidate=true) and the run metadata logs artifact_id 'build_002'; triage_status remains 'in_progress' with the main automation 'AUTO::automation::build_triage::run_007::canonical' completed, recording that status and artifact. Return updated details for 'run_007'. Rely solely on these identifiers and values."
        ),
        actions=[
            Action(name="AppendSimilarIncidentToRun", kwargs={"run_id":"run_007","incident_run_id":"run_008","similarity_score":0.92}),
            Action(name="LinkArtifactToRun", kwargs={"run_id":"run_007","artifact_id":"build_002"}),
            Action(name="UpdateArtifactMetadata", kwargs={"artifact_id":"build_002","metadata_patch":{"hotfix_candidate":True}}),
            Action(name="UpdateRunMetadata", kwargs={"run_id":"run_007","metadata_patch":{"artifact_id":"build_002"}}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"triage_status":"in_progress","artifact_id":"build_002"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "Similar incident run_008 (0.92) recorded; build_002 linked and hotfix_candidate=true; run_007 triage_status=in_progress; artifact_id persisted; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_048",
        instruction=(
            "Ensure stability of the CI context for 'run_007' with verified evidence and clear ownership. Upon completion, connect the failed-test evidence from 'test_run_002' (run metadata logs evidence_test_run='test_run_002'); access symbolication for 'GameEngine.dll' from 'build_001' on 'windows'; maintain the repro command 'make performance-test-windows'; resolve and permanently set ownership as owner_id 'user_001' with the owner_path 'src/game/engine/renderer.cpp'; and triage_status changes to 'manual_review' with the main automation 'AUTO::automation::build_triage::run_007::canonical' completed, capturing that context. Return updated details for 'run_007'. Rely solely on these identifiers and values."
        ),
        actions=[
            Action(name="ListFailedTestsForRun", kwargs={"test_run_id":"test_run_002"}),
            Action(name="MapPathToOwner", kwargs={"file_path":"src/game/engine/renderer.cpp"}),
            Action(name="PersistOwnerToRun", kwargs={"run_id":"run_007","owner_id":"user_001","owner_path":"src/game/engine/renderer.cpp"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id":"run_007","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id":"run_007","command":"make performance-test-windows"}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_007","triage_status":"manual_review"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id":"run_007","metadata_patch":{"evidence_test_run":"test_run_002"}}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"triage_status":"manual_review","owner_id":"user_001","owner_path":"src/game/engine/renderer.cpp","evidence_test_run":"test_run_002"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "Evidence test_run_002 persisted; symbolication attached; repro preserved; ownership persisted (user_001 for src/game/engine/renderer.cpp); triage_status=manual_review captured; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_049",
        instruction=(
            "Ensure and save the code ownership for 'src/game/network/multiplayer.cpp' within the triage record of 'run_005'. Upon finalization, the run’s metadata reflects owner_id 'user_008' and owner_path 'src/game/network/multiplayer.cpp', with triage_status as 'manual_review' after the canonical automation 'AUTO::automation::build_triage::run_005::canonical' has completed recording that status. Provide the updated details for 'run_005'."
        ),
        actions=[
        Action(name="MapPathToOwner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
        Action(name="UpdateRunMetadata", kwargs={"run_id": "run_005", "metadata_patch": {"owner_id": "user_008", "owner_path": "src/game/network/multiplayer.cpp"}}),
        Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
        Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
        Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "owner_id": "user_008", "owner_path": "src/game/network/multiplayer.cpp"}}),
        Action(name="GetBuildRunDetails", kwargs={"run_id": "run_005"})
        ],
        outputs=[
        "Ownership persisted (user_008 for src/game/network/multiplayer.cpp); triage_status=manual_review recorded; run_005 details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_050",
        instruction=(
            "Standardize diagnostics for 'run_003' according to a consistent classification snapshot. Once done, the run includes metadata.failure_category recorded as {category:'compilation_issue'}; attaches Windows symbolication for 'GameEngine.dll' from 'build_001'; metadata.component='render_core'; and triage_status='in_progress', completed under the canonical automation 'AUTO::automation::build_triage::run_003::canonical' with outputs containing triage_status 'in_progress'. Supply the updated details for 'run_003'. Utilize only these identifiers and values."
        ),
        actions=[
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_003","automation_run_id":"AUTO::automation::build_triage::run_003::canonical"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id":"run_003","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id":"run_003","metadata_patch":{"component":"render_core"}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_003","triage_status":"in_progress"}),
            Action(name="SetBuildFailureCategorization", kwargs={"run_id":"run_003","category":"compilation_issue"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_003::canonical","status":"completed","outputs_json":{"triage_status":"in_progress"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_003"})
        ],
        outputs=[
            "run_003: metadata.failure_category stored as {category:'compilation_issue'}; symbolication attached; metadata.component=render_core; triage_status=in_progress captured via automation; details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_051",
        instruction=(
            "Handle the creation of a defensible triage record for build run 'run_005'. Once finalized, the run encompasses Windows symbolication for 'GameEngine.dll' from 'build_001', includes the reproducible command 'make test-integration-linux', presents triage_status 'manual_review', and completes the canonical automation 'AUTO::automation::build_triage::run_005::canonical' with outputs featuring failure_categorization 'integration_failure'. Refresh and return updated details for 'run_005'. Adhere strictly to these identifiers and values."
        ),
        actions=[
        Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_005", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
        Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_005", "command": "make test-integration-linux"}),
        Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
        Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
        Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "failure_categorization": "integration_failure"}}),
        Action(name="GetBuildRunDetails", kwargs={"run_id": "run_005"})
        ],
        outputs=[
        "run_005 symbolicated for GameEngine.dll; repro recorded; triage_status=manual_review; automation outputs include failure_categorization=integration_failure; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_052",
        instruction=(
            "Coordinate the capture and preservation of regression evidence on 'run_001' in a triage-ready, auditable format. Upon completion, the canonical automation 'AUTO::automation::build_triage::run_001::canonical' is finalized with outputs showing first_bad_commit 'abc999888777666', bisect_result 'commit_abc999', and triage_status 'in_progress'; the run includes Windows symbolication for 'GameEngine.dll' from 'build_001' and logs the reproducible command 'make test-windows-x64'. Update and provide refreshed details for 'run_001'. Use solely these identifiers and values."
        ),
        actions=[
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_001", "command": "make test-windows-x64"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "first_bad_commit": "abc999888777666", "bisect_result": "commit_abc999"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Regression evidence captured for run_001 (symbolication + repro). Automation outputs: first_bad_commit=abc999888777666, bisect_result=commit_abc999, triage_status=in_progress. Final run_001 details still show first_bad_commit=abc123def456789 and bisect_result=commit_abc123; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_053",
        instruction=(
            "Handle clear quality indicators for 'run_007' and maintain an audit trail. Upon completion, metadata contains at least {'priority':'high','platform_hint':'linux'}, a related incident references 'run_006' with similarity_score 0.90, provenance indicates a completed step 'signals_ingested', and triage shows 'manual_review' with the canonical automation finalized. Utilize only these identifiers and values."
        ),
        actions=[
            Action(name="UpdateRunMetadata", kwargs={"run_id":"run_007","metadata_patch":{"priority":"high","platform_hint":"linux"}}),
            Action(name="AppendSimilarIncidentToRun", kwargs={"run_id":"run_007","incident_run_id":"run_006","similarity_score":0.90}),
            Action(name="AddRunStep", kwargs={"run_id":"run_007","step_id":"signals_ingested","name":"signals_ingested","status":"completed"}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_007","triage_status":"manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"triage_status":"manual_review"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_007"})
        ],
        outputs=["Signals present; similar incident run_006 (0.90); provenance step signals_ingested=completed; triage_status=manual_review; details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_054",
        instruction=(
            "Execute publication of a Windows performance snapshot and connect it to triage. By the end, the fixed test run id is 'AUTO::test_run::pipeline_perf_windows::175' for pipeline 'pipeline_perf_windows' with totals total=3, failed=0, skipped=0, passed=3, coverage_pct=92.4 and precisely these results—'FrameRateTest::SceneC' passed (duration_ms=1100), 'MemoryUsageTest::SceneC' passed (700), 'LoadTimeTest::SceneC' passed (450); artifact 'build_001' metadata indicates perf_baseline='2025-02' and regression_flag=false; and the canonical automation 'AUTO::automation::build_triage::run_007::canonical' is concluded with outputs containing triage_status 'in_progress' and test_run_id 'AUTO::test_run::pipeline_perf_windows::175'. You provide updated details for 'run_007'. Use solely these identifiers and values."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={"pipeline_id": "pipeline_perf_windows", "total": 3, "failed": 0, "skipped": 0, "passed": 3, "coverage_pct": 92.4}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "FrameRateTest::SceneC", "status": "passed", "duration_ms": 1100}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "MemoryUsageTest::SceneC", "status": "passed", "duration_ms": 700}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "LoadTimeTest::SceneC", "status": "passed", "duration_ms": 450}),
            Action(name="UpdateArtifactMetadata", kwargs={"artifact_id": "build_001", "metadata_patch": {"perf_baseline": "2025-02", "regression_flag": False}}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_007", "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_007::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_007"})
        ],
        outputs=[
            "Perf snapshot recorded for AUTO::test_run::pipeline_perf_windows::175; build_001 patched. Automation outputs include triage_status=in_progress and test_run_id=AUTO::test_run::pipeline_perf_windows::175; final run_007 details show triage_status=manual_review; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_055",
        instruction=(
            "Ensure catalog context for the UI texture is verified and stored with reproducibility and traceability in the triage phase. Upon completion, register 'assets/textures/ui/main_menu_bg.png' as a 'texture' asset named 'main_menu_bg'; confirm a QA result exists with validation_status 'passed', severity_max 'info', autofix_applied false; record its catalog performance_rating as 'medium'; log the build run 'run_006' containing the repro command 'scripts/validate_texture.sh --asset assets/textures/ui/main_menu_bg.png', include Windows symbolication for 'GameEngine.dll' from 'build_001', and note that the steps 'asset_validation' and 'context_indexed' are completed in the provenance, while triage reflects 'manual_review' within the finished canonical automation 'AUTO::automation::build_triage::run_006::canonical'; and ensure run metadata contains last_validated_asset='assets/textures/ui/main_menu_bg.png'. Provide updated details for 'run_006'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="RegisterAssetInCatalog", kwargs={
                "asset_path":"assets/textures/ui/main_menu_bg.png","asset_type":"texture","asset_name":"main_menu_bg"
            }),
            Action(name="CreateAssetQaResult", kwargs={
                "asset_path":"assets/textures/ui/main_menu_bg.png","asset_type":"texture",
                "validation_status":"passed","severity_max":"info","autofix_applied":False
            }),
            Action(name="UpdateAssetCatalogPerformanceRating", kwargs={
                "asset_path":"assets/textures/ui/main_menu_bg.png","performance_rating":"medium"
            }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id":"run_006","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"
            }),
            Action(name="RecordReproCommandForRun", kwargs={
                "run_id":"run_006","command":"scripts/validate_texture.sh --asset assets/textures/ui/main_menu_bg.png"
            }),
            Action(name="AddRunStep", kwargs={"run_id":"run_006","step_id":"asset_validation","name":"asset_validation","status":"completed"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_006","step_id":"context_indexed","name":"context_indexed","status":"completed"}),
            Action(name="StartAutomationRun", kwargs={
                "automation_type":"build_triage","input_ref":"run_006",
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed",
                "outputs_json":{"triage_status":"manual_review"}
            }),
            Action(name="UpdateRunMetadata", kwargs={
                "run_id":"run_006","metadata_patch":{"last_validated_asset":"assets/textures/ui/main_menu_bg.png"}
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_006"})
        ],
        outputs=[
            "UI texture validated and cataloged; rating=medium; repro recorded; symbolication attached; "
            "provenance steps completed; triage_status=manual_review; metadata updated; run_006 details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_056",
        instruction=(
            "Compile an auditable triage report for 'run_001' covering reproducibility, ownership, and artifact context. When finished, maintain the reproducible command 'make build-linux-x64'; attach Windows symbolication for 'GameEngine.dll' from 'build_001'; preserve ownership as owner_id 'user_008' (team 'team_003'), ownership_type 'file_owner', confidence_score 0.91 with owner_path 'src/game/network/multiplayer.cpp'; associate artifact 'build_002' and note in its metadata that hotfix_candidate=true; refer to a similar incident using 'run_006' with similarity_score 0.88; document completed steps 'triage_fetch_artifacts' and 'owner_resolution' in the provenance; and reflect triage_status 'in_progress' under the concluded canonical build_triage automation 'AUTO::automation::build_triage::run_001::canonical', whose outputs include triage_status 'in_progress', owner_id 'user_008', owner_path 'src/game/network/multiplayer.cpp', and artifact_id 'build_002'. Provide updated details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_001","automation_run_id":"AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id":"run_001","command":"make build-linux-x64"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id":"run_001","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),

            Action(name="PersistOwnerToRun", kwargs={"run_id":"run_001","owner_id":"user_008","team_id":"team_003","owner_path":"src/game/network/multiplayer.cpp","ownership_type":"file_owner","confidence_score":0.91}),
            Action(name="LinkArtifactToRun", kwargs={"run_id":"run_001","artifact_id":"build_002"}),
            Action(name="UpdateArtifactMetadata", kwargs={"artifact_id":"build_002","metadata_patch":{"hotfix_candidate":True}}),

            Action(name="AppendSimilarIncidentToRun", kwargs={"run_id":"run_001","incident_run_id":"run_006","similarity_score":0.88}),
            Action(name="AddRunStep", kwargs={"run_id":"run_001","step_id":"triage_fetch_artifacts","name":"triage_fetch_artifacts","status":"completed"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_001","step_id":"owner_resolution","name":"owner_resolution","status":"completed"}),

            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_001","triage_status":"in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_001::canonical","status":"completed","outputs_json":{"triage_status":"in_progress","owner_id":"user_008","owner_path":"src/game/network/multiplayer.cpp","artifact_id":"build_002"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_001"})
        ],
        outputs=[
            "run_001 triage_status=in_progress; repro preserved; symbolication attached; ownership persisted (user_008, team_003, file_owner, 0.91) with owner_path src/game/network/multiplayer.cpp; build_002 linked (hotfix_candidate=true); similar incident run_006 (0.88); steps triage_fetch_artifacts and owner_resolution completed.",
            "Automation AUTO::automation::build_triage::run_001::canonical completed with outputs (triage_status=in_progress, owner_id=user_008, owner_path=src/game/network/multiplayer.cpp, artifact_id=build_002); details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_057",
        instruction=(
            "Complete a deterministic performance record and make it visible in build triage for 'run_007'. Upon completion, the finalized test run 'AUTO::test_run::pipeline_perf_windows::175' (pipeline 'pipeline_perf_windows') annotates totals total=3, failed=1, skipped=0, passed=2, coverage_pct beginning at 0.0 and then adjusted to 0.72, with these specific outcomes—'FrameRateTest::SceneA' failed (1200), 'MemoryUsageTest::SceneA' passed (800), 'LoadTimeTest::SceneA' passed (500); triage reflects 'in_progress' under the completed canonical automation 'AUTO::automation::build_triage::run_007::canonical' with outputs including test_run_id 'AUTO::test_run::pipeline_perf_windows::175' and final_coverage_pct 0.72; and provenance indicates 'perf_results_appended' completed. Provide updated details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={
                "pipeline_id":"pipeline_perf_windows","total":3,"failed":1,"skipped":0,"passed":2,"coverage_pct":0.0
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"FrameRateTest::SceneA",
                "status":"failed","duration_ms":1200
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"MemoryUsageTest::SceneA",
                "status":"passed","duration_ms":800
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"LoadTimeTest::SceneA",
                "status":"passed","duration_ms":500
            }),
            Action(name="UpdateTestRunCoverage", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175","coverage_pct":0.72
            }),
            Action(name="AddRunStep", kwargs={
                "run_id":"run_007","step_id":"perf_results_appended","name":"perf_results_appended","status":"completed"
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type":"build_triage","input_ref":"run_007",
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed",
                "outputs_json":{"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","final_coverage_pct":0.72}
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "Perf results recorded and coverage=0.72; provenance step completed; triage_status=in_progress; automation outputs captured; run_007 details retrieved."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_058",
        instruction=(
            "Conduct a multi-stage triage for 'run_007' aligned with CI failure workflows. By the conclusion, the run is labeled 'performance_regression', first_bad_commit is 'abc123def456789' with bisect data (first_bad_commit 'abc123def456789', last_good_commit 'commit_prev111', confidence 0.97), the repro command 'make performance-test-windows' is maintained, Windows symbolication for 'GameEngine.dll' from 'build_001' is included, provenance indicates completed steps 'log_ingested' and 'bisect_queued', and triage reflects 'in_progress' under the completed canonical automation 'AUTO::automation::build_triage::run_007::canonical'."
        ),
        actions=[
            Action(name="SetBuildFailureCategorization", kwargs={"run_id":"run_007","category":"performance_regression"}),
            Action(name="SetFirstBadCommitOnRun", kwargs={"run_id":"run_007","commit_sha":"abc123def456789"}),
            Action(name="SetBisectResultOnRun", kwargs={
                "run_id":"run_007","first_bad_commit_sha":"abc123def456789",
                "last_good_commit_sha":"commit_prev111","confidence":0.97
            }),
            Action(name="RecordReproCommandForRun", kwargs={"run_id":"run_007","command":"make performance-test-windows"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id":"run_007","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_007","step_id":"log_ingested","name":"log_ingested","status":"completed"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_007","step_id":"bisect_queued","name":"bisect_queued","status":"completed"}),
            Action(name="StartAutomationRun", kwargs={
                "automation_type":"build_triage","input_ref":"run_007",
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical"
            }),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical",
                "status":"completed","outputs_json":{"triage_status":"in_progress"}
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "Categorized performance_regression; first_bad & bisect recorded; repro & symbolication present; provenance logged; triage_status=in_progress; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_059",
        instruction=(
            "Handle the availability of symbolication and a targeted fix proposal for 'run_006' while maintaining traceability. Once complete, ensure the run includes Windows symbolication for 'GameEngine.dll' from 'build_001', with fix_proposal_id as 'fix_021', run metadata containing {'regression': 'frame_time_spike'}, triage_status remaining 'in_progress', and the canonical automation 'AUTO::automation::build_triage::run_006::canonical' confirming that status. Provide updated details for 'run_006'. Use strictly these identifiers and values."
        ),
        actions=[
        Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_006", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
        Action(name="SetFixProposalOnRun", kwargs={"run_id": "run_006", "fix_proposal_id": "fix_021"}),
        Action(name="UpdateRunMetadata", kwargs={"run_id": "run_006", "metadata_patch": {"regression": "frame_time_spike"}}),
        Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_006", "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"}),
        Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_006", "triage_status": "in_progress"}),
        Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_006::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
        Action(name="GetBuildRunDetails", kwargs={"run_id": "run_006"})
        ],
        outputs=["Symbolication linked; fix proposal fix_021 recorded; metadata patched; triage_status=in_progress; run_006 details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_060",
        instruction=(
            "Coordinate the publication of a Linux performance record with a set id and link it to triage for 'run_006'. Upon finalization, 'AUTO::test_run::pipeline_perf_linux::001' (part of pipeline 'pipeline_perf_linux') logs totals total=3, failed=1, skipped=0, passed=2 with precisely three outcomes—'FrameRateTest::SceneA' failed (1250), 'MemoryUsageTest::SceneA' passed (780), 'LoadTimeTest::SceneA' passed (480); the artifact 'build_001' notes perf_baseline '2025-03'; run_006 metadata keeps the performance_test_run_id 'AUTO::test_run::pipeline_perf_linux::001'; provenance on run_006 confirms 'evidence_ingested' has been completed."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={
                "pipeline_id":"pipeline_perf_linux","total":3,"failed":1,"skipped":0,"passed":2
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_linux::001","test_name":"FrameRateTest::SceneA",
                "status":"failed","duration_ms":1250
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_linux::001","test_name":"MemoryUsageTest::SceneA",
                "status":"passed","duration_ms":780
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_linux::001","test_name":"LoadTimeTest::SceneA",
                "status":"passed","duration_ms":480
            }),
            Action(name="UpdateArtifactMetadata", kwargs={
                "artifact_id":"build_001","metadata_patch":{"perf_baseline":"2025-03"}
            }),
            Action(name="UpdateRunMetadata", kwargs={
                "run_id":"run_006","metadata_patch":{"performance_test_run_id":"AUTO::test_run::pipeline_perf_linux::001"}
            }),
            Action(name="AddRunStep", kwargs={
                "run_id":"run_006","step_id":"evidence_ingested","name":"evidence_ingested","status":"completed"
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_006"})
        ],
        outputs=[
            "Linux perf run recorded; build_001 baseline set; run_006 metadata linked (performance_test_run_id) and evidence_ingested=completed; details retrieved."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_061",
        instruction=(
            "Handle an auditable triage snapshot for 'run_001'. Once finished, the run should display metadata priority='medium', first_bad_commit 'abc123def456789', and bisect_result 'commit_abc123'; triage_status is 'in_progress' monitored under the canonical automation 'AUTO::automation::build_triage::run_001::canonical'. Provide updated details for 'run_001'."
        ),
        actions=[
            Action(name="UpdateRunMetadata", kwargs={"run_id": "run_001", "metadata_patch": {"priority": "medium"}}),
            Action(name="SetFirstBadCommitOnRun", kwargs={"run_id": "run_001", "commit_sha": "abc123def456789"}),
            Action(name="SetBisectResultOnRun", kwargs={"run_id": "run_001", "bisect_result": "commit_abc123"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=["Run 'run_001' shows priority=medium, first_bad_commit=abc123def456789, bisect_result=commit_abc123, triage_status=in_progress (automation recorded)."]
    ),
    Task(
        annotator="0",
        user_id="qap_062",
        instruction=(
            "Coordinate stabilization of the CI context for 'run_001' ensuring owner accountability and reproducibility. Upon completion, failed test evidence from 'test_run_002' is referenced; include a symbolicated stack for 'GameEngine.dll' from 'build_001' on 'windows'; utilize the reproducible command 'make build-windows-x64'; maintain ownership for 'src/game/engine/renderer.cpp' as owner_id 'user_001'; and triage_status remains 'in_progress' documented under 'AUTO::automation::build_triage::run_001::canonical'. Provide updated details for 'run_001'."
        ),
        actions=[
            Action(name="ListFailedTestsForRun", kwargs={"test_run_id": "test_run_002"}),
            Action(name="MapPathToOwner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "owner_id": "user_001", "owner_path": "src/game/engine/renderer.cpp", "evidence_test_run": "test_run_002"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=["CI context stabilized for run_001: evidence linked, symbolication and repro present, owner persisted (user_001), triage_status=in_progress."]
    ),
    Task(
        annotator="0",
        user_id="qap_063",
        instruction=(
            "Verify and catalog the animation asset 'assets/animations/character/walk_cycle.fbx,' linking it to 'run_006.' Once finalized, the catalog includes the asset labeled 'Walk Cycle'; QA 'qa_004' is upgraded (resulting status passed with severity_max 'warning,' autofix_applied true); the catalog performance_rating is 'medium'; and the canonical build_triage automation 'AUTO::automation::build_triage::run_006::canonical' is finished with outputs referencing the asset and results. Provide updated details for 'run_006.' Use only these identifiers and values."
        ),
        actions=[
            Action(name="RegisterAssetInCatalog", kwargs={"asset_path":"assets/animations/character/walk_cycle.fbx","asset_type":"animation","asset_name":"Walk Cycle"}),
            Action(name="PromoteAssetAutofixToPass", kwargs={"qa_id":"qa_004"}),
            Action(name="UpdateAssetCatalogPerformanceRating", kwargs={"asset_path":"assets/animations/character/walk_cycle.fbx","performance_rating":"medium"}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_006","automation_run_id":"AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed","outputs_json":{"asset_path":"assets/animations/character/walk_cycle.fbx","validation_status":"passed","performance_rating":"medium"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_006"})
        ],
        outputs=[
            "Asset registered; qa_004 promoted; performance_rating=medium; automation outputs recorded; run_006 details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_064",
        instruction=(
            "Maintain the symbolication and triage context for 'run_001' within the canonical automation. Upon completion, symbolicated data for 'GameEngine.dll' from 'build_001' on 'windows' is linked to 'run_001'; triage_status remains 'in_progress' and the automation 'AUTO::automation::build_triage::run_001::canonical' is executed. Deliver refreshed details for 'run_001.'"
        ),
        actions=[
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=["Symbolication attached; triage_status=in_progress recorded and automation completed for run_001."]
    ),
    Task(
        annotator="0",
        user_id="qap_065",
        instruction=(
            "Connect the unit-test signals to triage for 'run_007'. Upon completion, the determined test run ID should be 'AUTO::test_run::pipeline_unit_tests::001' for the 'pipeline_unit_tests' pipeline, with a total count of total=2, failed=0, skipped=0, passed=2, and coverage_pct=76.2; the results include exactly two passing outcomes—'MathUnitTest::MatrixOps' (120) and 'IOUnitTest::FileRead' (95). Artifact metadata 'build_002' should reflect qa_baseline='2025-04' and test_suite='smoke'. The run should be designated with triage_status 'in_progress' under the completed canonical automation 'AUTO::automation::build_triage::run_007::canonical', and its outputs should indicate triage_status 'in_progress' and test_run_id 'AUTO::test_run::pipeline_unit_tests::001'. The run metadata must log unit_test_run_id='AUTO::test_run::pipeline_unit_tests::001', while showing provenance that 'unit_test_evidence_ingest' is completed. Provide updated details for 'run_007', adhering strictly to the given identifiers and values."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={
                "pipeline_id":"pipeline_unit_tests","total":2,"failed":0,"skipped":0,"passed":2,"coverage_pct":76.2
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_unit_tests::001","test_name":"MathUnitTest::MatrixOps",
                "status":"passed","duration_ms":120
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_unit_tests::001","test_name":"IOUnitTest::FileRead",
                "status":"passed","duration_ms":95
            }),
            Action(name="UpdateArtifactMetadata", kwargs={
                "artifact_id":"build_002","metadata_patch":{"qa_baseline":"2025-04","test_suite":"smoke"}
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type":"build_triage","input_ref":"run_007",
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed",
                "outputs_json":{"triage_status":"in_progress","test_run_id":"AUTO::test_run::pipeline_unit_tests::001"}
            }),
            Action(name="UpdateRunMetadata", kwargs={
                "run_id":"run_007","metadata_patch":{"unit_test_run_id":"AUTO::test_run::pipeline_unit_tests::001"}
            }),
            Action(name="AddRunStep", kwargs={
                "run_id":"run_007","step_id":"unit_test_evidence_ingest","name":"unit_test_evidence_ingest","status":"completed"
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "Unit-test run AUTO::test_run::pipeline_unit_tests::001 recorded; build_002 metadata patched; triage_status=in_progress; "
            "unit_test_run_id linked; provenance step completed; run_007 details retrieved."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_066",
        instruction=(
            "Create a deterministic performance snapshot and associate it with the triage context for 'run_001'. At the end, confirm that the canonical test run ID 'AUTO::test_run::pipeline_perf_windows::175' assigned to 'pipeline_perf_windows' represents a total of total=3, failed=1, skipped=0, passed=2 with specific results —'FrameRateTest::Hallway' failed (1300ms), 'MemoryUsageTest::Intro' passed (700ms), 'LoadTimeTest::MainMenu' passed (450ms), and coverage_pct=80.0. For 'run_001', ensure the metadata captures performance_test_run_id='AUTO::test_run::pipeline_perf_windows::175'. The canonical automation 'AUTO::automation::build_triage::run_001::canonical' should be completed with the outputs showing triage_status 'in_progress', test_run_id 'AUTO::test_run::pipeline_perf_windows::175', and final_coverage_pct 80.0. Provide updated details for 'run_001'."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={"pipeline_id": "pipeline_perf_windows", "total": 3, "failed": 1, "skipped": 0, "passed": 2, "coverage_pct": 0.0}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "FrameRateTest::Hallway", "status": "failed", "duration_ms": 1300}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "MemoryUsageTest::Intro", "status": "passed", "duration_ms": 700}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "LoadTimeTest::MainMenu", "status": "passed", "duration_ms": 450}),
            Action(name="UpdateTestRunCoverage", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "coverage_pct": 80.0}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "final_coverage_pct": 80.0}}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id": "run_001", "metadata_patch": {"performance_test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=["Perf snapshot bound to run_001 (test_run ::175 with 3 results, coverage=80.0); metadata linked; triage_status=in_progress; automation outputs captured; details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_067",
        instruction=(
            "Your task is to maintain a reproducible triage record for 'run_001'. Upon completion, the run shows the first_bad_commit 'abc123def456789', failure_categorization 'compilation_issue', and two completed steps—'collect-logs' (2025-01-27T10:16:00Z–2025-01-27T10:17:00Z) and 'summarize-failure' (2025-01-27T10:17:00Z–2025-01-27T10:18:00Z); the triage_status 'in_progress' is logged under 'AUTO::automation::build_triage::run_001::canonical'. Return the updated details for 'run_001'."
        ),
        actions=[
            Action(name="SetFirstBadCommitOnRun", kwargs={"run_id": "run_001", "commit_sha": "abc123def456789"}),
            Action(name="SetBuildFailureCategorization", kwargs={"run_id": "run_001", "category": "compilation_issue"}),
            Action(name="AddRunStep", kwargs={"run_id": "run_001", "step_id": "collect-logs", "name": "collect-logs", "status": "success", "started_at": "2025-01-27T10:16:00Z", "ended_at": "2025-01-27T10:17:00Z"}),
            Action(name="AddRunStep", kwargs={"run_id": "run_001", "step_id": "summarize-failure", "name": "summarize-failure", "status": "success", "started_at": "2025-01-27T10:17:00Z", "ended_at": "2025-01-27T10:18:00Z"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=["run_001 updated with first_bad_commit, categorization, steps recorded; triage_status=in_progress under canonical automation; details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_068",
        instruction=(
            "Take charge of making 'run_005' accountable and reproducible for a networking issue. Once completed, include failed-test evidence from 'test_run_002'; attach symbolication for 'GameEngine.dll' from 'build_001' on 'windows'; record the reproducible command 'make test-integration-linux'; maintain ownership for 'src/game/network/multiplayer.cpp' as owner_id 'user_008', team 'team_003', ownership_type 'file_owner', confidence_score 0.92; show provenance with a completed step 'owner_resolution'; and log triage_status as 'manual_review' under the finished canonical automation 'AUTO::automation::build_triage::run_005::canonical' which includes triage_status 'manual_review', owner_id 'user_008', owner_path 'src/game/network/multiplayer.cpp', and evidence_test_run 'test_run_002'. Ensure to return the refreshed details for 'run_005'. Use the given identifiers and values only."
        ),
        actions=[
            Action(name="ListFailedTestsForRun", kwargs={"test_run_id":"test_run_002"}),
            Action(name="MapPathToOwner", kwargs={"file_path":"src/game/network/multiplayer.cpp"}),
            Action(name="PersistOwnerToRun", kwargs={"run_id":"run_005","owner_id":"user_008","team_id":"team_003","ownership_type":"file_owner","confidence_score":0.92,"owner_path":"src/game/network/multiplayer.cpp"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id":"run_005","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id":"run_005","command":"make test-integration-linux"}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_005","automation_run_id":"AUTO::automation::build_triage::run_005::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_005","triage_status":"manual_review"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_005","step_id":"owner_resolution","name":"owner_resolution","status":"completed"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_005::canonical","status":"completed","outputs_json":{"triage_status":"manual_review","owner_id":"user_008","owner_path":"src/game/network/multiplayer.cpp","evidence_test_run":"test_run_002"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_005"})
        ],
        outputs=[
            "Ownership persisted to user_008 (team_003, file_owner, confidence=0.92); evidence test_run_002 noted; symbolication and repro recorded; triage_status=manual_review; owner_resolution=completed; automation outputs captured; run_005 details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_069",
        instruction=(
            "Handle symbol availability and manage triage linkage for Netcode. When finished, symbol info for module 'Netcode.dll' on 'windows' from 'build_004' will be registered with pdb_uri 'https://symbols.techcorp.com/build_004/Netcode.pdb' and status 'available'; symbol 'symbol_004' is considered deprecated; artifact 'build_004' is connected to 'run_006'; and triage_status 'in_progress' is documented under 'AUTO::automation::build_triage::run_006::canonical'. You provide updated details for 'run_006'."
        ),
        actions=[
            Action(name="RegisterSymbol", kwargs={"build_id": "build_004", "module_name": "Netcode.dll", "platform": "windows", "pdb_uri": "https://symbols.techcorp.com/build_004/Netcode.pdb", "status": "available"}),
            Action(name="DeprecateSymbol", kwargs={"symbol_id": "symbol_004"}),
            Action(name="LinkArtifactToRun", kwargs={"run_id": "run_006", "artifact_id": "build_004"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_006", "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_006", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_006::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_006"})
        ],
        outputs=["Symbol registered and prior symbol deprecated; build_004 linked; triage_status=in_progress recorded for run_006; details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_070",
        instruction=(
            "Address accountable ownership and ensure reproducibility for 'run_001'. Upon completion, 'src/game/ai/pathfinding.cpp' ownership remains with owner_id 'user_007'; the symbolicated stack for 'GameEngine.dll' from 'build_001' on 'windows' is affixed; the reproducible command 'make build-windows-x64' is logged; and triage_status is 'manual_review' monitored under 'AUTO::automation::build_triage::run_001::canonical'. You provide refreshed details for 'run_001'."
        ),
        actions=[
            Action(name="MapPathToOwner", kwargs={"file_path": "src/game/ai/pathfinding.cpp"}),
            Action(name="PersistOwnerToRun", kwargs={"run_id": "run_001", "owner_id": "user_007"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "owner_id": "user_007"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=["Owner persisted (user_007), symbolication and repro recorded; triage_status=manual_review under canonical automation; run_001 details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_071",
        instruction=(
            "Handle and document build run 'run_002' ensuring a reproducible and auditable record. By the end, 'run_002' includes Windows symbolication for 'GameEngine.dll' from 'build_001'; the run’s metadata.failure_category is 'compilation_issue' and metadata.first_bad_commit is 'abc123def456789'; the run shows triage_status as 'in_progress'; the canonical automation 'AUTO::automation::build_triage::run_002::canonical' finishes with outputs reflecting that state (failure_categorization 'compilation_issue', first_bad_commit 'abc123def456789', triage_status 'in_progress'); and provenance indicates a completed step 'triage_capture'. You provide updated details for 'run_002'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_002",
                "automation_run_id": "AUTO::automation::build_triage::run_002::canonical"
            }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id": "run_002",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="UpdateRunMetadata", kwargs={
                "run_id": "run_002",
                "metadata_patch": {
                    "failure_category": "compilation_issue",
                    "first_bad_commit": "abc123def456789"
                }
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_002", "triage_status": "in_progress"}),
            Action(name="AddRunStep", kwargs={"run_id": "run_002", "step_id": "triage_capture", "name": "triage_capture", "status": "completed"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_002::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "in_progress",
                    "failure_categorization": "compilation_issue",
                    "first_bad_commit": "abc123def456789"
                }
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_002"})
        ],
        outputs=[
            "run_002: symbolication attached; metadata.failure_category=compilation_issue; metadata.first_bad_commit=abc123def456789; triage_status=in_progress; step triage_capture=completed; automation recorded; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_072",
        instruction=(
            "Coordinate making build run 'run_003' owner-accountable with an auditable record. Upon completion, 'src/game/network/multiplayer.cpp' is resolved and recorded as owner_id 'user_008' on the run; the run indicates triage_status 'manual_review'; and the canonical automation 'AUTO::automation::build_triage::run_003::canonical' completes with outputs showing triage_status and owner_path. You provide updated details for 'run_003'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="MapPathToOwner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="PersistOwnerToRun", kwargs={"run_id": "run_003", "owner_id": "user_008", "owner_path": "src/game/network/multiplayer.cpp"}),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_003",
                "automation_run_id": "AUTO::automation::build_triage::run_003::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_003", "triage_status": "manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_003::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "manual_review", "owner_path": "src/game/network/multiplayer.cpp"}
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_003"})
        ],
        outputs=[
            "Ownership persisted to user_008 for src/game/network/multiplayer.cpp; triage_status=manual_review; automation completed; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_073",
        instruction=(
            "Create a triage-ready, evidence-rich record for 'run_006'. Upon completion, ensure the run logs 'python validate_assets.py', incorporates Windows symbolication for 'GameEngine.dll' from 'build_001', connects artifacts at 'https://artifacts.techcorp.com/build_004/', includes metadata {'validation_suite':'assets_fast'}, shows provenance steps 'log_ingested' and 'repro_verified', references a similar incident 'run_004' (similarity_score 0.83), and reports manual review in the completed canonical automation 'AUTO::automation::build_triage::run_006::canonical'."
        ),
        actions=[
            Action(name="RecordReproCommandForRun", kwargs={"run_id":"run_006","command":"python validate_assets.py"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id":"run_006","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="LinkArtifactToRun", kwargs={"run_id":"run_006","artifacts_uri":"https://artifacts.techcorp.com/build_004/"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id":"run_006","metadata_patch":{"validation_suite":"assets_fast"}}),
            Action(name="AppendSimilarIncidentToRun", kwargs={"run_id":"run_006","incident_run_id":"run_004","similarity_score":0.83}),
            Action(name="AddRunStep", kwargs={"run_id":"run_006","step_id":"log_ingested","name":"log_ingested","status":"completed"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_006","step_id":"repro_verified","name":"repro_verified","status":"completed"}),
            Action(name="StartAutomationRun", kwargs={
                "automation_type":"build_triage","input_ref":"run_006",
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical",
                "status":"completed","outputs_json":{"triage_status":"manual_review"}
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_006"})
        ],
        outputs=[
            "Repro, symbolication, artifacts, metadata, provenance, and incident context captured; triage_status=manual_review; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_074",
        instruction=(
            "Compile a deterministic performance report and append it to CI triage. Once finalized, 'AUTO::test_run::pipeline_perf_windows::175' for 'pipeline_perf_windows' logs totals total=3, failed=1, skipped=0, passed=2 with outcomes 'PhysicsStabilityTest::SceneB' failed (1400), 'AIPathfindingTest::SceneC' passed (900), 'LoadingScreenTest::SceneD' passed (600), and coverage 82.5. The triage for 'run_003' indicates triage_status 'in_progress' while the canonical automation has been completed with outputs that include performance_test_run_id 'AUTO::test_run::pipeline_perf_windows::175'; the run's metadata maintains this id."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={"pipeline_id":"pipeline_perf_windows","total":3,"failed":1,"skipped":0,"passed":2}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"PhysicsStabilityTest::SceneB","status":"failed","duration_ms":1400}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"AIPathfindingTest::SceneC","status":"passed","duration_ms":900}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"LoadingScreenTest::SceneD","status":"passed","duration_ms":600}),
            Action(name="UpdateTestRunCoverage", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","coverage_pct":82.5}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_003","automation_run_id":"AUTO::automation::build_triage::run_003::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_003","triage_status":"in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_003::canonical","status":"completed","outputs_json":{"triage_status":"in_progress","performance_test_run_id":"AUTO::test_run::pipeline_perf_windows::175","coverage_pct":82.5}}),
            Action(name="UpdateRunMetadata", kwargs={"run_id":"run_003","metadata_patch":{"performance_test_run_id":"AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_003"})
        ],
        outputs=["Perf run anchored to run_003 (coverage 82.5); triage_status=in_progress; automation completed; details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_075",
        instruction=(
            "Handle gating and incident context for 'run_001' with a clear audit trail. Once completed, ensure 'run_001' metadata reflects {'coverage_gate':'waived'}; metadata.similar_incidents contains precisely one entry for {'incident_run_id':'run_006'}; metadata.first_bad_commit is 'abc123def456789'; and the run indicates triage_status 'manual_review' within the completed canonical automation 'AUTO::automation::build_triage::run_001::canonical' (with outputs including triage_status 'manual_review' and first_bad_commit 'abc123def456789'). Provenance confirms a completed step 'triage_context'. Return updated details for 'run_001'. Stick to only these identifiers and values."
        ),
        actions=[
            Action(name="UpdateRunMetadata", kwargs={
                "run_id": "run_001",
                "metadata_patch": {
                    "coverage_gate": "waived",
                    "similar_incidents": [{"incident_run_id": "run_006"}],
                    "first_bad_commit": "abc123def456789"
                }
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "manual_review"}),
            Action(name="AddRunStep", kwargs={"run_id": "run_001", "step_id": "triage_context", "name": "triage_context", "status": "completed"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "manual_review",
                    "first_bad_commit": "abc123def456789",
                    "similar_incident": "run_006"
                }
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "run_001: metadata.coverage_gate=waived; metadata.similar_incidents includes run_006; metadata.first_bad_commit=abc123def456789; triage_status=manual_review; step triage_context=completed; automation recorded; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_076",
        instruction=(
            "Coordinate triage tracking for 'run_001' ensuring status and provenance are explicit. When completed, 'run_001' metadata should show priority 'high' and impact 'build_blocker'; provenance includes step 'triage_ownership' (2025-01-27T12:31:00Z–2025-01-27T12:33:00Z) with status 'success'; and triage_status is 'in_progress' under the completed canonical automation 'AUTO::automation::build_triage::run_001::canonical'. Return updated details for 'run_001'."
        ),
        actions=[
            Action(name="UpdateRunMetadata", kwargs={"run_id": "run_001", "metadata_patch": {"priority": "high", "impact": "build_blocker"}}),
            Action(name="AddRunStep", kwargs={"run_id": "run_001", "step_id": "triage_ownership", "name": "triage_ownership", "status": "success", "started_at": "2025-01-27T12:31:00Z", "ended_at": "2025-01-27T12:33:00Z"}),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "in_progress"}
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Run metadata updated (priority=high, impact=build_blocker); step triage_ownership recorded; triage_status=in_progress; automation completed; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_077",
        instruction=(
            "Handle the QA and catalog state of the texture so that it becomes auditable and connect it to CI triage with clear indicators. By the end, 'assets/textures/environment/hero_character_diffuse.png' must be cataloged as type 'texture' with asset_name 'hero_character_diffuse'; ensure a QA record exists with validation_status 'failed', severity_max 'issue', and autofix_applied true; the catalog's performance_rating is 'low'; build run 'run_006' should indicate triage_status 'manual_review' under the finalized canonical automation 'AUTO::automation::build_triage::run_006::canonical' whose outputs reference the asset_path and performance_rating; Windows symbolication for 'GameEngine.dll' from 'build_001' (windows) must be attached; ensure provenance shows 'asset_validation' completed. Return refreshed information for 'run_006'. Use solely these identifiers and values."
        ),
        actions=[
            Action(name="RegisterAssetInCatalog", kwargs={
                "asset_path":"assets/textures/environment/hero_character_diffuse.png","asset_type":"texture","asset_name":"hero_character_diffuse"
            }),
            Action(name="CreateAssetQaResult", kwargs={
                "asset_path":"assets/textures/environment/hero_character_diffuse.png","asset_type":"texture",
                "validation_status":"failed","severity_max":"issue","autofix_applied":True
            }),
            Action(name="UpdateAssetCatalogPerformanceRating", kwargs={
                "asset_path":"assets/textures/environment/hero_character_diffuse.png","performance_rating":"low"
            }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id":"run_006","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type":"build_triage","input_ref":"run_006",
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed",
                "outputs_json":{
                    "triage_status":"manual_review",
                    "asset_path":"assets/textures/environment/hero_character_diffuse.png","validation_status":"failed","performance_rating":"low"
                }
            }),
            Action(name="AddRunStep", kwargs={
                "run_id":"run_006","step_id":"asset_validation","name":"asset_validation","status":"completed"
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_006"})
        ],
        outputs=[
            "Texture cataloged; QA recorded (failed/issue, autofix_applied=true); rating=low; symbolication attached; "
            "triage_status=manual_review; provenance step completed; run_006 details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_078",
        instruction=(
            "Coordinate the finalization of a deterministic performance record and link it to triage. Upon completion, the fixed test run 'AUTO::test_run::pipeline_perf_windows::175' for 'pipeline_perf_windows' should record totals (total=3, failed=1, skipped=0, passed=2) with exactly three results—'FrameRateTest::MainCity' failed (1200), 'MemoryUsageTest::Raid' passed (800), and 'LoadTimeTest::Startup' passed (500)—and coverage 0.66. Build run 'run_001' should show triage_status 'in_progress' under the concluded canonical automation 'AUTO::automation::build_triage::run_001::canonical', whose outputs involve test_run_id and final_coverage_pct; the run metadata should contain performance_test_run_id 'AUTO::test_run::pipeline_perf_windows::175'. Return updated details for 'run_001'."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={"pipeline_id": "pipeline_perf_windows", "total": 3, "failed": 1, "skipped": 0, "passed": 2, "coverage_pct": 0.0}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "FrameRateTest::MainCity", "status": "failed", "duration_ms": 1200}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "MemoryUsageTest::Raid", "status": "passed", "duration_ms": 800}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "LoadTimeTest::Startup", "status": "passed", "duration_ms": 500}),
            Action(name="UpdateTestRunCoverage", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "coverage_pct": 0.66}),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "final_coverage_pct": 0.66, "triage_status": "in_progress"}
            }),
            Action(name="UpdateRunMetadata", kwargs={"run_id": "run_001", "metadata_patch": {"performance_test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Perf evidence recorded (coverage 0.66) and anchored to run_001; triage_status=in_progress; automation completed; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_079",
        instruction=(
            "Handle the stabilization of CI for 'run_001' with definitive ownership and reproducibility. Once completed, reference the failed-test evidence from 'test_run_002'; include Windows symbolication for 'GameEngine.dll' from 'build_001'; record the reproducible command 'make build-windows-x64'; map ownership for 'src/game/engine/renderer.cpp'; and ensure the run shows triage_status 'in_progress' under the finalized canonical automation 'AUTO::automation::build_triage::run_001::canonical' whose outputs encompass owner_path and evidence_test_run. Return refreshed details for 'run_001'."
        ),
        actions=[
            Action(name="ListFailedTestsForRun", kwargs={"test_run_id": "test_run_002"}),
            Action(name="MapPathToOwner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "in_progress", "owner_path": "src/game/engine/renderer.cpp", "evidence_test_run": "test_run_002"}
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Ownership mapped, symbolication attached, repro recorded; triage_status=in_progress; automation completed; details retrieved for run_001."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_080",
        instruction=(
            "Coordinate the stabilization of CI for 'run_007' with evidence that is reproducible and an ownership framework. Upon finishing, reference the failed-test evidence from 'test_run_002'; attach Windows symbolication for 'GameEngine.dll' from 'build_001'; document the reproducible command 'make performance-test-windows'; map ownership for 'src/game/engine/renderer.cpp'; and ensure the run reflects triage_status 'manual_review' under the completed canonical automation 'AUTO::automation::build_triage::run_007::canonical' with outputs including owner_path and evidence_test_run. Return updated details for 'run_007'."
        ),
        actions=[
            Action(name="ListFailedTestsForRun", kwargs={"test_run_id": "test_run_002"}),
            Action(name="MapPathToOwner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id": "run_007", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_007", "command": "make performance-test-windows"}),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_007",
                "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_007", "triage_status": "manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_007::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "manual_review", "owner_path": "src/game/engine/renderer.cpp", "evidence_test_run": "test_run_002"}
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_007"})
        ],
        outputs=[
            "Evidence and symbolication attached; repro recorded; triage_status=manual_review; automation completed; details retrieved for run_007."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_081",
        instruction=(
            "Handle a model-asset intake QA result and link it to CI triage for 'run_006'. Eventually, the model asset 'assets/models/environment/castle_tower.fbx' has a QA result (validation_status 'failed', severity_max 'issue', autofix_applied true), its catalog performance_rating remains 'high', and triage for 'run_006' indicates 'manual_review' with the canonical automation outputs reflecting that asset path/state."
        ),
        actions=[
            Action(name="CreateAssetQaResult", kwargs={"asset_path":"assets/models/environment/castle_tower.fbx","asset_type":"model","validation_status":"failed","severity_max":"issue","autofix_applied":True}),
            Action(name="UpdateAssetCatalogPerformanceRating", kwargs={"asset_path":"assets/models/environment/castle_tower.fbx","performance_rating":"high"}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_006","automation_run_id":"AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed","outputs_json":{"asset_path":"assets/models/environment/castle_tower.fbx","validation_status":"failed","performance_rating":"high"}})
        ],
        outputs=["Asset QA persisted; rating=high; run_006 triage_status=manual_review."]
    ),
    Task(
        annotator="0",
        user_id="qap_082",
        instruction=(
            "Coordinate a deterministic triage snapshot for 'run_005'. Once finished, Windows symbolication for 'GameEngine.dll' from 'build_001' is linked; the reproducible command 'make test-integration-linux' is documented; responsibility for 'src/game/network/multiplayer.cpp' is secured as owner_id 'user_008' with ownership_type 'file_owner', confidence_score 0.9, and owner_path 'src/game/network/multiplayer.cpp'; run metadata records evidence_test_run='test_run_002'; and triage_status is 'manual_review' under the finalized canonical build_triage automation 'AUTO::automation::build_triage::run_005::canonical' with outputs showing triage_status 'manual_review', owner_id 'user_008', owner_path 'src/game/network/multiplayer.cpp', and evidence_test_run 'test_run_002'. Deliver updated details for 'run_005'. Retain only these identifiers and values."
        ),
        actions=[
            Action(name="PersistOwnerToRun", kwargs={
                "run_id": "run_005",
                "owner_id": "user_008",
                "owner_path": "src/game/network/multiplayer.cpp",
                "ownership_type": "file_owner",
                "confidence_score": 0.9
            }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id": "run_005",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="RecordReproCommandForRun", kwargs={
                "run_id": "run_005",
                "command": "make test-integration-linux"
            }),
            Action(name="UpdateRunMetadata", kwargs={
                "run_id": "run_005",
                "metadata_patch": {"evidence_test_run": "test_run_002"}
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_005",
                "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_005::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "manual_review",
                    "owner_id": "user_008",
                    "owner_path": "src/game/network/multiplayer.cpp",
                    "evidence_test_run": "test_run_002"
                }
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_005"})
        ],
        outputs=[
            "Evidence test_run_002 noted; symbolication attached (windows, GameEngine.dll); repro preserved; owner persisted "
            "(user_008 for src/game/network/multiplayer.cpp, confidence=0.9); triage_status=manual_review captured; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_083",
        instruction=(
            "Handle the registration and quality gate of the texture, while linking its CI context to 'run_006'. Upon finalization, the catalog houses 'assets/textures/environment/castle_wall_diffuse.png' as typed 'texture' named 'Castle Wall Diffuse'; a QA record shows with validation_status 'passed', severity_max 'warning', autofix_applied true; the catalog’s performance_rating is 'medium'; and 'run_006' highlights triage_status 'manual_review' within the canonical build_triage automation 'AUTO::automation::build_triage::run_006::canonical'. Use only these specified identifiers and values."
        ),
        actions=[
            Action(name="RegisterAssetInCatalog", kwargs={
                "asset_path": "assets/textures/environment/castle_wall_diffuse.png",
                "asset_type": "texture",
                "asset_name": "Castle Wall Diffuse"
            }),
            Action(name="CreateAssetQaResult", kwargs={
                "asset_path": "assets/textures/environment/castle_wall_diffuse.png",
                "asset_type": "texture",
                "validation_status": "passed",
                "severity_max": "warning",
                "autofix_applied": True
            }),
            Action(name="UpdateAssetCatalogPerformanceRating", kwargs={
                "asset_path": "assets/textures/environment/castle_wall_diffuse.png",
                "performance_rating": "medium"
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_006",
                "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_006", "triage_status": "manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_006::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "manual_review"}
            })
        ],
        outputs=["Texture registered; QA recorded; performance_rating=medium; run_006 triage_status=manual_review."]
    ),
    Task(
        annotator="0",
        user_id="qap_084",
        instruction=(
            "Coordinate a deterministic performance report for 'pipeline_perf_windows' using the fixed test run id 'AUTO::test_run::pipeline_perf_windows::175'. Once completed, the totals are total=3, failed=1, skipped=0, passed=2 with coverage_pct=0.8; the run includes precisely three results—'PhysicsStabilityTest::SceneB' failed (1400), 'AIPathfindingTest::SceneC' passed (900), and 'LoadingScreenTest::SceneD' passed (600); 'run_007' indicates triage_status 'in_progress' under the canonical automation 'AUTO::automation::build_triage::run_007::canonical', which outputs {'test_run_id':'AUTO::test_run::pipeline_perf_windows::175','final_coverage_pct':0.8}; and run metadata retains performance_test_run_id 'AUTO::test_run::pipeline_perf_windows::175'. Deliver updated details for 'run_007'. Use only these specified identifiers and values."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={
                "pipeline_id": "pipeline_perf_windows",
                "total": 3, "failed": 1, "skipped": 0, "passed": 2, "coverage_pct": 0.8
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "PhysicsStabilityTest::SceneB",
                "status": "failed",
                "duration_ms": 1400
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "AIPathfindingTest::SceneC",
                "status": "passed",
                "duration_ms": 900
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "LoadingScreenTest::SceneD",
                "status": "passed",
                "duration_ms": 600
            }),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_007", "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_007", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_007::canonical",
                "status": "completed",
                "outputs_json": {
                    "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                    "final_coverage_pct": 0.8
                }
            }),
            Action(name="UpdateRunMetadata", kwargs={"run_id": "run_007", "metadata_patch": {"performance_test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_007"})
        ],
        outputs=[
            "Test run AUTO::test_run::pipeline_perf_windows::175 summary+results recorded; coverage=0.8; run_007 triage_status=in_progress; "
            "metadata linked; automation completed; details retrieved."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_085",
        instruction=(
            "Handle the stabilization of CI for 'run_001' by consolidating failed-test evidence, Windows symbolication, repro, and ownership, and manage the initiative under canonical automation. Upon completion, attach Windows symbolication for 'GameEngine.dll' from 'build_001'; record the reproducible command 'make build-windows-x64'; maintain ownership as owner_id 'user_001' for owner_path 'src/game/engine/renderer.cpp' with ownership_type 'file_owner' and confidence_score 0.9; store evidence_test_run 'test_run_002' in run metadata; and ensure 'run_001' reflects triage_status 'in_progress' under 'AUTO::automation::build_triage::run_001::canonical' with outputs comprising {'triage_status':'in_progress','owner_id':'user_001','owner_path':'src/game/engine/renderer.cpp','evidence_test_run':'test_run_002'}. Provide updated details for 'run_001'. Utilize only the specified identifiers and values."
        ),
        actions=[
            Action(name="ListFailedTestsForRun", kwargs={"test_run_id": "test_run_002"}),
            Action(name="PersistOwnerToRun", kwargs={
                "run_id": "run_001",
                "owner_id": "user_001",
                "owner_path": "src/game/engine/renderer.cpp",
                "ownership_type": "file_owner",
                "confidence_score": 0.9
            }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id": "run_001",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(name="UpdateRunMetadata", kwargs={"run_id": "run_001", "metadata_patch": {"evidence_test_run": "test_run_002"}}),
            Action(name="StartAutomationRun", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "in_progress",
                    "owner_id": "user_001",
                    "owner_path": "src/game/engine/renderer.cpp",
                    "evidence_test_run": "test_run_002"
                }
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Triage recorded: in_progress for run_001; evidence_test_run pinned; symbolication attached; repro preserved; "
            "owner persisted (user_001 for src/game/engine/renderer.cpp, confidence=0.9); details refreshed."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_086",
        instruction=(
            "Coordinate the extension of the deterministic performance suite and encapsulate triage context for 'run_007'. Upon finalization, ensure that exactly three results are added to 'AUTO::test_run::pipeline_perf_windows::175'—'ShaderCompileTest::BatchA' failed (2000), 'StreamingIOTest::SetA' passed (950), 'MemoryLeakDetection::Level1' passed (1100); categorize the run as 'performance_regression', log the repro command 'make performance-test-windows', include Windows symbolication for 'GameEngine.dll' from 'build_001', indicate that 'perf_results_appended' is completed in provenance, and reflect triage as 'in_progress' within the completed canonical automation 'AUTO::automation::build_triage::run_007::canonical' with outputs containing {'appended_test_results_count':3,'test_run_id':'AUTO::test_run::pipeline_perf_windows::175'}. Provide updated details for 'run_007'. Employ exclusively the listed identifiers and values."
        ),
        actions=[
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175",
                "test_name":"ShaderCompileTest::BatchA","status":"failed","duration_ms":2000
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175",
                "test_name":"StreamingIOTest::SetA","status":"passed","duration_ms":950
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175",
                "test_name":"MemoryLeakDetection::Level1","status":"passed","duration_ms":1100
            }),
            Action(name="RecordReproCommandForRun", kwargs={"run_id":"run_007","command":"make performance-test-windows"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id":"run_007","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"
            }),
            Action(name="SetBuildFailureCategorization", kwargs={"run_id":"run_007","category":"performance_regression"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_007","step_id":"perf_results_appended","name":"perf_results_appended","status":"completed"}),
            Action(name="StartAutomationRun", kwargs={
                "automation_type":"build_triage","input_ref":"run_007",
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed",
                "outputs_json":{"appended_test_results_count":3,"test_run_id":"AUTO::test_run::pipeline_perf_windows::175"}
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "3 results appended; categorized performance_regression; repro & symbolication present; provenance logged; "
            "triage_status=in_progress; automation outputs captured; run_007 details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_087",
        instruction=(
            "You handle the stabilization of CI for 'run_005' by capturing reproducibility, symbolication, and ownership, ensuring that an auditable trail is recorded. Upon completion, the Windows symbolication for 'GameEngine.dll' from 'build_001' is attached; the reproducible command 'make test-integration-linux' is documented; ownership is maintained with owner_id 'user_008' for owner_path 'src/game/network/multiplayer.cpp' with ownership_type 'file_owner' and confidence_score 0.9; run metadata pins evidence_test_run='test_run_002'; and triage_status is 'manual_review' under 'AUTO::automation::build_triage::run_005::canonical' whose outputs reflect that context. You return the refreshed details for 'run_005'."
        ),
        actions=[
            Action(name="PersistOwnerToRun", kwargs={
                "run_id": "run_005",
                "owner_id": "user_008",
                "owner_path": "src/game/network/multiplayer.cpp",
                "ownership_type": "file_owner",
                "confidence_score": 0.9
            }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id": "run_005",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="RecordReproCommandForRun", kwargs={
                "run_id": "run_005",
                "command": "make test-integration-linux"
            }),
            Action(name="UpdateRunMetadata", kwargs={
                "run_id": "run_005",
                "metadata_patch": {"evidence_test_run": "test_run_002"}
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_005",
                "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_005::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "manual_review",
                    "owner_id": "user_008",
                    "owner_path": "src/game/network/multiplayer.cpp",
                    "evidence_test_run": "test_run_002"
                }
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_005"})
        ],
        outputs=[
            "Triage recorded: manual_review; Windows symbolication attached; repro preserved; owner persisted; evidence pinned; details refreshed."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_088",
        instruction=(
            "You coordinate the documentation of triage execution on 'run_004' and record it under the canonical automation. After completion, provenance includes step 'symbolication_setup' (success, 2025-01-27T12:10:00Z→2025-01-27T12:12:00Z) and step 'owner_mapping' (success, 2025-01-27T12:12:00Z→2025-01-27T12:14:00Z); and 'run_004' reflects triage_status 'in_progress' under 'AUTO::automation::build_triage::run_004::canonical' whose outputs document the steps ['symbolication_setup','owner_mapping']."
        ),
        actions=[
            Action(name="AddRunStep", kwargs={
                "run_id": "run_004",
                "step_id": "symbolication_setup",
                "name": "symbolication_setup",
                "status": "success",
                "started_at": "2025-01-27T12:10:00Z",
                "ended_at": "2025-01-27T12:12:00Z"
            }),
            Action(name="AddRunStep", kwargs={
                "run_id": "run_004",
                "step_id": "owner_mapping",
                "name": "owner_mapping",
                "status": "success",
                "started_at": "2025-01-27T12:12:00Z",
                "ended_at": "2025-01-27T12:14:00Z"
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_004",
                "automation_run_id": "AUTO::automation::build_triage::run_004::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_004", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_004::canonical",
                "status": "completed",
                "outputs_json": {"documented_steps": ["symbolication_setup", "owner_mapping"]}
            })
        ],
        outputs=["Provenance steps recorded; run_004 triage_status=in_progress; automation captured documented_steps."]
    ),
    Task(
        annotator="0",
        user_id="qap_089",
        instruction=(
            "Handle the registration and quality-gate of the texture, linking its result to CI triage for 'run_006'. Upon completion, the catalog should list 'assets/textures/props/torch_fire_diffuse.png' as type 'texture' with the name 'Torch Fire Diffuse'; a QA record must show validation_status 'passed', severity_max 'warning', autofix_applied true; catalog performance_rating should be 'medium'; and 'run_006' needs to show triage_status 'manual_review' under 'AUTO::automation::build_triage::run_006::canonical'. Ensure use of only these identifiers and values."
        ),
        actions=[
            Action(name="RegisterAssetInCatalog", kwargs={
                "asset_path": "assets/textures/props/torch_fire_diffuse.png",
                "asset_type": "texture",
                "asset_name": "Torch Fire Diffuse"
            }),
            Action(name="CreateAssetQaResult", kwargs={
                "asset_path": "assets/textures/props/torch_fire_diffuse.png",
                "asset_type": "texture",
                "validation_status": "passed",
                "severity_max": "warning",
                "autofix_applied": True
            }),
            Action(name="UpdateAssetCatalogPerformanceRating", kwargs={
                "asset_path": "assets/textures/props/torch_fire_diffuse.png",
                "performance_rating": "medium"
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_006",
                "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_006", "triage_status": "manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_006::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "manual_review"}
            })
        ],
        outputs=["Texture registered; QA recorded; performance_rating=medium; run_006 triage_status=manual_review."]
    ),
    Task(
        annotator="0",
        user_id="qap_090",
        instruction=(
            "Coordinate the finalization of a deterministic performance report for 'pipeline_perf_windows' on the specific test run 'AUTO::test_run::pipeline_perf_windows::175'. Upon finishing, overall totals should be total=3, failed=1, skipped=0, passed=2 with coverage_pct=0.7; the run includes 'FrameRateTest::SceneA' failed (1200), 'MemoryUsageTest::SceneA' passed (800), and 'LoadTimeTest::SceneA' passed (500); 'run_001' must indicate triage_status 'in_progress' under 'AUTO::automation::build_triage::run_001::canonical', with outputs comprising {'test_run_id':'AUTO::test_run::pipeline_perf_windows::175','final_coverage_pct':0.7}; furthermore, run metadata should contain performance_test_run_id 'AUTO::test_run::pipeline_perf_windows::175'."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={
                "pipeline_id": "pipeline_perf_windows",
                "total": 3, "failed": 1, "skipped": 0, "passed": 2, "coverage_pct": 0.0
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "FrameRateTest::SceneA",
                "status": "failed",
                "duration_ms": 1200
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "MemoryUsageTest::SceneA",
                "status": "passed",
                "duration_ms": 800
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "LoadTimeTest::SceneA",
                "status": "passed",
                "duration_ms": 500
            }),
            Action(name="UpdateTestRunCoverage", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "coverage_pct": 0.7
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {
                    "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                    "final_coverage_pct": 0.7
                }
            }),
            Action(name="UpdateRunMetadata", kwargs={
                "run_id": "run_001",
                "metadata_patch": {"performance_test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}
            })
        ],
        outputs=[
            "Coverage updated to 0.7 for AUTO::test_run::pipeline_perf_windows::175; results recorded.",
            "run_001 triage_status=in_progress; metadata linked; automation completed."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_091",
        instruction=(
            "Manage the registration of two UI assets and reveal their CI context for 'run_006'. Upon completion, ensure the animation 'assets/animations/character/walk_cycle.fbx' is cataloged as asset_name 'Character Walk Cycle'; the texture 'assets/textures/ui/health_bar.png' is enlisted as asset_name 'Health Bar', with a QA record (validation_status 'passed', severity_max 'warning', autofix_applied true), and holds a catalog performance_rating of 'medium'; the standard build_triage automation 'AUTO::automation::build_triage::run_006::canonical' is finalized, rendering outputs with triage_status 'manual_review'; and the run shows a triage_status of 'manual_review'. Utilize only these identifiers and values."
        ),
        actions=[
            Action(name="RegisterAssetInCatalog", kwargs={"asset_path":"assets/animations/character/walk_cycle.fbx","asset_type":"animation","asset_name":"Character Walk Cycle"}),
            Action(name="RegisterAssetInCatalog", kwargs={"asset_path":"assets/textures/ui/health_bar.png","asset_type":"texture","asset_name":"Health Bar"}),
            Action(name="CreateAssetQaResult", kwargs={"asset_path":"assets/textures/ui/health_bar.png","asset_type":"texture","validation_status":"passed","severity_max":"warning","autofix_applied":True}),
            Action(name="UpdateAssetCatalogPerformanceRating", kwargs={"asset_path":"assets/textures/ui/health_bar.png","performance_rating":"medium"}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_006","automation_run_id":"AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed","outputs_json":{"triage_status":"manual_review"}}),
        ],
        outputs=[
            "Animation and texture registered; QA recorded; performance_rating=medium.",
            "Run run_006 triage_status=manual_review; automation completed"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_092",
        instruction=(
            "Coordinate the integration of symbol-awareness for 'run_001' and associate its evidence while monitoring it in triage. Upon concluding, register the Windows symbol for 'Renderer.dll' on build 'build_001' with pdb_uri 'https://symbols.techcorp.com/build_001/Renderer.pdb' (status 'available'); link artifacts at 'https://artifacts.techcorp.com/build_001/' to the run; and ensure triage shows 'in_progress' for the completed canonical automation 'AUTO::automation::build_triage::run_001::canonical'."
        ),
        actions=[
            Action(name="RegisterSymbol", kwargs={
                "build_id":"build_001","module_name":"Renderer.dll","platform":"windows",
                "pdb_uri":"https://symbols.techcorp.com/build_001/Renderer.pdb","status":"available"
            }),
            Action(name="LinkArtifactToRun", kwargs={
                "run_id":"run_001","artifacts_uri":"https://artifacts.techcorp.com/build_001/"
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type":"build_triage","input_ref":"run_001",
                "automation_run_id":"AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_001","triage_status":"in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_001::canonical",
                "status":"completed","outputs_json":{"triage_status":"in_progress"}
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_001"})
        ],
        outputs=[
            "Renderer symbols registered; artifacts linked; triage_status=in_progress; automation recorded; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_093",
        instruction=(
            "Handle the accountable ownership for a Linux integration issue on 'run_006'. Upon completion, the owner resolved from 'src/game/network/multiplayer.cpp' is saved to the run as owner_id 'user_008' with owner_path 'src/game/network/multiplayer.cpp'; the canonical automation 'AUTO::automation::build_triage::run_006::canonical' is finalized with outputs showing triage_status 'manual_review' and owner_path 'src/game/network/multiplayer.cpp'; and the run indicates triage_status 'manual_review'. Provide updated details for 'run_006'."
        ),
        actions=[
            Action(name="MapPathToOwner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="PersistOwnerToRun", kwargs={
                "run_id": "run_006",
                "owner_id": "user_008",
                "owner_path": "src/game/network/multiplayer.cpp"
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_006",
                "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_006", "triage_status": "manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_006::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "manual_review", "owner_path": "src/game/network/multiplayer.cpp"}
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_006"})
        ],
        outputs=[
            "Ownership for src/game/network/multiplayer.cpp persisted to user_008; triage_status=manual_review; automation completed; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_094",
        instruction=(
            "Coordinate the stabilization of CI for 'run_007' by documenting reproducibility, symbolication, and ownership context. Upon completion, the run records 'make performance-test-windows'; symbolication for 'GameEngine.dll' from 'build_001' on 'windows' is included; ownership is documented as owner_id 'user_001' for owner_path 'src/game/engine/renderer.cpp'; the canonical automation 'AUTO::automation::build_triage::run_007::canonical' is concluded with outputs indicating triage_status 'manual_review', owner_id 'user_001', owner_path 'src/game/engine/renderer.cpp', and evidence_test_run 'test_run_002'; and the run shows triage_status 'manual_review'. Provide updated details for 'run_007'."
        ),
        actions=[
            Action(name="PersistOwnerToRun", kwargs={
                "run_id": "run_007",
                "owner_id": "user_001",
                "owner_path": "src/game/engine/renderer.cpp"
            }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id": "run_007",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_007", "command": "make performance-test-windows"}),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_007",
                "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_007", "triage_status": "manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_007::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "manual_review",
                    "owner_id": "user_001",
                    "owner_path": "src/game/engine/renderer.cpp",
                    "evidence_test_run": "test_run_002"
                }
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_007"})
        ],
        outputs=[
            "Repro recorded; symbolication attached; ownership persisted (user_001 for renderer.cpp); triage_status=manual_review; automation completed; details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_095",
        instruction=(
            "Handle a comprehensive texture QA ingest for 'assets/textures/environment/castle_gate_diffuse.png' into CI. By the end, the texture is registered as asset_name 'Castle Gate Diffuse', with QA details (validation_status 'failed', severity_max 'issue', autofix_applied true), catalog performance_rating 'low', and the canonical triage record for 'run_006' is finalized in 'manual_review' state, reflecting the asset's path/state."
        ),
        actions=[
            Action(name="RegisterAssetInCatalog", kwargs={"asset_path":"assets/textures/environment/castle_gate_diffuse.png","asset_type":"texture","asset_name":"Castle Gate Diffuse"}),
            Action(name="CreateAssetQaResult", kwargs={"asset_path":"assets/textures/environment/castle_gate_diffuse.png","asset_type":"texture","validation_status":"failed","severity_max":"issue","autofix_applied":True}),
            Action(name="UpdateAssetCatalogPerformanceRating", kwargs={"asset_path":"assets/textures/environment/castle_gate_diffuse.png","performance_rating":"low"}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_006","automation_run_id":"AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed","outputs_json":{"triage_status":"manual_review","asset_path":"assets/textures/environment/castle_gate_diffuse.png","validation_status":"failed","performance_rating":"low"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_006"})
        ],
        outputs=["Texture registered with QA; catalog rating=low; run_006 triage_status=manual_review captured; details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_096",
        instruction=(
            "Document a QA failure for 'assets/textures/environment/rock_albedo.png' and complete its catalog impact while managing triage for 'run_006'. Upon completion, the texture is listed as asset_name 'Rock Albedo'; a QA record is available with validation_status 'failed', severity_max 'issue', autofix_applied true; the catalog performance_rating is 'high'; the run provides the repro command 'scripts/qa_texture.sh --asset assets/textures/environment/rock_albedo.png', includes Windows symbolication for 'GameEngine.dll' from 'build_001', provenance covers completed steps 'asset_validation' and 'catalog_sync', and triage is noted as 'in_progress' under the completed canonical automation 'AUTO::automation::build_triage::run_006::canonical'. Provide updated details for 'run_006'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="RegisterAssetInCatalog", kwargs={
                "asset_path":"assets/textures/environment/rock_albedo.png","asset_type":"texture","asset_name":"Rock Albedo"
            }),
            Action(name="CreateAssetQaResult", kwargs={
                "asset_path":"assets/textures/environment/rock_albedo.png","asset_type":"texture",
                "validation_status":"failed","severity_max":"issue","autofix_applied":True
            }),
            Action(name="UpdateAssetCatalogPerformanceRating", kwargs={
                "asset_path":"assets/textures/environment/rock_albedo.png","performance_rating":"high"
            }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id":"run_006","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"
            }),
            Action(name="RecordReproCommandForRun", kwargs={
                "run_id":"run_006","command":"scripts/qa_texture.sh --asset assets/textures/environment/rock_albedo.png"
            }),
            Action(name="AddRunStep", kwargs={"run_id":"run_006","step_id":"asset_validation","name":"asset_validation","status":"completed"}),
            Action(name="AddRunStep", kwargs={"run_id":"run_006","step_id":"catalog_sync","name":"catalog_sync","status":"completed"}),
            Action(name="StartAutomationRun", kwargs={
                "automation_type":"build_triage","input_ref":"run_006",
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_006","triage_status":"in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical",
                "status":"completed","outputs_json":{"triage_status":"in_progress"}
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_006"})
        ],
        outputs=[
            "Rock Albedo registered; QA recorded; performance_rating=high; repro & symbolication recorded; "
            "provenance steps completed; triage_status=in_progress; run_006 details retrieved."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_097",
        instruction=(
            "Handle the stabilization of CI for 'run_001' by ensuring reproducibility, symbolication, and ownership evidence is captured. Upon completion, the run logs 'make build-windows-x64'; 'GameEngine.dll' symbolication from 'build_001' on 'windows' is included; run metadata locks evidence_test_run='test_run_002'; finalize the canonical automation 'AUTO::automation::build_triage::run_001::canonical' with outputs showing triage_status 'in_progress', owner_id 'user_001', owner_path 'src/game/engine/renderer.cpp', and evidence_test_run 'test_run_002'; the run status remains triage_status 'in_progress'. Retrieve updated details for 'run_001'."
        ),
        actions=[
            Action(name="MapPathToOwner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="UpdateRunMetadata", kwargs={
                "run_id": "run_001",
                "metadata_patch": {"evidence_test_run": "test_run_002"}
            }),
            Action(name="AttachSymbolicatedStackToRun", kwargs={
                "run_id": "run_001",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="RecordReproCommandForRun", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(name="StartAutomationRun", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "in_progress",
                    "owner_id": "user_001",
                    "owner_path": "src/game/engine/renderer.cpp",
                    "evidence_test_run": "test_run_002"
                }
            }),
            Action(name="GetBuildRunDetails", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Repro recorded; symbolication attached; evidence pinned; triage_status=in_progress with ownership context; automation completed; details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_098",
        instruction=(
            "Coordinate the consolidation of deterministic performance evidence for 'pipeline_perf_windows' and integrate it into build triage for 'run_001'. Upon finishing, the fixed test run 'AUTO::test_run::pipeline_perf_windows::175' holds exactly three results—'GPUDriverStability::NVScene' passed (700), 'DiskThroughputTest::SeqRead' passed (450), and 'ThreadingContention::AIJobs' failed (1600); coverage is revised to 0.66; wrap up the canonical build_triage automation 'AUTO::automation::build_triage::run_001::canonical' with outputs, including test_run_id 'AUTO::test_run::pipeline_perf_windows::175' and final_coverage_pct 0.66; the run maintains triage_status 'in_progress'. Employ only these identifiers and values."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={
                "pipeline_id": "pipeline_perf_windows",
                "total": 3, "failed": 1, "skipped": 0, "passed": 2, "coverage_pct": 0.66
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175",
                "test_name":"GPUDriverStability::NVScene","status":"passed","duration_ms":700
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175",
                "test_name":"DiskThroughputTest::SeqRead","status":"passed","duration_ms":450
            }),
            Action(name="AddTestResultToRun", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175",
                "test_name":"ThreadingContention::AIJobs","status":"failed","duration_ms":1600
            }),
            Action(name="UpdateTestRunCoverage", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175","coverage_pct":0.66
            }),
            Action(name="StartAutomationRun", kwargs={
                "automation_type":"build_triage","input_ref":"run_001",
                "automation_run_id":"AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="SetBuildTriageStatus", kwargs={
                "run_id":"run_001","triage_status":"in_progress"
            }),
            Action(name="CompleteAutomationRun", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_001::canonical",
                "status":"completed",
                "outputs_json":{"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","final_coverage_pct":0.66}
            }),
        ],
        outputs=[
            "3 deterministic results and coverage recorded for AUTO::test_run::pipeline_perf_windows::175; run_001 triage_status=in_progress."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_099",
        instruction=(
            "Manage code ownership for 'src/game/engine/renderer.cpp' on 'run_001' and present symbolication and triage status. Upon completion, the run maintains owner_id 'user_001' with owner_path 'src/game/engine/renderer.cpp'; Windows symbolication for 'GameEngine.dll' from 'build_001' is included; the standard build_triage automation 'AUTO::automation::build_triage::run_001::canonical' is concluded with outputs indicating triage_status 'manual_review' and owner_id 'user_001'; and the run displays triage_status 'manual_review'. Provide updated details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="PersistOwnerToRun", kwargs={"run_id":"run_001","owner_id":"user_001","owner_path":"src/game/engine/renderer.cpp"}),
            Action(name="AttachSymbolicatedStackToRun", kwargs={"run_id":"run_001","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_001","automation_run_id":"AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_001","triage_status":"manual_review"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_001::canonical","status":"completed","outputs_json":{"triage_status":"manual_review","owner_id":"user_001"}}),
            Action(name="GetBuildRunDetails", kwargs={"run_id":"run_001"}),
        ],
        outputs=[
            "Ownership persisted (owner_id=user_001, owner_path=src/game/engine/renderer.cpp); symbolication attached; triage complete; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_100",
        instruction=(
            "Complete a Windows performance snapshot and enable its actionability in triage for 'run_007'. Ultimately, 'AUTO::test_run::pipeline_perf_windows::175' records totals total=3, failed=1, skipped=0, passed=2 with precisely three results—'FrameRateTest::SceneA' failed (1200), 'MemoryUsageTest::SceneA' passed (800), 'LoadTimeTest::SceneA' passed (500)—and coverage is 0.78. Triage for 'run_007' indicates triage_status 'in_progress' with the canonical automation finalized, whose outputs comprise test_run_id 'AUTO::test_run::pipeline_perf_windows::175' and final_coverage_pct 0.78. Use only these identifiers and values."
        ),
        actions=[
            Action(name="CreateTestRunSummary", kwargs={"pipeline_id":"pipeline_perf_windows","total":3,"failed":1,"skipped":0,"passed":2}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"FrameRateTest::SceneA","status":"failed","duration_ms":1200}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"MemoryUsageTest::SceneA","status":"passed","duration_ms":800}),
            Action(name="AddTestResultToRun", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"LoadTimeTest::SceneA","status":"passed","duration_ms":500}),
            Action(name="UpdateTestRunCoverage", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","coverage_pct":0.78}),
            Action(name="StartAutomationRun", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="SetBuildTriageStatus", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="CompleteAutomationRun", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","final_coverage_pct":0.78}})
        ],
        outputs=["Test run totals/results recorded and coverage=0.78; run_007 triage_status=in_progress; automation completed."]
    ),
]
