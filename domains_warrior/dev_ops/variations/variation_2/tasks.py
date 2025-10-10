from domains.dto import Task, Action


TASKS = [
    Task(
        annotator="0",
        user_id="v2_task_001",
        instruction=(
            "You are responsible for CI triage on the game-engine repository. Resolve the failed Windows build run run_001 on branch feature/new-renderer at commit abc123def456789 (job build-windows-x64) using the CI Build Failure Protocol V2 and policy templates. Link evidence, open a draft PR on 'auto/fix-run_001', create the ENGINE-MIG work item tied to the PR, trigger smoke validation, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_001", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "build-windows-x64"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_001"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_001"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_001"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_001"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_001"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_001"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_001", "patch_id": "FP-run_001", "run_id": "run_001"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_001", "base": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_001", "description": "Automated triage for run_001", "run_id": "run_001", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_001"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_002",
        instruction=(
            "You manage CI triage for game-engine. Run run_003 failed (job test-unit-windows) on branch feature/new-renderer at commit abc123def456789. Follow the CI Build Failure Protocol V2 to persist signals, bisect using the run's repro command, stage a minimal fix, open a draft PR, file a BUILD-MOD ticket, validate the draft, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_003"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_003"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_003"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_003"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_003"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_003"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "run_id": "run_003"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "BUILD-MOD", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_003",
        instruction=(
            "As CI triage owner, your must address failed integration tests for run run_005 (job test-integration-linux) on branch feature/new-renderer at commit def456abc123789. Apply Protocol V2 end-to-end, keep to deterministic templates, file under ENGINE-MIG, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_005"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_005"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_005"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_005"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_005"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_005"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_004",
        instruction=(
            "You must handle performance regression triage for run run_007 (job performance-test-windows) on branch feature/new-renderer at commit abc123def456789. Use CI Build Failure Protocol V2, stage a minimal fix, open a draft PR, create BUILD-MOD ticket, validate, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_007"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_007"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_007"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_007"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_007"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_007"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "run_id": "run_007"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "BUILD-MOD", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_005",
        instruction=(
            "You must oversee CI triage. Resolve failed staging deployment run run_010 (job deploy-staging-windows) on feature/new-renderer at commit abc123def456789. Apply Protocol V2 with deterministic templates, open a draft PR, create ENGINE-MIG ticket, validate, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_010", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "deploy-staging-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_010"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_010"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_010"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_010"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_010"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_010"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_010", "patch_id": "FP-run_010", "run_id": "run_010"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_010", "base": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_010", "description": "Automated triage for run_010", "run_id": "run_010", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_010"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    # Repeat on other failure categories/routing projects to ensure diversity while staying deterministic
    Task(
        annotator="0",
        user_id="v2_task_006",
        instruction=(
            "For governance, you must ensure run run_001 build failure is triaged under BUILD-MOD with the same CI Build Failure Protocol V2 and template constraints. Produce the draft PR, link the ticket, validate, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_001", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "build-windows-x64"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_001"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_001"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_001"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_001"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_001"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_001"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_001", "patch_id": "FP-run_001", "run_id": "run_001"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_001", "base": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "BUILD-MOD", "summary": "CI failure run_001", "description": "Automated triage for run_001", "run_id": "run_001", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_001"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_007",
        instruction=(
            "You must triage unit test failure again for run run_003 under ENGINE-MIG to ensure cross-project rules are followed deterministically. Execute Protocol V2 fully, open draft PR, create ticket, validate, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_003"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_003"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_003"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_003"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_003"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_003"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "run_id": "run_003"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_008",
        instruction=(
            "You must resolve run run_005 integration failure under BUILD-MOD using Protocol V2 with deterministic fields only. Open a draft PR and linked ticket, validate, and return the draft PR number only."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_005"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_005"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_005"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_005"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_005"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_005"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "BUILD-MOD", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_009",
        instruction=(
            "You must re-run performance triage for run run_007 under ENGINE-MIG with CI Build Failure Protocol V2 and deterministic templates. Draft PR, link ticket, validate, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_007"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_007"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_007"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_007"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_007"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_007"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "run_id": "run_007"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_010",
        instruction=(
            "You must close the loop on run run_010 by executing CI Build Failure Protocol V2 with BUILD-MOD routing. Use policy templates, record all links, open a draft PR, create the ticket, validate the draft, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_010", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "deploy-staging-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_010"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_010"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_010"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_010"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_010"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_010"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_010", "patch_id": "FP-run_010", "run_id": "run_010"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_010", "base": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "BUILD-MOD", "summary": "CI failure run_010", "description": "Automated triage for run_010", "run_id": "run_010", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_010"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_011",
        instruction=(
            "You must resolve a unit test failure for run run_003 (job test-unit-windows) on branch feature/new-renderer at commit abc123def456789. Apply the CI Build Failure Protocol V2 strictly, persist signals, bisect using the job repro, open a draft PR, create a TEST-INFRA ticket, trigger validation, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_003"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_003"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_003"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_003"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_003"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_003"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "run_id": "run_003"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "TEST-INFRA", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "TEST-INFRA-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_012",
        instruction=(
            "You must triage the same unit test failure for run run_003 (test-unit-windows) under PERF-MON governance. Follow Protocol V2, open a draft PR, create the PERF-MON ticket with policy templates, trigger validation, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_003"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_003"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_003"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_003"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_003"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_003"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "run_id": "run_003"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "PERF-MON", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "PERF-MON-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_013",
        instruction=(
            "You must address integration test failures for run run_005 (job test-integration-linux) on feature/new-renderer at commit def456abc123789. Apply Protocol V2, open draft PR, create MULTI-PLAT ticket, validate, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_005"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_005"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_005"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_005"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_005"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_005"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "MULTI-PLAT", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "MULTI-PLAT-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_014",
        instruction=(
            "You must triage run run_005 integration failures under API-GATEWAY oversight. Execute Protocol V2, open a draft PR, create the API-GATEWAY ticket, trigger validation, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_005"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_005"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_005"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_005"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_005"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_005"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "API-GATEWAY", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "API-GATEWAY-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_015",
        instruction=(
            "You must resolve integration test failures for run run_005 under DB-UPGRADE policy. Follow Protocol V2 fully, open draft PR, create DB-UPGRADE ticket, validate, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_005"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_005"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_005"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_005"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_005"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_005"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "DB-UPGRADE", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "DB-UPGRADE-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_016",
        instruction=(
            "You must handle performance test failure triage for run run_007 (job performance-test-windows) on branch feature/new-renderer at commit abc123def456789. Execute Protocol V2, open a draft PR, create PERF-MON ticket, validate, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_007"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_007"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_007"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_007"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_007"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_007"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "run_id": "run_007"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "PERF-MON", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "PERF-MON-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_017",
        instruction=(
            "You must triage performance test failures for run run_007 under GAME-ANALYTICS. Apply Protocol V2, open a draft PR, create a GAME-ANALYTICS ticket, validate, and return the draft PR number only."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_007"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_007"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_007"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_007"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_007"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_007"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "run_id": "run_007"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "GAME-ANALYTICS", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "GAME-ANALYTICS-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_018",
        instruction=(
            "You must re-run performance test triage for run run_007 under BUILD-MOD as part of coverage. Follow Protocol V2 and policy templates, open a draft PR, create BUILD-MOD ticket, validate, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_007"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_007"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_007"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_007"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_007"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_007"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "run_id": "run_007"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "BUILD-MOD", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_019",
        instruction=(
            "You must reconcile unit test failure triage for run run_003 under ENGINE-MIG. Execute Protocol V2, open draft PR, create ENGINE-MIG ticket, validate, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_003"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_003"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_003"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_003"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_003"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_003"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "run_id": "run_003"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_020",
        instruction=(
            "You must finalize integration test failure triage for run run_005 under COST-OPT oversight. Strictly follow Protocol V2, open a draft PR, create COST-OPT ticket, validate, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_005"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_005"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_005"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_005"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_005"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_005"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "COST-OPT", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "COST-OPT-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_021",
        instruction=(
            "You must triage a crash-related build failure for run run_001 on branch feature/new-renderer at commit abc123def456789 (job build-windows-x64). Apply Protocol V2 with emphasis on reduced logs, symbolication, and incident correlation; then open a draft PR, create a GAME-SEC ticket, trigger validation, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_001", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "build-windows-x64"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_001"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_001"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_001"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_001"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_001"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_001"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_001", "patch_id": "FP-run_001", "run_id": "run_001"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_001", "base": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "GAME-SEC", "summary": "CI failure run_001", "description": "Automated triage for run_001", "run_id": "run_001", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_001"}, "outputs": {"pr_number": 33, "ticket_key": "GAME-SEC-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_022",
        instruction=(
            "You must triage a crash-related test failure for run run_003 (test-unit-windows) on feature/new-renderer at commit abc123def456789 by symbolication and incident correlation per Protocol V2 for signature='sig:abc123def456789:first_failure'; open a draft PR, create a REG-SEC ticket, run validation, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_003"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_003"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_003"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_003"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_003"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_003"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "run_id": "run_003"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "REG-SEC", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "REG-SEC-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_023",
        instruction=(
            "You must triage a crash-context integration failure for run run_005 (test-integration-linux) on feature/new-renderer at commit def456abc123789 by symbolication and correlation per policy; open a draft PR, create a NET-SEC ticket, validate, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_005"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_005"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_005"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_005"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_005"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_005"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "NET-SEC", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "NET-SEC-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_024",
        instruction=(
            "You must triage a crash-context performance regression for run run_007 (performance-test-windows) on feature/new-renderer at commit abc123def456789 using Protocol V2 with symbolication and incident correlation; open a draft PR, create a PERF-MON ticket, validate, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_007"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_007"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_007"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_007"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_007"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_007"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "run_id": "run_007"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "PERF-MON", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "PERF-MON-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_025",
        instruction=(
            "You must triage a crash-context deployment failure for run run_010 (deploy-staging-windows) on feature/new-renderer at commit abc123def456789, emphasizing symbolication and correlation; open a draft PR, create a DR-IMPL ticket, validate, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_010", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "deploy-staging-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_010"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_010"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_010"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_010"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_010"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_010"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_010", "patch_id": "FP-run_010", "run_id": "run_010"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_010", "base": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "DR-IMPL", "summary": "CI failure run_010", "description": "Automated triage for run_010", "run_id": "run_010", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_010"}, "outputs": {"pr_number": 33, "ticket_key": "DR-IMPL-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_026",
        instruction=(
            "You must Re-run Protocol V2 crash triage for run run_001 on branch feature/new-renderer at commit abc123def456789 (job build-windows-x64). Apply the crash triage policy areas (reduced log window, symbolication, similar-incident lookup), then open a draft PR, create an EDGE-PLAT ticket, trigger smoke validation for the associated PR, and return only the draft PR number."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_001", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "build-windows-x64"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_001"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_001"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_001"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_001"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_001"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_001"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_001", "patch_id": "FP-run_001", "run_id": "run_001"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_001", "base": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "EDGE-PLAT", "summary": "CI failure run_001", "description": "Automated triage for run_001", "run_id": "run_001", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_001", "test_target": "make build-windows-x64"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_001"}, "outputs": {"pr_number": 33, "ticket_key": "EDGE-PLAT-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_027",
        instruction=(
            "You must perform crash symbolication triage for run run_003 and then open a draft PR, create an API-GATEWAY ticket, validate, and return only the draft PR number, strictly following Protocol V2."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_003"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_003"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_003"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_003"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_003"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_003"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "run_id": "run_003"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "API-GATEWAY", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_003", "test_target": "make test-unit-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "API-GATEWAY-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_028",
        instruction=(
            "You must handle crash-context integration triage for run run_005 and then open a draft PR, create a DB-UPGRADE ticket, validate, and return only the draft PR number, all per Protocol V2."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_005"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_005"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_005"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_005"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_005"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_005"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "run_id": "run_005"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "DB-UPGRADE", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_005", "test_target": "make test-integration-linux"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "DB-UPGRADE-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_029",
        instruction=(
            "You must perform crash symbolication and correlation for run run_007 and proceed to open a draft PR, create a GAME-ANALYTICS ticket, validate, and return only the draft PR number per Protocol V2."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_007"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_007"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_007"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_007"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_007"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_007"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "run_id": "run_007"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "GAME-ANALYTICS", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_007", "test_target": "make performance-test-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "GAME-ANALYTICS-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_030",
        instruction=(
            "You must complete crash symbolication triage for run run_010 and then open a draft PR, create an IAC-MIG ticket, validate, and return only the draft PR number, strictly following Protocol V2."
        ),
        actions=[
            Action(name="ingest_ci_webhook_v2", kwargs={"provider": "github_actions", "run_id": "run_010", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "deploy-staging-windows"}),
            Action(name="guardrail_validate_sender_v2", kwargs={"run_id": "run_010"}),
            Action(name="attach_artifacts_index_v2", kwargs={"run_id": "run_010"}),
            Action(name="reduce_log_window_v2", kwargs={"run_id": "run_010"}),
            Action(name="symbolicate_minidump_v2", kwargs={"run_id": "run_010"}),
            Action(name="similar_incident_lookup_v2", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects_v2", kwargs={"run_id": "run_010"}),
            Action(name="launch_targeted_bisect_v2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="draft_fix_diff_v2", kwargs={"run_id": "run_010"}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-run_010", "patch_id": "FP-run_010", "run_id": "run_010"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-run_010", "base": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "IAC-MIG", "summary": "CI failure run_010", "description": "Automated triage for run_010", "run_id": "run_010", "pr_number": 33}),
            Action(name="trigger_smoke_validation_v2", kwargs={"run_id": "run_010", "test_target": "make deploy-staging-windows"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_010"}, "outputs": {"pr_number": 33, "ticket_key": "IAC-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_031",
        instruction=(
            "You are responsible for curating the asset QA intake associated with commit abc123def456789 on branch feature/new-renderer. Ensure the complete changed set is validated to texture and engine budgets, generate previews, stage a deterministic draft change linked to a GAME-ANALYTICS work item, and return only the draft PR number."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": [
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
            Action(name="enforce_texture_policies_v2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/animations/characters/hero_idle.fbx",
                "assets/models/environment/castle_tower.fbx"
            ], "scene": "BudgetScene:abc123def456789"}),
            Action(name="render_turntable_v2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/animations/characters/hero_idle.fbx",
                "assets/models/environment/castle_tower.fbx"
            ]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [
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
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "assetqa_abc123def456789"}),
            Action(name="deterministic_autofix_v2", kwargs={"qa_json": [
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
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-assetqa_abc123def456789", "patch_id": "AF-1", "run_id": "assetqa_abc123def456789"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-assetqa_abc123def456789", "base": "feature/new-renderer", "run_id": "assetqa_abc123def456789"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "GAME-ANALYTICS", "summary": "asset_qa:commit=abc123def456789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "assetqa_abc123def456789", "pr_number": 33}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=abc123def456789", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check_v2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "abc123def456789"}, "outputs": {"pr_number": 33, "ticket_key": "GAME-ANALYTICS-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_032",
        instruction=(
            "You are responsible for the environment-focused asset QA intake around commit def456abc123789 on branch feature/new-renderer. Deliver a reviewable QA bundle for the changed environment assets with previews, stage a deterministic draft change linked to a BUILD-MOD work item, and return only the draft PR number."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": [
                "assets/models/environment/castle_tower.fbx",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png",
                "assets/materials/environment/castle_tower.mtl"
            ]}),
            Action(name="enforce_texture_policies_v2", kwargs={"files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="render_turntable_v2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [
                {"file": "assets/models/environment/castle_tower.fbx", "issues": []},
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []},
                {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []},
                {"file": "assets/materials/environment/castle_tower.mtl", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/models/environment/castle_tower.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "assetqa_def456abc123789"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-assetqa_def456abc123789", "patch_id": "AF-assetqa_def456abc123789", "run_id": "assetqa_def456abc123789"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-assetqa_def456abc123789", "base": "feature/new-renderer", "run_id": "assetqa_def456abc123789"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "BUILD-MOD", "summary": "asset_qa:commit=def456abc123789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "assetqa_def456abc123789", "pr_number": 33}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=def456abc123789", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check_v2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "def456abc123789"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_033",
        instruction=(
            "You are accountable for the character normal-map QA tied to commit abc123def456789 on branch feature/new-renderer. Deliver a reviewable QA bundle for the impacted textures, generate previews, stage a deterministic draft linked to an ENGINE-MIG work item, and return only the draft PR number."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": [
                "assets/textures/characters/hero_character_normal.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="enforce_texture_policies_v2", kwargs={"files": [
                "assets/textures/characters/hero_character_normal.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": [
                "assets/textures/characters/hero_character_normal.png",
                "assets/textures/environment/castle_tower_normal.png"
            ], "scene": "BudgetScene:abc123def456789"}),
            Action(name="render_turntable_v2", kwargs={"files": [
                "assets/textures/characters/hero_character_normal.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="deterministic_autofix_v2", kwargs={"qa_json": [
                {"file": "assets/textures/characters/hero_character_normal.png"},
                {"file": "assets/textures/environment/castle_tower_normal.png"}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [
                {"file": "assets/textures/characters/hero_character_normal.png", "issues": []},
                {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": [
                "assets/textures/characters/hero_character_normal.png",
                "assets/textures/environment/castle_tower_normal.png"
            ], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/2", "stills_uris": ["artifact://still/1", "artifact://still/2"]}}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "assetqa_abc123def456789"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-assetqa_abc123def456789", "patch_id": "AF-1", "run_id": "assetqa_abc123def456789"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-assetqa_abc123def456789", "base": "feature/new-renderer", "run_id": "assetqa_abc123def456789"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "ENGINE-MIG", "summary": "asset_qa:commit=abc123def456789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "assetqa_abc123def456789", "pr_number": 33}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=abc123def456789", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check_v2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "abc123def456789"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_034",
        instruction=(
            "You must run asset QA for environment textures at commit def456abc123789. Apply Protocol V2 deterministically, enforce texture budgets, publish QA, open a draft PR, create a MULTI-PLAT ticket, and return the draft PR number only."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png", "assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="enforce_texture_policies_v2", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png", "assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png", "assets/textures/environment/castle_tower_diffuse.png"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="render_turntable_v2", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png", "assets/textures/environment/castle_tower_diffuse.png"]}),
            Action(name="deterministic_autofix_v2", kwargs={"qa_json": [
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []},
                {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [{"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}, {"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []}], "tex_report": [{"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}, {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True}], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/textures/environment/castle_tower_normal.png", "assets/textures/environment/castle_tower_diffuse.png"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/2", "stills_uris": ["artifact://still/1", "artifact://still/2"]}}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "main", "run_id": "def456abc123789"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-def456abc123789", "patch_id": "AF-1", "run_id": "def456abc123789"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-def456abc123789", "base": "main", "run_id": "def456abc123789"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "MULTI-PLAT", "summary": "asset_qa:commit=def456abc123789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "def456abc123789", "pr_number": 33}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=def456abc123789", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check_v2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "def456abc123789"}, "outputs": {"pr_number": 33, "ticket_key": "MULTI-PLAT-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_035",
        instruction=(
            "You own the character model-and-texture QA related to commit abc123def456789. Produce a comprehensive QA bundle with previews for the model and its textures, stage a deterministic draft linked to ENGINE-MIG, and return only the draft PR number."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="enforce_texture_policies_v2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": ["assets/models/characters/hero_character.fbx"], "scene": "BudgetScene:abc123def456789"}),
            Action(name="render_turntable_v2", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="deterministic_autofix_v2", kwargs={"qa_json": [
                {"file": "assets/models/characters/hero_character.fbx"},
                {"file": "assets/textures/characters/hero_character_diffuse.png"},
                {"file": "assets/textures/characters/hero_character_normal.png"}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "ok": True},
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True}
            ]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [
                {"file": "assets/models/characters/hero_character.fbx", "issues": []},
                {"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []},
                {"file": "assets/textures/characters/hero_character_normal.png", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "ok": True},
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": ["assets/models/characters/hero_character.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "main", "run_id": "assetqa_abc123def456789"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-assetqa_abc123def456789", "patch_id": "AF-1", "run_id": "assetqa_abc123def456789"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-assetqa_abc123def456789", "base": "main", "run_id": "assetqa_abc123def456789"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "ENGINE-MIG", "summary": "asset_qa:commit=abc123def456789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "assetqa_abc123def456789", "pr_number": 33}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=abc123def456789", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check_v2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "abc123def456789"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_036",
        instruction=(
            "You are to complete the material QA associated with commit def456abc123789. Provide a clear QA bundle, raise an API-GATEWAY work item linked to the draft, and return only the draft PR number."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": [
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
            Action(name="enforce_texture_policies_v2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="render_turntable_v2", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [{"file": "assets/materials/environment/castle_tower.mtl", "issues": []}], "tex_report": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "ok": True},
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/materials/environment/castle_tower.mtl"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "main", "run_id": "def456abc123789"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-def456abc123789", "base": "main", "run_id": "def456abc123789"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "API-GATEWAY", "summary": "asset_qa:commit=def456abc123789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "def456abc123789", "pr_number": 33}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=def456abc123789", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check_v2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "def456abc123789"}, "outputs": {"pr_number": 33, "ticket_key": "API-GATEWAY-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_037",
        instruction=(
            "You are responsible for the audio QA associated with commit abc123def456789. Provide a clean QA bundle for the changed audio assets, raise a GAME-ANALYTICS work item linked to the draft, and return only the draft PR number."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav", "assets/audio/music/main_theme.ogg"]}),
            Action(name="render_audio_preview_v2", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav", "assets/audio/music/main_theme.ogg"]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav", "assets/audio/music/main_theme.ogg"], "scene": "BudgetScene:abc123def456789"}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [{"file": "assets/audio/sfx/hero_sword_swing.wav", "issues": []}, {"file": "assets/audio/music/main_theme.ogg", "issues": []}], "tex_report": [], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": ["assets/audio/sfx/hero_sword_swing.wav", "assets/audio/music/main_theme.ogg"], "violations": []}, "previews": {"audio_preview_uri": "artifact://audio_preview/2"}}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "main", "run_id": "abc123def456789"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-abc123def456789", "base": "main", "run_id": "abc123def456789"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "GAME-ANALYTICS", "summary": "asset_qa:commit=abc123def456789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "abc123def456789", "pr_number": 33}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=abc123def456789", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check_v2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "abc123def456789"}, "outputs": {"pr_number": 33, "ticket_key": "GAME-ANALYTICS-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_038",
        instruction=(
            "You are accountable for the animation QA linked to commit abc123def456789. Prepare a focused QA bundle with previews, link a BUILD-MOD work item to the draft, and return only the draft PR number."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"], "scene": "BudgetScene:abc123def456789"}),
            Action(name="render_turntable_v2", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="deterministic_autofix_v2", kwargs={"qa_json": [{"file": "assets/animations/characters/hero_idle.fbx"}], "tex_report": []}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [{"file": "assets/animations/characters/hero_idle.fbx", "issues": []}], "tex_report": [], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": ["assets/animations/characters/hero_idle.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "main", "run_id": "assetqa_abc123def456789"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-assetqa_abc123def456789", "patch_id": "AF-1", "run_id": "assetqa_abc123def456789"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-assetqa_abc123def456789", "base": "main", "run_id": "assetqa_abc123def456789"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "BUILD-MOD", "summary": "asset_qa:commit=abc123def456789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "assetqa_abc123def456789", "pr_number": 33}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=abc123def456789", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check_v2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "abc123def456789"}, "outputs": {"pr_number": 33, "ticket_key": "BUILD-MOD-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_039",
        instruction=(
            "You are to deliver the environment texture QA associated with commit def456abc123789 on branch feature/new-renderer. Provide a clear QA bundle for the changed textures with previews, raise a GAME-ANALYTICS work item tied to the draft, and return only the draft PR number."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png", "assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="enforce_texture_policies_v2", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png", "assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png", "assets/textures/environment/castle_tower_normal.png"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="render_turntable_v2", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png", "assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="deterministic_autofix_v2", kwargs={"qa_json": [{"file": "assets/textures/environment/castle_tower_diffuse.png"}, {"file": "assets/textures/environment/castle_tower_normal.png"}], "tex_report": [{"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True}, {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [{"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []}, {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}], "tex_report": [{"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True}, {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/textures/environment/castle_tower_diffuse.png", "assets/textures/environment/castle_tower_normal.png"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/2", "stills_uris": ["artifact://still/1", "artifact://still/2"]}}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "feature/new-renderer", "run_id": "assetqa_def456abc123789"}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-assetqa_def456abc123789", "patch_id": "AF-1", "run_id": "assetqa_def456abc123789"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-assetqa_def456abc123789", "base": "feature/new-renderer", "run_id": "assetqa_def456abc123789"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "GAME-ANALYTICS", "summary": "asset_qa:commit=def456abc123789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "assetqa_def456abc123789", "pr_number": 33}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=def456abc123789", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check_v2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "def456abc123789"}, "outputs": {"pr_number": 33, "ticket_key": "GAME-ANALYTICS-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_040",
        instruction=(
            "You are responsible for an additional environment model QA tied to commit def456abc123789. Validate castle tower model budgets, attach previews, open a deterministic draft, create an ENGINE-MIG work item linked to the draft, and return only the draft PR number."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="render_turntable_v2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [{"file": "assets/models/environment/castle_tower.fbx", "issues": []}], "tex_report": [], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/models/environment/castle_tower.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="open_auto_branch_v2", kwargs={"base_ref": "main", "run_id": "assetqa_def456abc123789"}),
            Action(name="deterministic_autofix_v2", kwargs={"qa_json": [{"file": "assets/models/environment/castle_tower.fbx"}], "tex_report": []}),
            Action(name="commit_patch_to_branch_v2", kwargs={"branch_ref": "auto/fix-assetqa_def456abc123789", "patch_id": "AF-1", "run_id": "assetqa_def456abc123789"}),
            Action(name="open_draft_pr_v2", kwargs={"head": "auto/fix-assetqa_def456abc123789", "base": "main", "run_id": "assetqa_def456abc123789"}),
            Action(name="create_or_update_ticket_v2", kwargs={"project_key": "ENGINE-MIG", "summary": "asset_qa:commit=def456abc123789", "description": "asset_qa_details_uri=artifact://qa/summary", "run_id": "assetqa_def456abc123789", "pr_number": 33}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 33, "summary": "asset_qa:commit=def456abc123789", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check_v2", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-qa", "inputs": {"commit_sha": "def456abc123789"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_041",
        instruction=(
            "You are responsible for engine-side budget validation for the updated castle environment at commit def456abc123789. Validate model, textures, and material to engine budgets, publish previews, persist deterministic QA outcomes for each asset, and return the commit SHA only."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": [
                "assets/models/environment/castle_tower.fbx",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png",
                "assets/materials/environment/castle_tower.mtl"
            ]}),
            Action(name="enforce_texture_policies_v2", kwargs={"files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="render_turntable_v2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [
                {"file": "assets/models/environment/castle_tower.fbx", "issues": []},
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []},
                {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []},
                {"file": "assets/materials/environment/castle_tower.mtl", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/models/environment/castle_tower.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/models/environment/castle_tower.fbx", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/textures/environment/castle_tower_diffuse.png", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/textures/environment/castle_tower_normal.png", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/materials/environment/castle_tower.mtl", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "def456abc123789", "assets": [
                "assets/models/environment/castle_tower.fbx",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png",
                "assets/materials/environment/castle_tower.mtl"
            ]}, "outputs": {"assets_processed": 4}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "def456abc123789"}),
        ],
        outputs=["def456abc123789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_042",
        instruction=(
            "You own the engine budget validation for the updated hero character pack at commit abc123def456789. Validate model, textures, and animation, publish previews, persist the outcomes for each asset deterministically, and return the commit SHA only."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png",
                "assets/animations/characters/hero_idle.fbx"
            ]}),
            Action(name="enforce_texture_policies_v2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/animations/characters/hero_idle.fbx"
            ], "scene": "BudgetScene:abc123def456789"}),
            Action(name="render_turntable_v2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/animations/characters/hero_idle.fbx"
            ]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [
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
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/models/characters/hero_character.fbx", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/textures/characters/hero_character_diffuse.png", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/textures/characters/hero_character_normal.png", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/animations/characters/hero_idle.fbx", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "abc123def456789", "assets": [
                "assets/models/characters/hero_character.fbx",
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png",
                "assets/animations/characters/hero_idle.fbx"
            ]}, "outputs": {"assets_processed": 4}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "abc123def456789"}),
        ],
        outputs=["abc123def456789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_043",
        instruction=(
            "You must validate engine budgets for the environment textures changed at commit def456abc123789, publish previews, persist outcomes for each texture, and return only the commit SHA."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="enforce_texture_policies_v2", kwargs={"files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ], "scene": "BudgetScene:def456abc123789"}),
            Action(name="render_turntable_v2", kwargs={"files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []},
                {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/2", "stills_uris": ["artifact://still/1", "artifact://still/2"]}}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/textures/environment/castle_tower_diffuse.png", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/textures/environment/castle_tower_normal.png", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "def456abc123789", "assets": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}, "outputs": {"assets_processed": 2}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "def456abc123789"}),
        ],
        outputs=["def456abc123789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_044",
        instruction=(
            "You must run engine budget checks for the hero character textures at commit abc123def456789. Apply texture policies, publish previews, persist deterministic outcomes per texture, and return the commit SHA only."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="enforce_texture_policies_v2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ], "scene": "BudgetScene:abc123def456789"}),
            Action(name="render_turntable_v2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []},
                {"file": "assets/textures/characters/hero_character_normal.png", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "ok": True},
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/2", "stills_uris": ["artifact://still/1", "artifact://still/2"]}}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/textures/characters/hero_character_diffuse.png", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/textures/characters/hero_character_normal.png", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/2", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "abc123def456789", "assets": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}, "outputs": {"assets_processed": 2}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "abc123def456789"}),
        ],
        outputs=["abc123def456789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_045",
        instruction=(
            "You must complete engine budget validation for the castle tower model at commit def456abc123789. Publish previews, persist the outcome deterministically, and return only the commit SHA."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="render_turntable_v2", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [{"file": "assets/models/environment/castle_tower.fbx", "issues": []}], "tex_report": [], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/models/environment/castle_tower.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/models/environment/castle_tower.fbx", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "def456abc123789", "assets": ["assets/models/environment/castle_tower.fbx"]}, "outputs": {"assets_processed": 1}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "def456abc123789"}),
        ],
        outputs=["def456abc123789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_046",
        instruction=(
            "You must finalize engine budget validation for the castle material at commit def456abc123789. Publish preview, persist the material outcome deterministically, and return only the commit SHA."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"], "scene": "BudgetScene:def456abc123789"}),
            Action(name="render_turntable_v2", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [{"file": "assets/materials/environment/castle_tower.mtl", "issues": []}], "tex_report": [], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": ["assets/materials/environment/castle_tower.mtl"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/materials/environment/castle_tower.mtl", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "def456abc123789", "assets": ["assets/materials/environment/castle_tower.mtl"]}, "outputs": {"assets_processed": 1}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "def456abc123789"}),
        ],
        outputs=["def456abc123789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_047",
        instruction=(
            "You must perform engine budget checks for the hero character model at commit abc123def456789. Publish preview, persist the outcome deterministically, and return only the commit SHA."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": ["assets/models/characters/hero_character.fbx"], "scene": "BudgetScene:abc123def456789"}),
            Action(name="render_turntable_v2", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [{"file": "assets/models/characters/hero_character.fbx", "issues": []}], "tex_report": [], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": ["assets/models/characters/hero_character.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/models/characters/hero_character.fbx", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "abc123def456789", "assets": ["assets/models/characters/hero_character.fbx"]}, "outputs": {"assets_processed": 1}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "abc123def456789"}),
        ],
        outputs=["abc123def456789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_048",
        instruction=(
            "You must execute engine budget validation for the hero animation at commit abc123def456789. Publish preview, persist the outcome deterministically, and return only the commit SHA."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"], "scene": "BudgetScene:abc123def456789"}),
            Action(name="render_turntable_v2", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [{"file": "assets/animations/characters/hero_idle.fbx", "issues": []}], "tex_report": [], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": ["assets/animations/characters/hero_idle.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/animations/characters/hero_idle.fbx", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "abc123def456789", "assets": ["assets/animations/characters/hero_idle.fbx"]}, "outputs": {"assets_processed": 1}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "abc123def456789"}),
        ],
        outputs=["abc123def456789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_049",
        instruction=(
            "You must perform a combined engine budget validation for the environment model and textures at commit def456abc123789. Publish previews, persist all outcomes deterministically, and return only the commit SHA."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "def456abc123789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": [
                "assets/models/environment/castle_tower.fbx",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="enforce_texture_policies_v2", kwargs={"files": [
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": [
                "assets/models/environment/castle_tower.fbx"
            ], "scene": "BudgetScene:def456abc123789"}),
            Action(name="render_turntable_v2", kwargs={"files": [
                "assets/models/environment/castle_tower.fbx",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [
                {"file": "assets/models/environment/castle_tower.fbx", "issues": []},
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []},
                {"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/environment/castle_tower_diffuse.png", "ok": True},
                {"file": "assets/textures/environment/castle_tower_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:def456abc123789", "files": [
                "assets/models/environment/castle_tower.fbx"
            ], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/3", "stills_uris": ["artifact://still/1", "artifact://still/2", "artifact://still/3"]}}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/models/environment/castle_tower.fbx", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/3", "report_uri": "artifact://qa/summary"}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/textures/environment/castle_tower_diffuse.png", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/3", "report_uri": "artifact://qa/summary"}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/textures/environment/castle_tower_normal.png", "commit_sha": "def456abc123789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/3", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "def456abc123789", "assets": [
                "assets/models/environment/castle_tower.fbx",
                "assets/textures/environment/castle_tower_diffuse.png",
                "assets/textures/environment/castle_tower_normal.png"
            ]}, "outputs": {"assets_processed": 3}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "def456abc123789"}),
        ],
        outputs=["def456abc123789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_050",
        instruction=(
            "You must conclude engine budget checks for the hero character textures and model at commit abc123def456789. Publish previews, persist deterministic outcomes for all three assets, and return only the commit SHA."
        ),
        actions=[
            Action(name="list_changed_assets_v2", kwargs={"commit_sha": "abc123def456789"}),
            Action(name="dcc_validate_assets_v2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="enforce_texture_policies_v2", kwargs={"files": [
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="engine_budget_probe_v2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx"
            ], "scene": "BudgetScene:abc123def456789"}),
            Action(name="render_turntable_v2", kwargs={"files": [
                "assets/models/characters/hero_character.fbx",
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}),
            Action(name="publish_qa_bundle_v2", kwargs={"qa_json": [
                {"file": "assets/models/characters/hero_character.fbx", "issues": []},
                {"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []},
                {"file": "assets/textures/characters/hero_character_normal.png", "issues": []}
            ], "tex_report": [
                {"file": "assets/textures/characters/hero_character_diffuse.png", "ok": True},
                {"file": "assets/textures/characters/hero_character_normal.png", "ok": True}
            ], "engine_report": {"scene": "BudgetScene:abc123def456789", "files": [
                "assets/models/characters/hero_character.fbx"
            ], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/3", "stills_uris": ["artifact://still/1", "artifact://still/2", "artifact://still/3"]}}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/models/characters/hero_character.fbx", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/3", "report_uri": "artifact://qa/summary"}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/textures/characters/hero_character_diffuse.png", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/3", "report_uri": "artifact://qa/summary"}),
            Action(name="persist_qa_outcome_v2", kwargs={"asset_id": "assets/textures/characters/hero_character_normal.png", "commit_sha": "abc123def456789", "severity_max": "info", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/3", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "asset-engine-budget", "inputs": {"commit_sha": "abc123def456789", "assets": [
                "assets/models/characters/hero_character.fbx",
                "assets/textures/characters/hero_character_diffuse.png",
                "assets/textures/characters/hero_character_normal.png"
            ]}, "outputs": {"assets_processed": 3}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "abc123def456789"}),
        ],
        outputs=["abc123def456789"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_051",
        instruction=(
            "You must deduplicate the crash ticket work_026 against its canonical issue, compute an impact score using the renderer crash fingerprint, route it to the renderer module owner, transition it to Triage, and return only the ticket key."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026", "severity": "critical", "module": "renderer", "crash_fingerprint": "renderer_character_load_access_violation_xyz"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "work_026"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "work_026"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "work_026", "fingerprint": "renderer_character_load_access_violation_xyz"}),
            Action(name="find_ownership_path_v2", kwargs={"contains": "renderer"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "work_026"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "work_026", "fields": {"assigned_team": "team_001", "state": "Triage", "duplicate_of": "work_027"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_026", "fingerprint": "renderer_character_load_access_violation_xyz"}, "outputs": {"assigned_team": "team_001", "state": "Triage", "duplicate_of": "work_027"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "work_026"}),
        ],
        outputs=["work_026"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_052",
        instruction=(
            "You must compute impact for the texture artifact ticket work_027, resolve ownership specifically for the path 'assets/textures/character_models/' from the ownership map and assign the ticket to that team, confirm and record the canonical duplicate if present, persist exactly the generated summary text on the ticket (no alterations), set its state to Triage, and return only the ticket key."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_027"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "work_027"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "work_027"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "work_027"}),
            Action(name="find_ownership_path_v2", kwargs={"contains": "assets/textures/character_models/"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "assets/textures/character_models/"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "work_027"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "work_027", "fields": {"assigned_team": "team_002", "state": "Triage", "duplicate_of": "work_026", "summary_text": "Issue :: ", "impact_score": 2}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_027"}, "outputs": {"assigned_team": "team_002", "state": "Triage", "duplicate_of": "work_026", "impact_score": 2}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "work_027"}),
        ],
        outputs=["work_027"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_053",
        instruction=(
            "You must process the new bug work_029, compute impact, mark it as a duplicate of work_030 per deduplication records, and route it to the Network module owner responsible for 'src/game/network/multiplayer.cpp'. Set it to Triage and return only the ticket key."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_029"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "work_029"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "work_029"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "work_029"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "src/game/network/multiplayer.cpp"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "work_029"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "work_029", "fields": {"assigned_team": "team_003", "state": "Triage", "duplicate_of": "work_030"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_029"}, "outputs": {"assigned_team": "team_003", "state": "Triage", "duplicate_of": "work_030"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "work_029"}),
        ],
        outputs=["work_029"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_054",
        instruction=(
            "You must process bug_006 as a duplicate of bug_007 according to deduplication, compute impact, and route to the UI module owner responsible for 'src/game/ui/menu_system.cpp'. Move it to Triage and return only the ticket key."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_006"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "bug_006"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "bug_006"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "bug_006"}),
            Action(name="find_ownership_path_v2", kwargs={"contains": "menu_system.cpp"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "src/game/ui/menu_system.cpp"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "bug_006"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "bug_006", "fields": {"assigned_team": "team_005", "state": "Triage", "duplicate_of": "bug_007"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_006"}, "outputs": {"assigned_team": "team_005", "state": "Triage", "duplicate_of": "bug_007"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "bug_006"}),
        ],
        outputs=["bug_006"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_055",
        instruction=(
            "You must triage the Input System ticket bug_009. Use 'src/game/input/controller_handler.cpp' as the ownership anchor. After triage, the ticket must be assigned to the responsible team, set to Triage, and persist exactly the generated reviewer summary text (no alterations). Return only the ticket key."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_009"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "bug_009"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "bug_009"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "bug_009"}),
            Action(name="find_ownership_path_v2", kwargs={"contains": "controller_handler.cpp"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "src/game/input/controller_handler.cpp"}),
            Action(name="lookup_relation_v2", kwargs={"ticket_key": "bug_009"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "bug_009", "fields": {"assigned_team": "team_001", "state": "Triage", "summary_text": "Issue :: "}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_009"}, "outputs": {"assigned_team": "team_001", "state": "Triage"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "bug_009"}),
        ],
        outputs=["bug_009"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_056",
        instruction=(
            "You must route the related UI ticket work_031 to the UI owner, compute impact, update it to Triage with a relation to work_030, and return only the ticket key."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_031", "description": "Similar UI rendering issue in same menu system", "module": "ui_system"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "work_031"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "work_031"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "work_031"}),
            Action(name="find_ownership_path_v2", kwargs={"contains": "ui/"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "src/game/ui/menu_system.cpp"}),
            Action(name="lookup_relation_v2", kwargs={"ticket_key": "work_031"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "work_031", "fields": {"assigned_team": "team_005", "state": "Triage", "related_to": "work_030"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_031"}, "outputs": {"assigned_team": "team_005", "state": "Triage", "related_to": "work_030"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "work_031"}),
        ],
        outputs=["work_031"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_057",
        instruction=(
            "You must process bug_intake_012 as a duplicate of bug_intake_011. Use 'assets/audio/sound_effects/' as the ownership anchor for assignment, ensure impact is computed, set the ticket to Triage, and return only the ticket key."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_012"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="find_ownership_path_v2", kwargs={"contains": "assets/audio/sound_effects/"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "assets/audio/sound_effects/"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "bug_intake_012", "fields": {"assigned_team": "team_004", "state": "Triage", "duplicate_of": "bug_intake_011"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_intake_012"}, "outputs": {"assigned_team": "team_004", "state": "Triage", "duplicate_of": "bug_intake_011"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "bug_intake_012"}),
        ],
        outputs=["bug_intake_012"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_058",
        instruction=(
            "You must route bug_intake_014 as related to bug_intake_013 to the Physics owner. Use 'src/game/physics/collision_detection.cpp' as the ownership anchor, compute impact, set state to Triage, and return only the ticket key."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_014"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "bug_intake_014"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "bug_intake_014"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "bug_intake_014"}),
            Action(name="find_ownership_path_v2", kwargs={"contains": "src/game/physics/collision_detection.cpp"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "src/game/physics/collision_detection.cpp"}),
            Action(name="lookup_relation_v2", kwargs={"ticket_key": "bug_intake_014"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "bug_intake_014", "fields": {"assigned_team": "team_001", "state": "Triage", "related_to": "bug_intake_013"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_intake_014"}, "outputs": {"assigned_team": "team_001", "state": "Triage", "related_to": "bug_intake_013"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "bug_intake_014"}),
        ],
        outputs=["bug_intake_014"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_059",
        instruction=(
            "You must triage the AI System ticket work_028. Use 'src/game/ai/pathfinding.h' as the ownership anchor. Compute impact, check for a canonical duplicate and record it if present, check for any relation link, assign to the responsible team, set to Triage, and return only the ticket key."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_028"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "work_028"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "work_028"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "work_028"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "src/game/ai/pathfinding.h"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "work_028"}),
            Action(name="lookup_relation_v2", kwargs={"ticket_key": "work_028"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "work_028", "fields": {"assigned_team": "team_003", "state": "Triage", "duplicate_of": "work_029"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_028"}, "outputs": {"assigned_team": "team_003", "state": "Triage", "duplicate_of": "work_029"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "work_028"}),
        ],
        outputs=["work_028"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_060",
        instruction=(
            "You must process bug_016 as a duplicate of bug_017 per deduplication, compute impact, assign the physics owner, set it to Triage, and return only the ticket key."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_016"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "bug_016"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "bug_016"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "bug_016"}),
            Action(name="find_ownership_path_v2", kwargs={"contains": "physics"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "src/game/physics/collision_detection.cpp"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "bug_016"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "bug_016", "fields": {"assigned_team": "team_001", "state": "Triage", "duplicate_of": "bug_017"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_016"}, "outputs": {"assigned_team": "team_001", "state": "Triage", "duplicate_of": "bug_017"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "bug_016"}),
        ],
        outputs=["bug_016"],
    ),
    Task(
        annotator="0",
        user_id="v2_task_061",
        instruction=(
            "You must Ensure PR 999 localization readiness across de, fr, and ja per policy: deliver compliant localized content for the detected changed keys within a 200px UI constraint, register review coverage for these locales, surface the produced artifacts on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="detect_changed_strings_v2", kwargs={"pr_number": 999}),
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["de", "fr", "ja"], "keys": [
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
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": [
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
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": [
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
            Action(name="loc_lint_v2", kwargs={"locale": "ja", "keys": [
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
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": [
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
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": [
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
            Action(name="write_locale_bundle_v2", kwargs={"locale": "ja", "keys": [
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
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://tms/TMS-1", "report_uri": "artifact://tms/TMS-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-10", "report_uri": "artifact://bundle/bundle-de-10"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-10", "report_uri": "artifact://bundle/bundle-fr-10"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-10", "report_uri": "artifact://bundle/bundle-ja-10"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de", "fr", "ja"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"de": "artifact://bundle/bundle-de-10", "fr": "artifact://bundle/bundle-fr-10", "ja": "artifact://bundle/bundle-ja-10"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_062",
        instruction=(
            "You must validate PR 999 localization for de and fr: lint all changed keys at a 200px width budget, persist both locale bundles, open an in_review TMS job 'quest_shard' for de and fr, and annotate PR 999 with artifact://bundle/bundle-de-10 and artifact://bundle/bundle-fr-10. Return only 'pr_999'."
        ),
        actions=[
            Action(name="detect_changed_strings_v2", kwargs={"pr_number": 999}),
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "quest_shard", "locales": ["de", "fr"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-10", "report_uri": "artifact://bundle/bundle-de-10"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-10", "report_uri": "artifact://bundle/bundle-fr-10"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de", "fr"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"de": "artifact://bundle/bundle-de-10", "fr": "artifact://bundle/bundle-fr-10"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_063",
        instruction=(
            "You must prepare PR 999 localization for ja: lint all changed keys at a 200px width budget, persist the ja bundle, open an in_review TMS job 'quest_shard' for ja, annotate PR 999 with the bundle artifact URI, and return only 'pr_999'."
        ),
        actions=[
            Action(name="detect_changed_strings_v2", kwargs={"pr_number": 999}),
            Action(name="loc_lint_v2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "quest_shard", "locales": ["ja"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-10", "report_uri": "artifact://bundle/bundle-ja-10"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["ja"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"ja": "artifact://bundle/bundle-ja-10"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_064",
        instruction=(
            "You must complete PR 999 localization for de and ja: lint all changed keys at a 200px width budget, persist both bundles, open an in_review TMS job 'quest_shard' for de and ja, and annotate PR 999 with artifact://bundle/bundle-de-10 and artifact://bundle/bundle-ja-10. Return only 'pr_999'."
        ),
        actions=[
            Action(name="detect_changed_strings_v2", kwargs={"pr_number": 999}),
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "quest_shard", "locales": ["de", "ja"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-10", "report_uri": "artifact://bundle/bundle-de-10"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-10", "report_uri": "artifact://bundle/bundle-ja-10"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de", "ja"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"de": "artifact://bundle/bundle-de-10", "ja": "artifact://bundle/bundle-ja-10"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_065",
        instruction=(
            "You must ensure PR 999 localization readiness across de, fr, and ja in line with the localization policy: use the detected changed keys under a 200px UI width constraint to produce and persist locale bundles, open a single in_review TMS job 'loc_pr_999' covering these locales, and annotate PR 999 with the artifact URIs of the produced bundles. Return only 'pr_999'."
        ),
        actions=[
            Action(name="detect_changed_strings_v2", kwargs={"pr_number": 999}),
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-10", "report_uri": "artifact://bundle/bundle-de-10"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-10", "report_uri": "artifact://bundle/bundle-fr-10"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-10", "report_uri": "artifact://bundle/bundle-ja-10"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de", "fr", "ja"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"de": "artifact://bundle/bundle-de-10", "fr": "artifact://bundle/bundle-fr-10", "ja": "artifact://bundle/bundle-ja-10"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_066",
        instruction=(
            "You must complete PR 999 localization for de: lint all changed keys at a 200px width budget, persist the de bundle, open an in_review TMS job 'quest_shard' for de, annotate PR 999 with the bundle artifact URI, and return only 'pr_999'."
        ),
        actions=[
            Action(name="detect_changed_strings_v2", kwargs={"pr_number": 999}),
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "quest_shard", "locales": ["de"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-10", "report_uri": "artifact://bundle/bundle-de-10"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"de": "artifact://bundle/bundle-de-10"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_067",
        instruction=(
            "You must complete PR 999 localization for fr: lint all changed keys at a 200px width budget, persist the fr bundle, open an in_review TMS job 'quest_shard' for fr, annotate PR 999 with the bundle artifact URI, and return only 'pr_999'."
        ),
        actions=[
            Action(name="detect_changed_strings_v2", kwargs={"pr_number": 999}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "quest_shard", "locales": ["fr"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-10", "report_uri": "artifact://bundle/bundle-fr-10"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["fr"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"fr": "artifact://bundle/bundle-fr-10"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_068",
        instruction=(
            "You must complete PR 999 localization for ja: lint all changed keys at a 200px width budget, persist the ja bundle, open an in_review TMS job 'quest_shard' for ja, annotate PR 999 with the bundle artifact URI, and return only 'pr_999'."
        ),
        actions=[
            Action(name="detect_changed_strings_v2", kwargs={"pr_number": 999}),
            Action(name="loc_lint_v2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "quest_shard", "locales": ["ja"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-10", "report_uri": "artifact://bundle/bundle-ja-10"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["ja"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"ja": "artifact://bundle/bundle-ja-10"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_069",
        instruction=(
            "You must finalize PR 999 localization for de and fr: lint all changed keys at a 200px width budget, persist both bundles, open an in_review TMS job 'quest_shard' for de and fr, and annotate PR 999 with artifact://bundle/bundle-de-10 and artifact://bundle/bundle-fr-10. Return only 'pr_999'."
        ),
        actions=[
            Action(name="detect_changed_strings_v2", kwargs={"pr_number": 999}),
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "quest_shard", "locales": ["de", "fr"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-10", "report_uri": "artifact://bundle/bundle-de-10"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-10", "report_uri": "artifact://bundle/bundle-fr-10"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de", "fr"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"de": "artifact://bundle/bundle-de-10", "fr": "artifact://bundle/bundle-fr-10"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_070",
        instruction=(
            "You must ensure PR 999 localization meets policy across de, fr, and ja: deliver compliant localized assets using the detected changed keys within the 200px UI constraint, register review coverage for these locales, surface the produced artifacts on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="detect_changed_strings_v2", kwargs={"pr_number": 999}),
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "bundle-de-10+bundle-fr-10+bundle-ja-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-10", "report_uri": "artifact://bundle/bundle-de-10"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-10", "report_uri": "artifact://bundle/bundle-fr-10"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-10", "report_uri": "artifact://bundle/bundle-ja-10"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de", "fr", "ja"], "ui_px_limit": 200, "keys_count": 10, "bundle_uris": {"de": "artifact://bundle/bundle-de-10", "fr": "artifact://bundle/bundle-fr-10", "ja": "artifact://bundle/bundle-ja-10"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_071",
        instruction=(
            "You must bring PR 999 to a deterministic review‑ready state for hero intros in de and fr. You must ensure 'vo.hero.intro_01' (de) and 'vo.hero.intro_02' (fr) conform to the Localization/VO Protocol V2 under a 200‑pixel UI budget, validate subtitle timing for the mapped line‑ids, surface the exact produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["de", "fr"], "keys": ["vo.hero.intro_01", "vo.hero.intro_02"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["de", "fr"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "fr"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de","fr"], "line_ids": ["subtitle_002","subtitle_004"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "fr": "artifact://bundle/bundle-fr-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_072",
        instruction=(
            "You must bring PR 999 to a deterministic review‑ready state for hero intro line 2 across fr and en. You must ensure 'vo.hero.intro_02' conforms to policy for both locales under a 200‑pixel UI budget, validate the mapped subtitle timing, surface the exact produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["fr", "en"], "keys": ["vo.hero.intro_02"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "en", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "en", "keys": ["vo.hero.intro_02"]}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["fr", "en"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_001", "locale": "en"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "en", "keys": ["vo.hero.intro_02"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["fr", "en"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-en-1", "report_uri": "artifact://bundle/bundle-en-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["fr","en"], "line_ids": ["subtitle_004","subtitle_001"], "bundle_uris": {"fr": "artifact://bundle/bundle-fr-1", "en": "artifact://bundle/bundle-en-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_073",
        instruction=(
            "You must bring PR 999 to a deterministic review‑ready state for the villain threat line across ja and fr. You must ensure 'vo.villain.threat_01' conforms to policy for both locales under a 200‑pixel UI budget, validate the mapped subtitle timing, surface the exact produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["ja", "fr"], "keys": ["vo.villain.threat_01"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "fr", "keys": ["vo.villain.threat_01"]}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["ja", "fr"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["vo.villain.threat_01"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["ja", "fr"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["ja","fr"], "line_ids": ["subtitle_006","subtitle_004"], "bundle_uris": {"ja": "artifact://bundle/bundle-ja-1", "fr": "artifact://bundle/bundle-fr-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_074",
        instruction=(
            "You must bring PR 999 to a deterministic review‑ready state for the NPC quest line across de and es. You must ensure 'vo.npc.quest_01' conforms to policy for both locales under a 200‑pixel UI budget, validate the mapped subtitle timing, surface the exact produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["de", "es"], "keys": ["vo.npc.quest_01"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "de", "keys": ["vo.npc.quest_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["de", "es"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["vo.npc.quest_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "es"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-es-1", "report_uri": "artifact://bundle/bundle-es-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de","es"], "line_ids": ["subtitle_002","subtitle_008"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "es": "artifact://bundle/bundle-es-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_075",
        instruction=(
            "You must bring PR 999 to a deterministic review‑ready state for UI selection and NPC quest in zh and es. You must ensure 'vo.ui.menu_select' (zh) and 'vo.npc.quest_01' (es) conform to policy under a 200‑pixel UI budget, validate the mapped subtitle timing, surface the exact produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["zh", "es"], "keys": ["vo.ui.menu_select", "vo.npc.quest_01"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["zh", "es"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["zh", "es"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-zh-1", "report_uri": "artifact://bundle/bundle-zh-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-es-1", "report_uri": "artifact://bundle/bundle-es-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["zh","es"], "line_ids": ["subtitle_010","subtitle_008"], "bundle_uris": {"zh": "artifact://bundle/bundle-zh-1", "es": "artifact://bundle/bundle-es-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_076",
        instruction=(
            "You must bring PR 999 to a deterministic review‑ready state for hero intros across en, de, and fr. You must ensure 'vo.hero.intro_01' (en, de) and 'vo.hero.intro_02' (fr) conform to the Localization/VO Protocol V2 under a 200‑pixel UI budget, validate subtitle timing for the mapped line‑ids, surface the exact produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["en", "de", "fr"], "keys": ["vo.hero.intro_01", "vo.hero.intro_02"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["en", "de", "fr"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_001", "locale": "en"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["en", "de", "fr"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-en-1", "report_uri": "artifact://bundle/bundle-en-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["en","de","fr"], "line_ids": ["subtitle_001","subtitle_002","subtitle_004"], "bundle_uris": {"en": "artifact://bundle/bundle-en-1", "de": "artifact://bundle/bundle-de-1", "fr": "artifact://bundle/bundle-fr-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_077",
        instruction=(
            "You must bring PR 999 to a deterministic review‑ready state for 'vo.villain.threat_01' (en, ja) and 'vo.npc.quest_01' (es). You must conform to the Localization/VO Protocol V2 under a 200‑pixel UI budget, validate subtitle timing only for mapped line‑ids, surface the exact produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["en", "ja"], "keys": ["vo.villain.threat_01"], "glossary_lock": True}),
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["es"], "keys": ["vo.npc.quest_01"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "en", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "en", "keys": ["vo.villain.threat_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["ja", "es"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "en", "keys": ["vo.villain.threat_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["en", "ja", "es"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-en-1", "report_uri": "artifact://bundle/bundle-en-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-es-1", "report_uri": "artifact://bundle/bundle-es-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["en","ja","es"], "line_ids": ["subtitle_006","subtitle_008"], "bundle_uris": {"en": "artifact://bundle/bundle-en-1", "ja": "artifact://bundle/bundle-ja-1", "es": "artifact://bundle/bundle-es-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_078",
        instruction=(
            "You must bring PR 999 to a deterministic review‑ready state for hero intro 2 and the UI selection cue across fr and zh. You must ensure 'vo.hero.intro_02' (fr) and 'vo.ui.menu_select' (zh) conform to policy under a 200‑pixel UI budget, validate subtitle timing for the mapped line‑ids, surface the exact produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["fr", "zh"], "keys": ["vo.hero.intro_02", "vo.ui.menu_select"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"], "ui_px_limit": 200}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["fr", "zh"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["fr", "zh"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-zh-1", "report_uri": "artifact://bundle/bundle-zh-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["fr","zh"], "line_ids": ["subtitle_004","subtitle_010"], "bundle_uris": {"fr": "artifact://bundle/bundle-fr-1", "zh": "artifact://bundle/bundle-zh-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_079",
        instruction=(
            "You must bring PR 999 to a deterministic review‑ready state across en, de, and ja for hero and villain lines. You must ensure 'vo.hero.intro_01' (en, de) and 'vo.villain.threat_01' (ja) conform to policy under a 200‑pixel UI budget, validate subtitle timing for the mapped line‑ids, surface the exact produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["en", "de", "ja"], "keys": ["vo.hero.intro_01", "vo.villain.threat_01"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["en", "de", "ja"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_001", "locale": "en"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["en", "de", "ja"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-en-1", "report_uri": "artifact://bundle/bundle-en-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["en","de","ja"], "line_ids": ["subtitle_001","subtitle_002","subtitle_006"], "bundle_uris": {"en": "artifact://bundle/bundle-en-1", "de": "artifact://bundle/bundle-de-1", "ja": "artifact://bundle/bundle-ja-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_080",
        instruction=(
            "You must bring PR 999 to a deterministic review‑ready state across de, fr, ja, es, and zh for hero, villain, NPC, and UI lines. You must ensure the exact VO keys (de→'vo.hero.intro_01', fr→'vo.hero.intro_02', ja→'vo.villain.threat_01', es→'vo.npc.quest_01', zh→'vo.ui.menu_select') conform to policy under a 200‑pixel UI budget, validate subtitle timing for the mapped line‑ids, surface the exact produced bundle URIs on PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["de", "fr", "ja", "es", "zh"], "keys": ["vo.hero.intro_01", "vo.hero.intro_02", "vo.villain.threat_01", "vo.npc.quest_01", "vo.ui.menu_select"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"], "ui_px_limit": 200}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["de", "fr", "ja", "es", "zh"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "fr", "ja", "es", "zh"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-es-1", "report_uri": "artifact://bundle/bundle-es-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-zh-1", "report_uri": "artifact://bundle/bundle-zh-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de","fr","ja","es","zh"], "line_ids": ["subtitle_002","subtitle_004","subtitle_006","subtitle_008","subtitle_010"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "fr": "artifact://bundle/bundle-fr-1", "ja": "artifact://bundle/bundle-ja-1", "es": "artifact://bundle/bundle-es-1", "zh": "artifact://bundle/bundle-zh-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_081",
        instruction=(
            "You are the triage agent. Deduplicate the newly ingested ticket 'work_026' using the duplicate resolution protocol. Use severity High and the module path 'src/game/engine/renderer.cpp' to resolve ownership. Compute impact using the crash fingerprint 'renderer_character_load_access_violation_xyz' from the crash_events table. Update the ticket with owner team and triage state, record automation, and return only the canonical ticket id for 'work_026'."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026", "severity": "High", "module": "src/game/engine/renderer.cpp"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "work_026"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "work_026"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "work_026", "fingerprint": "renderer_character_load_access_violation_xyz"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "work_026"}),
            Action(name="lookup_relation_v2", kwargs={"ticket_key": "work_026"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "work_026", "fields": {"assignee": "team_001", "labels": ["auto-triage"], "state": "Triage", "canonical": "work_027"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_026"}, "outputs": {"canonical_bug_id": "work_027", "owner_team": "team_001"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "work_027"}),
        ],
        outputs=["work_027"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_082",
        instruction=(
            "You must apply the Bug Intake Protocol V2 to route 'work_029' for the module 'assets/models/environment/' with severity Medium. You must set assignee to the module owner, state to 'Triage', and label 'auto-triage'. Return only the canonical ticket id for 'work_029'."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_029", "severity": "Medium", "module": "assets/models/environment/"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "work_029"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "work_029"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "work_029"}),
            Action(name="find_ownership_path_v2", kwargs={"contains": "environment"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "assets/models/environment/"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "work_029"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "work_029", "fields": {"assignee": "team_002", "state": "Triage", "labels": ["auto-triage"], "canonical": "work_030"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_029"}, "outputs": {"canonical_bug_id": "work_030", "owner_team": "team_002"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "work_030"}),
        ],
        outputs=["work_030"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_083",
        instruction=(
            "You are handling 'bug_006' from gameplay UI. Resolve duplicates per policy and use UI ownership at 'src/game/ui/menu_system.cpp'. Keep severity High and compute impact without crash fingerprint. Persist owner assignment, set triage state, record the run, and return only the canonical ticket id for 'bug_006'."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_006", "severity": "High", "module": "src/game/ui/menu_system.cpp"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "bug_006"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "bug_006"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "bug_006"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "src/game/ui/menu_system.cpp"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "bug_006"}),
            Action(name="lookup_relation_v2", kwargs={"ticket_key": "bug_006"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "bug_006", "fields": {"assignee": "team_005", "state": "Triage", "labels": ["auto-triage"], "canonical": "bug_007"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_006"}, "outputs": {"canonical_bug_id": "bug_007", "owner_team": "team_005"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "bug_007"}),
        ],
        outputs=["bug_007"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_084",
        instruction=(
            "You must apply the Bug Intake Protocol V2 to 'bug_009' (module 'src/game/input/controller_handler.cpp', severity Medium). You must assign the ticket to the module owner, set state to 'Triage', add label 'auto-triage', and return only the canonical ticket id for 'bug_009'."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_009", "severity": "Medium", "module": "src/game/input/controller_handler.cpp"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "bug_009"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "bug_009"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "bug_009"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "src/game/input/controller_handler.cpp"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "bug_009"}),

            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "bug_009", "fields": {"assignee": "team_001", "state": "Triage", "labels": ["auto-triage"], "canonical": "bug_010"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_009"}, "outputs": {"canonical_bug_id": "bug_010", "owner_team": "team_001"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "bug_010"}),
        ],
        outputs=["bug_010"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_085",
        instruction=(
            "You must handle audio system duplicate intake for 'bug_intake_012'. Use audio ownership at 'assets/audio/sound_effects/'. Keep severity High, route to the audio team, and return only the canonical ticket id for 'bug_intake_012'."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_012", "severity": "High", "module": "assets/audio/sound_effects/"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "assets/audio/sound_effects/"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="lookup_relation_v2", kwargs={"ticket_key": "bug_intake_012"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "bug_intake_012", "fields": {"assignee": "team_004", "state": "Triage", "labels": ["auto-triage"], "canonical": "bug_intake_011"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_intake_012"}, "outputs": {"canonical_bug_id": "bug_intake_011", "owner_team": "team_004"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "bug_intake_011"}),
        ],
        outputs=["bug_intake_011"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_086",
        instruction=(
            "You must apply the Bug Intake Protocol V2 to 'bug_intake_016' (module 'src/game/network/multiplayer.cpp', severity Medium). You must compute impact using fingerprint 'network_connection_timeout_30s_xyz', assign to the owner team, set state 'Triage', add label 'auto-triage', and return only the canonical ticket id."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_016", "severity": "Medium", "module": "src/game/network/multiplayer.cpp"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "bug_intake_016"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "bug_intake_016"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "bug_intake_016", "fingerprint": "network_connection_timeout_30s_xyz"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "src/game/network/multiplayer.cpp"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "bug_intake_016"}),

            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "bug_intake_016", "fields": {"assignee": "team_003", "state": "Triage", "labels": ["auto-triage"], "canonical": "bug_intake_015"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_intake_016"}, "outputs": {"canonical_bug_id": "bug_intake_015", "owner_team": "team_003"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "bug_intake_015"}),
        ],
        outputs=["bug_intake_015"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_087",
        instruction=(
            "You must apply the Bug Intake Protocol V2 to 'bug_intake_020' (module 'src/game/engine/renderer.cpp', severity High). You must assign to the module owner, set state 'Triage', apply label 'auto-triage', and return only the canonical ticket id."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_020", "severity": "High", "module": "src/game/engine/renderer.cpp"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "bug_intake_020"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "bug_intake_020"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "bug_intake_020"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "bug_intake_020"}),

            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "bug_intake_020", "fields": {"assignee": "team_001", "state": "Triage", "labels": ["auto-triage"], "canonical": "bug_intake_019"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_intake_020"}, "outputs": {"canonical_bug_id": "bug_intake_019", "owner_team": "team_001"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "bug_intake_019"}),
        ],
        outputs=["bug_intake_019"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_088",
        instruction=(
            "You must apply the Bug Intake Protocol V2 to 'work_028' (module 'assets/textures/character_models/', severity Medium). You must assign to the module owner, set state to 'Triage', add label 'auto-triage', and return only the canonical ticket id for 'work_028'."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_028", "severity": "Medium", "module": "assets/textures/character_models/"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "work_028"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "work_028"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "work_028"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "assets/textures/character_models/"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "work_028"}),

            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "work_028", "fields": {"assignee": "team_002", "state": "Triage", "labels": ["auto-triage"], "canonical": "work_029"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "work_028"}, "outputs": {"canonical_bug_id": "work_029", "owner_team": "team_002"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "work_029"}),
        ],
        outputs=["work_029"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_089",
        instruction=(
            "You must apply the Bug Intake Protocol V2 to route 'bug_013' for the module 'assets/models/environment/' with severity Medium. You must assign to the module owner, set state 'Triage', apply label 'auto-triage', ensure duplicate resolution to the canonical record, and return only the canonical id for 'bug_013'."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_013", "severity": "Medium", "module": "assets/models/environment/"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "bug_013"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "bug_013"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "bug_013"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "assets/models/environment/"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "bug_013"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "bug_013", "fields": {"assignee": "team_002", "state": "Triage", "labels": ["auto-triage"], "canonical": "bug_014"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_013"}, "outputs": {"canonical_bug_id": "bug_014", "owner_team": "team_002"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "bug_014"}),
        ],
        outputs=["bug_014"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_090",
        instruction=(
            "You must process 'bug_016' and route based on 'src/game/physics/collision_detection.cpp' secondary ownership. Mark triage and return only the canonical id for 'bug_016'."
        ),
        actions=[
            Action(name="ingest_issue_webhook_v2", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_016", "severity": "Medium", "module": "src/game/physics/collision_detection.cpp"}}),
            Action(name="normalize_bug_v2", kwargs={"ticket_key": "bug_016"}),
            Action(name="summarize_bug_v2", kwargs={"ticket_key": "bug_016"}),
            Action(name="compute_impact_v2", kwargs={"ticket_key": "bug_016"}),
            Action(name="resolve_owner_v2", kwargs={"module_or_path": "src/game/physics/collision_detection.cpp"}),
            Action(name="find_canonical_duplicate_v2", kwargs={"ticket_key": "bug_016"}),
            Action(name="lookup_relation_v2", kwargs={"ticket_key": "bug_016"}),
            Action(name="update_bug_fields_v2", kwargs={"ticket_key": "bug_016", "fields": {"assignee": "team_001", "state": "Triage", "labels": ["auto-triage"], "canonical": "bug_017"}}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "bug-triage", "inputs": {"ticket_key": "bug_016"}, "outputs": {"canonical_bug_id": "bug_017", "owner_team": "team_001"}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "bug_017"}),
        ],
        outputs=["bug_017"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_091",
        instruction=(
            "You must complete a compact non‑English bundle pass for PR 999: enforce glossary lock, lint UI width, synthesize temp VO, validate timing for ('subtitle_002','de') and ('subtitle_006','ja'), persist bundles for 'vo.hero.intro_01' (de) and 'vo.villain.threat_01' (ja), create one in_review TMS job, annotate PR 999 with produced bundle URIs, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["de", "ja"], "keys": ["vo.hero.intro_01", "vo.villain.threat_01"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["de", "ja"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "ja"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de","ja"], "line_ids": ["subtitle_002","subtitle_006"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "ja": "artifact://bundle/bundle-ja-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_092",
        instruction=(
            "You must apply the Localization/VO Protocol V2 to PR 999 for fr and es. You must produce compliant review bundles for ('subtitle_004','fr')→'vo.hero.intro_02' and ('subtitle_008','es')→'vo.npc.quest_01' under a UI width budget of 200, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["fr", "es"], "keys": ["vo.hero.intro_02", "vo.npc.quest_01"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["fr", "es"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["fr", "es"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-es-1", "report_uri": "artifact://bundle/bundle-es-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["fr","es"], "line_ids": ["subtitle_004","subtitle_008"], "bundle_uris": {"fr": "artifact://bundle/bundle-fr-1", "es": "artifact://bundle/bundle-es-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_093",
        instruction=(
            "You must apply the Localization/VO Protocol V2 to PR 999 for zh and ja. You must produce compliant review bundles for ('subtitle_010','zh')→'vo.ui.menu_select' and ('subtitle_006','ja')→'vo.villain.threat_01' under a UI width budget of 200, and return only 'pr_999'."
        ),
        actions=[
            Action(name="loc_lint_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["zh", "ja"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["zh", "ja"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-zh-1", "report_uri": "artifact://bundle/bundle-zh-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["zh","ja"], "line_ids": ["subtitle_010","subtitle_006"], "bundle_uris": {"zh": "artifact://bundle/bundle-zh-1", "ja": "artifact://bundle/bundle-ja-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_094",
        instruction=(
            "You must apply the Localization/VO Protocol V2 to PR 999 for de and fr. You must produce compliant review bundles for ('subtitle_002','de')→'vo.hero.intro_01' and ('subtitle_004','fr')→'vo.hero.intro_02' under a UI width budget of 200, and return only 'pr_999'."
        ),
        actions=[
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["de", "fr"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "fr"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de","fr"], "line_ids": ["subtitle_002","subtitle_004"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "fr": "artifact://bundle/bundle-fr-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_095",
        instruction=(
            "You must apply the Localization/VO Protocol V2 to PR 999 for es and zh UI. You must produce compliant review bundles for ('subtitle_008','es')→'vo.npc.quest_01' and ('subtitle_010','zh')→'vo.ui.menu_select' under a UI width budget of 200, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["es", "zh"], "keys": ["vo.npc.quest_01", "vo.ui.menu_select"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"], "ui_px_limit": 200}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["es", "zh"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["es", "zh"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-es-1", "report_uri": "artifact://bundle/bundle-es-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-zh-1", "report_uri": "artifact://bundle/bundle-zh-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["es","zh"], "line_ids": ["subtitle_008","subtitle_010"], "bundle_uris": {"es": "artifact://bundle/bundle-es-1", "zh": "artifact://bundle/bundle-zh-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_096",
        instruction=(
            "You must apply the Localization/VO Protocol V2 to PR 999 for de and fr. You must produce compliant review bundles for ('subtitle_002','de')→'vo.hero.intro_01' and ('subtitle_004','fr')→'vo.hero.intro_02' under a UI width budget of 200, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["de", "fr"], "keys": ["vo.hero.intro_01", "vo.hero.intro_02"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["de", "fr"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "fr"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de","fr"], "line_ids": ["subtitle_002","subtitle_004"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "fr": "artifact://bundle/bundle-fr-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_097",
        instruction=(
            "You must apply the Localization/VO Protocol V2 to PR 999 for ja. You must produce a compliant review bundle for ('subtitle_006','ja')→'vo.villain.threat_01' under a UI width budget of 200, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["ja"], "keys": ["vo.villain.threat_01"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["ja"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["ja"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["ja"], "line_ids": ["subtitle_006"], "bundle_uris": {"ja": "artifact://bundle/bundle-ja-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_098",
        instruction=(
            "You must produce a zh+es UI compliance pass for PR 999 under the Localization/VO Protocol V2. You must generate compliant review bundles for ('subtitle_010','zh')→'vo.ui.menu_select' and ('subtitle_008','es')→'vo.npc.quest_01' under a UI width budget of 200, annotate PR 999, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["zh", "es"], "keys": ["vo.ui.menu_select", "vo.npc.quest_01"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"], "ui_px_limit": 200}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["zh", "es"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-zh-1", "report_uri": "artifact://bundle/bundle-zh-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-es-1", "report_uri": "artifact://bundle/bundle-es-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["zh","es"], "line_ids": ["subtitle_010","subtitle_008"], "bundle_uris": {"zh": "artifact://bundle/bundle-zh-1", "es": "artifact://bundle/bundle-es-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_099",
        instruction=(
            "You must apply the Localization/VO Protocol V2 to PR 999 for fr and ja. You must produce compliant review bundles for ('subtitle_004','fr')→'vo.hero.intro_02' and ('subtitle_006','ja')→'vo.villain.threat_01' under a UI width budget of 200, and return only 'pr_999'."
        ),
        actions=[
            Action(name="pretranslate_locked_glossary_v2", kwargs={"locales": ["fr", "ja"], "keys": ["vo.hero.intro_02", "vo.villain.threat_01"], "glossary_lock": True}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"], "ui_px_limit": 200}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["fr", "ja"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-ja-1", "report_uri": "artifact://bundle/bundle-ja-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["fr","ja"], "line_ids": ["subtitle_004","subtitle_006"], "bundle_uris": {"fr": "artifact://bundle/bundle-fr-1", "ja": "artifact://bundle/bundle-ja-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

    Task(
        annotator="0",
        user_id="v2_task_100",
        instruction=(
            "You must apply the Localization/VO Protocol V2 to PR 999 to produce a three‑locale confirmation for hero (de, fr) and UI (zh) keys. You must generate compliant review bundles for ('subtitle_002','de')→'vo.hero.intro_01', ('subtitle_004','fr')→'vo.hero.intro_02', and ('subtitle_010','zh')→'vo.ui.menu_select' under a UI width budget of 200, and return only 'pr_999'."
        ),
        actions=[
            Action(name="loc_lint_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"], "ui_px_limit": 200}),
            Action(name="loc_lint_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"], "ui_px_limit": 200}),
            Action(name="lookup_subtitle_ids_v2", kwargs={"locales": ["de", "fr", "zh"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="synthesize_temp_vo_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="validate_subtitle_timing_v2", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="write_locale_bundle_v2", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="create_tms_job_v2", kwargs={"bundle_name": "loc_pr_999", "locales": ["de", "fr", "zh"], "status": "in_review"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-de-1", "report_uri": "artifact://bundle/bundle-de-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-fr-1", "report_uri": "artifact://bundle/bundle-fr-1"}),
            Action(name="annotate_pr_with_qa_v2", kwargs={"pr_number": 999, "summary": "artifact://bundle/bundle-zh-1", "report_uri": "artifact://bundle/bundle-zh-1"}),
            Action(name="record_automation_run_v2", kwargs={"automation_type": "loc-shepherd", "inputs": {"pr_number": 999}, "outputs": {"locales": ["de","fr","zh"], "line_ids": ["subtitle_002","subtitle_004","subtitle_010"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "fr": "artifact://bundle/bundle-fr-1", "zh": "artifact://bundle/bundle-zh-1"}}, "status": "completed"}),
            Action(name="return_scalar_v2", kwargs={"value": "pr_999"}),
        ],
        outputs=["pr_999"],
    ),

]
