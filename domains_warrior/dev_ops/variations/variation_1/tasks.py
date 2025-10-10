from domains.dto import Task, Action


TASKS = [
    Task(
        annotator="0",
        user_id="task_001",
        instruction=(
            "You own CI triage for the game-engine pipeline. Resolve the failed Windows build run_001 on branch feature/new-renderer at commit abc123def456789 "
            "by applying the CI failure triage policy and deterministic templates end-to-end, and return the draft PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_001", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "build-windows-x64"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_001"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_001"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "abc123def456789"}),
            Action(name="run_bisect", kwargs={"run_id": "run_001", "suspects": [{"ref": "abc123def456789"}], "test_target": "build-windows-x64"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_001", "logs_uri": "artifact://logs/run_001", "first_bad_commit": "abc123def456789"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_001"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_001", "patch_id": "FP-run_001", "message": "auto tentative fix for run run_001"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_001", "base": "feature/new-renderer", "title": "auto fix build break run_001", "body": "summary for run run_001", "run_id": "run_001"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_001", "description": "Automated triage for run_001", "run_id": "run_001", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "build-windows-x64"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_001"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_002",
        instruction=(
            "You own CI triage for the game-engine pipeline. For failed run run_003 on branch feature/new-renderer at commit abc123def456789 (job test-unit-windows), "
            "apply the standard failure triage policy to persist context, extract signals, determine suspects from the commit’s changes, bisect, stage a template-based fix, "
            "open the draft PR and ticket via deterministic templates, validate, record, and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "test-unit-windows"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_003"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_003"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "abc123def456789"}),
            Action(name="run_bisect", kwargs={"run_id": "run_003", "suspects": [{"ref": "abc123def456789"}], "test_target": "test-unit-windows"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_003", "logs_uri": "artifact://logs/run_003", "first_bad_commit": "abc123def456789"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_003"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "message": "auto tentative fix for run run_003"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_003", "base": "feature/new-renderer", "title": "auto fix build break run_003", "body": "summary for run run_003", "run_id": "run_003"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "test-unit-windows"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_003",
        instruction=(
            "You own CI triage for the game-engine pipeline. For failed run run_005 on branch feature/new-renderer at commit def456abc123789 (job test-integration-linux), "
            "apply the triage policy with deterministic templates and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_005"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_005"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "def456abc123789"}),
            Action(name="run_bisect", kwargs={"run_id": "run_005", "suspects": [{"ref": "def456abc123789"}], "test_target": "test-integration-linux"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_005", "logs_uri": "artifact://logs/run_005", "first_bad_commit": "def456abc123789"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_005"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "message": "auto tentative fix for run run_005"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_005", "base": "feature/new-renderer", "title": "auto fix build break run_005", "body": "summary for run run_005", "run_id": "run_005"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "test-integration-linux"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_004",
        instruction=(
            "You own CI triage for the game-engine pipeline. For failed run run_007 on branch feature/new-renderer at commit abc123def456789 (job performance-test-windows), "
            "apply the triage policy with deterministic templates and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "performance-test-windows"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_007"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_007"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "abc123def456789"}),
            Action(name="run_bisect", kwargs={"run_id": "run_007", "suspects": [{"ref": "abc123def456789"}], "test_target": "performance-test-windows"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_007", "first_bad_commit": "abc123def456789"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_007"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "message": "auto tentative fix for run run_007"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_007", "base": "feature/new-renderer", "title": "auto fix build break run_007", "body": "summary for run run_007", "run_id": "run_007"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "performance-test-windows"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_005",
        instruction=(
            "You own CI triage for the game-engine pipeline. For failed run run_010 on branch feature/new-renderer at commit abc123def456789 (job deploy-staging-windows), "
            "apply the triage policy with deterministic templates and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_010", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "deploy-staging-windows"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_010"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_010"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "abc123def456789"}),
            Action(name="run_bisect", kwargs={"run_id": "run_010", "suspects": [{"ref": "abc123def456789"}], "test_target": "deploy-staging-windows"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_010", "first_bad_commit": "abc123def456789"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_010"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_010", "patch_id": "FP-run_010", "message": "auto tentative fix for run run_010"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_010", "base": "feature/new-renderer", "title": "auto fix build break run_010", "body": "summary for run run_010", "run_id": "run_010"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_010", "description": "Automated triage for run_010", "run_id": "run_010", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "deploy-staging-windows"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_010"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_006",
        instruction=(
            "You own CI triage for the game-engine pipeline. For new failed run run_011 on branch feature/new-renderer at commit abc123def456789 (job build-windows-x64), "
            "apply the triage policy with deterministic templates and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_011", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "build-windows-x64"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_011"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_011"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:abc123def456789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "abc123def456789"}),
            Action(name="run_bisect", kwargs={"run_id": "run_011", "suspects": [{"ref": "abc123def456789"}], "test_target": "build-windows-x64"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_011", "first_bad_commit": "abc123def456789"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_011"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_011", "patch_id": "FP-run_011", "message": "auto tentative fix for run run_011"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_011", "base": "feature/new-renderer", "title": "auto fix build break run_011", "body": "summary for run run_011", "run_id": "run_011"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_011", "description": "Automated triage for run_011", "run_id": "run_011", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "build-windows-x64"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_011"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_007",
        instruction=(
            "You own CI triage for the game-engine pipeline. For failed run run_012 on branch feature/new-renderer at commit def456abc123789 (job test-unit-windows), "
            "apply the triage policy with deterministic templates and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_012", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-unit-windows"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_012"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_012"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "def456abc123789"}),
            Action(name="run_bisect", kwargs={"run_id": "run_012", "suspects": [{"ref": "def456abc123789"}], "test_target": "test-unit-windows"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_012", "first_bad_commit": "def456abc123789"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_012"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_012", "patch_id": "FP-run_012", "message": "auto tentative fix for run run_012"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_012", "base": "feature/new-renderer", "title": "auto fix build break run_012", "body": "summary for run run_012", "run_id": "run_012"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_012", "description": "Automated triage for run_012", "run_id": "run_012", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "test-unit-windows"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_012"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_008",
        instruction=(
            "You own CI triage for the game-engine pipeline. For failed run run_013 on branch feature/new-renderer at commit def456abc123789 (job build-linux-x64), "
            "apply the triage policy with deterministic templates and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_013", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "build-linux-x64"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_013"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_013"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:def456abc123789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "def456abc123789"}),
            Action(name="run_bisect", kwargs={"run_id": "run_013", "suspects": [{"ref": "def456abc123789"}], "test_target": "build-linux-x64"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_013", "first_bad_commit": "def456abc123789"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_013"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_013", "patch_id": "FP-run_013", "message": "auto tentative fix for run run_013"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_013", "base": "feature/new-renderer", "title": "auto fix build break run_013", "body": "summary for run run_013", "run_id": "run_013"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_013", "description": "Automated triage for run_013", "run_id": "run_013", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "build-linux-x64"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_013"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_009",
        instruction=(
            "You own CI triage for the game-engine pipeline. For failed run run_014 on branch feature/new-renderer at commit ghi789def456abc (job build-macos-arm64), "
            "apply the triage policy with deterministic templates and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_014", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "ghi789def456abc", "job_name": "build-macos-arm64"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_014"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_014"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:ghi789def456abc:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "ghi789def456abc"}),
            Action(name="run_bisect", kwargs={"run_id": "run_014", "suspects": [{"ref": "ghi789def456abc"}], "test_target": "build-macos-arm64"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_014", "first_bad_commit": "ghi789def456abc"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/new-renderer", "run_id": "run_014"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_014", "patch_id": "FP-run_014", "message": "auto tentative fix for run run_014"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_014", "base": "feature/new-renderer", "title": "auto fix build break run_014", "body": "summary for run run_014", "run_id": "run_014"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_014", "description": "Automated triage for run_014", "run_id": "run_014", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "build-macos-arm64"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_014"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),


    Task(
        annotator="0",
        user_id="task_010",
        instruction=(
            "You own CI triage for the asset pipeline. For failed run run_006 on branch feature/new-assets at commit jkl012ghi789def (job validate-assets), "
            "apply the triage policy with deterministic templates and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_006", "status": "failure", "repo": "game-assets", "branch": "feature/new-assets", "commit_sha": "jkl012ghi789def", "job_name": "validate-assets"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_006"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_006"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:jkl012ghi789def:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "jkl012ghi789def"}),
            Action(name="run_bisect", kwargs={"run_id": "run_006", "suspects": [{"ref": "jkl012ghi789def"}], "test_target": "validate-assets"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_006", "first_bad_commit": "jkl012ghi789def"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/new-assets", "run_id": "run_006"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_006", "patch_id": "FP-run_006", "message": "auto tentative fix for run run_006"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_006", "base": "feature/new-assets", "title": "auto fix build break run_006", "body": "summary for run run_006", "run_id": "run_006"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_006", "description": "Automated triage for run_006", "run_id": "run_006", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "validate-assets"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_006"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_011",
        instruction=(
            "You own CI crash triage for the game-engine pipeline. For failed run run_015 on branch feature/physics-revamp at commit mno345jkl678pqr "
            "(job build-windows-x64), deterministically triage the failure per domain policy using only database-driven values: link to prior incidents when applicable, prepare a draft PR and linked ticket, validate, record the automation run, and return the PR number. Do not invent identifiers."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_015", "status": "failure", "repo": "game-engine", "branch": "feature/physics-revamp", "commit_sha": "mno345jkl678pqr", "job_name": "build-windows-x64"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_015"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_015"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:mno345jkl678pqr:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "mno345jkl678pqr"}),
            Action(name="run_bisect", kwargs={"run_id": "run_015", "suspects": [], "test_target": "build-windows-x64"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_015", "logs_uri": "artifact://logs/run_015", "first_bad_commit": "mno345jkl678pqr"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/physics-revamp", "run_id": "run_015"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_015", "patch_id": "FP-run_015", "message": "auto tentative fix for run run_015"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_015", "base": "feature/physics-revamp", "title": "auto fix build break run_015", "body": "summary for run run_015", "run_id": "run_015"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_015", "description": "Automated triage for run_015", "run_id": "run_015", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "build-windows-x64"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_015"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_012",
        instruction=(
            "You own CI crash triage for the game-engine pipeline. For failed run run_016 on branch feature/physics-revamp at commit mno345jkl678pqr "
            "(job test-unit-windows), execute deterministic crash symbolication and incident linking, open a draft PR and ticket, validate, record, and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_016", "status": "failure", "repo": "game-engine", "branch": "feature/physics-revamp", "commit_sha": "mno345jkl678pqr", "job_name": "test-unit-windows"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_016"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_016"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:mno345jkl678pqr:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "mno345jkl678pqr"}),
            Action(name="run_bisect", kwargs={"run_id": "run_016", "suspects": [{"ref": "mno345jkl678pqr"}], "test_target": "test-unit-windows"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_016", "logs_uri": "artifact://logs/run_016", "first_bad_commit": "mno345jkl678pqr"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/physics-revamp", "run_id": "run_016"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_016", "patch_id": "FP-run_016", "message": "auto tentative fix for run run_016"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_016", "base": "feature/physics-revamp", "title": "auto fix build break run_016", "body": "summary for run run_016", "run_id": "run_016"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_016", "description": "Automated triage for run_016", "run_id": "run_016", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "test-unit-windows"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_016"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_013",
        instruction=(
            "You own CI crash triage for the game-engine pipeline. For failed run run_017 on branch feature/ai-navigation at commit stu901vwx234yz0 "
            "(job test-integration-linux), perform deterministic symbolication and incident linking, produce a draft PR and linked ticket, validate, record, and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_017", "status": "failure", "repo": "game-engine", "branch": "feature/ai-navigation", "commit_sha": "stu901vwx234yz0", "job_name": "test-integration-linux"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_017"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_017"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:stu901vwx234yz0:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "stu901vwx234yz0"}),
            Action(name="run_bisect", kwargs={"run_id": "run_017", "suspects": [{"ref": "stu901vwx234yz0"}], "test_target": "test-integration-linux"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_017", "logs_uri": "artifact://logs/run_017", "first_bad_commit": "stu901vwx234yz0"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/ai-navigation", "run_id": "run_017"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_017", "patch_id": "FP-run_017", "message": "auto tentative fix for run run_017"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_017", "base": "feature/ai-navigation", "title": "auto fix build break run_017", "body": "summary for run run_017", "run_id": "run_017"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_017", "description": "Automated triage for run_017", "run_id": "run_017", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "test-integration-linux"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_017"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_014",
        instruction=(
            "You own CI crash triage for the game-engine pipeline. For failed run run_018 on branch feature/ai-navigation at commit stu901vwx234yz0 "
            "(job build-linux-x64), symbolicate and link incidents deterministically, create a draft PR and linked ticket, validate, record, and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_018", "status": "failure", "repo": "game-engine", "branch": "feature/ai-navigation", "commit_sha": "stu901vwx234yz0", "job_name": "build-linux-x64"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_018"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_018"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:stu901vwx234yz0:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "stu901vwx234yz0"}),
            Action(name="run_bisect", kwargs={"run_id": "run_018", "suspects": [{"ref": "stu901vwx234yz0"}], "test_target": "build-linux-x64"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_018", "logs_uri": "artifact://logs/run_018", "first_bad_commit": "stu901vwx234yz0"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/ai-navigation", "run_id": "run_018"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_018", "patch_id": "FP-run_018", "message": "auto tentative fix for run run_018"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_018", "base": "feature/ai-navigation", "title": "auto fix build break run_018", "body": "summary for run run_018", "run_id": "run_018"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_018", "description": "Automated triage for run_018", "run_id": "run_018", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "build-linux-x64"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_018"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_015",
        instruction=(
            "You own CI crash triage for the game-engine pipeline. For failed run run_019 on branch feature/render-optim at commit abc111def222ghi "
            "(job build-macos-arm64), symbolicate and link incidents deterministically, create a draft PR and linked ticket, validate, record, and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_019", "status": "failure", "repo": "game-engine", "branch": "feature/render-optim", "commit_sha": "abc111def222ghi", "job_name": "build-macos-arm64"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_019"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_019"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:abc111def222ghi:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "abc111def222ghi"}),
            Action(name="run_bisect", kwargs={"run_id": "run_019", "suspects": [{"ref": "abc111def222ghi"}], "test_target": "build-macos-arm64"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_019", "logs_uri": "artifact://logs/run_019", "first_bad_commit": "abc111def222ghi"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/render-optim", "run_id": "run_019"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_019", "patch_id": "FP-run_019", "message": "auto tentative fix for run run_019"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_019", "base": "feature/render-optim", "title": "auto fix build break run_019", "body": "summary for run run_019", "run_id": "run_019"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_019", "description": "Automated triage for run_019", "run_id": "run_019", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "build-macos-arm64"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_019"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_016",
        instruction=(
            "You own CI crash triage for the game-engine pipeline. For failed run run_020 on branch feature/render-optim at commit abc111def222ghi "
            "(job test-unit-windows), symbolicate and link incidents deterministically, create a draft PR and linked ticket, validate, record, and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_020", "status": "failure", "repo": "game-engine", "branch": "feature/render-optim", "commit_sha": "abc111def222ghi", "job_name": "test-unit-windows"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_020"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_020"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:abc111def222ghi:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "abc111def222ghi"}),
            Action(name="run_bisect", kwargs={"run_id": "run_020", "suspects": [{"ref": "abc111def222ghi"}], "test_target": "test-unit-windows"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_020", "logs_uri": "artifact://logs/run_020", "first_bad_commit": "abc111def222ghi"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/render-optim", "run_id": "run_020"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_020", "patch_id": "FP-run_020", "message": "auto tentative fix for run run_020"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_020", "base": "feature/render-optim", "title": "auto fix build break run_020", "body": "summary for run run_020", "run_id": "run_020"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_020", "description": "Automated triage for run_020", "run_id": "run_020", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "test-unit-windows"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_020"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_017",
        instruction=(
            "You own CI crash triage for the game-engine pipeline. For failed run run_021 on branch feature/netcode at commit zyx987wvu654tsr "
            "(job performance-test-windows), symbolicate and link incidents deterministically, create a draft PR and linked ticket, validate, record, and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_021", "status": "failure", "repo": "game-engine", "branch": "feature/netcode", "commit_sha": "zyx987wvu654tsr", "job_name": "performance-test-windows"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_021"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_021"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:zyx987wvu654tsr:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "zyx987wvu654tsr"}),
            Action(name="run_bisect", kwargs={"run_id": "run_021", "suspects": [{"ref": "zyx987wvu654tsr"}], "test_target": "performance-test-windows"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_021", "logs_uri": "artifact://logs/run_021", "first_bad_commit": "zyx987wvu654tsr"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/netcode", "run_id": "run_021"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_021", "patch_id": "FP-run_021", "message": "auto tentative fix for run run_021"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_021", "base": "feature/netcode", "title": "auto fix build break run_021", "body": "summary for run run_021", "run_id": "run_021"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_021", "description": "Automated triage for run_021", "run_id": "run_021", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "performance-test-windows"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_021"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_018",
        instruction=(
            "You own CI crash triage for the game-engine pipeline. For failed run run_022 on branch feature/netcode at commit zyx987wvu654tsr "
            "(job deploy-staging-windows), symbolicate and link incidents deterministically, create a draft PR and linked ticket, validate, record, and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_022", "status": "failure", "repo": "game-engine", "branch": "feature/netcode", "commit_sha": "zyx987wvu654tsr", "job_name": "deploy-staging-windows"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_022"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_022"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:zyx987wvu654tsr:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "zyx987wvu654tsr"}),
            Action(name="run_bisect", kwargs={"run_id": "run_022", "suspects": [{"ref": "zyx987wvu654tsr"}], "test_target": "deploy-staging-windows"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_022", "logs_uri": "artifact://logs/run_022", "first_bad_commit": "zyx987wvu654tsr"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/netcode", "run_id": "run_022"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_022", "patch_id": "FP-run_022", "message": "auto tentative fix for run run_022"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_022", "base": "feature/netcode", "title": "auto fix build break run_022", "body": "summary for run run_022", "run_id": "run_022"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_022", "description": "Automated triage for run_022", "run_id": "run_022", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "deploy-staging-windows"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_022"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_019",
        instruction=(
            "You own CI crash triage for the asset pipeline. For failed run run_023 on branch feature/vehicle-assets at commit lm123no456pq789 "
            "(job validate-assets), symbolicate and link incidents deterministically, create a draft PR and linked ticket, validate, record, and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_023", "status": "failure", "repo": "game-assets", "branch": "feature/vehicle-assets", "commit_sha": "lm123no456pq789", "job_name": "validate-assets"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_023"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_023"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:lm123no456pq789:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "lm123no456pq789"}),
            Action(name="run_bisect", kwargs={"run_id": "run_023", "suspects": [{"ref": "lm123no456pq789"}], "test_target": "validate-assets"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_023", "logs_uri": "artifact://logs/run_023", "first_bad_commit": "lm123no456pq789"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/vehicle-assets", "run_id": "run_023"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_023", "patch_id": "FP-run_023", "message": "auto tentative fix for run run_023"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_023", "base": "feature/vehicle-assets", "title": "auto fix build break run_023", "body": "summary for run run_023", "run_id": "run_023"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_023", "description": "Automated triage for run_023", "run_id": "run_023", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "validate-assets"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_023"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_020",
        instruction=(
            "You own CI crash triage for the game-engine pipeline. For failed run run_024 on branch feature/houdini-tools at commit pqrs111tuv222wxy "
            "(job build-windows-x64), symbolicate and link incidents deterministically, create a draft PR and linked ticket, validate, record, and return the PR number."
        ),
        actions=[
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_024", "status": "failure", "repo": "game-engine", "branch": "feature/houdini-tools", "commit_sha": "pqrs111tuv222wxy", "job_name": "build-windows-x64"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_024"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_024"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:pqrs111tuv222wxy:first_failure", "top_k": 5}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "pqrs111tuv222wxy"}),
            Action(name="run_bisect", kwargs={"run_id": "run_024", "suspects": [{"ref": "pqrs111tuv222wxy"}], "test_target": "build-windows-x64"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_024", "logs_uri": "artifact://logs/run_024", "first_bad_commit": "pqrs111tuv222wxy"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "feature/houdini-tools", "run_id": "run_024"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_024", "patch_id": "FP-run_024", "message": "auto tentative fix for run run_024"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_024", "base": "feature/houdini-tools", "title": "auto fix build break run_024", "body": "summary for run run_024", "run_id": "run_024"}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENG", "summary": "CI failure run_024", "description": "Automated triage for run_024", "run_id": "run_024", "pr_number": 33}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "build-windows-x64"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-triage", "inputs": {"run_id": "run_024"}, "outputs": {"pr_number": 33, "ticket_key": "ENG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_021",
        instruction=(
            "You own asset QA validation for asset asset_001 at catalog checksum sha256:a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456. "
            "Apply the standard intake QA policy in scene TestBudget to evaluate assets/textures/characters/hero_character_diffuse.png, then surface the result on a draft QA PR "
            "created for this checkpoint using summary 'errors 0 warnings 0' and the required status. Return the PR number 33."
        ),
        actions=[
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_001"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/textures/characters/hero_character_diffuse.png"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/textures/characters/hero_character_diffuse.png"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/textures/characters/hero_character_diffuse.png"], "scene": "TestBudget"}),
            Action(
                name="upload_qa_reports",
                kwargs={
                    "qa_json": [{"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []}],
                    "tex_report": [{"file": "assets/textures/characters/hero_character_diffuse.png"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/textures/characters/hero_character_diffuse.png"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_001"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(
                name="persist_asset_qa_results",
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
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_001"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_001-sha256:a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"},
                    "status": "completed",
                },
            ),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_022",
        instruction=(
            "You own asset QA validation for asset asset_002 at catalog checksum sha256:b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890. "
            "Apply the standard intake QA policy in scene TestBudget to evaluate assets/models/characters/hero_character.fbx, then surface the result on a draft QA PR "
            "created for this checkpoint using summary 'errors 0 warnings 0' and the required status. Return the PR number 33."
        ),
        actions=[
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_002"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/models/characters/hero_character.fbx"], "scene": "TestBudget"}),
            Action(
                name="upload_qa_reports",
                kwargs={
                    "qa_json": [{"file": "assets/models/characters/hero_character.fbx", "issues": []}],
                    "tex_report": [{"file": "assets/models/characters/hero_character.fbx"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/models/characters/hero_character.fbx"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_002"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="persist_asset_qa_results",
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
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_002"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_002-sha256:b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890"},
                    "status": "completed",
                },
            ),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_023",
        instruction=(
            "You own asset QA validation for asset asset_003 at catalog checksum sha256:c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcd. "
            "Apply the standard intake QA policy in scene TestBudget to evaluate assets/textures/characters/hero_character_normal.png, then surface the result on a draft QA PR "
            "created for this checkpoint using summary 'errors 0 warnings 0' and the required status. Return the PR number 33."
        ),
        actions=[
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_003"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/textures/characters/hero_character_normal.png"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/textures/characters/hero_character_normal.png"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/textures/characters/hero_character_normal.png"], "scene": "TestBudget"}),
            Action(
                name="upload_qa_reports",
                kwargs={
                    "qa_json": [{"file": "assets/textures/characters/hero_character_normal.png", "issues": []}],
                    "tex_report": [{"file": "assets/textures/characters/hero_character_normal.png"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/textures/characters/hero_character_normal.png"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_003"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="persist_asset_qa_results",
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
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_003"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_003-sha256:c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcd"},
                    "status": "completed",
                },
            ),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_024",
        instruction=(
            "You own asset QA validation for asset asset_004 at catalog checksum sha256:d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef. "
            "Apply the standard intake QA policy in scene TestBudget to evaluate assets/animations/characters/hero_idle.fbx, then reflect the outcome on the QA PR "
            "using summary 'errors 0 warnings 0' and mark the Asset QA check as success. Return the PR number 33."
        ),
        actions=[
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_004"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"], "scene": "TestBudget"}),
            Action(
                name="upload_qa_reports",
                kwargs={
                    "qa_json": [{"file": "assets/animations/characters/hero_idle.fbx", "issues": []}],
                    "tex_report": [{"file": "assets/animations/characters/hero_idle.fbx"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/animations/characters/hero_idle.fbx"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_004"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="persist_asset_qa_results",
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
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_004"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_004-sha256:d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef"},
                    "status": "completed",
                },
            ),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_025",
        instruction=(
            "You own asset QA validation for asset asset_005 at catalog checksum sha256:e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef12. "
            "Apply the standard intake QA policy in scene TestBudget to evaluate assets/models/environment/castle_tower.fbx, then reflect the outcome on the QA PR "
            "using summary 'errors 0 warnings 0' and mark the Asset QA check as success. Return the PR number 33."
        ),
        actions=[
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_005"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/models/environment/castle_tower.fbx"], "scene": "TestBudget"}),
            Action(
                name="upload_qa_reports",
                kwargs={
                    "qa_json": [{"file": "assets/models/environment/castle_tower.fbx", "issues": []}],
                    "tex_report": [{"file": "assets/models/environment/castle_tower.fbx"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/models/environment/castle_tower.fbx"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_005"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(
                name="persist_asset_qa_results",
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
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_005"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_005-sha256:e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef12"},
                    "status": "completed",
                },
            ),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),


    Task(
        annotator="0",
        user_id="task_026",
        instruction=(
            "You own asset QA validation for asset asset_006 at catalog checksum sha256:f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef1234. "
            "Apply the standard intake QA policy in scene TestBudget to evaluate assets/textures/environment/castle_tower_diffuse.png, then surface the result on a draft QA PR "
            "created for this checkpoint using summary 'errors 0 warnings 0' and the required status. Return the PR number 33."
        ),
        actions=[
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_006"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png"], "scene": "TestBudget"}),
            Action(
                name="upload_qa_reports",
                kwargs={
                    "qa_json": [{"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []}],
                    "tex_report": [{"file": "assets/textures/environment/castle_tower_diffuse.png"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/textures/environment/castle_tower_diffuse.png"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_006"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="persist_asset_qa_results",
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
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_006"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_006-sha256:f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef1234"},
                    "status": "completed",
                },
            ),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),


    Task(
        annotator="0",
        user_id="task_027",
        instruction=(
            "You own asset QA validation for asset asset_007 at catalog checksum sha256:789012345678901234567890abcdef1234567890abcdef1234567890abcdef123456. "
            "Apply the standard intake QA policy in scene TestBudget to evaluate assets/textures/environment/castle_tower_normal.png, then surface the result on a draft QA PR "
            "created for this checkpoint using summary 'errors 0 warnings 0' and the required status. Return the PR number 33."
        ),
        actions=[
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_007"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png"], "scene": "TestBudget"}),
            Action(
                name="upload_qa_reports",
                kwargs={
                    "qa_json": [{"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}],
                    "tex_report": [{"file": "assets/textures/environment/castle_tower_normal.png"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/textures/environment/castle_tower_normal.png"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_007"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="persist_asset_qa_results",
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
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_007"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_007-sha256:789012345678901234567890abcdef1234567890abcdef1234567890abcdef123456"},
                    "status": "completed",
                },
            ),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_028",
        instruction=(
            "You own asset QA validation for asset asset_008 at catalog checksum sha256:89012345678901234567890abcdef1234567890abcdef1234567890abcdef1234567. "
            "Apply the standard intake QA policy in scene TestBudget to evaluate assets/materials/environment/castle_tower.mtl, then surface the result on a draft QA PR "
            "created for this checkpoint using summary 'errors 0 warnings 0' and the required status. Return the PR number 33."
        ),
        actions=[
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_008"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"], "scene": "TestBudget"}),
            Action(
                name="upload_qa_reports",
                kwargs={
                    "qa_json": [{"file": "assets/materials/environment/castle_tower.mtl", "issues": []}],
                    "tex_report": [{"file": "assets/materials/environment/castle_tower.mtl"}],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/materials/environment/castle_tower.mtl"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": ["artifact://still/AR-1-1"]},
                },
            ),
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_008"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/qa-AR-1", "base": "main", "title": "asset-qa AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="persist_asset_qa_results",
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
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_008"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_008-sha256:89012345678901234567890abcdef1234567890abcdef1234567890abcdef1234567"},
                    "status": "completed",
                },
            ),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),


    Task(
        annotator="0",
        user_id="task_029",
        instruction=(
            "You own asset QA validation for asset asset_009 at catalog checksum sha256:9012345678901234567890abcdef1234567890abcdef1234567890abcdef12345678. "
            "Apply the standard intake QA policy in scene TestBudget to evaluate assets/audio/sfx/hero_sword_swing.wav, then reflect the outcome on the QA PR "
            "using summary 'errors 0 warnings 0' and mark the Asset QA check as success. Return the PR number 33."
        ),
        actions=[
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_009"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav"], "scene": "TestBudget"}),
            Action(
                name="upload_qa_reports",
                kwargs={
                    "qa_json": [{"file": "assets/audio/sfx/hero_sword_swing.wav", "issues": []}],
                    "tex_report": [],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/audio/sfx/hero_sword_swing.wav"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": []},
                },
            ),
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_009"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/qa-AR-2", "base": "main", "title": "asset-qa AR-2", "body": "qa AR-2", "run_id": "AR-2"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="persist_asset_qa_results",
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
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_009"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_009-sha256:9012345678901234567890abcdef1234567890abcdef1234567890abcdef12345678"},
                    "status": "completed",
                },
            ),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_030",
        instruction=(
            "You own asset QA validation for asset asset_010 at catalog checksum sha256:012345678901234567890abcdef1234567890abcdef1234567890abcdef123456789. "
            "Apply the standard intake QA policy in scene TestBudget to evaluate assets/audio/music/main_theme.ogg, then reflect the outcome on the QA PR "
            "using summary 'errors 0 warnings 0' and mark the Asset QA check as success. Return the PR number 33."
        ),
        actions=[
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_010"},
                    "outputs": {},
                    "status": "started",
                },
            ),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/audio/music/main_theme.ogg"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/audio/music/main_theme.ogg"], "scene": "TestBudget"}),
            Action(
                name="upload_qa_reports",
                kwargs={
                    "qa_json": [{"file": "assets/audio/music/main_theme.ogg", "issues": []}],
                    "tex_report": [],
                    "engine_report": {"scene": "TestBudget", "files": ["assets/audio/music/main_theme.ogg"], "violations": []},
                    "previews": {"turntable_uri": "artifact://turntable/AR-1", "stills_uris": []},
                },
            ),
            Action(
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_010"},
                    "outputs": {},
                    "status": "reports_uploaded",
                },
            ),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/qa-AR-2", "base": "main", "title": "asset-qa AR-2", "body": "qa AR-2", "run_id": "AR-2"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/summary"}),
            Action(
                name="persist_asset_qa_results",
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
                name="record_automation_run",
                kwargs={
                    "automation_type": "asset-qa",
                    "inputs": {"asset_id": "asset_010"},
                    "outputs": {"pr_number": 33, "qa_id": "QA-asset_010-sha256:012345678901234567890abcdef1234567890abcdef1234567890abcdef123456789"},
                    "status": "completed",
                },
            ),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="task_031",
        instruction=(
            "You own deterministic asset auto-remediation for asset asset_001 at catalog checksum sha256:a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456. "
            "Use the TestBudget scene to evaluate assets/textures/characters/hero_character_diffuse.png, then surface the outcome on the draft PR for this checkpoint, "
            "mark the Asset QA check as success, persist results keyed to the catalog checksum, and return PR number 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_001"}, "outputs": {}, "status": "started"}),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/textures/characters/hero_character_diffuse.png"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/textures/characters/hero_character_diffuse.png"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/textures/characters/hero_character_diffuse.png"], "scene": "TestBudget"}),
            Action(name="apply_asset_autofixes", kwargs={"qa_json": [{"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []}], "tex_report": [{"file": "assets/textures/characters/hero_character_diffuse.png"}]}),
            Action(name="render_asset_previews", kwargs={"files": ["assets/textures/characters/hero_character_diffuse.png"]}),
            Action(name="upload_qa_reports", kwargs={"qa_json": [{"file": "assets/textures/characters/hero_character_diffuse.png", "issues": []}], "tex_report": [{"file": "assets/textures/characters/hero_character_diffuse.png"}], "engine_report": {"scene": "TestBudget", "files": ["assets/textures/characters/hero_character_diffuse.png"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_001"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="persist_asset_qa_results", kwargs={"asset_id": "asset_001", "commit_sha": "sha256:a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_001"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_001-sha256:a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_032",
        instruction=(
            "You own deterministic asset auto-remediation for asset asset_002 at catalog checksum sha256:b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890. "
            "Use the TestBudget scene to evaluate assets/models/characters/hero_character.fbx, then surface the outcome on the draft PR for this checkpoint, set the Asset QA check to success, "
            "persist results keyed to the catalog checksum, and return PR number 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_002"}, "outputs": {}, "status": "started"}),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/models/characters/hero_character.fbx"], "scene": "TestBudget"}),
            Action(name="apply_asset_autofixes", kwargs={"qa_json": [{"file": "assets/models/characters/hero_character.fbx", "issues": []}], "tex_report": [{"file": "assets/models/characters/hero_character.fbx"}]}),
            Action(name="render_asset_previews", kwargs={"files": ["assets/models/characters/hero_character.fbx"]}),
            Action(name="upload_qa_reports", kwargs={"qa_json": [{"file": "assets/models/characters/hero_character.fbx", "issues": []}], "tex_report": [{"file": "assets/models/characters/hero_character.fbx"}], "engine_report": {"scene": "TestBudget", "files": ["assets/models/characters/hero_character.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_002"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="persist_asset_qa_results", kwargs={"asset_id": "asset_002", "commit_sha": "sha256:b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_002"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_002-sha256:b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_033",
        instruction=(
            "You own intake QA for asset asset_003 at catalog checksum sha256:c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcd. "
            "Evaluation context: TestBudget. Ensure the appropriate draft QA PR for this checkpoint reflects the outcome with the required status, "
            "persist the result keyed to the catalog checksum, and return PR number 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_003"}, "outputs": {}, "status": "started"}),
            Action(name="get_asset_files", kwargs={"asset_id": "asset_003"}),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/textures/characters/hero_character_normal.png"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/textures/characters/hero_character_normal.png"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/textures/characters/hero_character_normal.png"], "scene": "TestBudget"}),
            Action(name="render_asset_previews", kwargs={"files": ["assets/textures/characters/hero_character_normal.png"]}),
            Action(name="upload_qa_reports", kwargs={"qa_json": [{"file": "assets/textures/characters/hero_character_normal.png", "issues": []}], "tex_report": [{"file": "assets/textures/characters/hero_character_normal.png"}], "engine_report": {"scene": "TestBudget", "files": ["assets/textures/characters/hero_character_normal.png"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_003"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="persist_asset_qa_results", kwargs={"asset_id": "asset_003", "commit_sha": "sha256:c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcd", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_003"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_003-sha256:c3d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcd"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_034",
        instruction=(
            "You are responsible for deterministic asset auto-remediation for asset asset_004 (catalog checksum sha256:d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef). "
            "Within the TestBudget evaluation context and using only database-derived values, ensure the appropriate draft PR accurately reflects the outcome with the correct status, "
            "persist the result keyed to the checksum, maintain a complete automation audit trail, and return PR number 33. Do not invent identifiers."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_004"}, "outputs": {}, "status": "started"}),
            Action(name="get_asset_files", kwargs={"asset_id": "asset_004"}),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"], "scene": "TestBudget"}),
            Action(name="render_asset_previews", kwargs={"files": ["assets/animations/characters/hero_idle.fbx"]}),
            Action(name="upload_qa_reports", kwargs={"qa_json": [{"file": "assets/animations/characters/hero_idle.fbx", "issues": []}], "tex_report": [{"file": "assets/animations/characters/hero_idle.fbx"}], "engine_report": {"scene": "TestBudget", "files": ["assets/animations/characters/hero_idle.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_004"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="persist_asset_qa_results", kwargs={"asset_id": "asset_004", "commit_sha": "sha256:d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_004"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_004-sha256:d4e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_035",
        instruction=(
            "You are responsible for mechanical asset remediation for asset asset_005 at catalog checksum sha256:e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef12. "
            "Apply the standard auto-remediation policy in scene TestBudget for assets/models/environment/castle_tower.fbx, reflect the outcome on a draft QA PR with the required status, "
            "persist results keyed to the catalog checksum, and return PR number 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_005"}, "outputs": {}, "status": "started"}),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/models/environment/castle_tower.fbx"], "scene": "TestBudget"}),
            Action(name="apply_asset_autofixes", kwargs={"qa_json": [{"file": "assets/models/environment/castle_tower.fbx", "issues": []}], "tex_report": [{"file": "assets/models/environment/castle_tower.fbx"}]}),
            Action(name="render_asset_previews", kwargs={"files": ["assets/models/environment/castle_tower.fbx"]}),
            Action(name="upload_qa_reports", kwargs={"qa_json": [{"file": "assets/models/environment/castle_tower.fbx", "issues": []}], "tex_report": [{"file": "assets/models/environment/castle_tower.fbx"}], "engine_report": {"scene": "TestBudget", "files": ["assets/models/environment/castle_tower.fbx"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_005"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="persist_asset_qa_results", kwargs={"asset_id": "asset_005", "commit_sha": "sha256:e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef12", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_005"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_005-sha256:e5f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef12"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_036",
        instruction=(
            "You are responsible for mechanical asset remediation for asset asset_006 at catalog checksum sha256:f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef1234. "
            "Apply the standard auto-remediation policy in scene TestBudget for assets/textures/environment/castle_tower_diffuse.png, reflect the outcome on a draft QA PR with the required status, "
            "persist results keyed to the catalog checksum, and return PR number 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_006"}, "outputs": {}, "status": "started"}),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png"], "scene": "TestBudget"}),
            Action(name="apply_asset_autofixes", kwargs={"qa_json": [{"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []}], "tex_report": [{"file": "assets/textures/environment/castle_tower_diffuse.png"}]}),
            Action(name="render_asset_previews", kwargs={"files": ["assets/textures/environment/castle_tower_diffuse.png"]}),
            Action(name="upload_qa_reports", kwargs={"qa_json": [{"file": "assets/textures/environment/castle_tower_diffuse.png", "issues": []}], "tex_report": [{"file": "assets/textures/environment/castle_tower_diffuse.png"}], "engine_report": {"scene": "TestBudget", "files": ["assets/textures/environment/castle_tower_diffuse.png"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_006"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="persist_asset_qa_results", kwargs={"asset_id": "asset_006", "commit_sha": "sha256:f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef1234", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_006"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_006-sha256:f6789012345678901234567890abcdef1234567890abcdef1234567890abcdef1234"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_037",
        instruction=(
            "You own deterministic asset auto-remediation for asset asset_007 at catalog checksum sha256:789012345678901234567890abcdef1234567890abcdef1234567890abcdef123456. "
            "Use the TestBudget scene to evaluate assets/textures/environment/castle_tower_normal.png, then surface the outcome on the draft PR for this checkpoint, set the Asset QA check to success, "
            "persist results keyed to the catalog checksum, and return PR number 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_007"}, "outputs": {}, "status": "started"}),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png"], "scene": "TestBudget"}),
            Action(name="apply_asset_autofixes", kwargs={"qa_json": [{"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}], "tex_report": [{"file": "assets/textures/environment/castle_tower_normal.png"}]}),
            Action(name="render_asset_previews", kwargs={"files": ["assets/textures/environment/castle_tower_normal.png"]}),
            Action(name="upload_qa_reports", kwargs={"qa_json": [{"file": "assets/textures/environment/castle_tower_normal.png", "issues": []}], "tex_report": [{"file": "assets/textures/environment/castle_tower_normal.png"}], "engine_report": {"scene": "TestBudget", "files": ["assets/textures/environment/castle_tower_normal.png"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_007"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="persist_asset_qa_results", kwargs={"asset_id": "asset_007", "commit_sha": "sha256:789012345678901234567890abcdef1234567890abcdef1234567890abcdef123456", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_007"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_007-sha256:789012345678901234567890abcdef1234567890abcdef1234567890abcdef123456"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_038",
        instruction=(
            "You own deterministic asset auto-remediation for asset asset_008 at catalog checksum sha256:89012345678901234567890abcdef1234567890abcdef1234567890abcdef1234567. "
            "Use the TestBudget scene to evaluate assets/materials/environment/castle_tower.mtl, then surface the outcome on the draft PR for this checkpoint, set the Asset QA check to success, "
            "persist results keyed to the catalog checksum, and return PR number 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_008"}, "outputs": {}, "status": "started"}),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="validate_textures", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"], "scene": "TestBudget"}),
            Action(name="apply_asset_autofixes", kwargs={"qa_json": [{"file": "assets/materials/environment/castle_tower.mtl", "issues": []}], "tex_report": [{"file": "assets/materials/environment/castle_tower.mtl"}]}),
            Action(name="open_auto_branch", kwargs={"base_ref": "main", "run_id": "AR-1"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-AR-1", "patch_id": "AF-1", "message": "auto tentative fix for run AR-1"}),
            Action(name="render_asset_previews", kwargs={"files": ["assets/materials/environment/castle_tower.mtl"]}),
            Action(name="upload_qa_reports", kwargs={"qa_json": [{"file": "assets/materials/environment/castle_tower.mtl", "issues": []}], "tex_report": [{"file": "assets/materials/environment/castle_tower.mtl"}], "engine_report": {"scene": "TestBudget", "files": ["assets/materials/environment/castle_tower.mtl"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_008"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="persist_asset_qa_results", kwargs={"asset_id": "asset_008", "commit_sha": "sha256:89012345678901234567890abcdef1234567890abcdef1234567890abcdef1234567", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_008"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_008-sha256:89012345678901234567890abcdef1234567890abcdef1234567890abcdef1234567"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_039",
        instruction=(
            "You own intake QA for asset asset_009 at catalog checksum sha256:9012345678901234567890abcdef1234567890abcdef1234567890abcdef12345678. "
            "Evaluation context: TestBudget. Ensure the appropriate draft QA PR for this checkpoint reflects the outcome with the required status, "
            "persist the result keyed to the catalog checksum, and return PR number 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_009"}, "outputs": {}, "status": "started"}),
            Action(name="get_asset_files", kwargs={"asset_id": "asset_009"}),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav"], "scene": "TestBudget"}),
            Action(name="apply_asset_autofixes", kwargs={"qa_json": [{"file": "assets/audio/sfx/hero_sword_swing.wav", "issues": []}], "tex_report": []}),
            Action(name="open_auto_branch", kwargs={"base_ref": "main", "run_id": "AR-1"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-AR-1", "patch_id": "AF-1", "message": "auto tentative fix for run AR-1"}),
            Action(name="render_asset_previews", kwargs={"files": ["assets/audio/sfx/hero_sword_swing.wav"]}),
            Action(name="upload_qa_reports", kwargs={"qa_json": [{"file": "assets/audio/sfx/hero_sword_swing.wav", "issues": []}], "tex_report": [], "engine_report": {"scene": "TestBudget", "files": ["assets/audio/sfx/hero_sword_swing.wav"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_009"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="persist_asset_qa_results", kwargs={"asset_id": "asset_009", "commit_sha": "sha256:9012345678901234567890abcdef1234567890abcdef1234567890abcdef12345678", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_009"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_009-sha256:9012345678901234567890abcdef1234567890abcdef1234567890abcdef12345678"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_040",
        instruction=(
            "You own intake QA for asset asset_010 at catalog checksum sha256:012345678901234567890abcdef1234567890abcdef1234567890abcdef123456789. "
            "Evaluation context: TestBudget. Ensure the appropriate draft QA PR for this checkpoint reflects the outcome with the required status, "
            "persist the result keyed to the catalog checksum, and return PR number 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_010"}, "outputs": {}, "status": "started"}),
            Action(name="run_dcc_validation", kwargs={"files": ["assets/audio/music/main_theme.ogg"]}),
            Action(name="run_engine_budget_checks", kwargs={"files": ["assets/audio/music/main_theme.ogg"], "scene": "TestBudget"}),
            Action(name="apply_asset_autofixes", kwargs={"qa_json": [{"file": "assets/audio/music/main_theme.ogg", "issues": []}], "tex_report": []}),
            Action(name="render_asset_previews", kwargs={"files": ["assets/audio/music/main_theme.ogg"]}),
            Action(name="upload_qa_reports", kwargs={"qa_json": [{"file": "assets/audio/music/main_theme.ogg", "issues": []}], "tex_report": [], "engine_report": {"scene": "TestBudget", "files": ["assets/audio/music/main_theme.ogg"], "violations": []}, "previews": {"turntable_uri": "artifact://turntable/1", "stills_uris": ["artifact://still/1"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_010"}, "outputs": {}, "status": "reports_uploaded"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-AR-1", "base": "main", "title": "auto fix build break AR-1", "body": "summary for run AR-1", "run_id": "AR-1"}),
            Action(name="annotate_pr_with_qa", kwargs={"pr_number": 33, "summary": "errors 0 warnings 0", "report_uri": "artifact://qa/summary"}),
            Action(name="set_asset_qa_check", kwargs={"pr_number": 33, "conclusion": "success", "details_uri": "artifact://qa/details"}),
            Action(name="persist_asset_qa_results", kwargs={"asset_id": "asset_010", "commit_sha": "sha256:012345678901234567890abcdef1234567890abcdef1234567890abcdef123456789", "severity_max": "none", "errors_count": 0, "warnings_count": 0, "preview_uri": "artifact://turntable/1", "report_uri": "artifact://qa/summary"}),
            Action(name="record_automation_run", kwargs={"automation_type": "asset-qa", "inputs": {"asset_id": "asset_010"}, "outputs": {"pr_number": 33, "qa_id": "QA-asset_010-sha256:012345678901234567890abcdef1234567890abcdef1234567890abcdef123456789"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="task_041",
        instruction=(
            "You own intake normalization and routing for ticket work_026 with fingerprint renderer_character_load_access_violation_xyz. "
            "Ensure routing reflects the fingerprint-derived impact and owner resolution from src/game/engine/renderer.cpp and persist "
            "triage_status='In Triage', labels=['auto-triage'], impact_score, owner_team, and summary_text; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "started"}),
            # Seed from DB fields only; do not invent payload text
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "work_026"}),
            Action(name="summarize_issue", kwargs={"ticket_key": "work_026"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "work_026", "fingerprint": "renderer_character_load_access_violation_xyz"}),
            Action(name="resolve_owner_from_map", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            # Persist deterministic fields in one minimal update (include exact summary)
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"impact_score": 2, "owner_team": "team_001", "triage_status": "In Triage", "labels": ["auto-triage"], "summary_text": "Issue :: "}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "routed"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {"ticket_key": "work_026"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "work_026"}),
        ],
        outputs=["work_026"],
    ),

    Task(
        annotator="0",
        user_id="task_042",
        instruction=(
            "You are responsible for impact assessment and routing updates for ticket work_026 using its crash fingerprint renderer_character_load_access_violation_xyz. "
            "Persist triage_status='In Triage', labels=['auto-triage'], impact_score, owner_team resolved from src/game/engine/renderer.cpp, and summary_text; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "work_026"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "normalized"}),
            Action(name="summarize_issue", kwargs={"ticket_key": "work_026"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "summarized"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "work_026", "fingerprint": "renderer_character_load_access_violation_xyz"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "scored"}),
            Action(name="resolve_owner_from_map", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            # Persist actual computed values (single update, include summary and owner)
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"impact_score": 2, "owner_team": "team_001", "triage_status": "In Triage", "labels": ["auto-triage"], "summary_text": "Issue :: "}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "routed"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {"ticket_key": "work_026"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "work_026"}),
        ],
        outputs=["work_026"],
    ),

    Task(
        annotator="0",
        user_id="task_043",
        instruction=(
            "You own intake normalization and routing for ticket work_027 (texture artifacts). Link duplicate to work_026 (confidence 0.91), "
            "resolve owner from assets/textures/character_models/, and persist triage_status='In Triage', labels=['auto-triage'], impact_score, owner_team, and summary_text; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_027"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "work_027"}),
            Action(name="summarize_issue", kwargs={"ticket_key": "work_027"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "work_027"}),
            Action(name="link_duplicate_issue", kwargs={"primary_ticket_key": "work_027", "duplicate_ticket_key": "work_026", "confidence": 0.91}),
            Action(name="resolve_owner_from_map", kwargs={"module_or_path": "assets/textures/character_models/"}),
            # Persist computed fields and routing in one minimal update (exact summary from summarize_issue)
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_027", "fields": {"impact_score": 2, "owner_team": "team_002", "triage_status": "In Triage", "labels": ["auto-triage"], "summary_text": "Issue :: "}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {}, "status": "routed"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "work_027"}),
        ],
        outputs=["work_027"],
    ),

    Task(
        annotator="0",
        user_id="task_044",
        instruction=(
            "You are responsible for recording impact and routing fields for ticket work_027 from its normalized data. Persist triage_status='In Triage', "
            "labels=['auto-triage'], and impact_score derived from the normalized issue; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_027"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "work_027"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "normalized"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "work_027"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_027", "fields": {"impact_score": 2, "triage_status": "In Triage", "labels": ["auto-triage"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "routed"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "work_027"}),
        ],
        outputs=["work_027"],
    ),

    Task(
        annotator="0",
        user_id="task_045",
        instruction=(
            "You own routing for ticket work_026. Resolve owner from src/game/engine/renderer.cpp and persist owner_team, triage_status='In Triage', "
            "labels=['auto-triage'], impact_score, and summary_text; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "work_026"}),
            Action(name="summarize_issue", kwargs={"ticket_key": "work_026"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "work_026"}),
            Action(name="resolve_owner_from_map", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"owner_team": "team_001", "triage_status": "In Triage", "labels": ["auto-triage"], "impact_score": 2, "summary_text": "Issue :: "}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "routed"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {"ticket_key": "work_026"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "work_026"}),
        ],
        outputs=["work_026"],
    ),

    Task(
        annotator="0",
        user_id="task_046",
        instruction=(
            "You are responsible for recording a concise summary and impact for ticket work_027 and confirming routing metadata. Persist summary_text, impact_score, "
            "triage_status='In Triage', labels=['auto-triage'], and owner_team resolved from assets/textures/character_models/. Return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_027"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "work_027"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "normalized"}),
            Action(name="summarize_issue", kwargs={"ticket_key": "work_027"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "summarized"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "work_027"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "scored"}),
            Action(name="resolve_owner_from_map", kwargs={"module_or_path": "assets/textures/character_models/"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_027", "fields": {"owner_team": "team_002", "summary_text": "Issue :: ", "impact_score": 2, "triage_status": "In Triage", "labels": ["auto-triage"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "routed"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "work_027"}),
        ],
        outputs=["work_027"],
    ),

    Task(
        annotator="0",
        user_id="task_047",
        instruction=(
            "You own intake normalization and impact logging for ticket work_027; normalize, deduplicate with work_026 if applicable, compute impact, and persist "
            "impact_score, triage_status='In Triage', and labels=['auto-triage']; then return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_027"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "work_027"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {}, "status": "normalized"}),
            Action(name="link_duplicate_issue", kwargs={"primary_ticket_key": "work_026", "duplicate_ticket_key": "work_027", "confidence": 1.0}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "deduped"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "work_027"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "scored"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_027", "fields": {"impact_score": 2, "triage_status": "In Triage", "labels": ["auto-triage"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "work_027"}),
        ],
        outputs=["work_027"],
    ),

    Task(
        annotator="0",
        user_id="task_048",
        instruction=(
            "You are responsible for recording a deterministic summary and resolving owner for ticket work_026. Persist summary_text, impact_score, "
            "triage_status='In Triage', labels=['auto-triage'], and owner_team from src/game/engine/renderer.cpp; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "work_026"}),
            Action(name="summarize_issue", kwargs={"ticket_key": "work_026"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "work_026"}),
            Action(name="resolve_owner_from_map", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"owner_team": "team_001", "impact_score": 2, "summary_text": "Issue :: ", "triage_status": "In Triage", "labels": ["auto-triage"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {"ticket_key": "work_026"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "work_026"}),
        ],
        outputs=["work_026"],
    ),

    Task(
        annotator="0",
        user_id="task_049",
        instruction=(
            "You own deterministic replay of intake for ticket work_026 to confirm normalized fields and routing. Persist normalized flag, triage_status='In Triage', "
            "labels=['auto-triage'], and impact_score; then return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "work_026"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "normalized"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "work_026"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"normalized": True, "impact_score": 2, "triage_status": "In Triage", "labels": ["auto-triage"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {"ticket_key": "work_026"}, "status": "scored"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {"ticket_key": "work_026"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "work_026"}),
        ],
        outputs=["work_026"],
    ),

    Task(
        annotator="0",
        user_id="task_050",
        instruction=(
            "You are responsible for deterministic impact logging and routing for ticket work_027. Persist triage_status='In Triage', labels=['auto-triage'], "
            "impact_score and owner_team resolved from assets/textures/character_models/; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_027"}}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "work_027"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "scored"}),
            Action(name="resolve_owner_from_map", kwargs={"module_or_path": "assets/textures/character_models/"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_027", "fields": {"triage_status": "In Triage", "labels": ["auto-triage"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "routed"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_027", "fields": {"owner_team": "team_002", "impact_score": 2}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_027"}, "outputs": {"ticket_key": "work_027"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "work_027"}),
        ],
        outputs=["work_027"],
    ),

    Task(
        annotator="0",
        user_id="task_051",
        instruction=(
            "You own deterministic duplicate linking and routing for ticket work_026. Link it under canonical work_027 with confidence 0.91 and persist "
            "triage_status='In Triage', labels=['auto-triage','duplicate'], impact_score, owner_team resolved from src/game/engine/renderer.cpp; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_026"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "work_026"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "work_026"}),
            Action(name="resolve_owner_from_map", kwargs={"module_or_path": "src/game/engine/renderer.cpp"}),
            Action(name="link_duplicate_issue", kwargs={"primary_ticket_key": "work_027", "duplicate_ticket_key": "work_026", "confidence": 0.91}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"owner_team": "team_001", "impact_score": 2, "triage_status": "In Triage", "labels": ["auto-triage", "duplicate"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_026"}, "outputs": {"ticket_key": "work_026"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "work_026"}),
        ],
        outputs=["work_026"],
    ),

    Task(
        annotator="0",
        user_id="task_052",
        instruction=(
            "You are responsible for deduplicating ticket work_029 under canonical work_030 (confidence 0.78) and persisting routing labels and impact. "
            "Ensure the ticket exists and that labels=['auto-triage','duplicate'] and impact_score are updated; then return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_029"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "work_029"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "work_029"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "work_029"}),
            Action(name="link_duplicate_issue", kwargs={"primary_ticket_key": "work_030", "duplicate_ticket_key": "work_029", "confidence": 0.78}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_029", "fields": {"impact_score": 2, "labels": ["auto-triage", "duplicate"]}}),
            # Complete the same automation run deterministically
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_029"}, "outputs": {}, "status": "deduplicated"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "work_029"}, "outputs": {"ticket_key": "work_029"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "work_029"}),
        ],
        outputs=["work_029"],
    ),

    Task(
        annotator="0",
        user_id="task_053",
        instruction=(
            "You own duplicate linking for ticket bug_006 under canonical bug_007 with confidence 0.95. Normalize and score impact, then persist "
            "labels=['auto-triage','duplicate'] and impact_score; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_006"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_006"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "bug_006"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "bug_006"}),
            Action(name="link_duplicate_issue", kwargs={"primary_ticket_key": "bug_007", "duplicate_ticket_key": "bug_006", "confidence": 0.95}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "bug_006", "fields": {"impact_score": 2, "labels": ["auto-triage", "duplicate"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_006"}, "outputs": {"ticket_key": "bug_006"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "bug_006"}),
        ],
        outputs=["bug_006"],
    ),

    Task(
        annotator="0",
        user_id="task_054",
        instruction=(
            "You own duplicate linking for ticket bug_009 under canonical bug_010 with confidence 0.82. Normalize and score impact, then persist "
            "labels=['auto-triage','duplicate'] and impact_score; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_009"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_009"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "bug_009"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_009"}, "outputs": {"ticket_key": "bug_009"}, "status": "normalized"}),
            Action(name="summarize_issue", kwargs={"ticket_key": "bug_009"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_009"}, "outputs": {"ticket_key": "bug_009"}, "status": "summarized"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "bug_009"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_009"}, "outputs": {"ticket_key": "bug_009"}, "status": "scored"}),
            Action(name="link_duplicate_issue", kwargs={"primary_ticket_key": "bug_010", "duplicate_ticket_key": "bug_009", "confidence": 0.82}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_009"}, "outputs": {"ticket_key": "bug_009"}, "status": "deduplicated"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "bug_009", "fields": {"labels": ["auto-triage", "duplicate"]}}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "bug_009", "fields": {"impact_score": 2}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_009"}, "outputs": {"ticket_key": "bug_009"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "bug_009"}),
        ],
        outputs=["bug_009"],
    ),

    Task(
        annotator="0",
        user_id="task_055",
        instruction=(
            "You own duplicate linking for ticket bug_013 under canonical bug_014 with confidence 0.89. Normalize and score impact, then persist "
            "labels=['auto-triage','duplicate'] and impact_score; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_013"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_013"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "bug_013"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "bug_013"}),
            Action(name="link_duplicate_issue", kwargs={"primary_ticket_key": "bug_014", "duplicate_ticket_key": "bug_013", "confidence": 0.89}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "bug_013", "fields": {"impact_score": 2, "labels": ["auto-triage", "duplicate"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_013"}, "outputs": {"ticket_key": "bug_013"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "bug_013"}),
        ],
        outputs=["bug_013"],
    ),

    Task(
        annotator="0",
        user_id="task_056",
        instruction=(
            "You own duplicate linking for ticket bug_016 under canonical bug_017 with confidence 0.76. Normalize and score impact, then persist "
            "labels=['auto-triage','duplicate'] and impact_score; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_016"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_016"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "bug_016"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "bug_016"}),
            Action(name="link_duplicate_issue", kwargs={"primary_ticket_key": "bug_017", "duplicate_ticket_key": "bug_016", "confidence": 0.76}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "bug_016", "fields": {"impact_score": 2, "labels": ["auto-triage", "duplicate"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_016"}, "outputs": {"ticket_key": "bug_016"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "bug_016"}),
        ],
        outputs=["bug_016"],
    ),

    Task(
        annotator="0",
        user_id="task_057",
        instruction=(
            "You own duplicate linking for ticket bug_intake_008 under canonical bug_intake_007 with confidence 0.98. Normalize and score impact, then persist "
            "labels=['auto-triage','duplicate'] and impact_score; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_008"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_008"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "bug_intake_008"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_008"}, "outputs": {"ticket_key": "bug_intake_008"}, "status": "normalized"}),
            Action(name="summarize_issue", kwargs={"ticket_key": "bug_intake_008"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_008"}, "outputs": {"ticket_key": "bug_intake_008"}, "status": "summarized"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "bug_intake_008"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_008"}, "outputs": {"ticket_key": "bug_intake_008"}, "status": "scored"}),
            Action(name="link_duplicate_issue", kwargs={"primary_ticket_key": "bug_intake_007", "duplicate_ticket_key": "bug_intake_008", "confidence": 0.98}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_008"}, "outputs": {"ticket_key": "bug_intake_008"}, "status": "deduplicated"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "bug_intake_008", "fields": {"labels": ["auto-triage", "duplicate"]}}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "bug_intake_008", "fields": {"impact_score": 2}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_008"}, "outputs": {"ticket_key": "bug_intake_008"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "bug_intake_008"}),
        ],
        outputs=["bug_intake_008"],
    ),

    Task(
        annotator="0",
        user_id="task_058",
        instruction=(
            "You are responsible for deduplicating ticket bug_intake_016 under canonical bug_intake_015 (confidence 0.93) and persisting routing labels and impact. "
            "Ensure the ticket exists and that labels=['auto-triage','duplicate'] and impact_score are updated; then return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_016"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_016"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "bug_intake_016"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "bug_intake_016"}),
            Action(name="link_duplicate_issue", kwargs={"primary_ticket_key": "bug_intake_015", "duplicate_ticket_key": "bug_intake_016", "confidence": 0.93}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "bug_intake_016", "fields": {"impact_score": 2, "labels": ["auto-triage", "duplicate"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_016"}, "outputs": {}, "status": "deduplicated"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_016"}, "outputs": {"ticket_key": "bug_intake_016"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "bug_intake_016"}),
        ],
        outputs=["bug_intake_016"],
    ),

    Task(
        annotator="0",
        user_id="task_059",
        instruction=(
            "You own duplicate linking for ticket bug_intake_020 under canonical bug_intake_019 with confidence 0.89. Normalize and score impact, then persist "
            "labels=['auto-triage','duplicate'] and impact_score; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_020"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_020"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "bug_intake_020"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_020"}, "outputs": {"ticket_key": "bug_intake_020"}, "status": "normalized"}),
            Action(name="summarize_issue", kwargs={"ticket_key": "bug_intake_020"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_020"}, "outputs": {"ticket_key": "bug_intake_020"}, "status": "summarized"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "bug_intake_020"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_020"}, "outputs": {"ticket_key": "bug_intake_020"}, "status": "scored"}),
            Action(name="link_duplicate_issue", kwargs={"primary_ticket_key": "bug_intake_019", "duplicate_ticket_key": "bug_intake_020", "confidence": 0.89}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_020"}, "outputs": {"ticket_key": "bug_intake_020"}, "status": "deduplicated"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "bug_intake_020", "fields": {"labels": ["auto-triage", "duplicate"]}}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "bug_intake_020", "fields": {"impact_score": 2}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_020"}, "outputs": {"ticket_key": "bug_intake_020"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "bug_intake_020"}),
        ],
        outputs=["bug_intake_020"],
    ),

    Task(
        annotator="0",
        user_id="task_060",
        instruction=(
            "You own duplicate linking for ticket bug_intake_024 under canonical bug_intake_023 with confidence 0.96. Normalize and score impact, then persist "
            "labels=['auto-triage','duplicate'] and impact_score; return the ticket key."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_024"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ticket_webhook", kwargs={"event": "issue_created", "payload": {"ticket_key": "bug_intake_024"}}),
            Action(name="normalize_issue", kwargs={"ticket_key": "bug_intake_024"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_024"}, "outputs": {"ticket_key": "bug_intake_024"}, "status": "normalized"}),
            Action(name="summarize_issue", kwargs={"ticket_key": "bug_intake_024"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_024"}, "outputs": {"ticket_key": "bug_intake_024"}, "status": "summarized"}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "bug_intake_024"}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_024"}, "outputs": {"ticket_key": "bug_intake_024"}, "status": "scored"}),
            Action(name="link_duplicate_issue", kwargs={"primary_ticket_key": "bug_intake_023", "duplicate_ticket_key": "bug_intake_024", "confidence": 0.96}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_024"}, "outputs": {"ticket_key": "bug_intake_024"}, "status": "deduplicated"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "bug_intake_024", "fields": {"labels": ["auto-triage", "duplicate"]}}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "bug_intake_024", "fields": {"impact_score": 2}}),
            Action(name="record_automation_run", kwargs={"automation_type": "bug-intake", "inputs": {"ticket_key": "bug_intake_024"}, "outputs": {"ticket_key": "bug_intake_024"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "bug_intake_024"}),
        ],
        outputs=["bug_intake_024"],
    ),

    Task(
        annotator="0",
        user_id="task_061",
        instruction=(
            "You are responsible for a complete localization kit for PR 999 using all changed strings across de, fr, ja, with a 200px UI budget. Persist bundles and open a review TMS job; return the PR number."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="detect_changed_strings", kwargs={"pr_number": 999}),
            Action(name="capture_loc_context", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="loc_lint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "999"}),
        ],
        outputs=["999"],
    ),

    Task(
        annotator="0",
        user_id="task_062",
        instruction=(
            "You are responsible for verifying localization for PR 999 using all changed strings across de, fr, ja at a 200px budget. Persist bundles and open a review TMS job; return the PR number."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="detect_changed_strings", kwargs={"pr_number": 999}),
            Action(name="capture_loc_context", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="loc_lint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "999"}),
        ],
        outputs=["999"],
    ),

    Task(
        annotator="0",
        user_id="task_063",
        instruction=(
            "You are responsible for a German-first draft localization kit for PR 999 using all changed strings in de, fr, ja with a 200px budget. Persist bundles and open a review TMS job; return the PR number."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="detect_changed_strings", kwargs={"pr_number": 999}),
            Action(name="capture_loc_context", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="loc_lint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "999"}),
        ],
        outputs=["999"],
    ),

    Task(
        annotator="0",
        user_id="task_064",
        instruction=(
            "You are responsible for a context-rich localization kit for PR 999 using all changed strings in de, fr, ja with a 200px budget. Persist bundles and open a review TMS job; return the PR number."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="detect_changed_strings", kwargs={"pr_number": 999}),
            Action(name="capture_loc_context", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="loc_lint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "999"}),
        ],
        outputs=["999"],
    ),

    Task(
        annotator="0",
        user_id="task_065",
        instruction=(
            "You are responsible for pixel-budget-focused localization for PR 999 using all changed strings in de, fr, ja with a 200px budget. Persist bundles and open a review TMS job; return the PR number."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="detect_changed_strings", kwargs={"pr_number": 999}),
            Action(name="capture_loc_context", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="loc_lint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "999"}),
        ],
        outputs=["999"],
    ),

    Task(
        annotator="0",
        user_id="task_066",
        instruction=(
            "You are responsible for context capture and localization prep for PR 999 using all changed strings in de, fr, ja at a 200px budget. Persist bundles and open a review TMS job; return the PR number."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="detect_changed_strings", kwargs={"pr_number": 999}),
            Action(name="capture_loc_context", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="loc_lint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "999"}),
        ],
        outputs=["999"],
    ),

    Task(
        annotator="0",
        user_id="task_067",
        instruction=(
            "You are responsible for cross-locale lint verification for PR 999 using all changed strings across de, fr, ja at a 200px budget. Persist bundles and open a review TMS job; return the PR number."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="detect_changed_strings", kwargs={"pr_number": 999}),
            Action(name="capture_loc_context", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="loc_lint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "999"}),
        ],
        outputs=["999"],
    ),

    Task(
        annotator="0",
        user_id="task_068",
        instruction=(
            "You are responsible for bundle generation after lint for PR 999 using all changed strings in de, fr, ja at a 200px budget. Persist bundles and open a review TMS job; return the PR number."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="detect_changed_strings", kwargs={"pr_number": 999}),
            Action(name="capture_loc_context", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="loc_lint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "999"}),
        ],
        outputs=["999"],
    ),

    Task(
        annotator="0",
        user_id="task_069",
        instruction=(
            "You are responsible for a validation pass for PR 999 localization using all changed strings across de, fr, ja at a 200px budget. Persist bundles and open a review TMS job; return the PR number."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="detect_changed_strings", kwargs={"pr_number": 999}),
            Action(name="capture_loc_context", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="loc_lint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "999"}),
        ],
        outputs=["999"],
    ),

    Task(
        annotator="0",
        user_id="task_070",
        instruction=(
            "You finalize the localization kit for PR 999 using all changed strings in de, fr, ja at a 200px budget. Persist bundles and open a review TMS job; return the PR number."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {}, "status": "started"}),
            Action(name="detect_changed_strings", kwargs={"pr_number": 999}),
            Action(name="capture_loc_context", kwargs={"keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="loc_lint", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="loc_lint", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"], "ui_px_limit": 200}),
            Action(name="write_locale_bundle", kwargs={"locale": "de", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "fr", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "ja", "keys": ["ui.main_menu.start_game", "ui.settings.audio", "ui.settings.audio.master_volume", "ui.settings.audio.music_volume", "ui.settings.audio.sfx_volume", "ui.settings.graphics", "ui.settings.graphics.resolution", "ui.settings.graphics.quality", "ui.game.hud.health", "ui.game.hud.mana"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "bundles-pr-999-keys-10", "locales": ["de", "fr", "ja"], "status": "in_review"}),
            Action(name="record_automation_run", kwargs={"automation_type": "localization", "inputs": {"pr_number": 999}, "outputs": {"pr_number": 999}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "999"}),
        ],
        outputs=["999"],
    ),
    Task(
        annotator="0",
        user_id="task_071",
        instruction=(
            "You are responsible for validating subtitle timing and persisting VO workflow state for hero introduction across locales. Use the stored records for "
            "subtitle_001 (en) and subtitle_002 (de) tied to string_key 'vo.hero.intro_01', persist per-locale bundles, open a review job named 'tms-vo-lines-subtitle_001-subtitle_002' "
            "with locales ordered as ['en','de'], and reflect VO labels ['vo-subtitles','timing-validated'] on ticket 'work_026'; then return the number of processed lines."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_001", "subtitle_002"]}, "outputs": {}, "status": "started"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_001", "locale": "en"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="write_locale_bundle", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "de", "keys": ["vo.hero.intro_01"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "tms-vo-lines-subtitle_001-subtitle_002", "locales": ["en", "de"], "status": "in_review"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_001", "subtitle_002"]}, "outputs": {"lines": ["subtitle_001", "subtitle_002"]}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "2"}),
        ],
        outputs=["2"],
    ),

    Task(
        annotator="0",
        user_id="task_072",
        instruction=(
            "You are responsible for VO subtitle timing QA and handoff for the second hero introduction line across locales 'en' and 'fr'. "
            "Apply policy-driven validation, packaging, and review registration using deterministic identifiers derived from the involved line IDs and string keys, "
            "and reflect the outcome on tracking ticket 'work_026' with the appropriate labels. Return the number of lines processed."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_003", "subtitle_004"]}, "outputs": {}, "status": "started"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_003", "locale": "en"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="write_locale_bundle", kwargs={"locale": "en", "keys": ["subtitle_003"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "fr", "keys": ["subtitle_004"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "tms-vo-lines-subtitle_003-subtitle_004", "locales": ["en", "fr"], "status": "in_review"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_003", "subtitle_004"]}, "outputs": {"lines": ["subtitle_003", "subtitle_004"], "bundle_uri": "artifact://bundle/bundle-en-1", "tms_job_id": "TMS-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "2"}),
        ],
        outputs=["2"],
    ),

    Task(
        annotator="0",
        user_id="task_073",
        instruction=(
            "You are responsible for VO subtitle timing QA and handoff for the villain threat: process subtitle_005 (en) and subtitle_006 (ja) under string_key 'vo.villain.threat_01'. "
            "Apply policy-driven validation, packaging, and review registration using deterministic identifiers, and reflect the outcome on tracking ticket 'work_026' with the appropriate labels. "
            "Return the number of lines processed."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_005", "subtitle_006"]}, "outputs": {}, "status": "started"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_005", "locale": "en"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="write_locale_bundle", kwargs={"locale": "en", "keys": ["subtitle_005"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "ja", "keys": ["subtitle_006"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "tms-vo-lines-subtitle_005-subtitle_006", "locales": ["en", "ja"], "status": "in_review"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_005", "subtitle_006"]}, "outputs": {"lines": ["subtitle_005", "subtitle_006"], "bundle_uris": {"en": "artifact://bundle/bundle-en-1", "ja": "artifact://bundle/bundle-ja-1"}}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "2"}),
        ],
        outputs=["2"],
    ),
    Task(
        annotator="0",
        user_id="task_074",
        instruction=(
            "You are responsible for validating subtitle timing for the NPC quest line across locales. Use subtitle_007 (en) and subtitle_008 (es) for string_key 'vo.npc.quest_01', "
            "persist per-locale bundles, open a review job named 'tms-vo-lines-subtitle_007-subtitle_008' with locales ['en','es'], and update labels on ticket 'work_026'; "
            "then return the number of processed lines."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_007", "subtitle_008"]}, "outputs": {}, "status": "started"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_007", "locale": "en"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="write_locale_bundle", kwargs={"locale": "en", "keys": ["vo.npc.quest_01"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "tms-vo-lines-subtitle_007-subtitle_008", "locales": ["en", "es"], "status": "in_review"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_007", "subtitle_008"]}, "outputs": {"lines": ["subtitle_007", "subtitle_008"]}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "2"}),
        ],
        outputs=["2"],
    ),

    Task(
        annotator="0",
        user_id="task_075",
        instruction=(
            "You are responsible for VO subtitle timing QA and handoff for the menu selection line across locales 'en' and 'zh'. "
            "Apply policy-driven validation, packaging, and review registration using deterministic identifiers derived from the involved line IDs and string keys, "
            "and reflect the outcome on tracking ticket 'work_026' with the appropriate labels. Return the number of lines processed."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_009", "subtitle_010"]}, "outputs": {}, "status": "started"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_009", "locale": "en"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="write_locale_bundle", kwargs={"locale": "en", "keys": ["subtitle_009"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "zh", "keys": ["subtitle_010"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "tms-vo-lines-subtitle_009-subtitle_010", "locales": ["en", "zh"], "status": "in_review"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_009", "subtitle_010"]}, "outputs": {"lines": ["subtitle_009", "subtitle_010"], "bundle_uris": {"en": "artifact://bundle/bundle-en-1", "zh": "artifact://bundle/bundle-zh-1"}, "tms_job_id": "TMS-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "2"}),
        ],
        outputs=["2"],
    ),

    Task(
        annotator="0",
        user_id="task_076",
        instruction=(
            "You own consolidation of VO subtitle timing verification for English lines subtitle_001, subtitle_003, and subtitle_005. "
            "Apply policy-driven validation and compliant handoff using deterministic identifiers derived from the validated items, and reflect results on ticket 'work_026' "
            "with the standard VO timing labels 'vo-subtitles' and 'timing-validated'. Return the processed line count."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_001", "subtitle_003", "subtitle_005"]}, "outputs": {}, "status": "started"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_001", "locale": "en"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_003", "locale": "en"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_005", "locale": "en"}),
            Action(name="write_locale_bundle", kwargs={"locale": "en", "keys": ["subtitle_001", "subtitle_003", "subtitle_005"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "tms-vo-lines-subtitle_001-subtitle_003-subtitle_005", "locales": ["en"], "status": "in_review"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_001", "subtitle_003", "subtitle_005"]}, "outputs": {"lines": ["subtitle_001", "subtitle_003", "subtitle_005"], "bundle_uri": "artifact://bundle/bundle-en-3", "tms_job_id": "TMS-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "3"}),
        ],
        outputs=["3"],
    ),

    Task(
        annotator="0",
        user_id="task_077",
        instruction=(
            "You are responsible for VO subtitle timing QA and handoff for the hero introduction across locales 'de' and 'fr'. "
            "Apply policy-driven validation, packaging, and review registration using deterministic identifiers derived from the involved line IDs and string keys, "
            "and reflect the outcome on tracking ticket 'work_026' with the appropriate labels. Return the number of lines processed."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_002", "subtitle_004"]}, "outputs": {}, "status": "started"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_002", "locale": "de"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="write_locale_bundle", kwargs={"locale": "de", "keys": ["subtitle_002"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "fr", "keys": ["subtitle_004"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "tms-vo-lines-subtitle_002-subtitle_004", "locales": ["de", "fr"], "status": "in_review"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_002", "subtitle_004"]}, "outputs": {"lines": ["subtitle_002", "subtitle_004"], "bundle_uris": {"de": "artifact://bundle/bundle-de-1", "fr": "artifact://bundle/bundle-fr-1"}, "tms_job_id": "TMS-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "2"}),
        ],
        outputs=["2"],
    ),

    Task(
        annotator="0",
        user_id="task_078",
        instruction=(
            "You must confirm timing status and persist VO state for three locales without inventing identifiers. Validate subtitle_006 (ja), subtitle_008 (es), subtitle_010 (zh) "
            "with exact string_keys from data: ja→'vo.villain.threat_01', es→'vo.npc.quest_01', zh→'vo.ui.menu_select'. Persist per-locale bundles, register the review job "
            "'tms-vo-lines-subtitle_006-subtitle_008-subtitle_010' with locales ['ja','es','zh'], and update work item 'work_026' by adding labels ['vo-subtitles','timing-validated']. "
            "Return the processed line count."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_006", "subtitle_008", "subtitle_010"]}, "outputs": {}, "status": "started"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_006", "locale": "ja"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_008", "locale": "es"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_010", "locale": "zh"}),
            Action(name="write_locale_bundle", kwargs={"locale": "ja", "keys": ["vo.villain.threat_01"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "es", "keys": ["vo.npc.quest_01"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "zh", "keys": ["vo.ui.menu_select"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "tms-vo-lines-subtitle_006-subtitle_008-subtitle_010", "locales": ["ja", "es", "zh"], "status": "in_review"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_006", "subtitle_008", "subtitle_010"]}, "outputs": {"lines": ["subtitle_006", "subtitle_008", "subtitle_010"]}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "3"}),
        ],
        outputs=["3"],
    ),

    Task(
        annotator="0",
        user_id="task_079",
        instruction=(
            "You are responsible for VO subtitle timing QA and handoff for the English UI and quest lines. "
            "Apply policy-driven validation, packaging, and review registration using deterministic identifiers derived from the involved line IDs and string keys, "
            "and reflect the outcome on tracking ticket 'work_026' with the appropriate labels. Return the number of lines processed."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_007", "subtitle_009"]}, "outputs": {}, "status": "started"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_007", "locale": "en"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_009", "locale": "en"}),
            Action(name="write_locale_bundle", kwargs={"locale": "en", "keys": ["subtitle_007", "subtitle_009"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "tms-vo-lines-subtitle_007-subtitle_009", "locales": ["en"], "status": "in_review"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_007", "subtitle_009"]}, "outputs": {"lines": ["subtitle_007", "subtitle_009"], "bundle_uri": "artifact://bundle/bundle-en-2", "tms_job_id": "TMS-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "2"}),
        ],
        outputs=["2"],
    ),

    Task(
        annotator="0",
        user_id="task_080",
        instruction=(
            "You must validate cross-locale hero intro timing and persist outcomes deterministically. Use subtitle_001 (en→'vo.hero.intro_01') and subtitle_004 (fr→'vo.hero.intro_02'), "
            "persist per-locale bundles, register the review job 'tms-vo-lines-subtitle_001-subtitle_004' with locales ['en','fr'], and update work item 'work_026' by adding "
            "labels ['vo-subtitles','timing-validated']. Return the processed line count."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_001", "subtitle_004"]}, "outputs": {}, "status": "started"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_001", "locale": "en"}),
            Action(name="validate_subtitle_timing", kwargs={"line_id": "subtitle_004", "locale": "fr"}),
            Action(name="write_locale_bundle", kwargs={"locale": "en", "keys": ["vo.hero.intro_01"]}),
            Action(name="write_locale_bundle", kwargs={"locale": "fr", "keys": ["vo.hero.intro_02"]}),
            Action(name="create_tms_job", kwargs={"bundle_name": "tms-vo-lines-subtitle_001-subtitle_004", "locales": ["en", "fr"], "status": "in_review"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "work_026", "fields": {"labels": ["vo-subtitles", "timing-validated"]}}),
            Action(name="record_automation_run", kwargs={"automation_type": "vo-subtitles", "inputs": {"lines": ["subtitle_001", "subtitle_004"]}, "outputs": {"lines": ["subtitle_001", "subtitle_004"]}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "2"}),
        ],
        outputs=["2"],
    ),
    Task(
        annotator="0",
        user_id="task_081",
        instruction=(
            "You must close the CI→Bug→PR loop for run_001 using the system’s deterministic policy and stored evidence. Rely on the extracted signals and the canonical run-based fingerprint 'sig:run_001:first_failure'."
            " Produce a draft PR and linked ticket per policy and return 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_001"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_001", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_001"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_001"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_001:first_failure"}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "run_001"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "main", "run_id": "run_001"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_001"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_001", "patch_id": "FP-run_001", "message": "auto tentative fix for run run_001"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_001", "base": "main", "title": "auto fix build break run_001", "body": "summary for run run_001", "run_id": "run_001"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_001", "description": "Automated triage for run_001", "run_id": "run_001", "pr_number": 33}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "ENGINE-MIG-1", "fingerprint": "sig:run_001:first_failure"}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "run_001"}),
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_001"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),
    Task(
        annotator="0",
        user_id="task_082",
        instruction=(
            "You must close the loop for run_003 per policy using stored evidence. Use the extracted canonical fingerprint 'sig:run_003:first_failure' and produce a draft PR and linked ticket; return 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_003"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_003"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_003"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_003:first_failure"}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "run_003"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "main", "run_id": "run_003"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_003"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_003", "patch_id": "FP-run_003", "message": "auto tentative fix for run run_003"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_003", "base": "main", "title": "auto fix build break run_003", "body": "summary for run run_003", "run_id": "run_003"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003", "pr_number": 33}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "ENGINE-MIG-1", "fingerprint": "sig:run_003:first_failure"}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "run_003"}),
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_003"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_083",
        instruction=(
            "You must Close the CI→Bug→PR loop for run_005 using deterministic policy and stored evidence. Create a draft PR, open a linked ticket, reflect validation, and return 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_005"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "def456abc123789", "job_name": "test-integration-linux"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_005"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_005"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:def456abc123789:first_failure"}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "def456abc123789"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "main", "run_id": "run_005"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_005", "first_bad_commit": "def456abc123789"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_005", "patch_id": "FP-run_005", "message": "auto tentative fix for run run_005"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_005", "base": "main", "title": "auto fix build break run_005", "body": "summary for run run_005", "run_id": "run_005"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005", "pr_number": 33}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "ENGINE-MIG-1", "fingerprint": "sig:def456abc123789:first_failure"}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "test-integration-linux"}),
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_005"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_084",
        instruction=(
            "You must close the CI→Bug→PR loop for run_007 using deterministic policy and stored evidence. Create a draft PR, open a linked ticket, reflect validation, and return 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_007"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_007"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_007"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_007:first_failure"}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "run_007"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "main", "run_id": "run_007"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_007"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_007", "patch_id": "FP-run_007", "message": "auto tentative fix for run run_007"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_007", "base": "main", "title": "auto fix build break run_007", "body": "summary for run run_007", "run_id": "run_007"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007", "pr_number": 33}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "ENGINE-MIG-1", "fingerprint": "sig:run_007:first_failure"}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "run_007"}),
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_007"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_085",
        instruction=(
            "You must close the CI→Bug→PR loop for run_010 using deterministic policy and stored evidence. The CI provider is 'github_actions' and the validation test_target to use is 'run_010'.\n"
            "Create a draft PR, open a linked ticket, reflect validation deterministically, and return 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_010"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_010", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_010"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_010"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_010:first_failure"}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "run_010"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "main", "run_id": "run_010"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_010"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_010", "patch_id": "FP-run_010", "message": "auto tentative fix for run run_010"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_010", "base": "main", "title": "auto fix build break run_010", "body": "summary for run run_010", "run_id": "run_010"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_010", "description": "Automated triage for run_010", "run_id": "run_010", "pr_number": 33}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "ENGINE-MIG-1", "fingerprint": "sig:run_010:first_failure"}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "run_010"}),
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_010"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_086",
        instruction=(
            "You must maintain the CI→Bug→PR traceability for run_002 (successful run) using deterministic policy and stored evidence. Create a draft PR, open a linked ticket, reflect validation, and return 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_002"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_002", "status": "success"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_002"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "main", "run_id": "run_002"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_002", "base": "main", "title": "auto fix build break run_002", "body": "summary for run run_002", "run_id": "run_002"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_002", "description": "Automated triage for run_002", "run_id": "run_002", "pr_number": 33}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "ENGINE-MIG-1"}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "run_002"}),
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_002"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_087",
        instruction=(
            "You must maintain the CI→Bug→PR traceability for run_004 using deterministic policy and stored evidence. Create a draft PR, open a linked ticket, reflect validation, and return 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_004"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_004", "status": "success"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_004"}),
            Action(name="record_automation_run", kwargs={"automation_type": "artifact-index", "inputs": {"run_id": "run_004"}, "outputs": {}, "status": "completed"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "main", "run_id": "run_004"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_004", "base": "main", "title": "auto fix build break run_004", "body": "summary for run run_004", "run_id": "run_004"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_004", "description": "Automated triage for run_004", "run_id": "run_004", "pr_number": 33}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "ENGINE-MIG-1"}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "run_004"}),
            Action(name="record_automation_run", kwargs={"automation_type": "build-metrics", "inputs": {"run_id": "run_004"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_004"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_088",
        instruction=(
            "You must close the CI→Bug→PR loop for run_008 using deterministic policy and stored evidence. Create a draft PR, open a linked ticket, reflect validation, and return 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_008"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_008", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_008"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_008"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_008:first_failure"}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "run_008"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "main", "run_id": "run_008"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_008"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_008", "patch_id": "FP-run_008", "message": "auto tentative fix for run run_008"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_008", "base": "main", "title": "auto fix build break run_008", "body": "summary for run run_008", "run_id": "run_008"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_008", "description": "Automated triage for run_008", "run_id": "run_008", "pr_number": 33}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "ENGINE-MIG-1", "fingerprint": "sig:run_008:first_failure"}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "run_008"}),
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_008"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_089",
        instruction=(
            "You are responsible for maintaining CI→Bug→PR traceability for run_009 under deterministic policy using only stored evidence. "
            "Ensure the CI event status reflects the database record for run_009, coordinate the draft PR and linked ticket with deterministic identifiers, "
            "record validation status, and return 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_009"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_009", "status": "success", "repo": "game-engine", "branch": "feature/new-renderer", "commit_sha": "abc123def456789", "job_name": "security-scan-windows"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_009"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "main", "run_id": "run_009"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_009", "base": "main", "title": "auto fix build break run_009", "body": "summary for run run_009", "run_id": "run_009"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_009", "description": "Automated triage for run_009", "run_id": "run_009", "pr_number": 33}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "ENGINE-MIG-1"}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "run_009"}),
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_009"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1", "status": "success"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_090",
        instruction=(
            "You must close the CI→Bug→PR loop for run_006 using deterministic policy and stored evidence. Create a draft PR, open a linked ticket, reflect validation, and return 33."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_006"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_006", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_006"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_006"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_006:first_failure"}),
            Action(name="enumerate_suspects", kwargs={"failing_sha": "run_006"}),
            Action(name="open_auto_branch", kwargs={"base_ref": "main", "run_id": "run_006"}),
            Action(name="propose_fix_patch", kwargs={"run_id": "run_006"}),
            Action(name="commit_patch_to_branch", kwargs={"branch_ref": "auto/fix-run_006", "patch_id": "FP-run_006", "message": "auto tentative fix for run run_006"}),
            Action(name="open_draft_pull_request", kwargs={"head": "auto/fix-run_006", "base": "main", "title": "auto fix build break run_006", "body": "summary for run run_006", "run_id": "run_006"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_006", "description": "Automated triage for run_006", "run_id": "run_006", "pr_number": 33}),
            Action(name="compute_impact_score", kwargs={"ticket_key": "ENGINE-MIG-1", "fingerprint": "sig:run_006:first_failure"}),
            Action(name="run_validation_checks", kwargs={"pr_number": 33, "test_target": "run_006"}),
            Action(name="record_automation_run", kwargs={"automation_type": "ci-bug-pr-loop", "inputs": {"run_id": "run_006"}, "outputs": {"pr_number": 33, "ticket_key": "ENGINE-MIG-1"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "33"}),
        ],
        outputs=["33"],
    ),

    Task(
        annotator="0",
        user_id="task_091",
        instruction=(
            "You are responsible for release-blocker escalation and recurrence handling for run_001. Using only the JSON database and deterministic policy, you must rely on stored evidence\n"
            "(e.g., extracted failure signatures and prior incidents) to link the new failure to its canonical parent when appropriate, update the work item’s state and labels to reflect\n"
            "escalation, and ensure a complete audit trail via automation runs. Avoid inventing identifiers; all arguments must be unambiguous and derived from this run_id or data. Return 'ok'."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_001"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_001", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_001"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_001"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_001:first_failure"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_001", "description": "Automated triage for run_001", "run_id": "run_001"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_001"}}),
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_001"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_001:first_failure"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "ok"}),
        ],
        outputs=["ok"],
    ),

    Task(
        annotator="0",
        user_id="task_092",
        instruction=(
            "You must deterministically escalate a potential release-blocker for run_003 by leveraging the extracted signature and prior incidents, linking the event to the canonical\n"
            "ticket when applicable, updating state/labels to reflect escalation, and recording all actions for auditability. Use only database values and deterministic formats. Return 'ok'."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_003"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_003", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_003"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_003"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_003:first_failure"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_003", "description": "Automated triage for run_003", "run_id": "run_003"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated"}}),
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_003"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_003:first_failure"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "ok"}),
        ],
        outputs=["ok"],
    ),

    Task(
        annotator="0",
        user_id="task_093",
        instruction=(
            "You must perform deterministic recurrence escalation for run_013 using only stored evidence and policy (not step lists). You must link to the canonical incident for this fingerprint when deterministically available (do not invent IDs),"
            " apply labels 'release-blocker' and 'recurrence', set state to 'Escalated', ensure auditability via a recorded automation run, and return 'ok'."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_013"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_013", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_013"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_013"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_013:first_failure"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_013", "description": "Automated triage for run_013", "run_id": "run_013"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_013"}}),
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_013"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_013:first_failure"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "ok"}),
        ],
        outputs=["ok"],
    ),

    Task(
        annotator="0",
        user_id="task_094",
        instruction=(
            "You must escalate recurrence deterministically for run_012 by using the extracted signature and similar incidents to link to the canonical ticket, updating state/labels for\n"
            "release-blocker visibility, and persisting a complete automation run. Only deterministic, database-sourced arguments are permitted. Return 'ok'."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_012"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_012", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_012"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_012"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_012:first_failure"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_012", "description": "Automated triage for run_012", "run_id": "run_012"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated"}}),
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_012"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_012:first_failure"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "ok"}),
        ],
        outputs=["ok"],
    ),

    Task(
        annotator="0",
        user_id="task_095",
        instruction=(
            "You are responsible for deterministic CI triage and recurrence escalation for run_011 under the domain policy, using only database-driven values. You must achieve canonical linkage when applicable, reflect escalation via labels/state, ensure a complete automation audit trail, and return 'ok'. Do not invent identifiers."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_011"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_011", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_011"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_011"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_011:first_failure"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_011", "description": "Automated triage for run_011", "run_id": "run_011"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_011"}}),
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_011"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_011:first_failure"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "ok"}),
        ],
        outputs=["ok"],
    ),

    Task(
        annotator="0",
        user_id="task_096",
        instruction=(
            "You are accountable for deterministic release-blocker escalation on run_010 using only evidence from the database. Link to its canonical incident when applicable (do not invent IDs), apply labels"
            " 'release-blocker' and 'recurrence', set state to 'Escalated', and record the automation run for audit. All inputs must be deterministically sourced. Return 'ok'."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_010"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_010", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_010"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_010"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_010:first_failure"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_010", "description": "Automated triage for run_010", "run_id": "run_010"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_010"}}),
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_010"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_010:first_failure"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "ok"}),
        ],
        outputs=["ok"],
    ),

    Task(
        annotator="0",
        user_id="task_097",
        instruction=(
            "You must perform deterministic recurrence escalation for run_008 by deriving the failure signature deterministically, linking deterministically to its canonical parent, updating the\n"
            "work item’s labels/state to reflect a release-blocker, and recording the automation steps for audit. All arguments must be derived from the run or database. Return 'ok'."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_008"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_008", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_008"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_008"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_008:first_failure"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_008", "description": "Automated triage for run_008", "run_id": "run_008"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_008"}}),
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_008"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_008:first_failure"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "ok"}),
        ],
        outputs=["ok"],
    ),

    Task(
        annotator="0",
        user_id="task_098",
        instruction=(
            "You are responsible for release-blocker escalation for run_007 under deterministic policy. Using only database-driven values, you must derive the failure signature deterministically, retrieve similar incidents, link to the canonical incident when deterministically available, and reflect escalation via labels/state with a complete automation audit trail. Return 'ok'."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_007"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_007", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_007"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_007"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_007:first_failure"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_007", "description": "Automated triage for run_007", "run_id": "run_007"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_007"}}),
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_007"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_007:first_failure"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "ok"}),
        ],
        outputs=["ok"],
    ),
    Task(
        annotator="0",
        user_id="task_099",
        instruction=(
            "You must deterministically escalate the recurrence for run_006 using policy and stored evidence (no step-by-step guidance). Link to the canonical incident for this fingerprint when applicable,"
            " apply labels 'release-blocker' and 'recurrence', set state to 'Escalated', and capture a complete automation run. All arguments must be sourced from the run_id or database. Return 'ok'."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_006"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_006", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_006"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_006"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_006:first_failure"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_006", "description": "Automated triage for run_006", "run_id": "run_006"}),

            Action(name="update_ticket_fields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_006"}}),
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_006"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_006:first_failure"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "ok"}),
        ],
        outputs=["ok"],
    ),

    Task(
        annotator="0",
        user_id="task_100",
        instruction=(
            "You own recurrence detection for run_005 under deterministic policy. Link to the canonical incident for this fingerprint when applicable, escalate with labels 'release-blocker' and 'recurrence',"
            " set state to 'Escalated', and record a complete automation run trail. Do not invent IDs; derive all arguments deterministically. Return 'ok'."
        ),
        actions=[
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_005"}, "outputs": {}, "status": "started"}),
            Action(name="receive_ci_event", kwargs={"provider": "github_actions", "run_id": "run_005", "status": "failure"}),
            Action(name="attach_run_artifacts", kwargs={"run_id": "run_005"}),
            Action(name="extract_failure_signals", kwargs={"run_id": "run_005"}),
            Action(name="find_similar_incidents", kwargs={"signature": "sig:run_005:first_failure"}),
            Action(name="get_project_key", kwargs={}),
            Action(name="create_or_update_ticket", kwargs={"project_key": "ENGINE-MIG", "summary": "CI failure run_005", "description": "Automated triage for run_005", "run_id": "run_005"}),
            Action(name="update_ticket_fields", kwargs={"ticket_key": "ENGINE-MIG-1", "fields": {"labels": ["release-blocker", "recurrence"], "state": "Escalated", "duplicate_of_crash": "CR-run_005"}}),
            Action(name="record_automation_run", kwargs={"automation_type": "release-blocker", "inputs": {"run_id": "run_005"}, "outputs": {"ticket_key": "ENGINE-MIG-1", "signature": "sig:run_005:first_failure"}, "status": "completed"}),
            Action(name="return_scalar", kwargs={"value": "ok"}),
        ],
        outputs=["ok"],
    ),

]
