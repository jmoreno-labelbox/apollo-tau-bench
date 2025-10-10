from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="qap_001",
        instruction=(
        "You are the Quality Engineer & Performance Specialist triaging a Windows compile failure in build run 'run_001' "
        "for repository 'game-engine'. Use deterministic actions to ensure symbolication for module 'GameEngine.dll' "
        "from build 'build_001' on platform 'windows', record the reproducible build command 'make build-windows-x64', "
        "resolve ownership for the failing source file 'src/game/engine/renderer.cpp' using the ownership map, and "
        "track the triage in an automation run whose key MUST be 'AUTO::automation::build_triage::run_001::canonical' "
        "and whose completion status is 'completed'. Set the run's triage status to 'in_progress'. Return the refreshed "
        "details of 'run_001'. All parameters you use must come from this instruction or previous results."
        ),
        actions=[
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"}),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id": "run_001",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="record_repro_command_for_run", kwargs={
                "run_id": "run_001",
                "command": "make build-windows-x64"
            }),
            Action(name="map_path_to_owner", kwargs={
                "file_path": "src/game/engine/renderer.cpp"
            }),
            Action(name="set_build_triage_status", kwargs={
                "run_id": "run_001",
                "triage_status": "in_progress"
            }),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "in_progress",
                    "symbolicated_stack_uri": "https://symbols.techcorp.com/build_001/GameEngine.pdb"
                }
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="qap_002",
        instruction=(
            "You are a Quality Engineer focused on asset validation. You must bring the system to a state that reflects: "
            "a recorded QA result for the texture asset at 'assets/textures/environment/castle_tower_diffuse.png' "
            "with type 'texture', overall validation_status 'failed', severity_max 'issue', and autofix_applied true; "
            "the existing QA record 'qa_004' (castle_tower.fbx) is promoted so that its validation outcome reflects the applied auto-fix; "
            "in the asset catalog, the same PNG texture's performance_rating is 'high'; and "
            "you verify the CI context by reading the details of build run 'run_006'. "
            "Use only the exact identifiers and values listed here; default fields returned by read operations are acceptable."
        ),
        actions=[
            Action(
                name="create_asset_qa_result",
                kwargs={
                    "asset_path": "assets/textures/environment/castle_tower_diffuse.png",
                    "asset_type": "texture",
                    "validation_status": "failed",
                    "severity_max": "issue",
                    "autofix_applied": True
                }
            ),
            Action(
                name="promote_asset_autofix_to_pass",
                kwargs={"qa_id": "qa_004"}
            ),
            Action(
                name="update_asset_catalog_performance_rating",
                kwargs={
                    "asset_path": "assets/textures/environment/castle_tower_diffuse.png",
                    "performance_rating": "high"
                }
            ),
            Action(
                name="get_build_run_details",
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
        "You are a Performance Specialist driving Windows performance triage. Ensure the system reflects all of the following facts, "
        "without introducing any identifiers beyond those provided here: "
        "the pipeline 'pipeline_perf_windows' has a performance test run with the fixed id 'AUTO::test_run::pipeline_perf_windows::175' "
        "summarizing totals total=3, failed=1, skipped=0, passed=2 and coverage_pct=0.0; "
        "that same test_run_id contains exactly three results named 'FrameRateTest::SceneA' (failed, duration_ms=1200), "
        "'MemoryUsageTest::SceneA' (passed, duration_ms=800), and 'LoadTimeTest::SceneA' (passed, duration_ms=500); "
        "artifact 'build_001' is annotated with metadata perf_baseline='2025-01' and regression_flag=true; "
        "Windows symbolication for module 'GameEngine.dll' from build 'build_001' is available to run 'run_007'; "
        "a build-triage automation for 'run_007' exists with key 'AUTO::automation::build_triage::run_007::canonical' and completion status 'completed'; "
        "and the details of 'run_007' are readable."
        ),
        actions=[
            Action(
                name="attach_symbolicated_stack_to_run",
                kwargs={
                    "run_id": "run_007",
                    "build_id": "build_001",
                    "module_name": "GameEngine.dll",
                    "platform": "windows"
                }
            ),
            Action(
                name="create_test_run_summary",
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
                name="add_test_result_to_run",
                kwargs={
                    "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                    "test_name": "FrameRateTest::SceneA",
                    "status": "failed",
                    "duration_ms": 1200
                }
            ),
            Action(
                name="add_test_result_to_run",
                kwargs={
                    "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                    "test_name": "MemoryUsageTest::SceneA",
                    "status": "passed",
                    "duration_ms": 800
                }
            ),
            Action(
                name="add_test_result_to_run",
                kwargs={
                    "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                    "test_name": "LoadTimeTest::SceneA",
                    "status": "passed",
                    "duration_ms": 500
                }
            ),
            Action(
                name="update_artifact_metadata",
                kwargs={
                    "artifact_id": "build_001",
                    "metadata_patch": {"perf_baseline": "2025-01", "regression_flag": True}
                }
            ),
            Action(
                name="start_automation_run",
                kwargs={
                    "automation_type": "build_triage",
                    "input_ref": "run_007",
                    "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"
                }
            ),
            Action(
                name="complete_automation_run",
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
                name="get_build_run_details",
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
        "You are coordinating an integration failure on Linux for build run 'run_005'. "
        "Use failed test evidence from 'test_run_002' to identify the owner of 'src/game/network/multiplayer.cpp' and persist the triage context. "
        "Track the effort in a build-triage automation whose key MUST be 'AUTO::automation::build_triage::run_005::canonical' and whose completion status is 'completed'. "
        "Ensure the reproducible command for this run is 'make test-integration-linux', set the run's triage status to 'manual_review', "
        "and make symbolication available for Windows module 'GameEngine.dll' from build 'build_001' to assist cross-platform analysis. "
        "Return the updated details of 'run_005'. All parameters must come from this instruction or prior tool outputs."
        ),
        actions=[
            Action(name="list_failed_tests_for_run", kwargs={"test_run_id": "test_run_002"}),
            Action(name="map_path_to_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_005", "command": "make test-integration-linux"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id": "run_005",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_005",
                "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_005::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "manual_review",
                    "owner_id": "user_008",
                    "owner_path": "src/game/network/multiplayer.cpp",
                    "evidence_test_run": "test_run_002"
                }
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_005"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="qap_005",
        instruction=(
            "You are the Release & Performance steward. You make the CI triage state for 'run_007' and its "
            "performance signal explicit and auditable. At completion: 'run_007' is associated with symbolicated "
            "stacks for module 'GameEngine.dll' from 'build_001' on 'windows'; artifact 'build_001' metadata records "
            "regression_root_commit 'abc123def456789' and validated true; the performance pipeline 'pipeline_perf_windows' "
            "shows test run id 'AUTO::test_run::pipeline_perf_windows::175' with totals total=3, failed=1, skipped=0, "
            "passed=2, coverage_pct=0.0, and includes exactly 'FrameRateTest::SceneA' failed (duration_ms=1200), "
            "'MemoryUsageTest::SceneA' passed (800), and 'LoadTimeTest::SceneA' passed (500); a build_triage automation "
            "keyed 'AUTO::automation::build_triage::run_007::canonical' is completed with outputs triage_status "
            "'manual_review', and the run itself reflects triage_status 'manual_review'. Finally, you can read back "
            "refreshed details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(
                name="attach_symbolicated_stack_to_run",
                kwargs={"run_id": "run_007", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}
            ),
            Action(
                name="update_artifact_metadata",
                kwargs={"artifact_id": "build_001", "metadata_patch": {"regression_root_commit": "abc123def456789", "validated": True}}
            ),
            Action(
                name="create_test_run_summary",
                kwargs={"pipeline_id": "pipeline_perf_windows", "total": 3, "failed": 1, "skipped": 0, "passed": 2, "coverage_pct": 0.0}
            ),
            Action(
                name="add_test_result_to_run",
                kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "FrameRateTest::SceneA", "status": "failed", "duration_ms": 1200}
            ),
            Action(
                name="add_test_result_to_run",
                kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "MemoryUsageTest::SceneA", "status": "passed", "duration_ms": 800}
            ),
            Action(
                name="add_test_result_to_run",
                kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "LoadTimeTest::SceneA", "status": "passed", "duration_ms": 500}
            ),
            Action(
                name="start_automation_run",
                kwargs={"automation_type": "build_triage", "input_ref": "run_007", "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"}
            ),
            Action(
                name="complete_automation_run",
                kwargs={"automation_run_id": "AUTO::automation::build_triage::run_007::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review"}}
            ),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_007", "triage_status": "manual_review"}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_007"})
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
            "You are the Reliability Engineer for the asset‑validation pipeline. You bring build run 'run_006' on "
            "branch 'feature/new-assets' to a coherent triage state that, at completion, includes all of the following facts: "
            "failure category 'asset_validation_issue'; first bad commit 'jkl012ghi789def'; artifacts linked at "
            "'https://artifacts.techcorp.com/run_006/'; a completed build_triage automation "
            "'AUTO::automation::build_triage::run_006::canonical' whose outputs report triage_status 'pending'; the run itself "
            "records triage_status 'pending' and metadata.triage_note='owner to review assets'; and the run carries the repro "
            "command 'scripts/validate_assets.sh --run run_006 --branch feature/new-assets'. Return refreshed details for "
            "'run_006'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="set_build_failure_categorization", kwargs={"run_id": "run_006", "category": "asset_validation_issue"}),
            Action(name="set_first_bad_commit_on_run", kwargs={"run_id": "run_006", "commit_sha": "jkl012ghi789def"}),
            Action(name="link_artifact_to_run", kwargs={"run_id": "run_006", "artifacts_uri": "https://artifacts.techcorp.com/run_006/"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_006", "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_006::canonical", "status": "completed", "outputs_json": {"triage_status": "pending"}}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_006", "triage_status": "pending"}),
            Action(name="update_run_metadata", kwargs={"run_id": "run_006", "metadata_patch": {"triage_note": "owner to review assets"}}),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_006", "command": "scripts/validate_assets.sh --run run_006 --branch feature/new-assets"}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_006"})
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
            "You make ownership traceable and auditable for the Linux integration failure in run 'run_005'. "
            "At completion, the run metadata persists owner_id 'user_008' (team 'team_003') with ownership_type 'file_owner' "
            "and confidence_score 0.92; the run is categorized as 'integration_failure' and reflects triage_status 'manual_review'; "
            "a build_triage automation keyed 'AUTO::automation::build_triage::run_005::canonical' has completed with outputs "
            "including triage_status 'manual_review', owner_id 'user_008', and owner_path 'src/game/network/multiplayer.cpp'; "
            "a similar incident reference to 'run_001' is recorded with similarity_score 0.92; and for provenance the step "
            "'ownership_resolution' is marked completed. Return refreshed details for 'run_005'. Use only the identifiers and values provided here."
        ),
        actions=[
            Action(name="persist_owner_to_run", kwargs={"run_id": "run_005", "owner_id": "user_008", "team_id": "team_003", "ownership_type": "file_owner", "confidence_score": 0.92}),
            Action(name="set_build_failure_categorization", kwargs={"run_id": "run_005", "category": "integration_failure"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "owner_id": "user_008", "owner_path": "src/game/network/multiplayer.cpp"}}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
            Action(name="append_similar_incident_to_run", kwargs={"run_id": "run_005", "incident_run_id": "run_001", "similarity_score": 0.92}),
            Action(name="add_run_step", kwargs={"run_id": "run_005", "step_id": "ownership_resolution", "name": "ownership_resolution", "status": "completed"}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_005"})
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
            "You consolidate performance signal and bisect outcome without prescribing steps. When finished: for pipeline "
            "'pipeline_perf_windows' a test run exists with totals total=2, failed=0, skipped=0, passed=2 and initial coverage_pct=0.0, "
            "identified as 'AUTO::test_run::pipeline_perf_windows::175'; that run contains passing results for 'ShaderCompile::PassA' "
            "(600 ms) and 'ShaderCompile::PassB' (550 ms); coverage for that run is 72.5; CI run 'run_001' records bisect metadata "
            "first_bad_commit_sha='commit_abc123', last_good_commit_sha='commit_prev000', confidence=1.0 and associates "
            "fix_proposal_id='fix_001'; the run notes a repro command 'scripts/run_smoke_tests.sh --pipeline pipeline_perf_windows "
            "--run run_001'. Finally, you return refreshed details for 'run_001'. Use exactly these identifiers and values."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={"pipeline_id": "pipeline_perf_windows", "total": 2, "failed": 0, "skipped": 0, "passed": 2, "coverage_pct": 0.0}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "ShaderCompile::PassA", "status": "passed", "duration_ms": 600}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "ShaderCompile::PassB", "status": "passed", "duration_ms": 550}),
            Action(name="update_test_run_coverage", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "coverage_pct": 72.5}),
            Action(name="set_bisect_result_on_run", kwargs={"run_id": "run_001", "first_bad_commit_sha": "commit_abc123", "last_good_commit_sha": "commit_prev000", "confidence": 1.0}),
            Action(name="set_fix_proposal_on_run", kwargs={"run_id": "run_001", "fix_proposal_id": "fix_001"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_001", "command": "scripts/run_smoke_tests.sh --pipeline pipeline_perf_windows --run run_001"}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
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
            "You bring 'run_001' to a triage-ready state with compile-failure context and symbolication. "
            "By completion, the run’s failure_categorization is 'compilation_issue', its first_bad_commit is "
            "'abc123def456789', and Windows symbolication for 'GameEngine.dll' from 'build_001' is attached; "
            "the run reflects triage_status 'in_progress' and this state is captured under the canonical automation "
            "'AUTO::automation::build_triage::run_001::canonical'. You return refreshed details for 'run_001'. "
            "Use only these identifiers and values."
        ),
        actions=[
            Action(name="set_build_failure_categorization", kwargs={"run_id": "run_001", "category": "compilation_issue"}),
            Action(name="set_first_bad_commit_on_run", kwargs={"run_id": "run_001", "commit_sha": "abc123def456789"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "run_001 categorized as compilation_issue; first_bad_commit=abc123def456789; Windows symbolication attached; triage_status=in_progress captured via canonical automation; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_010",
        instruction=(
            "You ensure the asset‑intake state is coherent and its CI triage context is auditably captured. By the end of your work, "
            "the catalog contains 'assets/models/environment/castle_tower.fbx' typed 'model' with validation_status 'unverified' and "
            "performance_rating 'medium'; a QA record exists for the same asset with validation_status 'passed' and severity_max 'warning'; "
            "build run 'run_006' carries artifacts at 'https://artifacts.techcorp.com/run_006/', is categorized as 'asset_validation_issue', "
            "records the first bad commit 'jkl012ghi789def', and preserves the reproducibility command "
            "'scripts/validate_assets.sh --run run_006 --branch feature/new-assets'. A build_triage automation keyed "
            "'AUTO::automation::build_triage::run_006::canonical' is completed with outputs reporting triage_status 'pending', and the run "
            "itself reflects triage_status 'pending'. For provenance, the run shows completed steps 'triage_fetch_artifacts' and 'triage_repro'. "
            "Return refreshed details for 'run_006'. Use only the identifiers and values explicitly stated here."
        ),
        actions=[
            Action(name="register_asset_in_catalog", kwargs={"asset_path": "assets/models/environment/castle_tower.fbx", "asset_type": "model", "validation_status": "unverified", "performance_rating": "medium"}),
            Action(name="create_asset_qa_result", kwargs={"asset_path": "assets/models/environment/castle_tower.fbx", "asset_type": "model", "validation_status": "passed", "severity_max": "warning"}),
            Action(name="link_artifact_to_run", kwargs={"run_id": "run_006", "artifacts_uri": "https://artifacts.techcorp.com/run_006/"}),
            Action(name="set_build_failure_categorization", kwargs={"run_id": "run_006", "category": "asset_validation_issue"}),
            Action(name="set_first_bad_commit_on_run", kwargs={"run_id": "run_006", "commit_sha": "jkl012ghi789def"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_006", "command": "scripts/validate_assets.sh --run run_006 --branch feature/new-assets"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_006", "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_006::canonical", "status": "completed", "outputs_json": {"triage_status": "pending"}}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_006", "triage_status": "pending"}),
            Action(name="add_run_step", kwargs={"run_id": "run_006", "step_id": "triage_fetch_artifacts", "name": "triage_fetch_artifacts", "status": "completed"}),
            Action(name="add_run_step", kwargs={"run_id": "run_006", "step_id": "triage_repro", "name": "triage_repro", "status": "completed"}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_006"})
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
        "You are the Quality Engineer ensuring triage clarity for build run 'run_001'. Make symbolication available for module 'GameEngine.dll' from build 'build_001' on platform 'windows', "
        "record the reproducible command 'make build-windows-x64', resolve ownership for 'src/game/engine/renderer.cpp', and track the effort in a build-triage automation whose key must be 'AUTO::automation::build_triage::run_001::canonical'. "
        "Set the run triage_status to 'manual_review' and persist the owner mapping in the automation outputs. Return the refreshed details of 'run_001'."
        ),
        actions=[
            Action(name="get_build_run_details", kwargs={ "run_id": "run_001" }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={ "run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows" }),
            Action(name="record_repro_command_for_run", kwargs={ "run_id": "run_001", "command": "make build-windows-x64" }),
            Action(name="map_path_to_owner", kwargs={ "file_path": "src/game/engine/renderer.cpp" }),
            Action(name="start_automation_run", kwargs={ "automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical" }),
            Action(name="set_build_triage_status", kwargs={ "run_id": "run_001", "triage_status": "manual_review" }),
            Action(name="complete_automation_run", kwargs={ "automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "owner_id": "user_001", "owner_path": "src/game/engine/renderer.cpp"} }),
            Action(name="get_build_run_details", kwargs={ "run_id": "run_001" }),
        ],
        outputs=["Run run_001 updated: symbolication attached, repro recorded, triage_status=manual_review, owner persisted"],
    ),
    Task(
        annotator="0",
        user_id="qap_012",
        instruction=(
            "You consolidate Windows performance evidence and tie it cleanly to triage for 'run_007'. "
            "At completion, the system reflects: a fixed-id performance test run 'AUTO::test_run::pipeline_perf_windows::175' "
            "for pipeline 'pipeline_perf_windows' with totals total=4, failed=2, skipped=0, passed=2, coverage_pct=0.0 and exactly these "
            "results—'FrameRateTest::SceneB' failed (duration_ms=1100), 'MemoryUsageTest::SceneB' passed (700), "
            "'LoadTimeTest::SceneB' passed (450), 'StutterSpikeTest::SceneB' failed (1300); artifact 'build_001' metadata shows "
            "perf_baseline='2025-02' and regression_flag='true'; 'run_007' is linked to artifacts at "
            "'https://artifacts.techcorp.com/run_007/', carries symbolication for module 'GameEngine.dll' from build 'build_001' "
            "on 'windows', records a bisect outcome with first_bad_commit_sha='commit_def234', last_good_commit_sha='commit_prev111', "
            "confidence 0.97, preserves the repro command 'make perf-benchmark-windows', and reflects triage_status 'manual_review'. "
            "The canonical build_triage automation 'AUTO::automation::build_triage::run_007::canonical' is completed with outputs "
            "reporting triage_status 'manual_review' and bisect_first_bad 'commit_def234'. For provenance, the run shows a completed "
            "step with step_id 'perf_evidence_consolidated' and name 'perf_evidence_consolidated'. You return refreshed details for "
            "'run_007'. Use only the identifiers and values provided here."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={
                "pipeline_id": "pipeline_perf_windows", "total": 4, "failed": 2, "skipped": 0, "passed": 2, "coverage_pct": 0.0
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "FrameRateTest::SceneB", "status": "failed", "duration_ms": 1100
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "MemoryUsageTest::SceneB", "status": "passed", "duration_ms": 700
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "LoadTimeTest::SceneB", "status": "passed", "duration_ms": 450
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "StutterSpikeTest::SceneB", "status": "failed", "duration_ms": 1300
            }),
            Action(name="update_artifact_metadata", kwargs={
                "artifact_id": "build_001", "metadata_patch": {"perf_baseline": "2025-02", "regression_flag": "true"}
            }),
            Action(name="link_artifact_to_run", kwargs={
                "run_id": "run_007", "artifacts_uri": "https://artifacts.techcorp.com/run_007/"
            }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id": "run_007", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"
            }),
            Action(name="set_first_bad_commit_on_run", kwargs={
                "run_id": "run_007", "commit_sha": "commit_def234"
            }),
            Action(name="set_bisect_result_on_run", kwargs={
                "run_id": "run_007",
                "first_bad_commit_sha": "commit_def234",
                "last_good_commit_sha": "commit_prev111",
                "confidence": 0.97
            }),
            Action(name="record_repro_command_for_run", kwargs={
                "run_id": "run_007", "command": "make perf-benchmark-windows"
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_007",
                "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"
            }),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_007::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "manual_review", "bisect_first_bad": "commit_def234"}
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_007", "triage_status": "manual_review"}),
            Action(name="add_run_step", kwargs={
                "run_id": "run_007",
                "step_id": "perf_evidence_consolidated",
                "name": "perf_evidence_consolidated",
                "status": "completed"
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_007"})
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
            "You bring 'run_001' to a reproducible, auditably triaged state. At completion, the run has "
            "Windows symbolication attached for module 'GameEngine.dll' from build 'build_001'; its failure "
            "categorization is 'compilation_issue'; and the reproducible command 'make build-windows-x64' is "
            "recorded. A build_triage automation with the canonical key "
            "'AUTO::automation::build_triage::run_001::canonical' is present and completed with outputs showing "
            "triage_status 'in_progress', and the run itself reflects triage_status 'in_progress'. Finally, you "
            "return refreshed details for 'run_001'. Use only the identifiers and values stated here."
        ),
        actions=[
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="set_build_failure_categorization", kwargs={"run_id": "run_001", "category": "compilation_issue"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
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
        "You are coordinating a Linux integration failure in run 'run_005'. Use evidence from 'test_run_002' and ownership for 'src/game/network/multiplayer.cpp' to make the triage explicit. "
        "Ensure symbolication for module 'GameEngine.dll' from build 'build_001' on platform 'windows', set the reproducible command 'make test-integration-linux', "
        "and manage a build-triage automation with the key 'AUTO::automation::build_triage::run_005::canonical' that completes with triage_status 'in_progress' and the mapped owner. Return details of 'run_005'."
        ),
        actions=[
            Action(name="list_failed_tests_for_run", kwargs={ "test_run_id": "test_run_002" }),
            Action(name="map_path_to_owner", kwargs={ "file_path": "src/game/network/multiplayer.cpp" }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={ "run_id": "run_005", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows" }),
            Action(name="record_repro_command_for_run", kwargs={ "run_id": "run_005", "command": "make test-integration-linux" }),
            Action(name="start_automation_run", kwargs={ "automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical" }),
            Action(name="set_build_triage_status", kwargs={ "run_id": "run_005", "triage_status": "in_progress" }),
            Action(name="complete_automation_run", kwargs={ "automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "owner_id": "user_008", "owner_path": "src/game/network/multiplayer.cpp", "evidence_test_run": "test_run_002"} }),
            Action(name="get_build_run_details", kwargs={ "run_id": "run_005" }),
        ],
        outputs=["Run run_005 updated with symbols, repro, triage_status=in_progress; owner persisted from multiplayer.cpp"],
    ),
    Task(
        annotator="0",
        user_id="qap_015",
        instruction=(
            "You formalize the fix decision on build run 'run_001' with an auditable trail consistent with CI triage. "
            "At completion, the run persists fix_proposal_id 'fix_010' while triage_status remains 'in_progress'; "
            "the canonical build_triage automation 'AUTO::automation::build_triage::run_001::canonical' is completed with "
            "outputs capturing triage_status 'in_progress' and fix_proposal_id 'fix_010'; the run metadata includes "
            "fix_proposal_summary='fix_010 formalized' for provenance; and a provenance step with step_id "
            "'fix_proposal_formalized' and name 'fix_proposal_formalized' is marked completed. "
            "You then return refreshed details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="set_fix_proposal_on_run", kwargs={"run_id": "run_001", "fix_proposal_id": "fix_010"}),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "in_progress", "fix_proposal_id": "fix_010"}
            }),
            Action(name="update_run_metadata", kwargs={
                "run_id": "run_001",
                "metadata_patch": {"fix_proposal_summary": "fix_010 formalized"}
            }),
            Action(name="add_run_step", kwargs={
                "run_id": "run_001",
                "step_id": "fix_proposal_formalized",
                "name": "fix_proposal_formalized",
                "status": "completed"
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
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
            "You maintain triage hygiene on the feature branch with an auditable record. "
            "At completion, failures on branch 'feature/new-renderer' have been reviewed; "
            "run 'run_001' reflects triage_status 'in_progress', links artifacts at "
            "'https://artifacts.techcorp.com/run_001/', carries symbolication for module "
            "'GameEngine.dll' from build 'build_001' on platform 'windows', and preserves the "
            "reproducible command 'make build-windows-x64'. The run metadata records a "
            "failure_category with category 'render_pipeline_regression' and the first bad commit "
            "'abc123def456789'; the incident context includes a similar reference to 'run_007' with "
            "similarity_score 0.90; and provenance shows completed steps 'triage_fetch_artifacts' "
            "and 'triage_repro'. The canonical build_triage automation for this run "
            "'AUTO::automation::build_triage::run_001::canonical' is completed with outputs capturing "
            "triage_status 'in_progress' plus the branch, repro command, artifacts URI, and symbol "
            "module. You return refreshed details for 'run_001'. Use exactly these identifiers and values."
        ),
        actions=[
            Action(name="list_failed_build_runs_by_branch", kwargs={"branch": "feature/new-renderer"}),
            Action(name="link_artifact_to_run", kwargs={
                "run_id": "run_001",
                "artifacts_uri": "https://artifacts.techcorp.com/run_001/"
            }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id": "run_001",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="record_repro_command_for_run", kwargs={
                "run_id": "run_001",
                "command": "make build-windows-x64"
            }),
            Action(name="set_build_failure_categorization", kwargs={
                "run_id": "run_001",
                "category": "render_pipeline_regression"
            }),
            Action(name="set_first_bad_commit_on_run", kwargs={
                "run_id": "run_001",
                "commit_sha": "abc123def456789"
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="complete_automation_run", kwargs={
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
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="append_similar_incident_to_run", kwargs={
                "run_id": "run_001",
                "incident_run_id": "run_007",
                "similarity_score": 0.90
            }),
            Action(name="add_run_step", kwargs={
                "run_id": "run_001",
                "step_id": "triage_fetch_artifacts",
                "name": "triage_fetch_artifacts",
                "status": "completed"
            }),
            Action(name="add_run_step", kwargs={
                "run_id": "run_001",
                "step_id": "triage_repro",
                "name": "triage_repro",
                "status": "completed"
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
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
            "You make ownership and triage for the Linux integration failure in 'run_005' traceable and auditable. "
            "At completion, the run metadata persists owner_id 'user_008' (team 'team_003') with ownership_type "
            "'file_owner' and confidence_score 0.92; the run reflects triage_status 'manual_review'; Windows "
            "symbolication for 'GameEngine.dll' from 'build_001' (platform 'windows') is attached; the reproducible "
            "command 'make test-integration-linux' is recorded; and a build_triage automation with key "
            "'AUTO::automation::build_triage::run_005::canonical' is completed with outputs including "
            "triage_status 'manual_review', owner_id 'user_008', and owner_path 'src/game/network/multiplayer.cpp'. "
            "A similar-incident reference to 'run_001' with similarity_score 0.92 is stored. Finally, you return the "
            "refreshed details for 'run_005'. Use only the identifiers and values given here."
        ),
        actions=[
            Action(name="persist_owner_to_run", kwargs={"run_id": "run_005", "owner_id": "user_008", "team_id": "team_003", "ownership_type": "file_owner", "confidence_score": 0.92}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_005", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_005", "command": "make test-integration-linux"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "owner_id": "user_008", "owner_path": "src/game/network/multiplayer.cpp"}}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
            Action(name="append_similar_incident_to_run", kwargs={"run_id": "run_005", "incident_run_id": "run_001", "similarity_score": 0.92}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_005"})
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
            "You ground Windows shader performance signals in the triage record for 'run_001'. "
            "At completion, the system reflects a test run with id 'AUTO::test_run::pipeline_perf_windows::175' for "
            "'pipeline_perf_windows' (total=2, failed=1, skipped=0, passed=1, coverage_pct=0.0) containing exactly two results: "
            "'ShaderCompile::BatchA' passed (duration_ms=300) and 'ShaderCompile::BatchB' failed (duration_ms=450). "
            "Run 'run_001' links artifacts at 'https://artifacts.techcorp.com/run_001/', carries symbolication for "
            "'GameEngine.dll' from build 'build_001' on 'windows', records in its metadata a failure_category with category "
            "'performance_regression', records the first bad commit 'abc123def456789', and preserves the repro command "
            "'make test-integration-windows'. A build_triage automation "
            "'AUTO::automation::build_triage::run_001::canonical' is completed with outputs reporting triage_status "
            "'in_progress' and the same test_run_id; the run itself reflects triage_status 'in_progress', its metadata includes "
            "performance_test_run_id='AUTO::test_run::pipeline_perf_windows::175', and a similar-incident reference to 'run_007' "
            "with similarity_score 0.88 is present. You return refreshed details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={"pipeline_id": "pipeline_perf_windows", "total": 2, "failed": 1, "skipped": 0, "passed": 1, "coverage_pct": 0.0}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "ShaderCompile::BatchA", "status": "passed", "duration_ms": 300}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "ShaderCompile::BatchB", "status": "failed", "duration_ms": 450}),
            Action(name="link_artifact_to_run", kwargs={"run_id": "run_001", "artifacts_uri": "https://artifacts.techcorp.com/run_001/"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="set_build_failure_categorization", kwargs={"run_id": "run_001", "category": "performance_regression"}),
            Action(name="set_first_bad_commit_on_run", kwargs={"run_id": "run_001", "commit_sha": "abc123def456789"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_001", "command": "make test-integration-windows"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="update_run_metadata", kwargs={"run_id": "run_001", "metadata_patch": {"performance_test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="append_similar_incident_to_run", kwargs={"run_id": "run_001", "incident_run_id": "run_007", "similarity_score": 0.88}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
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
            "You strengthen the triage context for 'run_001'. At completion, the run has Windows symbolication attached "
            "for 'GameEngine.dll' from 'build_001'; artifacts are linked at 'https://artifacts.techcorp.com/run_001/'; "
            "its metadata is updated to {'stability': 'review'}; a build_triage automation with canonical key "
            "'AUTO::automation::build_triage::run_001::canonical' is completed with outputs showing triage_status "
            "'manual_review'; and the run itself reflects triage_status 'manual_review'. Finally, you return refreshed "
            "details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="link_artifact_to_run", kwargs={"run_id": "run_001", "artifacts_uri": "https://artifacts.techcorp.com/run_001/"}),
            Action(name="update_run_metadata", kwargs={"run_id": "run_001", "metadata_patch": {"stability": "review"}}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review"}}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "manual_review"}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
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
            "You prepare a performance triage record for 'run_007' consistent with real CI practice. "
            "At completion, the run reflects triage_status 'in_progress'; symbolication is available for "
            "'GameEngine.dll' from build 'build_001' on 'windows'; artifacts are linked at "
            "'https://artifacts.techcorp.com/run_007/'; the reproducible command is 'make performance-test-windows'; "
            "metadata records a failure_category with category 'performance_regression' and the first bad commit "
            "'abc123def456789'; the canonical build_triage automation "
            "'AUTO::automation::build_triage::run_007::canonical' is completed with outputs reporting triage_status "
            "'in_progress'; the incident context is persisted under run.metadata.similar_incidents as exactly one item "
            "{incident_run_id='run_001', similarity_score=0.90} (you do not modify any other similarly named fields); "
            "and provenance shows completed steps 'triage_fetch_artifacts' and 'triage_repro'. "
            "You return refreshed details for 'run_007'. Use exactly these identifiers and values."
        ),
        actions=[
            Action(
                name="link_artifact_to_run",
                kwargs={
                    "run_id": "run_007",
                    "artifacts_uri": "https://artifacts.techcorp.com/run_007/"
                }
            ),
            Action(
                name="attach_symbolicated_stack_to_run",
                kwargs={
                    "run_id": "run_007",
                    "build_id": "build_001",
                    "module_name": "GameEngine.dll",
                    "platform": "windows"
                }
            ),
            Action(
                name="record_repro_command_for_run",
                kwargs={
                    "run_id": "run_007",
                    "command": "make performance-test-windows"
                }
            ),
            Action(
                name="set_build_failure_categorization",
                kwargs={
                    "run_id": "run_007",
                    "category": "performance_regression"
                }
            ),
            Action(
                name="set_first_bad_commit_on_run",
                kwargs={
                    "run_id": "run_007",
                    "commit_sha": "abc123def456789"
                }
            ),
            Action(
                name="start_automation_run",
                kwargs={
                    "automation_type": "build_triage",
                    "input_ref": "run_007",
                    "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"
                }
            ),
            Action(
                name="complete_automation_run",
                kwargs={
                    "automation_run_id": "AUTO::automation::build_triage::run_007::canonical",
                    "status": "completed",
                    "outputs_json": {"triage_status": "in_progress"}
                }
            ),
            Action(
                name="set_build_triage_status",
                kwargs={
                    "run_id": "run_007",
                    "triage_status": "in_progress"
                }
            ),
            Action(
                name="add_run_step",
                kwargs={
                    "run_id": "run_007",
                    "step_id": "triage_fetch_artifacts",
                    "name": "triage_fetch_artifacts",
                    "status": "completed"
                }
            ),
            Action(
                name="add_run_step",
                kwargs={
                    "run_id": "run_007",
                    "step_id": "triage_repro",
                    "name": "triage_repro",
                    "status": "completed"
                }
            ),
            Action(
                name="update_run_metadata",
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
                name="get_build_run_details",
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
            "You update the Windows performance baseline and anchor it to triage context. "
            "At completion, the system reflects the fixed test run id "
            "'AUTO::test_run::pipeline_perf_windows::175' for pipeline 'pipeline_perf_windows' with totals "
            "total=3, failed=0, skipped=1, passed=2, coverage_pct=0.0 and exactly two results—"
            "'LoadTimeTest::LevelX' passed (duration_ms=600) and 'FrameRateTest::LevelX' passed (duration_ms=900); "
            "artifact 'build_001' metadata records perf_baseline='2025-03' and regression_flag='false'; build run 'run_007' "
            "reflects triage_status 'in_progress', its metadata records "
            "performance_test_run_id='AUTO::test_run::pipeline_perf_windows::175', provenance shows a completed step "
            "'perf_baseline_updated'; and the canonical build_triage automation "
            "'AUTO::automation::build_triage::run_007::canonical' is completed with outputs including triage_status "
            "'in_progress' and that test_run_id. You then return refreshed details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={"pipeline_id": "pipeline_perf_windows", "total": 3, "failed": 0, "skipped": 1, "passed": 2, "coverage_pct": 0.0}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "LoadTimeTest::LevelX", "status": "passed", "duration_ms": 600}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "FrameRateTest::LevelX", "status": "passed", "duration_ms": 900}),
            Action(name="update_artifact_metadata", kwargs={"artifact_id": "build_001", "metadata_patch": {"perf_baseline": "2025-03", "regression_flag": "false"}}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_007", "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_007::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_007", "triage_status": "in_progress"}),
            Action(name="update_run_metadata", kwargs={"run_id": "run_007", "metadata_patch": {"performance_test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="add_run_step", kwargs={"run_id": "run_007", "step_id": "perf_baseline_updated", "name": "perf_baseline_updated", "status": "completed"}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_007"})
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
            "You make ownership for the networking failure on 'run_005' auditable and persistent. By completion, failures from "
            "'test_run_002' are referenced as evidence; the code path 'src/game/network/multiplayer.cpp' resolves to owner_id "
            "'user_008' (team 'team_003') and that ownership is persisted on the run with ownership_type 'file_owner' and "
            "confidence_score 0.92; the run reflects triage_status 'manual_review' and the canonical build_triage automation for "
            "this run ('AUTO::automation::build_triage::run_005::canonical') is completed with outputs that include triage_status "
            "'manual_review', owner_id 'user_008', owner_path 'src/game/network/multiplayer.cpp', and evidence_test_run 'test_run_002'. "
            "For provenance, the run records a completed step 'owner_asserted'. Return refreshed details for 'run_005'. Use only these "
            "identifiers and values."
        ),
        actions=[
            Action(name="list_failed_tests_for_run", kwargs={"test_run_id": "test_run_002"}),
            Action(name="map_path_to_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="persist_owner_to_run", kwargs={"run_id": "run_005", "owner_id": "user_008", "team_id": "team_003", "ownership_type": "file_owner", "confidence_score": 0.92}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "owner_id": "user_008", "owner_path": "src/game/network/multiplayer.cpp", "evidence_test_run": "test_run_002"}}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
            Action(name="add_run_step", kwargs={"run_id": "run_005", "step_id": "owner_asserted", "name": "owner_asserted", "status": "completed"}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_005"})
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
        "You catalog and quality‑gate a VFX texture and anchor its CI triage context. "
        "At completion: the catalog contains 'assets/vfx/explosion/explosion_sparks.png' typed 'texture' named 'Explosion Sparks'; "
        "a passed QA exists with severity_max 'warning' and autofix_applied true; the catalog performance_rating is 'medium'; "
        "build run 'run_006' links artifacts at 'https://artifacts.techcorp.com/run_006/', carries symbolication for module "
        "'GameEngine.dll' from build 'build_001' on 'windows', preserves the reproducibility command "
        "'scripts/validate_assets.sh --asset assets/vfx/explosion/explosion_sparks.png --run run_006', reflects triage_status "
        "'in_progress', and is categorized as 'asset_validation_issue'. The canonical build_triage automation "
        "'AUTO::automation::build_triage::run_006::canonical' is completed with outputs including triage_status 'in_progress'. "
        "For provenance, the run shows a completed step 'vfx_texture_gated'. Return refreshed details for 'run_006'. "
        "Use only the identifiers and values stated here."
        ),
        actions=[
        Action(name="register_asset_in_catalog", kwargs={"asset_path": "assets/vfx/explosion/explosion_sparks.png", "asset_type": "texture", "asset_name": "Explosion Sparks"}),
        Action(name="create_asset_qa_result", kwargs={"asset_path": "assets/vfx/explosion/explosion_sparks.png", "asset_type": "texture", "validation_status": "passed", "severity_max": "warning", "autofix_applied": True}),
        Action(name="update_asset_catalog_performance_rating", kwargs={"asset_path": "assets/vfx/explosion/explosion_sparks.png", "performance_rating": "medium"}),
        Action(name="link_artifact_to_run", kwargs={"run_id": "run_006", "artifacts_uri": "https://artifacts.techcorp.com/run_006/"}),
        Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_006", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
        Action(name="record_repro_command_for_run", kwargs={"run_id": "run_006", "command": "scripts/validate_assets.sh --asset assets/vfx/explosion/explosion_sparks.png --run run_006"}),
        Action(name="set_build_failure_categorization", kwargs={"run_id": "run_006", "category": "asset_validation_issue"}),
        Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_006", "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"}),
        Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_006::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
        Action(name="set_build_triage_status", kwargs={"run_id": "run_006", "triage_status": "in_progress"}),
        Action(name="add_run_step", kwargs={"run_id": "run_006", "step_id": "vfx_texture_gated", "name": "vfx_texture_gated", "status": "completed"}),
        Action(name="get_build_run_details", kwargs={"run_id": "run_006"})
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
            "You advance the render regression investigation for 'run_001' and leave an audit trail. "
            "At completion: symbolication is attached for 'GameEngine.dll' from 'build_001' on 'windows'; the run reflects "
            "triage_status 'in_progress'; the reproducible command 'make build-windows-x64' is preserved; the canonical "
            "build_triage automation 'AUTO::automation::build_triage::run_001::canonical' is completed with outputs including "
            "triage_status 'in_progress' and symbol_module 'GameEngine.dll'; and provenance shows a completed step "
            "'symbols_attached'. You then return refreshed details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "symbol_module": "GameEngine.dll"}}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="add_run_step", kwargs={"run_id": "run_001", "step_id": "symbols_attached", "name": "symbols_attached", "status": "completed"}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Symbolication linked (GameEngine.dll, windows); repro command recorded; run_001 triage_status=in_progress; automation outputs captured; provenance step symbols_attached=completed; details retrieved."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_025",
        instruction=(
            "You stabilize the CI context for 'run_001' with owner accountability, reproducibility, and symbol awareness. "
            "At completion, failed test evidence from 'test_run_002' is referenced; the code path "
            "'src/game/engine/renderer.cpp' is mapped for ownership; symbolication for module 'GameEngine.dll' from build "
            "'build_001' on platform 'windows' is attached to the run; the run reflects triage_status 'in_progress' and "
            "preserves the reproducible command 'make build-windows-x64'; and the canonical build_triage automation for this run "
            "'AUTO::automation::build_triage::run_001::canonical' is completed with outputs that include triage_status "
            "'in_progress', owner_id 'user_001', owner_path 'src/game/engine/renderer.cpp', and evidence_test_run 'test_run_002'. "
            "You then return refreshed details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="list_failed_tests_for_run", kwargs={"test_run_id": "test_run_002"}),
            Action(name="map_path_to_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(
                name="attach_symbolicated_stack_to_run",
                kwargs={
                    "run_id": "run_001",
                    "build_id": "build_001",
                    "module_name": "GameEngine.dll",
                    "platform": "windows"
                }
            ),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(
                name="start_automation_run",
                kwargs={
                    "automation_type": "build_triage",
                    "input_ref": "run_001",
                    "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
                }
            ),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(
                name="complete_automation_run",
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
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Triage recorded: in_progress for run_001 with evidence test_run_002; ownership mapped for src/game/engine/renderer.cpp; symbolication attached; repro recorded; details retrieved."
        ]
    ),


    Task(
        annotator="0",
        user_id="qap_026",
        instruction=(
        "You align asset intake, catalog, and CI triage for a hero model with an auditable trail. "
        "At completion, the system reflects all of the following: a passed QA for "
        "'assets/characters/hero/hero_body.fbx' (type 'model', severity_max 'info', autofix_applied true); "
        "the same path is registered in the catalog as 'Hero Body' with performance_rating 'high'; "
        "build run 'run_006' links artifacts at 'https://artifacts.techcorp.com/run_006/', carries symbolication for "
        "module 'GameEngine.dll' from build 'build_001' on platform 'windows', is categorized as "
        "'asset_validation_issue', preserves the reproducibility command "
        "'scripts/validate_assets.sh --asset assets/characters/hero/hero_body.fbx --run run_006', and reflects "
        "triage_status 'manual_review'. The canonical build_triage automation "
        "'AUTO::automation::build_triage::run_006::canonical' is completed with outputs including "
        "triage_status 'manual_review' and asset_path 'assets/characters/hero/hero_body.fbx'. "
        "For provenance, the run shows completed steps 'triage_fetch_artifacts' and 'asset_intake_validated'. "
        "Return refreshed details for 'run_006'. Use only the identifiers and values provided here."
        ),
        actions=[
        Action(name="create_asset_qa_result", kwargs={"asset_path": "assets/characters/hero/hero_body.fbx", "asset_type": "model", "validation_status": "passed", "severity_max": "info", "autofix_applied": True}),
        Action(name="register_asset_in_catalog", kwargs={"asset_path": "assets/characters/hero/hero_body.fbx", "asset_type": "model", "asset_name": "Hero Body"}),
        Action(name="update_asset_catalog_performance_rating", kwargs={"asset_path": "assets/characters/hero/hero_body.fbx", "performance_rating": "high"}),
        Action(name="link_artifact_to_run", kwargs={"run_id": "run_006", "artifacts_uri": "https://artifacts.techcorp.com/run_006/"}),
        Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_006", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
        Action(name="set_build_failure_categorization", kwargs={"run_id": "run_006", "category": "asset_validation_issue"}),
        Action(name="record_repro_command_for_run", kwargs={"run_id": "run_006", "command": "scripts/validate_assets.sh --asset assets/characters/hero/hero_body.fbx --run run_006"}),
        Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_006", "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"}),
        Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_006::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "asset_path": "assets/characters/hero/hero_body.fbx"}}),
        Action(name="set_build_triage_status", kwargs={"run_id": "run_006", "triage_status": "manual_review"}),
        Action(name="add_run_step", kwargs={"run_id": "run_006", "step_id": "triage_fetch_artifacts", "name": "triage_fetch_artifacts", "status": "completed"}),
        Action(name="add_run_step", kwargs={"run_id": "run_006", "step_id": "asset_intake_validated", "name": "asset_intake_validated", "status": "completed"}),
        Action(name="get_build_run_details", kwargs={"run_id": "run_006"})
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
            "You document a targeted fix proposal for a shader compile failure on 'run_001' with traceability. "
            "At completion, the run shows fix_proposal_id 'fix_shader_001' while triage_status remains 'in_progress'; the "
            "canonical automation 'AUTO::automation::build_triage::run_001::canonical' is completed with outputs including "
            "triage_status 'in_progress' and fix_proposal_id 'fix_shader_001'; provenance shows a completed step "
            "'fix_proposal_documented'; and the incident context records a similar reference to 'run_007' with similarity_score "
            "0.85. You return refreshed details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="set_fix_proposal_on_run", kwargs={"run_id": "run_001", "fix_proposal_id": "fix_shader_001"}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "fix_proposal_id": "fix_shader_001"}}),
            Action(name="append_similar_incident_to_run", kwargs={"run_id": "run_001", "incident_run_id": "run_007", "similarity_score": 0.85}),
            Action(name="add_run_step", kwargs={"run_id": "run_001", "step_id": "fix_proposal_documented", "name": "fix_proposal_documented", "status": "completed"}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Fix proposal fix_shader_001 recorded; run_001 triage_status=in_progress; automation outputs captured; similar incident run_007 (0.85) noted; provenance step fix_proposal_documented=completed; details retrieved."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_028",
        instruction=(
            "You consolidate a focused Windows performance snapshot and bind it to the triage record for 'run_001' "
            "with reproducibility and provenance. By completion, the system shows a fixed-id performance test run "
            "'AUTO::test_run::pipeline_perf_windows::175' for pipeline 'pipeline_perf_windows' with totals total=2, "
            "failed=0, skipped=0, passed=2, coverage_pct=0.0 and exactly two results—'StreamingIO::ChunkLoad' passed "
            "(duration_ms=250) and 'Serialization::SaveGame' passed (duration_ms=380); run 'run_001' links artifacts at "
            "'https://artifacts.techcorp.com/run_001/', carries Windows symbolication for 'GameEngine.dll' from build "
            "'build_001', records first bad commit 'abc123def456789', preserves the reproducible command "
            "'make perf-benchmark-windows', and reflects triage_status 'in_progress'. The canonical build_triage automation "
            "'AUTO::automation::build_triage::run_001::canonical' is completed with outputs including triage_status "
            "'in_progress' and test_run_id 'AUTO::test_run::pipeline_perf_windows::175'; run metadata includes "
            "performance_test_run_id='AUTO::test_run::pipeline_perf_windows::175'. The incident context notes a similar "
            "reference to 'run_007' with similarity_score 0.88, and provenance shows a completed step 'perf_snapshot_curated'. "
            "Return refreshed details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={"pipeline_id": "pipeline_perf_windows", "total": 2, "failed": 0, "skipped": 0, "passed": 2, "coverage_pct": 0.0}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "StreamingIO::ChunkLoad", "status": "passed", "duration_ms": 250}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "Serialization::SaveGame", "status": "passed", "duration_ms": 380}),
            Action(name="link_artifact_to_run", kwargs={"run_id": "run_001", "artifacts_uri": "https://artifacts.techcorp.com/run_001/"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="set_first_bad_commit_on_run", kwargs={"run_id": "run_001", "commit_sha": "abc123def456789"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_001", "command": "make perf-benchmark-windows"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="update_run_metadata", kwargs={"run_id": "run_001", "metadata_patch": {"performance_test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="append_similar_incident_to_run", kwargs={"run_id": "run_001", "incident_run_id": "run_007", "similarity_score": 0.88}),
            Action(name="add_run_step", kwargs={"run_id": "run_001", "step_id": "perf_snapshot_curated", "name": "perf_snapshot_curated", "status": "completed"}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
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
            "You validate and catalog the texture while capturing the asset decision in the CI record. "
            "At completion, 'assets/textures/environment/castle_tower_diffuse.png' (type 'texture') has a QA result recorded "
            "with validation_status 'failed', severity_max 'issue', and autofix_applied true; QA 'qa_004' is promoted to pass; "
            "the catalog performance_rating for that asset is 'high'; and the canonical build_triage automation for 'run_006' "
            "('AUTO::automation::build_triage::run_006::canonical') is completed with outputs reflecting "
            "asset_path 'assets/textures/environment/castle_tower_diffuse.png', validation_status 'failed', and "
            "performance_rating 'high'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="create_asset_qa_result", kwargs={"asset_path": "assets/textures/environment/castle_tower_diffuse.png", "asset_type": "texture", "validation_status": "failed", "severity_max": "issue", "autofix_applied": True}),
            Action(name="promote_asset_autofix_to_pass", kwargs={"qa_id": "qa_004"}),
            Action(name="update_asset_catalog_performance_rating", kwargs={"asset_path": "assets/textures/environment/castle_tower_diffuse.png", "performance_rating": "high"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_006", "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_006::canonical", "status": "completed", "outputs_json": {"asset_path": "assets/textures/environment/castle_tower_diffuse.png", "validation_status": "failed", "performance_rating": "high"}})
        ],
        outputs=[
            "Asset castle_tower_diffuse.png QA recorded (failed, issue, autofix_applied=true), promoted qa_004 to pass; catalog performance_rating=high; automation recorded asset decision."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_030",
        instruction=(
            "You establish symbol availability across two runs with auditable context. "
            "At completion, both 'run_005' and 'run_007' carry symbolication for module 'GameEngine.dll' from build 'build_001' "
            "on 'windows' while triage_status for each is 'in_progress'; the canonical build_triage automation for each run "
            "('AUTO::automation::build_triage::run_005::canonical' and 'AUTO::automation::build_triage::run_007::canonical') is "
            "completed with outputs including triage_status 'in_progress'; and provenance shows a completed step "
            "'symbols_verified' on each. Use only these identifiers and values."
        ),
        actions=[
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_005", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_007", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_005", "triage_status": "in_progress"}),
            Action(name="add_run_step", kwargs={"run_id": "run_005", "step_id": "symbols_verified", "name": "symbols_verified", "status": "completed"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_007", "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_007::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_007", "triage_status": "in_progress"}),
            Action(name="add_run_step", kwargs={"run_id": "run_007", "step_id": "symbols_verified", "name": "symbols_verified", "status": "completed"})
        ],
        outputs=[
            "Symbolication attached and triage_status=in_progress for run_005 and run_007; automation outputs captured; provenance steps symbols_verified=completed for both."
        ]
    ),
        Task(
        annotator="0",
        user_id="qap_031",
        instruction=(
            "You publish an AI behavior performance snapshot and tie it into CI triage. "
            "At completion, the system reflects a test run 'AUTO::test_run::pipeline_perf_windows::175' for "
            "'pipeline_perf_windows' with totals total=2, failed=1, skipped=0, passed=1, coverage_pct=0.0 and exactly "
            "two results—'AI::PathfindingNavmesh' failed (duration_ms=980) and 'AI::DecisionTreeTick' passed (410). "
            "Artifact 'build_001' metadata records ai_profile='aggressive'. Build run 'run_007' reflects "
            "triage_status 'in_progress', a completed canonical build_triage automation "
            "'AUTO::automation::build_triage::run_007::canonical' whose outputs include "
            "ai_test_run_id 'AUTO::test_run::pipeline_perf_windows::175', and run metadata stores "
            "ai_perf_test_run_id='AUTO::test_run::pipeline_perf_windows::175'. You return refreshed details for 'run_007'. "
            "Use only these identifiers and values."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={"pipeline_id":"pipeline_perf_windows","total":2,"failed":1,"skipped":0,"passed":1,"coverage_pct":0.0}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"AI::PathfindingNavmesh","status":"failed","duration_ms":980}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"AI::DecisionTreeTick","status":"passed","duration_ms":410}),
            Action(name="update_artifact_metadata", kwargs={"artifact_id":"build_001","metadata_patch":{"ai_profile":"aggressive"}}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"ai_test_run_id":"AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="update_run_metadata", kwargs={"run_id":"run_007","metadata_patch":{"ai_perf_test_run_id":"AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_007"})
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
            "You establish a performance‑triage evidence bundle for 'run_006' with a clear audit trail. "
            "At completion, run_006 metadata shows priority='high'; the reproducibility command "
            "'make perf-benchmark-windows' is recorded; symbolication for 'GameEngine.dll' from 'build_001' on 'windows' "
            "is attached; a similar incident references 'run_007' with similarity_score 0.87; the run reflects "
            "triage_status 'manual_review' under a completed canonical build_triage automation "
            "'AUTO::automation::build_triage::run_006::canonical' whose outputs report triage_status 'manual_review'; "
            "and provenance shows completed steps 'triage_fetch_artifacts' and 'triage_repro'. "
            "You return refreshed details for 'run_006'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="update_run_metadata", kwargs={"run_id":"run_006","metadata_patch":{"priority":"high"}}),
            Action(name="record_repro_command_for_run", kwargs={"run_id":"run_006","command":"make perf-benchmark-windows"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id":"run_006","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="append_similar_incident_to_run", kwargs={"run_id":"run_006","incident_run_id":"run_007","similarity_score":0.87}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_006","automation_run_id":"AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="add_run_step", kwargs={"run_id":"run_006","step_id":"triage_fetch_artifacts","name":"triage_fetch_artifacts","status":"completed"}),
            Action(name="add_run_step", kwargs={"run_id":"run_006","step_id":"triage_repro","name":"triage_repro","status":"completed"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed","outputs_json":{"triage_status":"manual_review"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_006"})
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
            "You catalog and quality‑gate the UI audio click while surfacing its CI context. "
            "By completion, the catalog registers 'assets/audio/ui/click.wav' typed 'audio' with asset_name 'UI Click'; "
            "a QA record exists with validation_status 'passed', severity_max 'info', autofix_applied false; the catalog performance_rating is 'high'; "
            "build run 'run_006' is tracked under the completed canonical build_triage automation "
            "'AUTO::automation::build_triage::run_006::canonical' with triage_status 'in_progress'; Windows symbolication for "
            "'GameEngine.dll' from 'build_001' on 'windows' is attached; provenance shows 'audio_asset_evidence_ingest' completed; "
            "and run metadata stores audio_asset_path='assets/audio/ui/click.wav'. Return refreshed details for 'run_006'. "
            "Use only these identifiers and values."
        ),
        actions=[
            Action(name="register_asset_in_catalog", kwargs={
                "asset_path":"assets/audio/ui/click.wav","asset_type":"audio","asset_name":"UI Click"
            }),
            Action(name="create_asset_qa_result", kwargs={
                "asset_path":"assets/audio/ui/click.wav","asset_type":"audio",
                "validation_status":"passed","severity_max":"info","autofix_applied":False
            }),
            Action(name="update_asset_catalog_performance_rating", kwargs={
                "asset_path":"assets/audio/ui/click.wav","performance_rating":"high"
            }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id":"run_006","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type":"build_triage","input_ref":"run_006",
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_006","triage_status":"in_progress"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical",
                "status":"completed","outputs_json":{"triage_status":"in_progress"}
            }),
            Action(name="add_run_step", kwargs={
                "run_id":"run_006","step_id":"audio_asset_evidence_ingest","name":"audio_asset_evidence_ingest","status":"completed"
            }),
            Action(name="update_run_metadata", kwargs={
                "run_id":"run_006","metadata_patch":{"audio_asset_path":"assets/audio/ui/click.wav"}
            }),
            Action(name="get_build_run_details", kwargs={"run_id":"run_006"})
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
            "You make 'run_007' reproducible and symbol‑aware for performance triage with incident correlation. "
            "At completion, the run stores the command 'make performance-test-windows'; carries symbolication for 'GameEngine.dll' "
            "from 'build_001' on 'windows'; reflects triage_status 'manual_review' under a completed canonical build_triage automation "
            "'AUTO::automation::build_triage::run_007::canonical'; provenance includes a completed step 'triage_repro'; and a similar "
            "incident referencing 'run_006' is recorded with similarity_score 0.83. You return refreshed details for 'run_007'. "
            "Use only these identifiers and values."
        ),
        actions=[
            Action(name="record_repro_command_for_run", kwargs={"run_id":"run_007","command":"make performance-test-windows"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id":"run_007","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="append_similar_incident_to_run", kwargs={"run_id":"run_007","incident_run_id":"run_006","similarity_score":0.83}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_007","triage_status":"manual_review"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"triage_status":"manual_review"}}),
            Action(name="add_run_step", kwargs={"run_id":"run_007","step_id":"triage_repro","name":"triage_repro","status":"completed"}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_007"})
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
            "You publish a memory‑profiling snapshot and anchor it to CI triage for 'run_007'. "
            "At completion, the system holds test run 'AUTO::test_run::pipeline_perf_windows::175' for 'pipeline_perf_windows' "
            "with totals total=2, failed=0, skipped=0, passed=2, coverage_pct=0.0 and exactly two results—"
            "'Memory::PeakUsageSceneA' passed (820) and 'Memory::PeakUsageSceneB' passed (910); artifact 'build_001' metadata "
            "records memory_sampling='heap_only'; symbolication for 'GameEngine.dll' from 'build_001' on 'windows' is attached to the run; "
            "'run_007' reflects triage_status 'in_progress'; the canonical build_triage automation "
            "'AUTO::automation::build_triage::run_007::canonical' is completed with outputs including "
            "performance_test_run_id 'AUTO::test_run::pipeline_perf_windows::175' and triage_status 'in_progress'; "
            "run metadata stores performance_test_run_id='AUTO::test_run::pipeline_perf_windows::175'; and provenance shows a "
            "completed step 'perf_snapshot_curated'. You return refreshed details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={"pipeline_id":"pipeline_perf_windows","total":2,"failed":0,"skipped":0,"passed":2,"coverage_pct":0.0}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"Memory::PeakUsageSceneA","status":"passed","duration_ms":820}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"Memory::PeakUsageSceneB","status":"passed","duration_ms":910}),
            Action(name="update_artifact_metadata", kwargs={"artifact_id":"build_001","metadata_patch":{"memory_sampling":"heap_only"}}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id":"run_007","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"performance_test_run_id":"AUTO::test_run::pipeline_perf_windows::175","triage_status":"in_progress"}}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="update_run_metadata", kwargs={"run_id":"run_007","metadata_patch":{"performance_test_run_id":"AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="add_run_step", kwargs={"run_id":"run_007","step_id":"perf_snapshot_curated","name":"perf_snapshot_curated","status":"completed"}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_007"})
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
            "You consolidate reproducibility and evidence for 'run_008' to support manual triage. "
            "At completion, the run stores reproducible command 'make test-windows-x64'; carries symbolication for "
            "'GameEngine.dll' from 'build_001' on 'windows'; metadata records repro_env='windows_x64_ci'; provenance shows "
            "completed steps 'triage_repro' and 'evidence_bundle'; a similar incident references 'run_006' with similarity_score 0.82; "
            "and the run reflects triage_status 'manual_review' under a completed canonical build_triage automation "
            "'AUTO::automation::build_triage::run_008::canonical' whose outputs report triage_status 'manual_review'. "
            "You return refreshed details for 'run_008'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_008","automation_run_id":"AUTO::automation::build_triage::run_008::canonical"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id":"run_008","command":"make test-windows-x64"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id":"run_008","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="update_run_metadata", kwargs={"run_id":"run_008","metadata_patch":{"repro_env":"windows_x64_ci"}}),
            Action(name="add_run_step", kwargs={"run_id":"run_008","step_id":"triage_repro","name":"triage_repro","status":"completed"}),
            Action(name="add_run_step", kwargs={"run_id":"run_008","step_id":"evidence_bundle","name":"evidence_bundle","status":"completed"}),
            Action(name="append_similar_incident_to_run", kwargs={"run_id":"run_008","incident_run_id":"run_006","similarity_score":0.82}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_008","triage_status":"manual_review"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_008::canonical","status":"completed","outputs_json":{"triage_status":"manual_review"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_008"})
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
            "You register and quality‑gate the UI texture while surfacing its CI context. "
            "At completion, the catalog contains 'assets/textures/ui/health_bar.png' typed 'texture' named 'Health Bar'; "
            "a QA record exists for that texture with validation_status 'failed', severity_max 'warning', autofix_applied true; "
            "the catalog performance_rating is 'medium'; symbolication for 'GameEngine.dll' from 'build_001' on 'windows' is attached; "
            "and build run 'run_006' reflects triage_status 'manual_review' under a completed canonical build_triage automation "
            "'AUTO::automation::build_triage::run_006::canonical'. You return refreshed details for 'run_006'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="register_asset_in_catalog", kwargs={"asset_path":"assets/textures/ui/health_bar.png","asset_type":"texture","asset_name":"Health Bar"}),
            Action(name="create_asset_qa_result", kwargs={"asset_path":"assets/textures/ui/health_bar.png","asset_type":"texture","validation_status":"failed","severity_max":"warning","autofix_applied":True}),
            Action(name="update_asset_catalog_performance_rating", kwargs={"asset_path":"assets/textures/ui/health_bar.png","performance_rating":"medium"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id":"run_006","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_006","automation_run_id":"AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed","outputs_json":{"triage_status":"manual_review"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_006"})
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
            "You establish a deterministic performance record and link it to triage for 'run_007'. "
            "At completion, the system holds fixed test_run 'AUTO::test_run::pipeline_perf_windows::175' for 'pipeline_perf_windows' "
            "with totals total=3, failed=1, skipped=0, passed=2, coverage_pct=78.3 and exactly three results—"
            "'FrameRateTest::SceneB' failed (1300), 'MemoryUsageTest::SceneB' passed (780), 'LoadTimeTest::SceneB' passed (520); "
            "artifact 'build_002' metadata records perf_baseline='2025-02' and regression_flag=true; 'run_007' reflects "
            "triage_status 'in_progress', a completed canonical build_triage automation "
            "'AUTO::automation::build_triage::run_007::canonical' whose outputs include "
            "test_run_id 'AUTO::test_run::pipeline_perf_windows::175', and run metadata stores "
            "performance_test_run_id='AUTO::test_run::pipeline_perf_windows::175'; and provenance shows a completed step "
            "'triage_fetch_artifacts'. You return refreshed details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={"pipeline_id":"pipeline_perf_windows","total":3,"failed":1,"skipped":0,"passed":2,"coverage_pct":78.3}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"FrameRateTest::SceneB","status":"failed","duration_ms":1300}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"MemoryUsageTest::SceneB","status":"passed","duration_ms":780}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"LoadTimeTest::SceneB","status":"passed","duration_ms":520}),
            Action(name="update_artifact_metadata", kwargs={"artifact_id":"build_002","metadata_patch":{"perf_baseline":"2025-02","regression_flag":True}}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"test_run_id":"AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="update_run_metadata", kwargs={"run_id":"run_007","metadata_patch":{"performance_test_run_id":"AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="add_run_step", kwargs={"run_id":"run_007","step_id":"triage_fetch_artifacts","name":"triage_fetch_artifacts","status":"completed"}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_007"})
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
            "You make the networking failure on 'run_005' fully auditable with clear ownership and context. "
            "At completion, ownership resolved from 'src/game/network/multiplayer.cpp' is persisted to the run as "
            "owner_id 'user_008', team 'team_003', ownership_type 'file_owner', confidence_score 0.92; the run records "
            "repro command 'make test-networking-lan'; carries symbolication for 'GameEngine.dll' from 'build_001' on 'windows'; "
            "provenance shows completed steps 'triage_fetch_artifacts' and 'owner_resolution'; a similar incident references 'run_004' "
            "with similarity_score 0.83; and the run reflects triage_status 'manual_review' under a completed canonical build_triage "
            "automation 'AUTO::automation::build_triage::run_005::canonical' whose outputs report triage_status 'manual_review' and "
            "owner_path 'src/game/network/multiplayer.cpp'. You return refreshed details for 'run_005'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="persist_owner_to_run", kwargs={"run_id":"run_005","owner_id":"user_008","team_id":"team_003","ownership_type":"file_owner","confidence_score":0.92}),
            Action(name="record_repro_command_for_run", kwargs={"run_id":"run_005","command":"make test-networking-lan"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id":"run_005","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_005","automation_run_id":"AUTO::automation::build_triage::run_005::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_005","triage_status":"manual_review"}),
            Action(name="add_run_step", kwargs={"run_id":"run_005","step_id":"triage_fetch_artifacts","name":"triage_fetch_artifacts","status":"completed"}),
            Action(name="add_run_step", kwargs={"run_id":"run_005","step_id":"owner_resolution","name":"owner_resolution","status":"completed"}),
            Action(name="append_similar_incident_to_run", kwargs={"run_id":"run_005","incident_run_id":"run_004","similarity_score":0.83}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_005::canonical","status":"completed","outputs_json":{"triage_status":"manual_review","owner_id":"user_008","owner_path":"src/game/network/multiplayer.cpp"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_005"})
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
            "You prepare symbol availability and root‑cause context for build run 'run_001'. "
            "At completion, symbols for module 'GameEngine.dll' from 'build_001' on 'windows' are registered and attached to "
            "the run; the failure categorization is 'compilation_issue'; the first_bad_commit is 'abc123def456789'; "
            "and the canonical build_triage automation 'AUTO::automation::build_triage::run_001::canonical' is completed with "
            "outputs reporting triage_status 'in_progress', while the run reflects triage_status 'in_progress'. "
            "You return refreshed details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="register_symbol", kwargs={"build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id":"run_001","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="set_build_failure_categorization", kwargs={"run_id":"run_001","category":"compilation_issue"}),
            Action(name="set_first_bad_commit_on_run", kwargs={"run_id":"run_001","commit_sha":"abc123def456789"}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_001","automation_run_id":"AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_001","triage_status":"in_progress"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_001::canonical","status":"completed","outputs_json":{"triage_status":"in_progress"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_001"})
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
            "You make 'run_007' auditable with a clear classification snapshot and repro context. "
            "By completion, the run’s metadata.failure_category is 'test_failure'; first_bad_commit is "
            "'abc123def456789'; the repro command 'make test-windows-x64' is recorded; triage_status is "
            "'in_progress' under the completed canonical automation 'AUTO::automation::build_triage::run_007::canonical' "
            "whose outputs include triage_status 'in_progress' and failure_categorization 'test_failure'; and provenance "
            "shows a completed step 'triage_classified'. You return refreshed details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id":"run_007","command":"make test-windows-x64"}),
            Action(name="set_first_bad_commit_on_run", kwargs={"run_id":"run_007","commit_sha":"abc123def456789"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="add_run_step", kwargs={"run_id":"run_007","step_id":"triage_classified","name":"triage_classified","status":"completed"}),
            Action(name="set_build_failure_categorization", kwargs={"run_id":"run_007","category":"test_failure"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"triage_status":"in_progress","failure_categorization":"test_failure"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "run_007: failure_categorization remained 'performance_regression'; metadata.failure_category stored as {category:'test_failure'}; first_bad_commit=abc123def456789; repro preserved; triage_status=in_progress via automation; step triage_classified=completed; details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_042",
        instruction=(
        "You establish owner accountability for 'run_005'. By completion, the run’s metadata persists owner_id 'user_001' "
        "and owner_path 'src/game/engine/renderer.cpp', symbolication for 'GameEngine.dll' from 'build_001' on 'windows' "
        "is attached, and triage_status is 'manual_review' with the canonical automation "
        "'AUTO::automation::build_triage::run_005::canonical' completed capturing that status. Return the refreshed "
        "details for 'run_005'. Use only these identifiers and values."
        ),
        actions=[
        Action(name="map_path_to_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
        Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_005", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
        Action(name="update_run_metadata", kwargs={"run_id": "run_005", "metadata_patch": {"owner_id": "user_001", "owner_path": "src/game/engine/renderer.cpp"}}),
        Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
        Action(name="set_build_triage_status", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
        Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "owner_id": "user_001", "owner_path": "src/game/engine/renderer.cpp"}}),
        Action(name="get_build_run_details", kwargs={"run_id": "run_005"})
        ],
        outputs=[
        "Ownership persisted (user_001 for src/game/engine/renderer.cpp); symbolication attached; triage_status=manual_review captured via automation; run_005 details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_043",
        instruction=(
        "You enrich incident context for 'run_005'. At completion, the run carries a similar‑incident reference to 'run_003' "
        "with similarity_score 0.84; a bisect outcome isolates first_bad_commit 'commit_def456' and last_good_commit "
        "'commit_prev111' at confidence 0.95; metadata includes owner_team 'networking'; and triage_status 'manual_review' "
        "is recorded with the canonical automation 'AUTO::automation::build_triage::run_005::canonical' marked completed. "
        "Return refreshed details for 'run_005'."
        ),
        actions=[
        Action(name="append_similar_incident_to_run", kwargs={"run_id": "run_005", "incident_run_id": "run_003", "similarity_score": 0.84}),
        Action(name="set_bisect_result_on_run", kwargs={"run_id": "run_005", "first_bad_commit_sha": "commit_def456", "last_good_commit_sha": "commit_prev111", "confidence": 0.95}),
        Action(name="update_run_metadata", kwargs={"run_id": "run_005", "metadata_patch": {"owner_team": "networking"}}),
        Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
        Action(name="set_build_triage_status", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
        Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "bisect_first_bad": "commit_def456"}}),
        Action(name="get_build_run_details", kwargs={"run_id": "run_005"})
        ],
        outputs=[
        "Similar incident run_003 (0.84) recorded; bisect first_bad=commit_def456 last_good=commit_prev111 (0.95); metadata updated; triage_status=manual_review recorded; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_044",
        instruction=(
        "You provide symbol context for 'run_001'. By the end, symbols for 'AudioEngine.dll' from 'build_003' on 'windows' "
        "are registered and the symbolicated stack is attached to the run; triage_status is 'in_progress' with the canonical "
        "automation 'AUTO::automation::build_triage::run_001::canonical' completed capturing that status. Return refreshed "
        "details for 'run_001'."
        ),
        actions=[
        Action(name="register_symbol", kwargs={"build_id": "build_003", "module_name": "AudioEngine.dll", "platform": "windows"}),
        Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_001", "build_id": "build_003", "module_name": "AudioEngine.dll", "platform": "windows"}),
        Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
        Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
        Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
        Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=[
        "Symbols registered and attached (AudioEngine.dll build_003/windows); triage_status=in_progress recorded; run_001 details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_045",
        instruction=(
            "You consolidate a reproducible triage dossier for 'run_001' linking evidence, ownership, and artifact context. "
            "By completion, the run preserves the repro command 'make build-windows-x64'; carries Windows symbolication for "
            "'GameEngine.dll' from 'build_001'; links artifact 'build_002' whose metadata records hotfix_candidate=true and perf_baseline='2025-03'; "
            "evidence test run 'AUTO::test_run::pipeline_perf_windows::175' exists with totals total=2, failed=1, skipped=0, passed=1, coverage_pct=78.0 and exactly two results—"
            "'FrameRateTest::SceneC' failed (1250) and 'MemoryUsageTest::SceneC' passed (810); ownership is persisted as owner_id 'user_001' for owner_path "
            "'src/game/engine/renderer.cpp' with ownership_type 'file_owner' and confidence_score 0.9; a similar incident references 'run_006' with similarity_score 0.88; "
            "provenance shows completed steps 'triage_fetch_artifacts' and 'owner_resolution'; triage reflects 'in_progress' under the completed canonical build_triage automation "
            "'AUTO::automation::build_triage::run_001::canonical'; and run metadata stores "
            "{'evidence_test_run':'AUTO::test_run::pipeline_perf_windows::175','linked_artifact':'build_002'}. "
            "Return refreshed details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="record_repro_command_for_run", kwargs={"run_id":"run_001","command":"make build-windows-x64"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id":"run_001","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"
            }),
            Action(name="link_artifact_to_run", kwargs={"run_id":"run_001","artifact_id":"build_002"}),
            Action(name="update_artifact_metadata", kwargs={
                "artifact_id":"build_002","metadata_patch":{"hotfix_candidate":True,"perf_baseline":"2025-03"}
            }),
            Action(name="create_test_run_summary", kwargs={
                "pipeline_id":"pipeline_perf_windows","total":2,"failed":1,"skipped":0,"passed":1,"coverage_pct":78.0
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"FrameRateTest::SceneC",
                "status":"failed","duration_ms":1250
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"MemoryUsageTest::SceneC",
                "status":"passed","duration_ms":810
            }),
            Action(name="update_run_metadata", kwargs={
                "run_id":"run_001",
                "metadata_patch":{"evidence_test_run":"AUTO::test_run::pipeline_perf_windows::175","linked_artifact":"build_002"}
            }),
            Action(name="persist_owner_to_run", kwargs={
                "run_id":"run_001","owner_id":"user_001","owner_path":"src/game/engine/renderer.cpp",
                "ownership_type":"file_owner","confidence_score":0.9
            }),
            Action(name="append_similar_incident_to_run", kwargs={
                "run_id":"run_001","incident_run_id":"run_006","similarity_score":0.88
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type":"build_triage","input_ref":"run_001",
                "automation_run_id":"AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_001","triage_status":"in_progress"}),
            Action(name="add_run_step", kwargs={"run_id":"run_001","step_id":"triage_fetch_artifacts","name":"triage_fetch_artifacts","status":"completed"}),
            Action(name="add_run_step", kwargs={"run_id":"run_001","step_id":"owner_resolution","name":"owner_resolution","status":"completed"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_001::canonical","status":"completed",
                "outputs_json":{
                    "triage_status":"in_progress","artifact_id":"build_002",
                    "owner_id":"user_001","owner_path":"src/game/engine/renderer.cpp",
                    "evidence_test_run":"AUTO::test_run::pipeline_perf_windows::175"
                }
            }),
            Action(name="get_build_run_details", kwargs={"run_id":"run_001"})
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
            "You publish a deterministic unit‑test snapshot and tie it to triage on 'run_002'. "
            "At completion, the system carries a test run with the fixed id 'AUTO::test_run::pipeline_unit_tests::001' "
            "for pipeline 'pipeline_unit_tests' with totals total=2, failed=1, skipped=0, passed=1 and "
            "coverage_pct=85.5; it contains exactly two results—'PhysicsUnitTest::VectorMath' passed (75) and "
            "'PhysicsUnitTest::Collision' failed (210). Build run 'run_002' reflects triage_status 'in_progress' "
            "under the completed canonical automation 'AUTO::automation::build_triage::run_002::canonical' whose "
            "outputs include test_run_id 'AUTO::test_run::pipeline_unit_tests::001', and run metadata stores "
            "unit_test_run_id='AUTO::test_run::pipeline_unit_tests::001'. You return refreshed details for 'run_002'. "
            "Use only these identifiers and values."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={"pipeline_id":"pipeline_unit_tests","total":2,"failed":1,"skipped":0,"passed":1,"coverage_pct":85.5}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_unit_tests::001","test_name":"PhysicsUnitTest::VectorMath","status":"passed","duration_ms":75}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_unit_tests::001","test_name":"PhysicsUnitTest::Collision","status":"failed","duration_ms":210}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_002","automation_run_id":"AUTO::automation::build_triage::run_002::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_002","triage_status":"in_progress"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_002::canonical","status":"completed","outputs_json":{"triage_status":"in_progress","test_run_id":"AUTO::test_run::pipeline_unit_tests::001"}}),
            Action(name="add_run_step", kwargs={"run_id":"run_002","step_id":"unit_test_evidence_ingest","name":"unit_test_evidence_ingest","status":"completed"}),
            Action(name="update_run_metadata", kwargs={"run_id":"run_002","metadata_patch":{"unit_test_run_id":"AUTO::test_run::pipeline_unit_tests::001"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_002"})
        ],
        outputs=[
            "Unit test run AUTO::test_run::pipeline_unit_tests::001 recorded with 2 results (85.5%); run_002 triage_status=in_progress; evidence ingested; metadata linked; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_047",
        instruction=(
            "You progress the performance investigation for 'run_007'. At completion, the incident context contains a single "
            "similar reference to 'run_008' with similarity_score 0.92; the run is linked to artifact 'build_002' (also marked "
            "hotfix_candidate=true) and run metadata records artifact_id 'build_002'; triage_status is 'in_progress' with the "
            "canonical automation 'AUTO::automation::build_triage::run_007::canonical' completed capturing that status and artifact. "
            "Return refreshed details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="append_similar_incident_to_run", kwargs={"run_id":"run_007","incident_run_id":"run_008","similarity_score":0.92}),
            Action(name="link_artifact_to_run", kwargs={"run_id":"run_007","artifact_id":"build_002"}),
            Action(name="update_artifact_metadata", kwargs={"artifact_id":"build_002","metadata_patch":{"hotfix_candidate":True}}),
            Action(name="update_run_metadata", kwargs={"run_id":"run_007","metadata_patch":{"artifact_id":"build_002"}}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"triage_status":"in_progress","artifact_id":"build_002"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "Similar incident run_008 (0.92) recorded; build_002 linked and hotfix_candidate=true; run_007 triage_status=in_progress; artifact_id persisted; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_048",
        instruction=(
            "You stabilize CI context for 'run_007' with clear evidence and ownership. By completion, failed‑test evidence from "
            "'test_run_002' is associated (run metadata records evidence_test_run='test_run_002'); symbolication for 'GameEngine.dll' "
            "from 'build_001' on 'windows' is available; the run preserves the repro command 'make performance-test-windows'; "
            "ownership is resolved and persisted as owner_id 'user_001' for owner_path 'src/game/engine/renderer.cpp'; and "
            "triage_status is 'manual_review' with the canonical automation 'AUTO::automation::build_triage::run_007::canonical' "
            "completed capturing that context. Return refreshed details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="list_failed_tests_for_run", kwargs={"test_run_id":"test_run_002"}),
            Action(name="map_path_to_owner", kwargs={"file_path":"src/game/engine/renderer.cpp"}),
            Action(name="persist_owner_to_run", kwargs={"run_id":"run_007","owner_id":"user_001","owner_path":"src/game/engine/renderer.cpp"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id":"run_007","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id":"run_007","command":"make performance-test-windows"}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_007","triage_status":"manual_review"}),
            Action(name="update_run_metadata", kwargs={"run_id":"run_007","metadata_patch":{"evidence_test_run":"test_run_002"}}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"triage_status":"manual_review","owner_id":"user_001","owner_path":"src/game/engine/renderer.cpp","evidence_test_run":"test_run_002"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "Evidence test_run_002 persisted; symbolication attached; repro preserved; ownership persisted (user_001 for src/game/engine/renderer.cpp); triage_status=manual_review captured; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_049",
        instruction=(
        "You confirm and persist code ownership for 'src/game/network/multiplayer.cpp' within the triage record of 'run_005'. "
        "By the end, the run’s metadata carries owner_id 'user_008' and owner_path 'src/game/network/multiplayer.cpp', and "
        "triage_status is 'manual_review' with the canonical automation "
        "'AUTO::automation::build_triage::run_005::canonical' completed capturing that status. Return refreshed details "
        "for 'run_005'."
        ),
        actions=[
        Action(name="map_path_to_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
        Action(name="update_run_metadata", kwargs={"run_id": "run_005", "metadata_patch": {"owner_id": "user_008", "owner_path": "src/game/network/multiplayer.cpp"}}),
        Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
        Action(name="set_build_triage_status", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
        Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "owner_id": "user_008", "owner_path": "src/game/network/multiplayer.cpp"}}),
        Action(name="get_build_run_details", kwargs={"run_id": "run_005"})
        ],
        outputs=[
        "Ownership persisted (user_008 for src/game/network/multiplayer.cpp); triage_status=manual_review recorded; run_005 details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_050",
        instruction=(
            "You normalize diagnostics for 'run_003' with a consistent classification snapshot. At completion, the run carries "
            "metadata.failure_category stored as {category:'compilation_issue'}; Windows symbolication for 'GameEngine.dll' from 'build_001' is attached; "
            "metadata.component='render_core'; and triage_status='in_progress' under the completed canonical automation "
            "'AUTO::automation::build_triage::run_003::canonical' whose outputs include triage_status 'in_progress'. You return refreshed "
            "details for 'run_003'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_003","automation_run_id":"AUTO::automation::build_triage::run_003::canonical"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id":"run_003","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="update_run_metadata", kwargs={"run_id":"run_003","metadata_patch":{"component":"render_core"}}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_003","triage_status":"in_progress"}),
            Action(name="set_build_failure_categorization", kwargs={"run_id":"run_003","category":"compilation_issue"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_003::canonical","status":"completed","outputs_json":{"triage_status":"in_progress"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_003"})
        ],
        outputs=[
            "run_003: metadata.failure_category stored as {category:'compilation_issue'}; symbolication attached; metadata.component=render_core; triage_status=in_progress captured via automation; details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_051",
        instruction=(
        "You advance a defensible triage record for build run 'run_005'. At completion, the run carries Windows symbolication "
        "for 'GameEngine.dll' from 'build_001', records the reproducible command 'make test-integration-linux', reflects "
        "triage_status 'manual_review', and the canonical automation 'AUTO::automation::build_triage::run_005::canonical' is "
        "completed with outputs that include failure_categorization 'integration_failure'. You return refreshed details for "
        "'run_005'. Use only these identifiers and values."
        ),
        actions=[
        Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_005", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
        Action(name="record_repro_command_for_run", kwargs={"run_id": "run_005", "command": "make test-integration-linux"}),
        Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_005", "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"}),
        Action(name="set_build_triage_status", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
        Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_005::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "failure_categorization": "integration_failure"}}),
        Action(name="get_build_run_details", kwargs={"run_id": "run_005"})
        ],
        outputs=[
        "run_005 symbolicated for GameEngine.dll; repro recorded; triage_status=manual_review; automation outputs include failure_categorization=integration_failure; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_052",
        instruction=(
            "You capture and persist regression evidence on 'run_001' in a triage‑ready, auditable form. At completion, the "
            "canonical automation 'AUTO::automation::build_triage::run_001::canonical' is completed with outputs including "
            "first_bad_commit 'abc999888777666', bisect_result 'commit_abc999', and triage_status 'in_progress'; the run has "
            "Windows symbolication for 'GameEngine.dll' from 'build_001' and records the reproducible command 'make test-windows-x64'. "
            "You return refreshed details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_001", "command": "make test-windows-x64"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "first_bad_commit": "abc999888777666", "bisect_result": "commit_abc999"}}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Regression evidence captured for run_001 (symbolication + repro). Automation outputs: first_bad_commit=abc999888777666, bisect_result=commit_abc999, triage_status=in_progress. Final run_001 details still show first_bad_commit=abc123def456789 and bisect_result=commit_abc123; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_053",
        instruction=(
            "You raise clear quality signals for 'run_007' and leave an audit trail. "
            "By completion, metadata includes at least {'priority':'high','platform_hint':'linux'}, "
            "a similar incident references 'run_006' with similarity_score 0.90, provenance shows a completed "
            "step 'signals_ingested', and triage reflects 'manual_review' with the canonical automation completed. "
            "Use only these identifiers and values."
        ),
        actions=[
            Action(name="update_run_metadata", kwargs={"run_id":"run_007","metadata_patch":{"priority":"high","platform_hint":"linux"}}),
            Action(name="append_similar_incident_to_run", kwargs={"run_id":"run_007","incident_run_id":"run_006","similarity_score":0.90}),
            Action(name="add_run_step", kwargs={"run_id":"run_007","step_id":"signals_ingested","name":"signals_ingested","status":"completed"}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_007","triage_status":"manual_review"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"triage_status":"manual_review"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_007"})
        ],
        outputs=["Signals present; similar incident run_006 (0.90); provenance step signals_ingested=completed; triage_status=manual_review; details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_054",
        instruction=(
            "You publish a targeted Windows performance snapshot and link it to triage. At completion, the fixed test run id is "
            "'AUTO::test_run::pipeline_perf_windows::175' for pipeline 'pipeline_perf_windows' with totals total=3, failed=0, skipped=0, "
            "passed=3, coverage_pct=92.4 and exactly these results—'FrameRateTest::SceneC' passed (duration_ms=1100), "
            "'MemoryUsageTest::SceneC' passed (700), 'LoadTimeTest::SceneC' passed (450); artifact 'build_001' metadata shows "
            "perf_baseline='2025-02' and regression_flag=false; and the canonical automation "
            "'AUTO::automation::build_triage::run_007::canonical' is completed with outputs including triage_status 'in_progress' and "
            "test_run_id 'AUTO::test_run::pipeline_perf_windows::175'. You return refreshed details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={"pipeline_id": "pipeline_perf_windows", "total": 3, "failed": 0, "skipped": 0, "passed": 3, "coverage_pct": 92.4}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "FrameRateTest::SceneC", "status": "passed", "duration_ms": 1100}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "MemoryUsageTest::SceneC", "status": "passed", "duration_ms": 700}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "LoadTimeTest::SceneC", "status": "passed", "duration_ms": 450}),
            Action(name="update_artifact_metadata", kwargs={"artifact_id": "build_001", "metadata_patch": {"perf_baseline": "2025-02", "regression_flag": False}}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_007", "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_007::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_007"})
        ],
        outputs=[
            "Perf snapshot recorded for AUTO::test_run::pipeline_perf_windows::175; build_001 patched. Automation outputs include triage_status=in_progress and test_run_id=AUTO::test_run::pipeline_perf_windows::175; final run_007 details show triage_status=manual_review; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_055",
        instruction=(
            "You validate and persist catalog context for the UI texture with reproducibility and triage traceability. "
            "By completion, 'assets/textures/ui/main_menu_bg.png' is registered as a 'texture' asset named 'main_menu_bg'; a QA result "
            "exists with validation_status 'passed', severity_max 'info', autofix_applied false; its catalog performance_rating is 'medium'; "
            "build run 'run_006' records the repro command 'scripts/validate_texture.sh --asset assets/textures/ui/main_menu_bg.png', "
            "has Windows symbolication for 'GameEngine.dll' from 'build_001', provenance shows completed steps 'asset_validation' and 'context_indexed', "
            "triage reflects 'manual_review' under the completed canonical automation 'AUTO::automation::build_triage::run_006::canonical'; and run metadata stores "
            "last_validated_asset='assets/textures/ui/main_menu_bg.png'. Return refreshed details for 'run_006'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="register_asset_in_catalog", kwargs={
                "asset_path":"assets/textures/ui/main_menu_bg.png","asset_type":"texture","asset_name":"main_menu_bg"
            }),
            Action(name="create_asset_qa_result", kwargs={
                "asset_path":"assets/textures/ui/main_menu_bg.png","asset_type":"texture",
                "validation_status":"passed","severity_max":"info","autofix_applied":False
            }),
            Action(name="update_asset_catalog_performance_rating", kwargs={
                "asset_path":"assets/textures/ui/main_menu_bg.png","performance_rating":"medium"
            }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id":"run_006","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"
            }),
            Action(name="record_repro_command_for_run", kwargs={
                "run_id":"run_006","command":"scripts/validate_texture.sh --asset assets/textures/ui/main_menu_bg.png"
            }),
            Action(name="add_run_step", kwargs={"run_id":"run_006","step_id":"asset_validation","name":"asset_validation","status":"completed"}),
            Action(name="add_run_step", kwargs={"run_id":"run_006","step_id":"context_indexed","name":"context_indexed","status":"completed"}),
            Action(name="start_automation_run", kwargs={
                "automation_type":"build_triage","input_ref":"run_006",
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed",
                "outputs_json":{"triage_status":"manual_review"}
            }),
            Action(name="update_run_metadata", kwargs={
                "run_id":"run_006","metadata_patch":{"last_validated_asset":"assets/textures/ui/main_menu_bg.png"}
            }),
            Action(name="get_build_run_details", kwargs={"run_id":"run_006"})
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
            "You consolidate an auditable triage dossier for 'run_001' with reproducibility, ownership, "
            "and artifact context. By completion, the run preserves the reproducible command "
            "'make build-linux-x64'; Windows symbolication for 'GameEngine.dll' from 'build_001' is "
            "attached; ownership is persisted as owner_id 'user_008' (team 'team_003'), ownership_type "
            "'file_owner', confidence_score 0.91 with owner_path 'src/game/network/multiplayer.cpp'; "
            "artifact 'build_002' is linked and its metadata records hotfix_candidate=true; a similar "
            "incident references 'run_006' with similarity_score 0.88; provenance shows completed steps "
            "'triage_fetch_artifacts' and 'owner_resolution'; and the run reflects triage_status "
            "'in_progress' under the completed canonical build_triage automation "
            "'AUTO::automation::build_triage::run_001::canonical' whose outputs include "
            "triage_status 'in_progress', owner_id 'user_008', owner_path 'src/game/network/multiplayer.cpp', "
            "and artifact_id 'build_002'. You return refreshed details for 'run_001'. "
            "Use only these identifiers and values."
        ),
        actions=[
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_001","automation_run_id":"AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id":"run_001","command":"make build-linux-x64"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id":"run_001","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),

            Action(name="persist_owner_to_run", kwargs={"run_id":"run_001","owner_id":"user_008","team_id":"team_003","owner_path":"src/game/network/multiplayer.cpp","ownership_type":"file_owner","confidence_score":0.91}),
            Action(name="link_artifact_to_run", kwargs={"run_id":"run_001","artifact_id":"build_002"}),
            Action(name="update_artifact_metadata", kwargs={"artifact_id":"build_002","metadata_patch":{"hotfix_candidate":True}}),

            Action(name="append_similar_incident_to_run", kwargs={"run_id":"run_001","incident_run_id":"run_006","similarity_score":0.88}),
            Action(name="add_run_step", kwargs={"run_id":"run_001","step_id":"triage_fetch_artifacts","name":"triage_fetch_artifacts","status":"completed"}),
            Action(name="add_run_step", kwargs={"run_id":"run_001","step_id":"owner_resolution","name":"owner_resolution","status":"completed"}),

            Action(name="set_build_triage_status", kwargs={"run_id":"run_001","triage_status":"in_progress"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_001::canonical","status":"completed","outputs_json":{"triage_status":"in_progress","owner_id":"user_008","owner_path":"src/game/network/multiplayer.cpp","artifact_id":"build_002"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_001"})
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
            "You finalize a deterministic performance record and expose it in build triage for 'run_007'. "
            "By completion, the fixed test run 'AUTO::test_run::pipeline_perf_windows::175' (pipeline 'pipeline_perf_windows') records totals total=3, failed=1, skipped=0, passed=2, "
            "coverage_pct initially 0.0 then updated to 0.72, with exactly these results—'FrameRateTest::SceneA' failed (1200), 'MemoryUsageTest::SceneA' passed (800), "
            "'LoadTimeTest::SceneA' passed (500); triage reflects 'in_progress' under the completed canonical automation "
            "'AUTO::automation::build_triage::run_007::canonical' with outputs including test_run_id 'AUTO::test_run::pipeline_perf_windows::175' and final_coverage_pct 0.72; "
            "and provenance shows 'perf_results_appended' completed. Return refreshed details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={
                "pipeline_id":"pipeline_perf_windows","total":3,"failed":1,"skipped":0,"passed":2,"coverage_pct":0.0
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"FrameRateTest::SceneA",
                "status":"failed","duration_ms":1200
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"MemoryUsageTest::SceneA",
                "status":"passed","duration_ms":800
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"LoadTimeTest::SceneA",
                "status":"passed","duration_ms":500
            }),
            Action(name="update_test_run_coverage", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175","coverage_pct":0.72
            }),
            Action(name="add_run_step", kwargs={
                "run_id":"run_007","step_id":"perf_results_appended","name":"perf_results_appended","status":"completed"
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type":"build_triage","input_ref":"run_007",
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed",
                "outputs_json":{"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","final_coverage_pct":0.72}
            }),
            Action(name="get_build_run_details", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "Perf results recorded and coverage=0.72; provenance step completed; triage_status=in_progress; automation outputs captured; run_007 details retrieved."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_058",
        instruction=(
            "You drive a multi-stage triage for 'run_007' consistent with CI failure workflows. "
            "By the end, the run is categorized 'performance_regression', first_bad_commit is 'abc123def456789' with bisect data "
            "(first_bad_commit 'abc123def456789', last_good_commit 'commit_prev111', confidence 0.97), the repro command "
            "'make performance-test-windows' is preserved, Windows symbolication for 'GameEngine.dll' from 'build_001' is attached, "
            "provenance shows completed steps 'log_ingested' and 'bisect_queued', and triage reflects 'in_progress' under the completed "
            "canonical automation 'AUTO::automation::build_triage::run_007::canonical'."
        ),
        actions=[
            Action(name="set_build_failure_categorization", kwargs={"run_id":"run_007","category":"performance_regression"}),
            Action(name="set_first_bad_commit_on_run", kwargs={"run_id":"run_007","commit_sha":"abc123def456789"}),
            Action(name="set_bisect_result_on_run", kwargs={
                "run_id":"run_007","first_bad_commit_sha":"abc123def456789",
                "last_good_commit_sha":"commit_prev111","confidence":0.97
            }),
            Action(name="record_repro_command_for_run", kwargs={"run_id":"run_007","command":"make performance-test-windows"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id":"run_007","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="add_run_step", kwargs={"run_id":"run_007","step_id":"log_ingested","name":"log_ingested","status":"completed"}),
            Action(name="add_run_step", kwargs={"run_id":"run_007","step_id":"bisect_queued","name":"bisect_queued","status":"completed"}),
            Action(name="start_automation_run", kwargs={
                "automation_type":"build_triage","input_ref":"run_007",
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical"
            }),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical",
                "status":"completed","outputs_json":{"triage_status":"in_progress"}
            }),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_007"})
        ],
        outputs=[
            "Categorized performance_regression; first_bad & bisect recorded; repro & symbolication present; provenance logged; triage_status=in_progress; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_059",
        instruction=(
        "You make symbolication and a targeted fix proposal available for 'run_006' while preserving traceability. At completion, "
        "the run carries Windows symbolication for 'GameEngine.dll' from 'build_001', fix_proposal_id is 'fix_021', run metadata "
        "includes {'regression': 'frame_time_spike'}, triage_status is 'in_progress', and the canonical automation "
        "'AUTO::automation::build_triage::run_006::canonical' is completed capturing that status. You return refreshed details for "
        "'run_006'. Use only these identifiers and values."
        ),
        actions=[
        Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_006", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
        Action(name="set_fix_proposal_on_run", kwargs={"run_id": "run_006", "fix_proposal_id": "fix_021"}),
        Action(name="update_run_metadata", kwargs={"run_id": "run_006", "metadata_patch": {"regression": "frame_time_spike"}}),
        Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_006", "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"}),
        Action(name="set_build_triage_status", kwargs={"run_id": "run_006", "triage_status": "in_progress"}),
        Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_006::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
        Action(name="get_build_run_details", kwargs={"run_id": "run_006"})
        ],
        outputs=["Symbolication linked; fix proposal fix_021 recorded; metadata patched; triage_status=in_progress; run_006 details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_060",
        instruction=(
            "You publish a Linux performance record with a fixed id and anchor it to triage for 'run_006'. "
            "At completion, 'AUTO::test_run::pipeline_perf_linux::001' (pipeline 'pipeline_perf_linux') records totals total=3, failed=1, skipped=0, passed=2 "
            "with exactly three results—'FrameRateTest::SceneA' failed (1250), 'MemoryUsageTest::SceneA' passed (780), 'LoadTimeTest::SceneA' passed (480); "
            "artifact 'build_001' shows perf_baseline '2025-03'; run_006 metadata stores performance_test_run_id "
            "'AUTO::test_run::pipeline_perf_linux::001'; provenance on run_006 shows 'evidence_ingested' completed."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={
                "pipeline_id":"pipeline_perf_linux","total":3,"failed":1,"skipped":0,"passed":2
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_linux::001","test_name":"FrameRateTest::SceneA",
                "status":"failed","duration_ms":1250
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_linux::001","test_name":"MemoryUsageTest::SceneA",
                "status":"passed","duration_ms":780
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_linux::001","test_name":"LoadTimeTest::SceneA",
                "status":"passed","duration_ms":480
            }),
            Action(name="update_artifact_metadata", kwargs={
                "artifact_id":"build_001","metadata_patch":{"perf_baseline":"2025-03"}
            }),
            Action(name="update_run_metadata", kwargs={
                "run_id":"run_006","metadata_patch":{"performance_test_run_id":"AUTO::test_run::pipeline_perf_linux::001"}
            }),
            Action(name="add_run_step", kwargs={
                "run_id":"run_006","step_id":"evidence_ingested","name":"evidence_ingested","status":"completed"
            }),
            Action(name="get_build_run_details", kwargs={"run_id":"run_006"})
        ],
        outputs=[
            "Linux perf run recorded; build_001 baseline set; run_006 metadata linked (performance_test_run_id) and evidence_ingested=completed; details retrieved."
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_061",
        instruction=(
            "You maintain an auditable triage snapshot for 'run_001'. At completion, the run reflects "
            "metadata priority='medium', first_bad_commit 'abc123def456789', and bisect_result 'commit_abc123'; "
            "triage_status is 'in_progress' tracked under the canonical automation "
            "'AUTO::automation::build_triage::run_001::canonical'. You return refreshed details for 'run_001'."
        ),
        actions=[
            Action(name="update_run_metadata", kwargs={"run_id": "run_001", "metadata_patch": {"priority": "medium"}}),
            Action(name="set_first_bad_commit_on_run", kwargs={"run_id": "run_001", "commit_sha": "abc123def456789"}),
            Action(name="set_bisect_result_on_run", kwargs={"run_id": "run_001", "bisect_result": "commit_abc123"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=["Run 'run_001' shows priority=medium, first_bad_commit=abc123def456789, bisect_result=commit_abc123, triage_status=in_progress (automation recorded)."]
    ),
    Task(
        annotator="0",
        user_id="qap_062",
        instruction=(
            "You stabilize CI context for 'run_001' with owner accountability and reproducibility. At completion, "
            "failed test evidence from 'test_run_002' is referenced; symbolicated stack for 'GameEngine.dll' "
            "from 'build_001' on 'windows' is attached; the reproducible command is 'make build-windows-x64'; "
            "ownership for 'src/game/engine/renderer.cpp' is persisted as owner_id 'user_001'; and triage_status "
            "is 'in_progress' recorded under 'AUTO::automation::build_triage::run_001::canonical'. You return refreshed details for 'run_001'."
        ),
        actions=[
            Action(name="list_failed_tests_for_run", kwargs={"test_run_id": "test_run_002"}),
            Action(name="map_path_to_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "owner_id": "user_001", "owner_path": "src/game/engine/renderer.cpp", "evidence_test_run": "test_run_002"}}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=["CI context stabilized for run_001: evidence linked, symbolication and repro present, owner persisted (user_001), triage_status=in_progress."]
    ),
    Task(
        annotator="0",
        user_id="qap_063",
        instruction=(
            "You validate and catalog the animation asset 'assets/animations/character/walk_cycle.fbx' and tie the work to 'run_006'. "
            "At completion, the catalog contains the asset named 'Walk Cycle'; QA 'qa_004' is promoted (resulting status passed with "
            "severity_max 'warning', autofix_applied true); the catalog performance_rating is 'medium'; and the canonical build_triage "
            "automation 'AUTO::automation::build_triage::run_006::canonical' is completed with outputs referencing the asset and results. "
            "You return refreshed details for 'run_006'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="register_asset_in_catalog", kwargs={"asset_path":"assets/animations/character/walk_cycle.fbx","asset_type":"animation","asset_name":"Walk Cycle"}),
            Action(name="promote_asset_autofix_to_pass", kwargs={"qa_id":"qa_004"}),
            Action(name="update_asset_catalog_performance_rating", kwargs={"asset_path":"assets/animations/character/walk_cycle.fbx","performance_rating":"medium"}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_006","automation_run_id":"AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed","outputs_json":{"asset_path":"assets/animations/character/walk_cycle.fbx","validation_status":"passed","performance_rating":"medium"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_006"})
        ],
        outputs=[
            "Asset registered; qa_004 promoted; performance_rating=medium; automation outputs recorded; run_006 details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_064",
        instruction=(
            "You keep symbolication and triage context current for 'run_001' under the canonical automation. At completion, "
            "symbolicated data for 'GameEngine.dll' from 'build_001' on 'windows' is attached to 'run_001'; triage_status is 'in_progress' "
            "and the automation 'AUTO::automation::build_triage::run_001::canonical' is completed. You return refreshed details for 'run_001'."
        ),
        actions=[
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=["Symbolication attached; triage_status=in_progress recorded and automation completed for run_001."]
    ),
    Task(
        annotator="0",
        user_id="qap_065",
        instruction=(
            "You gate unit‑test signals and connect them to triage for 'run_007'. "
            "By completion, the fixed test run id is 'AUTO::test_run::pipeline_unit_tests::001' for pipeline 'pipeline_unit_tests' with totals total=2, failed=0, skipped=0, passed=2, "
            "coverage_pct=76.2 and exactly two results—'MathUnitTest::MatrixOps' passed (120) and 'IOUnitTest::FileRead' passed (95); "
            "artifact 'build_002' metadata records qa_baseline='2025-04' and test_suite='smoke'; the run reflects triage_status 'in_progress' under the completed canonical automation "
            "'AUTO::automation::build_triage::run_007::canonical' whose outputs include triage_status 'in_progress' and test_run_id 'AUTO::test_run::pipeline_unit_tests::001'; "
            "run metadata stores unit_test_run_id='AUTO::test_run::pipeline_unit_tests::001'; and provenance shows 'unit_test_evidence_ingest' completed. "
            "Return refreshed details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={
                "pipeline_id":"pipeline_unit_tests","total":2,"failed":0,"skipped":0,"passed":2,"coverage_pct":76.2
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_unit_tests::001","test_name":"MathUnitTest::MatrixOps",
                "status":"passed","duration_ms":120
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_unit_tests::001","test_name":"IOUnitTest::FileRead",
                "status":"passed","duration_ms":95
            }),
            Action(name="update_artifact_metadata", kwargs={
                "artifact_id":"build_002","metadata_patch":{"qa_baseline":"2025-04","test_suite":"smoke"}
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type":"build_triage","input_ref":"run_007",
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed",
                "outputs_json":{"triage_status":"in_progress","test_run_id":"AUTO::test_run::pipeline_unit_tests::001"}
            }),
            Action(name="update_run_metadata", kwargs={
                "run_id":"run_007","metadata_patch":{"unit_test_run_id":"AUTO::test_run::pipeline_unit_tests::001"}
            }),
            Action(name="add_run_step", kwargs={
                "run_id":"run_007","step_id":"unit_test_evidence_ingest","name":"unit_test_evidence_ingest","status":"completed"
            }),
            Action(name="get_build_run_details", kwargs={"run_id":"run_007"})
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
            "You curate a deterministic performance snapshot and bind it to triage context for 'run_001'. At completion, the canonical "
            "test run id 'AUTO::test_run::pipeline_perf_windows::175' for pipeline 'pipeline_perf_windows' reflects totals total=3, failed=1, "
            "skipped=0, passed=2 with exactly 'FrameRateTest::Hallway' failed (1300ms), 'MemoryUsageTest::Intro' passed (700ms), "
            "'LoadTimeTest::MainMenu' passed (450ms), and coverage_pct=80.0; run 'run_001' metadata records "
            "performance_test_run_id='AUTO::test_run::pipeline_perf_windows::175'; and the canonical automation "
            "'AUTO::automation::build_triage::run_001::canonical' is completed with outputs including triage_status 'in_progress', "
            "test_run_id 'AUTO::test_run::pipeline_perf_windows::175', and final_coverage_pct 80.0. You return refreshed details for 'run_001'."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={"pipeline_id": "pipeline_perf_windows", "total": 3, "failed": 1, "skipped": 0, "passed": 2, "coverage_pct": 0.0}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "FrameRateTest::Hallway", "status": "failed", "duration_ms": 1300}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "MemoryUsageTest::Intro", "status": "passed", "duration_ms": 700}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "LoadTimeTest::MainMenu", "status": "passed", "duration_ms": 450}),
            Action(name="update_test_run_coverage", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "coverage_pct": 80.0}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress", "test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "final_coverage_pct": 80.0}}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="update_run_metadata", kwargs={"run_id": "run_001", "metadata_patch": {"performance_test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=["Perf snapshot bound to run_001 (test_run ::175 with 3 results, coverage=80.0); metadata linked; triage_status=in_progress; automation outputs captured; details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_067",
        instruction=(
            "You maintain a reproducible triage record for 'run_001'. At completion, the run reflects first_bad_commit 'abc123def456789', "
            "failure_categorization 'compilation_issue', and two completed steps—'collect-logs' (2025-01-27T10:16:00Z–2025-01-27T10:17:00Z) "
            "and 'summarize-failure' (2025-01-27T10:17:00Z–2025-01-27T10:18:00Z); triage_status 'in_progress' is recorded under "
            "'AUTO::automation::build_triage::run_001::canonical'. You return refreshed details for 'run_001'."
        ),
        actions=[
            Action(name="set_first_bad_commit_on_run", kwargs={"run_id": "run_001", "commit_sha": "abc123def456789"}),
            Action(name="set_build_failure_categorization", kwargs={"run_id": "run_001", "category": "compilation_issue"}),
            Action(name="add_run_step", kwargs={"run_id": "run_001", "step_id": "collect-logs", "name": "collect-logs", "status": "success", "started_at": "2025-01-27T10:16:00Z", "ended_at": "2025-01-27T10:17:00Z"}),
            Action(name="add_run_step", kwargs={"run_id": "run_001", "step_id": "summarize-failure", "name": "summarize-failure", "status": "success", "started_at": "2025-01-27T10:17:00Z", "ended_at": "2025-01-27T10:18:00Z"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=["run_001 updated with first_bad_commit, categorization, steps recorded; triage_status=in_progress under canonical automation; details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_068",
        instruction=(
            "You make 'run_005' accountable and reproducible for a networking issue. At completion, failed‑test evidence from "
            "'test_run_002' is referenced; symbolication for 'GameEngine.dll' from 'build_001' on 'windows' is attached; the reproducible "
            "command 'make test-integration-linux' is recorded; ownership for 'src/game/network/multiplayer.cpp' is persisted as "
            "owner_id 'user_008', team 'team_003', ownership_type 'file_owner', confidence_score 0.92; provenance shows a completed "
            "step 'owner_resolution'; and triage_status is 'manual_review' under the completed canonical automation "
            "'AUTO::automation::build_triage::run_005::canonical' whose outputs include triage_status 'manual_review', owner_id 'user_008', "
            "owner_path 'src/game/network/multiplayer.cpp', and evidence_test_run 'test_run_002'. You return refreshed details for 'run_005'. "
            "Use only these identifiers and values."
        ),
        actions=[
            Action(name="list_failed_tests_for_run", kwargs={"test_run_id":"test_run_002"}),
            Action(name="map_path_to_owner", kwargs={"file_path":"src/game/network/multiplayer.cpp"}),
            Action(name="persist_owner_to_run", kwargs={"run_id":"run_005","owner_id":"user_008","team_id":"team_003","ownership_type":"file_owner","confidence_score":0.92,"owner_path":"src/game/network/multiplayer.cpp"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id":"run_005","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id":"run_005","command":"make test-integration-linux"}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_005","automation_run_id":"AUTO::automation::build_triage::run_005::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_005","triage_status":"manual_review"}),
            Action(name="add_run_step", kwargs={"run_id":"run_005","step_id":"owner_resolution","name":"owner_resolution","status":"completed"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_005::canonical","status":"completed","outputs_json":{"triage_status":"manual_review","owner_id":"user_008","owner_path":"src/game/network/multiplayer.cpp","evidence_test_run":"test_run_002"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_005"})
        ],
        outputs=[
            "Ownership persisted to user_008 (team_003, file_owner, confidence=0.92); evidence test_run_002 noted; symbolication and repro recorded; triage_status=manual_review; owner_resolution=completed; automation outputs captured; run_005 details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_069",
        instruction=(
            "You manage symbol availability and triage linkage for Netcode. At completion, symbol info for module 'Netcode.dll' on 'windows' "
            "from 'build_004' is registered with pdb_uri 'https://symbols.techcorp.com/build_004/Netcode.pdb' and status 'available'; "
            "symbol 'symbol_004' is deprecated; artifact 'build_004' is linked to 'run_006'; and triage_status 'in_progress' is recorded under "
            "'AUTO::automation::build_triage::run_006::canonical'. You return refreshed details for 'run_006'."
        ),
        actions=[
            Action(name="register_symbol", kwargs={"build_id": "build_004", "module_name": "Netcode.dll", "platform": "windows", "pdb_uri": "https://symbols.techcorp.com/build_004/Netcode.pdb", "status": "available"}),
            Action(name="deprecate_symbol", kwargs={"symbol_id": "symbol_004"}),
            Action(name="link_artifact_to_run", kwargs={"run_id": "run_006", "artifact_id": "build_004"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_006", "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_006", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_006::canonical", "status": "completed", "outputs_json": {"triage_status": "in_progress"}}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_006"})
        ],
        outputs=["Symbol registered and prior symbol deprecated; build_004 linked; triage_status=in_progress recorded for run_006; details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_070",
        instruction=(
            "You resolve accountable ownership and reproducibility for 'run_001'. At completion, 'src/game/ai/pathfinding.cpp' ownership "
            "is persisted as owner_id 'user_007'; symbolicated stack for 'GameEngine.dll' from 'build_001' on 'windows' is attached; the reproducible "
            "command 'make build-windows-x64' is recorded; and triage_status is 'manual_review' tracked under "
            "'AUTO::automation::build_triage::run_001::canonical'. You return refreshed details for 'run_001'."
        ),
        actions=[
            Action(name="map_path_to_owner", kwargs={"file_path": "src/game/ai/pathfinding.cpp"}),
            Action(name="persist_owner_to_run", kwargs={"run_id": "run_001", "owner_id": "user_007"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "manual_review"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id": "AUTO::automation::build_triage::run_001::canonical", "status": "completed", "outputs_json": {"triage_status": "manual_review", "owner_id": "user_007"}}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=["Owner persisted (user_007), symbolication and repro recorded; triage_status=manual_review under canonical automation; run_001 details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_071",
        instruction=(
            "You stabilize and document build run 'run_002' with a reproducible, auditable record. "
            "At completion, 'run_002' has Windows symbolication for 'GameEngine.dll' from 'build_001' attached; "
            "the run’s metadata.failure_category is 'compilation_issue' and metadata.first_bad_commit is 'abc123def456789'; "
            "the run reflects triage_status 'in_progress'; the canonical automation "
            "'AUTO::automation::build_triage::run_002::canonical' is completed with outputs mirroring that state "
            "(failure_categorization 'compilation_issue', first_bad_commit 'abc123def456789', triage_status 'in_progress'); "
            "and provenance shows a completed step 'triage_capture'. You return refreshed details for 'run_002'. "
            "Use only these identifiers and values."
        ),
        actions=[
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_002",
                "automation_run_id": "AUTO::automation::build_triage::run_002::canonical"
            }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id": "run_002",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="update_run_metadata", kwargs={
                "run_id": "run_002",
                "metadata_patch": {
                    "failure_category": "compilation_issue",
                    "first_bad_commit": "abc123def456789"
                }
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_002", "triage_status": "in_progress"}),
            Action(name="add_run_step", kwargs={"run_id": "run_002", "step_id": "triage_capture", "name": "triage_capture", "status": "completed"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_002::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "in_progress",
                    "failure_categorization": "compilation_issue",
                    "first_bad_commit": "abc123def456789"
                }
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_002"})
        ],
        outputs=[
            "run_002: symbolication attached; metadata.failure_category=compilation_issue; metadata.first_bad_commit=abc123def456789; triage_status=in_progress; step triage_capture=completed; automation recorded; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_072",
        instruction=(
            "You make build run 'run_003' owner‑accountable with an auditable record. "
            "At completion, 'src/game/network/multiplayer.cpp' resolves to and is persisted as owner_id 'user_008' on the run; "
            "the run reflects triage_status 'manual_review'; and the canonical automation "
            "'AUTO::automation::build_triage::run_003::canonical' is completed with outputs showing triage_status and owner_path. "
            "You return refreshed details for 'run_003'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="map_path_to_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="persist_owner_to_run", kwargs={"run_id": "run_003", "owner_id": "user_008", "owner_path": "src/game/network/multiplayer.cpp"}),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_003",
                "automation_run_id": "AUTO::automation::build_triage::run_003::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_003", "triage_status": "manual_review"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_003::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "manual_review", "owner_path": "src/game/network/multiplayer.cpp"}
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_003"})
        ],
        outputs=[
            "Ownership persisted to user_008 for src/game/network/multiplayer.cpp; triage_status=manual_review; automation completed; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_073",
        instruction=(
            "You produce a triage-ready, evidence-rich record for 'run_006'. "
            "At completion, the run stores 'python validate_assets.py', carries Windows symbolication for 'GameEngine.dll' from 'build_001', "
            "links artifacts at 'https://artifacts.techcorp.com/build_004/', metadata includes {'validation_suite':'assets_fast'}, provenance shows "
            "completed steps 'log_ingested' and 'repro_verified', a similar incident references 'run_004' (similarity_score 0.83), and "
            "triage reflects 'manual_review' under the completed canonical automation 'AUTO::automation::build_triage::run_006::canonical'."
        ),
        actions=[
            Action(name="record_repro_command_for_run", kwargs={"run_id":"run_006","command":"python validate_assets.py"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id":"run_006","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="link_artifact_to_run", kwargs={"run_id":"run_006","artifacts_uri":"https://artifacts.techcorp.com/build_004/"}),
            Action(name="update_run_metadata", kwargs={"run_id":"run_006","metadata_patch":{"validation_suite":"assets_fast"}}),
            Action(name="append_similar_incident_to_run", kwargs={"run_id":"run_006","incident_run_id":"run_004","similarity_score":0.83}),
            Action(name="add_run_step", kwargs={"run_id":"run_006","step_id":"log_ingested","name":"log_ingested","status":"completed"}),
            Action(name="add_run_step", kwargs={"run_id":"run_006","step_id":"repro_verified","name":"repro_verified","status":"completed"}),
            Action(name="start_automation_run", kwargs={
                "automation_type":"build_triage","input_ref":"run_006",
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical",
                "status":"completed","outputs_json":{"triage_status":"manual_review"}
            }),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_006"})
        ],
        outputs=[
            "Repro, symbolication, artifacts, metadata, provenance, and incident context captured; triage_status=manual_review; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_074",
        instruction=(
            "You consolidate a deterministic performance report and attach it to CI triage. "
            "At completion, 'AUTO::test_run::pipeline_perf_windows::175' for 'pipeline_perf_windows' records totals total=3, failed=1, skipped=0, passed=2 with results "
            "'PhysicsStabilityTest::SceneB' failed (1400), 'AIPathfindingTest::SceneC' passed (900), 'LoadingScreenTest::SceneD' passed (600), and coverage 82.5. "
            "Triage for 'run_003' shows triage_status 'in_progress' with the canonical automation completed whose outputs include "
            "performance_test_run_id 'AUTO::test_run::pipeline_perf_windows::175'; run metadata stores the same id."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={"pipeline_id":"pipeline_perf_windows","total":3,"failed":1,"skipped":0,"passed":2}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"PhysicsStabilityTest::SceneB","status":"failed","duration_ms":1400}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"AIPathfindingTest::SceneC","status":"passed","duration_ms":900}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"LoadingScreenTest::SceneD","status":"passed","duration_ms":600}),
            Action(name="update_test_run_coverage", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","coverage_pct":82.5}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_003","automation_run_id":"AUTO::automation::build_triage::run_003::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_003","triage_status":"in_progress"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_003::canonical","status":"completed","outputs_json":{"triage_status":"in_progress","performance_test_run_id":"AUTO::test_run::pipeline_perf_windows::175","coverage_pct":82.5}}),
            Action(name="update_run_metadata", kwargs={"run_id":"run_003","metadata_patch":{"performance_test_run_id":"AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_003"})
        ],
        outputs=["Perf run anchored to run_003 (coverage 82.5); triage_status=in_progress; automation completed; details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_075",
        instruction=(
            "You capture gating and incident context for 'run_001' with a clear audit trail. "
            "At completion, run_001 metadata reflects {'coverage_gate':'waived'}; metadata.similar_incidents contains exactly one entry for "
            "{'incident_run_id':'run_006'}; metadata.first_bad_commit is 'abc123def456789'; and the run reflects triage_status 'manual_review' "
            "under the completed canonical automation 'AUTO::automation::build_triage::run_001::canonical' (whose outputs include triage_status 'manual_review' "
            "and first_bad_commit 'abc123def456789'). Provenance shows a completed step 'triage_context'. You return refreshed details for 'run_001'. "
            "Use only these identifiers and values."
        ),
        actions=[
            Action(name="update_run_metadata", kwargs={
                "run_id": "run_001",
                "metadata_patch": {
                    "coverage_gate": "waived",
                    "similar_incidents": [{"incident_run_id": "run_006"}],
                    "first_bad_commit": "abc123def456789"
                }
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "manual_review"}),
            Action(name="add_run_step", kwargs={"run_id": "run_001", "step_id": "triage_context", "name": "triage_context", "status": "completed"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "manual_review",
                    "first_bad_commit": "abc123def456789",
                    "similar_incident": "run_006"
                }
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "run_001: metadata.coverage_gate=waived; metadata.similar_incidents includes run_006; metadata.first_bad_commit=abc123def456789; triage_status=manual_review; step triage_context=completed; automation recorded; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_076",
        instruction=(
            "You formalize triage tracking for 'run_001' so status and provenance are explicit. "
            "At completion, run metadata reflects priority 'high' and impact 'build_blocker'; provenance includes step 'triage_ownership' "
            "(2025-01-27T12:31:00Z–2025-01-27T12:33:00Z) with status 'success'; and triage_status is 'in_progress' under the completed canonical automation "
            "'AUTO::automation::build_triage::run_001::canonical'. You return refreshed details for 'run_001'."
        ),
        actions=[
            Action(name="update_run_metadata", kwargs={"run_id": "run_001", "metadata_patch": {"priority": "high", "impact": "build_blocker"}}),
            Action(name="add_run_step", kwargs={"run_id": "run_001", "step_id": "triage_ownership", "name": "triage_ownership", "status": "success", "started_at": "2025-01-27T12:31:00Z", "ended_at": "2025-01-27T12:33:00Z"}),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "in_progress"}
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Run metadata updated (priority=high, impact=build_blocker); step triage_ownership recorded; triage_status=in_progress; automation completed; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_077",
        instruction=(
            "You make the texture’s QA and catalog state auditable and tie it to CI triage with clear signals. "
            "By completion, 'assets/textures/environment/hero_character_diffuse.png' is in the catalog typed 'texture' with asset_name 'hero_character_diffuse'; "
            "a QA record exists with validation_status 'failed', severity_max 'issue', autofix_applied true; the catalog performance_rating is 'low'; "
            "build run 'run_006' reflects triage_status 'manual_review' under the completed canonical automation 'AUTO::automation::build_triage::run_006::canonical' "
            "whose outputs reference the asset_path and performance_rating; Windows symbolication for 'GameEngine.dll' from 'build_001' (windows) is attached; "
            "and provenance shows 'asset_validation' completed. Return refreshed details for 'run_006'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="register_asset_in_catalog", kwargs={
                "asset_path":"assets/textures/environment/hero_character_diffuse.png","asset_type":"texture","asset_name":"hero_character_diffuse"
            }),
            Action(name="create_asset_qa_result", kwargs={
                "asset_path":"assets/textures/environment/hero_character_diffuse.png","asset_type":"texture",
                "validation_status":"failed","severity_max":"issue","autofix_applied":True
            }),
            Action(name="update_asset_catalog_performance_rating", kwargs={
                "asset_path":"assets/textures/environment/hero_character_diffuse.png","performance_rating":"low"
            }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id":"run_006","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type":"build_triage","input_ref":"run_006",
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed",
                "outputs_json":{
                    "triage_status":"manual_review",
                    "asset_path":"assets/textures/environment/hero_character_diffuse.png","validation_status":"failed","performance_rating":"low"
                }
            }),
            Action(name="add_run_step", kwargs={
                "run_id":"run_006","step_id":"asset_validation","name":"asset_validation","status":"completed"
            }),
            Action(name="get_build_run_details", kwargs={"run_id":"run_006"})
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
            "You finalize a deterministic performance record and anchor it to triage. "
            "At completion, the fixed test run 'AUTO::test_run::pipeline_perf_windows::175' for 'pipeline_perf_windows' records totals "
            "(total=3, failed=1, skipped=0, passed=2) with exactly three results—'FrameRateTest::MainCity' failed (1200), "
            "'MemoryUsageTest::Raid' passed (800), and 'LoadTimeTest::Startup' passed (500)—and coverage 0.66. "
            "Build run 'run_001' reflects triage_status 'in_progress' under the completed canonical automation "
            "'AUTO::automation::build_triage::run_001::canonical', whose outputs include test_run_id and final_coverage_pct; "
            "run metadata stores performance_test_run_id 'AUTO::test_run::pipeline_perf_windows::175'. You return refreshed details for 'run_001'."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={"pipeline_id": "pipeline_perf_windows", "total": 3, "failed": 1, "skipped": 0, "passed": 2, "coverage_pct": 0.0}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "FrameRateTest::MainCity", "status": "failed", "duration_ms": 1200}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "MemoryUsageTest::Raid", "status": "passed", "duration_ms": 800}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "test_name": "LoadTimeTest::Startup", "status": "passed", "duration_ms": 500}),
            Action(name="update_test_run_coverage", kwargs={"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "coverage_pct": 0.66}),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {"test_run_id": "AUTO::test_run::pipeline_perf_windows::175", "final_coverage_pct": 0.66, "triage_status": "in_progress"}
            }),
            Action(name="update_run_metadata", kwargs={"run_id": "run_001", "metadata_patch": {"performance_test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Perf evidence recorded (coverage 0.66) and anchored to run_001; triage_status=in_progress; automation completed; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_079",
        instruction=(
            "You stabilize CI for 'run_001' with clear ownership and reproducibility. "
            "At completion, failed‑test evidence from 'test_run_002' is referenced; Windows symbolication for 'GameEngine.dll' from 'build_001' "
            "is attached; the reproducible command 'make build-windows-x64' is recorded; ownership for 'src/game/engine/renderer.cpp' is mapped; "
            "and the run reflects triage_status 'in_progress' under the completed canonical automation "
            "'AUTO::automation::build_triage::run_001::canonical' whose outputs include owner_path and evidence_test_run. "
            "You return refreshed details for 'run_001'."
        ),
        actions=[
            Action(name="list_failed_tests_for_run", kwargs={"test_run_id": "test_run_002"}),
            Action(name="map_path_to_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_001", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "in_progress", "owner_path": "src/game/engine/renderer.cpp", "evidence_test_run": "test_run_002"}
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Ownership mapped, symbolication attached, repro recorded; triage_status=in_progress; automation completed; details retrieved for run_001."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_080",
        instruction=(
            "You stabilize CI for 'run_007' with reproducible evidence and ownership context. "
            "At completion, failed‑test evidence from 'test_run_002' is referenced; Windows symbolication for 'GameEngine.dll' from 'build_001' "
            "is attached; the reproducible command 'make performance-test-windows' is recorded; ownership for "
            "'src/game/engine/renderer.cpp' is mapped; and the run reflects triage_status 'manual_review' under the completed canonical automation "
            "'AUTO::automation::build_triage::run_007::canonical' whose outputs include owner_path and evidence_test_run. "
            "You return refreshed details for 'run_007'."
        ),
        actions=[
            Action(name="list_failed_tests_for_run", kwargs={"test_run_id": "test_run_002"}),
            Action(name="map_path_to_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id": "run_007", "build_id": "build_001", "module_name": "GameEngine.dll", "platform": "windows"}),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_007", "command": "make performance-test-windows"}),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_007",
                "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_007", "triage_status": "manual_review"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_007::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "manual_review", "owner_path": "src/game/engine/renderer.cpp", "evidence_test_run": "test_run_002"}
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_007"})
        ],
        outputs=[
            "Evidence and symbolication attached; repro recorded; triage_status=manual_review; automation completed; details retrieved for run_007."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_081",
        instruction=(
            "You surface a model-asset intake QA outcome and anchor it to CI triage for 'run_006'. "
            "By the end, the model asset 'assets/models/environment/castle_tower.fbx' has a QA result (validation_status 'failed', severity_max 'issue', "
            "autofix_applied true), its catalog performance_rating is 'high', and triage for 'run_006' reflects 'manual_review' with the canonical automation "
            "outputs echoing that asset path/state."
        ),
        actions=[
            Action(name="create_asset_qa_result", kwargs={"asset_path":"assets/models/environment/castle_tower.fbx","asset_type":"model","validation_status":"failed","severity_max":"issue","autofix_applied":True}),
            Action(name="update_asset_catalog_performance_rating", kwargs={"asset_path":"assets/models/environment/castle_tower.fbx","performance_rating":"high"}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_006","automation_run_id":"AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed","outputs_json":{"asset_path":"assets/models/environment/castle_tower.fbx","validation_status":"failed","performance_rating":"high"}})
        ],
        outputs=["Asset QA persisted; rating=high; run_006 triage_status=manual_review."]
    ),
    Task(
        annotator="0",
        user_id="qap_082",
        instruction=(
            "You anchor a deterministic triage snapshot for 'run_005'. "
            "At completion, Windows symbolication for 'GameEngine.dll' from 'build_001' is attached; "
            "the reproducible command 'make test-integration-linux' is recorded; ownership for "
            "'src/game/network/multiplayer.cpp' is persisted as owner_id 'user_008' with ownership_type 'file_owner', "
            "confidence_score 0.9, and owner_path 'src/game/network/multiplayer.cpp'; run metadata includes "
            "evidence_test_run='test_run_002'; and triage_status is 'manual_review' under the completed canonical "
            "build_triage automation 'AUTO::automation::build_triage::run_005::canonical' whose outputs include "
            "triage_status 'manual_review', owner_id 'user_008', owner_path 'src/game/network/multiplayer.cpp', and "
            "evidence_test_run 'test_run_002'. You return refreshed details for 'run_005'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="persist_owner_to_run", kwargs={
                "run_id": "run_005",
                "owner_id": "user_008",
                "owner_path": "src/game/network/multiplayer.cpp",
                "ownership_type": "file_owner",
                "confidence_score": 0.9
            }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id": "run_005",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="record_repro_command_for_run", kwargs={
                "run_id": "run_005",
                "command": "make test-integration-linux"
            }),
            Action(name="update_run_metadata", kwargs={
                "run_id": "run_005",
                "metadata_patch": {"evidence_test_run": "test_run_002"}
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_005",
                "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_005::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "manual_review",
                    "owner_id": "user_008",
                    "owner_path": "src/game/network/multiplayer.cpp",
                    "evidence_test_run": "test_run_002"
                }
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_005"})
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
            "You register and quality‑gate the texture while anchoring its CI context to 'run_006'. "
            "At completion, the catalog contains 'assets/textures/environment/castle_wall_diffuse.png' typed 'texture' "
            "named 'Castle Wall Diffuse'; a QA record exists with validation_status 'passed', severity_max 'warning', "
            "autofix_applied true; the catalog performance_rating is 'medium'; and 'run_006' reflects triage_status "
            "'manual_review' under the canonical build_triage automation "
            "'AUTO::automation::build_triage::run_006::canonical'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="register_asset_in_catalog", kwargs={
                "asset_path": "assets/textures/environment/castle_wall_diffuse.png",
                "asset_type": "texture",
                "asset_name": "Castle Wall Diffuse"
            }),
            Action(name="create_asset_qa_result", kwargs={
                "asset_path": "assets/textures/environment/castle_wall_diffuse.png",
                "asset_type": "texture",
                "validation_status": "passed",
                "severity_max": "warning",
                "autofix_applied": True
            }),
            Action(name="update_asset_catalog_performance_rating", kwargs={
                "asset_path": "assets/textures/environment/castle_wall_diffuse.png",
                "performance_rating": "medium"
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_006",
                "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_006", "triage_status": "manual_review"}),
            Action(name="complete_automation_run", kwargs={
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
            "You consolidate a deterministic performance report for 'pipeline_perf_windows' using the fixed test run "
            "id 'AUTO::test_run::pipeline_perf_windows::175'. At completion, totals are total=3, failed=1, skipped=0, "
            "passed=2 with coverage_pct=0.8; the run holds exactly three results—'PhysicsStabilityTest::SceneB' failed (1400), "
            "'AIPathfindingTest::SceneC' passed (900), and 'LoadingScreenTest::SceneD' passed (600); 'run_007' reflects "
            "triage_status 'in_progress' under the canonical automation 'AUTO::automation::build_triage::run_007::canonical' "
            "whose outputs include {'test_run_id':'AUTO::test_run::pipeline_perf_windows::175','final_coverage_pct':0.8}; "
            "and run metadata stores performance_test_run_id 'AUTO::test_run::pipeline_perf_windows::175'. "
            "You return refreshed details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={
                "pipeline_id": "pipeline_perf_windows",
                "total": 3, "failed": 1, "skipped": 0, "passed": 2, "coverage_pct": 0.8
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "PhysicsStabilityTest::SceneB",
                "status": "failed",
                "duration_ms": 1400
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "AIPathfindingTest::SceneC",
                "status": "passed",
                "duration_ms": 900
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "LoadingScreenTest::SceneD",
                "status": "passed",
                "duration_ms": 600
            }),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_007", "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_007", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_007::canonical",
                "status": "completed",
                "outputs_json": {
                    "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                    "final_coverage_pct": 0.8
                }
            }),
            Action(name="update_run_metadata", kwargs={"run_id": "run_007", "metadata_patch": {"performance_test_run_id": "AUTO::test_run::pipeline_perf_windows::175"}}),
            Action(name="get_build_run_details", kwargs={"run_id": "run_007"})
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
            "You stabilize CI for 'run_001' by anchoring failed‑test evidence, Windows symbolication, repro, and ownership, "
            "and you track the effort under the canonical automation. At completion, Windows symbolication for 'GameEngine.dll' "
            "from 'build_001' is attached; the reproducible command 'make build-windows-x64' is recorded; ownership is persisted "
            "as owner_id 'user_001' for owner_path 'src/game/engine/renderer.cpp' with ownership_type 'file_owner' and confidence_score 0.9; "
            "run metadata stores evidence_test_run 'test_run_002'; and 'run_001' reflects triage_status 'in_progress' under "
            "'AUTO::automation::build_triage::run_001::canonical' whose outputs include "
            "{'triage_status':'in_progress','owner_id':'user_001','owner_path':'src/game/engine/renderer.cpp','evidence_test_run':'test_run_002'}. "
            "You return refreshed details for 'run_001'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="list_failed_tests_for_run", kwargs={"test_run_id": "test_run_002"}),
            Action(name="persist_owner_to_run", kwargs={
                "run_id": "run_001",
                "owner_id": "user_001",
                "owner_path": "src/game/engine/renderer.cpp",
                "ownership_type": "file_owner",
                "confidence_score": 0.9
            }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id": "run_001",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(name="update_run_metadata", kwargs={"run_id": "run_001", "metadata_patch": {"evidence_test_run": "test_run_002"}}),
            Action(name="start_automation_run", kwargs={"automation_type": "build_triage", "input_ref": "run_001", "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "in_progress",
                    "owner_id": "user_001",
                    "owner_path": "src/game/engine/renderer.cpp",
                    "evidence_test_run": "test_run_002"
                }
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
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
            "You extend the deterministic performance suite and capture triage context for 'run_007'. "
            "By completion, exactly three results are appended to 'AUTO::test_run::pipeline_perf_windows::175'—"
            "'ShaderCompileTest::BatchA' failed (2000), 'StreamingIOTest::SetA' passed (950), 'MemoryLeakDetection::Level1' passed (1100); "
            "the run is categorized 'performance_regression', records the repro command 'make performance-test-windows', "
            "has Windows symbolication for 'GameEngine.dll' from 'build_001', provenance shows 'perf_results_appended' completed, "
            "and triage reflects 'in_progress' under the completed canonical automation 'AUTO::automation::build_triage::run_007::canonical' "
            "whose outputs include {'appended_test_results_count':3,'test_run_id':'AUTO::test_run::pipeline_perf_windows::175'}. "
            "Return refreshed details for 'run_007'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175",
                "test_name":"ShaderCompileTest::BatchA","status":"failed","duration_ms":2000
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175",
                "test_name":"StreamingIOTest::SetA","status":"passed","duration_ms":950
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175",
                "test_name":"MemoryLeakDetection::Level1","status":"passed","duration_ms":1100
            }),
            Action(name="record_repro_command_for_run", kwargs={"run_id":"run_007","command":"make performance-test-windows"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id":"run_007","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"
            }),
            Action(name="set_build_failure_categorization", kwargs={"run_id":"run_007","category":"performance_regression"}),
            Action(name="add_run_step", kwargs={"run_id":"run_007","step_id":"perf_results_appended","name":"perf_results_appended","status":"completed"}),
            Action(name="start_automation_run", kwargs={
                "automation_type":"build_triage","input_ref":"run_007",
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed",
                "outputs_json":{"appended_test_results_count":3,"test_run_id":"AUTO::test_run::pipeline_perf_windows::175"}
            }),
            Action(name="get_build_run_details", kwargs={"run_id":"run_007"})
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
            "You stabilize CI for 'run_005' by capturing reproducibility, symbolication, and ownership, and by recording an auditable trail. "
            "At completion, Windows symbolication for 'GameEngine.dll' from 'build_001' is attached; the reproducible command "
            "'make test-integration-linux' is recorded; ownership is persisted as owner_id 'user_008' for owner_path "
            "'src/game/network/multiplayer.cpp' with ownership_type 'file_owner' and confidence_score 0.9; run metadata pins "
            "evidence_test_run='test_run_002'; and triage_status is 'manual_review' under "
            "'AUTO::automation::build_triage::run_005::canonical' whose outputs mirror that context. You return refreshed details for 'run_005'."
        ),
        actions=[
            Action(name="persist_owner_to_run", kwargs={
                "run_id": "run_005",
                "owner_id": "user_008",
                "owner_path": "src/game/network/multiplayer.cpp",
                "ownership_type": "file_owner",
                "confidence_score": 0.9
            }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id": "run_005",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="record_repro_command_for_run", kwargs={
                "run_id": "run_005",
                "command": "make test-integration-linux"
            }),
            Action(name="update_run_metadata", kwargs={
                "run_id": "run_005",
                "metadata_patch": {"evidence_test_run": "test_run_002"}
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_005",
                "automation_run_id": "AUTO::automation::build_triage::run_005::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_005", "triage_status": "manual_review"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_005::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "manual_review",
                    "owner_id": "user_008",
                    "owner_path": "src/game/network/multiplayer.cpp",
                    "evidence_test_run": "test_run_002"
                }
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_005"})
        ],
        outputs=[
            "Triage recorded: manual_review; Windows symbolication attached; repro preserved; owner persisted; evidence pinned; details refreshed."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_088",
        instruction=(
            "You document triage execution on 'run_004' and capture it under the canonical automation. "
            "At completion, provenance includes step 'symbolication_setup' (success, 2025-01-27T12:10:00Z→2025-01-27T12:12:00Z) "
            "and step 'owner_mapping' (success, 2025-01-27T12:12:00Z→2025-01-27T12:14:00Z); and 'run_004' reflects "
            "triage_status 'in_progress' under 'AUTO::automation::build_triage::run_004::canonical' whose outputs record "
            "documented_steps ['symbolication_setup','owner_mapping']."
        ),
        actions=[
            Action(name="add_run_step", kwargs={
                "run_id": "run_004",
                "step_id": "symbolication_setup",
                "name": "symbolication_setup",
                "status": "success",
                "started_at": "2025-01-27T12:10:00Z",
                "ended_at": "2025-01-27T12:12:00Z"
            }),
            Action(name="add_run_step", kwargs={
                "run_id": "run_004",
                "step_id": "owner_mapping",
                "name": "owner_mapping",
                "status": "success",
                "started_at": "2025-01-27T12:12:00Z",
                "ended_at": "2025-01-27T12:14:00Z"
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_004",
                "automation_run_id": "AUTO::automation::build_triage::run_004::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_004", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={
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
            "You register and quality‑gate the texture and anchor its outcome to CI triage for 'run_006'. "
            "At completion, the catalog contains 'assets/textures/props/torch_fire_diffuse.png' typed 'texture' named "
            "'Torch Fire Diffuse'; a QA record exists with validation_status 'passed', severity_max 'warning', "
            "autofix_applied true; the catalog performance_rating is 'medium'; and 'run_006' reflects triage_status "
            "'manual_review' under 'AUTO::automation::build_triage::run_006::canonical'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="register_asset_in_catalog", kwargs={
                "asset_path": "assets/textures/props/torch_fire_diffuse.png",
                "asset_type": "texture",
                "asset_name": "Torch Fire Diffuse"
            }),
            Action(name="create_asset_qa_result", kwargs={
                "asset_path": "assets/textures/props/torch_fire_diffuse.png",
                "asset_type": "texture",
                "validation_status": "passed",
                "severity_max": "warning",
                "autofix_applied": True
            }),
            Action(name="update_asset_catalog_performance_rating", kwargs={
                "asset_path": "assets/textures/props/torch_fire_diffuse.png",
                "performance_rating": "medium"
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_006",
                "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_006", "triage_status": "manual_review"}),
            Action(name="complete_automation_run", kwargs={
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
            "You finalize a deterministic performance report for 'pipeline_perf_windows' on the fixed test run "
            "'AUTO::test_run::pipeline_perf_windows::175'. At completion, totals are total=3, failed=1, skipped=0, "
            "passed=2 with coverage_pct=0.7; the run holds 'FrameRateTest::SceneA' failed (1200), "
            "'MemoryUsageTest::SceneA' passed (800), and 'LoadTimeTest::SceneA' passed (500); 'run_001' reflects "
            "triage_status 'in_progress' under 'AUTO::automation::build_triage::run_001::canonical' whose outputs include "
            "{'test_run_id':'AUTO::test_run::pipeline_perf_windows::175','final_coverage_pct':0.7}; and "
            "run metadata stores performance_test_run_id 'AUTO::test_run::pipeline_perf_windows::175'."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={
                "pipeline_id": "pipeline_perf_windows",
                "total": 3, "failed": 1, "skipped": 0, "passed": 2, "coverage_pct": 0.0
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "FrameRateTest::SceneA",
                "status": "failed",
                "duration_ms": 1200
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "MemoryUsageTest::SceneA",
                "status": "passed",
                "duration_ms": 800
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "test_name": "LoadTimeTest::SceneA",
                "status": "passed",
                "duration_ms": 500
            }),
            Action(name="update_test_run_coverage", kwargs={
                "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                "coverage_pct": 0.7
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {
                    "test_run_id": "AUTO::test_run::pipeline_perf_windows::175",
                    "final_coverage_pct": 0.7
                }
            }),
            Action(name="update_run_metadata", kwargs={
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
            "You register two UI assets and surface their CI context for 'run_006'. "
            "At completion, the animation 'assets/animations/character/walk_cycle.fbx' "
            "is in the catalog as asset_name 'Character Walk Cycle'; the texture "
            "'assets/textures/ui/health_bar.png' is registered as asset_name 'Health Bar', "
            "has a QA record (validation_status 'passed', severity_max 'warning', "
            "autofix_applied true), and its catalog performance_rating is 'medium'; "
            "the canonical build_triage automation 'AUTO::automation::build_triage::run_006::canonical' "
            "is completed with outputs reporting triage_status 'manual_review'; and the run reflects "
            "triage_status 'manual_review'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="register_asset_in_catalog", kwargs={"asset_path":"assets/animations/character/walk_cycle.fbx","asset_type":"animation","asset_name":"Character Walk Cycle"}),
            Action(name="register_asset_in_catalog", kwargs={"asset_path":"assets/textures/ui/health_bar.png","asset_type":"texture","asset_name":"Health Bar"}),
            Action(name="create_asset_qa_result", kwargs={"asset_path":"assets/textures/ui/health_bar.png","asset_type":"texture","validation_status":"passed","severity_max":"warning","autofix_applied":True}),
            Action(name="update_asset_catalog_performance_rating", kwargs={"asset_path":"assets/textures/ui/health_bar.png","performance_rating":"medium"}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_006","automation_run_id":"AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed","outputs_json":{"triage_status":"manual_review"}}),
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
            "You make 'run_001' symbol-aware and link its evidence while it’s tracked in triage. "
            "At completion, the Windows symbol for 'Renderer.dll' on build 'build_001' is registered with pdb_uri "
            "'https://symbols.techcorp.com/build_001/Renderer.pdb' (status 'available'); artifacts at "
            "'https://artifacts.techcorp.com/build_001/' are linked to the run; and triage reflects 'in_progress' under "
            "the completed canonical automation 'AUTO::automation::build_triage::run_001::canonical'."
        ),
        actions=[
            Action(name="register_symbol", kwargs={
                "build_id":"build_001","module_name":"Renderer.dll","platform":"windows",
                "pdb_uri":"https://symbols.techcorp.com/build_001/Renderer.pdb","status":"available"
            }),
            Action(name="link_artifact_to_run", kwargs={
                "run_id":"run_001","artifacts_uri":"https://artifacts.techcorp.com/build_001/"
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type":"build_triage","input_ref":"run_001",
                "automation_run_id":"AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_001","triage_status":"in_progress"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_001::canonical",
                "status":"completed","outputs_json":{"triage_status":"in_progress"}
            }),
            Action(name="get_build_run_details", kwargs={"run_id":"run_001"})
        ],
        outputs=[
            "Renderer symbols registered; artifacts linked; triage_status=in_progress; automation recorded; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_093",
        instruction=(
            "You establish accountable ownership for a Linux integration issue on 'run_006'. "
            "At completion, the owner resolved from 'src/game/network/multiplayer.cpp' is persisted to the run as owner_id 'user_008' "
            "with owner_path 'src/game/network/multiplayer.cpp'; the canonical automation 'AUTO::automation::build_triage::run_006::canonical' "
            "is completed with outputs reporting triage_status 'manual_review' and owner_path 'src/game/network/multiplayer.cpp'; "
            "and the run reflects triage_status 'manual_review'. Return refreshed details for 'run_006'."
        ),
        actions=[
            Action(name="map_path_to_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="persist_owner_to_run", kwargs={
                "run_id": "run_006",
                "owner_id": "user_008",
                "owner_path": "src/game/network/multiplayer.cpp"
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_006",
                "automation_run_id": "AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_006", "triage_status": "manual_review"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_006::canonical",
                "status": "completed",
                "outputs_json": {"triage_status": "manual_review", "owner_path": "src/game/network/multiplayer.cpp"}
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_006"})
        ],
        outputs=[
            "Ownership for src/game/network/multiplayer.cpp persisted to user_008; triage_status=manual_review; automation completed; details retrieved"
        ]
    ),

    Task(
        annotator="0",
        user_id="qap_094",
        instruction=(
            "You stabilize CI for 'run_007' by capturing reproducibility, symbolication, and ownership context. "
            "At completion, the run records 'make performance-test-windows'; symbolication for 'GameEngine.dll' from 'build_001' on 'windows' is attached; "
            "ownership is persisted as owner_id 'user_001' for owner_path 'src/game/engine/renderer.cpp'; the canonical automation "
            "'AUTO::automation::build_triage::run_007::canonical' is completed with outputs reporting triage_status 'manual_review', owner_id 'user_001', "
            "owner_path 'src/game/engine/renderer.cpp', and evidence_test_run 'test_run_002'; and the run reflects triage_status 'manual_review'. "
            "Return refreshed details for 'run_007'."
        ),
        actions=[
            Action(name="persist_owner_to_run", kwargs={
                "run_id": "run_007",
                "owner_id": "user_001",
                "owner_path": "src/game/engine/renderer.cpp"
            }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id": "run_007",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_007", "command": "make performance-test-windows"}),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_007",
                "automation_run_id": "AUTO::automation::build_triage::run_007::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_007", "triage_status": "manual_review"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_007::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "manual_review",
                    "owner_id": "user_001",
                    "owner_path": "src/game/engine/renderer.cpp",
                    "evidence_test_run": "test_run_002"
                }
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_007"})
        ],
        outputs=[
            "Repro recorded; symbolication attached; ownership persisted (user_001 for renderer.cpp); triage_status=manual_review; automation completed; details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_095",
        instruction=(
            "You reflect an end-to-end texture QA ingest for 'assets/textures/environment/castle_gate_diffuse.png' into CI. "
            "At completion, the texture is registered as asset_name 'Castle Gate Diffuse', has QA (validation_status 'failed', severity_max 'issue', autofix_applied true), "
            "catalog performance_rating 'low', and the canonical triage record for 'run_006' is completed in 'manual_review' state echoing the asset’s path/state."
        ),
        actions=[
            Action(name="register_asset_in_catalog", kwargs={"asset_path":"assets/textures/environment/castle_gate_diffuse.png","asset_type":"texture","asset_name":"Castle Gate Diffuse"}),
            Action(name="create_asset_qa_result", kwargs={"asset_path":"assets/textures/environment/castle_gate_diffuse.png","asset_type":"texture","validation_status":"failed","severity_max":"issue","autofix_applied":True}),
            Action(name="update_asset_catalog_performance_rating", kwargs={"asset_path":"assets/textures/environment/castle_gate_diffuse.png","performance_rating":"low"}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_006","automation_run_id":"AUTO::automation::build_triage::run_006::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_006","triage_status":"manual_review"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_006::canonical","status":"completed","outputs_json":{"triage_status":"manual_review","asset_path":"assets/textures/environment/castle_gate_diffuse.png","validation_status":"failed","performance_rating":"low"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_006"})
        ],
        outputs=["Texture registered with QA; catalog rating=low; run_006 triage_status=manual_review captured; details retrieved."]
    ),
    Task(
        annotator="0",
        user_id="qap_096",
        instruction=(
            "You record a QA failure for 'assets/textures/environment/rock_albedo.png' and finalize its catalog impact while tracking triage for 'run_006'. "
            "By completion, the texture is registered as asset_name 'Rock Albedo'; a QA record exists with validation_status 'failed', severity_max 'issue', autofix_applied true; "
            "the catalog performance_rating is 'high'; the run records the repro command 'scripts/qa_texture.sh --asset assets/textures/environment/rock_albedo.png', "
            "has Windows symbolication for 'GameEngine.dll' from 'build_001', provenance shows completed steps 'asset_validation' and 'catalog_sync', "
            "and triage reflects 'in_progress' under the completed canonical automation 'AUTO::automation::build_triage::run_006::canonical'. "
            "Return refreshed details for 'run_006'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="register_asset_in_catalog", kwargs={
                "asset_path":"assets/textures/environment/rock_albedo.png","asset_type":"texture","asset_name":"Rock Albedo"
            }),
            Action(name="create_asset_qa_result", kwargs={
                "asset_path":"assets/textures/environment/rock_albedo.png","asset_type":"texture",
                "validation_status":"failed","severity_max":"issue","autofix_applied":True
            }),
            Action(name="update_asset_catalog_performance_rating", kwargs={
                "asset_path":"assets/textures/environment/rock_albedo.png","performance_rating":"high"
            }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id":"run_006","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"
            }),
            Action(name="record_repro_command_for_run", kwargs={
                "run_id":"run_006","command":"scripts/qa_texture.sh --asset assets/textures/environment/rock_albedo.png"
            }),
            Action(name="add_run_step", kwargs={"run_id":"run_006","step_id":"asset_validation","name":"asset_validation","status":"completed"}),
            Action(name="add_run_step", kwargs={"run_id":"run_006","step_id":"catalog_sync","name":"catalog_sync","status":"completed"}),
            Action(name="start_automation_run", kwargs={
                "automation_type":"build_triage","input_ref":"run_006",
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_006","triage_status":"in_progress"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id":"AUTO::automation::build_triage::run_006::canonical",
                "status":"completed","outputs_json":{"triage_status":"in_progress"}
            }),
            Action(name="get_build_run_details", kwargs={"run_id":"run_006"})
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
            "You stabilize CI for 'run_001' by capturing reproducibility, symbolication, and ownership evidence. "
            "At completion, the run records 'make build-windows-x64'; symbolication for 'GameEngine.dll' from 'build_001' on 'windows' is attached; "
            "run metadata pins evidence_test_run='test_run_002'; the canonical automation 'AUTO::automation::build_triage::run_001::canonical' is completed "
            "with outputs reporting triage_status 'in_progress', owner_id 'user_001', owner_path 'src/game/engine/renderer.cpp', and evidence_test_run 'test_run_002'; "
            "and the run reflects triage_status 'in_progress'. Return refreshed details for 'run_001'."
        ),
        actions=[
            Action(name="map_path_to_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="update_run_metadata", kwargs={
                "run_id": "run_001",
                "metadata_patch": {"evidence_test_run": "test_run_002"}
            }),
            Action(name="attach_symbolicated_stack_to_run", kwargs={
                "run_id": "run_001",
                "build_id": "build_001",
                "module_name": "GameEngine.dll",
                "platform": "windows"
            }),
            Action(name="record_repro_command_for_run", kwargs={"run_id": "run_001", "command": "make build-windows-x64"}),
            Action(name="start_automation_run", kwargs={
                "automation_type": "build_triage",
                "input_ref": "run_001",
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={"run_id": "run_001", "triage_status": "in_progress"}),
            Action(name="complete_automation_run", kwargs={
                "automation_run_id": "AUTO::automation::build_triage::run_001::canonical",
                "status": "completed",
                "outputs_json": {
                    "triage_status": "in_progress",
                    "owner_id": "user_001",
                    "owner_path": "src/game/engine/renderer.cpp",
                    "evidence_test_run": "test_run_002"
                }
            }),
            Action(name="get_build_run_details", kwargs={"run_id": "run_001"})
        ],
        outputs=[
            "Repro recorded; symbolication attached; evidence pinned; triage_status=in_progress with ownership context; automation completed; details retrieved"
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_098",
        instruction=(
            "You consolidate deterministic performance evidence for 'pipeline_perf_windows' and surface it into build triage for 'run_001'. "
            "At completion, the fixed test run 'AUTO::test_run::pipeline_perf_windows::175' contains exactly three results—"
            "'GPUDriverStability::NVScene' passed (700), 'DiskThroughputTest::SeqRead' passed (450), and "
            "'ThreadingContention::AIJobs' failed (1600); its coverage is updated to 0.66; the canonical build_triage automation "
            "'AUTO::automation::build_triage::run_001::canonical' is completed with outputs including "
            "test_run_id 'AUTO::test_run::pipeline_perf_windows::175' and final_coverage_pct 0.66; and the run reflects "
            "triage_status 'in_progress'. Use only these identifiers and values."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={
                "pipeline_id": "pipeline_perf_windows",
                "total": 3, "failed": 1, "skipped": 0, "passed": 2, "coverage_pct": 0.66
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175",
                "test_name":"GPUDriverStability::NVScene","status":"passed","duration_ms":700
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175",
                "test_name":"DiskThroughputTest::SeqRead","status":"passed","duration_ms":450
            }),
            Action(name="add_test_result_to_run", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175",
                "test_name":"ThreadingContention::AIJobs","status":"failed","duration_ms":1600
            }),
            Action(name="update_test_run_coverage", kwargs={
                "test_run_id":"AUTO::test_run::pipeline_perf_windows::175","coverage_pct":0.66
            }),
            Action(name="start_automation_run", kwargs={
                "automation_type":"build_triage","input_ref":"run_001",
                "automation_run_id":"AUTO::automation::build_triage::run_001::canonical"
            }),
            Action(name="set_build_triage_status", kwargs={
                "run_id":"run_001","triage_status":"in_progress"
            }),
            Action(name="complete_automation_run", kwargs={
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
            "You persist code ownership for 'src/game/engine/renderer.cpp' on 'run_001' and surface symbolication and triage status. "
            "At completion, the run holds owner_id 'user_001' with owner_path 'src/game/engine/renderer.cpp'; Windows symbolication for "
            "'GameEngine.dll' from 'build_001' is attached; the canonical build_triage automation "
            "'AUTO::automation::build_triage::run_001::canonical' is completed with outputs reporting triage_status 'manual_review' and "
            "owner_id 'user_001'; and the run reflects triage_status 'manual_review'. You return refreshed details for 'run_001'. "
            "Use only these identifiers and values."
        ),
        actions=[
            Action(name="persist_owner_to_run", kwargs={"run_id":"run_001","owner_id":"user_001","owner_path":"src/game/engine/renderer.cpp"}),
            Action(name="attach_symbolicated_stack_to_run", kwargs={"run_id":"run_001","build_id":"build_001","module_name":"GameEngine.dll","platform":"windows"}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_001","automation_run_id":"AUTO::automation::build_triage::run_001::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_001","triage_status":"manual_review"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_001::canonical","status":"completed","outputs_json":{"triage_status":"manual_review","owner_id":"user_001"}}),
            Action(name="get_build_run_details", kwargs={"run_id":"run_001"}),
        ],
        outputs=[
            "Ownership persisted (owner_id=user_001, owner_path=src/game/engine/renderer.cpp); symbolication attached; triage complete; details retrieved."
        ]
    ),
    Task(
        annotator="0",
        user_id="qap_100",
        instruction=(
            "You finalize a Windows performance snapshot and make it actionable in triage for 'run_007'. "
            "By the end, 'AUTO::test_run::pipeline_perf_windows::175' holds totals total=3, failed=1, skipped=0, passed=2 with exactly three results—"
            "'FrameRateTest::SceneA' failed (1200), 'MemoryUsageTest::SceneA' passed (800), 'LoadTimeTest::SceneA' passed (500)—and coverage is 0.78. "
            "Triage for 'run_007' shows triage_status 'in_progress' with the canonical automation completed, whose outputs include "
            "test_run_id 'AUTO::test_run::pipeline_perf_windows::175' and final_coverage_pct 0.78. Use only these identifiers and values."
        ),
        actions=[
            Action(name="create_test_run_summary", kwargs={"pipeline_id":"pipeline_perf_windows","total":3,"failed":1,"skipped":0,"passed":2}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"FrameRateTest::SceneA","status":"failed","duration_ms":1200}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"MemoryUsageTest::SceneA","status":"passed","duration_ms":800}),
            Action(name="add_test_result_to_run", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","test_name":"LoadTimeTest::SceneA","status":"passed","duration_ms":500}),
            Action(name="update_test_run_coverage", kwargs={"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","coverage_pct":0.78}),
            Action(name="start_automation_run", kwargs={"automation_type":"build_triage","input_ref":"run_007","automation_run_id":"AUTO::automation::build_triage::run_007::canonical"}),
            Action(name="set_build_triage_status", kwargs={"run_id":"run_007","triage_status":"in_progress"}),
            Action(name="complete_automation_run", kwargs={"automation_run_id":"AUTO::automation::build_triage::run_007::canonical","status":"completed","outputs_json":{"test_run_id":"AUTO::test_run::pipeline_perf_windows::175","final_coverage_pct":0.78}})
        ],
        outputs=["Test run totals/results recorded and coverage=0.78; run_007 triage_status=in_progress; automation completed."]
    ),
]
