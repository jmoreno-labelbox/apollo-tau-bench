from domains.dto import Task, Action


TASKS = [
    Task(
        annotator="0",
        user_id="v2_task_001",
        instruction=(
            "Handle CI triage tasks related to the game-engine repository. Address the issue with the failed Windows build run_001 on the branch feature/new-renderer at commit abc123def456789 (job build-windows-x64). Follow the CI Build Failure Protocol V2 and utilize policy templates. Collect and link evidence, initiate a draft PR on 'auto/fix-run_001', generate the ENGINE-MIG work item associated with the PR, start smoke validation, and provide just the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_001", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "build-windows-x64"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_001"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_001"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_001"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_001"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_001"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_001"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_001", "patch_id": "FP-run_001", "run_id": "run_001"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_001", "base": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_001", "description": "Automated triage for run_001", "run_id": "run_001", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_001"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_002",
        instruction=(
            "Coordinate CI triage for the game-engine. The run_003 (job test-unit-windows) on branch feature/new-renderer at commit abc123def456789 encountered a failure. Utilize the CI Build Failure Protocol V2 to maintain signals, conduct bisect using the run's repro command, prepare a minimal fix, initiate a draft PR, lodge a BUILD-MOD ticket, authenticate the draft, and deliver only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_003"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_003"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_003"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_003"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_003"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_003"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "run_id": "run_003"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "BUILD-MOD", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_003",
        instruction=(
            "As the CI triage owner, you need to manage failed integration tests for run run_005 (job test-integration-linux) on branch feature/new-renderer at commit def456abc123789. Employ Protocol V2 for end-to-end processing, adhere to deterministic templates, categorize under ENGINE-MIG, and provide solely the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_005"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_005"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_005"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_005"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_005"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_005"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_004",
        instruction=(
            "You are required to coordinate performance regression triage for run run_007 (job performance-test-windows) on branch feature/new-renderer at commit abc123def456789. Implement the CI Build Failure Protocol V2, prepare a minimal fix, initiate a draft PR, generate a BUILD-MOD ticket, validate, and deliver only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_007"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_007"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_007"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_007"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_007"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_007"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "run_id": "run_007"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "BUILD-MOD", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_005",
        instruction=(
            "Ensure oversight of CI triage. Address the failed staging deployment run run_010 (job deploy-staging-windows) on feature/new-renderer at commit abc123def456789. Implement Protocol V2 utilizing deterministic templates, initiate a draft PR, create an ENGINE-MIG ticket, validate, and provide solely the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_010", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "deploy-staging-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_010"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_010"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_010"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_010"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_010"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_010"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_010", "patch_id": "FP-run_010", "run_id": "run_010"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_010", "base": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_010", "description": "Automated triage for run_010", "run_id": "run_010", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_010"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    # Repeat on other failure categories/routing projects to ensure diversity while staying deterministic
    Task(
        annotator="0",
        user_id="v2_task_006",
        instruction=(
            "In the context of governance, confirm that the run run_001 build failure is triaged under BUILD-MOD following the same CI Build Failure Protocol V2 and template constraints. Generate the draft PR, associate the ticket, validate, and supply only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_001", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "build-windows-x64"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_001"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_001"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_001"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_001"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_001"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_001"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_001", "patch_id": "FP-run_001", "run_id": "run_001"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_001", "base": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "BUILD-MOD", "summary": "CI failure run_001", "description": "Automated triage for run_001", "run_id": "run_001", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_001"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_007",
        instruction=(
            "Handle the triage of unit test failure once more for run run_003 under ENGINE-MIG to ensure cross-project rules are applied deterministically. Follow Protocol V2 completely, open a draft PR, create a ticket, validate, and return solely the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_003"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_003"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_003"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_003"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_003"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_003"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "run_id": "run_003"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_008",
        instruction=(
            "Coordinate the resolution of run run_005 integration failure under BUILD-MOD by employing Protocol V2 with only deterministic fields. Initiate a draft PR and linked ticket, validate, and provide just the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_005"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_005"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_005"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_005"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_005"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_005"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "BUILD-MOD", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_009",
        instruction=(
            "Handle the re-execution of performance triage for run run_007 within ENGINE-MIG using CI Build Failure Protocol V2 and deterministic templates. Prepare a draft PR, associate the ticket, complete validation, and provide only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_007"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_007"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_007"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_007"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_007"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_007"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "run_id": "run_007"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_010",
        instruction=(
            "Coordinate the closure of the loop on run run_010 by implementing CI Build Failure Protocol V2 with BUILD-MOD routing. Apply policy templates, document all links, initiate a draft PR, develop the ticket, validate the draft, and provide only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_010", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "deploy-staging-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_010"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_010"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_010"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_010"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_010"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_010"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_010", "patch_id": "FP-run_010", "run_id": "run_010"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_010", "base": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "BUILD-MOD", "summary": "CI failure run_010", "description": "Automated triage for run_010", "run_id": "run_010", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_010"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_011",
        instruction=(
            "Handle a unit test failure for run run_003 (job test-unit-windows) on the branch feature/new-renderer at commit abc123def456789. Adhere strictly to the CI Build Failure Protocol V2, maintain signals, bisect with the job repro, initiate a draft PR, generate a TEST-INFRA ticket, initiate validation, and provide only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_003"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_003"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_003"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_003"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_003"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_003"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "run_id": "run_003"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "TEST-INFRA", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "TEST-INFRA-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_012",
        instruction=(
            "Address the same unit test failure for run run_003 (test-unit-windows) under PERF-MON governance. Follow Protocol V2, prepare a draft PR, generate the PERF-MON ticket utilizing policy templates, initiate validation, and supply only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_003"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_003"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_003"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_003"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_003"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_003"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "run_id": "run_003"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "PERF-MON", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "PERF-MON-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_013",
        instruction=(
            "Handle integration test failures for run run_005 (job test-integration-linux) on feature/new-renderer at commit def456abc123789. Follow Protocol V2, initiate a draft PR, make a MULTI-PLAT ticket, validate, and provide only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_005"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_005"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_005"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_005"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_005"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_005"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "MULTI-PLAT", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "MULTI-PLAT-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_014",
        instruction=(
            "You need to address run run_005 integration failures under the supervision of API-GATEWAY. Follow Protocol V2, start a draft PR, generate the API-GATEWAY ticket, initiate validation, and return solely the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_005"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_005"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_005"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_005"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_005"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_005"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "API-GATEWAY", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "API-GATEWAY-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_015",
        instruction=(
            "Address the integration test issues for run run_005 under the DB-UPGRADE policy. Adhere completely to Protocol V2, initiate a draft PR, generate a DB-UPGRADE ticket, validate the process, and submit solely the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_005"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_005"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_005"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_005"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_005"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_005"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "DB-UPGRADE", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "DB-UPGRADE-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_016",
        instruction=(
            "Manage the performance test failure triage for run run_007 (job performance-test-windows) on branch feature/new-renderer at commit abc123def456789. Implement Protocol V2, start a draft PR, initiate a PERF-MON ticket, ensure validation, and provide only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_007"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_007"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_007"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_007"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_007"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_007"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "run_id": "run_007"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "PERF-MON", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "PERF-MON-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_017",
        instruction=(
            "Triaging performance test failures for run run_007 under GAME-ANALYTICS is required. Utilize Protocol V2, initiate a draft PR, make a GAME-ANALYTICS ticket, carry out validation, and provide solely the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_007"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_007"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_007"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_007"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_007"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_007"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "run_id": "run_007"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "GAME-ANALYTICS", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "GAME-ANALYTICS-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_018",
        instruction=(
            "Re-running the performance test triage for run run_007 under BUILD-MOD needs to be coordinated to ensure coverage. Adhere to Protocol V2 and use policy templates, start a draft PR, generate a BUILD-MOD ticket, validate, and deliver only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_007"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_007"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_007"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_007"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_007"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_007"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "run_id": "run_007"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "BUILD-MOD", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_019",
        instruction=(
            "You are to reconcile unit test failure triage for run run_003 under ENGINE-MIG. Handle Protocol V2, open a draft PR, create an ENGINE-MIG ticket, validate, and provide only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_003"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_003"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_003"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_003"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_003"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_003"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "run_id": "run_003"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_020",
        instruction=(
            "You are required to finalize integration test failure triage for run run_005 under COST-OPT oversight. Adhere strictly to Protocol V2, open a draft PR, create a COST-OPT ticket, validate, and submit only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_005"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_005"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_005"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_005"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_005"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_005"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "COST-OPT", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "COST-OPT-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_021",
        instruction=(
            "Handle a crash-related build failure for run run_001 on the branch feature/new-renderer at commit abc123def456789 (job build-windows-x64). Follow Protocol V2 focusing on reduced logs, symbolication, and incident correlation; next, initiate a draft PR, create a GAME-SEC ticket, trigger validation, and provide only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_001", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "build-windows-x64"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_001"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_001"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_001"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_001"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_001"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_001"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_001", "patch_id": "FP-run_001", "run_id": "run_001"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_001", "base": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "GAME-SEC", "summary": "CI failure run_001", "description": "Automated triage for run_001", "run_id": "run_001", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_001"}, "outputs": {"pr_number": 33, "ticket_key": "GAME-SEC-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_022",
        instruction=(
            "Handle a crash-related test failure for run run_003 (test-unit-windows) on the feature/new-renderer at commit abc123def456789 by employing symbolication and incident correlation as outlined in Protocol V2 for signature='sig:abc123def456789:first_failure'; start a draft PR, create a REG-SEC ticket, execute validation, and submit only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_003"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_003"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_003"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_003"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_003"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_003"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "run_id": "run_003"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "REG-SEC", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "REG-SEC-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_023",
        instruction=(
            "Handle a crash-context integration error for run run_005 (test-integration-linux) on feature/new-renderer at commit def456abc123789 by conducting symbolication and correlation according to policy; initiate a draft PR, generate a NET-SEC ticket, confirm, and provide solely the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_005"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_005"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_005"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_005"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_005"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_005"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "NET-SEC", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "NET-SEC-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_024",
        instruction=(
            "Address a crash-context performance regression for run run_007 (performance-test-windows) on feature/new-renderer at commit abc123def456789 employing Protocol V2 utilizing symbolication and incident correlation; begin a draft PR, create a PERF-MON ticket, validate, and submit only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_007"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_007"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_007"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_007"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_007"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_007"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "run_id": "run_007"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "PERF-MON", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "PERF-MON-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_025",
        instruction=(
            "Handle a crash-context deployment failure for run run_010 (deploy-staging-windows) on feature/new-renderer at commit abc123def456789, focusing on symbolication and correlation; initiate a draft PR, generate a DR-IMPL ticket, perform validation, and provide only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_010", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "deploy-staging-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_010"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_010"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_010"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_010"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_010"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_010"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_010", "patch_id": "FP-run_010", "run_id": "run_010"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_010", "base": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "DR-IMPL", "summary": "CI failure run_010", "description": "Automated triage for run_010", "run_id": "run_010", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_010"}, "outputs": {"pr_number": 33, "ticket_key": "DR-IMPL-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_026",
        instruction=(
            "Coordinate the re-execution of Protocol V2 crash triage for run run_001 on branch feature/new-renderer at commit abc123def456789 (job build-windows-x64). Utilize the crash triage policy areas (reduced log window, symbolication, similar-incident lookup), then initiate a draft PR, generate an EDGE-PLAT ticket, start smoke validation for the related PR, and deliver only the draft PR number."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_001", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "build-windows-x64"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_001"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_001"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_001"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_001"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_001"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_001"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_001", "patch_id": "FP-run_001", "run_id": "run_001"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_001", "base": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "EDGE-PLAT", "summary": "CI failure run_001", "description": "Automated triage for run_001", "run_id": "run_001", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_001"}, "outputs": {"pr_number": 33, "ticket_key": "EDGE-PLAT-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_027",
        instruction=(
            "You need to handle crash symbolication triage for run run_003 and subsequently open a draft PR, create an API-GATEWAY ticket, validate, and provide only the draft PR number, strictly following Protocol V2."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_003"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_003"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_003"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_003"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_003"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_003"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "run_id": "run_003"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "API-GATEWAY", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "API-GATEWAY-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_028",
        instruction=(
            "You need to manage crash-context integration triage for run run_005 and then open a draft PR, create a DB-UPGRADE ticket, validate, and supply only the draft PR number, all per Protocol V2."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_005"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_005"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_005"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_005"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_005"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_005"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "DB-UPGRADE", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "DB-UPGRADE-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_029",
        instruction=(
            "You are required to handle crash symbolication and correlation for run run_007 and then initiate a draft PR, generate a GAME-ANALYTICS ticket, validate, and return solely the draft PR number as per Protocol V2."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_007"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_007"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_007"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_007"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_007"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_007"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "run_id": "run_007"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "GAME-ANALYTICS", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "GAME-ANALYTICS-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_030",
        instruction=(
            "You need to manage crash symbolication triage for run run_010, after which you open a draft PR, produce an IAC-MIG ticket, validate, and provide only the draft PR number, adhering strictly to Protocol V2."
        ),
        actions=[
            Action(name="IngestCiWebhookV2", kwargs={"provider": "github_actions", "run_id": "run_010", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "deploy-staging-windows"}),
            Action(name="GuardrailValidateSenderV2", kwargs={"run_id": "run_010"}),
            Action(name="AttachArtifactsIndexV2", kwargs={"run_id": "run_010"}),
            Action(name="ReduceLogWindowV2", kwargs={"run_id": "run_010"}),
            Action(name="SymbolicateMinidumpV2", kwargs={"run_id": "run_010"}),
            Action(name="SimilarIncidentLookupV2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="EnumerateSuspectsV2", kwargs={"run_id": "run_010"}),
            Action(name="LaunchTargetedBisectV2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="DraftFixDiffV2", kwargs={"run_id": "run_010"}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-run_010", "patch_id": "FP-run_010", "run_id": "run_010"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-run_010", "base": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "IAC-MIG", "summary": "CI failure run_010", "description": "Automated triage for run_010", "run_id": "run_010", "pr_number": 33}),
            Action(name="TriggerSmokeValidationV2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_010"}, "outputs": {"pr_number": 33, "ticket_key": "IAC-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_031",
        instruction=(
            "Handle the asset QA intake related to commit abc123def456789 on branch feature/new-renderer. Validate the complete set of changes against texture and engine budgets, create previews, stage a deterministic draft change linked to a GAME-ANALYTICS work item, and return solely the draft PR number."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/models/characters/hero_character.fbx",
                "assets/textures/characters/hero_character_normal.png",
                "assets/animations/characters/hero_idle.fbx",
                "assets/models/environment/castle_tower.fbx",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png",
                "assets/materials/environment/castle_tower.mtl",
                "assets/audio/sfx/hero_sword_swing.wav",
                "assets/audio/music/main_theme.ogg"
            ]}),
            Action(name="EnforceTexturePoliciesV2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/animations/characters/hero_idle.fbx",
                "assets/models/environment/castle_tower.fbx"
            ], "scene": "BudgetScene:abc123def456789"}),
            Action(name="RenderTurntableV2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/animations/characters/hero_idle.fbx",
                "assets/models/environment/castle_tower.fbx"
            ]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []},
                {"file": "assets/models/characters/hero_character.fbx", "issues": []},
                {"file": "assets/textures/characters/hero_character_normal.png", "issues": []},
                {"file": "assets/animations/characters/hero_idle.fbx", "issues": []},
                {"file": "assets/models/environment/castle_tower.fbx", "issues": []},
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []},
                {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []},
                {"file": "assets/materials/environment/castle_tower.mtl", "issues": []},
                {"file": "assets/audio/sfx/hero_sword_swing.wav", "issues": []},
                {"file": "assets/audio/music/main_theme.ogg", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "ok": True},
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": [
                "assets/models/characters/hero_character.fbx",
                "assets/animations/characters/hero_idle.fbx",
                "assets/models/environment/castle_tower.fbx"
            ], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/3", "stills_uris": ["artifact://still/1", "artifact://still/2", "artifact://still/3"]}}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "assetqa_abc123def456789"}),
            Action(name="DeterministicAutofixV2", kwargs={"qa_json": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []},
                {"file": "assets/models/characters/hero_character.fbx", "issues": []},
                {"file": "assets/textures/characters/hero_character_normal.png", "issues": []},
                {"file": "assets/animations/characters/hero_idle.fbx", "issues": []},
                {"file": "assets/models/environment/castle_tower.fbx", "issues": []},
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []},
                {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []},
                {"file": "assets/materials/environment/castle_tower.mtl", "issues": []},
                {"file": "assets/audio/sfx/hero_sword_swing.wav", "issues": []},
                {"file": "assets/audio/music/main_theme.ogg", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "ok": True},
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ]}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-assetqa_abc123def456789", "patch_id": "AF-1", "run_id": "assetqa_abc123def456789"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-assetqa_abc123def456789", "base": "feature/new-renderer", "run_id": "assetqa_abc123def456789"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "GAME-ANALYTICS", "summary": "asset_qa:commit=abc123def456789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "assetqa_abc123def456789", "pr_number": 33}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=abc123def456789", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheckV2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "abc123def456789"}, "outputs": {"pr_number": 33, "ticket_key": "GAME-ANALYTICS-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_032",
        instruction=(
            "Oversee the environment-focused asset QA intake concerning commit def456abc123789 on branch feature/new-renderer. Produce a reviewable QA bundle for the modified environment assets with previews, stage a deterministic draft change tied to a BUILD-MOD work item, and provide only the draft PR number."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": [
                "assets/models/environment/castle_tower.fbx",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png",
                "assets/materials/environment/castle_tower.mtl"
            ]}),
            Action(name="EnforceTexturePoliciesV2", kwargs={"files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="RenderTurntableV2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [
                {"file": "assets/models/environment/castle_tower.fbx", "issues": []},
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []},
                {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []},
                {"file": "assets/materials/environment/castle_tower.mtl", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/models/environment/castle_tower.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "assetqa_def456abc123789"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-assetqa_def456abc123789", "patch_id": "AF-assetqa_def456abc123789", "run_id": "assetqa_def456abc123789"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-assetqa_def456abc123789", "base": "feature/new-renderer", "run_id": "assetqa_def456abc123789"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "BUILD-MOD", "summary": "asset_qa:commit=def456abc123789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "assetqa_def456abc123789", "pr_number": 33}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=def456abc123789", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheckV2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "def456abc123789"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_033",
        instruction=(
            "Ensure the character normal-map QA is conducted in relation to commit abc123def456789 on branch feature/new-renderer. Assemble a reviewable QA package for the affected textures, create previews, prepare a deterministic draft associated with an ENGINE-MIG work item, and provide solely the draft PR number."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": [
                "assets/textures/characters/hero_character_normal.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="EnforceTexturePoliciesV2", kwargs={"files": [
                "assets/textures/characters/hero_character_normal.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": [
                "assets/textures/characters/hero_character_normal.png",
                "assets/textures/environment/castle_tower_normal.png"
            ], "scene": "BudgetScene:abc123def456789"}),
            Action(name="RenderTurntableV2", kwargs={"files": [
                "assets/textures/characters/hero_character_normal.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="DeterministicAutofixV2", kwargs={"qa_json": [
                {"file": "assets/textures/characters/hero_character_normal.png"},
                {"file": "assets/textures/environment/castle_tower_normal.png"}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [
                {"file": "assets/textures/characters/hero_character_normal.png", "issues": []},
                {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": [
                "assets/textures/characters/hero_character_normal.png",
                "assets/textures/environment/castle_tower_normal.png"
            ], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/2", "stills_uris": ["artifact://still/1", "artifact://still/2"]}}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "assetqa_abc123def456789"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-assetqa_abc123def456789", "patch_id": "AF-1", "run_id": "assetqa_abc123def456789"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-assetqa_abc123def456789", "base": "feature/new-renderer", "run_id": "assetqa_abc123def456789"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "ENGINE-MIG", "summary": "asset_qa:commit=abc123def456789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "assetqa_abc123def456789", "pr_number": 33}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=abc123def456789", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheckV2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "abc123def456789"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_034",
        instruction=(
            "Conduct asset QA for environment textures at commit def456abc123789. Utilize Protocol V2 in a deterministic manner, strictly adhere to texture budgets, release the QA results, initiate a draft PR, generate a MULTI-PLAT ticket, and furnish only the draft PR number."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png", "assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="EnforceTexturePoliciesV2", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png", "assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png", "assets/textures/environment/castle_tower_diffuse.png"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="RenderTurntableV2", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png", "assets/textures/environment/castle_tower_diffuse.png"]}),
            Action(name="DeterministicAutofixV2", kwargs={"qa_json": [
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []},
                {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [{"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}, {"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []}], "tex_report": [{"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}, {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True}], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/textures/environment/castle_tower_normal.png", "assets/textures/environment/castle_tower_diffuse.png"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/2", "stills_uris": ["artifact://still/1", "artifact://still/2"]}}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "main", "run_id": "def456abc123789"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-def456abc123789", "patch_id": "AF-1", "run_id": "def456abc123789"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-def456abc123789", "base": "main", "run_id": "def456abc123789"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "MULTI-PLAT", "summary": "asset_qa:commit=def456abc123789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "def456abc123789", "pr_number": 33}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=def456abc123789", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheckV2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "def456abc123789"}, "outputs": {"pr_number": 33, "ticket_key": "MULTI-PLAT-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_035",
        instruction=(
            "Handle the character model-and-texture QA concerning commit abc123def456789. Assemble an all-inclusive QA bundle featuring previews for the model and its textures, arrange a deterministic draft tied to ENGINE-MIG, and supply only the draft PR number."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="EnforceTexturePoliciesV2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": ["assets/models/characters/hero_character.fbx"], "scene": "BudgetScene:abc123def456789"}),
            Action(name="RenderTurntableV2", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="DeterministicAutofixV2", kwargs={"qa_json": [
                {"file": "assets/models/characters/hero_character.fbx"},
                {"file": "assets/textures/characters/hero_character_diffuse.png"},
                {"file": "assets/textures/characters/hero_character_normal.png"}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "ok": True},
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True}
            ]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [
                {"file": "assets/models/characters/hero_character.fbx", "issues": []},
                {"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []},
                {"file": "assets/textures/characters/hero_character_normal.png", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "ok": True},
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": ["assets/models/characters/hero_character.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "main", "run_id": "assetqa_abc123def456789"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-assetqa_abc123def456789", "patch_id": "AF-1", "run_id": "assetqa_abc123def456789"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-assetqa_abc123def456789", "base": "main", "run_id": "assetqa_abc123def456789"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "ENGINE-MIG", "summary": "asset_qa:commit=abc123def456789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "assetqa_abc123def456789", "pr_number": 33}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=abc123def456789", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheckV2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "abc123def456789"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_036",
        instruction=(
            "Coordinate the material QA related to commit def456abc123789. Generate a precise QA bundle, initiate an API-GATEWAY work item connected to the draft, and provide just the draft PR number."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/models/characters/hero_character.fbx",
                "assets/textures/characters/hero_character_normal.png",
                "assets/animations/characters/hero_idle.fbx",
                "assets/models/environment/castle_tower.fbx",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png",
                "assets/materials/environment/castle_tower.mtl",
                "assets/audio/sfx/hero_sword_swing.wav",
                "assets/audio/music/main_theme.ogg"
            ]}),
            Action(name="EnforceTexturePoliciesV2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="RenderTurntableV2", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [{"file": "assets/materials/environment/castle_tower.mtl", "issues": []}], "tex_report": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "ok": True},
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/materials/environment/castle_tower.mtl"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "main", "run_id": "def456abc123789"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-def456abc123789", "base": "main", "run_id": "def456abc123789"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "API-GATEWAY", "summary": "asset_qa:commit=def456abc123789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "def456abc123789", "pr_number": 33}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=def456abc123789", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheckV2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "def456abc123789"}, "outputs": {"pr_number": 33, "ticket_key": "API-GATEWAY-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_037",
        instruction=(
            "Handle the audio QA related to commit abc123def456789. Create a comprehensive QA bundle for the altered audio assets, initiate a GAME-ANALYTICS work item connected to the draft, and provide only the draft PR number."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav", "assets/audio/music/main_theme.ogg"]}),
            Action(name="RenderAudioPreviewV2", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav", "assets/audio/music/main_theme.ogg"]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav", "assets/audio/music/main_theme.ogg"], "scene": "BudgetScene:abc123def456789"}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [{"file": "assets/audio/sfx/hero_sword_swing.wav", "issues": []}, {"file": "assets/audio/music/main_theme.ogg", "issues": []}], "tex_report": [], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": ["assets/audio/sfx/hero_sword_swing.wav", "assets/audio/music/main_theme.ogg"], "violations": []}, "previews": {"audio_preview_uri": "artifact://audio_preview/2"}}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "main", "run_id": "abc123def456789"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-abc123def456789", "base": "main", "run_id": "abc123def456789"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "GAME-ANALYTICS", "summary": "asset_qa:commit=abc123def456789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "abc123def456789", "pr_number": 33}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=abc123def456789", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheckV2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "abc123def456789"}, "outputs": {"pr_number": 33, "ticket_key": "GAME-ANALYTICS-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_038",
        instruction=(
            "Coordinate the animation QA associated with commit abc123def456789. Assemble a complete QA bundle including previews, associate a BUILD-MOD work item with the draft, and submit only the draft PR number."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"], "scene": "BudgetScene:abc123def456789"}),
            Action(name="RenderTurntableV2", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="DeterministicAutofixV2", kwargs={"qa_json": [{"file": "assets/animations/characters/hero_idle.fbx"}], "tex_report": []}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [{"file": "assets/animations/characters/hero_idle.fbx", "issues": []}], "tex_report": [], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": ["assets/animations/characters/hero_idle.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "main", "run_id": "assetqa_abc123def456789"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-assetqa_abc123def456789", "patch_id": "AF-1", "run_id": "assetqa_abc123def456789"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-assetqa_abc123def456789", "base": "main", "run_id": "assetqa_abc123def456789"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "BUILD-MOD", "summary": "asset_qa:commit=abc123def456789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "assetqa_abc123def456789", "pr_number": 33}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=abc123def456789", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheckV2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "abc123def456789"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_039",
        instruction=(
            "Handle the QA of the environment texture connected to commit def456abc123789 on branch feature/new-renderer. Ensure to supply a detailed QA bundle for the altered textures including previews, initiate a GAME-ANALYTICS work item associated with the draft, and provide solely the draft PR number."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png", "assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="EnforceTexturePoliciesV2", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png", "assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png", "assets/textures/environment/castle_tower_normal.png"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="RenderTurntableV2", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png", "assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="DeterministicAutofixV2", kwargs={"qa_json": [{"file": "assets/textures/environment/castle_tower_diffuse.png"}, {"file": "assets/textures/environment/castle_tower_normal.png"}], "tex_report": [{"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True}, {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [{"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []}, {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}], "tex_report": [{"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True}, {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/textures/environment/castle_tower_diffuse.png", "assets/textures/environment/castle_tower_normal.png"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/2", "stills_uris": ["artifact://still/1", "artifact://still/2"]}}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "feature/new-renderer", "run_id": "assetqa_def456abc123789"}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-assetqa_def456abc123789", "patch_id": "AF-1", "run_id": "assetqa_def456abc123789"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-assetqa_def456abc123789", "base": "feature/new-renderer", "run_id": "assetqa_def456abc123789"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "GAME-ANALYTICS", "summary": "asset_qa:commit=def456abc123789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "assetqa_def456abc123789", "pr_number": 33}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=def456abc123789", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheckV2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "def456abc123789"}, "outputs": {"pr_number": 33, "ticket_key": "GAME-ANALYTICS-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_040",
        instruction=(
            "Coordinate an additional QA for the environment model related to commit def456abc123789. Check the budget for the castle tower model, include previews, initiate a deterministic draft, establish an ENGINE-MIG work item linked to the draft, and furnish only the draft PR number."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="RenderTurntableV2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [{"file": "assets/models/environment/castle_tower.fbx", "issues": []}], "tex_report": [], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/models/environment/castle_tower.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="OpenAutoBranchV2", kwargs={"base_ref": "main", "run_id": "assetqa_def456abc123789"}),
            Action(name="DeterministicAutofixV2", kwargs={"qa_json": [{"file": "assets/models/environment/castle_tower.fbx"}], "tex_report": []}),
            Action(name="CommitPatchToBranchV2", kwargs={"branch_ref": "auto/fix-assetqa_def456abc123789", "patch_id": "AF-1", "run_id": "assetqa_def456abc123789"}),
            Action(name="OpenDraftPrV2", kwargs={"head": "auto/fix-assetqa_def456abc123789", "base": "main", "run_id": "assetqa_def456abc123789"}),
            Action(name="CreateOrUpdateTicketV2", kwargs={"project_key": "ENGINE-MIG", "summary": "asset_qa:commit=def456abc123789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "assetqa_def456abc123789", "pr_number": 33}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=def456abc123789", "report_uri": "artifact://qa/summary"}),
            Action(name="SetAssetQaCheckV2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "def456abc123789"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_041",
        instruction=(
            "Handle the validation of engine-side budgets for the revamped castle environment at commit def456abc123789. Ensure that the model, textures, and materials conform to engine budgets, publish previews, save deterministic QA results for each asset, and provide the commit SHA only."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": [
                "assets/models/environment/castle_tower.fbx",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png",
                "assets/materials/environment/castle_tower.mtl"
            ]}),
            Action(name="EnforceTexturePoliciesV2", kwargs={"files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="RenderTurntableV2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [
                {"file": "assets/models/environment/castle_tower.fbx", "issues": []},
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []},
                {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []},
                {"file": "assets/materials/environment/castle_tower.mtl", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/models/environment/castle_tower.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/models/environment/castle_tower.fbx", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/textures/environment/castle_tower_diffuse.png", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/textures/environment/castle_tower_normal.png", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/materials/environment/castle_tower.mtl", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "def456abc123789", "assets": [
                "assets/models/environment/castle_tower.fbx",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png",
                "assets/materials/environment/castle_tower.mtl"
            ]}, "outputs": {"assets_processed": 4}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "def456abc123789"}),
        ],
        outputs=["def456abc123789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_042",
        instruction=(
            "Coordinate the engine budget validation for the updated hero character pack at commit abc123def456789. Confirm that the model, textures, and animation meet engine budgets, release previews, securely store the outcomes for each asset deterministically, and supply the commit SHA only."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png",
                "assets/animations/characters/hero_idle.fbx"
            ]}),
            Action(name="EnforceTexturePoliciesV2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/animations/characters/hero_idle.fbx"
            ], "scene": "BudgetScene:abc123def456789"}),
            Action(name="RenderTurntableV2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/animations/characters/hero_idle.fbx"
            ]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [
                {"file": "assets/models/characters/hero_character.fbx", "issues": []},
                {"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []},
                {"file": "assets/textures/characters/hero_character_normal.png", "issues": []},
                {"file": "assets/animations/characters/hero_idle.fbx", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "ok": True},
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": [
                "assets/models/characters/hero_character.fbx",
                "assets/animations/characters/hero_idle.fbx"
            ], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/2", "stills_uris": ["artifact://still/1", "artifact://still/2"]}}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/models/characters/hero_character.fbx", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/textures/characters/hero_character_diffuse.png", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/textures/characters/hero_character_normal.png", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/animations/characters/hero_idle.fbx", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "abc123def456789", "assets": [
                "assets/models/characters/hero_character.fbx",
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png",
                "assets/animations/characters/hero_idle.fbx"
            ]}, "outputs": {"assets_processed": 4}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "abc123def456789"}),
        ],
        outputs=["abc123def456789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_043",
        instruction=(
            "Ensure the engine budgets for the environment textures altered at commit def456abc123789 are validated, generate previews, save results for each texture, and provide just the commit SHA."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="EnforceTexturePoliciesV2", kwargs={"files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ], "scene": "BudgetScene:def456abc123789"}),
            Action(name="RenderTurntableV2", kwargs={"files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []},
                {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/2", "stills_uris": ["artifact://still/1", "artifact://still/2"]}}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/textures/environment/castle_tower_diffuse.png", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/textures/environment/castle_tower_normal.png", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "def456abc123789", "assets": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}, "outputs": {"assets_processed": 2}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "def456abc123789"}),
        ],
        outputs=["def456abc123789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_044",
        instruction=(
            "Conduct engine budget verifications for the hero character textures at commit abc123def456789. Implement texture policies, publish previews, save deterministic results for each texture, and deliver only the commit SHA."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="EnforceTexturePoliciesV2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ], "scene": "BudgetScene:abc123def456789"}),
            Action(name="RenderTurntableV2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []},
                {"file": "assets/textures/characters/hero_character_normal.png", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "ok": True},
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/2", "stills_uris": ["artifact://still/1", "artifact://still/2"]}}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/textures/characters/hero_character_diffuse.png", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/textures/characters/hero_character_normal.png", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "abc123def456789", "assets": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}, "outputs": {"assets_processed": 2}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "abc123def456789"}),
        ],
        outputs=["abc123def456789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_045",
        instruction=(
            "Ensure the engine budget validation for the castle tower model at commit def456abc123789 is completed. Issue previews, save the result deterministically, and provide only the commit SHA."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="RenderTurntableV2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [{"file": "assets/models/environment/castle_tower.fbx", "issues": []}], "tex_report": [], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/models/environment/castle_tower.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/models/environment/castle_tower.fbx", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "def456abc123789", "assets": ["assets/models/environment/castle_tower.fbx"]}, "outputs": {"assets_processed": 1}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "def456abc123789"}),
        ],
        outputs=["def456abc123789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_046",
        instruction=(
            "Conclude the engine budget validation for the castle material at commit def456abc123789. Release preview, store the material result deterministically, and deliver only the commit SHA."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="RenderTurntableV2", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [{"file": "assets/materials/environment/castle_tower.mtl", "issues": []}], "tex_report": [], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/materials/environment/castle_tower.mtl"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/materials/environment/castle_tower.mtl", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "def456abc123789", "assets": ["assets/materials/environment/castle_tower.mtl"]}, "outputs": {"assets_processed": 1}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "def456abc123789"}),
        ],
        outputs=["def456abc123789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_047",
        instruction=(
            "Handle engine budget checks for the hero character model at commit abc123def456789. Generate a preview, save the results deterministically, and provide only the commit SHA."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": ["assets/models/characters/hero_character.fbx"], "scene": "BudgetScene:abc123def456789"}),
            Action(name="RenderTurntableV2", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [{"file": "assets/models/characters/hero_character.fbx", "issues": []}], "tex_report": [], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": ["assets/models/characters/hero_character.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/models/characters/hero_character.fbx", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "abc123def456789", "assets": ["assets/models/characters/hero_character.fbx"]}, "outputs": {"assets_processed": 1}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "abc123def456789"}),
        ],
        outputs=["abc123def456789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_048",
        instruction=(
            "Conduct engine budget validation for the hero animation at commit abc123def456789. Produce a preview, ensure the outcome is saved deterministically, and yield only the commit SHA."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"], "scene": "BudgetScene:abc123def456789"}),
            Action(name="RenderTurntableV2", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [{"file": "assets/animations/characters/hero_idle.fbx", "issues": []}], "tex_report": [], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": ["assets/animations/characters/hero_idle.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/animations/characters/hero_idle.fbx", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "abc123def456789", "assets": ["assets/animations/characters/hero_idle.fbx"]}, "outputs": {"assets_processed": 1}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "abc123def456789"}),
        ],
        outputs=["abc123def456789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_049",
        instruction=(
            "You are required to conduct a combined engine budget validation for the environment model and textures at commit def456abc123789. Release previews, ensure all outcomes are persisted deterministically, and provide only the commit SHA."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": [
                "assets/models/environment/castle_tower.fbx",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="EnforceTexturePoliciesV2", kwargs={"files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": [
                "assets/models/environment/castle_tower.fbx"
            ], "scene": "BudgetScene:def456abc123789"}),
            Action(name="RenderTurntableV2", kwargs={"files": [
                "assets/models/environment/castle_tower.fbx",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [
                {"file": "assets/models/environment/castle_tower.fbx", "issues": []},
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []},
                {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": [
                "assets/models/environment/castle_tower.fbx"
            ], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/3", "stills_uris": ["artifact://still/1", "artifact://still/2", "artifact://still/3"]}}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/models/environment/castle_tower.fbx", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/3", "report_uri": "artifact://qa/summary"}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/textures/environment/castle_tower_diffuse.png", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/3", "report_uri": "artifact://qa/summary"}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/textures/environment/castle_tower_normal.png", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/3", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "def456abc123789", "assets": [
                "assets/models/environment/castle_tower.fbx",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}, "outputs": {"assets_processed": 3}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "def456abc123789"}),
        ],
        outputs=["def456abc123789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_050",
        instruction=(
            "You need to finalize engine budget checks for the hero character textures and model at commit abc123def456789. Release previews, ensure deterministic outcomes are persisted for all three assets, and provide only the commit SHA."
        ),
        actions=[
            Action(name="ListChangedAssetsV2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="DccValidateAssetsV2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="EnforceTexturePoliciesV2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="EngineBudgetProbeV2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx"
            ], "scene": "BudgetScene:abc123def456789"}),
            Action(name="RenderTurntableV2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="PublishQaBundleV2", kwargs={"qa_json": [
                {"file": "assets/models/characters/hero_character.fbx", "issues": []},
                {"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []},
                {"file": "assets/textures/characters/hero_character_normal.png", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "ok": True},
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": [
                "assets/models/characters/hero_character.fbx"
            ], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/3", "stills_uris": ["artifact://still/1", "artifact://still/2", "artifact://still/3"]}}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/models/characters/hero_character.fbx", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/3", "report_uri": "artifact://qa/summary"}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/textures/characters/hero_character_diffuse.png", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/3", "report_uri": "artifact://qa/summary"}),
            Action(name="PersistQaOutcomeV2", kwargs={"asset_id": "assets/textures/characters/hero_character_normal.png", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/3", "report_uri": "artifact://qa/summary"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "abc123def456789", "assets": [
                "assets/models/characters/hero_character.fbx",
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}, "outputs": {"assets_processed": 3}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "abc123def456789"}),
        ],
        outputs=["abc123def456789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_051",
        instruction=(
            "Handle the deduplication of crash ticket work_026 against its canonical issue, calculate an impact score using the renderer crash fingerprint, assign it to the renderer module owner, move it to Triage, and provide solely the ticket key."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026", "severity": "critical", "module": "renderer", "crash_fingerprint": "renderer_character_load_access_violation_xyz"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "work_026"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "work_026"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "work_026", "fingerprint": "renderer_character_load_access_violation_xyz"}),
            Action(name="FindOwnershipPathV2", kwargs={"contains": "renderer"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "work_026"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "work_026", "fields": {"assigned_team": "team_001", "state": "Triage", "duplicate_of": "work_027"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_026", "fingerprint": "renderer_character_load_access_violation_xyz"}, "outputs": {"assigned_team": "team_001", "state": "Triage", "duplicate_of": "work_027"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "work_026"}),
        ],
        outputs=["work_026"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_052",
        instruction=(
            "Determine the impact for the texture artifact ticket work_027, identify the team responsible for the path 'assets/textures/character_models/' from the ownership map and assign the ticket accordingly, verify and document the canonical duplicate if it exists, ensure the generated summary text is stored on the ticket without any changes, update its status to Triage, and supply only the ticket key."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_027"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "work_027"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "work_027"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "work_027"}),
            Action(name="FindOwnershipPathV2", kwargs={"contains": "assets/textures/character_models/"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "assets/textures/character_models/"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "work_027"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "work_027", "fields": {"assigned_team": "team_002", "state": "Triage", "duplicate_of": "work_026", "summary_text": "Issue :: ", "impact_score": 2}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_027"}, "outputs": {"assigned_team": "team_002", "state": "Triage", "duplicate_of": "work_026", "impact_score": 2}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "work_027"}),
        ],
        outputs=["work_027"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_053",
        instruction=(
            "Handle the new bug work_029 by evaluating its impact, categorize it as a duplicate of work_030 in accordance with deduplication records, and direct it to the Network module owner in charge of 'src/game/network/multiplayer.cpp'. Assign it to Triage and return the ticket key only."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_029"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "work_029"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "work_029"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "work_029"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "src/game/network/multiplayer.cpp"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "work_029"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "work_029", "fields": {"assigned_team": "team_003", "state": "Triage", "duplicate_of": "work_030"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_029"}, "outputs": {"assigned_team": "team_003", "state": "Triage", "duplicate_of": "work_030"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "work_029"}),
        ],
        outputs=["work_029"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_054",
        instruction=(
            "Address bug_006 by designating it as a duplicate of bug_007 based on deduplication, determine its impact, and forward it to the UI module owner taking care of 'src/game/ui/menu_system.cpp'. Shift it to Triage and provide the ticket key only."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_006"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "bug_006"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "bug_006"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "bug_006"}),
            Action(name="FindOwnershipPathV2", kwargs={"contains": "menu_system.cpp"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "src/game/ui/menu_system.cpp"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "bug_006"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "bug_006", "fields": {"assigned_team": "team_005", "state": "Triage", "duplicate_of": "bug_007"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_006"}, "outputs": {"assigned_team": "team_005", "state": "Triage", "duplicate_of": "bug_007"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "bug_006"}),
        ],
        outputs=["bug_006"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_055",
        instruction=(
            "Handle the triaging of the Input System ticket bug_009. Utilize 'src/game/input/controller_handler.cpp' as the ownership anchor. Following triage, the ticket should be assigned to the responsible team, marked as Triage, and retain the generated reviewer summary text exactly (no changes). Only the ticket key should be returned."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_009"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "bug_009"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "bug_009"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "bug_009"}),
            Action(name="FindOwnershipPathV2", kwargs={"contains": "controller_handler.cpp"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "src/game/input/controller_handler.cpp"}),
            Action(name="LookupRelationV2", kwargs={"ticket_key": "bug_009"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "bug_009", "fields": {"assigned_team": "team_001", "state": "Triage", "summary_text": "Issue :: "}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_009"}, "outputs": {"assigned_team": "team_001", "state": "Triage"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "bug_009"}),
        ],
        outputs=["bug_009"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_056",
        instruction=(
            "Coordinate the routing of the related UI ticket work_031 to the UI owner, calculate the impact, update it to Triage with an association to work_030, and provide only the ticket key."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_031", "description": "Similar UI rendering issue in same menu system", "module": "ui_system"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "work_031"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "work_031"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "work_031"}),
            Action(name="FindOwnershipPathV2", kwargs={"contains": "ui/"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "src/game/ui/menu_system.cpp"}),
            Action(name="LookupRelationV2", kwargs={"ticket_key": "work_031"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "work_031", "fields": {"assigned_team": "team_005", "state": "Triage", "related_to": "work_030"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_031"}, "outputs": {"assigned_team": "team_005", "state": "Triage", "related_to": "work_030"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "work_031"}),
        ],
        outputs=["work_031"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_057",
        instruction=(
            "Handle bug_intake_012 as a duplicate of bug_intake_011. Make use of 'assets/audio/sound_effects/' for the ownership anchor during assignment, ensure the impact is calculated, change the ticket status to Triage, and respond solely with the ticket key."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_012"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="FindOwnershipPathV2", kwargs={"contains": "assets/audio/sound_effects/"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "assets/audio/sound_effects/"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "bug_intake_012", "fields": {"assigned_team": "team_004", "state": "Triage", "duplicate_of": "bug_intake_011"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_intake_012"}, "outputs": {"assigned_team": "team_004", "state": "Triage", "duplicate_of": "bug_intake_011"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "bug_intake_012"}),
        ],
        outputs=["bug_intake_012"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_058",
        instruction=(
            "Coordinate the routing of bug_intake_014 as related to bug_intake_013 to the Physics owner. Utilize 'src/game/physics/collision_detection.cpp' as the ownership anchor, determine the impact, adjust the state to Triage, and provide only the ticket key."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_014"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "bug_intake_014"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "bug_intake_014"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "bug_intake_014"}),
            Action(name="FindOwnershipPathV2", kwargs={"contains": "src/game/physics/collision_detection.cpp"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "src/game/physics/collision_detection.cpp"}),
            Action(name="LookupRelationV2", kwargs={"ticket_key": "bug_intake_014"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "bug_intake_014", "fields": {"assigned_team": "team_001", "state": "Triage", "related_to": "bug_intake_013"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_intake_014"}, "outputs": {"assigned_team": "team_001", "state": "Triage", "related_to": "bug_intake_013"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "bug_intake_014"}),
        ],
        outputs=["bug_intake_014"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_059",
        instruction=(
            "Handle the triage for the AI System ticket work_028. Use 'src/game/ai/pathfinding.h' as the ownership anchor. Calculate the impact, verify if there is a canonical duplicate and document it if found, look for any related link, assign it to the appropriate team, set the status to Triage, and return just the ticket key."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_028"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "work_028"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "work_028"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "work_028"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "src/game/ai/pathfinding.h"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "work_028"}),
            Action(name="LookupRelationV2", kwargs={"ticket_key": "work_028"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "work_028", "fields": {"assigned_team": "team_003", "state": "Triage", "duplicate_of": "work_029"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_028"}, "outputs": {"assigned_team": "team_003", "state": "Triage", "duplicate_of": "work_029"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "work_028"}),
        ],
        outputs=["work_028"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_060",
        instruction=(
            "Coordinate the processing of bug_016 as a duplicate of bug_017 following the deduplication process, determine the impact, assign it to the physics owner, set to Triage, and only return the ticket key."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_016"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "bug_016"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "bug_016"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "bug_016"}),
            Action(name="FindOwnershipPathV2", kwargs={"contains": "physics"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "src/game/physics/collision_detection.cpp"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "bug_016"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "bug_016", "fields": {"assigned_team": "team_001", "state": "Triage", "duplicate_of": "bug_017"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_016"}, "outputs": {"assigned_team": "team_001", "state": "Triage", "duplicate_of": "bug_017"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "bug_016"}),
        ],
        outputs=["bug_016"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_061",
        instruction=(
            "Handle the localization readiness of PR 999 for de, fr, and ja following the policy: provide compliant localized content for the identified changed keys within a 200px UI limit, document review coverage for these locales, present the generated artifacts on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="DetectChangedStringsV2", kwargs={"pr_number": 999}),
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["de", "fr", "ja"], "keys": [
                "ui.main_menu.start_game",
                "ui.settings.audio",
                "ui.settings.audio.master_volume",
                "ui.settings.audio.music_volume",
                "ui.settings.audio.sfx_volume",
                "ui.settings.graphics",
                "ui.settings.graphics.resolution",
                "ui.settings.graphics.quality",
                "ui.game.hud.health",
                "ui.game.hud.mana"
            ], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": [
                "ui.main_menu.start_game",
                "ui.settings.audio",
                "ui.settings.audio.master_volume",
                "ui.settings.audio.music_volume",
                "ui.settings.audio.sfx_volume",
                "ui.settings.graphics",
                "ui.settings.graphics.resolution",
                "ui.settings.graphics.quality",
                "ui.game.hud.health",
                "ui.game.hud.mana"
            ], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": [
                "ui.main_menu.start_game",
                "ui.settings.audio",
                "ui.settings.audio.master_volume",
                "ui.settings.audio.music_volume",
                "ui.settings.audio.sfx_volume",
                "ui.settings.graphics",
                "ui.settings.graphics.resolution",
                "ui.settings.graphics.quality",
                "ui.game.hud.health",
                "ui.game.hud.mana"
            ], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "ja", "keys": [
                "ui.main_menu.start_game",
                "ui.settings.audio",
                "ui.settings.audio.master_volume",
                "ui.settings.audio.music_volume",
                "ui.settings.audio.sfx_volume",
                "ui.settings.graphics",
                "ui.settings.graphics.resolution",
                "ui.settings.graphics.quality",
                "ui.game.hud.health",
                "ui.game.hud.mana"
            ], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": [
                "ui.main_menu.start_game",
                "ui.settings.audio",
                "ui.settings.audio.master_volume",
                "ui.settings.audio.music_volume",
                "ui.settings.audio.sfx_volume",
                "ui.settings.graphics",
                "ui.settings.graphics.resolution",
                "ui.settings.graphics.quality",
                "ui.game.hud.health",
                "ui.game.hud.mana"
            ]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": [
                "ui.main_menu.start_game",
                "ui.settings.audio",
                "ui.settings.audio.master_volume",
                "ui.settings.audio.music_volume",
                "ui.settings.audio.sfx_volume",
                "ui.settings.graphics",
                "ui.settings.graphics.resolution",
                "ui.settings.graphics.quality",
                "ui.game.hud.health",
                "ui.game.hud.mana"
            ]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "ja", "keys": [
                "ui.main_menu.start_game",
                "ui.settings.audio",
                "ui.settings.audio.master_volume",
                "ui.settings.audio.music_volume",
                "ui.settings.audio.sfx_volume",
                "ui.settings.graphics",
                "ui.settings.graphics.resolution",
                "ui.settings.graphics.quality",
                "ui.game.hud.health",
                "ui.game.hud.mana"
            ]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://tms/TMS-1", "report_uri": "artifact://tms/TMS-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-10", "report_uri": "artifact://bundle/bundle-de-10"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-10", "report_uri": "artifact://bundle/bundle-fr-10"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-10", "report_uri": "artifact://bundle/bundle-ja-10"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de", "fr", "ja"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"de": "artifact://bundle/bundle-de-10", "fr": "artifact://bundle/bundle-fr-10", "ja": "artifact://bundle/bundle-ja-10"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_062",
        instruction=(
            "Ensure the validation of PR 999 localization for de and fr: check all modified keys within a 200px width budget, save both locale bundles, initiate an in_review TMS job 'quest_shard' for de and fr, and tag PR 999 with artifact://bundle/bundle-de-10 and artifact://bundle/bundle-fr-10. Return only 'pr_999'."
        ),
        actions=[
            Action(name="DetectChangedStringsV2", kwargs={"pr_number": 999}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "quest_shard", "locales": ["de", "fr"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-10", "report_uri": "artifact://bundle/bundle-de-10"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-10", "report_uri": "artifact://bundle/bundle-fr-10"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de", "fr"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"de": "artifact://bundle/bundle-de-10", "fr": "artifact://bundle/bundle-fr-10"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_063",
        instruction=(
            "Handle the preparation of PR 999 localization for ja: check all updated keys against a 200px width limit, save the ja bundle, initiate an in_review TMS job 'quest_shard' for ja, update PR 999 with the bundle artifact URI, and provide only 'pr_999'."
        ),
        actions=[
            Action(name="DetectChangedStringsV2", kwargs={"pr_number": 999}),
            Action(name="LocLintV2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "quest_shard", "locales": ["ja"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-10", "report_uri": "artifact://bundle/bundle-ja-10"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["ja"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"ja": "artifact://bundle/bundle-ja-10"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_064",
        instruction=(
            "Complete the localization process for PR 999 for de and ja: verify all altered keys adhere to a 200px width constraint, store both bundles, start an in_review TMS job 'quest_shard' for de and ja, and add to PR 999 artifact://bundle/bundle-de-10 and artifact://bundle/bundle-ja-10. Provide only 'pr_999'."
        ),
        actions=[
            Action(name="DetectChangedStringsV2", kwargs={"pr_number": 999}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "quest_shard", "locales": ["de", "ja"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-10", "report_uri": "artifact://bundle/bundle-de-10"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-10", "report_uri": "artifact://bundle/bundle-ja-10"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de", "ja"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"de": "artifact://bundle/bundle-de-10", "ja": "artifact://bundle/bundle-ja-10"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_065",
        instruction=(
            "Ensure PR 999 is ready for localization in de, fr, and ja according to the localization policy: utilize the identified changed keys while adhering to a 200px UI width limit to generate and save locale bundles, initiate a single in_review TMS job named 'loc_pr_999' to cover these locales, and tag PR 999 with the artifact URIs of the generated bundles. Return only 'pr_999'."
        ),
        actions=[
            Action(name="DetectChangedStringsV2", kwargs={"pr_number": 999}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-10", "report_uri": "artifact://bundle/bundle-de-10"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-10", "report_uri": "artifact://bundle/bundle-fr-10"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-10", "report_uri": "artifact://bundle/bundle-ja-10"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de", "fr", "ja"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"de": "artifact://bundle/bundle-de-10", "fr": "artifact://bundle/bundle-fr-10", "ja": "artifact://bundle/bundle-ja-10"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_066",
        instruction=(
            "Finalize the localization of PR 999 for de: check all changed keys with a 200px width constraint, save the de bundle, create an in_review TMS job called 'quest_shard' for de, tag PR 999 with the bundle artifact URI, and return only 'pr_999'."
        ),
        actions=[
            Action(name="DetectChangedStringsV2", kwargs={"pr_number": 999}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "quest_shard", "locales": ["de"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-10", "report_uri": "artifact://bundle/bundle-de-10"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"de": "artifact://bundle/bundle-de-10"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_067",
        instruction=(
            "Ensure you finalize PR 999 localization for fr: lint every modified key adhering to a 200px width budget, save the fr bundle, initiate an in_review TMS job 'quest_shard' for fr, mark PR 999 with the bundle artifact URI, and return solely 'pr_999'."
        ),
        actions=[
            Action(name="DetectChangedStringsV2", kwargs={"pr_number": 999}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "quest_shard", "locales": ["fr"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-10", "report_uri": "artifact://bundle/bundle-fr-10"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["fr"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"fr": "artifact://bundle/bundle-fr-10"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_068",
        instruction=(
            "Ensure you finalize PR 999 localization for ja: lint every modified key adhering to a 200px width budget, save the ja bundle, initiate an in_review TMS job 'quest_shard' for ja, mark PR 999 with the bundle artifact URI, and return solely 'pr_999'."
        ),
        actions=[
            Action(name="DetectChangedStringsV2", kwargs={"pr_number": 999}),
            Action(name="LocLintV2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "quest_shard", "locales": ["ja"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-10", "report_uri": "artifact://bundle/bundle-ja-10"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["ja"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"ja": "artifact://bundle/bundle-ja-10"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_069",
        instruction=(
            "Handle the completion of PR 999 localization for de and fr: lint all modified keys within a 200px width constraint, save both bundles, initiate an in_review TMS job 'quest_shard' for de and fr, and tag PR 999 with artifact://bundle/bundle-de-10 and artifact://bundle/bundle-fr-10. Return only 'pr_999'."
        ),
        actions=[
            Action(name="DetectChangedStringsV2", kwargs={"pr_number": 999}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "quest_shard", "locales": ["de", "fr"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-10", "report_uri": "artifact://bundle/bundle-de-10"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-10", "report_uri": "artifact://bundle/bundle-fr-10"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de", "fr"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"de": "artifact://bundle/bundle-de-10", "fr": "artifact://bundle/bundle-fr-10"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_070",
        instruction=(
            "Make sure PR 999 localization adheres to policy across de, fr, and ja: provide compliant localized assets using the identified changed keys within the 200px UI constraint, document review coverage for these locales, highlight the generated artifacts on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="DetectChangedStringsV2", kwargs={"pr_number": 999}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "bundle-de-10+bundle-fr-10+bundle-ja-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-10", "report_uri": "artifact://bundle/bundle-de-10"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-10", "report_uri": "artifact://bundle/bundle-fr-10"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-10", "report_uri": "artifact://bundle/bundle-ja-10"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de", "fr", "ja"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"de": "artifact://bundle/bundle-de-10", "fr": "artifact://bundle/bundle-fr-10", "ja": "artifact://bundle/bundle-ja-10"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_071",
        instruction=(
            "Handle PR 999 to achieve a deterministic review-ready state for hero intros in de and fr. Ensure that 'vo.hero.intro_01' (de) and 'vo.hero.intro_02' (fr) adhere to the Localization/VO Protocol V2 within a 200-pixel UI budget, confirm subtitle timing for the mapped line-ids, highlight the precise produced bundle URIs on PR 999, and only return 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["de", "fr"], "keys": ["vo.hero.intro_01", "vo.hero.intro_02"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["de", "fr"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "fr"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de","fr"], "line_ids": ["subtitle_002","subtitle_004"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "fr": "artifact://bundle/bundle-fr-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_072",
        instruction=(
            "Coordinate PR 999 to reach a deterministic review-ready state for hero intro line 2 in fr and en. Confirm 'vo.hero.intro_02' complies with policy for each locale within a 200-pixel UI budget, validate the subtitle timing for the mapped instances, highlight the precise produced bundle URIs on PR 999, and only return 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["fr", "en"], "keys": ["vo.hero.intro_02"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "en", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "en", "keys": ["vo.hero.intro_02"]}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["fr", "en"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_001", "locale": "en"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "en", "keys": ["vo.hero.intro_02"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["fr", "en"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-en-1", "report_uri": "artifact://bundle/bundle-en-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["fr","en"], "line_ids": ["subtitle_004","subtitle_001"], "bundle_uris": {"fr": "artifact://bundle/bundle-fr-1", "en": "artifact://bundle/bundle-en-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_073",
        instruction=(
            "Manage PR 999 to achieve a deterministic review-ready state for the villain threat line in both ja and fr. Ensure 'vo.villain.threat_01' adheres to policy for both locales within a 200-pixel UI budget, verify the mapped subtitle timing, display the precise produced bundle URIs on PR 999, and output only 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["ja", "fr"], "keys": ["vo.villain.threat_01"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "fr", "keys": ["vo.villain.threat_01"]}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["ja", "fr"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["vo.villain.threat_01"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["ja", "fr"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["ja","fr"], "line_ids": ["subtitle_006","subtitle_004"], "bundle_uris": {"ja": "artifact://bundle/bundle-ja-1", "fr": "artifact://bundle/bundle-fr-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_074",
        instruction=(
            "Coordinate PR 999 to reach a deterministic review-ready state for the NPC quest line across de and es. Confirm that 'vo.npc.quest_01' aligns with policy for both locales within a 200-pixel UI budget, check the mapped subtitle timing, present the accurate produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["de", "es"], "keys": ["vo.npc.quest_01"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "de", "keys": ["vo.npc.quest_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["de", "es"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["vo.npc.quest_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "es"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-es-1", "report_uri": "artifact://bundle/bundle-es-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de","es"], "line_ids": ["subtitle_002","subtitle_008"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "es": "artifact://bundle/bundle-es-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_075",
        instruction=(
            "Ensure that PR 999 is in a deterministic review-ready state for UI selection and NPC quest in zh and es. Confirm that 'vo.ui.menu_select' (zh) and 'vo.npc.quest_01' (es) adhere to policy within a 200-pixel UI budget, verify the synchronization of subtitle timing, reveal the precise produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["zh", "es"], "keys": ["vo.ui.menu_select", "vo.npc.quest_01"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["zh", "es"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["zh", "es"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-zh-1", "report_uri": "artifact://bundle/bundle-zh-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-es-1", "report_uri": "artifact://bundle/bundle-es-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["zh","es"], "line_ids": ["subtitle_010","subtitle_008"], "bundle_uris": {"zh": "artifact://bundle/bundle-zh-1", "es": "artifact://bundle/bundle-es-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_076",
        instruction=(
            "Ensure PR 999 reaches a deterministic review-ready state for hero intros across en, de, and fr. Confirm that 'vo.hero.intro_01' (en, de) and 'vo.hero.intro_02' (fr) adhere to the Localization/VO Protocol V2 within a 200-pixel UI budget, verify the subtitle timing for the mapped line-ids, reveal the precise produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["en", "de", "fr"], "keys": ["vo.hero.intro_01", "vo.hero.intro_02"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["en", "de", "fr"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_001", "locale": "en"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["en", "de", "fr"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-en-1", "report_uri": "artifact://bundle/bundle-en-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["en","de","fr"], "line_ids": ["subtitle_001","subtitle_002","subtitle_004"], "bundle_uris": {"en": "artifact://bundle/bundle-en-1", "de": "artifact://bundle/bundle-de-1", "fr": "artifact://bundle/bundle-fr-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_077",
        instruction=(
            "Ensure PR 999 reaches a deterministic review‑ready status for 'vo.villain.threat_01' (en, ja) and 'vo.npc.quest_01' (es). Adhere to the Localization/VO Protocol V2 while staying within a 200‑pixel UI limit, validate subtitle timing solely for mapped line‑ids, display the exact produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["en", "ja"], "keys": ["vo.villain.threat_01"], "glossary_lock": True}),
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["es"], "keys": ["vo.npc.quest_01"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "en", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "en", "keys": ["vo.villain.threat_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["ja", "es"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "en", "keys": ["vo.villain.threat_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["en", "ja", "es"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-en-1", "report_uri": "artifact://bundle/bundle-en-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-es-1", "report_uri": "artifact://bundle/bundle-es-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["en","ja","es"], "line_ids": ["subtitle_006","subtitle_008"], "bundle_uris": {"en": "artifact://bundle/bundle-en-1", "ja": "artifact://bundle/bundle-ja-1", "es": "artifact://bundle/bundle-es-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_078",
        instruction=(
            "Ensure PR 999 reaches a deterministic review‑ready status for hero intro 2 and the UI selection cue for both fr and zh. Verify that 'vo.hero.intro_02' (fr) and 'vo.ui.menu_select' (zh) adhere to policy with a 200‑pixel UI constraint, validate subtitle timing for the mapped line‑ids, display the exact produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["fr", "zh"], "keys": ["vo.hero.intro_02", "vo.ui.menu_select"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"], "ui_px_limit": 200}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["fr", "zh"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["fr", "zh"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-zh-1", "report_uri": "artifact://bundle/bundle-zh-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["fr","zh"], "line_ids": ["subtitle_004","subtitle_010"], "bundle_uris": {"fr": "artifact://bundle/bundle-fr-1", "zh": "artifact://bundle/bundle-zh-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_079",
        instruction=(
            "Handle PR 999 to achieve a review‑ready state deterministically across the languages en, de, and ja for hero and villain lines. Ensure 'vo.hero.intro_01' (en, de) and 'vo.villain.threat_01' (ja) comply with policy under a 200‑pixel UI budget, confirm the subtitle timing for the mapped line‑ids, present the exact produced bundle URIs on PR 999, and provide only 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["en", "de", "ja"], "keys": ["vo.hero.intro_01", "vo.villain.threat_01"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["en", "de", "ja"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_001", "locale": "en"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["en", "de", "ja"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-en-1", "report_uri": "artifact://bundle/bundle-en-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["en","de","ja"], "line_ids": ["subtitle_001","subtitle_002","subtitle_006"], "bundle_uris": {"en": "artifact://bundle/bundle-en-1", "de": "artifact://bundle/bundle-de-1", "ja": "artifact://bundle/bundle-ja-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_080",
        instruction=(
            "Coordinate PR 999 to become a deterministic review‑ready state across de, fr, ja, es, and zh for hero, villain, NPC, and UI lines. Ensure the precise VO keys (de→'vo.hero.intro_01', fr→'vo.hero.intro_02', ja→'vo.villain.threat_01', es→'vo.npc.quest_01', zh→'vo.ui.menu_select') adhere to policy within a 200‑pixel UI budget, verify subtitle timing for the mapped line‑ids, display the exact produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["de", "fr", "ja", "es", "zh"], "keys": ["vo.hero.intro_01", "vo.hero.intro_02", "vo.villain.threat_01", "vo.npc.quest_01", "vo.ui.menu_select"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"], "ui_px_limit": 200}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["de", "fr", "ja", "es", "zh"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "fr", "ja", "es", "zh"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-es-1", "report_uri": "artifact://bundle/bundle-es-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-zh-1", "report_uri": "artifact://bundle/bundle-zh-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de","fr","ja","es","zh"], "line_ids": ["subtitle_002","subtitle_004","subtitle_006","subtitle_008","subtitle_010"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "fr": "artifact://bundle/bundle-fr-1", "ja": "artifact://bundle/bundle-ja-1", "es": "artifact://bundle/bundle-es-1", "zh": "artifact://bundle/bundle-zh-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_081",
        instruction=(
            "You are the triage agent. Consolidate the newly ingested ticket 'work_026' using the duplicate resolution protocol. Apply severity High and the module path 'src/game/engine/renderer.cpp' to determine ownership. Calculate impact using the crash fingerprint 'renderer_character_load_access_violation_xyz' from the crash_events table. Revise the ticket with owner team and triage state, document automation, and provide only the canonical ticket id for 'work_026'."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026", "severity": "High", "module": "src/game/engine/renderer.cpp"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "work_026"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "work_026"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "work_026", "fingerprint": "renderer_character_load_access_violation_xyz"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "work_026"}),
            Action(name="LookupRelationV2", kwargs={"ticket_key": "work_026"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "work_026", "fields": {"assignee": "team_001", "labels": ["auto-triage"], "state": "Triage", "canonical": "work_027"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_026"}, "outputs": {"canonical_bug_id": "work_027", "owner_team": "team_001"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "work_027"}),
        ],
        outputs=["work_027"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_082",
        instruction=(
            "Handle the Bug Intake Protocol V2 to channel 'work_029' for the module 'assets/models/environment/' with severity Medium. Assign the module owner as the assignee, set the state to 'Triage', and add label 'auto-triage'. Provide only the canonical ticket id for 'work_029'."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_029", "severity": "Medium", "module": "assets/models/environment/"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "work_029"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "work_029"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "work_029"}),
            Action(name="FindOwnershipPathV2", kwargs={"contains": "environment"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "assets/models/environment/"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "work_029"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "work_029", "fields": {"assignee": "team_002", "state": "Triage", "labels": ["auto-triage"], "canonical": "work_030"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_029"}, "outputs": {"canonical_bug_id": "work_030", "owner_team": "team_002"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "work_030"}),
        ],
        outputs=["work_030"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_083",
        instruction=(
            "Handle 'bug_006' from gameplay UI. Settle duplicates following policy and utilize UI ownership at 'src/game/ui/menu_system.cpp'. Maintain severity High and evaluate impact absent of crash fingerprint. Retain owner assignment, designate triage state, log the run, and provide only the canonical ticket id for 'bug_006'."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_006", "severity": "High", "module": "src/game/ui/menu_system.cpp"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "bug_006"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "bug_006"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "bug_006"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "src/game/ui/menu_system.cpp"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "bug_006"}),
            Action(name="LookupRelationV2", kwargs={"ticket_key": "bug_006"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "bug_006", "fields": {"assignee": "team_005", "state": "Triage", "labels": ["auto-triage"], "canonical": "bug_007"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_006"}, "outputs": {"canonical_bug_id": "bug_007", "owner_team": "team_005"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "bug_007"}),
        ],
        outputs=["bug_007"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_084",
        instruction=(
            "Coordinate the Bug Intake Protocol V2 application to 'bug_009' (module 'src/game/input/controller_handler.cpp', severity Medium). Assign the ticket to its module owner, adjust state to 'Triage', append label 'auto-triage', and deliver only the canonical ticket id for 'bug_009'."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_009", "severity": "Medium", "module": "src/game/input/controller_handler.cpp"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "bug_009"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "bug_009"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "bug_009"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "src/game/input/controller_handler.cpp"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "bug_009"}),

            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "bug_009", "fields": {"assignee": "team_001", "state": "Triage", "labels": ["auto-triage"], "canonical": "bug_010"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_009"}, "outputs": {"canonical_bug_id": "bug_010", "owner_team": "team_001"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "bug_010"}),
        ],
        outputs=["bug_010"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_085",
        instruction=(
            "Manage the audio system duplicate intake for 'bug_intake_012'. Utilize audio ownership at 'assets/audio/sound_effects/'. Maintain severity as High, direct it to the audio team, and provide only the canonical ticket id for 'bug_intake_012'."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_012", "severity": "High", "module": "assets/audio/sound_effects/"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "assets/audio/sound_effects/"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="LookupRelationV2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "bug_intake_012", "fields": {"assignee": "team_004", "state": "Triage", "labels": ["auto-triage"], "canonical": "bug_intake_011"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_intake_012"}, "outputs": {"canonical_bug_id": "bug_intake_011", "owner_team": "team_004"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "bug_intake_011"}),
        ],
        outputs=["bug_intake_011"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_086",
        instruction=(
            "Implement the Bug Intake Protocol V2 for 'bug_intake_016' (module 'src/game/network/multiplayer.cpp', severity Medium). Calculate the impact using fingerprint 'network_connection_timeout_30s_xyz', allocate to the owner team, designate state as 'Triage', append label 'auto-triage', and supply only the canonical ticket id."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_016", "severity": "Medium", "module": "src/game/network/multiplayer.cpp"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "bug_intake_016"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "bug_intake_016"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "bug_intake_016", "fingerprint": "network_connection_timeout_30s_xyz"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "src/game/network/multiplayer.cpp"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "bug_intake_016"}),

            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "bug_intake_016", "fields": {"assignee": "team_003", "state": "Triage", "labels": ["auto-triage"], "canonical": "bug_intake_015"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_intake_016"}, "outputs": {"canonical_bug_id": "bug_intake_015", "owner_team": "team_003"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "bug_intake_015"}),
        ],
        outputs=["bug_intake_015"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_087",
        instruction=(
            "Handle using the Bug Intake Protocol V2 for 'bug_intake_020' (module 'src/game/engine/renderer.cpp', severity High). Assign to the module owner, set the state as 'Triage', attach the label 'auto-triage', and provide only the canonical ticket id."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_020", "severity": "High", "module": "src/game/engine/renderer.cpp"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "bug_intake_020"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "bug_intake_020"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "bug_intake_020"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "bug_intake_020"}),

            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "bug_intake_020", "fields": {"assignee": "team_001", "state": "Triage", "labels": ["auto-triage"], "canonical": "bug_intake_019"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_intake_020"}, "outputs": {"canonical_bug_id": "bug_intake_019", "owner_team": "team_001"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "bug_intake_019"}),
        ],
        outputs=["bug_intake_019"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_088",
        instruction=(
            "Coordinate utilizing the Bug Intake Protocol V2 for 'work_028' (module 'assets/textures/character_models/', severity Medium). Delegate to the module owner, change the state to 'Triage', include the label 'auto-triage', and supply only the canonical ticket id for 'work_028'."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_028", "severity": "Medium", "module": "assets/textures/character_models/"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "work_028"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "work_028"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "work_028"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "assets/textures/character_models/"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "work_028"}),

            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "work_028", "fields": {"assignee": "team_002", "state": "Triage", "labels": ["auto-triage"], "canonical": "work_029"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_028"}, "outputs": {"canonical_bug_id": "work_029", "owner_team": "team_002"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "work_029"}),
        ],
        outputs=["work_029"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_089",
        instruction=(
            "Handle the Bug Intake Protocol V2 to direct 'bug_013' for the module 'assets/models/environment/' with severity Medium. Assign it to the module owner, designate state 'Triage', apply label 'auto-triage', ensure resolution of duplicates to the canonical record, and provide only the canonical id for 'bug_013'."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_013", "severity": "Medium", "module": "assets/models/environment/"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "bug_013"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "bug_013"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "bug_013"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "assets/models/environment/"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "bug_013"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "bug_013", "fields": {"assignee": "team_002", "state": "Triage", "labels": ["auto-triage"], "canonical": "bug_014"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_013"}, "outputs": {"canonical_bug_id": "bug_014", "owner_team": "team_002"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "bug_014"}),
        ],
        outputs=["bug_014"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_090",
        instruction=(
            "Handle 'bug_016', routing it according to 'src/game/physics/collision_detection.cpp' secondary ownership. Designate triage and provide only the canonical id for 'bug_016'."
        ),
        actions=[
            Action(name="IngestIssueWebhookV2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_016", "severity": "Medium", "module": "src/game/physics/collision_detection.cpp"}}),
            Action(name="NormalizeBugV2", kwargs={"ticket_key": "bug_016"}),
            Action(name="SummarizeBugV2", kwargs={"ticket_key": "bug_016"}),
            Action(name="ComputeImpactV2", kwargs={"ticket_key": "bug_016"}),
            Action(name="ResolveOwnerV2", kwargs={"module_or_path": "src/game/physics/collision_detection.cpp"}),
            Action(name="FindCanonicalDuplicateV2", kwargs={"ticket_key": "bug_016"}),
            Action(name="LookupRelationV2", kwargs={"ticket_key": "bug_016"}),
            Action(name="UpdateBugFieldsV2", kwargs={"ticket_key": "bug_016", "fields": {"assignee": "team_001", "state": "Triage", "labels": ["auto-triage"], "canonical": "bug_017"}}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_016"}, "outputs": {"canonical_bug_id": "bug_017", "owner_team": "team_001"}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "bug_017"}),
        ],
        outputs=["bug_017"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_091",
        instruction=(
            "Ensure the completion of a compact non-English bundle pass for PR 999: enforce glossary lock, lint UI width, synthesize temp VO, validate timing for ('subtitle_002','de') and ('subtitle_006','ja'), persist bundles for 'vo.hero.intro_01' (de) and 'vo.villain.threat_01' (ja), create one in_review TMS job, annotate PR 999 with produced bundle URIs, and return only 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["de", "ja"], "keys": ["vo.hero.intro_01", "vo.villain.threat_01"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["de", "ja"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "ja"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de","ja"], "line_ids": ["subtitle_002","subtitle_006"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "ja": "artifact://bundle/bundle-ja-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_092",
        instruction=(
            "Implement the Localization/VO Protocol V2 for PR 999 for fr and es. Produce compliant review bundles for ('subtitle_004','fr')→'vo.hero.intro_02' and ('subtitle_008','es')→'vo.npc.quest_01' while adhering to a UI width budget of 200, and return only 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["fr", "es"], "keys": ["vo.hero.intro_02", "vo.npc.quest_01"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["fr", "es"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["fr", "es"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-es-1", "report_uri": "artifact://bundle/bundle-es-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["fr","es"], "line_ids": ["subtitle_004","subtitle_008"], "bundle_uris": {"fr": "artifact://bundle/bundle-fr-1", "es": "artifact://bundle/bundle-es-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_093",
        instruction=(
            "Handle the application of the Localization/VO Protocol V2 to PR 999 for zh and ja. Develop compliant review bundles for ('subtitle_010','zh')→'vo.ui.menu_select' and ('subtitle_006','ja')→'vo.villain.threat_01' adhering to a UI width budget of 200, and return solely 'pr_999'."
        ),
        actions=[
            Action(name="LocLintV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["zh", "ja"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["zh", "ja"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-zh-1", "report_uri": "artifact://bundle/bundle-zh-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["zh","ja"], "line_ids": ["subtitle_010","subtitle_006"], "bundle_uris": {"zh": "artifact://bundle/bundle-zh-1", "ja": "artifact://bundle/bundle-ja-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_094",
        instruction=(
            "Coordinate the application of the Localization/VO Protocol V2 to PR 999 for de and fr. Create compliant review bundles for ('subtitle_002','de')→'vo.hero.intro_01' and ('subtitle_004','fr')→'vo.hero.intro_02' within a UI width budget of 200, and return only 'pr_999'."
        ),
        actions=[
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["de", "fr"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "fr"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de","fr"], "line_ids": ["subtitle_002","subtitle_004"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "fr": "artifact://bundle/bundle-fr-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_095",
        instruction=(
            "Handle the application of Localization/VO Protocol V2 to PR 999 for es and zh UI. Coordinate the creation of compliant review bundles for ('subtitle_008','es')→'vo.npc.quest_01' and ('subtitle_010','zh')→'vo.ui.menu_select' within a UI width budget of 200, and return solely 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["es", "zh"], "keys": ["vo.npc.quest_01", "vo.ui.menu_select"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"], "ui_px_limit": 200}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["es", "zh"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["es", "zh"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-es-1", "report_uri": "artifact://bundle/bundle-es-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-zh-1", "report_uri": "artifact://bundle/bundle-zh-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["es","zh"], "line_ids": ["subtitle_008","subtitle_010"], "bundle_uris": {"es": "artifact://bundle/bundle-es-1", "zh": "artifact://bundle/bundle-zh-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_096",
        instruction=(
            "Carry out the application of Localization/VO Protocol V2 to PR 999 for de and fr. Generate compliant review bundles for ('subtitle_002','de')→'vo.hero.intro_01' and ('subtitle_004','fr')→'vo.hero.intro_02' within a UI width budget of 200, and return exclusively 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["de", "fr"], "keys": ["vo.hero.intro_01", "vo.hero.intro_02"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["de", "fr"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "fr"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de","fr"], "line_ids": ["subtitle_002","subtitle_004"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "fr": "artifact://bundle/bundle-fr-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_097",
        instruction=(
            "Apply the Localization/VO Protocol V2 to PR 999 for ja. Generate a review bundle that adheres to standards for ('subtitle_006','ja') → 'vo.villain.threat_01', ensuring it fits within a UI width budget of 200, and submit only 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["ja"], "keys": ["vo.villain.threat_01"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["ja"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["ja"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["ja"], "line_ids": ["subtitle_006"], "bundle_uris": {"ja": "artifact://bundle/bundle-ja-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_098",
        instruction=(
            "Create a zh+es UI compliance pass for PR 999 following the Localization/VO Protocol V2. Produce compliant review bundles for ('subtitle_010','zh') → 'vo.ui.menu_select' and ('subtitle_008','es') → 'vo.npc.quest_01', making sure they meet a UI width budget of 200. Annotate PR 999 and return solely 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["zh", "es"], "keys": ["vo.ui.menu_select", "vo.npc.quest_01"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["zh", "es"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-zh-1", "report_uri": "artifact://bundle/bundle-zh-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-es-1", "report_uri": "artifact://bundle/bundle-es-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["zh","es"], "line_ids": ["subtitle_010","subtitle_008"], "bundle_uris": {"zh": "artifact://bundle/bundle-zh-1", "es": "artifact://bundle/bundle-es-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_099",
        instruction=(
            "Handle the Localization/VO Protocol V2 for PR 999 concerning fr and ja. Develop compliant review bundles for ('subtitle_004','fr')→'vo.hero.intro_02' and ('subtitle_006','ja')→'vo.villain.threat_01' adhering to a UI width limit of 200, and return solely 'pr_999'."
        ),
        actions=[
            Action(name="PretranslateLockedGlossaryV2", kwargs={"locales": ["fr", "ja"], "keys": ["vo.hero.intro_02", "vo.villain.threat_01"], "glossary_lock": True}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["fr", "ja"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["fr","ja"], "line_ids": ["subtitle_004","subtitle_006"], "bundle_uris": {"fr": "artifact://bundle/bundle-fr-1", "ja": "artifact://bundle/bundle-ja-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_100",
        instruction=(
            "Administer the Localization/VO Protocol V2 for PR 999 to create a three‑locale confirmation for hero (de, fr) and UI (zh) keys. Formulate compliant review bundles for ('subtitle_002','de')→'vo.hero.intro_01', ('subtitle_004','fr')→'vo.hero.intro_02', and ('subtitle_010','zh')→'vo.ui.menu_select' with a UI width limit of 200, and return strictly 'pr_999'."
        ),
        actions=[
            Action(name="LocLintV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="LocLintV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="LookupSubtitleIdsV2", kwargs={"locales": ["de", "fr", "zh"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="SynthesizeTempVoV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="ValidateSubtitleTimingV2", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="WriteLocaleBundleV2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="CreateTmsJobV2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "fr", "zh"], "status": "in_review"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="AnnotatePrWithQaV2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-zh-1", "report_uri": "artifact://bundle/bundle-zh-1"}),
            Action(name="RecordAutomationRunV2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de","fr","zh"], "line_ids": ["subtitle_002","subtitle_004","subtitle_010"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "fr": "artifact://bundle/bundle-fr-1", "zh": "artifact://bundle/bundle-zh-1"}}, "status": "completed"}),
            Action(name="ReturnScalarV2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

]
