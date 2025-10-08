from tau_bench.types import Action, Task


TASKS = [
    Task(
        annotator="0",
        user_id="task_001",
        instruction=(
            "Handle CI triage for the game-engine pipeline. Address the issue in the failed Windows build run_001 on branch feature/new-renderer at commit abc123def456789 by implementing the CI failure triage policy and employing deterministic templates throughout. Afterward, return the draft PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_001", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "build-windows-x64"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_001"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_001"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "abc123def456789"}),
            Action(name="RunBisect", kwargs={"run_id": "run_001", "suspects": [{"ref": "abc123def456789"}], "test_target": "build-windows-x64"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_001", "logs_uri": "artifact://logs/run_001", "first_bad_commit": "abc123def456789"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_001", "patch_id": "FP-run_001", "message": "auto tentative fix for run run_001"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_001", "base": "feature/new-renderer", "title": "auto fix build break run_001", "body": "summary for run run_001", "run_id": "run_001"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_001", "description": "Automated triage for run_001", "run_id": "run_001", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "build-windows-x64"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_001"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_002",
        instruction=(
            "Conduct CI triage for the game-engine pipeline. For the unsuccessful run run_003 on branch feature/new-renderer at commit abc123def456789 (job test-unit-windows), apply the standard failure triage policy to preserve context, extract signals, identify suspects from the commit’s changes, perform bisection, stage a fix using templates, create the draft PR and ticket via deterministic templates, validate, document, and provide the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_003"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_003"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "abc123def456789"}),
            Action(name="RunBisect", kwargs={"run_id": "run_003", "suspects": [{"ref": "abc123def456789"}], "test_target": "test-unit-windows"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_003", "logs_uri": "artifact://logs/run_003", "first_bad_commit": "abc123def456789"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "message": "auto tentative fix for run run_003"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "title": "auto fix build break run_003", "body": "summary for run run_003", "run_id": "run_003"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "test-unit-windows"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_003",
        instruction=(
            "Manage CI triage for the game-engine pipeline. In the event of a failed run, run_005, on branch feature/new-renderer at commit def456abc123789 (job test-integration-linux), utilize the triage policy employing deterministic templates and provide the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_005"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_005"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "def456abc123789"}),
            Action(name="RunBisect", kwargs={"run_id": "run_005", "suspects": [{"ref": "def456abc123789"}], "test_target": "test-integration-linux"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_005", "logs_uri": "artifact://logs/run_005", "first_bad_commit": "def456abc123789"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "message": "auto tentative fix for run run_005"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "title": "auto fix build break run_005", "body": "summary for run run_005", "run_id": "run_005"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "test-integration-linux"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_004",
        instruction=(
            "Oversee CI triage for the game-engine pipeline. When run run_007 fails on branch feature/new-renderer at commit abc123def456789 (job performance-test-windows), implement the triage policy using deterministic templates and submit the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_007"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_007"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "abc123def456789"}),
            Action(name="RunBisect", kwargs={"run_id": "run_007", "suspects": [{"ref": "abc123def456789"}], "test_target": "performance-test-windows"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_007", "first_bad_commit": "abc123def456789"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "message": "auto tentative fix for run run_007"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "title": "auto fix build break run_007", "body": "summary for run run_007", "run_id": "run_007"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "performance-test-windows"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_005",
        instruction=(
            "Oversee CI triage for the game-engine pipeline. In the event of a failed run run_010 on the feature/new-renderer branch at commit abc123def456789 (job deploy-staging-windows), implement the triage policy using deterministic templates and provide the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_010", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "deploy-staging-windows"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_010"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_010"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "abc123def456789"}),
            Action(name="RunBisect", kwargs={"run_id": "run_010", "suspects": [{"ref": "abc123def456789"}], "test_target": "deploy-staging-windows"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_010", "first_bad_commit": "abc123def456789"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_010", "patch_id": "FP-run_010", "message": "auto tentative fix for run run_010"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_010", "base": "feature/new-renderer", "title": "auto fix build break run_010", "body": "summary for run run_010", "run_id": "run_010"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_010", "description": "Automated triage for run_010", "run_id": "run_010", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "deploy-staging-windows"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_010"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_006",
        instruction=(
            "Supervise CI triage for the game-engine pipeline. For the recent failed run run_011 on the feature/new-renderer branch at commit abc123def456789 (job build-windows-x64), execute the triage policy utilizing deterministic templates and convey the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_011", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "build-windows-x64"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_011"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_011"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "abc123def456789"}),
            Action(name="RunBisect", kwargs={"run_id": "run_011", "suspects": [{"ref": "abc123def456789"}], "test_target": "build-windows-x64"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_011", "first_bad_commit": "abc123def456789"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_011"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_011", "patch_id": "FP-run_011", "message": "auto tentative fix for run run_011"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_011", "base": "feature/new-renderer", "title": "auto fix build break run_011", "body": "summary for run run_011", "run_id": "run_011"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_011", "description": "Automated triage for run_011", "run_id": "run_011", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "build-windows-x64"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_011"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_007",
        instruction=(
            "Handle CI triage for the game-engine pipeline. For the unsuccessful run run_012 on branch feature/new-renderer at commit def456abc123789 (job test-unit-windows), apply the triage policy using deterministic templates and provide the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_012", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-unit-windows"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_012"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_012"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "def456abc123789"}),
            Action(name="RunBisect", kwargs={"run_id": "run_012", "suspects": [{"ref": "def456abc123789"}], "test_target": "test-unit-windows"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_012", "first_bad_commit": "def456abc123789"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_012"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_012", "patch_id": "FP-run_012", "message": "auto tentative fix for run run_012"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_012", "base": "feature/new-renderer", "title": "auto fix build break run_012", "body": "summary for run run_012", "run_id": "run_012"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_012", "description": "Automated triage for run_012", "run_id": "run_012", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "test-unit-windows"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_012"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_008",
        instruction=(
            "Oversee CI triage for the game-engine pipeline. Regarding the failed run run_013 on branch feature/new-renderer at commit def456abc123789 (job build-linux-x64), use the triage policy with deterministic templates and deliver the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_013", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "build-linux-x64"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_013"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_013"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "def456abc123789"}),
            Action(name="RunBisect", kwargs={"run_id": "run_013", "suspects": [{"ref": "def456abc123789"}], "test_target": "build-linux-x64"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_013", "first_bad_commit": "def456abc123789"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_013"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_013", "patch_id": "FP-run_013", "message": "auto tentative fix for run run_013"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_013", "base": "feature/new-renderer", "title": "auto fix build break run_013", "body": "summary for run run_013", "run_id": "run_013"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_013", "description": "Automated triage for run_013", "run_id": "run_013", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "build-linux-x64"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_013"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_009",
        instruction=(
            "Handle the CI triage for the game-engine pipeline. In the case of failed run run_014 on branch feature/new-renderer at commit ghi789def456abc (job build-macos-arm64), employ the triage policy using deterministic templates and provide the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_014", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "ghi789def456abc", "job_name": "build-macos-arm64"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_014"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_014"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:ghi789def456abc:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "ghi789def456abc"}),
            Action(name="RunBisect", kwargs={"run_id": "run_014", "suspects": [{"ref": "ghi789def456abc"}], "test_target": "build-macos-arm64"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_014", "first_bad_commit": "ghi789def456abc"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_014"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_014", "patch_id": "FP-run_014", "message": "auto tentative fix for run run_014"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_014", "base": "feature/new-renderer", "title": "auto fix build break run_014", "body": "summary for run run_014", "run_id": "run_014"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_014", "description": "Automated triage for run_014", "run_id": "run_014", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "build-macos-arm64"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_014"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),


    Task(
        annotator="0",
        user_id="task_010",
        instruction=(
            "Oversee CI triage for the asset pipeline. For the failed run run_006 on branch feature/new-assets at commit jkl012ghi789def (job validate-assets), utilize the triage policy with deterministic templates and share the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_006", "status": "failure", "repo": "game-assets", "branch": "feature/new-assets", "commit_sha": "jkl012ghi789def", "job_name": "validate-assets"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_006"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_006"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:jkl012ghi789def:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "jkl012ghi789def"}),
            Action(name="RunBisect", kwargs={"run_id": "run_006", "suspects": [{"ref": "jkl012ghi789def"}], "test_target": "validate-assets"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_006", "first_bad_commit": "jkl012ghi789def"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/new-assets", "run_id": "run_006"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_006", "patch_id": "FP-run_006", "message": "auto tentative fix for run run_006"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_006", "base": "feature/new-assets", "title": "auto fix build break run_006", "body": "summary for run run_006", "run_id": "run_006"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_006", "description": "Automated triage for run_006", "run_id": "run_006", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "validate-assets"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_006"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_011",
        instruction=(
            "Oversee CI crash triage for the game-engine pipeline. Regarding failed run run_015 on branch feature/physics-revamp at commit mno345jkl678pqr (job build-windows-x64), deterministically triage the failure according to domain policy using only database-driven values: link to prior incidents when applicable, prepare a draft PR and linked ticket, validate, record the automation run, and provide the PR number. Do not invent identifiers."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_015", "status": "failure", "repo": "game-engine", "branch": "feature/physics-revamp", "commit_sha": "mno345jkl678pqr", "job_name": "build-windows-x64"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_015"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_015"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:mno345jkl678pqr:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "mno345jkl678pqr"}),
            Action(name="RunBisect", kwargs={"run_id": "run_015", "suspects": [], "test_target": "build-windows-x64"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_015", "logs_uri": "artifact://logs/run_015", "first_bad_commit": "mno345jkl678pqr"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/physics-revamp", "run_id": "run_015"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_015", "patch_id": "FP-run_015", "message": "auto tentative fix for run run_015"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_015", "base": "feature/physics-revamp", "title": "auto fix build break run_015", "body": "summary for run run_015", "run_id": "run_015"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_015", "description": "Automated triage for run_015", "run_id": "run_015", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "build-windows-x64"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_015"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_012",
        instruction=(
            "Responsible for CI crash triage for the game-engine pipeline. For failed run run_016 on branch feature/physics-revamp at commit mno345jkl678pqr (job test-unit-windows), carry out deterministic crash symbolication and incident linking, initiate a draft PR and ticket, validate, record, and deliver the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_016", "status": "failure", "repo": "game-engine", "branch": "feature/physics-revamp", "commit_sha": "mno345jkl678pqr", "job_name": "test-unit-windows"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_016"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_016"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:mno345jkl678pqr:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "mno345jkl678pqr"}),
            Action(name="RunBisect", kwargs={"run_id": "run_016", "suspects": [{"ref": "mno345jkl678pqr"}], "test_target": "test-unit-windows"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_016", "logs_uri": "artifact://logs/run_016", "first_bad_commit": "mno345jkl678pqr"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/physics-revamp", "run_id": "run_016"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_016", "patch_id": "FP-run_016", "message": "auto tentative fix for run run_016"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_016", "base": "feature/physics-revamp", "title": "auto fix build break run_016", "body": "summary for run run_016", "run_id": "run_016"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_016", "description": "Automated triage for run_016", "run_id": "run_016", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "test-unit-windows"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_016"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_013",
        instruction=(
            "Handle the CI crash triage for the game-engine pipeline. For the unsuccessful run run_017 on branch feature/ai-navigation at commit stu901vwx234yz0 (job test-integration-linux), carry out deterministic symbolication and incident linking, draft a PR and connected ticket, validate, document, and provide the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_017", "status": "failure", "repo": "game-engine", "branch": "feature/ai-navigation", "commit_sha": "stu901vwx234yz0", "job_name": "test-integration-linux"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_017"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_017"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:stu901vwx234yz0:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "stu901vwx234yz0"}),
            Action(name="RunBisect", kwargs={"run_id": "run_017", "suspects": [{"ref": "stu901vwx234yz0"}], "test_target": "test-integration-linux"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_017", "logs_uri": "artifact://logs/run_017", "first_bad_commit": "stu901vwx234yz0"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/ai-navigation", "run_id": "run_017"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_017", "patch_id": "FP-run_017", "message": "auto tentative fix for run run_017"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_017", "base": "feature/ai-navigation", "title": "auto fix build break run_017", "body": "summary for run run_017", "run_id": "run_017"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_017", "description": "Automated triage for run_017", "run_id": "run_017", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "test-integration-linux"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_017"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_014",
        instruction=(
            "Manage the CI crash triage for the game-engine pipeline. For the failed run run_018 on branch feature/ai-navigation at commit stu901vwx234yz0 (job build-linux-x64), execute symbolicating and incident linking deterministically, prepare a draft PR and associated ticket, validate, note, and present the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_018", "status": "failure", "repo": "game-engine", "branch": "feature/ai-navigation", "commit_sha": "stu901vwx234yz0", "job_name": "build-linux-x64"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_018"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_018"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:stu901vwx234yz0:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "stu901vwx234yz0"}),
            Action(name="RunBisect", kwargs={"run_id": "run_018", "suspects": [{"ref": "stu901vwx234yz0"}], "test_target": "build-linux-x64"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_018", "logs_uri": "artifact://logs/run_018", "first_bad_commit": "stu901vwx234yz0"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/ai-navigation", "run_id": "run_018"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_018", "patch_id": "FP-run_018", "message": "auto tentative fix for run run_018"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_018", "base": "feature/ai-navigation", "title": "auto fix build break run_018", "body": "summary for run run_018", "run_id": "run_018"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_018", "description": "Automated triage for run_018", "run_id": "run_018", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "build-linux-x64"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_018"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_015",
        instruction=(
            "Handle CI crash triage for the game-engine pipeline. For the unsuccessful run run_019 on branch feature/render-optim at commit abc111def222ghi (job build-macos-arm64), symbolicate and link incidents in a deterministic manner, draft a PR and associated ticket, validate, document, and provide the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_019", "status": "failure", "repo": "game-engine", "branch": "feature/render-optim", "commit_sha": "abc111def222ghi", "job_name": "build-macos-arm64"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_019"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_019"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:abc111def222ghi:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "abc111def222ghi"}),
            Action(name="RunBisect", kwargs={"run_id": "run_019", "suspects": [{"ref": "abc111def222ghi"}], "test_target": "build-macos-arm64"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_019", "logs_uri": "artifact://logs/run_019", "first_bad_commit": "abc111def222ghi"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/render-optim", "run_id": "run_019"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_019", "patch_id": "FP-run_019", "message": "auto tentative fix for run run_019"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_019", "base": "feature/render-optim", "title": "auto fix build break run_019", "body": "summary for run run_019", "run_id": "run_019"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_019", "description": "Automated triage for run_019", "run_id": "run_019", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "build-macos-arm64"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_019"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_016",
        instruction=(
            "Coordinate CI crash triage for the game-engine pipeline. For the unsuccessful run run_020 on branch feature/render-optim at commit abc111def222ghi (job test-unit-windows), symbolicate and link incidents in a deterministic way, draft a PR and related ticket, validate, document, and supply the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_020", "status": "failure", "repo": "game-engine", "branch": "feature/render-optim", "commit_sha": "abc111def222ghi", "job_name": "test-unit-windows"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_020"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_020"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:abc111def222ghi:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "abc111def222ghi"}),
            Action(name="RunBisect", kwargs={"run_id": "run_020", "suspects": [{"ref": "abc111def222ghi"}], "test_target": "test-unit-windows"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_020", "logs_uri": "artifact://logs/run_020", "first_bad_commit": "abc111def222ghi"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/render-optim", "run_id": "run_020"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_020", "patch_id": "FP-run_020", "message": "auto tentative fix for run run_020"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_020", "base": "feature/render-optim", "title": "auto fix build break run_020", "body": "summary for run run_020", "run_id": "run_020"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_020", "description": "Automated triage for run_020", "run_id": "run_020", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "test-unit-windows"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_020"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_017",
        instruction=(
            "Handle CI crash triage for the game-engine pipeline. With failed run run_021 on branch feature/netcode at commit zyx987wvu654tsr (job performance-test-windows), symbolicate and connect incidents deterministically, formulate a draft PR and associated ticket, validate, document, and provide the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_021", "status": "failure", "repo": "game-engine", "branch": "feature/netcode", "commit_sha": "zyx987wvu654tsr", "job_name": "performance-test-windows"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_021"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_021"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:zyx987wvu654tsr:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "zyx987wvu654tsr"}),
            Action(name="RunBisect", kwargs={"run_id": "run_021", "suspects": [{"ref": "zyx987wvu654tsr"}], "test_target": "performance-test-windows"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_021", "logs_uri": "artifact://logs/run_021", "first_bad_commit": "zyx987wvu654tsr"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/netcode", "run_id": "run_021"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_021", "patch_id": "FP-run_021", "message": "auto tentative fix for run run_021"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_021", "base": "feature/netcode", "title": "auto fix build break run_021", "body": "summary for run run_021", "run_id": "run_021"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_021", "description": "Automated triage for run_021", "run_id": "run_021", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "performance-test-windows"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_021"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_018",
        instruction=(
            "Supervise CI crash triage for the game-engine pipeline. In the case of failed run run_022 on branch feature/netcode at commit zyx987wvu654tsr (job deploy-staging-windows), symbolicate and associate incidents deterministically, develop a draft PR and linked ticket, verify, record, and furnish the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_022", "status": "failure", "repo": "game-engine", "branch": "feature/netcode", "commit_sha": "zyx987wvu654tsr", "job_name": "deploy-staging-windows"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_022"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_022"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:zyx987wvu654tsr:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "zyx987wvu654tsr"}),
            Action(name="RunBisect", kwargs={"run_id": "run_022", "suspects": [{"ref": "zyx987wvu654tsr"}], "test_target": "deploy-staging-windows"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_022", "logs_uri": "artifact://logs/run_022", "first_bad_commit": "zyx987wvu654tsr"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/netcode", "run_id": "run_022"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_022", "patch_id": "FP-run_022", "message": "auto tentative fix for run run_022"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_022", "base": "feature/netcode", "title": "auto fix build break run_022", "body": "summary for run run_022", "run_id": "run_022"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_022", "description": "Automated triage for run_022", "run_id": "run_022", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "deploy-staging-windows"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_022"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_019",
        instruction=(
            "Take charge of CI crash triage for the asset pipeline. For the unsuccessful execution run_023 on branch feature/vehicle-assets at commit lm123no456pq789 (job validate-assets), systematically symbolicate and link incidents, prepare a draft PR along with a linked ticket, validate, document, and provide the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_023", "status": "failure", "repo": "game-assets", "branch": "feature/vehicle-assets", "commit_sha": "lm123no456pq789", "job_name": "validate-assets"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_023"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_023"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:lm123no456pq789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "lm123no456pq789"}),
            Action(name="RunBisect", kwargs={"run_id": "run_023", "suspects": [{"ref": "lm123no456pq789"}], "test_target": "validate-assets"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_023", "logs_uri": "artifact://logs/run_023", "first_bad_commit": "lm123no456pq789"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/vehicle-assets", "run_id": "run_023"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_023", "patch_id": "FP-run_023", "message": "auto tentative fix for run run_023"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_023", "base": "feature/vehicle-assets", "title": "auto fix build break run_023", "body": "summary for run run_023", "run_id": "run_023"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_023", "description": "Automated triage for run_023", "run_id": "run_023", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "validate-assets"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_023"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_020",
        instruction=(
            "Manage CI crash triage for the game-engine pipeline. For the unsuccessful execution run_024 on branch feature/houdini-tools at commit pqrs111tuv222wxy (job build-windows-x64), systematically symbolicate and link incidents, prepare a draft PR along with a linked ticket, validate, document, and provide the PR number."
        ),
        actions=[
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_024", "status": "failure", "repo": "game-engine", "branch": "feature/houdini-tools", "commit_sha": "pqrs111tuv222wxy", "job_name": "build-windows-x64"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_024"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_024"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:pqrs111tuv222wxy:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "pqrs111tuv222wxy"}),
            Action(name="RunBisect", kwargs={"run_id": "run_024", "suspects": [{"ref": "pqrs111tuv222wxy"}], "test_target": "build-windows-x64"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_024", "logs_uri": "artifact://logs/run_024", "first_bad_commit": "pqrs111tuv222wxy"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "feature/houdini-tools", "run_id": "run_024"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_024", "patch_id": "FP-run_024", "message": "auto tentative fix for run run_024"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_024", "base": "feature/houdini-tools", "title": "auto fix build break run_024", "body": "summary for run run_024", "run_id": "run_024"}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENG", "summary": "CI failure run_024", "description": "Automated triage for run_024", "run_id": "run_024", "pr_number": 33}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "build-windows-x64"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_024"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_021",
        instruction=(
            "Handle asset QA validation for asset asset_001 at catalog checksum sha256:a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456. Employ the standard intake QA policy in scene TestBudget to assess assets/textures/characters/hero_character_diffuse.png, then display the outcome on a draft QA PR established for this checkpoint using summary 'errors 0 warnings 0' and the necessary status. Provide the PR number 33."
        ),
        actions=[
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_001"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="RunDccValidation", kwargs={"files": ["assets/textures/characters/hero_character_diffuse.png"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/textures/characters/hero_character_diffuse.png"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/textures/characters/hero_character_diffuse.png"], "scene": "TestBudget"}),
            Action(
                name="UploadQaReports",
                kwargs={
                    "qa_json": [{"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []}],
                    "tex_report": [{"file": "assets/textures/characters/hero_character_diffuse.png"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/textures/characters/hero_character_diffuse.png"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_001"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(
                name="PersistAssetQaResults",
                kwargs={
                    "asset_id": "asset_001",
                    "commit_sha": "sha256:a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456",
                    "severity_max": "none",
                    "errors_count": 0,
                    "warnings_count": 0,
                    "preview_uri": "artifact://turntable/AR-1",
                    "report_uri": "artifact://qa/summary",
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_001"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_001-sha256:a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"},
                    "status": "completed",
                },
            ),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_022",
        instruction=(
            "Oversee asset QA validation for asset asset_002 at catalog checksum sha256:b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890. Utilize the standard intake QA policy in scene TestBudget to review assets/models/characters/hero_character.fbx, then reveal the result on a draft QA PR prepared for this checkpoint using summary 'errors 0 warnings 0' and the necessary status. Supply the PR number 33."
        ),
        actions=[
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_002"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="RunDccValidation", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/models/characters/hero_character.fbx"], "scene": "TestBudget"}),
            Action(
                name="UploadQaReports",
                kwargs={
                    "qa_json": [{"file": "assets/models/characters/hero_character.fbx", "issues": []}],
                    "tex_report": [{"file": "assets/models/characters/hero_character.fbx"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/models/characters/hero_character.fbx"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_002"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="PersistAssetQaResults",
                kwargs={
                    "asset_id": "asset_002",
                    "commit_sha": "sha256:b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890",
                    "severity_max": "none",
                    "errors_count": 0,
                    "warnings_count": 0,
                    "preview_uri": "artifact://turntable/AR-1",
                    "report_uri": "artifact://qa/summary",
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_002"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_002-sha256:b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890"},
                    "status": "completed",
                },
            ),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_023",
        instruction=(
            "Handle asset QA validation for asset asset_003 at catalog checksum sha256:c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcd. Utilize the standard intake QA policy in scene TestBudget to assess assets/textures/characters/hero_character_normal.png. Afterward, present the result on a draft QA PR created for this checkpoint with the summary 'errors 0 warnings 0' and the necessary status. Return the PR number 33."
        ),
        actions=[
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_003"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="RunDccValidation", kwargs={"files": ["assets/textures/characters/hero_character_normal.png"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/textures/characters/hero_character_normal.png"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/textures/characters/hero_character_normal.png"], "scene": "TestBudget"}),
            Action(
                name="UploadQaReports",
                kwargs={
                    "qa_json": [{"file": "assets/textures/characters/hero_character_normal.png", "issues": []}],
                    "tex_report": [{"file": "assets/textures/characters/hero_character_normal.png"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/textures/characters/hero_character_normal.png"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_003"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="PersistAssetQaResults",
                kwargs={
                    "asset_id": "asset_003",
                    "commit_sha": "sha256:c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcd",
                    "severity_max": "none",
                    "errors_count": 0,
                    "warnings_count": 0,
                    "preview_uri": "artifact://turntable/AR-1",
                    "report_uri": "artifact://qa/summary",
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_003"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_003-sha256:c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcd"},
                    "status": "completed",
                },
            ),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_024",
        instruction=(
            "Conduct asset QA validation for asset asset_004 at catalog checksum sha256:d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef. Employ the standard intake QA policy in scene TestBudget to appraise assets/animations/characters/hero_idle.fbx. Subsequently, display the result on the QA PR using the summary 'errors 0 warnings 0' and confirm the Asset QA check as successful. Return the PR number 33."
        ),
        actions=[
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_004"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="RunDccValidation", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"], "scene": "TestBudget"}),
            Action(
                name="UploadQaReports",
                kwargs={
                    "qa_json": [{"file": "assets/animations/characters/hero_idle.fbx", "issues": []}],
                    "tex_report": [{"file": "assets/animations/characters/hero_idle.fbx"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/animations/characters/hero_idle.fbx"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_004"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="PersistAssetQaResults",
                kwargs={
                    "asset_id": "asset_004",
                    "commit_sha": "sha256:d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef",
                    "severity_max": "none",
                    "errors_count": 0,
                    "warnings_count": 0,
                    "preview_uri": "artifact://turntable/AR-1",
                    "report_uri": "artifact://qa/summary",
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_004"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_004-sha256:d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef"},
                    "status": "completed",
                },
            ),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_025",
        instruction=(
            "Handle the QA validation for asset asset_005 at catalog checksum sha256:e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef12. Utilize the standard intake QA policy in scene TestBudget to assess assets/models/environment/castle_tower.fbx, then document the results on the QA PR using summary 'errors 0 warnings 0' and indicate the Asset QA check as successful. Provide the PR number 33."
        ),
        actions=[
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_005"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="RunDccValidation", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/models/environment/castle_tower.fbx"], "scene": "TestBudget"}),
            Action(
                name="UploadQaReports",
                kwargs={
                    "qa_json": [{"file": "assets/models/environment/castle_tower.fbx", "issues": []}],
                    "tex_report": [{"file": "assets/models/environment/castle_tower.fbx"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/models/environment/castle_tower.fbx"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_005"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(
                name="PersistAssetQaResults",
                kwargs={
                    "asset_id": "asset_005",
                    "commit_sha": "sha256:e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef12",
                    "severity_max": "none",
                    "errors_count": 0,
                    "warnings_count": 0,
                    "preview_uri": "artifact://turntable/AR-1",
                    "report_uri": "artifact://qa/summary",
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_005"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_005-sha256:e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef12"},
                    "status": "completed",
                },
            ),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),


    Task(
        annotator="0",
        user_id="task_026",
        instruction=(
            "Coordinate the asset QA validation for asset asset_006 at catalog checksum sha256:f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef1234. Apply the standard intake QA policy within scene TestBudget to review assets/textures/environment/castle_tower_diffuse.png, then present the outcome on a draft QA PR created for this checkpoint using summary 'errors 0 warnings 0' and the necessary status. Supply the PR number 33."
        ),
        actions=[
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_006"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="RunDccValidation", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png"], "scene": "TestBudget"}),
            Action(
                name="UploadQaReports",
                kwargs={
                    "qa_json": [{"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []}],
                    "tex_report": [{"file": "assets/textures/environment/castle_tower_diffuse.png"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/textures/environment/castle_tower_diffuse.png"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_006"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="PersistAssetQaResults",
                kwargs={
                    "asset_id": "asset_006",
                    "commit_sha": "sha256:f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef1234",
                    "severity_max": "none",
                    "errors_count": 0,
                    "warnings_count": 0,
                    "preview_uri": "artifact://turntable/AR-1",
                    "report_uri": "artifact://qa/summary",
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_006"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_006-sha256:f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef1234"},
                    "status": "completed",
                },
            ),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),


    Task(
        annotator="0",
        user_id="task_027",
        instruction=(
            "Handle asset QA validation for asset asset_007 at catalog checksum sha256:789012345678901234567890abcdef1234567890abcdef1234567890abcdef123456. Utilize the standard intake QA policy in scene TestBudget to evaluate assets/textures/environment/castle_tower_normal.png, then present the result on a draft QA PR created for this checkpoint using summary 'errors 0 warnings 0' and the required status. Provide the PR number 33."
        ),
        actions=[
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_007"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="RunDccValidation", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png"], "scene": "TestBudget"}),
            Action(
                name="UploadQaReports",
                kwargs={
                    "qa_json": [{"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}],
                    "tex_report": [{"file": "assets/textures/environment/castle_tower_normal.png"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/textures/environment/castle_tower_normal.png"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_007"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="PersistAssetQaResults",
                kwargs={
                    "asset_id": "asset_007",
                    "commit_sha": "sha256:789012345678901234567890abcdef1234567890abcdef1234567890abcdef123456",
                    "severity_max": "none",
                    "errors_count": 0,
                    "warnings_count": 0,
                    "preview_uri": "artifact://turntable/AR-1",
                    "report_uri": "artifact://qa/summary",
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_007"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_007-sha256:789012345678901234567890abcdef1234567890abcdef1234567890abcdef123456"},
                    "status": "completed",
                },
            ),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_028",
        instruction=(
            "Coordinate asset QA validation for asset asset_008 at catalog checksum sha256:89012345678901234567890abcdef1234567890abcdef1234567890abcdef1234567. Implement the standard intake QA policy in scene TestBudget to evaluate assets/materials/environment/castle_tower.mtl, then reveal the result on a draft QA PR created for this checkpoint using summary 'errors 0 warnings 0' and the required status. Supply the PR number 33."
        ),
        actions=[
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_008"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="RunDccValidation", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"], "scene": "TestBudget"}),
            Action(
                name="UploadQaReports",
                kwargs={
                    "qa_json": [{"file": "assets/materials/environment/castle_tower.mtl", "issues": []}],
                    "tex_report": [{"file": "assets/materials/environment/castle_tower.mtl"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/materials/environment/castle_tower.mtl"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_008"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="PersistAssetQaResults",
                kwargs={
                    "asset_id": "asset_008",
                    "commit_sha": "sha256:89012345678901234567890abcdef1234567890abcdef1234567890abcdef1234567",
                    "severity_max": "none",
                    "errors_count": 0,
                    "warnings_count": 0,
                    "preview_uri": "artifact://turntable/AR-1",
                    "report_uri": "artifact://qa/summary",
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_008"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_008-sha256:89012345678901234567890abcdef1234567890abcdef1234567890abcdef1234567"},
                    "status": "completed",
                },
            ),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),


    Task(
        annotator="0",
        user_id="task_029",
        instruction=(
            "Handle asset QA validation for asset asset_009 at catalog checksum sha256:9012345678901234567890abcdef1234567890abcdef1234567890abcdef12345678. Implement the standard intake QA policy in scene TestBudget to evaluate assets/audio/sfx/hero_sword_swing.wav, then note the outcome on the QA PR using summary 'errors 0 warnings 0' and indicate the Asset QA check as successful. Return the PR number 33."
        ),
        actions=[
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_009"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="RunDccValidation", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav"], "scene": "TestBudget"}),
            Action(
                name="UploadQaReports",
                kwargs={
                    "qa_json": [{"file": "assets/audio/sfx/hero_sword_swing.wav", "issues": []}],
                    "tex_report": [],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/audio/sfx/hero_sword_swing.wav"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": []},
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_009"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/qa-AR-2", "base": "main", "title": "asset-qa AR-2", "body": "qa AR-2", "run_id": "AR-2"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="PersistAssetQaResults",
                kwargs={
                    "asset_id": "asset_009",
                    "commit_sha": "sha256:9012345678901234567890abcdef1234567890abcdef1234567890abcdef12345678",
                    "severity_max": "none",
                    "errors_count": 0,
                    "warnings_count": 0,
                    "preview_uri": "artifact://turntable/AR-1",
                    "report_uri": "artifact://qa/summary",
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_009"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_009-sha256:9012345678901234567890abcdef1234567890abcdef1234567890abcdef12345678"},
                    "status": "completed",
                },
            ),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_030",
        instruction=(
            "Handle asset QA validation for asset asset_010 at catalog checksum sha256:012345678901234567890abcdef1234567890abcdef1234567890abcdef123456789. Implement the standard intake QA policy in scene TestBudget to evaluate assets/audio/music/main_theme.ogg, then note the outcome on the QA PR using summary 'errors 0 warnings 0' and indicate the Asset QA check as successful. Return the PR number 33."
        ),
        actions=[
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_010"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="RunDccValidation", kwargs={"files": ["assets/audio/music/main_theme.ogg"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/audio/music/main_theme.ogg"], "scene": "TestBudget"}),
            Action(
                name="UploadQaReports",
                kwargs={
                    "qa_json": [{"file": "assets/audio/music/main_theme.ogg", "issues": []}],
                    "tex_report": [],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/audio/music/main_theme.ogg"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": []},
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_010"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/qa-AR-2", "base": "main", "title": "asset-qa AR-2", "body": "qa AR-2", "run_id": "AR-2"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="PersistAssetQaResults",
                kwargs={
                    "asset_id": "asset_010",
                    "commit_sha": "sha256:012345678901234567890abcdef1234567890abcdef1234567890abcdef123456789",
                    "severity_max": "none",
                    "errors_count": 0,
                    "warnings_count": 0,
                    "preview_uri": "artifact://turntable/AR-1",
                    "report_uri": "artifact://qa/summary",
                },
            ),
            Action(
                name="RecordAutomationRun",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_010"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_010-sha256:012345678901234567890abcdef1234567890abcdef1234567890abcdef123456789"},
                    "status": "completed",
                },
            ),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_031",
        instruction=(
            "Handle deterministic asset auto-remediation for asset asset_001 at catalog checksum sha256:a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456. Utilize the TestBudget scene to assess assets/textures/characters/hero_character_diffuse.png, then present the findings on the draft PR for this checkpoint, mark the Asset QA check as success, save results keyed to the catalog checksum, and provide PR number 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_001"}, "outputs": {}, "status": "started"}),
            Action(name="RunDccValidation", kwargs={"files": ["assets/textures/characters/hero_character_diffuse.png"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/textures/characters/hero_character_diffuse.png"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/textures/characters/hero_character_diffuse.png"], "scene": "TestBudget"}),
            Action(name="ApplyAssetAutofixes", kwargs={"qa_json": [{"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []}], "tex_report": [{"file": "assets/textures/characters/hero_character_diffuse.png"}]}),
            Action(name="RenderAssetPreviews", kwargs={"files": ["assets/textures/characters/hero_character_diffuse.png"]}),
            Action(name="UploadQaReports", kwargs={"qa_json": [{"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []}], "tex_report": [{"file": "assets/textures/characters/hero_character_diffuse.png"}], "engine_report": {"scene": "TestBudget", "files": ["assets/textures/characters/hero_character_diffuse.png"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_001"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="PersistAssetQaResults", kwargs={"asset_id": "asset_001", "commit_sha": "sha256:a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_001"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_001-sha256:a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_032",
        instruction=(
            "Coordinate deterministic asset auto-remediation for asset asset_002 at catalog checksum sha256:b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890. Employ the TestBudget scene to inspect assets/models/characters/hero_character.fbx, then exhibit the results on the draft PR for this checkpoint, mark the Asset QA check as success, store results keyed to the catalog checksum, and return PR number 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_002"}, "outputs": {}, "status": "started"}),
            Action(name="RunDccValidation", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/models/characters/hero_character.fbx"], "scene": "TestBudget"}),
            Action(name="ApplyAssetAutofixes", kwargs={"qa_json": [{"file": "assets/models/characters/hero_character.fbx", "issues": []}], "tex_report": [{"file": "assets/models/characters/hero_character.fbx"}]}),
            Action(name="RenderAssetPreviews", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="UploadQaReports", kwargs={"qa_json": [{"file": "assets/models/characters/hero_character.fbx", "issues": []}], "tex_report": [{"file": "assets/models/characters/hero_character.fbx"}], "engine_report": {"scene": "TestBudget", "files": ["assets/models/characters/hero_character.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_002"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="PersistAssetQaResults", kwargs={"asset_id": "asset_002", "commit_sha": "sha256:b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_002"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_002-sha256:b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_033",
        instruction=(
            "Handle intake QA for asset asset_003 with catalog checksum sha256:c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcd. Within the TestBudget evaluation context, make sure the corresponding draft QA PR for this checkpoint indicates the result with the needed status, save the result associated with the catalog checksum, and provide PR number 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_003"}, "outputs": {}, "status": "started"}),
            Action(name="GetAssetFiles", kwargs={"asset_id": "asset_003"}),
            Action(name="RunDccValidation", kwargs={"files": ["assets/textures/characters/hero_character_normal.png"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/textures/characters/hero_character_normal.png"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/textures/characters/hero_character_normal.png"], "scene": "TestBudget"}),
            Action(name="RenderAssetPreviews", kwargs={"files": ["assets/textures/characters/hero_character_normal.png"]}),
            Action(name="UploadQaReports", kwargs={"qa_json": [{"file": "assets/textures/characters/hero_character_normal.png", "issues": []}], "tex_report": [{"file": "assets/textures/characters/hero_character_normal.png"}], "engine_report": {"scene": "TestBudget", "files": ["assets/textures/characters/hero_character_normal.png"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_003"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="PersistAssetQaResults", kwargs={"asset_id": "asset_003", "commit_sha": "sha256:c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcd", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_003"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_003-sha256:c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcd"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_034",
        instruction=(
            "Oversee deterministic asset auto-remediation for asset asset_004 (catalog checksum sha256:d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef). In the TestBudget evaluation framework, using only values drawn from the database, confirm the corresponding draft PR accurately shows the result with the correct status, store the result linked to the checksum, keep a thorough automation audit log, and return PR number 33. Avoid creating new identifiers."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_004"}, "outputs": {}, "status": "started"}),
            Action(name="GetAssetFiles", kwargs={"asset_id": "asset_004"}),
            Action(name="RunDccValidation", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"], "scene": "TestBudget"}),
            Action(name="RenderAssetPreviews", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="UploadQaReports", kwargs={"qa_json": [{"file": "assets/animations/characters/hero_idle.fbx", "issues": []}], "tex_report": [{"file": "assets/animations/characters/hero_idle.fbx"}], "engine_report": {"scene": "TestBudget", "files": ["assets/animations/characters/hero_idle.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_004"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="PersistAssetQaResults", kwargs={"asset_id": "asset_004", "commit_sha": "sha256:d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_004"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_004-sha256:d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_035",
        instruction=(
            "Handle the mechanical asset remediation for asset asset_005 associated with catalog checksum sha256:e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef12. Implement the standard auto-remediation policy in the scene TestBudget for assets/models/environment/castle_tower.fbx, document the outcome in a draft QA PR with the necessary status, save results keyed to the catalog checksum, and provide PR number 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_005"}, "outputs": {}, "status": "started"}),
            Action(name="RunDccValidation", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/models/environment/castle_tower.fbx"], "scene": "TestBudget"}),
            Action(name="ApplyAssetAutofixes", kwargs={"qa_json": [{"file": "assets/models/environment/castle_tower.fbx", "issues": []}], "tex_report": [{"file": "assets/models/environment/castle_tower.fbx"}]}),
            Action(name="RenderAssetPreviews", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="UploadQaReports", kwargs={"qa_json": [{"file": "assets/models/environment/castle_tower.fbx", "issues": []}], "tex_report": [{"file": "assets/models/environment/castle_tower.fbx"}], "engine_report": {"scene": "TestBudget", "files": ["assets/models/environment/castle_tower.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_005"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="PersistAssetQaResults", kwargs={"asset_id": "asset_005", "commit_sha": "sha256:e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef12", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_005"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_005-sha256:e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef12"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_036",
        instruction=(
            "Handle the mechanical asset remediation for asset asset_006 linked to catalog checksum sha256:f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef1234. Implement the standard auto-remediation policy in the scene TestBudget for assets/textures/environment/castle_tower_diffuse.png, document the outcome in a draft QA PR with the necessary status, save results keyed to the catalog checksum, and provide PR number 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_006"}, "outputs": {}, "status": "started"}),
            Action(name="RunDccValidation", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png"], "scene": "TestBudget"}),
            Action(name="ApplyAssetAutofixes", kwargs={"qa_json": [{"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []}], "tex_report": [{"file": "assets/textures/environment/castle_tower_diffuse.png"}]}),
            Action(name="RenderAssetPreviews", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png"]}),
            Action(name="UploadQaReports", kwargs={"qa_json": [{"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []}], "tex_report": [{"file": "assets/textures/environment/castle_tower_diffuse.png"}], "engine_report": {"scene": "TestBudget", "files": ["assets/textures/environment/castle_tower_diffuse.png"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_006"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="PersistAssetQaResults", kwargs={"asset_id": "asset_006", "commit_sha": "sha256:f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef1234", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_006"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_006-sha256:f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef1234"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_037",
        instruction=(
            "Handle deterministic asset auto-remediation for asset asset_007 at catalog checksum sha256:789012345678901234567890abcdef1234567890abcdef1234567890abcdef123456. Utilize the TestBudget scene to evaluate assets/textures/environment/castle_tower_normal.png, proceed to surface the outcome on the draft PR for this checkpoint, assign the Asset QA check to success, persist results keyed to the catalog checksum, and provide PR number 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_007"}, "outputs": {}, "status": "started"}),
            Action(name="RunDccValidation", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png"], "scene": "TestBudget"}),
            Action(name="ApplyAssetAutofixes", kwargs={"qa_json": [{"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}], "tex_report": [{"file": "assets/textures/environment/castle_tower_normal.png"}]}),
            Action(name="RenderAssetPreviews", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="UploadQaReports", kwargs={"qa_json": [{"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}], "tex_report": [{"file": "assets/textures/environment/castle_tower_normal.png"}], "engine_report": {"scene": "TestBudget", "files": ["assets/textures/environment/castle_tower_normal.png"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_007"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="PersistAssetQaResults", kwargs={"asset_id": "asset_007", "commit_sha": "sha256:789012345678901234567890abcdef1234567890abcdef1234567890abcdef123456", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_007"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_007-sha256:789012345678901234567890abcdef1234567890abcdef1234567890abcdef123456"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_038",
        instruction=(
            "Oversee deterministic asset auto-remediation for asset asset_008 at catalog checksum sha256:89012345678901234567890abcdef1234567890abcdef1234567890abcdef1234567. Employ the TestBudget scene to evaluate assets/materials/environment/castle_tower.mtl, subsequently surface the outcome on the draft PR for this checkpoint, designate the Asset QA check to success, persist results keyed to the catalog checksum, and return PR number 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_008"}, "outputs": {}, "status": "started"}),
            Action(name="RunDccValidation", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="ValidateTextures", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"], "scene": "TestBudget"}),
            Action(name="ApplyAssetAutofixes", kwargs={"qa_json": [{"file": "assets/materials/environment/castle_tower.mtl", "issues": []}], "tex_report": [{"file": "assets/materials/environment/castle_tower.mtl"}]}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "main", "run_id": "AR-1"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-AR-1", "patch_id": "AF-1", "message": "auto tentative fix for run AR-1"}),
            Action(name="RenderAssetPreviews", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="UploadQaReports", kwargs={"qa_json": [{"file": "assets/materials/environment/castle_tower.mtl", "issues": []}], "tex_report": [{"file": "assets/materials/environment/castle_tower.mtl"}], "engine_report": {"scene": "TestBudget", "files": ["assets/materials/environment/castle_tower.mtl"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_008"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="PersistAssetQaResults", kwargs={"asset_id": "asset_008", "commit_sha": "sha256:89012345678901234567890abcdef1234567890abcdef1234567890abcdef1234567", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_008"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_008-sha256:89012345678901234567890abcdef1234567890abcdef1234567890abcdef1234567"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_039",
        instruction=(
            "Arrange intake QA for asset asset_009 at catalog checksum sha256:9012345678901234567890abcdef1234567890abcdef1234567890abcdef12345678. Evaluation context: TestBudget. Ensure the relevant draft QA PR for this checkpoint mirrors the outcome with the required status, save the result keyed to the catalog checksum, and return PR number 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_009"}, "outputs": {}, "status": "started"}),
            Action(name="GetAssetFiles", kwargs={"asset_id": "asset_009"}),
            Action(name="RunDccValidation", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav"], "scene": "TestBudget"}),
            Action(name="ApplyAssetAutofixes", kwargs={"qa_json": [{"file": "assets/audio/sfx/hero_sword_swing.wav", "issues": []}], "tex_report": []}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "main", "run_id": "AR-1"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-AR-1", "patch_id": "AF-1", "message": "auto tentative fix for run AR-1"}),
            Action(name="RenderAssetPreviews", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav"]}),
            Action(name="UploadQaReports", kwargs={"qa_json": [{"file": "assets/audio/sfx/hero_sword_swing.wav", "issues": []}], "tex_report": [], "engine_report": {"scene": "TestBudget", "files": ["assets/audio/sfx/hero_sword_swing.wav"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_009"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="PersistAssetQaResults", kwargs={"asset_id": "asset_009", "commit_sha": "sha256:9012345678901234567890abcdef1234567890abcdef1234567890abcdef12345678", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_009"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_009-sha256:9012345678901234567890abcdef1234567890abcdef1234567890abcdef12345678"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_040",
        instruction=(
            "Handle intake QA for asset asset_010 at catalog checksum sha256:012345678901234567890abcdef1234567890abcdef1234567890abcdef123456789. Evaluation context: TestBudget. Ensure the correct draft QA PR for this checkpoint represents the outcome with the required status, store the result keyed to the catalog checksum, and return PR number 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_010"}, "outputs": {}, "status": "started"}),
            Action(name="RunDccValidation", kwargs={"files": ["assets/audio/music/main_theme.ogg"]}),
            Action(name="RunEngineBudgetChecks", kwargs={"files": ["assets/audio/music/main_theme.ogg"], "scene": "TestBudget"}),
            Action(name="ApplyAssetAutofixes", kwargs={"qa_json": [{"file": "assets/audio/music/main_theme.ogg", "issues": []}], "tex_report": []}),
            Action(name="RenderAssetPreviews", kwargs={"files": ["assets/audio/music/main_theme.ogg"]}),
            Action(name="UploadQaReports", kwargs={"qa_json": [{"file": "assets/audio/music/main_theme.ogg", "issues": []}], "tex_report": [], "engine_report": {"scene": "TestBudget", "files": ["assets/audio/music/main_theme.ogg"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_010"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="AnnotatePrWithQa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheck", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="PersistAssetQaResults", kwargs={"asset_id": "asset_010", "commit_sha": "sha256:012345678901234567890abcdef1234567890abcdef1234567890abcdef123456789", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_010"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_010-sha256:012345678901234567890abcdef1234567890abcdef1234567890abcdef123456789"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_041",
        instruction=(
            "Manage intake normalization and routing for ticket work_026 featuring fingerprint renderer_character_load_access_violation_xyz. Ensure that the routing incorporates the impact and owner resolution derived from the fingerprint in src/game/engine/renderer.cpp. Persist triage_status='In Triage', labels=['auto-triage'], impact_score, owner_team, and summary_text; then return the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "started"}),
            # Seed from DB fields only; do not invent payload text
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "work_026"}),
            Action(name="SummarizeIssue", kwargs={"ticket_key": "work_026"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "work_026", "fingerprint": "renderer_character_load_access_violation_xyz"}),
            Action(name="ResolveOwnerFromMap", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            # Persist deterministic fields in one minimal update (include exact summary)
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"impact_score": 2, "owner_team": "team_001", "triage_status": "In Triage", "labels": ["auto-triage"], "summary_text": "Issue :: "}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "routed"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {"ticket_key": "work_026"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "work_026"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_042",
        instruction=(
            "Handle the impact assessment and routing updates for ticket work_026 utilizing its crash fingerprint renderer_character_load_access_violation_xyz. Ensure to persist triage_status='In Triage', labels=['auto-triage'], impact_score, owner_team resolved from src/game/engine/renderer.cpp, and summary_text; then return the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "work_026"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "normalized"}),
            Action(name="SummarizeIssue", kwargs={"ticket_key": "work_026"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "summarized"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "work_026", "fingerprint": "renderer_character_load_access_violation_xyz"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "scored"}),
            Action(name="ResolveOwnerFromMap", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            # Persist actual computed values (single update, include summary and owner)
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"impact_score": 2, "owner_team": "team_001", "triage_status": "In Triage", "labels": ["auto-triage"], "summary_text": "Issue :: "}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "routed"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {"ticket_key": "work_026"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "work_026"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_043",
        instruction=(
            "Manage intake normalization and ticket routing for work_027 (texture artifacts). Connect any duplicates to work_026 (confidence 0.91), determine the owner from assets/textures/character_models/, and save triage_status='In Triage', labels=['auto-triage'], impact_score, owner_team, and summary_text; provide the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_027"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "work_027"}),
            Action(name="SummarizeIssue", kwargs={"ticket_key": "work_027"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "work_027"}),
            Action(name="LinkDuplicateIssue", kwargs={"primary_ticket_key": "work_027", "duplicate_ticket_key": "work_026", "confidence": 0.91}),
            Action(name="ResolveOwnerFromMap", kwargs={"module_or_path": "assets/textures/character_models/"}),
            # Persist computed fields and routing in one minimal update (exact summary from summarize_issue)
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_027", "fields": {"impact_score": 2, "owner_team": "team_002", "triage_status": "In Triage", "labels": ["auto-triage"], "summary_text": "Issue :: "}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {}, "status": "routed"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "work_027"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_044",
        instruction=(
            "Oversee the logging of impact and routing fields for ticket work_027 using its normalized data. Save triage_status='In Triage', labels=['auto-triage'], and impact_score extracted from the normalized issue; deliver the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_027"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "work_027"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "normalized"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "work_027"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_027", "fields": {"impact_score": 2, "triage_status": "In Triage", "labels": ["auto-triage"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "routed"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "work_027"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_045",
        instruction=(
            "Handle routing for ticket work_026. Identify the owner from src/game/engine/renderer.cpp and save owner_team, triage_status='In Triage', labels=['auto-triage'], impact_score, and summary_text; provide the ticket key afterward."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "work_026"}),
            Action(name="SummarizeIssue", kwargs={"ticket_key": "work_026"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "work_026"}),
            Action(name="ResolveOwnerFromMap", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"owner_team": "team_001", "triage_status": "In Triage", "labels": ["auto-triage"], "impact_score": 2, "summary_text": "Issue :: "}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "routed"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {"ticket_key": "work_026"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "work_026"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_046",
        instruction=(
            "Assume responsibility for summarizing and assessing the impact for ticket work_027 and verify routing metadata. Store summary_text, impact_score, triage_status='In Triage', labels=['auto-triage'], and the owner_team identified from assets/textures/character_models/. Return the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_027"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "work_027"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "normalized"}),
            Action(name="SummarizeIssue", kwargs={"ticket_key": "work_027"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "summarized"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "work_027"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "scored"}),
            Action(name="ResolveOwnerFromMap", kwargs={"module_or_path": "assets/textures/character_models/"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_027", "fields": {"owner_team": "team_002", "summary_text": "Issue :: ", "impact_score": 2, "triage_status": "In Triage", "labels": ["auto-triage"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "routed"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "work_027"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_047",
        instruction=(
            "Take charge of intake normalization and impact logging for ticket work_027; ensure normalization, deduplication with work_026 if necessary, calculation of impact, and storage of impact_score, triage_status='In Triage', and labels=['auto-triage']; then provide the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_027"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "work_027"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {}, "status": "normalized"}),
            Action(name="LinkDuplicateIssue", kwargs={"primary_ticket_key": "work_026", "duplicate_ticket_key": "work_027", "confidence": 1.0}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "deduped"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "work_027"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "scored"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_027", "fields": {"impact_score": 2, "triage_status": "In Triage", "labels": ["auto-triage"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "work_027"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_048",
        instruction=(
            "Oversee the documentation of a deterministic summary and identification of the owner for ticket work_026. Store summary_text, impact_score, triage_status='In Triage', labels=['auto-triage'], and owner_team from src/game/engine/renderer.cpp; return the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "work_026"}),
            Action(name="SummarizeIssue", kwargs={"ticket_key": "work_026"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "work_026"}),
            Action(name="ResolveOwnerFromMap", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"owner_team": "team_001", "impact_score": 2, "summary_text": "Issue :: ", "triage_status": "In Triage", "labels": ["auto-triage"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {"ticket_key": "work_026"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "work_026"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_049",
        instruction=(
            "Handle deterministic replay of intake for ticket work_026 to verify normalized fields and routing. Maintain the normalized flag, set triage_status to 'In Triage', apply labels=['auto-triage'], and ensure impact_score is retained; subsequently, provide the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "work_026"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "normalized"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "work_026"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"normalized": True, "impact_score": 2, "triage_status": "In Triage", "labels": ["auto-triage"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {"ticket_key": "work_026"}, "status": "scored"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {"ticket_key": "work_026"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "work_026"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_050",
        instruction=(
            "Oversee deterministic impact logging and routing for ticket work_027. Keep triage_status as 'In Triage', apply labels=['auto-triage'], retain impact_score, and determine owner_team from assets/textures/character_models/; finally, return the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_027"}}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "work_027"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "scored"}),
            Action(name="ResolveOwnerFromMap", kwargs={"module_or_path": "assets/textures/character_models/"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_027", "fields": {"triage_status": "In Triage", "labels": ["auto-triage"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "routed"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_027", "fields": {"owner_team": "team_002", "impact_score": 2}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "work_027"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_051",
        instruction=(
            "Handle deterministic duplicate linking and routing for ticket work_026. Associate it with canonical work_027 with a confidence level of 0.91, and maintain triage_status='In Triage', labels=['auto-triage','duplicate'], impact_score, owner_team resolved from src/game/engine/renderer.cpp; then provide the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "work_026"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "work_026"}),
            Action(name="ResolveOwnerFromMap", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            Action(name="LinkDuplicateIssue", kwargs={"primary_ticket_key": "work_027", "duplicate_ticket_key": "work_026", "confidence": 0.91}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"owner_team": "team_001", "impact_score": 2, "triage_status": "In Triage", "labels": ["auto-triage", "duplicate"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {"ticket_key": "work_026"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "work_026"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_052",
        instruction=(
            "Coordinate deduplication of ticket work_029 under canonical work_030 with a confidence level of 0.78 and ensure routing labels and impact persist. Confirm the existence of the ticket and update labels=['auto-triage','duplicate'] and impact_score; then return the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_029"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_029"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "work_029"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "work_029"}),
            Action(name="LinkDuplicateIssue", kwargs={"primary_ticket_key": "work_030", "duplicate_ticket_key": "work_029", "confidence": 0.78}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_029", "fields": {"impact_score": 2, "labels": ["auto-triage", "duplicate"]}}),
            # Complete the same automation run deterministically
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_029"}, "outputs": {}, "status": "deduplicated"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_029"}, "outputs": {"ticket_key": "work_029"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "work_029"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_053",
        instruction=(
            "You are responsible for linking duplicate ticket bug_006 to canonical bug_007 with a confidence level of 0.95. Standardize and evaluate the impact, then save labels=['auto-triage','duplicate'] and the impact_score; return the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_006"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_006"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "bug_006"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "bug_006"}),
            Action(name="LinkDuplicateIssue", kwargs={"primary_ticket_key": "bug_007", "duplicate_ticket_key": "bug_006", "confidence": 0.95}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "bug_006", "fields": {"impact_score": 2, "labels": ["auto-triage", "duplicate"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_006"}, "outputs": {"ticket_key": "bug_006"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "bug_006"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_054",
        instruction=(
            "You are responsible for linking duplicate ticket bug_009 to canonical bug_010 with a confidence level of 0.82. Standardize and evaluate the impact, then save labels=['auto-triage','duplicate'] and the impact_score; return the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_009"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_009"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "bug_009"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_009"}, "outputs": {"ticket_key": "bug_009"}, "status": "normalized"}),
            Action(name="SummarizeIssue", kwargs={"ticket_key": "bug_009"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_009"}, "outputs": {"ticket_key": "bug_009"}, "status": "summarized"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "bug_009"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_009"}, "outputs": {"ticket_key": "bug_009"}, "status": "scored"}),
            Action(name="LinkDuplicateIssue", kwargs={"primary_ticket_key": "bug_010", "duplicate_ticket_key": "bug_009", "confidence": 0.82}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_009"}, "outputs": {"ticket_key": "bug_009"}, "status": "deduplicated"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "bug_009", "fields": {"labels": ["auto-triage", "duplicate"]}}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "bug_009", "fields": {"impact_score": 2}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_009"}, "outputs": {"ticket_key": "bug_009"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "bug_009"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_055",
        instruction=(
            "Handle the task of linking the duplicate ticket bug_013 to the primary bug_014 with a confidence level of 0.89. Adjust and evaluate the impact, then save the labels=['auto-triage','duplicate'] and impact_score; provide the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_013"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_013"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "bug_013"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "bug_013"}),
            Action(name="LinkDuplicateIssue", kwargs={"primary_ticket_key": "bug_014", "duplicate_ticket_key": "bug_013", "confidence": 0.89}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "bug_013", "fields": {"impact_score": 2, "labels": ["auto-triage", "duplicate"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_013"}, "outputs": {"ticket_key": "bug_013"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "bug_013"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_056",
        instruction=(
            "Coordinates are needed for linking the duplicate ticket bug_016 to the main bug_017 with a confidence level of 0.76. Adapt and determine the impact, then retain the labels=['auto-triage','duplicate'] and impact_score; supply the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_016"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_016"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "bug_016"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "bug_016"}),
            Action(name="LinkDuplicateIssue", kwargs={"primary_ticket_key": "bug_017", "duplicate_ticket_key": "bug_016", "confidence": 0.76}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "bug_016", "fields": {"impact_score": 2, "labels": ["auto-triage", "duplicate"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_016"}, "outputs": {"ticket_key": "bug_016"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "bug_016"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_057",
        instruction=(
            "Handle the linking of duplicate ticket bug_intake_008 to the main ticket bug_intake_007 with a confidence of 0.98. Standardize and evaluate the impact, then save labels=['auto-triage','duplicate'] and impact_score; provide the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_008"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_008"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "bug_intake_008"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_008"}, "outputs": {"ticket_key": "bug_intake_008"}, "status": "normalized"}),
            Action(name="SummarizeIssue", kwargs={"ticket_key": "bug_intake_008"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_008"}, "outputs": {"ticket_key": "bug_intake_008"}, "status": "summarized"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "bug_intake_008"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_008"}, "outputs": {"ticket_key": "bug_intake_008"}, "status": "scored"}),
            Action(name="LinkDuplicateIssue", kwargs={"primary_ticket_key": "bug_intake_007", "duplicate_ticket_key": "bug_intake_008", "confidence": 0.98}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_008"}, "outputs": {"ticket_key": "bug_intake_008"}, "status": "deduplicated"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "bug_intake_008", "fields": {"labels": ["auto-triage", "duplicate"]}}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "bug_intake_008", "fields": {"impact_score": 2}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_008"}, "outputs": {"ticket_key": "bug_intake_008"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "bug_intake_008"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_058",
        instruction=(
            "Coordinate deduplication of ticket bug_intake_016 with the primary ticket bug_intake_015 at confidence 0.93, ensuring routing labels and impact are recorded. Verify the ticket exists and update labels=['auto-triage','duplicate'] and impact_score; subsequently return the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_016"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_016"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "bug_intake_016"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "bug_intake_016"}),
            Action(name="LinkDuplicateIssue", kwargs={"primary_ticket_key": "bug_intake_015", "duplicate_ticket_key": "bug_intake_016", "confidence": 0.93}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "bug_intake_016", "fields": {"impact_score": 2, "labels": ["auto-triage", "duplicate"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_016"}, "outputs": {}, "status": "deduplicated"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_016"}, "outputs": {"ticket_key": "bug_intake_016"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "bug_intake_016"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_059",
        instruction=(
            "You are responsible for linking the duplicate ticket bug_intake_020 to the canonical bug_intake_019 with a confidence of 0.89. Standardize and evaluate the impact, then save labels=['auto-triage','duplicate'] and impact_score; provide the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_020"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_020"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "bug_intake_020"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_020"}, "outputs": {"ticket_key": "bug_intake_020"}, "status": "normalized"}),
            Action(name="SummarizeIssue", kwargs={"ticket_key": "bug_intake_020"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_020"}, "outputs": {"ticket_key": "bug_intake_020"}, "status": "summarized"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "bug_intake_020"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_020"}, "outputs": {"ticket_key": "bug_intake_020"}, "status": "scored"}),
            Action(name="LinkDuplicateIssue", kwargs={"primary_ticket_key": "bug_intake_019", "duplicate_ticket_key": "bug_intake_020", "confidence": 0.89}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_020"}, "outputs": {"ticket_key": "bug_intake_020"}, "status": "deduplicated"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "bug_intake_020", "fields": {"labels": ["auto-triage", "duplicate"]}}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "bug_intake_020", "fields": {"impact_score": 2}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_020"}, "outputs": {"ticket_key": "bug_intake_020"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "bug_intake_020"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_060",
        instruction=(
            "You are responsible for linking the duplicate ticket bug_intake_024 to the canonical bug_intake_023 with a confidence of 0.96. Standardize and evaluate the impact, then save labels=['auto-triage','duplicate'] and impact_score; provide the ticket key."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_024"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveTicketWebhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_024"}}),
            Action(name="NormalizeIssue", kwargs={"ticket_key": "bug_intake_024"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_024"}, "outputs": {"ticket_key": "bug_intake_024"}, "status": "normalized"}),
            Action(name="SummarizeIssue", kwargs={"ticket_key": "bug_intake_024"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_024"}, "outputs": {"ticket_key": "bug_intake_024"}, "status": "summarized"}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "bug_intake_024"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_024"}, "outputs": {"ticket_key": "bug_intake_024"}, "status": "scored"}),
            Action(name="LinkDuplicateIssue", kwargs={"primary_ticket_key": "bug_intake_023", "duplicate_ticket_key": "bug_intake_024", "confidence": 0.96}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_024"}, "outputs": {"ticket_key": "bug_intake_024"}, "status": "deduplicated"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "bug_intake_024", "fields": {"labels": ["auto-triage", "duplicate"]}}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "bug_intake_024", "fields": {"impact_score": 2}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_024"}, "outputs": {"ticket_key": "bug_intake_024"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "bug_intake_024"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_061",
        instruction=(
            "Handle the complete localization kit for PR 999, incorporating all changed strings across de, fr, ja, with a 200px UI budget. Maintain bundles and initiate a review TMS job; provide the PR number."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="DetectChangedStrings", kwargs={"pr_number": 999}),
            Action(name="CaptureLocContext", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="LocLint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "999"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_062",
        instruction=(
            "Coordinate the verification of localization for PR 999, using all changed strings across de, fr, ja within a 200px budget. Preserve bundles and commence a review TMS job; submit the PR number."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="DetectChangedStrings", kwargs={"pr_number": 999}),
            Action(name="CaptureLocContext", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="LocLint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "999"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_063",
        instruction=(
            "Handle the creation of a German-first draft localization kit for PR 999 using all altered strings in de, fr, ja within a 200px budget. Maintain bundles and initiate a review TMS job; provide the PR number."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="DetectChangedStrings", kwargs={"pr_number": 999}),
            Action(name="CaptureLocContext", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="LocLint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "999"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_064",
        instruction=(
            "Coordinate a context-rich localization kit for PR 999 using all altered strings in de, fr, ja within a 200px budget. Maintain bundles and initiate a review TMS job; provide the PR number."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="DetectChangedStrings", kwargs={"pr_number": 999}),
            Action(name="CaptureLocContext", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="LocLint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "999"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_065",
        instruction=(
            "Handle pixel-budget-focused localization for PR 999 using all changed strings in de, fr, ja within a 200px budget. Save bundles and initiate a review TMS job; provide the PR number."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="DetectChangedStrings", kwargs={"pr_number": 999}),
            Action(name="CaptureLocContext", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="LocLint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "999"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_066",
        instruction=(
            "Coordinate context capture and localization preparation for PR 999 using all changed strings in de, fr, ja at a 200px budget. Save bundles and initiate a review TMS job; provide the PR number."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="DetectChangedStrings", kwargs={"pr_number": 999}),
            Action(name="CaptureLocContext", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="LocLint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "999"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_067",
        instruction=(
            "Handle cross-locale lint verification for PR 999, utilizing all modified strings in de, fr, ja with a budget of 200px. Save bundles and initiate a review TMS task; provide the PR number."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="DetectChangedStrings", kwargs={"pr_number": 999}),
            Action(name="CaptureLocContext", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="LocLint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "999"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_068",
        instruction=(
            "Coordinate bundle generation following lint for PR 999, using all modified strings in de, fr, ja with a budget of 200px. Save bundles and initiate a review TMS task; provide the PR number."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="DetectChangedStrings", kwargs={"pr_number": 999}),
            Action(name="CaptureLocContext", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="LocLint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "999"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_069",
        instruction=(
            "Handle a validation pass for PR 999 localization utilizing all changed strings across de, fr, ja within a 200px budget. Persist bundles and initiate a review TMS job; return the PR number."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="DetectChangedStrings", kwargs={"pr_number": 999}),
            Action(name="CaptureLocContext", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="LocLint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "999"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_070",
        instruction=(
            "Coordinate the localization kit finalization for PR 999 with all changed strings in de, fr, ja at a 200px budget. Persist bundles and open a review TMS job; return the PR number."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="DetectChangedStrings", kwargs={"pr_number": 999}),
            Action(name="CaptureLocContext", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="LocLint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "999"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_071",
        instruction=(
            "Handle the task of confirming subtitle timing and maintaining VO workflow state for the hero introduction in various locales. Utilize the stored records for subtitle_001 (en) and subtitle_002 (de) associated with the string_key 'vo.hero.intro_01', sustain per-locale bundles, initiate a review job titled 'tms-vo-lines-subtitle_001-subtitle_002' with locales sorted as ['en','de'], and apply VO labels ['vo-subtitles','timing-validated'] to ticket 'work_026'; then provide the count of processed lines."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_001", "subtitle_002"]}, "outputs": {}, "status": "started"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_001", "locale": "en"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "tms-vo-lines-subtitle_001-subtitle_002", "locales": ["en", "de"], "status": "in_review"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_001", "subtitle_002"]}, "outputs": {"lines": ["subtitle_001", "subtitle_002"]}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "2"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_072",
        instruction=(
            "Coordinate the VO subtitle timing QA and transition process for the second hero introduction line across locales 'en' and 'fr'. Implement policy-guided validation, packaging, and registering of reviews using deterministic identifiers from the relevant line IDs and string keys, and log the result on tracking ticket 'work_026' with the suitable labels. Return the total number of lines processed."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_003", "subtitle_004"]}, "outputs": {}, "status": "started"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_003", "locale": "en"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "en", "keys": ["subtitle_003"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "fr", "keys": ["subtitle_004"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "tms-vo-lines-subtitle_003-subtitle_004", "locales": ["en", "fr"], "status": "in_review"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_003", "subtitle_004"]}, "outputs": {"lines": ["subtitle_003", "subtitle_004"], "bundle_uri": "artifact://bundle/bundle-en-1", "tms_job_id": "TMS-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "2"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_073",
        instruction=(
            "Handle the VO subtitle timing QA and handoff for the villain threat: manage subtitle_005 (en) and subtitle_006 (ja) under string_key 'vo.villain.threat_01'. Execute policy-driven validation, packaging, and review registration using deterministic identifiers, and update the outcome on tracking ticket 'work_026' with the appropriate labels. Report the number of lines processed."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_005", "subtitle_006"]}, "outputs": {}, "status": "started"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_005", "locale": "en"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "en", "keys": ["subtitle_005"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "ja", "keys": ["subtitle_006"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "tms-vo-lines-subtitle_005-subtitle_006", "locales": ["en", "ja"], "status": "in_review"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_005", "subtitle_006"]}, "outputs": {"lines": ["subtitle_005", "subtitle_006"], "bundle_uris": {"en": "artifact://bundle/bundle-en-1", "ja": "artifact://bundle/bundle-ja-1"}}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "2"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_074",
        instruction=(
            "Coordinate the validation of subtitle timing for the NPC quest line across locales. Utilize subtitle_007 (en) and subtitle_008 (es) for string_key 'vo.npc.quest_01', maintain per-locale bundles, initiate a review job named 'tms-vo-lines-subtitle_007-subtitle_008' with locales ['en','es'], and revise labels on ticket 'work_026'; then provide the number of lines processed."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_007", "subtitle_008"]}, "outputs": {}, "status": "started"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_007", "locale": "en"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "en", "keys": ["vo.npc.quest_01"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "tms-vo-lines-subtitle_007-subtitle_008", "locales": ["en", "es"], "status": "in_review"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_007", "subtitle_008"]}, "outputs": {"lines": ["subtitle_007", "subtitle_008"]}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "2"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_075",
        instruction=(
            "Handle the QA of VO subtitle timing and transfer for the menu selection line across locales 'en' and 'zh'. Implement policy-based validation, packaging, and review registration using deterministic identifiers generated from the associated line IDs and string keys, and update tracking ticket 'work_026' with the correct labels. Provide the number of lines processed."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_009", "subtitle_010"]}, "outputs": {}, "status": "started"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_009", "locale": "en"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "en", "keys": ["subtitle_009"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "zh", "keys": ["subtitle_010"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "tms-vo-lines-subtitle_009-subtitle_010", "locales": ["en", "zh"], "status": "in_review"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_009", "subtitle_010"]}, "outputs": {"lines": ["subtitle_009", "subtitle_010"], "bundle_uris": {"en": "artifact://bundle/bundle-en-1", "zh": "artifact://bundle/bundle-zh-1"}, "tms_job_id": "TMS-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "2"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_076",
        instruction=(
            "Coordinate the consolidation of VO subtitle timing verification for English lines subtitle_001, subtitle_003, and subtitle_005. Use policy-based validation and compliant handoff with deterministic identifiers derived from the validated items, and document results on ticket 'work_026' with standard VO timing labels 'vo-subtitles' and 'timing-validated'. Provide the processed line count."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_001", "subtitle_003", "subtitle_005"]}, "outputs": {}, "status": "started"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_001", "locale": "en"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_003", "locale": "en"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_005", "locale": "en"}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "en", "keys": ["subtitle_001", "subtitle_003", "subtitle_005"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "tms-vo-lines-subtitle_001-subtitle_003-subtitle_005", "locales": ["en"], "status": "in_review"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_001", "subtitle_003", "subtitle_005"]}, "outputs": {"lines": ["subtitle_001", "subtitle_003", "subtitle_005"], "bundle_uri": "artifact://bundle/bundle-en-3", "tms_job_id": "TMS-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "3"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_077",
        instruction=(
            "Take charge of VO subtitle timing QA and handoff for the hero introduction in the locales 'de' and 'fr'. Utilize policy-driven validation, packaging, and review registration by employing deterministic identifiers derived from the pertinent line IDs and string keys, and document the outcome on tracking ticket 'work_026' with the suitable labels. Provide the number of lines that were processed."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_002", "subtitle_004"]}, "outputs": {}, "status": "started"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "de", "keys": ["subtitle_002"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "fr", "keys": ["subtitle_004"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "tms-vo-lines-subtitle_002-subtitle_004", "locales": ["de", "fr"], "status": "in_review"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_002", "subtitle_004"]}, "outputs": {"lines": ["subtitle_002", "subtitle_004"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "fr": "artifact://bundle/bundle-fr-1"}, "tms_job_id": "TMS-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "2"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_078",
        instruction=(
            "Confirm timing status and maintain the VO state for three locales without creating new identifiers. Validate subtitle_006 (ja), subtitle_008 (es), subtitle_010 (zh) using the exact string_keys from data: ja→'vo.villain.threat_01', es→'vo.npc.quest_01', zh→'vo.ui.menu_select'. Preserve per-locale bundles, register the review job 'tms-vo-lines-subtitle_006-subtitle_008-subtitle_010' with locales ['ja','es','zh'], and update work item 'work_026' by adding labels ['vo-subtitles','timing-validated']. Report the processed line count."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_006", "subtitle_008", "subtitle_010"]}, "outputs": {}, "status": "started"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "tms-vo-lines-subtitle_006-subtitle_008-subtitle_010", "locales": ["ja", "es", "zh"], "status": "in_review"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_006", "subtitle_008", "subtitle_010"]}, "outputs": {"lines": ["subtitle_006", "subtitle_008", "subtitle_010"]}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "3"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_079",
        instruction=(
            "Handle the task of VO subtitle timing QA and transfer for the English UI and quest lines. Implement policy-driven validation, packaging, and registration review using deterministic identifiers derived from the relevant line IDs and string keys, and document the outcome on tracking ticket 'work_026' with the correct labels. Report the number of lines processed."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_007", "subtitle_009"]}, "outputs": {}, "status": "started"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_007", "locale": "en"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_009", "locale": "en"}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "en", "keys": ["subtitle_007", "subtitle_009"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "tms-vo-lines-subtitle_007-subtitle_009", "locales": ["en"], "status": "in_review"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_007", "subtitle_009"]}, "outputs": {"lines": ["subtitle_007", "subtitle_009"], "bundle_uri": "artifact://bundle/bundle-en-2", "tms_job_id": "TMS-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "2"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_080",
        instruction=(
            "Ensure the validation of cross-locale hero intro timing and consistently maintain the outcomes. Utilize subtitle_001 (en→'vo.hero.intro_01') and subtitle_004 (fr→'vo.hero.intro_02'), maintain per-locale bundles, register the review job 'tms-vo-lines-subtitle_001-subtitle_004' with locales ['en','fr'], and update work item 'work_026' by incorporating labels ['vo-subtitles','timing-validated']. Provide the count of lines processed."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_001", "subtitle_004"]}, "outputs": {}, "status": "started"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_001", "locale": "en"}),
            Action(name="ValidateSubtitleTiming", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"]}),
            Action(name="WriteLocaleBundle", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="CreateTmsJob", kwargs={"bundle_name": "tms-vo-lines-subtitle_001-subtitle_004", "locales": ["en", "fr"], "status": "in_review"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_001", "subtitle_004"]}, "outputs": {"lines": ["subtitle_001", "subtitle_004"]}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "2"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_081",
        instruction=(
            "Handle the closure of the CI→Bug→PR loop for run_001 by utilizing the system's deterministic policy and stored evidence. Depend on the extracted signals and the canonical run-based fingerprint 'sig:run_001:first_failure'. Draft a PR and a linked ticket according to the policy and return 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_001"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_001", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_001"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_001"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_001:first_failure"}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "run_001"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "main", "run_id": "run_001"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_001"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_001", "patch_id": "FP-run_001", "message": "auto tentative fix for run run_001"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_001", "base": "main", "title": "auto fix build break run_001", "body": "summary for run run_001", "run_id": "run_001"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_001", "description": "Automated triage for run_001", "run_id": "run_001", "pr_number": 33}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "ENGINE-MIG-1", "fingerprint": "sig:run_001:first_failure"}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "run_001"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_001"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_082",
        instruction=(
            "Coordinate the loop closure for run_003 in accordance with policy using stored evidence. Utilize the extracted canonical fingerprint 'sig:run_003:first_failure' to draft a PR and a linked ticket, and return 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_003"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_003"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_003"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_003:first_failure"}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "run_003"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "main", "run_id": "run_003"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_003"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "message": "auto tentative fix for run run_003"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_003", "base": "main", "title": "auto fix build break run_003", "body": "summary for run run_003", "run_id": "run_003"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "ENGINE-MIG-1", "fingerprint": "sig:run_003:first_failure"}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "run_003"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_083",
        instruction=(
            "It is necessary to Close the CI→Bug→PR loop for run_005 employing deterministic policy and stored evidence. Draft a PR, initiate a linked ticket, confirm validation, and return 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_005"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_005"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_005"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:def456abc123789:first_failure"}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "def456abc123789"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "main", "run_id": "run_005"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_005", "first_bad_commit": "def456abc123789"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "message": "auto tentative fix for run run_005"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_005", "base": "main", "title": "auto fix build break run_005", "body": "summary for run run_005", "run_id": "run_005"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "ENGINE-MIG-1", "fingerprint": "sig:def456abc123789:first_failure"}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "test-integration-linux"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_084",
        instruction=(
            "It is essential to close the CI→Bug→PR loop for run_007 utilizing deterministic policy and stored evidence. Prepare a draft PR, open a linked ticket, verify validation, and return 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_007"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_007"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_007"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_007:first_failure"}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "run_007"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "main", "run_id": "run_007"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_007"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "message": "auto tentative fix for run run_007"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_007", "base": "main", "title": "auto fix build break run_007", "body": "summary for run run_007", "run_id": "run_007"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "ENGINE-MIG-1", "fingerprint": "sig:run_007:first_failure"}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "run_007"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_085",
        instruction=(
            "Ensure the closure of the CI→Bug→PR cycle for run_010 utilizing a deterministic approach and available evidence. The CI service in use is 'github_actions', and the test_target required for validation is 'run_010'. Prepare a draft PR, initiate a related ticket, reflect on validation in a deterministic manner, and return 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_010"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_010", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_010"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_010"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_010:first_failure"}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "run_010"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "main", "run_id": "run_010"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_010"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_010", "patch_id": "FP-run_010", "message": "auto tentative fix for run run_010"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_010", "base": "main", "title": "auto fix build break run_010", "body": "summary for run run_010", "run_id": "run_010"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_010", "description": "Automated triage for run_010", "run_id": "run_010", "pr_number": 33}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "ENGINE-MIG-1", "fingerprint": "sig:run_010:first_failure"}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "run_010"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_010"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_086",
        instruction=(
            "Ensure the maintenance of CI→Bug→PR traceability for run_002 (successful run) by employing a deterministic method and existing evidence. Prepare a draft PR, initiate a corresponding ticket, reflect validation, and return 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_002"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_002", "status": "success"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_002"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "main", "run_id": "run_002"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_002", "base": "main", "title": "auto fix build break run_002", "body": "summary for run run_002", "run_id": "run_002"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_002", "description": "Automated triage for run_002", "run_id": "run_002", "pr_number": 33}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "ENGINE-MIG-1"}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "run_002"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_002"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_087",
        instruction=(
            "Ensure the CI→Bug→PR traceability is maintained for run_004 by applying a deterministic policy and using stored evidence. Draft a PR, initiate a linked ticket, validate the necessary steps, and revert with 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_004"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_004", "status": "success"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_004"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "artifact-index", "inputs": {"run_id": "run_004"}, "outputs": {}, "status": "completed"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "main", "run_id": "run_004"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_004", "base": "main", "title": "auto fix build break run_004", "body": "summary for run run_004", "run_id": "run_004"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_004", "description": "Automated triage for run_004", "run_id": "run_004", "pr_number": 33}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "ENGINE-MIG-1"}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "run_004"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "build-metrics", "inputs": {"run_id": "run_004"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_004"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_088",
        instruction=(
            "Complete the CI→Bug→PR loop for run_008 utilizing a deterministic policy and stored evidence. Draft a PR, initiate a linked ticket, validate the necessary steps, and revert with 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_008"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_008", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_008"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_008"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_008:first_failure"}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "run_008"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "main", "run_id": "run_008"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_008"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_008", "patch_id": "FP-run_008", "message": "auto tentative fix for run run_008"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_008", "base": "main", "title": "auto fix build break run_008", "body": "summary for run run_008", "run_id": "run_008"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_008", "description": "Automated triage for run_008", "run_id": "run_008", "pr_number": 33}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "ENGINE-MIG-1", "fingerprint": "sig:run_008:first_failure"}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "run_008"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_008"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_089",
        instruction=(
            "Handle the maintenance of CI→Bug→PR traceability for run_009 under deterministic policy utilizing only stored evidence. Make sure the CI event status is consistent with the database record for run_009, coordinate the draft PR and linked ticket with deterministic identifiers, document the validation status, and return 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_009"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_009", "status": "success", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "security-scan-windows"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_009"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "main", "run_id": "run_009"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_009", "base": "main", "title": "auto fix build break run_009", "body": "summary for run run_009", "run_id": "run_009"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_009", "description": "Automated triage for run_009", "run_id": "run_009", "pr_number": 33}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "ENGINE-MIG-1"}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "run_009"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_009"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1", "status": "success"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_090",
        instruction=(
            "You need to complete the CI→Bug→PR loop for run_006 using deterministic policy and stored evidence. Draft a PR, open a linked ticket, document validation, and return 33."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_006"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_006", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_006"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_006"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_006:first_failure"}),
            Action(name="EnumerateSuspects", kwargs={"failing_sha": "run_006"}),
            Action(name="OpenAutoBranch", kwargs={"base_ref": "main", "run_id": "run_006"}),
            Action(name="ProposeFixPatch", kwargs={"run_id": "run_006"}),
            Action(name="CommitPatchToBranch", kwargs={"branch_ref": "auto/fix-run_006", "patch_id": "FP-run_006", "message": "auto tentative fix for run run_006"}),
            Action(name="OpenDraftPullRequest", kwargs={"head": "auto/fix-run_006", "base": "main", "title": "auto fix build break run_006", "body": "summary for run run_006", "run_id": "run_006"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_006", "description": "Automated triage for run_006", "run_id": "run_006", "pr_number": 33}),
            Action(name="ComputeImpactScore", kwargs={"ticket_key": "ENGINE-MIG-1", "fingerprint": "sig:run_006:first_failure"}),
            Action(name="RunValidationChecks", kwargs={"pr_number": 33, "test_target": "run_006"}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_006"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "33"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_091",
        instruction=(
            "Handle the escalation of release-blockers and the recurrence management for run_001. By using solely the JSON database and deterministic policy, depend on stored evidence (e.g., extracted failure signatures and prior incidents) to associate the new failure with its canonical parent when suitable, modify the work item’s status and labels to signify escalation, and guarantee a comprehensive audit trail via automation runs. Refrain from creating identifiers; all arguments should be clear and derived from this run_id or data. Return 'ok'."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_001"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_001", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_001"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_001"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_001:first_failure"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_001", "description": "Automated triage for run_001", "run_id": "run_001"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_001"}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_001"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_001:first_failure"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "ok"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_092",
        instruction=(
            "Coordinate the deterministic escalation of a potential release-blocker for run_003 by utilizing the extracted signature and previous incidents, associating the event with the canonical ticket when applicable, updating status/labels to represent escalation, and documenting all actions for auditability. Employ only database values and deterministic formats. Return 'ok'."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_003"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_003"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_003"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_003:first_failure"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated"}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_003"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_003:first_failure"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "ok"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_093",
        instruction=(
            "Handle deterministic recurrence escalation for run_013 utilizing solely stored evidence and policy, not step lists. Ensure to associate with the canonical incident for this fingerprint when deterministically available (do not create IDs). Adopt the labels 'release-blocker' and 'recurrence,' adjust the state to 'Escalated,' guarantee auditability through a documented automation run, and provide 'ok' as a response."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_013"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_013", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_013"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_013"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_013:first_failure"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_013", "description": "Automated triage for run_013", "run_id": "run_013"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_013"}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_013"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_013:first_failure"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "ok"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_094",
        instruction=(
            "Coordinate the deterministic escalation of recurrence for run_012 by employing the extracted signature and similar incidents to connect to the canonical ticket, and update the state and labels for release-blocker visibility, while maintaining a complete automation run. Only arguments from deterministic, database sources should be used. Return 'ok'."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_012"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_012", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_012"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_012"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_012:first_failure"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_012", "description": "Automated triage for run_012", "run_id": "run_012"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated"}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_012"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_012:first_failure"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "ok"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_095",
        instruction=(
            "Handle deterministic CI triage and recurrence escalation for run_011 within the domain policy framework, utilizing exclusively database-driven values. Ensure canonical linkage where applicable, reflect escalation through labels/state, maintain a complete automation audit trail, and respond with 'ok'. Do not create identifiers."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_011"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_011", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_011"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_011"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_011:first_failure"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_011", "description": "Automated triage for run_011", "run_id": "run_011"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_011"}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_011"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_011:first_failure"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "ok"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_096",
        instruction=(
            "Coordinate deterministic release-blocker escalation on run_010 using solely database-provided evidence. Connect to its canonical incident when applicable (do not create IDs), apply the labels 'release-blocker' and 'recurrence', set the state to 'Escalated', and record the automation run to keep an audit trail. All inputs must be deterministically sourced. Respond with 'ok'."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_010"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_010", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_010"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_010"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_010:first_failure"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_010", "description": "Automated triage for run_010", "run_id": "run_010"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_010"}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_010"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_010:first_failure"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "ok"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_097",
        instruction=(
            "Handle deterministic recurrence escalation for run_008 by precisely deriving the failure signature, deterministically associating it with its canonical parent, and updating the work item’s labels/state to indicate a release-blocker. You must record all automation steps for audit purposes. Ensure all arguments are obtained from the run or database. Return 'ok'."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_008"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_008", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_008"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_008"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_008:first_failure"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_008", "description": "Automated triage for run_008", "run_id": "run_008"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_008"}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_008"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_008:first_failure"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "ok"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_098",
        instruction=(
            "Coordinate release-blocker escalation for run_007 in adherence to deterministic policy. With values drawn exclusively from the database, deterministically determine the failure signature, retrieve any similar incidents, link to the canonical incident if deterministically possible, and represent the escalation through labels/state, ensuring a thorough automation audit trail. Return 'ok'."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_007"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_007"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_007"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_007:first_failure"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_007"}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_007"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_007:first_failure"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "ok"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_099",
        instruction=(
            "Handle the deterministic escalation of the recurrence for run_006 using policy and available evidence (avoid step-by-step instructions). Connect to the canonical incident for this fingerprint when relevant, use the labels 'release-blocker' and 'recurrence', switch the state to 'Escalated', and document a full automation run. All arguments must be obtained from the run_id or database. Provide 'ok' as the return value."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_006"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_006", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_006"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_006"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_006:first_failure"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_006", "description": "Automated triage for run_006", "run_id": "run_006"}),

            Action(name="UpdateTicketFields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_006"}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_006"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_006:first_failure"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "ok"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_100",
        instruction=(
            "You are responsible for detecting recurrences for run_005 in accordance with the deterministic policy. Connect to the canonical incident for this fingerprint when appropriate, escalate using the labels 'release-blocker' and 'recurrence', change the state to 'Escalated', and keep a full record of the automation run. Ensure IDs are not invented; all arguments should be derived deterministically. Provide 'ok' as the return value."
        ),
        actions=[
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_005"}, "outputs": {}, "status": "started"}),
            Action(name="ReceiveCiEvent", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure"}),
            Action(name="AttachRunArtifacts", kwargs={"run_id": "run_005"}),
            Action(name="ExtractFailureSignals", kwargs={"run_id": "run_005"}),
            Action(name="FindSimilarIncidents", kwargs={"signature": "sig:run_005:first_failure"}),
            Action(name="GetProjectKey", kwargs={}),
            Action(name="CreateOrUpdateTicket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005"}),
            Action(name="UpdateTicketFields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_005"}}),
            Action(name="RecordAutomationRun", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_005"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_005:first_failure"}, "status": "completed"}),
            Action(name="ReturnScalar", kwargs={"value": "ok"}),
        ],
        outputs=[]
    ),

]
