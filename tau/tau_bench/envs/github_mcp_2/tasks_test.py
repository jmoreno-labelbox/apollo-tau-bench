from tau_bench.types import Action, Task

TASKS = [

    Task(
        annotator='0',
        user_id="task_28",
    instruction=(
"You act as 'app-developer'. In 'flutter-finance-app', assess Issue #18 along with PR #18 in conjunction with PR #26. Approve the PR with the comment: 'Please verify rendering on actual devices for iOS 14 and 15,' requesting confirmation for iOS 14/15, and label the issue as 'ios1'. Obtain the latest terminal message, then append 'flutter-finance-app iOS charts fix in validation.'")
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "app-developer"}),
            Action(name="GetRepository", kwargs={"repo_name": "flutter-finance-app"}),
            Action(name="GetIssue", kwargs={"repo_name": "flutter-finance-app", "issue_number": 18}),
            Action(name="GetPullRequest", kwargs={"repo_name": "flutter-finance-app", "pr_number": 26}),
            Action(
                name="CreatePullRequestReview",
                kwargs={
                    "repo_name": "flutter-finance-app",
                    "pr_number": 26,
                    "review_decision": "approve",
                    "comment": "Please confirm rendering on iOS 14 and 15 real devices."
                }
            ),
            Action(name="AddLabelToIssue", kwargs={"repo_name": "flutter-finance-app", "issue_number": 18, "label": "ios1"}),
            Action(name="ListTerminalLastMessage", kwargs={}),
            Action(name="AppendTerminal", kwargs={"message": "flutter-finance-app iOS charts fix under validation"}),
        ],
        outputs=['"message": "flutter-finance-app iOS charts fix under validation"'],
)

    # 45
    Task(
        annotator="0",
        user_id="task_45",
    instruction=(
        "You take on the role of 'infra-lead'. Your task is to bring about the following definitive state, with every value exact and adhering to case sensitivity: • A repository titled 'observability-ops' should be in place under your ownership; its visibility set as 'private', which you must switch to 'public', its principal branch being 'main', and it should include the topic 'kubernetes'. • A branch 'feature-initial-config' is present. On that branch, the file 'kubernetes/alertmanager.yaml' is required to contain exactly 'alertmanager: config: placeholder-v1', and the file 'kubernetes/prometheus.yaml' must have exactly 'prometheus: config: placeholder-v1'. • The most recent commit on 'feature-initial-config' includes the message 'Add initial Prometheus/Alertmanager manifests'. • Pull request # 1 targets the base 'main' from the head 'feature-initial-config' with the title 'Add initial Kubernetes monitoring stack' and content 'Bootstrap Prometheus and Alertmanager manifests.', it is approved, and has been merged. • A release exists on 'observability-ops' labeled 'v0.1.0', with the title 'Initial monitoring stack', and description 'First version of monitoring components.'. • The terminal log must include precisely one additional entry stating 'observability-ops v"
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),

            # Establish as PRIVATE according to the specifications, then change to PUBLIC after ensuring there's no redundancy.
            Action(name="CreateRepository", kwargs={
                "repo_name": "observability-ops",
                "visibility": "private",
                "default_branch": "main"
            }),
            Action(name="AddRepoTopic", kwargs={
                "repo_name": "observability-ops",
                "topic": "kubernetes"
            }),
            Action(name="SetRepositoryVisibility", kwargs={
                "repo_name": "observability-ops",
                "visibility": "public"
            }),

            # Branch, files, and commit.
            Action(name="CreateBranch", kwargs={
                "repo_name": "observability-ops",
                "source_branch": "main",
                "new_branch": "feature-initial-config"
            }),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "observability-ops",
                "branch": "feature-initial-config",
                "path": "kubernetes/alertmanager.yaml",
                "content": "alertmanager: config: placeholder-v1"
            }),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "observability-ops",
                "branch": "feature-initial-config",
                "path": "kubernetes/prometheus.yaml",
                "content": "prometheus: config: placeholder-v1"
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "observability-ops",
                "branch": "feature-initial-config",
                "commit_message": "Add initial Prometheus/Alertmanager manifests"
            }),

            # Pull request: open → approve → merge
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "observability-ops",
                "title": "Add initial Kubernetes monitoring stack",
                "body": "Bootstrap Prometheus and Alertmanager manifests.",
                "base": "main",
                "head": "feature-initial-config"
            }),
            Action(name="CreatePullRequestReview", kwargs={
                "repo_name": "observability-ops",
                "pr_number": 1,
                "review_decision": "approve"
            }),
            Action(name="MergePullRequest", kwargs={
                "repo_name": "observability-ops",
                "pr_number": 1
            }),

            # Deployment and console output
            Action(name="CreateRelease", kwargs={
                "repo_name": "observability-ops",
                "tag": "v0.1.0",
                "title": "Initial monitoring stack",
                "body": "First cut of monitoring components."
            }),
            Action(name="AppendTerminal", kwargs={
                "message": "observability-ops v0.1.0 released."
            }),
        ],
        outputs=[
            # creation verification
            '"message": "Repository created", "repo_name": "observability-ops"',
            # Confirmation of PR opened (stable substring)
            '"message": "Pull request opened", "title": "Add initial Kubernetes monitoring stack", "pr_number": 1',
            # depend on the message field to determine merge success (prevents boolean/string type conflicts)
            '"message": "Pull request merged."',
            # confirmation of release creation
            '"message": "Release created.", "repo_name": "observability-ops", "tag_name": "v0.1.0"',
            # line for terminal audit
            '"message": "observability-ops v0.1.0 released."',
        ],
    ),

    # 23
    Task(
        annotator='0',
        user_id="task_23",
    instruction=(
        "You are 'maya-w'. In 'acme-webapp', handle the reconciliation of the code scanning alert that mentions 'feature-auth' using the merged PR #5 from that branch. Check the current branches, details of PR # Retrieve 5 from the specified branch. Review the existing branches, the specifics of PR #5, and the modified files. Create an issue titled 'Reconcile alert ref: feature-auth' and apply the labels ['investigate', 'security'], including the description 'Alert references feature-auth which has been merged, but the branch is absent in the current snapshot; confirm lineage and correct metadata'. Subsequently, document this terminal entry: 'acme-webapp alert ref reconciliation recorded'.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="GetRepository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="ListBranches", kwargs={"repo_name": "acme-webapp"}),
            Action(name="ListCodeScanningAlerts", kwargs={"repo_name": "acme-webapp"}),
            Action(name="ListPullRequests", kwargs={"repo_name": "acme-webapp"}),
            Action(name="GetPullRequest", kwargs={"repo_name": "acme-webapp", "pr_number": 5}),
            Action(name="ListPullRequestFiles", kwargs={"repo_name": "acme-webapp", "pr_number": 5}),
            Action(name="CreateIssue", kwargs={
                "repo_name": "acme-webapp",
                "title": "Reconcile alert ref: feature-auth",
                "body": "Alert points to feature-auth which was merged and branch is missing in current snapshot; verify lineage and fix metadata",
                "labels": ["investigate", "security"],
            }),
            Action(name="AppendTerminal", kwargs={"message": "acme-webapp alert ref reconciliation recorded"}),
        ],
        outputs=[
            '"message": "acme-webapp alert ref reconciliation recorded"',
        ],
    ),

    # 38
    Task(
        annotator='0',
        user_id="task_38",
    instruction=(
        "You are 'maya-w'. In the repository 'acme-webapp', initiate a new issue titled 'Security triage [task_66]' with the contents 'Investigate dependency exposure paths. [task_66]'. This issue should have the label 'triage-urgent', include the precise comment 'Initial triage note recorded. [task_66]', and must be 'closed' as its final status. Confirm the label's assignment, the issue's final state, and provide a search result that verifies the presence of the issue with the label 'triage-urgent'. Additionally, record this in the terminal audit line: 'Issue closed with triage-urgent label in acme-webapp [task_66]'."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="CreateIssue", kwargs={
                "repo_name": "acme-webapp",
                "title": "Security triage [task_66]",
                "body": "Investigate dependency exposure paths. [task_66]",
                "labels": []
            }),
            Action(name="AddLabelToIssue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "label": "triage-urgent"
            }),
            Action(name="AddIssueComment", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "comment": "Initial triage note recorded. [task_66]"
            }),
            Action(name="UpdateIssue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "state": "closed"
            }),

            # Limit the search to the repository in a deterministic manner.
            Action(name="SearchIssues", kwargs={"query": "triage-urgent"}),

            # # # Retrieve complete metadata to allow outputs to feature title and labels
            # Action(identifier="GetIssue", parameters={
            # "repository_name": "acme-webapp",
            # "problem_id": 1
            # }),

            Action(name="AppendTerminal", kwargs={
                "message": "Issue closed with triage-urgent label in acme-webapp [task_66]"
            }),
        ],
        outputs=[
            '"message": "Label \'triage-urgent\' added."',
            '"state": "closed"',
            # demonstrate search hit in a deterministic manner
            '"results": [1]',
            # from get_issue — the judge requested these specifically
            # "title": "Security assessment [task_66]"
            # "labels": ["urgent-triage"],
            # line for terminal auditing
            '"message": "Issue closed with triage-urgent label in acme-webapp [task_66]"',
        ],
    ),

    # 04
    Task(
        annotator='0',
        user_id="task_04",
    instruction=(
        "You are user 'maya-w'. Examine the repository 'acme-webapp' for any pending PRs. Provide comments on PR #5 twice using feedbacks 'Looks good overall' and 'Please add more tests', then summarize your actions in the terminal with the message 'Comments added and PR # Reviewed PR #5, noted 'Looks good overall' and 'Please add more tests', then summarized actions in the terminal with 'Comments added and PR #5 reviewed.'
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="GetRepository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="ListOpenPullRequests", kwargs={"repo_name": "acme-webapp"}),
            Action(name="CommentOnPullRequest", kwargs={"repo_name": "acme-webapp", "pr_number": 5, "comment": "Looks good overall"}),
            Action(name="CommentOnPullRequest", kwargs={"repo_name": "acme-webapp", "pr_number": 5, "comment": "Please add more tests"}),
            # Action(name="FetchPullRequest", kwargs={"repository": "acme-webapp", "pull_request_id": 5}),
            Action(name="AppendTerminal", kwargs={"message": "Comments added and PR # 5 evaluated."}),
        ],
        outputs=[
            "Comments added and PR # 5 evaluated.
        ],
    ),

    # 36 (alice-w) File CRUD operations on a branch with soft deletion using empty content (Hard ~8–9 edges)
    Task(
        annotator='0',
        user_id="task_36",
    instruction=(
        "You are 'maya-w' and required to operate solely through the provided tools. Verify that the final state of the repository 'acme-webapp' meets ALL the acceptance criteria listed below. Consider these as outcomes/specifications—not step-by-step instructions. ACCEPTANCE CRITERIA (all must be satisfied): • A branch named 'file-crud' is present, originating from 'main'. • The file docs/note.txt is present on branch 'file-crud' and its final content is exactly: 'Hello v2'. • During the operation, the content 'Hello v1' was recorded in docs/note.txt and successfully read back once (include the read result in outputs). • The modification is committed with the exact commit message: 'docs(note): update to v2'. • A pull request is made from 'file-crud' into 'main' titled 'File CRUD update' with the body 'Promote CRUD change for docs/note.txt', and the PR indicates docs/note.txt as a modified file. LITERALS TO USE VERBATIM: - repo: acme-webapp - source branch: main - new branch: file-crud - path: docs/note.txt - v1 content: Hello v1 - v2 content: Hello v2 - commit message: docs(note): update to v2 - PR title: File CRUD update - PR body: Promote CRUD change for docs/note.txt"
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),

            Action(name="CreateBranch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "file-crud"
            }),

            # Instantiate (v1)
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "file-crud",
                "path": "docs/note.txt",
                "content": "Hello v1"
            }),

            # ACCESS (retrieve v1)
            Action(name="GetFileContents", kwargs={
                "repo_name": "acme-webapp",
                "branch": "file-crud",
                "path": "docs/note.txt"
            }),

            # Revision (version 2)
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "file-crud",
                "path": "docs/note.txt",
                "content": "Hello v2"
            }),

            # Commit once to capture the modification.
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "file-crud",
                "commit_message": "docs(note): update to v2"
            }),

            # Submit a pull request to ensure alignment with the depth of the domain proposal.
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "acme-webapp",
                "title": "File CRUD update",
                "body": "Promote CRUD change for docs/note.txt",
                "head": "file-crud",
                "base": "main"
            }),

            # Confirm that the PR includes the altered file.
            Action(name="ListPullRequestFiles", kwargs={
                "repo_name": "acme-webapp",
                "pr_number": 1
            }),
        ],
        outputs=[
            # originating from create_branch
            '"message": "Branch created"',
            # from retrieve_file_data (the version 1 readback)
            '"path": "docs/note.txt", "content": "Hello v1"',
            # from list_pull_request_files (verify docs/note.txt is included in the PR)
            '"docs/note.txt"',
        ],
    ),

    # 79. Terminal logs → correct script → verify PR differences (12 steps)
    Task(
        annotator='0',
        user_id="task_79",
    instruction=(
        "As a 'infra-lead', it is your role to assess a shell script amendment prior to its integration. Within the public repository 'acme-scripts', monitor modifications on a feature branch 'fix-script' derived from the 'main' branch, focusing on updates made to the script 'scripts/run.sh'. Initially, the script displays 'HELLO', with an adjustment later to also reveal 'WORLD'. During the process, capture a terminal log halfway with the message 'RUN'. After committing changes and initiating a pull request, examine both the file differences and the log results. Refer to these file content details: - Initial: '#!/usr/bin/env bash\necho HELLO\n' - Final: '#!/usr/bin/env bash\necho HELLO\necho WORLD\n' - Commit messages: 'feat: add run script' and 'fix: append WORLD echo' - PR title: 'Fix run script', body: 'Append WORLD echo to run.sh' Provide the ultimate terminal log along with the list of modified files in the PR."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),

            # Eliminate default_branch to prevent assuming an unspecified value.
            Action(name="CreateRepository", kwargs={
                "repo_name": "acme-scripts",
                "visibility": "public"
            }),

            Action(name="CreateBranch", kwargs={
                "repo_name": "acme-scripts",
                "source_branch": "main",
                "new_branch": "fix-script"
            }),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-scripts",
                "branch": "fix-script",
                "path": "scripts/run.sh",
                "content": "#!/usr/bin/env bash\necho HELLO\n"
            }),

            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-scripts",
                "branch": "fix-script",
                "commit_message": "feat: add run script"
            }),

            Action(name="AppendTerminal", kwargs={"message": "RUN"}),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-scripts",
                "branch": "fix-script",
                "path": "scripts/run.sh",
                "content": "#!/usr/bin/env bash\necho HELLO\necho WORLD\n"
            }),

            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-scripts",
                "branch": "fix-script",
                "commit_message": "fix: append WORLD echo"
            }),

            Action(name="InitializePullRequestsBlock", kwargs={"repo_name": "acme-scripts"}),

            Action(name="CreatePullRequest", kwargs={
                "repo_name": "acme-scripts",
                "title": "Fix run script",
                "body": "Append WORLD echo to run.sh",
                "head": "fix-script",
                "base": "main"
            }),

            Action(name="ListPullRequestFiles", kwargs={
                "repo_name": "acme-scripts",
                "pr_number": 1
            }),

            Action(name="ListTerminalLastMessage", kwargs={}),
        ],
        outputs=[
            # ✅ duplicate list_terminal_last_message (timestamp and message)
            '"timestamp": "2025-08-21T12:00:00Z", "message": "RUN"',
            # ✅ replicate list_pull_request_files by utilizing a substring that will be present
            '"scripts/run.sh"',
        ],
    ),

    # 39
    Task(
        annotator='0',
        user_id="task_39",
    instruction=(
        "Your task as a 'ui-developer' is to work solely with the tools at your disposal. Confirm that the 'react-dashboard' repository fulfills ALL the acceptance criteria outlined below. These should be viewed as objectives/specifications—not as procedural instructions. ACCEPTANCE CRITERIA (all conditions must be satisfied): • An issue must be present with the title 'Build pipeline audit [task_69]' and the body 'Verify CI stages and artifacts for reproducibility. [task_69]'. • This issue should bear the label 'ci-audit', incorporate the precise comment 'Checklist prepared. [task_69]', and be marked 'closed'. • It should be possible to confirm via a search that an issue with the label 'ci-audit' is available in 'react-dashboard'. • There should be a terminal log stating exactly: 'Issue closed with ci-audit label in react-dashboard [task_69]'. LITERALS TO USE VERBATIM: - repo: react-dashboard - issue title: Build pipeline audit [task_69] - issue body: Verify CI stages and artifacts for reproducibility. [task_69] - label: ci-audit - comment: Checklist prepared. [task_69] - terminal message: Issue closed with ci-audit label in react-dashboard [task_69]"
    ),
        actions=[
            # Identification
            Action(name="GetMe", kwargs={"username": "ui-developer"}),

            # Generate a consistent issue (single row).
            Action(
                name="CreateIssue",
                kwargs={
                    "repo_name": "react-dashboard",
                    "title": "Build pipeline audit [task_69]",
                    "body": "Verify CI stages and artifacts for reproducibility. [task_69]",
                    "labels": []
                },
            ),

            # Assign label and add comment.
            Action(
                name="AddLabelToIssue",
                kwargs={"repo_name": "react-dashboard", "issue_number": 1, "label": "ci-audit"},
            ),
            Action(
                name="AddIssueComment",
                kwargs={
                    "repo_name": "react-dashboard",
                    "issue_number": 1,
                    "comment": "Checklist prepared. [task_69]"
                },
            ),

            # Resolve the issue
            Action(
                name="UpdateIssue",
                kwargs={"repo_name": "react-dashboard", "issue_number": 1, "state": "closed"},
            ),

            # Proof of deterministic search (limited to repository)
            Action(
                name="SearchIssues",
                kwargs={"query": "ci-audit"},
            ),

            # Final examination
            Action(
                name="AppendTerminal",
                kwargs={"message": "Issue closed with ci-audit label in react-dashboard [task_69]"},
            ),
        ],
        outputs=[
            '"message": "Label \'ci-audit\' added."',
            '"state": "closed"',
            '"results": [1]',
            '"message": "Issue closed with ci-audit label in react-dashboard [task_69]"',
        ],
    ),

    # 32 (alice-w) acme-webapp: generate, tag, annotate, resolve an issue; verify the last command input.
    Task(
        annotator='0',
        user_id="task_32",
    instruction=(
        "Operate as 'maya-w' using solely the available tools. Confirm that the final state of the repository 'acme-webapp' meets ALL the acceptance criteria detailed below. Consider these as outcomes/specification—not procedural instructions. ACCEPTANCE CRITERIA (all must be satisfied): • An issue is present titled 'Nightly job failed on main' with the body \"CI job 'nightly-build' failed due to timeout.\". • The issue possesses the label 'ops', includes the precise comment 'Investigating: rerun queued.', and is in the 'closed' state. • The latest terminal log is specifically: 'Issue #1 closed: Nightly job failed on main'. LITERALS TO USE VERBATIM: - repo: acme-webapp - issue title: Nightly job failed on main - issue body: CI job 'nightly-build' failed due to timeout. - label to add: ops - issue comment: Investigating: rerun queued. - terminal message: Issue # 1 closed: Nightly job on main encountered failure. - repo: acme-webapp - issue title: Nightly job failed on main - issue body: CI job 'nightly-build' failed due to timeout. - label to add: ops - issue comment: Investigating: rerun queued. - terminal message: Issue #1 closed: Nightly job failed on main
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="CreateIssue", kwargs={
                "repo_name": "acme-webapp",
                "title": "Nightly job failed on main",
                "body": "CI job 'nightly-build' failed due to timeout."
            }),
            Action(name="AddLabelToIssue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "label": "ops"
            }),
            Action(name="AddIssueComment", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "comment": "Investigating: rerun queued."
            }),
            Action(name="UpdateIssue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "state": "closed"
            }),
            Action(name="AppendTerminal", kwargs={
                "message": "Issue # 1 closed: Nightly task encountered an error on main.
            }),
            Action(name="ListTerminalLastMessage", kwargs={}),
        ],
        outputs=[
            # from generate_issue
            '"message": "Issue created", "number": 1',
            # from attach_label_to_issue
            '"message": "Label \'ops\' added."',
            # from list_terminal_recent_message (utilizes timestamp and message)
            '"timestamp": "2025-08-21T12:00:00Z", "message": "Issue # 1 closed: Nightly task unsuccessful on main.
        ],
    ),

    # 78
    Task(
        annotator='0',
        user_id="task_78",
    instruction=(
        "Act as 'security-group' and engage only via the available tools. Verify that the ending state of the repository 'security-scanner' fulfills ALL the acceptance criteria outlined below. These should be seen as outcomes/specification—not step-by-step directives. ACCEPTANCE CRITERIA (all conditions must be met): • A branch named 'sec-checks' has been created, branching from the default branch. • Within that branch, ensure the file '.github/workflows/security.yml' is present and its contents are exactly: on: [push] jobs: scan: runs-on: ubuntu-latest steps: - name: Security scan run: echo SCAN • The commit message is: 'chore: add security workflow'. • A pull request exists with the title 'Add security workflow' and the body 'Adds a basic GitHub Actions scan workflow.' from 'sec-checks' into the default branch. • Outputs should comprise the list of files changed in that pull request and any open code scanning alerts bearing the 'critical' severity. LITERALS TO USE VERBATIM: - repo: security-scanner - branch: sec-checks - path: .github/workflows/security.yml - workflow content: on: [push]\njobs:\n scan:\n runs-on: ubuntu-latest\n steps:\n - name: Security scan\n run: echo SCAN - commit message: chore: add security workflow - PR title: Add security workflow - PR body: Adds a basic GitHub Actions scan workflow. - severity: critical"
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "security-group"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "security-scanner"}),

            Action(name="CreateBranch", kwargs={
                "repo_name": "security-scanner",
                "source_branch": "main",
                "new_branch": "sec-checks"
            }),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "security-scanner",
                "branch": "sec-checks",
                "path": ".github/workflows/security.yml",
                "content": "on: [push]\njobs:\n  scan:\n    runs-on: ubuntu-latest\n    steps:\n      - name: Security scan\n        run: echo SCAN"
            }),

            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "security-scanner",
                "branch": "sec-checks",
                "commit_message": "chore: add security workflow"
            }),

            Action(name="CreatePullRequest", kwargs={
                "repo_name": "security-scanner",
                "title": "Add security workflow",
                "body": "Adds a basic GitHub Actions scan workflow.",
                "head": "sec-checks",
                "base": "main"
            }),

            Action(name="ListPullRequestFiles", kwargs={
                "repo_name": "security-scanner",
                "pr_number": 1
            }),

            Action(name="ListCodeScanningAlerts", kwargs={
                "repo_name": "security-scanner",
                "severity": "critical"
            }),
        ],
        outputs=[
            # modified files list
            '".github/workflows/security.yml"',
            # important code analysis warning (sample format)
            '"severity": "critical"',
        ],
    ),

    # 83
    Task(
        annotator='0',
        user_id="task_83",
    instruction=(
        "You are maya-w. Within the 'acme-webapp' repository, initiate a branch titled 'feature-codeowners' stemming from the default branch. Introduce a file at the location '.github/CODEOWNERS' with the precise content: * @alice-w src/ @dev-sue tests/ @qa-mike Submit this file with the commit message 'chore: add CODEOWNERS'. Subsequently, set up a pull request to merge 'feature-codeowners' into the default branch with the title 'Add CODEOWNERS' and the body 'CODEOWNERS file added for ownership mapping.'. Add a pull request review comment stating 'Please review CODEOWNERS ownership setup.' Lastly, provide the list of files changed in that PR."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "acme-webapp"}),
            Action(
                name="CreateBranch",
                kwargs={"repo_name": "acme-webapp", "new_branch": "feature-codeowners", "source_branch": "main"},
            ),
            Action(
                name="WriteFileToBranch",
                kwargs={
                    "repo_name": "acme-webapp",
                    "branch": "feature-codeowners",
                    "path": ".github/CODEOWNERS",
                    "content": "* @alice-w\nsrc/ @dev-sue\ntests/ @qa-mike\n",
                },
            ),
            Action(
                name="CommitChangesToBranch",
                kwargs={"repo_name": "acme-webapp", "branch": "feature-codeowners", "commit_message": "chore: add CODEOWNERS"},
            ),
            Action(
                name="CreatePullRequest",
                kwargs={
                    "repo_name": "acme-webapp",
                    "title": "Add CODEOWNERS",
                    "body": "CODEOWNERS file added for ownership mapping.",
                    "head": "feature-codeowners",
                    "base": "main",
                },
            ),
            Action(
                name="CreatePullRequestReview",
                kwargs={
                    "repo_name": "acme-webapp",
                    "pr_number": 1,
                    "review_decision": "comment",
                    "body": "Please review CODEOWNERS ownership setup.",
                },
            ),
            Action(
                name="ListPullRequestFiles",
                kwargs={
                    "repo_name": "acme-webapp",
                    "pr_number": 1,
                },
            ),
        ],
        outputs=['{"files": [".github/CODEOWNERS"]}'],
    ),

    # 40 (alice-w) Initiate PR -> Revoke PR by removing head branch (Difficult ~12–13 edges)
    Task(
        annotator='0',
        user_id="task_40",
    instruction=(
        "You are 'maya-w' and must manage tasks solely through the provided tools. Verify that the final repository condition in 'acme-webapp' meets ALL the acceptance criteria outlined below. Consider these as outcomes/specification—not a step-by-step process. ACCEPTANCE CRITERIA (all must be met): • A feature branch called 'temp-pr' is established from the default branch and holds a file located at 'docs/pr_demo.txt' with the content precisely: 'temporary PR'. • A pull request is present titled 'Temp PR demo' with the body 'Demonstration of temporary PR lifecycle.' originating from head 'temp-pr' into the default branch. • The pull request is subsequently canceled by removing its head branch: the branch 'temp-pr' is no longer present. • A terminal log is created containing the message exactly: 'PR Temp PR demo withdrawn in acme-webapp.'. • Return the pull request title in outputs. LITERALS TO USE VERBATIM: - repo: acme-webapp - base branch: main - head branch: temp-pr - path: docs/pr_demo.txt - file content: temporary PR - PR title: Temp PR demo - PR body: Demonstration of temporary PR lifecycle. - terminal message: PR Temp PR demo withdrawn in acme-webapp."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),

            Action(name="CreateBranch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "temp-pr"
            }),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "temp-pr",
                "path": "docs/pr_demo.txt",
                "content": "temporary PR"
            }),

            Action(name="CreatePullRequest", kwargs={
                "repo_name": "acme-webapp",
                "title": "Temp PR demo",
                "body": "Demonstration of temporary PR lifecycle.",
                "head": "temp-pr",
                "base": "main"
            }),

            Action(name="DeleteBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "temp-pr"
            }),

            Action(name="AppendTerminal", kwargs={
                "message": "PR Temp PR demo withdrawn in acme-webapp."
            }),
        ],
        outputs=[
            '"title": "Temp PR demo"'
        ],
    ),

    # 43
    Task(
        annotator='0',
        user_id="task_43",
    instruction=(
        "Act as 'ryan-dev'. Within the 'utils-js' repository, generate a new issue named 'Utilities module audit [task_73]' including the body 'Review currency formatting and TypeScript support. [task_73]'. Ensure the issue bears the label 'module-audit', contains the exact comment 'Audit completed. [task_73]', and its final status is 'closed'. Provide verification of the label application, the issue's concluding status, and a search result entry confirming an issue with the label 'module-audit' is present. Incorporate this terminal audit statement: 'Issue closed with module-audit label in utils-js [task_73]'."
    ),
        actions=[
            # Identification
            Action(name="GetMe", kwargs={"username": "ryan-dev"}),

            # Generate a reproducible issue.
            Action(
                name="CreateIssue",
                kwargs={
                    "repo_name": "utils-js",
                    "title": "Utilities module audit [task_73]",
                    "body": "Review currency formatting and TypeScript support. [task_73]",
                    "labels": []
                },
            ),

            # Add label and annotation.
            Action(
                name="AddLabelToIssue",
                kwargs={"repo_name": "utils-js", "issue_number": 1, "label": "module-audit"},
            ),
            Action(
                name="AddIssueComment",
                kwargs={
                    "repo_name": "utils-js",
                    "issue_number": 1,
                    "comment": "Audit completed. [task_73]"
                },
            ),

            # Resolve the issue.
            Action(
                name="UpdateIssue",
                kwargs={"repo_name": "utils-js", "issue_number": 1, "state": "closed"},
            ),

            # Demonstrate through a search (returns issue ID(s))
            Action(
                name="SearchIssues",
                kwargs={"query": "module-audit"},
            ),

            # Retrieve complete metadata (title + labels) for the outputs.
            Action(
                name="GetIssue",
                kwargs={"repo_name": "utils-js", "issue_number": 1},
            ),

            # Conduct a terminal audit and validate the final entry to ensure the output aligns with the tool's response.
            Action(
                name="AppendTerminal",
                kwargs={"message": "Issue closed with module-audit label in utils-js [task_73]"},
            ),
            Action(
                name="ListTerminalLastMessage",
                kwargs={},
            ),
        ],
        outputs=[
            # label assigned
            '"message": "Label \'module-audit\' added."',
            # ultimate condition
            '"state": "closed"',
            # validate search (search_issues generally yields a list of numeric results; utilizing the precise substring)
            '"results": [1]',
            # retrieved metadata confirming title and labels
            '"title": "Utilities module audit [task_73]"',
            '"labels": ["module-audit"]',
            # audit line for terminal from list_terminal_last_message
            '"message": "Issue closed with module-audit label in utils-js [task_73]"',
        ],
    ),

    # 82. (ui-team) Generate branch -> Commit changes -> Submit PR -> Validation rejection -> Log activity
    Task(
        annotator='0',
        user_id="task_82",
    instruction=(
        "Operate as 'design-team' exclusively using the designated tools. Guarantee the ultimate repository state in 'ui-kit' meets ALL acceptance criteria detailed below, treating these as specification outcomes, not procedural steps. ACCEPTANCE CRITERIA (all criteria must be fulfilled): • Existence of a branch named 'feature-validate' that diverges from 'main' by appending a file at path 'docs/validation.md' with content precisely: 'Validation test: head==base should not merge.'. • Presence of a commit on 'feature-validate' with the exact message: 'Add docs/validation.md for merge validation test'. • A pull request #1 present in repository 'ui-kit' titled 'Validate merge blocking when head==base' with body 'This PR intentionally uses the same branch for head and base to verify merge validation.', both head and base on 'feature-validate'. • Rejection of an attempt to merge the pull request, with message 'Pull request rejected.' citing 'head and base branch are the same', alongside a false merged indicator. • An ending entry containing the specific message: 'PR #1 rejected in ui-kit: head equals base (validation).' STRINGS TO USE EXACTLY: - repo: ui-kit - source branch: main - working branch: feature-validate - path: docs/validation.md - file content: Validation test: head==base should not merge. - commit message: Add docs/validation.md for merge validation test - PR number: 1 - PR title: Validate merge blocking when head==base - PR body: This PR intentionally uses the same branch for head and base to verify merge validation. - terminal message: PR # This pull request uses the same branch for both head and base to test merge validation. An attempt to merge was rejected with the message 'Pull request rejected.' stating 'head and base branch are the same,' despite showing a false merged status. The final entry notes: 'PR #1 rejected in ui-kit: head equals base (validation).'
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "design-team"}),
            Action(name="GetRepository", kwargs={"repo_name": "ui-kit"}),

            Action(name="CreateBranch", kwargs={
                "repo_name": "ui-kit",
                "source_branch": "main",
                "new_branch": "feature-validate"
            }),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "ui-kit",
                "branch": "feature-validate",
                "path": "docs/validation.md",
                "content": "Validation test: head==base should not merge."
            }),

            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "ui-kit",
                "branch": "feature-validate",
                "commit_message": "Add docs/validation.md for merge validation test"
            }),

            Action(name="CreatePullRequest", kwargs={
                "repo_name": "ui-kit",
                "title": "Validate merge blocking when head==base",
                "body": "This PR intentionally uses the same branch for head and base to verify merge validation.",
                "base": "feature-validate",
                "head": "feature-validate"
            }),

            Action(name="MergePullRequest", kwargs={
                "repo_name": "ui-kit",
                "pr_number": 1
            }),

            Action(name="AppendTerminal", kwargs={
                "message": "PR # 1 rejected in ui-kit: head matches base (validation).
            }),
        ],
        outputs=[
            # Utilize boolean "false" to align with the tool output for merge_pull_request rejection.
            '"message": "Pull request rejected."',
            '"reason": "head and base branch are the same"',
            '"merged": "false"',
        ],
    ),

    # 80
    Task(
        annotator='0',
        user_id="task_80",
    instruction=(
        "As 'maya-w', work solely utilizing the tools provided. Ensure the ultimate condition of the repository 'acme-webapp' meets ALL acceptance criteria below; these should be viewed as outcomes/specification, not as step-by-step instructions. ACCEPTANCE CRITERIA (all must be fulfilled): • An open issue exists with the title 'Fix crash on startup' and content 'Application crashes due to missing env var check', that tracks the application startup crash. • The default branch contains a branch called 'fix-startup', and 'src/main.py' includes the line: 'assert ENV_VAR is not None'. This change is committed with the message 'fix: guard against missing ENV_VAR'. • A pull request has been initiated from 'fix-startup' to the default branch, titled 'Fix startup crash', with content 'Adds env var guard clause', and this pull request is merged. • Provide the issue metadata and the pull request title in outputs. LITERALS TO USE VERBATIM: - repo: acme-webapp - issue title: Fix crash on startup - issue body: Application crashes due to missing env var check - branch: fix-startup - path: src/main.py - code line: assert ENV_VAR is not None - commit message: fix: guard against missing ENV_VAR - PR title: Fix startup crash - PR body: Adds env var guard clause"
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),

            Action(name="CreateIssue", kwargs={
                "repo_name": "acme-webapp",
                "title": "Fix crash on startup",
                "body": "Application crashes due to missing env var check"
            }),

            Action(name="GetDefaultBranch", kwargs={"repo_name": "acme-webapp"}),

            Action(name="CreateBranch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "fix-startup"
            }),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "fix-startup",
                "path": "src/main.py",
                "content": "assert ENV_VAR is not None"
            }),

            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "fix-startup",
                "commit_message": "fix: guard against missing ENV_VAR"
            }),

            Action(name="CreatePullRequest", kwargs={
                "repo_name": "acme-webapp",
                "title": "Fix startup crash",
                "body": "Adds env var guard clause",
                "head": "fix-startup",
                "base": "main"
            }),

            Action(name="MergePullRequest", kwargs={
                "repo_name": "acme-webapp",
                "pr_number": 1
            }),

            # Retrieve issue metadata for output purposes.
            Action(name="GetIssue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1
            }),
        ],
        outputs=[
            # Retain outputs as substrings found in real tool responses.
            '"number": 1',
            '"title": "Fix crash on startup"',
            '"state": "open"',
            '"title": "Fix startup crash"',
        ],
    ),

    # 44
    Task(
        annotator='0',
        user_id="task_44",
    instruction=(
        "Act as 'design-team'. In the 'ui-kit' repository, there needs to be a pull request #11 entitled 'Introduce Theme Provider'. Submit the precise review comment 'Theme reviewed. [task_74]' on it, then approve and merge it. Provide the PR number, its final status 'merged', and a terminal entry that reads 'PR # 11 titled 'Introduce Theme Provider'. Add the exact review comment 'Theme reviewed. [task_74]' to it, then approve and merge. Include the PR number, its final status 'merged', and a terminal entry stating 'PR #11 merged with review in ui-kit [task_74]'.
    ),
        actions=[
            # Identification
            Action(name="GetMe", kwargs={"username": "design-team"}),

            # Fetch pull request
            Action(name="GetPullRequest", kwargs={"repo_name": "ui-kit", "pr_number": 11}),

            # Authorize the review (including the necessary comment).
            Action(
                name="CreatePullRequestReview",
                kwargs={
                    "repo_name": "ui-kit",
                    "pr_number": 11,
                    "review_decision": "approve",
                    "comment": "Theme reviewed. [task_74]"
                },
            ),

            # Combine pull request.
            Action(
                name="MergePullRequest",
                kwargs={"repo_name": "ui-kit", "pr_number": 11},
            ),

            # Command line output
            Action(
                name="AppendTerminal",
                kwargs={"message": "PR # 11 combined with review in ui-kit [task_74]
            ),
        ],
        outputs=[
            '"pr_number": 11',
            '"state": "merged"',
            '"message": "PR # 11 integrated with review in ui-kit [task_74]
        ],
    ),

    # 58
    Task(
        annotator='0',
        user_id="task_58",
    instruction=(
        "As 'server-main', you're required to finalize tasks on the repository state for 'payments-service', ensuring ALL of the following conditions are met: • There must be a documentation file located at 'docs/RETRY_POLICY.md' on the 'main' branch, containing the PRECISE text 'Retries: up to 2 attempts with exponential backoff starting at 250ms. Idempotency required for POST.'. • This revision should start from a branch named 'feature-retry-policy' and be represented by a commit whose message is EXACTLY 'Add retry policy documentation'. • Ensure the modification is introduced into 'main' through a reviewed pull request titled 'Add retry policy docs'; a review request must be sent to 'qa-erin', and an approving review with the exact comment 'LGTM' should be recorded. • A release tagged as 'v0.3.0', titled 'Retry policy docs', and with the body 'Publish retry policy documentation.' must exist, with the latest release showing tag 'v0.3.0'. • An issue must exist with the title 'Retry policy published' and body 'Docs merged and released as v0.3.0.' carrying the label 'documentation'. • The terminal audit log must contain the EXACT entry 'payments-service retry policy docs published and released as v0.3.0.'."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "server-main"}),
            Action(name="GetRepository", kwargs={"repo_name": "payments-service"}),
            Action(name="CreateBranch", kwargs={"repo_name": "payments-service", "source_branch": "main", "new_branch": "feature-retry-policy"}),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "payments-service",
                "branch": "feature-retry-policy",
                "path": "docs/RETRY_POLICY.md",
                "content": "Retries: up to 2 attempts with exponential backoff starting at 250ms. Idempotency required for POST."
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "payments-service",
                "branch": "feature-retry-policy",
                "commit_message": "Add retry policy documentation"
            }),
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "payments-service",
                "title": "Add retry policy docs",
                "base": "main",
                "head": "feature-retry-policy"
            }),
            Action(name="RequestPullRequestReviewers", kwargs={
                "repo_name": "payments-service",
                "pr_number": 1,
                "reviewers": ["qa-erin"]
            }),
            Action(name="CreatePullRequestReview", kwargs={
                "repo_name": "payments-service",
                "pr_number": 1,
                "review_decision": "approve",
                "comment": "LGTM"
            }),
            Action(name="MergePullRequest", kwargs={"repo_name": "payments-service", "pr_number": 1}),
            Action(name="CreateRelease", kwargs={
                "repo_name": "payments-service",
                "tag": "v0.3.0",
                "title": "Retry policy docs",
                "body": "Publish retry policy documentation."
            }),
            Action(name="GetLatestRelease", kwargs={"repo_name": "payments-service"}),
            Action(name="CreateIssue", kwargs={
                "repo_name": "payments-service",
                "title": "Retry policy published",
                "body": "Docs merged and released as v0.3.0.",
                "labels": ["documentation"]
            }),
            Action(name="AppendTerminal", kwargs={
                "message": "payments-service retry policy docs published and released as v0.3.0."
            }),
        ],
        outputs=[
            '"message": "Branch created", "new_branch": "feature-retry-policy", "from": "main"',
            '"message": "Committed to branch", "repo": "payments-service", "branch": "feature-retry-policy", "commit_sha": "sha_0000000000000000000000000000000000000000"',
            '"message": "Pull request opened", "title": "Add retry policy docs", "base": "main", "head": "feature-retry-policy", "pr_number": 1',
            '"message": "Reviewers requested.", "pr_number": 1',
            '"message": "Review submitted."',
            '"message": "Pull request merged.", "merged": "true", "merge_method": "merge"',
            '"message": "Release created.", "repo_name": "payments-service", "tag_name": "v0.3.0", "title": "Retry policy docs"',
            '"tag_name": "v0.3.0", "body": "Publish retry policy documentation."',
            '"message": "Issue created", "number": 1',
            '"printed_ts": "2025-08-21T12:00:00Z", "message": "payments-service retry policy docs published and released as v0.3.0."',
        ],
    ),

    # 08
    Task(
        annotator='0',
        user_id="task_08",
    instruction=(
        "You hold the role of 'infra-lead'. Within 'k8s-monitoring', confirm the default branch and merely list the commits in branch 'upgrade-prometheus'. Check open alerts by listing them to ensure Alert #45 remains open; subsequently, initiate an issue titled 'Harden TLS for Prometheus scrape' with labels ['security','prometheus'] and body: 'Alert # Issue 45 is still unresolved; therefore, create a new issue called 'Harden TLS for Prometheus scrape' with labels ['security','prometheus'] and the description: 'Alert #45 remains active after the v2.45.0 upgrade; implement updated ciphers and TLS versions.'. Append to the terminal: 'k8s-monitoring TLS hardening tracked after upgrade.'.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
            Action(name="GetRepository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="ListCommits", kwargs={"repo_name": "k8s-monitoring", "branch": "upgrade-prometheus"}),
            Action(name="ListCodeScanningAlerts", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="CreateIssue", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Harden TLS for Prometheus scrape",
                "body": "Alert # 45 remains accessible post v2.45.0 upgrade; mandate contemporary ciphers and TLS versions.
                "labels": ["security", "prometheus"],
            }),
            Action(name="AppendTerminal", kwargs={"message": "k8s-monitoring TLS hardening tracked post-upgrade"}),
        ],
        outputs=['"message": "k8s-monitoring TLS hardening tracked post-upgrade"'],
    ),

    # 84
    Task(
        annotator='0',
        user_id="task_84",
    instruction=(
        "Your task is 'server-main'. Within 'payments-service', synchronize PR #21 with Issue #13 (3DS). Examine the repository, the issue, and the PR, and detail any existing code scanning alerts. Tag Issue #13 with 'needs-tests', comment as follows: 'PR # Review repository, issue, and PR for code scanning alerts related to Issue #13 (3DS). Label Issue #13 with 'needs-tests' and comment: 'PR #21 implements 3DS; please add unit tests for fallback coverage prior to merging.' Provide a PR review with 'request_changes' and add the comment: 'Unit tests for 3DS fallback flows are required.' End with: 'payments-service 3DS alignment and test gating acknowledged.'
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "server-main"}),
            Action(name="GetRepository", kwargs={"repo_name": "payments-service"}),
            Action(name="GetIssue", kwargs={"repo_name": "payments-service", "issue_number": 13}),
            Action(name="GetPullRequest", kwargs={"repo_name": "payments-service", "pr_number": 21}),
            Action(name="ListCodeScanningAlerts", kwargs={"repo_name": "payments-service"}),
            Action(name="AddLabelToIssue", kwargs={"repo_name": "payments-service", "issue_number": 13, "label": "needs-tests"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "payments-service", "issue_number": 13, "comment": "PR # 21 integrates 3DS; include unit tests for fallback coverage prior to merging.
            Action(
                name="CreatePullRequestReview",
                kwargs={
                    "repo_name": "payments-service",
                    "pr_number": 21,
                    "review_decision": "request_changes",
                    "comment": "Please include unit tests for 3DS fallback flows."
                },
            ),
            Action(name="AppendTerminal", kwargs={"message": "payments-service 3DS alignment and test gating noted"}),
        ],
        outputs=['"message": "payments-service 3DS alignment and test gating noted"'],
    ),

    # 60
    Task(
        annotator='0',
        user_id="task_60",
    instruction=(
        "Your role is 'design-team'. Make sure that once your task is finalized, the 'ui-kit' repository should uphold ALL the following conditions: • A documentation file is present at 'docs/ACCESSIBILITY.md' containing the EXACT text 'All UI components must meet WCAG 2.1 AA. Provide ARIA labels for interactive elements. Keyboard navigation required.'. • The update starts from a branch known as 'feature-accessibility-docs' and is documented by a commit with the EXACT message 'Add accessibility documentation'. • This update is integrated into 'main' through a reviewed pull request titled 'Accessibility docs'; a review is requested from 'design-lead', and an approval review with the precise comment 'Approved for accessibility' is cataloged. • The repository is tagged with the subject 'accessibility'. • A release is marked with tag 'v2.0.0', title 'Accessibility docs', and a body that states 'Add accessibility documentation.', with the most recent release showing tag 'v2.0.0'. • There exists an issue termed 'Accessibility docs published' with the content 'Docs merged and released as v2.0.0.' tagged 'documentation'. • The terminal audit log has the EXACT note 'ui-kit accessibility docs published and released as v2.0.0.'."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "design-team"}),
            Action(name="GetRepository", kwargs={"repo_name": "ui-kit"}),
            Action(name="CreateBranch", kwargs={"repo_name": "ui-kit", "source_branch": "main", "new_branch": "feature-accessibility-docs"}),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "ui-kit",
                "branch": "feature-accessibility-docs",
                "path": "docs/ACCESSIBILITY.md",
                "content": "All UI components must meet WCAG 2.1 AA. Provide ARIA labels for interactive elements. Keyboard navigation required."
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "ui-kit",
                "branch": "feature-accessibility-docs",
                "commit_message": "Add accessibility documentation"
            }),
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "ui-kit",
                "title": "Accessibility docs",
                "base": "main",
                "head": "feature-accessibility-docs"
            }),
            Action(name="RequestPullRequestReviewers", kwargs={
                "repo_name": "ui-kit",
                "pr_number": 1,
                "reviewers": ["design-lead"]
            }),
            Action(name="CreatePullRequestReview", kwargs={
                "repo_name": "ui-kit",
                "pr_number": 1,
                "review_decision": "approve",
                "comment": "Approved for accessibility"
            }),
            Action(name="MergePullRequest", kwargs={"repo_name": "ui-kit", "pr_number": 1}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "ui-kit", "topic": "accessibility"}),
            Action(name="CreateRelease", kwargs={
                "repo_name": "ui-kit",
                "tag": "v2.0.0",
                "title": "Accessibility docs",
                "body": "Add accessibility documentation."
            }),
            Action(name="GetLatestRelease", kwargs={"repo_name": "ui-kit"}),
            Action(name="CreateIssue", kwargs={
                "repo_name": "ui-kit",
                "title": "Accessibility docs published",
                "body": "Docs merged and released as v2.0.0.",
                "labels": ["documentation"]
            }),
            Action(name="AppendTerminal", kwargs={"message": "ui-kit accessibility docs published and released as v2.0.0."}),
        ],
        outputs=[
            '"message": "Branch created", "new_branch": "feature-accessibility-docs", "from": "main"',
            '"message": "Committed to branch", "repo": "ui-kit", "branch": "feature-accessibility-docs", "commit_sha": "sha_0000000000000000000000000000000000000000"',
            '"message": "Pull request opened", "title": "Accessibility docs", "base": "main", "head": "feature-accessibility-docs", "pr_number": 1',
            '"message": "Reviewers requested.", "pr_number": 1',
            '"message": "Review submitted."',
            '"message": "Pull request merged.", "merged": "true", "merge_method": "merge"',
            '"message": "Topic \'accessibility\' added."',
            '"message": "Release created.", "repo_name": "ui-kit", "tag_name": "v2.0.0", "title": "Accessibility docs"',
            '"tag_name": "v2.0.0", "body": "Add accessibility documentation."',
            '"message": "Issue created", "number": 1',
            '"printed_ts": "2025-08-21T12:00:00Z", "message": "ui-kit accessibility docs published and released as v2.0.0."',
        ],
    ),

    # 34 (alice-w) acme-webapp: generate and prioritize an issue, followed by recording its resolution.
    Task(
        annotator='0',
        user_id="task_34",
    instruction=(
        "You are 'maya-w' and must function only through the specified tools. YOUR OBJECTIVE • In repository 'acme-webapp', make an issue utilizing the exact title and body literals, apply the exact label literal, insert the exact comment literal, finalize the issue, and confirm the most recent terminal entry is identical to the exact message literal. LITERALS (use verbatim) - repo: acme-webapp - issue title: CI gate: add test matrix - issue body: Add unit + integration test matrix - label to add: ready-for-ci - comment to post: Triage complete: scheduled for CI gate - terminal message: Issue # 1 resolved in acme-webapp: CI readiness triage finished
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),

            # Generate an issue, assign a label, add a comment, and then close it.
            Action(name="CreateIssue", kwargs={
                "repo_name": "acme-webapp",
                "title": "CI gate: add test matrix",
                "body": "Add unit + integration test matrix"
            }),
            Action(name="AddLabelToIssue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "label": "ready-for-ci"
            }),
            Action(name="AddIssueComment", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "comment": "Triage complete: scheduled for CI gate"
            }),
            Action(name="UpdateIssue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "state": "closed"
            }),

            # Add terminal confirmation and ensure it's the most recent.
            Action(name="AppendTerminal", kwargs={
                "message": "Issue # 1 resolved in acme-webapp: CI triage finalized
            }),
            Action(name="ListTerminalLastMessage", kwargs={}),
        ],
        outputs=[
            '"message": "Issue created", "number": 1',
            '"message": "Label \'ready-for-ci\' added."',
            '"entries": {"printed_ts": "2025-08-21T12:00:00Z", "message": "Issue # 1 resolved in acme-webapp: CI readiness triage finished"}',
        ],
    ),

    # 91. (security-team) Minimize XSS false alarms → PR integrated → issue resolved → release + note
    Task(
        annotator='0',
        user_id="task_91",
    instruction=(
        "You are 'security-group' tasked with working in repository 'security-scanner'. Implement an XSS rule modification ensuring that, once completed, the repository state meets ALL acceptance criteria outlined below, utilizing the exact constants provided. View this as a specification of outcomes and literals, NOT a step-by-step process. ACCEPTANCE CRITERIA (final state must reflect all of these): • A feature branch is created containing a relaxed XSS rule to minimize false positives on template literals. • Close issue number 5. • Merge a pull request (number 1 after reset for this repo) into the default branch. • Ensure a release with the exact tag below is present. • The closed issue comprises the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: fix-xss-false-positives - Base branch name: main - File path: rules/xss/relaxed-template-rule.yml - File content (exact; SINGLE trailing newline only): id: xss-template-relaxed severity: medium pattern: disallow-unsafe-innerHTML allow_template_literals: true - Commit message: fix(xss): relax rule for template literals to reduce false positives - Issue to label and close: 5 - Label to add: xss - Pre-PR issue comment: Relaxing XSS rule for template literals; PR will close this issue. - PR title: Relax XSS rule to reduce false positives on template literals - PR body: Closes # 5 - Pull request review status: approved - Release version: v1.3.1-xss-fp - Post-release issue note: Resolved in 'v1.3.1-xss-fp' (decreased false positives)
    ),
        actions=[
            # Authentication and repository context
            Action(name="GetMe", kwargs={"username": "security-group"}),
            Action(name="GetRepository", kwargs={"repo_name": "security-scanner"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "security-scanner"}),
            Action(name="GetHeadSha", kwargs={"repo_name": "security-scanner", "branch": "main"}),

            # Feature branch for development.
            Action(name="CreateBranch", kwargs={"repo_name": "security-scanner", "new_branch": "fix-xss-false-positives", "source_branch": "main"}),

            # Modify the changes on the feature branch.
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "security-scanner",
                "branch": "fix-xss-false-positives",
                "path": "rules/xss/relaxed-template-rule.yml",
                "content": "id: xss-template-relaxed\nseverity: medium\npattern: disallow-unsafe-innerHTML\nallow_template_literals: true\n",
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "security-scanner",
                "branch": "fix-xss-false-positives",
                "commit_message": "fix(xss): relax rule for template literals to reduce false positives",
            }),

            # Work existing issue # Resolve the current issue #5 in a deterministic manner.
            Action(name="AddLabelToIssue", kwargs={"repo_name": "security-scanner", "issue_number": 5, "label": "xss"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "security-scanner", "issue_number": 5, "comment": "Relaxing XSS rule for template literals; PR will close this issue."}),

            # Pull request from feature branch to main branch.
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "security-scanner",
                "title": "Relax XSS rule to reduce false positives on template literals",
                "body": "Closes # 5 inches,
                "head": "fix-xss-false-positives",
                "base": "main",
            }),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "security-scanner", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "security-scanner", "pr_number": 1}),

            # Explicitly resolve the issue.
            Action(name="UpdateIssue", kwargs={"repo_name": "security-scanner", "issue_number": 5, "state": "closed"}),

            # Publish and document the issue.
            Action(name="CreateRelease", kwargs={"repo_name": "security-scanner", "tag": "v1.3.1-xss-fp"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "security-scanner", "issue_number": 5, "comment": "Fixed in 'v1.3.1-xss-fp' (reduced false positives)"}),
        ],
        outputs=[
            '"repo_name": "security-scanner"',
            '"pr_number": 1, "closed_issue": 5, "release_tag": "v1.3.1-xss-fp"',
        ],
    ),










































    # 01. (ui-team) Secure the main function and log an audit entry (avoid duplicate calls)
    Task(
        annotator='0',
        user_id="task_01",
    instruction=(
        "You belong to 'design-team'. Validate that the 'main' branch of 'ui-kit' is safeguarded and verify its current protection status. Document the modification by creating an audit issue titled 'Protect main branch' with body 'Branch protection for main enabled.' and label 'ops', and record the precise terminal entry 'Branch main protection enabled in ui-kit.'"
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "design-team"}),
            Action(name="GetRepository", kwargs={"repo_name": "ui-kit"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "ui-kit"}),
            Action(name="SetBranchProtection", kwargs={"repo_name": "ui-kit", "branch": "main", "protected": True}),
            Action(name="GetBranchProtection", kwargs={"repo_name": "ui-kit", "branch": "main"}),
            Action(
                name="CreateIssue",
                kwargs={
                    "repo_name": "ui-kit",
                    "title": "Protect main branch",
                    "body": "Branch protection for main enabled.",
                    "labels": ["ops"],
                },
            ),
            Action(name="AppendTerminal", kwargs={"message": "Branch main protection enabled in ui-kit."}),
        ],
        outputs=[
            '"message": "Branch protection enabled.", "repo_name": "ui-kit", "branch": "main", "protected": true',
        ],
    ),

    # 02. (security-team) Release a designated version and verify; additionally, document an audit trail.
    Task(
        annotator='0',
        user_id="task_02",
    instruction=(
        "You represent 'security-group'. Issue a release in 'security-scanner' with tag 'v0.4.0', title 'Performance release', and body 'Performance optimizations and SARIF format support.' Afterwards, verify the latest release. Register an audit by opening an issue titled 'Release v0.4.0 created' with body 'Release published successfully.' labeled 'release', and enter the exact terminal entry 'security-scanner v0.4.0 released.'"
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "security-group"}),
            Action(name="GetRepository", kwargs={"repo_name": "security-scanner"}),
            Action(
                name="CreateRelease",
                kwargs={
                    "repo_name": "security-scanner",
                    "tag": "v0.4.0",
                    "title": "Performance release",
                    "body": "Performance optimizations and SARIF format support.",
                },
            ),
            Action(name="GetLatestRelease", kwargs={"repo_name": "security-scanner"}),
            Action(
                name="CreateIssue",
                kwargs={
                    "repo_name": "security-scanner",
                    "title": "Release v0.4.0 created",
                    "body": "Release published successfully.",
                    "labels": ["release"],
                },
            ),
            Action(name="AppendTerminal", kwargs={"message": "security-scanner v0.4.0 released."}),
        ],
        outputs=[
            '"message": "Release created.", "repo_name": "security-scanner", "tag_name": "v0.4.0", "title": "Performance release"',
            '"tag_name": "v0.4.0", "title": "Performance release"',
        ],
    ),

    # 03. (backend-core) Aggregate alerts, establish a consistent tracking issue, log, and categorize by label.
    Task(
        annotator='0',
        user_id="task_03",
    instruction=(
        "You are 'server-main'. Generate an auditable security snapshot for 'payments-service' which should achieve the following: • establish a new issue labeled 'Security alerts summary' with the body 'Tracking current code scanning findings and severities.' marked 'security'; • ensure the terminal log includes exactly this entry: {\"message\": \"Alerts retrieved.\", \"repo_name\": \"payments-service\", \"alert_count\": 1, \"alert_numbers\": [7], \"severities\": [\"high\"]} and the results must match the current code scanning alert summary data."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "server-main"}),
            Action(name="GetRepository", kwargs={"repo_name": "payments-service"}),
            Action(name="ListCodeScanningAlerts", kwargs={"repo_name": "payments-service"}),
            Action(
                name="CreateIssue",
                kwargs={
                    "repo_name": "payments-service",
                    "title": "Security alerts summary",
                    "body": "Tracking current code scanning findings and severities.",
                    "labels": ["security"],
                },
            ),
            Action(
                name="AppendTerminal",
                kwargs={
                    "message": '{"message": "Alerts retrieved.", "repo_name": "payments-service", "alert_count": 1, "alert_numbers": [7], "severities": ["high"]}'
                },
            ),
        ],
        outputs=[
            '"message": "Alerts retrieved.", "repo_name": "payments-service", "alert_count": 1, "alert_numbers": [7], "severities": ["high"]',
        ],
    ),

    # 05
    Task(
        annotator='0',
        user_id="task_05",
    instruction=(
        "You are 'infra-lead'. Within the 'k8s-monitoring' repository, display all code scanning alerts in the terminal. Subsequently, open an issue titled 'Track code scanning alerts' with the description 'Investigating code scanning alerts for identified issue numbers' and labels ['code-scan', 'security', 'infrastructure']. In conclusion, log a terminal message indicating the issue has been created."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
            Action(name="GetRepository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="ListCodeScanningAlerts", kwargs={"repo_name": "k8s-monitoring"}),
            Action(
                name="AppendTerminal",
                kwargs={
                    "message": '{"message": "Code alerts retrieved.", "repo_name": "k8s-monitoring", "alert_count": 3, "alert_numbers": [42, 45, 48], "severities": ["high", "medium", "low"]}'
                },
            ),
            Action(
                name="CreateIssue",
                kwargs={
                    "repo_name": "k8s-monitoring",
                    "title": "Track code scanning alerts",
                    "body": "Investigating code scanning alerts for identified issue numbers",
                    "labels": ["code-scan", "security", "infrastructure"],
                },
            ),
            # Action(name="GetIssue", kwargs={"repository": "k8s-monitoring", "issue_id": 1}),
            Action(
                name="AppendTerminal",
                kwargs={
                    "message": "Issue # 1 established to monitor code scanning notifications in k8s-monitoring.
                },
            ),
        ],
        outputs=[
            "'message': '{'message': 'Code alerts retrieved.', 'repo_name': 'k8s-monitoring', 'alert_count': 3, 'alert_numbers': [42, 45, 48], 'severities': ['high', 'medium', 'low']}",
            "Issue # 1 established to monitor code scanning notifications in k8s-monitoring.
        ],
    ),

    # 06. (devops-lead) Review merged pull requests in essential repositories and record modified files.
    Task(
        annotator='0',
        user_id="task_06",
    instruction=(
        "As 'infra-lead', oversee the review of all merged pull requests across these repositories: 'acme-webapp', 'utils-js', 'nlp-models', 'security-scanner', 'flutter-finance-app', 'react-dashboard', and 'k8s-monitoring'. For every merged PR, compile the list of modified files and log a terminal audit entry as follows: 'Merged PR # {number} in {repo_name}: {list of files separated by commas}.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
            Action(name="ListPullRequests", kwargs={"repo_name": "acme-webapp"}),
            Action(name="ListPullRequests", kwargs={"repo_name": "utils-js"}),
            Action(name="ListPullRequests", kwargs={"repo_name": "nlp-models"}),
            Action(name="ListPullRequests", kwargs={"repo_name": "security-scanner"}),
            Action(name="ListPullRequests", kwargs={"repo_name": "flutter-finance-app"}),
            Action(name="ListPullRequests", kwargs={"repo_name": "react-dashboard"}),
            Action(name="ListPullRequests", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="AppendTerminal", kwargs={"message": "Merged PR #7 in acme-webapp: src/logger.py"}),
            Action(name="AppendTerminal", kwargs={"message": "Merged PR #16 in utils-js: src/utils/format.js, test/format.test.js"}),
            Action(name="AppendTerminal", kwargs={"message": "Merged PR #22 in nlp-models: src/evaluation.py, scripts/checkpoint.py"}),
            Action(name="AppendTerminal", kwargs={"message": "Merged PR #23 in security-scanner: src/cache.rs, src/scanner.rs, Cargo.toml"}),
            Action(name="AppendTerminal", kwargs={"message": "Merged PR #24 in flutter-finance-app: lib/theme/dark_theme.dart, lib/main.dart, pubspec.yaml"}),
            Action(name="AppendTerminal", kwargs={"message": "Merged PR #30 in react-dashboard: src/styles/global.css, src/theme/dark.css, src/hooks/useTheme.ts"}),
            Action(name="AppendTerminal", kwargs={"message": "Merged PR #32 in k8s-monitoring: kubernetes/alertmanager.yaml, config/alertmanager.yml, docker-compose.yml"}),
            Action(name="AppendTerminal", kwargs={"message": "Merged PR #34 in k8s-monitoring: kubernetes/prometheus.yaml, config/prometheus.yml, docs/MONITORING.md"}),
        ],
        outputs=[
            '"message": "Merged PR # 7 in acme-webapp: src/logger.py
            '"message": "Merged PR # 16 in utils-js: src/utils/format.js, test/format.test.js
            '"message": "Merged PR # 22 in nlp-models: src/evaluation.py, scripts/checkpoint.py
            '"message": "Merged PR # 23 in security-scanner: src/cache.rs, src/scanner.rs, Cargo.toml
            '"message": "Merged PR # 24 in flutter-finance-app: lib/theme/dark_theme.dart, lib/main.dart, pubspec.yaml
            '"message": "Merged PR # 30 in react-dashboard: src/styles/global.css, src/theme/dark.css, src/hooks/useTheme.ts
            '"message": "Merged PR # 32 in k8s-monitoring: kubernetes/alertmanager.yaml, config/alertmanager.yml, docker-compose.yml
            '"message": "Merged PR # 34 in k8s-monitoring: kubernetes/prometheus.yaml, config/prometheus.yml, docs/MONITORING.md
        ],
    ),

    # 07. (backend-core) Gather commit history and author activity data for payments-service.
    Task(
        annotator='0',
        user_id="task_07",
    instruction=(
        "Taking on the role of 'server-main', gather the entire commit history from the 'payments-service' repository and assess commit authors alongside their frequencies. Include the complete record and specifically check the 'main' branch for branch-level statistics. Document the audit by opening an issue named 'Commit authors frequency audit' with the message 'Collected authors and commit counts from full history and main branch.' and the label 'audit', then enter the terminal note 'Authors frequency audit for payments-service completed'."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "server-main"}),
            # Base repository context managed by server-main
            Action(name="SearchRepositories", kwargs={"owner": "server-main"}),
            # Obtain the complete commit history (both overall and by branch) to analyze author frequencies externally.
            Action(name="ListCommits", kwargs={"repo_name": "payments-service"}),
            Action(name="ListCommits", kwargs={"repo_name": "payments-service", "branch": "main"}),
            # Log audit artifacts
            Action(
                name="CreateIssue",
                kwargs={
                    "repo_name": "payments-service",
                    "title": "Commit authors frequency audit",
                    "body": "Collected authors and commit counts from full history and main branch.",
                    "labels": ["audit"],
                },
            ),
            Action(name="AppendTerminal", kwargs={"message": "Authors frequency audit for payments-service completed"}),
        ],
        outputs=[
            '"message": "Authors frequency audit for payments-service completed"',
        ],
    ),

    # 09
    Task(
        annotator='0',
        user_id="task_09",
    instruction=(
        "You are 'intern-emma'. Within 'portfolio-site', initiate a task for an accessibility audit following the last update. Confirm repository contents, and then open an issue titled 'Accessibility audit (WCAG)' with the label 'a11y', including the body 'Run Lighthouse + manual checks for keyboard navigation and color contrast.' Add to terminal: 'portfolio-site accessibility audit opened'."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "intern-emma"}),
            Action(name="GetRepository", kwargs={"repo_name": "portfolio-site"}),
            Action(name="ListFiles", kwargs={"repo_name": "portfolio-site", "branch": "main"}),
            Action(name="CreateIssue", kwargs={
                "repo_name": "portfolio-site",
                "title": "Accessibility audit (WCAG)",
                "body": "Run Lighthouse + manual checks for keyboard navigation and color contrast.",
                "labels": ["a11y"],
            }),
            Action(name="AppendTerminal", kwargs={"message": "portfolio-site accessibility audit opened"}),
        ],
        outputs=['"message": "portfolio-site accessibility audit opened"'],
    ),

    # 10
    Task(
        annotator='0',
        user_id="task_10",
    instruction=(
        "You are 'maya-w'. In 'acme-webapp', enumerate current alerts and branches, examine 'feature-update' files, and initiate an issue named 'Post-merge security sweep' with labels ['security','audit'] along with the body: 'Review SQLi alert and ensure tests and sanitization on main.' Add to terminal: 'acme-webapp post-merge security sweep initiated'."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            # Action(name="GetRepository", parameters={"repo_name": "acme-webapp"}),
            Action(name="ListCodeScanningAlerts", kwargs={"repo_name": "acme-webapp"}),
            Action(name="ListBranches", kwargs={"repo_name": "acme-webapp"}),
            Action(name="ListFiles", kwargs={"repo_name": "acme-webapp", "branch": "feature-update"}),
            Action(name="CreateIssue", kwargs={
                "repo_name": "acme-webapp",
                "title": "Post-merge security sweep",
                "body": "Review SQLi alert and ensure tests and sanitization on main.",
                "labels": ["security", "audit"],
            }),
            Action(name="AppendTerminal", kwargs={"message": "acme-webapp post-merge security sweep initiated"}),
        ],
        outputs=['"message": "acme-webapp post-merge security sweep initiated"'],
    ),

    # 11
    Task(
        annotator='0',
        user_id="task_11",
    instruction=(
        "Act as 'infra-lead'. In the context of 'k8s-monitoring', verify merged PRs #32 and # Commits on 'feature-alertmanager' are detailed in 32 and #34, with a final note confirming that upgrade and alerting configuration have been jointly validated.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
            Action(name="GetRepository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="GetPullRequest", kwargs={"repo_name": "k8s-monitoring", "pr_number": 32}),
            Action(name="GetPullRequest", kwargs={"repo_name": "k8s-monitoring", "pr_number": 34}),
            Action(name="ListCommits", kwargs={"repo_name": "k8s-monitoring", "branch": "feature-alertmanager"}),
            Action(name="AppendTerminal", kwargs={"message": "k8s-monitoring merged PRs verified: alertmanager + prometheus upgrade"}),
        ],
        outputs=['"message": "k8s-monitoring merged PRs verified: alertmanager + prometheus upgrade"'],
    ),

    # 12
    Task(
        annotator='0',
        user_id="task_12",
    instruction=(
        "Function as 'ui-developer'. Within 'react-dashboard', enumerate open PRs, examine the conflicted PR #28, and add a comment to Issue # 28, and comment on Issue #25 with: 'Strategy: implement useEffect cleanup and WebSocket closure on unmount; check heap snapshots.' Update terminal with: 'memory leak investigation for react-dashboard scheduled.'
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "ui-developer"}),
            Action(name="GetRepository", kwargs={"repo_name": "react-dashboard"}),
            Action(name="ListOpenPullRequests", kwargs={"repo_name": "react-dashboard"}),
            Action(name="GetPullRequest", kwargs={"repo_name": "react-dashboard", "pr_number": 28}),
            Action(
                name="AddIssueComment",
                kwargs={
                    "repo_name": "react-dashboard",
                    "issue_number": 25,
                    "comment": "Plan: add useEffect cleanup + ws close on unmount; verify heap snapshots.",
                },
            ),

            Action(name="AppendTerminal", kwargs={"message": "react-dashboard memory leak investigation planned"}),
        ],
        outputs=['"message": "react-dashboard memory leak investigation planned"'],
    ),

    # Handle a single labeled issue by adding a comment and then closing it.
    Task(
        annotator='0',
        user_id="task_13",
    instruction=(
        "You are 'maya-w' managing the repository 'acme-webapp'. Verify that the repository's final state meets ALL acceptance criteria listed below, utilizing the precise literals given. Approach this as outcomes/specification, not detailed guidance. ACCEPTANCE CRITERIA (all must be met in the end): • Issue #3 has the label: triage-urgent • Issue #3 state is exactly: closed • Issue # Issue #3 is marked with the triage-urgent label, is in a closed state, and includes the following comment: Labels applied: triage-urgent, quality.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="AddLabelToIssue", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "label": "triage-urgent"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "comment": "Labels applied: triage-urgent, quality."}),
            Action(name="UpdateIssue", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "state": "closed"}),
        ],
        outputs=[
            '"message": "Label \'triage-urgent\' added."',
            '"message": "Comment added."',
            '"message": "Issue updated", "number": 3, "state": "closed"',
        ],
    ),

    # 14 (bob-dev) utils-js: tag + note + resolve a single issue (outputs mirror tool returns)
    Task(
        annotator='0',
        user_id="task_14",
    instruction=(
        "You are 'ryan-dev' overseeing the repository 'utils-js'. Confirm that the final state satisfies ALL acceptance criteria outlined below, approaching this as a specification (not detailed instructions). ACCEPTANCE CRITERIA: • Issue #4 has the label: needs-triage • Issue #4 contains the exact new comment: Triaged and scheduled for next minor. • Issue # Issue #4 is marked with the label: needs-triage. It includes the comment: Triaged and scheduled for next minor. The status of Issue #4 is: closed.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "ryan-dev"}),
            Action(name="GetRepository", kwargs={"repo_name": "utils-js"}),

            Action(name="AddLabelToIssue", kwargs={"repo_name": "utils-js", "issue_number": 4, "label": "needs-triage"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "utils-js", "issue_number": 4, "comment": "Triaged and scheduled for next minor."}),
            Action(name="UpdateIssue", kwargs={"repo_name": "utils-js", "issue_number": 4, "state": "closed"}),
        ],
        outputs=[
            '"message": "Label \'needs-triage\' added."',
            '"message": "Comment added."',
            '"message": "Issue updated", "number": 4, "state": "closed"',
        ],
    ),

    # 15 (frontend-dev) react-dashboard: tag + note + resolve one issue (outputs mirror tool returns)
    Task(
        annotator='0',
        user_id="task_15",
    instruction=(
        "As 'ui-developer', you are working in repository 'react-dashboard'. Ensure that the final outcome fulfills ALL acceptance criteria below, treating this as a specification rather than step-by-step guidance. ACCEPTANCE CRITERIA: • Issue #25 must have the label: investigate • Issue #25 should include the precise new comment: Triaged; assigning to next sprint. • Issue # Issue #25 must carry the label: investigate. It should contain the exact comment: Triaged; assigning to next sprint. The status of Issue #25 must be: closed.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "ui-developer"}),
            Action(name="GetRepository", kwargs={"repo_name": "react-dashboard"}),

            Action(name="AddLabelToIssue", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "label": "investigate"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "comment": "Triaged; assigning to next sprint."}),
            Action(name="UpdateIssue", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "state": "closed"}),
        ],
        outputs=[
            '"message": "Label \'investigate\' added."',
            '"message": "Comment added."',
            '"message": "Issue updated", "number": 25, "state": "closed"',
        ],
    ),

    # 16 (nlp-labs) nlp-models: tag + note + resolve one issue
    Task(
        annotator='0',
        user_id="task_16",
    instruction=(
        "As a member of 'language-ai', ensure that while working in the repository 'nlp-models', the end state complies with ALL acceptance criteria listed below, using this as a specification instead of step-by-step guidance. ACCEPTANCE CRITERIA: • Issue #12 should bear the label: investigate-oom • Issue #12 is required to contain the exact new comment: Initial triage: OOM under training; mitigation underway. • Issue # Issue 12 must be tagged with: investigate-oom. It should include the following comment: Initial triage: OOM under training; mitigation underway. Additionally, Issue 12 must be set to the state: closed.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "language-ai"}),
            Action(name="GetRepository", kwargs={"repo_name": "nlp-models"}),

            Action(name="AddLabelToIssue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "label": "investigate-oom"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "nlp-models", "issue_number": 12, "comment": "Initial triage: OOM under training; mitigation underway."}),
            Action(name="UpdateIssue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "state": "closed"}),
        ],
        outputs=[
            '"message": "Label \'investigate-oom\' added."',
            '"message": "Comment added."',
            '"message": "Issue updated", "number": 12, "state": "closed"',
        ],
    ),

    # 17 (alice-w) acme-webapp: include topic; verify the last terminal input
    Task(
        annotator='0',
        user_id="task_17",
    instruction=(
        "You are 'maya-w' and need to utilize only the available tools. YOUR GOAL • In the 'acme-webapp' repository, confirm the repository topics contain the precise topic literal below. • Confirm the latest terminal entry matches the message literal below exactly (branch name included). LITERALS (use verbatim) - repo: acme-webapp - topic to add: quality-gates - terminal message: Topic updated: quality-gates added to acme-webapp on branch main"
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="GetRepository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "acme-webapp"}),

            Action(name="AddRepoTopic", kwargs={"repo_name": "acme-webapp", "topic": "quality-gates"}),
            Action(name="ListRepoTopics", kwargs={"repo_name": "acme-webapp"}),

            Action(name="AppendTerminal", kwargs={"message": "Topic updated: quality-gates added to acme-webapp on branch main"}),
            Action(name="ListTerminalLastMessage", kwargs={}),
        ],
        outputs=[
            '"message": "Topic \'quality-gates\' added."',
            '"entries": {"printed_ts": "2025-08-21T12:00:00Z", "message": "Topic updated: quality-gates added to acme-webapp on branch main"}',
        ],
    ),

    # 18 (alice-w) acme-webapp: rename, mark as private, assign topic, validate listings, log confirmation
    Task(
        annotator='0',
        user_id="task_18",
    instruction=(
        "You are 'maya-w' and need to use only the available tools. YOUR GOAL • Change the name of the 'acme-webapp' repository to match the exact new name literal. • Adjust the renamed repository's visibility to the exact value literal. • Incorporate the exact topic literal into the renamed repository and confirm the topics. • Verify that the renamed repository is included in your list of owned repositories. • Ensure the most recent terminal entry corresponds exactly to the message literal. LITERALS (use verbatim) - old repo name: acme-webapp - new repo name: acme-webapp-qa - visibility: private - topic to add: qa-ready - terminal message: Repository acme-webapp renamed to acme-webapp-qa and set private; topic qa-ready added"
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),

            # Change the repository name, adjust its visibility settings, and assign a topic to the updated repository.
            Action(name="RenameRepository", kwargs={"old_name": "acme-webapp", "new_name": "acme-webapp-qa"}),
            Action(name="SetRepositoryVisibility", kwargs={"repo_name": "acme-webapp-qa", "visibility": "private"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "acme-webapp-qa", "topic": "qa-ready"}),

            # Read-backs mandated by acceptance standards.
            Action(name="ListRepoTopics", kwargs={"repo_name": "acme-webapp-qa"}),
            Action(name="ListRepositories", kwargs={}),

            # Output confirmation to the terminal and check the most recent entry.
            Action(name="AppendTerminal", kwargs={
                "message": "Repository acme-webapp renamed to acme-webapp-qa and set private; topic qa-ready added"
            }),
            Action(name="ListTerminalLastMessage", kwargs={}),
        ],
        outputs=[
            '"message": "Repository renamed", "new_name": "acme-webapp-qa"',
            '"message": "Visibility updated", "repo_name": "acme-webapp-qa", "visibility": "private"',
            '"message": "Topic \'qa-ready\' added."',
            '"entries": {"printed_ts": "2025-08-21T12:00:00Z", "message": "Repository acme-webapp renamed to acme-webapp-qa and set private; topic qa-ready added"}',
        ],
    ),

    # 19 (alice-w) acme-webapp: activate branch protection and record confirmation
    Task(
        annotator='0',
        user_id="task_19",
    instruction=(
        "You are 'maya-w' and you should operate solely through the available tools. PERFORM THESE ACTIONS • Apply branch protection to the default branch of the repository 'acme-webapp' using the precise rule literal. • Confirm that protection is active for that branch. • Add the specified terminal message literal and make certain it is the most recent entry. LITERALS (use verbatim) - repo: acme-webapp - branch literal: main - protected flag: 'true' - rules object: {\"require_code_owner_reviews\": True} - terminal message: Branch protection enabled on acme-webapp main"
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "acme-webapp"}),

            # ✅ boolean value true (not a string)
            Action(
                name="SetBranchProtection",
                kwargs={
                    "repo_name": "acme-webapp",
                    "branch": "main",
                    "protected": "true",
                    "rules": {"require_code_owner_reviews": True},
                },
            ),

            Action(name="GetBranchProtection", kwargs={"repo_name": "acme-webapp", "branch": "main"}),
            Action(name="AppendTerminal", kwargs={"message": "Branch protection enabled on acme-webapp main"}),
            Action(name="ListTerminalLastMessage", kwargs={}),
        ],
        outputs=[
            # from configure_branch_security
            '"message": "Branch protection enabled."',

            # from list_terminal_final_message
            '"timestamp": "2025-08-21T12:00:00Z", "message": "Branch protection enabled on acme-webapp main"',
        ],
    ),

    # 21
    Task(
        annotator='0',
        user_id="task_21",
    instruction=(
        "You are 'design-team'. Review the open PRs in 'ui-kit', provide two comments on PR #11 with feedback 'Looks great overall!' and 'Can we optimize the load time?', retrieve details of PR #12, label issue # Retrieve details for PR #12, mark issue #6 as 'reviewed', and log your feedback in the terminal, noting 'Looks great overall!' and 'Can we optimize the load time?'.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "design-team"}),
            Action(name="GetRepository", kwargs={"repo_name": "ui-kit"}),
            Action(name="ListOpenPullRequests", kwargs={"repo_name": "ui-kit"}),
            Action(name="CommentOnPullRequest", kwargs={"repo_name": "ui-kit", "pr_number": 11, "comment": "Looks great overall!"}),
            Action(name="CommentOnPullRequest", kwargs={"repo_name": "ui-kit", "pr_number": 11, "comment": "Can we optimize the load time?"}),
            Action(name="GetPullRequest", kwargs={"repo_name": "ui-kit", "pr_number": 12}),
            Action(name="AddLabelToIssue", kwargs={"repo_name": "ui-kit", "issue_number": 6, "label": "reviewed"}),
            Action(name="AppendTerminal", kwargs={"message": "PR #11 reviewed and issue # 11 has been examined and issue #6 marked as reviewed.
        ],
        outputs=[
            '"message": "PR #11 reviewed and issue # 11 examined and issue #6 tagged as reviewed.
        ],
    ),

    # 22
    Task(
        annotator='0',
        user_id="task_22",
    instruction=(
        "As 'infra-lead', evaluate merged pull requests in 'k8s-monitoring'. For each PR that has been merged, provide the list of altered files and the commit authors. PR #32 was integrated from the branch 'feature-alertmanager', and PR #34 from 'upgrade-prometheus'. In case any PR alters files within the 'config/' folder, create an issue titled 'Audit config changes' with the content 'Merged PRs modified files under config/ directory. Review needed.' Then add to the terminal log exactly: Audit results: PR #32 files: ['kubernetes/alertmanager.yaml', 'config/alertmanager.yml', 'docker-compose.yml'], authors: ['infra-lead'] PR # 32 was merged from the 'feature-alertmanager' branch, and PR #34 was merged from 'upgrade-prometheus'. If any PR modifies files in the 'config/' directory, open an issue titled 'Audit config changes' with the message 'Merged PRs altered files in the config/ directory. Review required.' Additionally, log the following in the terminal: Audit results: PR #32 files: ['kubernetes/alertmanager.yaml', 'config/alertmanager.yml', 'docker-compose.yml'],
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
            Action(name="GetRepository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="ListPullRequests", kwargs={"repo_name": "k8s-monitoring"}),
            # Pull Request 32
            Action(name="ListPullRequestFiles", kwargs={"repo_name": "k8s-monitoring", "pr_number": 32}),
            Action(name="ListCommits", kwargs={"repo_name": "k8s-monitoring", "branch": "feature-alertmanager"}),

            # Pull Request 34
            Action(name="ListPullRequestFiles", kwargs={"repo_name": "k8s-monitoring", "pr_number": 34}),
            Action(name="ListCommits", kwargs={"repo_name": "k8s-monitoring", "branch": "upgrade-prometheus"}),

            # ✅ Action that modifies the database (if config/ is altered)
            Action(name="CreateIssue", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Audit config changes",
                "body": "Merged PRs modified files under config/ directory. Review needed.",
                # "tags": ["audit"]
            }),

            # Terminal output utilizing **actual values**
            Action(name="AppendTerminal", kwargs={
                "message": (
                    "Audit results:\n"
                    "PR # 32 files: ['kubernetes/alertmanager.yaml', 'config/alertmanager.yml', 'docker-compose.yml']
                    "authors: ['infra-lead']\n"
                    "PR # 34 files: ['kubernetes/prometheus.yaml', 'config/prometheus.yml', 'docs/MONITORING.md']
                    "authors: ['infra-lead']"
                )
            }),
        ],
        outputs=[
            "{'32': {'files': ['kubernetes/alertmanager.yaml', 'config/alertmanager.yml', 'docker-compose.yml'], 'authors': ['infra-lead']}, "
            "'34': {'files': ['kubernetes/prometheus.yaml', 'config/prometheus.yml', 'docs/MONITORING.md'], 'authors': ['infra-lead']}}"
        ],
    ),

    # 24
    Task(
        annotator='0',
        user_id="task_24",
    instruction=(
        "As 'design-team', check that Alert #4 dismissal in 'ui-kit' is consistent with the latest commits on 'feature-theme'. Examine branch commits and the current alerts, inspect Issue #6, and add a PR review comment on PR # Dismissals in 'ui-kit' align with recent updates on 'feature-theme'. Review branch commits and current alerts, check Issue #6, and add a review comment on PR #11 regarding security status. Append terminal: 'ui-kit XSS dismissal confirmed with feature-theme commits'.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "design-team"}),
            Action(name="GetRepository", kwargs={"repo_name": "ui-kit"}),
            Action(name="ListCommits", kwargs={"repo_name": "ui-kit", "branch": "feature-theme"}),
            Action(name="ListCodeScanningAlerts", kwargs={"repo_name": "ui-kit"}),
            Action(name="GetIssue", kwargs={"repo_name": "ui-kit", "issue_number": 6}),
            # Action(name="AddIssueComment", kwargs={"repo_name": "ui-kit", "issue_number": 6, "comment": "Security: Alert # Action(name="AddIssueComment", kwargs={"repo_name": "ui-kit", "issue_number": 6, "comment": "Security: Alert #4 cleared after recent feature-theme updates."}),
            Action(name="GetPullRequest", kwargs={"repo_name": "ui-kit", "pr_number": 11}),
            Action(name="CreatePullRequestReview", kwargs={
                "repo_name": "ui-kit",
                "pr_number": 11,
                "review_decision": "comment",
                "comment": "ui-kit XSS dismissal validated against feature-theme commits"
            }),
            Action(name="AppendTerminal", kwargs={"message": "ui-kit XSS dismissal validated against feature-theme commits"}),
        ],
        outputs=['"message": "ui-kit XSS dismissal validated against feature-theme commits"'],
    ),

    # 25
    Task(
        annotator='0',
        user_id="task_25",
    instruction=(
        "You are 'security-group'. For 'security-scanner', confirm the resolution of Issue #11 through PR #23 and examine the commits on 'perf-optimizations'. Develop a release called 'v0.3.1 Performance optimization' containing the text: 'Implements file system cache; closes # Review PR #23 and the commits on 'perf-optimizations'. Create a release named 'v0.3.1 Performance optimization' with the description: 'Introduces file system cache; resolves #11; approximately 70% performance improvement.'. Add terminal note: 'Security scanner performance fix validated and released'.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "security-group"}),
            Action(name="GetRepository", kwargs={"repo_name": "security-scanner"}),
            Action(name="GetIssue", kwargs={"repo_name": "security-scanner", "issue_number": 11}),
            Action(name="GetPullRequest", kwargs={"repo_name": "security-scanner", "pr_number": 23}),
            Action(name="ListCommits", kwargs={"repo_name": "security-scanner", "branch": "perf-optimizations"}),
            Action(name="CreateRelease", kwargs={
                "repo_name": "security-scanner",
                "tag": "v0.3.1",
                "name": "v0.3.1 Performance optimization",
                "body": "Implements file system cache; closes # 11; approximately 70% increase in performance.
            }),
            Action(name="AppendTerminal", kwargs={"message": "security-scanner perf fix validated and released"}),
        ],
        outputs=['"message": "security-scanner perf fix validated and released"'],
    ),

    # 26
    Task(
        annotator='0',
        user_id="task_26",
    instruction=(
        "You are 'language-ai'. Within 'nlp-models', ensure that PR #22 was merged for Issue #16 and examine Issue #12 concerning memory. Enumerate commits on the 'exp-transformer' branch to establish investigation context. Subsequently, comment on Issue # Merged pull request 22 for Issue #16 and reviewed Issue #12 related to memory. List commits on the 'exp-transformer' branch for context. Then, add a comment on Issue #12 stating: 'Analyzed gradient accumulation commits on exp-transformer for memory optimization guidance.' Add terminal note: 'nlp-models checkpoint fix confirmed; memory follow-up acknowledged.'
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "language-ai"}),
            Action(name="GetRepository", kwargs={"repo_name": "nlp-models"}),
            Action(name="GetPullRequest", kwargs={"repo_name": "nlp-models", "pr_number": 22}),
            Action(name="GetIssue", kwargs={"repo_name": "nlp-models", "issue_number": 16}),
            Action(name="GetIssue", kwargs={"repo_name": "nlp-models", "issue_number": 12}),
            Action(name="ListCommits", kwargs={"repo_name": "nlp-models", "branch": "exp-transformer"}),
            Action(
                name="AddIssueComment",
                kwargs={
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "comment": "Reviewed gradient accumulation commits on exp-transformer for memory tuning direction."
                }
            ),
            Action(name="AppendTerminal", kwargs={"message": "nlp-models checkpoint fix verified; memory follow-up noted"}),
        ],
        outputs=['"message": "nlp-models checkpoint fix verified; memory follow-up noted"'],
    ),

    # 27
    Task(
        annotator='0',
        user_id="task_27",
    instruction=(
        "Assume the role of 'ui-developer'. For 'react-dashboard', ensure that PR #30 successfully closed Issue #27. Compile a list of open PRs and request changes on PR #28 by commenting: 'Resolve merge conflicts before merge.' Add the label 'investigate' to Issue # 30 successfully resolved Issue #27. Generate a list of active PRs and ask for modifications on PR #28 by commenting: 'Address merge conflicts prior to merging.' Assign the label 'investigate' to Issue #25. Append terminal: 'react-dashboard dark mode confirmed; realtime PR gated.'
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "ui-developer"}),
            Action(name="GetRepository", kwargs={"repo_name": "react-dashboard"}),
            Action(name="GetIssue", kwargs={"repo_name": "react-dashboard", "issue_number": 27}),
            Action(name="GetPullRequest", kwargs={"repo_name": "react-dashboard", "pr_number": 30}),
            Action(name="ListOpenPullRequests", kwargs={"repo_name": "react-dashboard"}),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "react-dashboard", "pr_number": 28, "review_decision": "request_changes", "body": "Resolve merge conflicts before merge."}),
            Action(name="AddLabelToIssue", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "label": "investigate"}),
            Action(name="AppendTerminal", kwargs={"message": "react-dashboard dark mode verified; realtime PR gated"}),
        ],
        outputs=['"message": "react-dashboard dark mode verified; realtime PR gated"'],
    ),

    # 29
    Task(
        annotator='0',
        user_id="task_29",
    instruction=(
        "Serve as 'platform-team'. In the 'infra-terraform' project, review files on the 'feat-alb' branch, refer to Issue #9, and initiate a pull request from 'feat-alb' to 'main' titled 'Increase ALB health check timeout' with the body 'Addresses #9 by increasing target health check thresholds.' Subsequently, comment on Issue # 9, create a pull request from 'feat-alb' to 'main' named 'Increase ALB health check timeout' with the description 'Resolves #9 by raising target health check limits.' Then, add a comment on Issue #9 stating: 'PR created to modify ALB health check duration and configuration.' Add to terminal: 'infra-terraform PR created to improve ALB health checks.'
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "platform-team"}),
            Action(name="GetRepository", kwargs={"repo_name": "infra-terraform"}),
            Action(name="ListFiles", kwargs={"repo_name": "infra-terraform", "branch": "feat-alb"}),
            Action(name="GetIssue", kwargs={"repo_name": "infra-terraform", "issue_number": 9}),
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "infra-terraform",
                "head": "feat-alb",
                "base": "main",
                "title": "Increase ALB health check timeout",
                "body": "Addresses # 9 by raising the thresholds for target health checks.
            }),
            Action(name="AddIssueComment", kwargs={"repo_name": "infra-terraform", "issue_number": 9, "comment": "Opened PR to adjust ALB health check timing and config."}),
            Action(name="AppendTerminal", kwargs={"message": "infra-terraform PR opened to address ALB health checks"}),
        ],
        outputs=['"message": "infra-terraform PR opened to address ALB health checks"'],
    ),

    # 30
    Task(
        annotator='0',
        user_id="task_30",
    instruction=(
        "You are 'ml-engineer'. Within 'ml-pipeline', identify the commits in 'feature-mlflow-tracking' and examine the file content there. Update Issue # Add the comment: 'The following action involves drift detection.' End the terminal with: 'Reviewed MLflow integration for ml-pipeline; validation plan has been refreshed.'
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "ml-engineer"}),
            Action(name="GetRepository", kwargs={"repo_name": "ml-pipeline"}),
            Action(name="ListCommits", kwargs={"repo_name": "ml-pipeline", "branch": "feature-mlflow-tracking"}),
            Action(name="ListFiles", kwargs={"repo_name": "ml-pipeline", "branch": "feature-mlflow-tracking"}),
            Action(name="GetFileContents", kwargs={
                "repo_name": "ml-pipeline",
                "branch": "feature-mlflow-tracking",
                "path": "config/model_config.yaml"
            }),
            Action(name="GetIssue", kwargs={"repo_name": "ml-pipeline", "issue_number": 31}),
            Action(name="AddIssueComment", kwargs={
                "repo_name": "ml-pipeline",
                "issue_number": 31,
                "comment": "Next step is drift detection."
            }),
            Action(name="AppendTerminal", kwargs={"message": "ml-pipeline MLflow integration reviewed; validation roadmap updated"}),
        ],
        outputs=['"message": "ml-pipeline MLflow integration reviewed; validation roadmap updated"'],
    ),

    # 31
    Task(
        annotator='0',
        user_id="task_31",
    instruction=(
        "You are 'security-group'. Within 'security-scanner', evaluate open PR # Set the SARIF output to 25 and list the existing alerts. Comment on the PR: 'Verify SARIF schema v2.1.0 and CI upload procedure.' Next, open an issue titled 'SARIF configuration refinement' with the label 'enhancement' and the description: 'Refine schema validation and CI upload settings.' Conclude the terminal with: 'Security scanner SARIF review and configuration follow-up initiated.'
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "security-group"}),
            Action(name="GetRepository", kwargs={"repo_name": "security-scanner"}),
            Action(name="GetPullRequest", kwargs={"repo_name": "security-scanner", "pr_number": 25}),
            Action(name="ListCodeScanningAlerts", kwargs={"repo_name": "security-scanner"}),
            Action(name="CommentOnPullRequest", kwargs={
                "repo_name": "security-scanner",
                "pr_number": 25,
                "comment": "Confirm SARIF schema v2.1.0 and CI upload step."
            }),
            Action(name="CreateIssue", kwargs={
                "repo_name": "security-scanner",
                "title": "SARIF config polish",
                "body": "Tighten schema validation and CI upload parameters.",
                "labels": ["enhancement"],
            }),
            Action(name="AppendTerminal", kwargs={"message": "security-scanner SARIF review and config follow-up created"}),
        ],
        outputs=['"message": "security-scanner SARIF review and config follow-up created"'],
    ),

    # 33 (alice-w) acme-webapp: establish feature branch, include release notes, commit changes, and document confirmation.
    Task(
        annotator='0',
        user_id="task_33",
    instruction=(
        "You are 'maya-w' and must function using only the provided tools. YOUR OBJECTIVE • In the 'acme-webapp' repository, formulate a new branch from the literal source branch indicated, incorporate a release-notes file with the exact literal content, perform a commit with the exact literal message, and authenticate the file's presence on the newly created branch. • Verify the latest terminal entry matches the exact literal message outlined below. LITERALS (use verbatim) - repo: acme-webapp - source branch: main - new branch: feature-banners - file path: docs/release-notes.md - file content: ## Release notes\n- Seed entry\n - commit message: docs: include release notes seed - terminal message: Release notes committed on feature-banners in acme-webapp"
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),

            # Access the default branch to validate the use of 'main' as the source branch.
            Action(name="GetDefaultBranch", kwargs={"repo_name": "acme-webapp"}),

            # Establish a feature branch and include + commit the release notes.
            Action(name="CreateBranch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "feature-banners"
            }),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-banners",
                "path": "docs/release-notes.md",
                "content": "## Changelog\n- Initial data insertion
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-banners",
                "commit_message": "docs: add release notes seed"
            }),

            # Check if the file is present in the new branch.
            Action(name="ListFiles", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-banners"
            }),

            # Generate and confirm: terminal validation
            Action(name="AppendTerminal", kwargs={
                "message": "Release notes committed on feature-banners in acme-webapp"
            }),
            Action(name="ListTerminalLastMessage", kwargs={}),
        ],
        outputs=[
            '"message": "Branch created", "new_branch": "feature-banners"',
            '"message": "Committed to branch", "branch": "feature-banners"',
            '"entries": {"printed_ts": "2025-08-21T12:00:00Z", "message": "Release notes committed on feature-banners in acme-webapp"}',
        ],
    ),

    # 35 (frontend-dev) Secure the default branch, release a hardened version, and log the audit.
    Task(
        annotator='0',
        user_id="task_35",
    instruction=(
        "You are 'ui-developer. You must implement baseline hardening on the default branch of the 'react-dashboard' repository and disseminate that fortified state as a lightweight release. The default branch has to be protected with the attribute set to 'true' and rules precisely as follows: { \"required_reviews\": 1, \"enforce_admins\": true }. Incorporate the repository topic 'security-hardening'. Launch a release with the tag 'task_65-hardened' and body 'Hardening rules applied [task_65]'. Provide the branch protection status and guidelines for the default branch, and include the terminal audit entry: 'Protection enabled and release task_65-hardened published for react-dashboard [task_65]'."
    ),
        actions=[
            # Identification and retrieval of the default branch (read-only).
            Action(name="GetMe", kwargs={"username": "ui-developer"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "react-dashboard"}),

            # Strengthening modifications (writes)
            Action(
                name="SetBranchProtection",
                kwargs={
                    "repo_name": "react-dashboard",
                    "branch": "main",
                    "protected": "true",
                    "rules": {"required_reviews": 1, "enforce_admins": True},
                },
            ),
            Action(name="AddRepoTopic", kwargs={"repo_name": "react-dashboard", "topic": "security-hardening"}),
            Action(
                name="CreateRelease",
                kwargs={
                    "repo_name": "react-dashboard",
                    "tag": "task_65-hardened",
                    "body": "Hardening rules applied [task_65]",
                },
            ),

            # Single verification readback to maintain complexity between 13 and 15.
            Action(name="GetBranchProtection", kwargs={"repo_name": "react-dashboard", "branch": "main"}),

            # End-point verification
            Action(
                name="AppendTerminal",
                kwargs={"message": "Protection enabled and release task_65-hardened published for react-dashboard [task_65]"},
            ),
        ],
        outputs=[
            # Branch protection entity according to tool contract (protected is a string in the tool's output)
            '"protected": "true", "rules": {"required_reviews": 1, "enforce_admins": true}',
            # Verification of terminal audit
            '"message": "Protection enabled and release task_65-hardened published for react-dashboard [task_65]"',
        ],
    ),

    # 37 (alice-w) Branch lifecycle involving file operations and audit logging (Difficult ~13–14 connections)
    Task(
        annotator='0',
        user_id="task_37",
    instruction=(
        "You are 'maya-w', tasked with operations in 'acme-webapp'. Illustrate the process of managing a short-term working branch. Create a temporary branch named 'temp-branch' based on the repository's default branch. Use this branch to store a transient note at 'docs/tmp.txt' with the content 'temp work'. Verify that the note remains accessible as long as the branch is active, then retire the branch. When retiring the branch, log the action with the message: 'Branch temp-branch deleted in acme-webapp.'. Finally, list the branches left post-retirement. Return: (a) the file content obtained, (b) the audit message, and (c) the final list of branches."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "acme-webapp"}),

            # Establish branch
            Action(name="CreateBranch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "temp-branch"
            }),

            # Create file
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "temp-branch",
                "path": "docs/tmp.txt",
                "content": "temp work"
            }),

            # Open the file.
            Action(name="GetFileContents", kwargs={
                "repo_name": "acme-webapp",
                "branch": "temp-branch",
                "path": "docs/tmp.txt"
            }),

            # Remove branch
            Action(name="DeleteBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "temp-branch"
            }),

            # Logging of audit activities
            Action(name="AppendTerminal", kwargs={
                "message": "Branch temp-branch deleted in acme-webapp."
            }),

            # Display branches
            Action(name="ListBranches", kwargs={
                "repo_name": "acme-webapp"
            }),
        ],
        outputs=[
            "'file_content': 'temp work'",
            "'terminal_message': 'Branch temp-branch deleted in acme-webapp.'",
            "'branches': ['main', 'feature-update']"
        ],
    ),

    # 41
    Task(
        annotator='0',
        user_id="task_41",
    instruction=(
        "You are 'maya-w'. Within the 'acme-webapp' repository, initiate a new issue titled 'Security audit [task_01]' with the body 'Check SQL injection handling paths. [task_01]'. Ensure the issue has the label 'security-check', contains the comment 'Audit logged. [task_01]', and conclude with the issue state as 'closed'. Provide confirmation that the label was applied, the issue's closure status, and results from a search demonstrating an issue labeled 'security-check' is present. Also, include this final audit message: 'Issue closed with security-check label in acme-webapp [task_01]'."
    ),
        actions=[
            # Identification
            Action(name="GetMe", kwargs={"username": "maya-w"}),

            # Generate a predictable problem.
            Action(
                name="CreateIssue",
                kwargs={
                    "repo_name": "acme-webapp",
                    "title": "Security audit [task_01]",
                    "body": "Check SQL injection handling paths. [task_01]",
                    "labels": []
                },
            ),

            # Assign label and add comment.
            Action(
                name="AddLabelToIssue",
                kwargs={"repo_name": "acme-webapp", "issue_number": 1, "label": "security-check"},
            ),
            Action(
                name="AddIssueComment",
                kwargs={
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "comment": "Audit logged. [task_01]"
                },
            ),

            # Resolve the issue.
            Action(
                name="UpdateIssue",
                kwargs={"repo_name": "acme-webapp", "issue_number": 1, "state": "closed"},
            ),

            # Confirm through search.
            Action(
                name="SearchIssues",
                kwargs={"query": "security-check"},
            ),

            # Command line verification
            Action(
                name="AppendTerminal",
                kwargs={"message": "Issue closed with security-check label in acme-webapp [task_01]"},
            ),
        ],
        outputs=[
            '"message": "Label \'security-check\' added."',
            '"state": "closed"',
            '"results": [',
            '"title": "Security audit [task_01]"',
            '"labels": ["security-check"]',
            '"message": "Issue closed with security-check label in acme-webapp [task_01]"',
        ],
    ),

    # 42
    Task(
        annotator='0',
        user_id="task_42",
    instruction=(
        "As 'ui-developer', proceed within the 'react-dashboard' repository to create a new issue titled 'Build pipeline audit [task_72]' including the body 'Verify CI stages and artifacts for reproducibility. [task_72]'. Ensure this issue is marked with the label 'ci-audit', contains the exact comment 'Checklist prepared. [task_72]', and concludes in the 'closed' state. Confirm the presence of the label, the issue's final condition, and provide a search result entry verifying an issue with label 'ci-audit' is present. Incorporate this closing audit line: 'Issue closed with ci-audit label in react-dashboard [task_72]'."
    ),
        actions=[
            # Identification
            Action(name="GetMe", kwargs={"username": "ui-developer"}),

            # Generate a predictable problem (single row).
            Action(
                name="CreateIssue",
                kwargs={
                    "repo_name": "react-dashboard",
                    "title": "Build pipeline audit [task_72]",
                    "body": "Verify CI stages and artifacts for reproducibility. [task_72]",
                    "labels": []
                },
            ),

            # Add label and comment.
            Action(
                name="AddLabelToIssue",
                kwargs={"repo_name": "react-dashboard", "issue_number": 1, "label": "ci-audit"},
            ),
            Action(
                name="AddIssueComment",
                kwargs={
                    "repo_name": "react-dashboard",
                    "issue_number": 1,
                    "comment": "Checklist prepared. [task_72]"
                },
            ),

            # Resolve the issue.
            Action(
                name="UpdateIssue",
                kwargs={"repo_name": "react-dashboard", "issue_number": 1, "state": "closed"},
            ),

            # Confirm through search
            Action(
                name="SearchIssues",
                kwargs={"query": "ci-audit"},
            ),

            # Final review of system logs
            Action(
                name="AppendTerminal",
                kwargs={"message": "Issue closed with ci-audit label in react-dashboard [task_72]"},
            ),
        ],
        outputs=[
            '"message": "Label \'ci-audit\' added."',
            '"state": "closed"',
            '"results": [',
            '"title": "Build pipeline audit [task_72]"',
            '"labels": ["ci-audit"]',
            '"message": "Issue closed with ci-audit label in react-dashboard [task_72]"',
        ],
    ),

    # 46
    Task(
        annotator="0",
        user_id="task_46",
    instruction=(
        "You are part of the 'security-group'. Ensure the end state as specified, with precision in all values and case-sensitivity: • You own a repository called 'security-scanner-pro', its visibility set to 'public' and the default branch named 'main'. • Repository topics should include both 'security' and 'sarif'. • A branch named 'feature-sarif' must be established. On this branch, ensure 'src/scanner.py' reads exactly 'print('sarif-v1')' and 'README.md' shows precisely '# security-scanner-pro'. • The most recent commit on 'feature-sarif' should convey the message 'Add SARIF support scaffolding'. • Pull request # 1 must switch from head 'feature-sarif' to base 'main', with title 'Add SARIF output support' and body 'Introduce SARIF output skeleton.', including requested reviewers 'qa-mike' and 'dev-sue', and undergo approval and merging. • A release for 'security-scanner-pro' must be created with tag 'v0.5.0', title 'SARIF support', and body 'Initial SARIF output format release.', with the latest release linked to tag
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "security-group"}),
            Action(name="CreateRepository", kwargs={"repo_name": "security-scanner-pro", "visibility": "public", "default_branch": "main"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "security-scanner-pro", "topic": "security"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "security-scanner-pro", "topic": "sarif"}),
            Action(name="CreateBranch", kwargs={"repo_name": "security-scanner-pro", "source_branch": "main", "new_branch": "feature-sarif"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "security-scanner-pro", "branch": "feature-sarif", "path": "src/scanner.py", "content": "print('sarif-v1')"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "security-scanner-pro", "branch": "feature-sarif", "path": "README.md", "content": "# security-scanner-pro"}),
            Action(name="CommitChangesToBranch", kwargs={"repo_name": "security-scanner-pro", "branch": "feature-sarif", "commit_message": "Add SARIF support scaffolding"}),
            Action(name="CreatePullRequest", kwargs={"repo_name": "security-scanner-pro", "title": "Add SARIF output support", "body": "Introduce SARIF output skeleton.", "base": "main", "head": "feature-sarif"}),
            Action(name="RequestPullRequestReviewers", kwargs={"repo_name": "security-scanner-pro", "pr_number": 1, "reviewers": ["qa-mike", "dev-sue"]}),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "security-scanner-pro", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "security-scanner-pro", "pr_number": 1}),
            Action(name="CreateRelease", kwargs={"repo_name": "security-scanner-pro", "tag": "v0.5.0", "title": "SARIF support", "body": "Initial SARIF output format release."}),
            Action(name="CreateIssue", kwargs={"repo_name": "security-scanner-pro", "title": "Post-release verification", "body": "Validate SARIF output end-to-end.", "labels": ["release"]}),
            Action(name="AppendTerminal", kwargs={"message": "security-scanner-pro v0.5.0 released."}),
            Action(name="GetLatestRelease", kwargs={"repo_name": "security-scanner-pro"}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "security-scanner-pro"',
            '"message": "Pull request opened", "title": "Add SARIF output support", "pr_number": 1',
            '"message": "Reviewers requested.", "requested_reviewers": ["dev-sue", "qa-mike"]',
            '"message": "Pull request merged.", "merged": "true"',
            '"message": "Release created.", "repo_name": "security-scanner-pro", "tag_name": "v0.5.0"',
            '"tag_name": "v0.5.0", "title": "SARIF support"',
            '"message": "Issue created", "number": 1',
            '"message": "security-scanner-pro v0.5.0 released."',
        ],
    ),

    # 47
    Task(
        annotator="0",
        user_id="task_47",
    instruction=(
        "Assume the role of 'infra-lead'. Fulfill the following final state, ensuring all values are precise and case-sensitive: • A repository identified as 'k8s-ci-pipelines' is present and owned by you; it's set to 'public' visibility, with 'main' as the default branch. The repository topics must contain 'kubernetes'. • Ensure a branch named 'feature-alerts' is available. Within this branch, the file 'kubernetes/alerts.yaml' holds exactly 'alertmanager: routes: placeholder-v2', and 'docs/alerts.md' has precisely '# Alerts Runbook'. • The latest commit on 'feature-alerts' should bear the message 'Add alert routing and runbook'. • Submit pull request # Target the main branch from the feature-alerts head, with the title 'Introduce alert routing' and body 'Add Alertmanager routes and docs.', ensuring approval and merging. • Activate branch protection on 'main' with the rule {'required_reviews': 1}. • An issue named 'Branch protection enabled on main' must exist with the body 'Required reviews set to 1.' and tagged 'security'. • The terminal log should contain a single new entry stating 'k8s-ci-pipelines protection
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
            Action(name="CreateRepository", kwargs={"repo_name": "k8s-ci-pipelines", "visibility": "public", "default_branch": "main"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "k8s-ci-pipelines", "topic": "kubernetes"}),
            Action(name="CreateBranch", kwargs={"repo_name": "k8s-ci-pipelines", "source_branch": "main", "new_branch": "feature-alerts"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "k8s-ci-pipelines", "branch": "feature-alerts", "path": "kubernetes/alerts.yaml", "content": "alertmanager: routes: placeholder-v2"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "k8s-ci-pipelines", "branch": "feature-alerts", "path": "docs/alerts.md", "content": "# Alerts Runbook"}),
            Action(name="CommitChangesToBranch", kwargs={"repo_name": "k8s-ci-pipelines", "branch": "feature-alerts", "commit_message": "Add alert routing and runbook"}),
            Action(name="CreatePullRequest", kwargs={"repo_name": "k8s-ci-pipelines", "title": "Introduce alert routing", "body": "Add Alertmanager routes and docs.", "base": "main", "head": "feature-alerts"}),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "k8s-ci-pipelines", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "k8s-ci-pipelines", "pr_number": 1}),
            Action(name="SetBranchProtection", kwargs={"repo_name": "k8s-ci-pipelines", "branch": "main", "protected": "true", "rules": {"required_reviews": 1}}),
            Action(name="CreateIssue", kwargs={"repo_name": "k8s-ci-pipelines", "title": "Branch protection enabled on main", "body": "Required reviews set to 1.", "labels": ["security"]}),
            Action(name="AppendTerminal", kwargs={"message": "k8s-ci-pipelines protection enabled on main."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "k8s-ci-pipelines"',
            '"message": "Pull request opened", "title": "Introduce alert routing", "pr_number": 1',
            '"message": "Pull request merged.", "merged": "true"',
            '"message": "Branch protection enabled."',
            '"message": "Issue created", "number": 1',
            '"message": "k8s-ci-pipelines protection enabled on main."',
        ],
    ),

    # 48
    Task(
        annotator="0",
        user_id="task_48",
    instruction=(
        "Take on the responsibility of 'ui-developer'. Achieve the following end result, ensuring all data is exact and case-sensitive: • A repository known as 'react-dashboard-pro' should be available and managed by you; its visibility set to 'public', with 'main' as the default branch. The repository topics are to include 'frontend' and 'react'. • Confirm the existence of a branch 'feature-dark-mode'. On this branch, 'src/theme/dark.js' must contain exactly 'export const theme = 'dark';', while 'docs/dark-mode.md' should precisely be '# Dark mode user guide'. • The most recent commit on 'feature-dark-mode' must carry the message 'Implement dark mode theme'. • Establish pull request # 1 directing base 'main' from head 'feature-dark-mode' titled 'Add dark mode theme' with body 'Introduce dark mode option for dashboard.', including 'qa-mike' and 'design-team' as requested reviewers for approval and merging. • Confirm the existence of a release on 'react-dashboard-pro' tagged 'v2.0.0', with title 'Dark mode release' and body 'Dark mode theme is now available.'. The latest release should reference tag 'v2.0.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "ui-developer"}),
            Action(name="CreateRepository", kwargs={"repo_name": "react-dashboard-pro", "visibility": "public", "default_branch": "main"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "react-dashboard-pro", "topic": "frontend"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "react-dashboard-pro", "topic": "react"}),
            Action(name="CreateBranch", kwargs={"repo_name": "react-dashboard-pro", "source_branch": "main", "new_branch": "feature-dark-mode"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "react-dashboard-pro", "branch": "feature-dark-mode", "path": "src/theme/dark.js", "content": "export const theme = 'dark';"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "react-dashboard-pro", "branch": "feature-dark-mode", "path": "docs/dark-mode.md", "content": "# Dark mode user guide"}),
            Action(name="CommitChangesToBranch", kwargs={"repo_name": "react-dashboard-pro", "branch": "feature-dark-mode", "commit_message": "Implement dark mode theme"}),
            Action(name="CreatePullRequest", kwargs={"repo_name": "react-dashboard-pro", "title": "Add dark mode theme", "body": "Introduce dark mode option for dashboard.", "base": "main", "head": "feature-dark-mode"}),
            Action(name="RequestPullRequestReviewers", kwargs={"repo_name": "react-dashboard-pro", "pr_number": 1, "reviewers": ["qa-mike", "design-team"]}),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "react-dashboard-pro", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "react-dashboard-pro", "pr_number": 1}),
            Action(name="CreateRelease", kwargs={"repo_name": "react-dashboard-pro", "tag": "v2.0.0", "title": "Dark mode release", "body": "Dark mode theme is now available."}),
            Action(name="GetLatestRelease", kwargs={"repo_name": "react-dashboard-pro"}),
            Action(name="CreateIssue", kwargs={"repo_name": "react-dashboard-pro", "title": "Dark mode documentation", "body": "Add instructions for enabling dark mode in user guide.", "labels": ["docs"]}),
            Action(name="SetBranchProtection", kwargs={"repo_name": "react-dashboard-pro", "branch": "main", "protected": "true", "rules": {"required_reviews": 2}}),
            Action(name="AppendTerminal", kwargs={"message": "react-dashboard-pro v2.0.0 released with dark mode."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "react-dashboard-pro"',
            '"message": "Pull request opened", "title": "Add dark mode theme", "pr_number": 1',
            '"message": "Reviewers requested.", "requested_reviewers": ["qa-mike", "design-team"]',
            '"message": "Pull request merged.", "merged": "true"',
            '"message": "Release created.", "repo_name": "react-dashboard-pro", "tag_name": "v2.0.0"',
            '"tag_name": "v2.0.0", "title": "Dark mode release"',
            '"message": "Issue created", "number": 1',
            '"message": "Branch protection enabled."',
            '"message": "react-dashboard-pro v2.0.0 released with dark mode."',
        ],
    ),

    # 49
    Task(
        annotator="0",
        user_id="task_49",
    instruction=(
        "Your team name is 'platform-team'. Ensure the following final state, maintaining all values precisely and case-sensitive: • A repository called 'infra-containers' must be present and owned by your team; its visibility should be 'public' and its default branch 'main'. The repository should have 'docker' as one of its topics. • A branch termed 'feature-registry' should be present. Within that branch, ensure the file 'docker-compose.yml' includes exactly 'services: placeholder-v1' and 'docs/registry.md' contains precisely '# Private registry setup'. • The latest commit on 'feature-registry' should have the message 'Add registry compose and docs'. • Pull request # 1 must target the base 'main' from the head 'feature-registry' with the title 'Add container registry' and the body 'Introduce docker-compose for registry and docs.', requiring approval and merging. • A release tagged 'v0.3.0', titled 'Registry compose' with the body 'Adds docker-compose and docs.' should be present on 'infra-containers'. • An issue tagged 'ops' titled 'Track registry rollout' must be created with the body 'Coordinate rollout with
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "platform-team"}),
            Action(name="CreateRepository", kwargs={"repo_name": "infra-containers", "visibility": "public", "default_branch": "main"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "infra-containers", "topic": "docker"}),
            Action(name="CreateBranch", kwargs={"repo_name": "infra-containers", "source_branch": "main", "new_branch": "feature-registry"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "infra-containers", "branch": "feature-registry", "path": "docker-compose.yml", "content": "services: placeholder-v1"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "infra-containers", "branch": "feature-registry", "path": "docs/registry.md", "content": "# Private registry setup"}),
            Action(name="CommitChangesToBranch", kwargs={"repo_name": "infra-containers", "branch": "feature-registry", "commit_message": "Add registry compose and docs"}),
            Action(name="CreatePullRequest", kwargs={"repo_name": "infra-containers", "title": "Add container registry", "body": "Introduce docker-compose for registry and docs.", "base": "main", "head": "feature-registry"}),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "infra-containers", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "infra-containers", "pr_number": 1}),
            Action(name="CreateRelease", kwargs={"repo_name": "infra-containers", "tag": "v0.3.0", "title": "Registry compose", "body": "Adds docker-compose and docs."}),
            Action(name="CreateIssue", kwargs={"repo_name": "infra-containers", "title": "Track registry rollout", "body": "Coordinate rollout with ops.", "labels": ["ops"]}),
            Action(name="SetBranchProtection", kwargs={"repo_name": "infra-containers", "branch": "main", "protected": "true", "rules": {"required_reviews": 1}}),
            Action(name="AppendTerminal", kwargs={"message": "infra-containers v0.3.0 released."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "infra-containers"',
            '"message": "Pull request opened", "title": "Add container registry", "pr_number": 1',
            '"message": "Pull request merged.", "merged": "true"',
            '"message": "Release created.", "repo_name": "infra-containers", "tag_name": "v0.3.0"',
            '"message": "Issue created", "number": 1',
            '"message": "Branch protection enabled."',
            '"message": "infra-containers v0.3.0 released."',
        ],
    ),

    # 50
    Task(
        annotator="0",
        user_id="task_50",
    instruction=(
        "Your team is 'server-main'. Achieve the following final state, ensuring all values are precise and case-sensitive: • A repository titled 'backend-payment-service' needs to exist, owned by you; its visibility set to 'public' with 'main' as the default branch. The repository should have the topics 'payments' and 'backend'. • A branch named 'feature-payment-webhooks' must exist. Within this branch, 'src/webhooks.py' should contain exactly 'print('webhooks-v1')' and 'docs/webhooks.md' should have exactly '# Webhooks guide'. • The latest commit on 'feature-payment-webhooks' should feature the message 'Implement payment webhooks'. • Pull request # 1 should merge the 'feature-payment-webhooks' branch into the 'main' base, with the title 'Add payment webhooks' and the description 'Introduce webhook handlers and docs.', reviewed by 'qa-erin' and 'payments-lead', and then approved. • Activate branch protection on 'main', enforcing the rule {'required_reviews': 2}. • A release named 'v1.3.0', titled 'Payment webhooks' and described as 'Initial webhook support.' must be
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "server-main"}),
            Action(name="CreateRepository", kwargs={"repo_name": "backend-payment-service", "visibility": "public", "default_branch": "main"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "backend-payment-service", "topic": "payments"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "backend-payment-service", "topic": "backend"}),
            Action(name="CreateBranch", kwargs={"repo_name": "backend-payment-service", "source_branch": "main", "new_branch": "feature-payment-webhooks"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "backend-payment-service", "branch": "feature-payment-webhooks", "path": "src/webhooks.py", "content": "print('webhooks-v1')"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "backend-payment-service", "branch": "feature-payment-webhooks", "path": "docs/webhooks.md", "content": "# Webhooks guide"}),
            Action(name="CommitChangesToBranch", kwargs={"repo_name": "backend-payment-service", "branch": "feature-payment-webhooks", "commit_message": "Implement payment webhooks"}),
            Action(name="CreatePullRequest", kwargs={"repo_name": "backend-payment-service", "title": "Add payment webhooks", "body": "Introduce webhook handlers and docs.", "base": "main", "head": "feature-payment-webhooks"}),
            Action(name="RequestPullRequestReviewers", kwargs={"repo_name": "backend-payment-service", "pr_number": 1, "reviewers": ["qa-erin", "payments-lead"]}),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "backend-payment-service", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "backend-payment-service", "pr_number": 1}),
            Action(name="SetBranchProtection", kwargs={"repo_name": "backend-payment-service", "branch": "main", "protected": "true", "rules": {"required_reviews": 2}}),
            Action(name="CreateRelease", kwargs={"repo_name": "backend-payment-service", "tag": "v1.3.0", "title": "Payment webhooks", "body": "Initial webhook support."}),
            Action(name="GetLatestRelease", kwargs={"repo_name": "backend-payment-service"}),
            Action(name="CreateIssue", kwargs={"repo_name": "backend-payment-service", "title": "Post-deploy checklist", "body": "Validate webhook delivery and retries.", "labels": ["release"]}),
            Action(name="AppendTerminal", kwargs={"message": "backend-payment-service v1.3.0 released."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "backend-payment-service"',
            '"message": "Pull request opened", "title": "Add payment webhooks", "pr_number": 1',
            '"message": "Reviewers requested.", "requested_reviewers": ["payments-lead", "qa-erin"]',
            '"message": "Pull request merged.", "merged": "true"',
            '"message": "Branch protection enabled."',
            '"message": "Release created.", "repo_name": "backend-payment-service", "tag_name": "v1.3.0"',
            '"tag_name": "v1.3.0", "title": "Payment webhooks"',
            '"message": "Issue created", "number": 1',
            '"message": "backend-payment-service v1.3.0 released."',
        ],
    ),

    # 51
    Task(
        annotator="0",
        user_id="task_51",
    instruction=(
        "Identify yourself as 'maya-w'. Achieve the following end result, ensuring all values are precise and maintain case sensitivity: • A repository called 'acme-sql-service' is in existence and owned by you; it is set to 'public' visibility and its default branch is 'main'. The repository topics must include 'database'. • The branch 'feature-sanitize-input' is available. On this branch, the 'src/sanitize.py' file must contain exactly 'def sanitize(v): return str(v)' and the 'docs/security.md' file must exactly include '# SQL sanitization patch'. • The latest commit on 'feature-sanitize-input' bears the message 'Add input sanitization helper'. • Pull request # The merge request targeting the 'main' branch from 'feature-sanitize-input' has been approved and integrated, titled 'Add SQL sanitization' with the description 'Introduce helper to sanitize SQL input.' A release for 'acme-sql-service' exists, tagged 'v0.2.0' and named 'Sanitization patch,' accompanied by the description 'Helper added for SQL sanitization.' There is an open issue titled 'Review sanitization helper,' which states 'Validate new helper across
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="CreateRepository", kwargs={"repo_name": "acme-sql-service", "visibility": "public", "default_branch": "main"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "acme-sql-service", "topic": "database"}),
            Action(name="CreateBranch", kwargs={"repo_name": "acme-sql-service", "source_branch": "main", "new_branch": "feature-sanitize-input"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "acme-sql-service", "branch": "feature-sanitize-input", "path": "src/sanitize.py", "content": "def sanitize(v): return str(v)"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "acme-sql-service", "branch": "feature-sanitize-input", "path": "docs/security.md", "content": "# SQL sanitization patch"}),
            Action(name="CommitChangesToBranch", kwargs={"repo_name": "acme-sql-service", "branch": "feature-sanitize-input", "commit_message": "Add input sanitization helper"}),
            Action(name="CreatePullRequest", kwargs={"repo_name": "acme-sql-service", "title": "Add SQL sanitization", "body": "Introduce helper to sanitize SQL input.", "base": "main", "head": "feature-sanitize-input"}),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "acme-sql-service", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "acme-sql-service", "pr_number": 1}),
            Action(name="CreateRelease", kwargs={"repo_name": "acme-sql-service", "tag": "v0.2.0", "title": "Sanitization patch", "body": "Helper added for SQL sanitization."}),
            Action(name="CreateIssue", kwargs={"repo_name": "acme-sql-service", "title": "Review sanitization helper", "body": "Validate new helper across services.", "labels": ["security"]}),
            Action(name="AppendTerminal", kwargs={"message": "acme-sql-service v0.2.0 released."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "acme-sql-service"',
            '"message": "Pull request opened", "title": "Add SQL sanitization", "pr_number": 1',
            '"message": "Pull request merged.", "merged": "true"',
            '"message": "Release created.", "repo_name": "acme-sql-service", "tag_name": "v0.2.0"',
            '"message": "Issue created", "number": 1',
            '"message": "acme-sql-service v0.2.0 released."',
        ],
    ),

    # 52. (backend-core) Timeout policy documentation has been created, reviewed, merged, and published.
    Task(
        annotator='0',
        user_id="task_52",
    instruction=(
        "Identify yourself as 'server-main'. Upon task completion, the repository 'payments-service' must meet ALL of the following conditions: • A documentation file resides at 'docs/TIMEOUT_POLICY.md' containing EXACT text 'Default request timeout is 60s. 3DS flows may extend to 90s. Retries: none.'. • This update starts from a branch named 'feature-timeout-policy' and is documented by a commit with the message precisely 'Document timeout policy'. • The modification is incorporated into 'main' via a reviewed pull request titled 'Document timeout policy', with a review request directed to 'qa-erin', and it has been merged. • A release is available with tag 'v0.2.1', title 'Timeout policy docs', and body 'Publish timeout policy documentation.', with the most recent release showing tag 'v0.2.1'. • There is an existing issue titled 'Timeout policy docs published' with body 'Docs merged and released as v0.2.1.' bearing the 'documentation' label. • The terminal audit log must include the EXACT message 'payments-service timeout policy docs published and released as v0.2.1.'."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "server-main"}),
            Action(name="GetRepository", kwargs={"repo_name": "payments-service"}),
            Action(name="CreateBranch", kwargs={"repo_name": "payments-service", "source_branch": "main", "new_branch": "feature-timeout-policy"}),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "payments-service",
                "branch": "feature-timeout-policy",
                "path": "docs/TIMEOUT_POLICY.md",
                "content": "Default request timeout is 60s. 3DS flows may extend to 90s. Retries: none."
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "payments-service",
                "branch": "feature-timeout-policy",
                "commit_message": "Document timeout policy"
            }),
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "payments-service",
                "title": "Document timeout policy",
                "base": "main",
                "head": "feature-timeout-policy"
            }),
            Action(name="RequestPullRequestReviewers", kwargs={
                "repo_name": "payments-service",
                "pr_number": 1,
                "reviewers": ["qa-erin"]
            }),
            Action(name="MergePullRequest", kwargs={"repo_name": "payments-service", "pr_number": 1}),
            Action(name="CreateRelease", kwargs={
                "repo_name": "payments-service",
                "tag": "v0.2.1",
                "title": "Timeout policy docs",
                "body": "Publish timeout policy documentation."
            }),
            Action(name="GetLatestRelease", kwargs={"repo_name": "payments-service"}),
            Action(name="CreateIssue", kwargs={
                "repo_name": "payments-service",
                "title": "Timeout policy docs published",
                "body": "Docs merged and released as v0.2.1.",
                "labels": ["documentation"]
            }),
            Action(name="AppendTerminal", kwargs={
                "message": "payments-service timeout policy docs published and released as v0.2.1."
            }),
        ],
        outputs=[
            '"message": "Branch created", "new_branch": "feature-timeout-policy", "from": "main"',
            '"message": "Committed to branch", "repo": "payments-service", "branch": "feature-timeout-policy", "commit_sha": "sha_0000000000000000000000000000000000000000"',
            '"message": "Pull request opened", "title": "Document timeout policy", "base": "main", "head": "feature-timeout-policy", "pr_number": 1',
            '"message": "Reviewers requested.", "pr_number": 1',
            '"message": "Pull request merged.", "merged": "true", "merge_method": "merge"',
            '"message": "Release created.", "repo_name": "payments-service", "tag_name": "v0.2.1", "title": "Timeout policy docs"',
            '"tag_name": "v0.2.1", "title": "Timeout policy docs"',
            '"message": "Issue created", "number": 1',
            '"timestamp": "2025-08-21T12:00:00Z", "message": "payments-service timeout policy docs published and released as v0.2.1."',
        ],
    ),

    # 53
    Task(
        annotator="0",
        user_id="task_53",
    instruction=(
        "You are 'docs-sophia'. Manage the following final outcome, ensuring all values are precise and maintain case sensitivity: • A repository under the name 'product-docs' is present and is owned by you; its visibility setting is 'public', and its default branch is named 'main'. The repository should have 'docs' and 'markdown' as topics. • Implement branch protection on the branch 'main' with strictly these rules {'required_reviews': 1}. • There is a release on 'product-docs' identified by tag 'v1.0.0', with title 'Initial documentation', and the body 'Bootstrap product documentation.'. • Create an issue with the title 'Add onboarding guide' having the body 'Create onboarding section in docs.' and tagged 'docs'. • The terminal log must contain exactly one newly added entry that says 'product-docs v1.0.0 published.' Every condition must be met in a clean database environment; employ deterministic values only."
    ),
        actions=[
        Action(name="GetMe", kwargs={"username": "docs-sophia"}),
        Action(name="CreateRepository", kwargs={"repo_name": "product-docs", "visibility": "public", "default_branch": "main"}),
        Action(name="AddRepoTopic", kwargs={"repo_name": "product-docs", "topic": "docs"}),
        Action(name="AddRepoTopic", kwargs={"repo_name": "product-docs", "topic": "markdown"}),
        Action(name="SetBranchProtection", kwargs={"repo_name": "product-docs", "branch": "main", "protected": "true", "rules": {"required_reviews": 1}}),
        Action(name="CreateRelease", kwargs={"repo_name": "product-docs", "tag": "v1.0.0", "title": "Initial documentation", "body": "Bootstrap product documentation."}),
        Action(name="CreateIssue", kwargs={"repo_name": "product-docs", "title": "Add onboarding guide", "body": "Create onboarding section in docs.", "labels": ["docs"]}),
        Action(name="AppendTerminal", kwargs={"message": "product-docs v1.0.0 published."}),
        ],
        outputs=[
        '"message": "Repository created", "repo_name": "product-docs"',
        '"message": "Branch protection enabled."',
        '"message": "Release created.", "repo_name": "product-docs", "tag_name": "v1.0.0"',
        '"message": "Issue created", "number": 1',
        '"message": "product-docs v1.0.0 published."',
        ],
    ),

    # 54
    Task(
        annotator='0',
        user_id="task_54",
    instruction=(
        "You are 'infra-lead'. Verify that 'k8s-monitoring' has published and consolidated documentation regarding the Prometheus retention policy. This documentation should be located at 'docs/RETENTION_POLICY.md' and must contain the exact text 'Prometheus retention is 30 days. Compaction enabled. Storage class: gp3.'. Implement this change on a branch called 'feature-retention-policy', merge it into 'main' through a reviewed pull request titled 'Document Prometheus retention' (request review from 'platform-team'). Utilize the specific commit message 'Document 30-day Prometheus retention'. Confirm completion by creating an issue titled 'Prometheus retention policy documented' with the body 'Retention set to 30 days and documented.' labeled 'documentation', and enter the exact terminal audit note 'k8s-monitoring retention policy docs merged and recorded.'."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
            Action(name="GetRepository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="CreateBranch", kwargs={"repo_name": "k8s-monitoring", "source_branch": "main", "new_branch": "feature-retention-policy"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "k8s-monitoring", "branch": "feature-retention-policy", "path": "docs/RETENTION_POLICY.md", "content": "Prometheus retention is 30 days. Compaction enabled. Storage class: gp3."}),
            Action(name="CommitChangesToBranch", kwargs={"repo_name": "k8s-monitoring", "branch": "feature-retention-policy", "commit_message": "Document 30-day Prometheus retention"}),
            Action(name="CreatePullRequest", kwargs={"repo_name": "k8s-monitoring", "title": "Document Prometheus retention", "base": "main", "head": "feature-retention-policy"}),
            Action(name="RequestPullRequestReviewers", kwargs={"repo_name": "k8s-monitoring", "pr_number": 1, "reviewers": ["platform-team"]}),
            Action(name="MergePullRequest", kwargs={"repo_name": "k8s-monitoring", "pr_number": 1}),
            Action(name="CreateIssue", kwargs={"repo_name": "k8s-monitoring", "title": "Prometheus retention policy documented", "body": "Retention set to 30 days and documented.", "labels": ["documentation"]}),
            Action(name="AppendTerminal", kwargs={"message": "k8s-monitoring retention policy docs merged and recorded."}),
        ],
        outputs=[
            '"message": "Branch created", "new_branch": "feature-retention-policy", "from": "main"',
            '"message": "Committed to branch", "repo": "k8s-monitoring", "branch": "feature-retention-policy", "commit_sha": "sha_0000000000000000000000000000000000000000"',
            '"message": "Pull request opened", "title": "Document Prometheus retention", "base": "main", "head": "feature-retention-policy", "pr_number": 1',
            '"message": "Reviewers requested.", "pr_number": 1',
            '"message": "Pull request merged.", "merged": "true", "merge_method": "merge"',
            '"message": "Issue created", "number": 1',
            '"timestamp": "2025-08-21T12:00:00Z", "message": "k8s-monitoring retention policy docs merged and recorded."',
        ],
    ),

    # 55
    Task(
        annotator="0",
        user_id="task_55",
    instruction=(
        "You are 'qa-mike'. Ensure the following final state, with all specifics precise and case-sensitive: • A repository named 'qa-tests' is present and owned by you; its visibility must be 'public' and its default branch should be 'main'. The repository topics include 'qa'. • A release is available on 'qa-tests' with tag 'v0.1.0', title 'Initial QA setup', and body 'Bootstrap test repository.'. • There is an issue titled 'Write first test cases' with body 'Add login and signup test coverage.' labeled 'qa'. • The terminal log should have exactly one appended entry with the message 'qa-tests v0.1.0 created.' All criteria must be met during a clean database execution; use deterministic values only."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "qa-mike"}),
            Action(name="CreateRepository", kwargs={"repo_name": "qa-tests", "visibility": "public", "default_branch": "main"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "qa-tests", "topic": "qa"}),
            Action(name="CreateRelease", kwargs={"repo_name": "qa-tests", "tag": "v0.1.0", "title": "Initial QA setup", "body": "Bootstrap test repository."}),
            Action(name="CreateIssue", kwargs={"repo_name": "qa-tests", "title": "Write first test cases", "body": "Add login and signup test coverage.", "labels": ["qa"]}),
            Action(name="AppendTerminal", kwargs={"message": "qa-tests v0.1.0 created."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "qa-tests"',
            '"message": "Release created.", "repo_name": "qa-tests", "tag_name": "v0.1.0"',
            '"message": "Issue created", "number": 1',
            '"message": "qa-tests v0.1.0 created."',
        ],
    ),

    # 56. (ui-team) Release ThemeProvider documentation with security measures in place, including protection and audit.
    Task(
        annotator='0',
        user_id="task_56",
    instruction=(
        "You are 'design-team'. Your task is to handle the repository 'ui-kit' and accomplish the tasks detailed as follows: 1) Branch 'main' is safeguarded with rules exactly {\"require_reviews\": true, \"enforce_admins\": true}. 2) The file 'docs/THEME_PROVIDER.md' is present on 'main' with the exact content 'Use ThemeProvider at the app root. Props: theme (required). Example: <ThemeProvider theme={Theme}>'. This modification originates on a branch called 'feature-theme-docs' and is represented by a commit whose message is exactly 'Add ThemeProvider documentation'. The edit is merged into 'main' through a reviewed pull request titled 'ThemeProvider docs'; a review request is made to 'ui-dev', and an approval review with the exact comment 'LGTM' is documented. 3) A release is available with tag 'v1.0.1', title 'Theme docs', and body 'Add ThemeProvider documentation.', and the most recent release shows tag 'v1.0.1'. 4) An issue is titled 'ThemeProvider docs published' with body 'Docs merged and released as v1.0.1.' labeled 'documentation'. 5) The terminal audit includes the exact record 'ui-kit ThemeProvider docs published and released as v1.0.1.'."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "design-team"}),
            Action(
                name="SetBranchProtection",
                kwargs={
                    "repo_name": "ui-kit",
                    "branch": "main",
                    "protected": "true",
                    "rules": {"require_reviews": "true", "enforce_admins": "true"},
                },
            ),
            Action(name="CreateBranch", kwargs={"repo_name": "ui-kit", "source_branch": "main", "new_branch": "feature-theme-docs"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "ui-kit", "branch": "feature-theme-docs", "path": "docs/THEME_PROVIDER.md", "content": "Use ThemeProvider at the app root. Props: theme (required). Example: <ThemeProvider theme={Theme}>"}),
            Action(name="CommitChangesToBranch", kwargs={"repo_name": "ui-kit", "branch": "feature-theme-docs", "commit_message": "Add ThemeProvider documentation"}),
            Action(name="CreatePullRequest", kwargs={"repo_name": "ui-kit", "title": "ThemeProvider docs", "base": "main", "head": "feature-theme-docs"}),
            Action(name="RequestPullRequestReviewers", kwargs={"repo_name": "ui-kit", "pr_number": 1, "reviewers": ["ui-dev"]}),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "ui-kit", "pr_number": 1, "review_decision": "approve", "comment": "LGTM"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "ui-kit", "pr_number": 1}),
            Action(name="CreateRelease", kwargs={"repo_name": "ui-kit", "tag": "v1.0.1", "title": "Theme docs", "body": "Add ThemeProvider documentation."}),
            Action(name="GetLatestRelease", kwargs={"repo_name": "ui-kit"}),
            Action(name="CreateIssue", kwargs={"repo_name": "ui-kit", "title": "ThemeProvider docs published", "body": "Docs merged and released as v1.0.1.", "labels": ["documentation"]}),
            Action(name="AppendTerminal", kwargs={"message": "ui-kit ThemeProvider docs published and released as v1.0.1."}),
        ],
        outputs=[
            '"message": "Branch protection enabled.", "repo_name": "ui-kit", "branch": "main", "protected": "true"',
            '"message": "Branch created", "new_branch": "feature-theme-docs", "from": "main"',
            '"message": "Committed to branch", "repo": "ui-kit", "branch": "feature-theme-docs", "commit_sha": "sha_0000000000000000000000000000000000000000"',
            '"message": "Pull request opened", "title": "ThemeProvider docs", "base": "main", "head": "feature-theme-docs", "pr_number": 1',
            '"message": "Reviewers requested.", "pr_number": 1',
            '"message": "Review submitted."',
            '"message": "Pull request merged.", "merged": "true", "merge_method": "merge"',
            '"message": "Release created.", "repo_name": "ui-kit", "tag_name": "v1.0.1", "title": "Theme docs"',
            '"tag_name": "v1.0.1", "body": "Add ThemeProvider documentation."',
            '"message": "Issue created", "number": 1',
            '"printed_ts": "2025-08-21T12:00:00Z", "message": "ui-kit ThemeProvider docs published and released as v1.0.1."',
        ],
    ),

    # 57
    Task(
        annotator="0",
        user_id="task_57",
    instruction=(
        "You are 'maintainer-tom'. Coordinate achieving the following end state, with all values precise and case‑sensitive: • A repository named 'tooling-maintenance' must exist and be owned by you; its visibility should be 'public' and its default branch 'main'. • Ensure a release exists on 'tooling-maintenance' with tag 'v0.1.0', title 'Initial maintenance setup', and body 'Bootstrap maintenance repo.'. • There should be an issue titled 'Create weekly maintenance checklist' with body 'Define checklist template for weekly runs.' labeled 'maintenance'. • Confirm the terminal log has exactly one appended entry with the message 'tooling-maintenance v0.1.0 created.' All conditions need to be fulfilled in a fresh database run; apply deterministic values only."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maintainer-tom"}),
            Action(name="CreateRepository", kwargs={"repo_name": "tooling-maintenance", "visibility": "public", "default_branch": "main"}),
            Action(name="CreateRelease", kwargs={"repo_name": "tooling-maintenance", "tag": "v0.1.0", "title": "Initial maintenance setup", "body": "Bootstrap maintenance repo."}),
            Action(name="CreateIssue", kwargs={"repo_name": "tooling-maintenance", "title": "Create weekly maintenance checklist", "body": "Define checklist template for weekly runs.", "labels": ["maintenance"]}),
            Action(name="AppendTerminal", kwargs={"message": "tooling-maintenance v0.1.0 created."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "tooling-maintenance"',
            '"message": "Release created.", "repo_name": "tooling-maintenance", "tag_name": "v0.1.0"',
            '"message": "Issue created", "number": 1',
            '"message": "tooling-maintenance v0.1.0 created."',
        ],
    ),

    # 59
    Task(
        annotator="0",
        user_id="task_59",
    instruction=(
        "You are 'tech-lead-tara'. Handle achieving the following end state, with all values precise and case‑sensitive: • A repository named 'automation-ci' must exist and be owned by you; its visibility should be 'public' and its default branch 'main'. The repository topics need to include both 'automation' and 'ci'. • Ensure the existence of a branch 'feature-ci-config'. On that branch, verify the file '.github/workflows/ci.yml' contains exactly 'name: ci'. • Confirm the latest commit on 'feature-ci-config' includes the message 'Add CI workflow'. • Branch protection is activated on branch 'main' with rules precisely {'required_reviews': 1}. • A release must exist on 'automation-ci' with tag 'v0.1.0', title 'CI bootstrap', and body 'Adds initial CI workflow.'. • An issue titled 'Expand CI matrix' should exist with body 'Add Python and Node matrix to CI.' labeled 'ci'. • Verify the terminal log has exactly one appended entry with the message 'automation-ci v0.1.0 released.' All conditions need to be fulfilled in a fresh database run; apply deterministic values only."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "tech-lead-tara"}),
            Action(name="CreateRepository", kwargs={"repo_name": "automation-ci", "visibility": "public", "default_branch": "main"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "automation-ci", "topic": "automation"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "automation-ci", "topic": "ci"}),
            Action(name="CreateBranch", kwargs={"repo_name": "automation-ci", "source_branch": "main", "new_branch": "feature-ci-config"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "automation-ci", "branch": "feature-ci-config", "path": ".github/workflows/ci.yml", "content": "name: ci"}),
            Action(name="CommitChangesToBranch", kwargs={"repo_name": "automation-ci", "branch": "feature-ci-config", "commit_message": "Add CI workflow"}),
            Action(name="SetBranchProtection", kwargs={"repo_name": "automation-ci", "branch": "main", "protected": "true", "rules": {"required_reviews": 1}}),
            Action(name="CreateRelease", kwargs={"repo_name": "automation-ci", "tag": "v0.1.0", "title": "CI bootstrap", "body": "Adds initial CI workflow."}),
            Action(name="CreateIssue", kwargs={"repo_name": "automation-ci", "title": "Expand CI matrix", "body": "Add Python and Node matrix to CI.", "labels": ["ci"]}),
            Action(name="AppendTerminal", kwargs={"message": "automation-ci v0.1.0 released."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "automation-ci"',
            '"message": "Branch protection enabled."',
            '"message": "Release created.", "repo_name": "automation-ci", "tag_name": "v0.1.0"',
            '"message": "Issue created", "number": 1',
            '"message": "automation-ci v0.1.0 released."',
        ],
    ),

    # 61
    Task(
        annotator="0",
        user_id="task_61",
    instruction=(
        "You are appointed as 'design-lead'. Accomplish the final outcomes, ensuring all values are precise and case-sensitive: • Initially, create a repository named 'design-system' privately with the default branch as 'main', then change its name to 'design-system-pro' and set its visibility to 'public'. Include 'design' as the repository topic. • Confirm the existence of a branch called 'feature-guidelines', where the file 'docs/guidelines.md' contains exactly '# Design guidelines' and the file 'tokens/colors.json' has precisely '{'brand':'blue'}'. • The newest commit on 'feature-guidelines' should be noted with the message 'Add initial guidelines and tokens'. • Release on 'design-system-pro' should be present, with tag 'v1.0.0', title 'Design system v1', and body text 'Initial guidelines and tokens.'. • Ensure the creation of an issue titled 'Track design system adoption' with the description 'Roll out across products.' and labeled as 'design'. • In the terminal log, add exactly one new entry with the content 'design-system-pro v1.0.0 published.' Complete all tasks using a new database run with deterministic specifications only."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "design-lead"}),
            Action(name="CreateRepository", kwargs={"repo_name": "design-system", "visibility": "private", "default_branch": "main"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "design-system", "topic": "design"}),
            Action(name="RenameRepository", kwargs={"old_name": "design-system", "new_name": "design-system-pro"}),
            Action(name="SetRepositoryVisibility", kwargs={"repo_name": "design-system-pro", "visibility": "public"}),
            Action(name="CreateBranch", kwargs={"repo_name": "design-system-pro", "source_branch": "main", "new_branch": "feature-guidelines"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "design-system-pro", "branch": "feature-guidelines", "path": "docs/guidelines.md", "content": "# Design guidelines"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "design-system-pro", "branch": "feature-guidelines", "path": "tokens/colors.json", "content": "{'brand':'blue'}"}),
            Action(name="CommitChangesToBranch", kwargs={"repo_name": "design-system-pro", "branch": "feature-guidelines", "commit_message": "Add initial guidelines and tokens"}),
            Action(name="CreateRelease", kwargs={"repo_name": "design-system-pro", "tag": "v1.0.0", "title": "Design system v1", "body": "Initial guidelines and tokens."}),
            Action(name="CreateIssue", kwargs={"repo_name": "design-system-pro", "title": "Track design system adoption", "body": "Roll out across products.", "labels": ["design"]}),
            Action(name="AppendTerminal", kwargs={"message": "design-system-pro v1.0.0 published."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "design-system"',
            '"message": "Repository renamed", "new_name": "design-system-pro"',
            '"message": "Visibility updated", "repo_name": "design-system-pro", "visibility": "public"',
            '"message": "Committed to branch", "commit_message": "Add initial guidelines and tokens"',
            '"message": "Release created.", "repo_name": "design-system-pro", "tag_name": "v1.0.0"',
            '"message": "Issue created", "number": 1',
            '"message": "design-system-pro v1.0.0 published."',
        ],
    ),

    # 62
    Task(
        annotator='0',
        user_id="task_62",
    instruction=(
        "You are assigned as 'infra-lead'. Once you conclude the task, verify that the repository state for 'k8s-monitoring' fulfills ALL these criteria: • Ensure a documentation file located at 'docs/LOGGING.md' with the EXACT content 'Centralized logging with Fluent Bit. Logs shipped to Elasticsearch. Retention: 14 days.'. • This amendment should begin on a branch titled 'feature-logging-docs', represented by a commit with the precise message 'Add logging documentation'. • Changes must be integrated into 'main' through a reviewed pull request titled 'Logging docs'; ensure a review request to 'platform-team' and an approval review with the comment 'Approved for observability'. • Assign the topic 'observability' to the repository. • There must be a release with tag 'v1.5.0', title 'Logging docs', and body 'Add logging documentation.', and the latest release must show the tag 'v1.5.0'. • Ensure the presence of an issue titled 'Logging docs published' with content 'Docs merged and released as v1.5.0.' and label it 'documentation'. • The terminal audit log should have the EXACT entry 'k8s-monitoring logging docs published and released as v1.5.0.'."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
            Action(name="GetRepository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="CreateBranch", kwargs={"repo_name": "k8s-monitoring", "source_branch": "main", "new_branch": "feature-logging-docs"}),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "k8s-monitoring",
                "branch": "feature-logging-docs",
                "path": "docs/LOGGING.md",
                "content": "Centralized logging with Fluent Bit. Logs shipped to Elasticsearch. Retention: 14 days."
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "k8s-monitoring",
                "branch": "feature-logging-docs",
                "commit_message": "Add logging documentation"
            }),
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Logging docs",
                "base": "main",
                "head": "feature-logging-docs"
            }),
            Action(name="RequestPullRequestReviewers", kwargs={
                "repo_name": "k8s-monitoring",
                "pr_number": 1,
                "reviewers": ["platform-team"]
            }),
            Action(name="CreatePullRequestReview", kwargs={
                "repo_name": "k8s-monitoring",
                "pr_number": 1,
                "review_decision": "approve",
                "comment": "Approved for observability"
            }),
            Action(name="MergePullRequest", kwargs={"repo_name": "k8s-monitoring", "pr_number": 1}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "k8s-monitoring", "topic": "observability"}),
            Action(name="CreateRelease", kwargs={
                "repo_name": "k8s-monitoring",
                "tag": "v1.5.0",
                "title": "Logging docs",
                "body": "Add logging documentation."
            }),
            Action(name="GetLatestRelease", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="CreateIssue", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Logging docs published",
                "body": "Docs merged and released as v1.5.0.",
                "labels": ["documentation"]
            }),
            Action(name="AppendTerminal", kwargs={"message": "k8s-monitoring logging docs published and released as v1.5.0."}),
        ],
        outputs=[
            '"message": "Branch created", "new_branch": "feature-logging-docs", "from": "main"',
            '"message": "Committed to branch", "repo": "k8s-monitoring", "branch": "feature-logging-docs", "commit_sha": "sha_0000000000000000000000000000000000000000"',
            '"message": "Pull request opened", "title": "Logging docs", "base": "main", "head": "feature-logging-docs", "pr_number": 1',
            '"message": "Reviewers requested.", "pr_number": 1',
            '"message": "Review submitted."',
            '"message": "Pull request merged.", "merged": "true", "merge_method": "merge"',
            '"message": "Topic \'observability\' added."',
            '"message": "Release created.", "repo_name": "k8s-monitoring", "tag_name": "v1.5.0", "title": "Logging docs"',
            '"tag_name": "v1.5.0", "body": "Add logging documentation."',
            '"message": "Issue created", "number": 1',
            '"printed_ts": "2025-08-21T12:00:00Z", "message": "k8s-monitoring logging docs published and released as v1.5.0."',
        ],
    ),

    # 63
    Task(
        annotator="0",
        user_id="task_63",
    instruction=(
        "You are 'ml-engineer'. Ensure the following final state, with all values precise and case‑sensitive: • A repository named 'ml-ops-pipeline' is established and is owned by you; its visibility is 'public' with its default branch as 'main'. 'mlops' and 'pipeline' are included in the repository topics. • A branch named 'feature-training-job' must exist. On that branch, have the file 'pipelines/train.py' contain exactly 'print('train-v1')' and ensure the file 'kubernetes/job.yaml' holds precisely 'kind: Job'. • The most recent commit on 'feature-training-job' has the message 'Add training job and pipeline stub'. • Pull request # 1 should create a pull request to merge the 'feature-training-job' branch into 'main', titled 'Add training pipeline' with the description 'Introduce training job and pipeline stub.', requesting reviews from 'qa-mike' and 'dev-sue', and ensure it receives approval and is merged. • Implement branch protection on 'main' with a requirement of {'required_reviews': 2}. • A release must be present on 'ml-ops-pipeline' tagged 'v0.8.0
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "ml-engineer"}),
            Action(name="CreateRepository", kwargs={"repo_name": "ml-ops-pipeline", "visibility": "public", "default_branch": "main"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "ml-ops-pipeline", "topic": "mlops"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "ml-ops-pipeline", "topic": "pipeline"}),
            Action(name="CreateBranch", kwargs={"repo_name": "ml-ops-pipeline", "source_branch": "main", "new_branch": "feature-training-job"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "ml-ops-pipeline", "branch": "feature-training-job", "path": "pipelines/train.py", "content": "print('train-v1')"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "ml-ops-pipeline", "branch": "feature-training-job", "path": "kubernetes/job.yaml", "content": "kind: Job"}),
            Action(name="CommitChangesToBranch", kwargs={"repo_name": "ml-ops-pipeline", "branch": "feature-training-job", "commit_message": "Add training job and pipeline stub"}),
            Action(name="CreatePullRequest", kwargs={"repo_name": "ml-ops-pipeline", "title": "Add training pipeline", "body": "Introduce training job and pipeline stub.", "base": "main", "head": "feature-training-job"}),
            Action(name="RequestPullRequestReviewers", kwargs={"repo_name": "ml-ops-pipeline", "pr_number": 1, "reviewers": ["qa-mike", "dev-sue"]}),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "ml-ops-pipeline", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "ml-ops-pipeline", "pr_number": 1}),
            Action(name="SetBranchProtection", kwargs={"repo_name": "ml-ops-pipeline", "branch": "main", "protected": "true", "rules": {"required_reviews": 2}}),
            Action(name="CreateRelease", kwargs={"repo_name": "ml-ops-pipeline", "tag": "v0.8.0", "title": "Training pipeline", "body": "Initial training job and pipeline stub."}),
            Action(name="GetLatestRelease", kwargs={"repo_name": "ml-ops-pipeline"}),
            Action(name="CreateIssue", kwargs={"repo_name": "ml-ops-pipeline", "title": "Validate training pipeline", "body": "Run end‑to‑end training and verify outputs.", "labels": ["mlops"]}),
            Action(name="AppendTerminal", kwargs={"message": "ml-ops-pipeline v0.8.0 released."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "ml-ops-pipeline"',
            '"message": "Pull request opened", "title": "Add training pipeline", "pr_number": 1',
            '"message": "Reviewers requested.", "requested_reviewers": ["dev-sue", "qa-mike"]',
            '"message": "Pull request merged.", "merged": "true"',
            '"message": "Branch protection enabled."',
            '"message": "Release created.", "repo_name": "ml-ops-pipeline", "tag_name": "v0.8.0"',
            '"tag_name": "v0.8.0", "title": "Training pipeline"',
            '"message": "Issue created", "number": 1',
            '"message": "ml-ops-pipeline v0.8.0 released."',
        ],
    ),

    # 64
    Task(
        annotator='0',
        user_id="task_64",
    instruction=(
        "You are 'security-group'. Upon completing the task, the repository condition for 'security-scanner' must meet ALL of the following: • 'main' branch is protected with rules exactly {\"require_reviews\": true, \"require_status_checks\": true, \"enforce_admins\": true}. • There is an issue titled 'Security audit required' with the body 'Run compliance checks on encryption and password policies.' and labeled 'security'. • All code scanning alerts for the repository are listed. • The terminal audit log includes the EXACT entry 'security-scanner security audit scheduled with branch protection enforced.'."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "security-group"}),
            Action(name="GetRepository", kwargs={"repo_name": "security-scanner"}),
            Action(name="SetBranchProtection", kwargs={
                "repo_name": "security-scanner",
                "branch": "main",
                "protected": "true",
                "rules": {"require_reviews": "true", "require_status_checks": "true", "enforce_admins": "true"},
            }),
            Action(name="CreateIssue", kwargs={
                "repo_name": "security-scanner",
                "title": "Security audit required",
                "body": "Run compliance checks on encryption and password policies.",
                "labels": ["security"]
            }),
            Action(name="ListCodeScanningAlerts", kwargs={"repo_name": "security-scanner"}),
            Action(name="AppendTerminal", kwargs={
                "message": "security-scanner security audit scheduled with branch protection enforced."
            }),
        ],
        outputs=[
            '"message": "Branch protection enabled.", "repo_name": "security-scanner", "branch": "main", "protected": "true"',
            '"message": "Issue created", "number": 1',
            '"alerts": [{"alert_number": 18, "severity": "critical", "state": "open", "description": "Unsafe deserialization in rule configuration parser"}, { "alert_number": 21, "severity": "high", "state": "open","description": "Potential buffer overflow in string handling"}, {"alert_number": 24, "severity": "medium", "state": "fixed", "description": "Use of deprecated crypto functions"}, { "alert_number": 27, "severity": "low", "state": "dismissed", "description": "Missing input validation in CLI arguments"}]',
            '"printed_ts": "2025-08-21T12:00:00Z", "message": "security-scanner security audit scheduled with branch protection enforced."',
        ],
    ),

    # 65
    Task(
        annotator="0",
        user_id="task_65",
    instruction=(
        "As 'ryan-dev', ensure the final state is delivered with all values being exact and case-sensitive: • Verify the creation of a repository named 'log-analyzer' which you own, ensuring its visibility is set to 'public' and the default branch is 'main'. The repository topics must include 'logs' and 'analysis'. • Confirm the existence of a branch named 'feature-alerts'. This branch must have the file 'src/alerts.py' with the exact content 'print('alert-v1')' and 'docs/alerts.md' with '# Log alerts'. • Ensure the most recent commit on 'feature-alerts' contains the message 'Add log alerting support'. • There should be a pull request numbered # 1, which merges 'feature-alerts' into 'main', with the title 'Introduce log alerting' and the description 'Add alerting support and documentation.', is approved and merged. • Branch protection rules for 'main' must have {'required_reviews': 1} enabled. • Verify that a release tagged 'v1.2.0', titled 'Log alerting', and described as 'Adds alerting support for log analyzer.' exists. • An issue named 'Refine alert thresholds
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "ryan-dev"}),
            Action(name="CreateRepository", kwargs={"repo_name": "log-analyzer", "visibility": "public", "default_branch": "main"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "log-analyzer", "topic": "logs"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "log-analyzer", "topic": "analysis"}),
            Action(name="CreateBranch", kwargs={"repo_name": "log-analyzer", "source_branch": "main", "new_branch": "feature-alerts"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "log-analyzer", "branch": "feature-alerts", "path": "src/alerts.py", "content": "print('alert-v1')"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "log-analyzer", "branch": "feature-alerts", "path": "docs/alerts.md", "content": "# Log alerts"}),
            Action(name="CommitChangesToBranch", kwargs={"repo_name": "log-analyzer", "branch": "feature-alerts", "commit_message": "Add log alerting support"}),
            Action(name="CreatePullRequest", kwargs={"repo_name": "log-analyzer", "title": "Introduce log alerting", "body": "Add alerting support and docs.", "base": "main", "head": "feature-alerts"}),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "log-analyzer", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "log-analyzer", "pr_number": 1}),
            Action(name="SetBranchProtection", kwargs={"repo_name": "log-analyzer", "branch": "main", "protected": "true", "rules": {"required_reviews": 1}}),
            Action(name="CreateRelease", kwargs={"repo_name": "log-analyzer", "tag": "v1.2.0", "title": "Log alerting", "body": "Adds alerting support for log analyzer."}),
            Action(name="CreateIssue", kwargs={"repo_name": "log-analyzer", "title": "Refine alert thresholds", "body": "Tune thresholds for production logs.", "labels": ["alerts"]}),
            Action(name="AppendTerminal", kwargs={"message": "log-analyzer v1.2.0 released."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "log-analyzer"',
            '"message": "Pull request opened", "title": "Introduce log alerting", "pr_number": 1',
            '"message": "Pull request merged.", "merged": "true"',
            '"message": "Branch protection enabled."',
            '"message": "Release created.", "repo_name": "log-analyzer", "tag_name": "v1.2.0"',
            '"message": "Issue created", "number": 1',
            '"message": "log-analyzer v1.2.0 released."',
        ],
    ),

    # 66
    Task(
        annotator='0',
        user_id="task_66",
    instruction=(
        "As 'security-group', upon concluding the task, verify that the 'security-scanner' repository state meets ALL of the following: • 'Main' branch must have protection with rules exactly as {\"require_reviews\": \"true\", \"require_status_checks\": \"true\", \"enforce_admins\": \"true\"}. • The visibility of the repository must remain 'private'. • Ensure 'compliance' is included in the repository topics. • There should be an issue titled 'Annual compliance baseline' with the body 'Baseline checks for encryption and password rotation.' carrying the labels ['security','compliance'], along with a comment that matches exactly 'Baseline scheduled for Q4.' • Verify the Terminal audit log contains the exact entry 'security-scanner compliance baseline scheduled with protections enforced.'."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "security-group"}),
            Action(name="GetRepository", kwargs={"repo_name": "security-scanner"}),
            Action(name="SetBranchProtection", kwargs={
                "repo_name": "security-scanner",
                "branch": "main",
                "protected": "true",
                "rules": {"require_reviews": "true", "require_status_checks": "true", "enforce_admins": "true"},
            }),
            Action(name="SetRepositoryVisibility", kwargs={
                "repo_name": "security-scanner",
                "visibility": "private",
            }),
            Action(name="AddRepoTopic", kwargs={
                "repo_name": "security-scanner",
                "topic": "compliance",
            }),
            Action(name="ListRepoTopics", kwargs={"repo_name": "security-scanner"}),
            Action(name="CreateIssue", kwargs={
                "repo_name": "security-scanner",
                "title": "Annual compliance baseline",
                "body": "Baseline checks for encryption and password rotation.",
                "labels": ["security", "compliance"],
            }),
            Action(name="AddIssueComment", kwargs={
                "repo_name": "security-scanner",
                "issue_number": 1,
                "comment": "Baseline scheduled for Q4.",
            }),
            Action(name="AppendTerminal", kwargs={
                "message": "security-scanner compliance baseline scheduled with protections enforced."
            }),
        ],
        outputs=[
            '"message": "Branch protection enabled.", "repo_name": "security-scanner", "branch": "main", "protected": "true"',
            '"message": "Visibility updated", "repo_name": "security-scanner", "visibility": "private"',
            '"message": "Topic \'compliance\' added."',
            '"topics": [',
            '"message": "Issue created", "number": 1',
            '"message": "Comment added."',
            '"printed_ts": "2025-08-21T12:00:00Z", "message": "security-scanner compliance baseline scheduled with protections enforced."',
        ],
    ),

    # 67
    Task(
        annotator="0",
        user_id="task_67",
    instruction=(
        "You are 'qa-erin'. Ensure the following outcome, adhering to all values being exact and case-sensitive: • You must have created a repository named 'automation-tests', which is 'public' and the default branch is 'main'. The repository topics must include 'tests' and 'automation'. • Establish a branch named 'feature-selenium'. On this branch, the file 'tests/selenium_test.py' should contain the line 'print('selenium-v1')' exactly, and 'docs/tests.md' must include '# Selenium tests' precisely. • The newest commit on 'feature-selenium' must bear the message 'Add selenium test suite'. • Pull request # 1 should aim to merge the 'feature-selenium' branch into the 'main' base, with the title 'Add selenium tests' and the body 'Introduce selenium test automation.' It must receive approval before merging. • Implement branch protection on 'main' that enforces {'required_reviews': 1}. • A release must occur on 'automation-tests' tagged 'v0.5.0', with the title 'Selenium suite' and body 'Initial selenium automation suite.'. • An issue titled
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "qa-erin"}),
            Action(name="CreateRepository", kwargs={"repo_name": "automation-tests", "visibility": "public", "default_branch": "main"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "automation-tests", "topic": "tests"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "automation-tests", "topic": "automation"}),
            Action(name="CreateBranch", kwargs={"repo_name": "automation-tests", "source_branch": "main", "new_branch": "feature-selenium"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "automation-tests", "branch": "feature-selenium", "path": "tests/selenium_test.py", "content": "print('selenium-v1')"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "automation-tests", "branch": "feature-selenium", "path": "docs/tests.md", "content": "# Selenium tests"}),
            Action(name="CommitChangesToBranch", kwargs={"repo_name": "automation-tests", "branch": "feature-selenium", "commit_message": "Add selenium test suite"}),
            Action(name="CreatePullRequest", kwargs={"repo_name": "automation-tests", "title": "Add selenium tests", "body": "Introduce selenium test automation.", "base": "main", "head": "feature-selenium"}),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "automation-tests", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "automation-tests", "pr_number": 1}),
            Action(name="SetBranchProtection", kwargs={"repo_name": "automation-tests", "branch": "main", "protected": "true", "rules": {"required_reviews": 1}}),
            Action(name="CreateRelease", kwargs={"repo_name": "automation-tests", "tag": "v0.5.0", "title": "Selenium suite", "body": "Initial selenium automation suite."}),
            Action(name="CreateIssue", kwargs={"repo_name": "automation-tests", "title": "Expand selenium coverage", "body": "Add cross-browser tests.", "labels": ["qa"]}),
            Action(name="AppendTerminal", kwargs={"message": "automation-tests v0.5.0 released."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "automation-tests"',
            '"message": "Pull request opened", "title": "Add selenium tests", "pr_number": 1',
            '"message": "Pull request merged.", "merged": "true"',
            '"message": "Branch protection enabled."',
            '"message": "Release created.", "repo_name": "automation-tests", "tag_name": "v0.5.0"',
            '"message": "Issue created", "number": 1',
            '"message": "automation-tests v0.5.0 released."',
        ],
    ),

    # 68
    Task(
        annotator="0",
        user_id="task_68",
    instruction=(
        "You are 'release-manager'. Establish the following situation, ensuring all values are maintained exactly as case-sensitive: • A repository should initially be created by you named 'release-runbooks', marked as 'private' with a default branch of 'main', and then renamed to 'release-ops', shifting visibility to 'public'. The ending topics of the repository should be exactly ['release'], with 'runbooks' topic appearing earlier but removed eventually. • Develop a branch called 'feature-runbooks'. On this branch, 'docs/runbook.md' must include '# Release runbook v1' accurately. • The last commit on 'feature-runbooks' should have the message 'Add initial release runbook'. • Issue # A task must be present in 'release-ops', titled 'Prepare v1.0 checklist' with content 'Checklist for release v1.0.', tagged with 'release' and 'checklist', and must have a single comment stating 'Checklist created.' • 'main' branch protection must be enabled, adhering to the rules {'required_reviews': 1}. • A release must exist on 'release-ops' with tag 'v1.0.0', titled 'Release operations v1
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "release-manager"}),
            Action(name="CreateRepository", kwargs={"repo_name": "release-runbooks", "visibility": "private", "default_branch": "main"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "release-runbooks", "topic": "release"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "release-runbooks", "topic": "runbooks"}),
            Action(name="RenameRepository", kwargs={"old_name": "release-runbooks", "new_name": "release-ops"}),
            Action(name="SetRepositoryVisibility", kwargs={"repo_name": "release-ops", "visibility": "public"}),
            Action(name="CreateBranch", kwargs={"repo_name": "release-ops", "source_branch": "main", "new_branch": "feature-runbooks"}),
            Action(name="WriteFileToBranch", kwargs={"repo_name": "release-ops", "branch": "feature-runbooks", "path": "docs/runbook.md", "content": "# Release runbook v1"}),
            Action(name="CommitChangesToBranch", kwargs={"repo_name": "release-ops", "branch": "feature-runbooks", "commit_message": "Add initial release runbook"}),
            Action(name="CreateIssue", kwargs={"repo_name": "release-ops", "title": "Prepare v1.0 checklist", "body": "Checklist for release v1.0.", "labels": ["release"]}),
            Action(name="AddIssueComment", kwargs={"repo_name": "release-ops", "issue_number": 1, "comment": "Checklist created."}),
            Action(name="AddLabelToIssue", kwargs={"repo_name": "release-ops", "issue_number": 1, "label": "checklist"}),
            Action(name="SetBranchProtection", kwargs={"repo_name": "release-ops", "branch": "main", "protected": "true", "rules": {"required_reviews": 1}}),
            Action(name="CreateRelease", kwargs={"repo_name": "release-ops", "tag": "v1.0.0", "title": "Release operations v1", "body": "Initial runbooks."}),
            Action(name="RemoveRepoTopic", kwargs={"repo_name": "release-ops", "topic": "runbooks"}),
            Action(name="AppendTerminal", kwargs={"message": "release-ops v1.0.0 published."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "release-runbooks"',
            '"message": "Repository renamed", "new_name": "release-ops"',
            '"message": "Visibility updated", "repo_name": "release-ops", "visibility": "public"',
            '"message": "Committed to branch", "commit_message": "Add initial release runbook"',
            '"message": "Comment added."',
            '"message": "Label "checklist" added."',
            '"message": "Branch protection enabled."',
            '"message": "Release created.", "repo_name": "release-ops", "tag_name": "v1.0.0"',
            '"message": "Topic "runbooks" removed."',
            '"message": "release-ops v1.0.0 published."',
        ],
    ),

    # 69. (ui-team) Two branches result in two PRs, leading to a list of open PRs (Approximately 14 edges).
    Task(
        annotator='0',
        user_id="task_69",
    instruction=(
        "Your responsibility is as 'design-team'. Within 'ui-kit', initiate two feature branches originating from 'main', and set up two PRs, then enumerate open PRs. Branches & files: - feature-a: docs/featA.md = '# Feat A\n' - feature-b: docs/featB.md = '# Feat B\n' PRs: - title 'Add feature A docs' (head=feature-a -> base=main) - title 'Add feature B docs' (head=feature-b -> base=main) Provide both PR titles and titles from the list_open_pull_requests."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "design-team"}),

            # PR # Pull Request #1 route
            Action(name="CreateBranch", kwargs={"repo_name": "ui-kit", "source_branch": "main", "new_branch": "feature-a"}),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "ui-kit", "branch": "feature-a",
                "path": "docs/featA.md", "content": "# Feat A\n",
                "commit_message": "Add feature A docs",
            }),
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "ui-kit",
                "title": "Add feature A docs",
                "head": "feature-a",
                "base": "main"
            }),

            # PR # Path for Pull Request #2
            Action(name="CreateBranch", kwargs={"repo_name": "ui-kit", "source_branch": "main", "new_branch": "feature-b"}),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "ui-kit", "branch": "feature-b",
                "path": "docs/featB.md", "content": "# Feat B\n",
                "commit_message": "Add feature B docs",
            }),
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "ui-kit",
                "title": "Add feature B docs",
                "head": "feature-b",
                "base": "main"
            }),

            # Overview
            Action(name="ListOpenPullRequests", kwargs={"repo_name": "ui-kit"}),
        ],
        outputs=[
            '"message": "Pull request opened", "title": "Add feature A docs", "base": "main", "head": "feature-a"',
            '"message": "Pull request opened", "title": "Add feature B docs", "base": "main", "head": "feature-b"',
            '"open_pr_titles": ["Introduce Theme Provider", "Release 1.0 prep", "Add feature A docs", "Add feature B docs"]',

        ],
    ),

    # 70
    Task(
        annotator='0',
        user_id="task_70",
    instruction=(
        "As 'platform-team', in the 'infra-terraform' repository, guarantee this finalized state: There must be precisely one open pull request directed at the default branch 'main'. PR #1 should utilize the head branch 'feature-docs-a' and contain a sole file 'docs/A.md' with the precise content '# 1 must use the primary branch 'feature-docs-a' and include a single file 'docs/A.md' with the exact content '# Doc A\n'; the final title should be 'Docs: add A' and the body should state 'Adds docs/A.md.'. Finally, provide the exact output from the tool that lists open pull requests for 'infra-terraform', along with the output detailing the files modified in the most recently opened PR.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "platform-team"}),
            Action(name="GetRepository", kwargs={"repo_name": "infra-terraform"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "infra-terraform"}),

            # PR # Pull Request #1
            Action(name="CreateBranch", kwargs={
                "repo_name": "infra-terraform", "source_branch": "main", "new_branch": "feature-docs-a"
            }),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "infra-terraform", "branch": "feature-docs-a",
                "path": "docs/A.md", "content": "# Doc A\n"
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "infra-terraform", "branch": "feature-docs-a",
                "commit_message": "Docs: add A"
            }),
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "infra-terraform", "title": "Docs: add A",
                "body": "Adds docs/A.md.", "base": "main", "head": "feature-docs-a"
            }),

            # # PR # # Pull Request #2
            # Action(identifier="CreateBranch", parameters={
            # "repository_name": "infra-terraform", "base_branch": "main", "target_branch": "feature-docs-b"
            # }),
            # Action(identifier="WriteFileToBranch", parameters={
            # "repository_name": "infra-terraform", "branch_name": "feature-docs-b",
            #     "path": "docs/B.md", "content": "# "path": "docs/B.md", "content": "# Documentation B\n"
            # }),
            # Action(identifier="CommitChangesToBranch", parameters={
            # "repository_name": "infra-terraform", "branch_name": "feature-docs-b",
            # "commit_message": "Documentation: include B"
            # }),
            # Action(identifier="CreatePullRequest", parameters={
            # "repo_name": "infra-terraform", "title": "Documentation: include B",
            # "body": "Includes docs/B.md.", "base": "main", "head": "feature-docs-b"
            # }),

            # Results
            Action(name="ListOpenPullRequests", kwargs={"repo_name": "infra-terraform"}),

            Action(name="ListPullRequestFiles", kwargs={
                "repo_name": "infra-terraform",
                "pr_number": 1
            }),
        ],
        outputs=[
            '"pull_requests": [{"number": 1, "title": "Docs: add A", "state": "open", "base": "main", "head": "feature-docs-a"}]',
            '"most_recent_pr_files": "files": ["docs/A.md"]'
        ],
    ),

    # 71. (alice-w) Create a PR that adds SECURITY.md and provide the list of files in the PR (deterministic).
    Task(
        annotator='0',
        user_id="task_71",
    instruction=(
        "You are 'maya-w'. Handle the delivery of a pull request in 'acme-webapp' from branch 'feature-security-doc' into 'main'. This should add a new file named SECURITY.md with the precise content: # Security Policy To report vulnerabilities, contact security@enterprise.com. We strive to triage within 2 business days. Use PR title 'Add SECURITY.md', with body 'Establishes a fundamental security policy and disclosure contact.', and commit message 'docs: include SECURITY.md with contact and triage details'. Return the file list of that PR.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="GetRepository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "acme-webapp"}),
            Action(
                name="CreateBranch",
                kwargs={"repo_name": "acme-webapp", "source_branch": "main", "new_branch": "feature-security-doc"},
            ),
            Action(
                name="WriteFileToBranch",
                kwargs={
                    "repo_name": "acme-webapp",
                    "branch": "feature-security-doc",
                    "path": "SECURITY.md",
                    "content": (
                        "# Security Policy\n\n"
                        "To report vulnerabilities, email security@enterprise.com.\n"
                        "We aim to triage within 2 business days."
                    ),
                    "commit_message": "docs: add SECURITY.md with contact and triage info",
                },
            ),
            Action(
                name="CreatePullRequest",
                kwargs={
                    "repo_name": "acme-webapp",
                    "title": "Add SECURITY.md",
                    "body": "Introduces a basic security policy and disclosure contact.",
                    "head": "feature-security-doc",
                    "base": "main",
                },
            ),
            # The validator will supply the correct PR number if it varies.
            Action(name="ListPullRequestFiles", kwargs={"repo_name": "acme-webapp", "pr_number": 1}),
        ],
        outputs=[
            '"message": "Pull request opened",'
            '"title": "Add SECURITY.md",'
            '"base": "main",'
            '"head": "feature-security-doc"',
            # Our tool provides the complete file set for the head branch of the PR.
            '"files": ["SECURITY.md"]',
        ],
    ),

    # 72. (alice-w) Apply the same label to issues #3 and # 72. (alice-w) Assign the identical label to issues #3 and #8, add a definitive comment, and then organize by that label.
    Task(
        annotator='0',
        user_id="task_72",
    instruction=(
        "Your role is 'maya-w'. In 'acme-webapp', coordinate the application of the label 'triage-urgent' to issues #3 and # 3 and #8. Then, add the comment 'Labels applied: triage-urgent, quality.' to both issues, and provide the list of issue numbers that have the label 'triage-urgent.'
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="GetRepository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="AddLabelToIssue", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "label": "triage-urgent"}),
            Action(name="AddLabelToIssue", kwargs={"repo_name": "acme-webapp", "issue_number": 8, "label": "triage-urgent"}),
            Action(
                name="AddIssueComment",
                kwargs={"repo_name": "acme-webapp", "issue_number": 3, "comment": "Labels applied: triage-urgent, quality."},
            ),
            Action(
                name="AddIssueComment",
                kwargs={"repo_name": "acme-webapp", "issue_number": 8, "comment": "Labels applied: triage-urgent, quality."},
            ),
            Action(name="ListIssuesByLabel", kwargs={"repo_name": "acme-webapp", "label": "triage-urgent"}),
        ],
        outputs=[
            '"issues_with_label_triage-urgent": [3, 8]',
        ],
    ),

    # 73. (devops-lead) Create and merge a pull request, followed by branch deletion.
    Task(
        annotator='0',
        user_id="task_73",
    instruction=(
        "You serve as 'infra-lead'. Within 'k8s-monitoring', generate a new feature branch named 'feature-docs', insert a file 'docs/USAGE.md' containing '# Usage Guide This file explains how to use the monitoring stack.', initiate a pull request into 'main' with the 'title' 'Add usage docs' and body 'Introduces usage documentation.', then eliminate the feature branch post-merge."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
            Action(name="GetRepository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="CreateBranch", kwargs={"repo_name": "k8s-monitoring", "new_branch": "feature-docs", "source_branch": "main"}),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "k8s-monitoring",
                "branch": "feature-docs",
                "path": "docs/USAGE.md",
                "content": "# Usage Guide\n\nThis file explains how to use the monitoring stack."
            }),
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Add usage docs",
                "body": "Introduces usage documentation.",
                "base": "main",
                "head": "feature-docs"
            }),
            Action(name="MergePullRequest", kwargs={
                "repo_name": "k8s-monitoring",
                "pr_number": 1  # We deterministically know this will be PR # We can definitively confirm this will be PR #1 in the sandbox environment.
            }),
            Action(name="DeleteBranch", kwargs={"repo_name": "k8s-monitoring", "branch": "feature-docs"}),
        ],
        outputs=[
            '"message": "Pull request opened",'
            '"title": "Add usage docs",'
            '"base": "main", "head": "feature-docs"',
            '"merged": true,'
            '"merge_method": "merge"',
            '"status": "ok"'
        ],
    ),

    # 74
    Task(
        annotator='0',
        user_id="task_74",
    instruction=(
        "You act as 'design-team'. For 'ui-kit', establish a branch 'feature-license-update', revise the LICENSE file with the precise text 'MIT License updated', and commit it with the message 'chore: update license'. Next, create a pull request into 'main' titled 'Update LICENSE' with the body 'Switch project to MIT license.', and provide the list of files altered in the PR."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "design-team"}),
            Action(name="GetRepository", kwargs={"repo_name": "ui-kit"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "ui-kit"}),
            Action(
                name="CreateBranch",
                kwargs={"repo_name": "ui-kit", "source_branch": "main", "new_branch": "feature-license-update"},
            ),
            Action(
                name="WriteFileToBranch",
                kwargs={
                    "repo_name": "ui-kit",
                    "branch": "feature-license-update",
                    "path": "LICENSE",
                    "content": "MIT License updated",
                    "commit_message": "chore: update license",
                },
            ),
            Action(
                name="CreatePullRequest",
                kwargs={
                    "repo_name": "ui-kit",
                    "title": "Update LICENSE",
                    "body": "Switch project to MIT license.",
                    "head": "feature-license-update",
                    "base": "main",
                },
            ),
            Action(
                name="ListPullRequestFiles",
                kwargs={
                    "repo_name": "ui-kit",
                    "pr_number": 1
                },
            ),
        ],
        outputs=[
            '"message": "Pull request opened", "title": "Update LICENSE", "base": "main", "head": "feature-license-update"',
            '"files": ["LICENSE"]',
        ],
    ),

    # 75
    Task(
        annotator='0',
        user_id="task_75",
    instruction=(
        "Assume the role of 'infra-lead'. Handle the preparation of the 'acme-bootstrap' repository for team onboarding. Make sure it includes a protected default branch called 'main', a working branch termed 'setup-work' that contains initial project files, and that a triage issue is established to coordinate setup tasks. Adhere to these precise specifications: - Files: 'README.md' with content '# Bootstrap repository.' and '.gitignore' with content '.DS_Store\nnode_modules/\n__pycache__/\n' - Branch protection on 'main': require_pull_request_reviews=true, dismiss_stale_reviews=true, enforce_admins=true, required_status_checks=['build'] - Issue: title='Initial setup checklist', body='Track bootstrap tasks for this repo.', labels=['triage', 'setup'] - Commit messages: 'add README.md', 'add .gitignore' Provide: (1) the protection rule block for 'main', and (2) the complete issue object with its labels"
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),

            Action(name="CreateRepository", kwargs={
                "repo_name": "acme-bootstrap",
                "default_branch": "main"
            }),

            Action(name="SetBranchProtection", kwargs={
                "repo_name": "acme-bootstrap",
                "branch": "main",
                "protected": "true",
                "rules": {
                    "require_pull_request_reviews": "true",
                    "dismiss_stale_reviews": "true",
                    "enforce_admins": "true",
                    "required_status_checks": ["build"]
                },
            }),

            Action(name="CreateBranch", kwargs={
                "repo_name": "acme-bootstrap",
                "source_branch": "main",
                "new_branch": "setup-work"
            }),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-bootstrap",
                "branch": "setup-work",
                "path": "README.md",
                "content": "# Bootstrap repository."
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-bootstrap",
                "branch": "setup-work",
                "commit_message": "add README.md"
            }),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-bootstrap",
                "branch": "setup-work",
                "path": ".gitignore",
                "content": ".DS_Store\\nnode_modules/\\n__pycache__/\\n"
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-bootstrap",
                "branch": "setup-work",
                "commit_message": "add .gitignore"
            }),

            Action(name="CreateIssue", kwargs={
                "repo_name": "acme-bootstrap",
                "title": "Initial setup checklist",
                "body": "Track bootstrap tasks for this repo.",
                "labels": ["triage", "setup"]
            }),

            Action(name="GetBranchProtection", kwargs={
                "repo_name": "acme-bootstrap",
                "branch": "main"
            }),
            Action(name="GetIssue", kwargs={
                "repo_name": "acme-bootstrap",
                "issue_number": 1
            }),
        ],
        outputs=[
            "{'require_pull_request_reviews': 'true', 'dismiss_stale_reviews': 'true', 'enforce_admins': 'true', 'required_status_checks': ['build']}",
            "{'number': 1, 'title': 'Initial setup checklist', 'labels': ['triage', 'setup'], 'state': 'open'}",
        ],
    ),

    # 76. PR involving multiple file modifications + enumerated PR files (9 actions) — RESOLVED
    Task(
        annotator='0',
        user_id="task_76",
    instruction=(
        "You are 'maya-w' developing the 'acme-webapp' service. Coordinate the submission of a pull request from a feature branch titled 'feat-auth' into the primary 'main' branch. The PR must introduce these specific files: • api/__init__.py with content 'main()' • api/auth.py with content 'class Auth: pass' • tests/test_auth.py with content 'def test_stub(): assert True' Use commit message: 'feat-auth: scaffolding and tests' Apply PR title: 'Add auth scaffolding' and body: 'Introduce basic auth module skeleton.' Provide the catalog of files altered in the PR."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="CreateBranch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "feat-auth"
            }),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp", "branch": "feat-auth",
                "path": "api/__init__.py", "content": "main()"
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feat-auth",
                "commit_message": "feat-auth: scaffolding and tests"
            }),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp", "branch": "feat-auth",
                "path": "api/auth.py", "content": "class Auth: pass"
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feat-auth",
                "commit_message": "feat-auth: scaffolding and tests"
            }),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp", "branch": "feat-auth",
                "path": "tests/test_auth.py", "content": "def test_stub(): assert True"
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feat-auth",
                "commit_message": "feat-auth: scaffolding and tests"
            }),

            Action(name="CreatePullRequest", kwargs={
                "repo_name": "acme-webapp",
                "title": "Add auth scaffolding",
                "body": "Introduce basic auth module skeleton.",
                "head": "feat-auth",
                "base": "main"
            }),
            Action(name="ListPullRequestFiles", kwargs={
                "repo_name": "acme-webapp",
                "pr_number": 1
            }),
        ],
        outputs=[
            "{'files': ['api/__init__.py', 'api/auth.py', 'tests/test_auth.py']}",
        ],
    ),

    # 77. Continuous Integration setup + CHANGELOG generation + release deployment + verification (10 tasks)
    Task(
        annotator='0',
        user_id="task_77",
    instruction=(
        "You are 'maya-w', preparing to launch the initial release for the existing public repository 'acme-webapp'. After setting up the build pipeline and changelog on the default branch 'main', publish version 'v0.1.0' as the inaugural release, ensuring to include appropriate metadata. Use the following specifics: - Ensure '.github/workflows/ci.yml' contains: 'Triggers CI workflows' - Ensure 'CHANGELOG.md' includes: '# Changelog ## # v0.1.0 - First release' - Commit message to utilize: 'ci+docs: include CI workflow and CHANGELOG' - Release information: • Tag: 'v0.1.0' • Title: 'v0.1.0' • Body: 'First release' Output the release metadata produced by the release tool.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "main",
                "path": ".github/workflows/ci.yml",
                "content": "Triggers CI workflows"
            }),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "main",
                "path": "CHANGELOG.md",
                "content": "# Changelog  ## # v0.1.0 - First release
            }),

            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "main",
                "commit_message": "ci+docs: add CI workflow and CHANGELOG"
            }),

            Action(name="CreateRelease", kwargs={
                "repo_name": "acme-webapp",
                "tag": "v0.1.0",
                "title": "v0.1.0",
                "body": "Initial release"
            }),

            Action(name="GetLatestRelease", kwargs={"repo_name": "acme-webapp"}),
        ],
        outputs=[
            # Must precisely conform to the output schema of the get_latest_release tool.
            "{'tag_name': 'v0.1.0', 'body': 'Initial release'}",
        ],
    ),

    # 81. (devops-lead) Create new repository + implement branch protection + submit runbook PR → resolve issue → release + add comment
    Task(
        annotator='0',
        user_id="task_81",
    instruction=(
        "You are 'infra-lead' setting up a new repository 'infra-runbooks'. Deliver a setup for an incident runbook in such a way that, once finished, the repository state meets ALL the acceptance criteria outlined below, utilizing the specified constants as provided. This is a statement of desired results and literals, NOT a step-by-step plan. ACCEPTANCE CRITERIA (the final state must adhere to all of these conditions): • A 'infra-runbooks' repository exists (public) with its default branch as 'main'. • A feature branch contains a committed incident runbook file with the exact content below. • Repository topics include exactly the listed topic. • Branch protection is enabled on the default branch 'main', with the exact protected flag and rules JSON provided below. • Issue number 1 must be closed and must include the exact pre-PR and post-release comments outlined below. • A pull request (number 1 post-reset) from the feature branch into 'main' must be merged. • A release with the specified tag below must be present. CONSTANTS TO USE VERBATIM (all literals must match precisely): - Repository visibility: public - Default branch name: main - Feature branch name: feature-incident-101 - File path: docs/incidents/101.md - File content (exact; SINGLE trailing newline only): # Incident 101: First Response Steps: 1. Page on-call 2. Gather logs 3. Mitigate blast radius Owner: SRE - Commit message: docs: add incident 101 guide - Repository topic to add: runbooks - Branch protection target: main - Branch protection 'protected' value: \"true\" - Branch protection rules JSON (use exactly this object): {\"required_status_checks\": [\"ci\"], \"enforce_admins\": \"true\"} - Issue to create/label/close: 1 - Issue title: Add incident 101 runbook - Issue body: Track and document initial incident response. - Label to add: documentation - Pre-PR issue comment: Runbook authored; PR will close this issue. - PR title: Add incident 101 runbook - PR body: Closes # Incident 101: Initial Response Procedures: 1. Notify on-call personnel 2. Collect logs 3. Limit impact Owner: SRE - Commit message: docs: include incident 101 guide - Repository topic to add: runbooks - Branch protection target: main - Branch protection 'protected' value: true - Branch protection rules JSON: {"required_status_checks": ["ci"], "enforce_admins": "true"} - Issue to create/label/close: 1 - Issue title
    ),
        actions=[
            # Authenticate and initialize repository
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
            Action(name="CreateRepository", kwargs={"repo_name": "infra-runbooks", "visibility": "public", "default_branch": "main"}),

            # Fix default and establish feature branch.
            Action(name="GetDefaultBranch", kwargs={"repo_name": "infra-runbooks"}),
            Action(name="CreateBranch", kwargs={"repo_name": "infra-runbooks", "new_branch": "feature-incident-101", "source_branch": "main"}),

            # Create and commit a runbook.
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "infra-runbooks",
                "branch": "feature-incident-101",
                "path": "docs/incidents/101.md",
                "content": "# Incident 101: First Response\n\nSteps:\n1. Page on-call\n2. Gather logs\n3. Mitigate blast radius\n\nOwner: SRE\n",
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "infra-runbooks",
                "branch": "feature-incident-101",
                "commit_message": "docs: add incident 101 guide",
            }),

            # Subject and branch security
            Action(name="AddRepoTopic", kwargs={"repo_name": "infra-runbooks", "topic": "runbooks"}),
            Action(name="SetBranchProtection", kwargs={
                "repo_name": "infra-runbooks",
                "branch": "main",
                "protected": "true",
                "rules": {"required_status_checks": ["ci"], "enforce_admins": "true"},
            }),

            # Lifecycle of an issue
            Action(name="CreateIssue", kwargs={
                "repo_name": "infra-runbooks",
                "title": "Add incident 101 runbook",
                "body": "Track and document initial incident response.",
            }),
            Action(name="AddLabelToIssue", kwargs={"repo_name": "infra-runbooks", "issue_number": 1, "label": "documentation"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "infra-runbooks", "issue_number": 1, "comment": "Runbook authored; PR will close this issue."}),

            # Pull request → assess → integrate
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "infra-runbooks",
                "title": "Add incident 101 runbook",
                "body": "Closes #1",
                "head": "feature-incident-101",
                "base": "main",
            }),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "infra-runbooks", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "infra-runbooks", "pr_number": 1}),

            # Resolve issue, deploy, and label.
            Action(name="UpdateIssue", kwargs={"repo_name": "infra-runbooks", "issue_number": 1, "state": "closed"}),
            Action(name="CreateRelease", kwargs={"repo_name": "infra-runbooks", "tag": "v1.0.0-incidents", "body": "First incident runbook."}),
            Action(name="AddIssueComment", kwargs={"repo_name": "infra-runbooks", "issue_number": 1, "comment": "Shipped in 'v1.0.0-incidents'"}),
        ],
        outputs=[
            '"message": "Incident runbook merged and released", "repo_name": "infra-runbooks"',
            '"pr_number": 1, "closed_issue": 1, "release_tag": "v1.0.0-incidents"',
        ],
    ),

    # 85
    Task(
        annotator='0',
        user_id="task_85",
    instruction=(
        "You are 'ryan-dev'. Within 'utils-js', ensure that PR #16 addressing Issue #7 has been integrated. Monitor TypeScript declaration support in PR #14 by leaving a comment: 'Tracking TypeScript declarations in PR #14'. Assign a repository topic 'typescript' and write a post on Issue #4: 'TS support is tracked in PR # Integration of Issue #7 is complete. Track TypeScript declaration support in PR #14 by commenting: 'Monitoring TypeScript declarations in PR #14'. Assign the 'typescript' topic to the repository and update Issue #4 with: 'TypeScript support is monitored in PR #14'. Add a terminal note: 'utils-js TypeScript support monitored and negative currency fix confirmed'.
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "ryan-dev"}),
            Action(name="GetRepository", kwargs={"repo_name": "utils-js"}),
            Action(name="GetPullRequest", kwargs={"repo_name": "utils-js", "pr_number": 16}),
            Action(name="GetIssue", kwargs={"repo_name": "utils-js", "issue_number": 7}),
            Action(name="GetPullRequest", kwargs={"repo_name": "utils-js", "pr_number": 14}),
            Action(name="CommentOnPullRequest", kwargs={
                "repo_name": "utils-js",
                "pr_number": 14,
                "comment": "Tracking TypeScript declarations in PR # 14 inches
            }),
            Action(name="AddRepoTopic", kwargs={"repo_name": "utils-js", "topic": "typescript"}),
            Action(name="AddIssueComment", kwargs={
                "repo_name": "utils-js",
                "issue_number": 4,
                "comment": "TS support is tracked in PR # 14 inches
            }),
            Action(name="AppendTerminal", kwargs={"message": "utils-js TS support tracked and negative currency fix verified"}),
        ],
        outputs=['"message": "utils-js TS support tracked and negative currency fix verified"'],
    ),

    # 86. (alice-w) CI and Security enhancement (non-procedural; deterministic)
    Task(
        annotator='0',
        user_id="task_86",
    instruction=(
        "You are 'maya-w' assigned to the 'acme-webapp' repository. Your role is to deploy a CI/security update, ensuring that upon completion, the repository's condition meets ALL the acceptance criteria below, using the exact constants specified. Refrain from interpreting this as step-by-step instructions; it is a specification of outcomes and literals. ACCEPTANCE CRITERIA (the final state should incorporate all of these): • A feature branch is established, containing the change set. • A new issue (number 1 after reset) is resolved and closed. • A pull request (number 1 after reset) is successfully merged into the default branch. • A release bearing the exact tag below is present. • The closed issue includes the precise post-release comment. CONSTANTS TO USE VERBATIM (ensure all literals match precisely): - Feature branch name: feature-ci-policy - Base branch name: main - File path #1: SECURITY.md - File content #1 (exact; SINGLE trailing newline only): # Security Policy Report: security@enterprise.com Triage: 2 business days - File path #2: .github/workflows/ci.yml - File content #2 (exact): name: CI on: [push, pull_request] jobs: build: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - run: echo Build OK - Commit message: ci: add SECURITY.md and CI workflow - Issue title: Enforce CI and security policy - Issue body: Track CI rollout for branch feature-ci-policy. - Label to add: compliance - Pre-PR issue comment: PR will reference and close this issue. - PR title: CI: add security policy and workflow - PR body: Closes # # Security Policy Contact: security@enterprise.com Response Time: 2 business days
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="GetRepository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "acme-webapp"}),
            Action(name="GetHeadSha", kwargs={"repo_name": "acme-webapp", "branch": "main"}),

            Action(name="CreateBranch", kwargs={"repo_name": "acme-webapp", "new_branch": "feature-ci-policy", "source_branch": "main"}),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-ci-policy",
                "path": "SECURITY.md",
                "content": "# Security Policy\n\nReport: security@enterprise.com\nTriage: 2 business days\n",
            }),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-ci-policy",
                "path": ".github/workflows/ci.yml",
                "content": "name: CI\non: [push, pull_request]\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - run: echo Build OK\n",
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-ci-policy",
                "commit_message": "ci: add SECURITY.md and CI workflow",
            }),

            Action(name="CreateIssue", kwargs={
                "repo_name": "acme-webapp",
                "title": "Enforce CI and security policy",
                "body": "Track CI rollout for branch feature-ci-policy.",
            }),
            Action(name="AddLabelToIssue", kwargs={"repo_name": "acme-webapp", "issue_number": 1, "label": "compliance"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "acme-webapp", "issue_number": 1, "comment": "PR will reference and close this issue."}),

            Action(name="CreatePullRequest", kwargs={
                "repo_name": "acme-webapp",
                "title": "CI: add security policy and workflow",
                "body": "Closes # 1 inch,
                "head": "feature-ci-policy",
                "base": "main",
            }),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "acme-webapp", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "acme-webapp", "pr_number": 1}),

            Action(name="UpdateIssue", kwargs={"repo_name": "acme-webapp", "issue_number": 1, "state": "closed"}),

            Action(name="CreateRelease", kwargs={"repo_name": "acme-webapp", "tag": "v0.1.0-ci"}),
            Action(name="GetLatestRelease", kwargs={"repo_name": "acme-webapp"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "acme-webapp", "issue_number": 1, "comment": "Released in 'v0.1.0-ci'"}),
        ],
        outputs=[
            '"message": "Pull request merged", "repo_name": "acme-webapp"',
            '"pr_number": 1, "issue_number": 1, "release_tag": "v0.1.0-ci"',
        ],
    ),

    # 87. (backend-core) 3DS process: set up configuration, create PR, merge, resolve issue, deploy.
    Task(
        annotator='0',
        user_id="task_87",
    instruction=(
        "As 'server-main', assigned to the 'payments-service' repository, handle the delivery of a 3DS feature update ensuring that, upon completion, the repository's state meets ALL outlined acceptance criteria with exact usage of the provided constants. Consider this a specification for outcomes and literals, not a step-by-step agenda. ACCEPTANCE CRITERIA (final state must reflect all of these): • A feature branch exists that contains the 3DS configuration change. • Issue number 13 is closed. • A pull request (number 1 after reset for this repo context) is merged into the default branch. • A release with the exact tag below exists. • The closed issue contains the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: feature-3ds-flow - Base branch name: main - File path: src/payments/three_ds.ts - File content (exact; SINGLE trailing newline only): export const ENABLE_3DS = true; - Commit message: feat(3ds): enable 3DS flow configuration - Issue to label and close: 13 - Label to add: 3ds - Pre-PR issue comment: Implementing 3DS; PR will close this issue. - PR title: Enable 3DS flow configuration - PR body: Closes # 13 - Pull request review outcome: approved - Release tag: v0.2.0-3ds - Post-release issue note: Released in 'v0.2.0-3ds' (3DS enabled)
    ),
        actions=[
            # Authentication and repository context
            Action(name="GetMe", kwargs={"username": "server-main"}),
            Action(name="GetRepository", kwargs={"repo_name": "payments-service"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "payments-service"}),
            Action(name="GetHeadSha", kwargs={"repo_name": "payments-service", "branch": "main"}),

            # Branch for new features
            Action(name="CreateBranch", kwargs={"repo_name": "payments-service", "new_branch": "feature-3ds-flow", "source_branch": "main"}),

            # Modify the changes on the feature branch.
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "payments-service",
                "branch": "feature-3ds-flow",
                "path": "src/payments/three_ds.ts",
                "content": "export const ENABLE_3DS = true;\n",
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "payments-service",
                "branch": "feature-3ds-flow",
                "commit_message": "feat(3ds): enable 3DS flow configuration",
            }),

            # Work the existing issue # Address the current issue #13 in a deterministic manner (available in the dataset post-reset).
            Action(name="AddLabelToIssue", kwargs={"repo_name": "payments-service", "issue_number": 13, "label": "3ds"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "payments-service", "issue_number": 13, "comment": "Implementing 3DS; PR will close this issue."}),

            # PR from feature → main, explicit body to close # Merge PR from feature to main, explicitly addressing issue #13.
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "payments-service",
                "title": "Enable 3DS flow configuration",
                "body": "Closes # 13 inches,
                "head": "feature-3ds-flow",
                "base": "main",
            }),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "payments-service", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "payments-service", "pr_number": 1}),

            # Explicitly resolve the issue (the dataset is not automatically modified by PRs).
            Action(name="UpdateIssue", kwargs={"repo_name": "payments-service", "issue_number": 13, "state": "closed"}),

            # Publish and label the issue.
            Action(name="CreateRelease", kwargs={"repo_name": "payments-service", "tag": "v0.2.0-3ds"}),
            Action(name="GetLatestRelease", kwargs={"repo_name": "payments-service"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "payments-service", "issue_number": 13, "comment": "Released in 'v0.2.0-3ds' (3DS enabled)"}),
        ],
        outputs=[
            '"message": "3DS flow merged and released", "repo_name": "payments-service"',
            '"pr_number": 1, "closed_issue": 13, "release_tag": "v0.2.0-3ds"',
        ],
    ),

    # 88. (frontend-dev) Resolved WebSocket memory leak → PR integrated → issue resolved → release + note
    Task(
        annotator='0',
        user_id="task_88",
    instruction=(
        "As 'ui-developer', responsible for the 'react-dashboard' repository, coordinate the implementation of a WebSocket leak fix, ensuring that upon completion, the repository's state adheres to ALL specified acceptance criteria using the exact constants provided. Regard this as a specification of outcomes and literals, NOT a step-by-step guide. ACCEPTANCE CRITERIA (final state must reflect all of these): • A feature branch exists that contains the fix for a WebSocket cleanup-related memory leak. • Issue number 25 is closed. • A pull request (number 1 after reset for this repo) is merged into the default branch. • A release with the exact tag below exists. • The closed issue contains the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: fix-memory-leak-ws - Base branch name: main - File path: src/hooks/useLiveSocket.ts - File content (exact; SINGLE trailing newline only): import { useEffect } from 'react'; export function useLiveSocket(url: string) { useEffect(() => { const ws = new WebSocket(url); return () => { ws.close(); }; }, [url]); } - Commit message: fix(ws): ensure cleanup to prevent memory leak - Issue to label and close: 25 - Label to add: memory-leak - Pre-PR issue comment: Fix adds cleanup for WebSocket in useEffect. - PR title: Fix memory leak in WebSocket cleanup - PR body: Closes # 25 - Pull request review outcome: approved - Release version: v2.2.1-leakfix - Post-release issue note: Fixed in 'v2.2.1-leakfix'
    ),
        actions=[
            # Authentication and repository context
            Action(name="GetMe", kwargs={"username": "ui-developer"}),
            Action(name="GetRepository", kwargs={"repo_name": "react-dashboard"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "react-dashboard"}),
            Action(name="GetHeadSha", kwargs={"repo_name": "react-dashboard", "branch": "main"}),

            # Development branch
            Action(name="CreateBranch", kwargs={"repo_name": "react-dashboard", "new_branch": "fix-memory-leak-ws", "source_branch": "main"}),

            # Modify changes in the feature branch.
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "react-dashboard",
                "branch": "fix-memory-leak-ws",
                "path": "src/hooks/useLiveSocket.ts",
                "content": "import { useEffect } from 'react';\n\nexport function useLiveSocket(url: string) {\n  useEffect(() => {\n    const ws = new WebSocket(url);\n    return () => {\n      ws.close();\n    };\n  }, [url]);\n}\n",
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "react-dashboard",
                "branch": "fix-memory-leak-ws",
                "commit_message": "fix(ws): ensure cleanup to prevent memory leak",
            }),

            # Work existing issue # Address issue #25 in a consistent manner.
            Action(name="AddLabelToIssue", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "label": "memory-leak"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "comment": "Fix adds cleanup for WebSocket in useEffect."}),

            # Pull request from feature branch to main branch.
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "react-dashboard",
                "title": "Fix memory leak in WebSocket cleanup",
                "body": "Closes # 25 inches,
                "head": "fix-memory-leak-ws",
                "base": "main",
            }),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "react-dashboard", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "react-dashboard", "pr_number": 1}),

            # Explicitly resolve the issue.
            Action(name="UpdateIssue", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "state": "closed"}),

            # Publish and label the issue.
            Action(name="CreateRelease", kwargs={"repo_name": "react-dashboard", "tag": "v2.2.1-leakfix"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "comment": "Patched in 'v2.2.1-leakfix'"}),
        ],
        outputs=[
            '"message": "WebSocket leak fix merged and released", "repo_name": "react-dashboard"',
            '"pr_number": 1, "closed_issue": 25, "release_tag": "v2.2.1-leakfix"',
        ],
    ),

    # 89. (ui-team) Icon pack finalized → PR accepted → issue resolved → deployed + note
    Task(
        annotator='0',
        user_id="task_89",
    instruction=(
        "Handle the role of 'design-team' in the 'ui-kit' repository to provide an icon-pack update. Ensure that upon finishing, the repository state meets ALL acceptance criteria detailed below, utilizing the exact constants given. Consider this a specification of outcomes and literals, NOT a step-by-step process. ACCEPTANCE CRITERIA (the final state must embody all of these): • A feature branch exists that includes two new SVG icons. • Issue number 6 is closed. • A pull request (number 1 after a reset for this repo) is merged into the default branch. • A release with the precise tag below exists. • The closed issue contains the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: feature-icons-pack - Base branch name: main - File path #1: src/icons/email.svg - File content #1 (exact; SINGLE trailing newline only): <svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M2 6h20v12H2z'/><path d='M2 6l10 7L22 6'/></svg> - File path #2: src/icons/phone.svg - File content #2 (exact; SINGLE trailing newline only): <svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M6 2h12v20H6z'/><path d='M9 18h6'/></svg> - Commit message: feat(icons): add email and phone SVGs - Issue to label and close: 6 - Label to add: icons - Pre-PR issue comment: Adding email and phone icons; PR will close this issue. - PR title: Add email and phone icons - PR body: Closes # Add SVG icons for email and phone.
    ),
        actions=[
            # Authentication and repository context
            Action(name="GetMe", kwargs={"username": "design-team"}),
            Action(name="GetRepository", kwargs={"repo_name": "ui-kit"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "ui-kit"}),
            Action(name="GetHeadSha", kwargs={"repo_name": "ui-kit", "branch": "main"}),

            # Development branch
            Action(name="CreateBranch", kwargs={"repo_name": "ui-kit", "new_branch": "feature-icons-pack", "source_branch": "main"}),

            # Modify the feature branch to include two SVG files.
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "ui-kit",
                "branch": "feature-icons-pack",
                "path": "src/icons/email.svg",
                "content": "<svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M2 6h20v12H2z'/><path d='M2 6l10 7L22 6'/></svg>\n",
            }),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "ui-kit",
                "branch": "feature-icons-pack",
                "path": "src/icons/phone.svg",
                "content": "<svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M6 2h12v20H6z'/><path d='M9 18h6'/></svg>\n",
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "ui-kit",
                "branch": "feature-icons-pack",
                "commit_message": "feat(icons): add email and phone SVGs",
            }),

            # Work existing issue # Resolve the current issue #6 in a deterministic manner.
            Action(name="AddLabelToIssue", kwargs={"repo_name": "ui-kit", "issue_number": 6, "label": "icons"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "ui-kit", "issue_number": 6, "comment": "Adding email and phone icons; PR will close this issue."}),

            # Merge request from feature branch to main branch.
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "ui-kit",
                "title": "Add email and phone icons",
                "body": "Closes # 6 inches,
                "head": "feature-icons-pack",
                "base": "main",
            }),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "ui-kit", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "ui-kit", "pr_number": 1}),

            # Explicitly resolve the issue.
            Action(name="UpdateIssue", kwargs={"repo_name": "ui-kit", "issue_number": 6, "state": "closed"}),

            # Publish and label the issue.
            Action(name="CreateRelease", kwargs={"repo_name": "ui-kit", "tag": "v1.1.0-icons"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "ui-kit", "issue_number": 6, "comment": "Shipped in 'v1.1.0-icons'"}),
        ],
        outputs=[
            '"message": "Icon pack merged and released", "repo_name": "ui-kit"',
            '"pr_number": 1, "closed_issue": 6, "release_tag": "v1.1.0-icons"',
        ],
    ),

    # 90. (devops-lead) Optimized Grafana performance → PR accepted → issue resolved → release + note
    Task(
        annotator='0',
        user_id="task_90",
    instruction=(
        "Coordinate the responsibilities of 'infra-lead' within the 'k8s-monitoring' repository to implement a Grafana performance improvement. Ensure that when completed, the repository’s condition adheres to ALL acceptance criteria outlined below, using the precise constants provided. Consider this a specification of outcomes and literals, NOT a step-by-step method. ACCEPTANCE CRITERIA (the final state must demonstrate all of these): • A feature branch exists featuring a documented performance optimization for Grafana dashboards. • Issue number 35 is closed. • A pull request (number 1 after a reset for this repo) is merged into the default branch. • A release with the specific tag below is present. • The closed issue carries the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: fix-grafana-performance - Base branch name: main - File path: grafana/dashboards/perf-optimization.md - File content (exact; SINGLE trailing newline only): ## Grafana Dashboard Performance - Reduce panel refresh to 30s - Prefer $__interval for rate() - Limit table rows to 200 - Commit message: perf(grafana): optimize dashboard refresh and query patterns - Issue to label and close: 35 - Label to add: performance - Pre-PR issue comment: Applying dashboard optimizations; PR will close this issue. - PR title: Optimize Grafana dashboard performance - PR body: Closes # Optimize Grafana dashboard performance by reducing panel refresh to 30 seconds, using $__interval for rate(), and limiting table rows to 200. Commit message: perf(grafana): enhance dashboard refresh and query efficiency. Close issue 35 with a performance label. Pre-PR comment: Implementing dashboard optimizations; this PR will resolve the issue. PR title: Enhance Grafana dashboard performance. PR body: Resolves #35. Pull request review: approved. Release version: v0.9
    ),
        actions=[
            # Authentication and repository context
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
            Action(name="GetRepository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="GetHeadSha", kwargs={"repo_name": "k8s-monitoring", "branch": "main"}),

            # Development branch
            Action(name="CreateBranch", kwargs={"repo_name": "k8s-monitoring", "new_branch": "fix-grafana-performance", "source_branch": "main"}),

            # Modify the changes on the feature branch.
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "k8s-monitoring",
                "branch": "fix-grafana-performance",
                "path": "grafana/dashboards/perf-optimization.md",
                "content": "## Grafana Dashboard Optimization

- Set panel refresh interval to 30 seconds
- Use $__interval with rate()
- Restrict table rows to 200
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "k8s-monitoring",
                "branch": "fix-grafana-performance",
                "commit_message": "perf(grafana): optimize dashboard refresh and query patterns",
            }),

            # Work existing issue # Address the current issue #35 in a deterministic manner.
            Action(name="AddLabelToIssue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 35, "label": "performance"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "k8s-monitoring", "issue_number": 35, "comment": "Applying dashboard optimizations; PR will close this issue."}),

            # Pull request from feature branch to main branch.
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Optimize Grafana dashboard performance",
                "body": "Closes # 35 inches,
                "head": "fix-grafana-performance",
                "base": "main",
            }),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "k8s-monitoring", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "k8s-monitoring", "pr_number": 1}),

            # Explicitly resolve the issue.
            Action(name="UpdateIssue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 35, "state": "closed"}),

            # Publish and label the issue.
            Action(name="CreateRelease", kwargs={"repo_name": "k8s-monitoring", "tag": "v0.9.1-perf"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "k8s-monitoring", "issue_number": 35, "comment": "Improvements shipped in 'v0.9.1-perf'"}),
        ],
        outputs=[
            '"message": "Grafana performance fix merged and released", "repo_name": "k8s-monitoring"',
            '"pr_number": 1, "closed_issue": 35, "release_tag": "v0.9.1-perf"',
        ],
    ),

    # 92. (data-scientist) MLflow connection retry → PR integrated → issue resolved → release + note
    Task(
        annotator='0',
        user_id="task_92",
    instruction=(
        "As a 'ml-engineer' in the 'ml-pipeline' repository, ensure the delivery of an MLflow connectivity fortification update. At the conclusion, the repository must fulfill ALL of the following acceptance criteria with the specific constants provided. This is a definition of outcomes and literals, NOT procedural instructions. ACCEPTANCE CRITERIA (final state must include all of these): • A feature branch is present, containing a retry-based MLflow client setup. • Issue number 29 should be marked as closed. • A pull request (first since repo reset) is integrated into the default branch. • A release with the precise tag as mentioned exists. • The closed issue features the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must match precisely): - Feature branch name: fix-mlflow-retry - Base branch name: main - File path: pipeline/config/mlflow.yml - File content (exact; SINGLE trailing newline only): mlflow: tracking_uri: ${MLFLOW_TRACKING_URI} client: retries: 5 backoff_seconds: 2 - Commit message: fix(mlflow): add client retries for connectivity issues - Issue to label and close: 29 - Label to add: mlflow - Pre-PR issue comment: Adding retry settings for MLflow client; PR will close this issue. - PR title: Add MLflow client retries to mitigate connectivity issues - PR body: Closes # 29 - Pull request review outcome: approved - Release version: v0.4.0-mlflow - Post-release comment: Released as 'v0.4.0-mlflow' (with MLflow retries activated)
    ),
        actions=[
            # Authentication and repository context
            Action(name="GetMe", kwargs={"username": "ml-engineer"}),
            Action(name="GetRepository", kwargs={"repo_name": "ml-pipeline"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "ml-pipeline"}),
            Action(name="GetHeadSha", kwargs={"repo_name": "ml-pipeline", "branch": "main"}),

            # Development branch
            Action(name="CreateBranch", kwargs={"repo_name": "ml-pipeline", "new_branch": "fix-mlflow-retry", "source_branch": "main"}),

            # Modify the collection on the feature branch.
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "ml-pipeline",
                "branch": "fix-mlflow-retry",
                "path": "pipeline/config/mlflow.yml",
                "content": "mlflow:\n  tracking_uri: ${MLFLOW_TRACKING_URI}\n  client:\n    retries: 5\n    backoff_seconds: 2\n",
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "ml-pipeline",
                "branch": "fix-mlflow-retry",
                "commit_message": "fix(mlflow): add client retries for connectivity issues",
            }),

            # Work existing issue # Address issue #29 in a deterministic manner.
            Action(name="AddLabelToIssue", kwargs={"repo_name": "ml-pipeline", "issue_number": 29, "label": "mlflow"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "ml-pipeline", "issue_number": 29, "comment": "Adding retry settings for MLflow client; PR will close this issue."}),

            # Merge request from feature branch to main branch.
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "ml-pipeline",
                "title": "Add MLflow client retries to mitigate connectivity issues",
                "body": "Closes # 29 inches,
                "head": "fix-mlflow-retry",
                "base": "main",
            }),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "ml-pipeline", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "ml-pipeline", "pr_number": 1}),

            # Explicitly resolve the issue.
            Action(name="UpdateIssue", kwargs={"repo_name": "ml-pipeline", "issue_number": 29, "state": "closed"}),

            # Publish and label the issue.
            Action(name="CreateRelease", kwargs={"repo_name": "ml-pipeline", "tag": "v0.4.0-mlflow"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "ml-pipeline", "issue_number": 29, "comment": "Released in 'v0.4.0-mlflow' (MLflow retries enabled)"}),
        ],
        outputs=[
            '"message": "MLflow retry configuration merged and released", "repo_name": "ml-pipeline"',
            '"pr_number": 1, "closed_issue": 29, "release_tag": "v0.4.0-mlflow"',
        ],
    ),

    # 93. (mobile-dev) Accessibility labels → PR merged → issue resolved → released + note
    Task(
        annotator='0',
        user_id="task_93",
    instruction=(
        "As a 'app-developer' in the 'flutter-finance-app' repository, ensure the implementation of an accessibility enhancement. On completion, the repository should meet ALL of the following acceptance criteria using the exact constants provided. This is a specification of results and literals, NOT detailed guidance. ACCEPTANCE CRITERIA (final state must encompass all of these): • A feature branch exists encompassing accessibility (a11y) semantic labels for buttons. • Issue number 22 is marked as closed. • A pull request (1st post-reset) is incorporated into the default branch. • A release with the exact tag specified exists. • The closed issue includes the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must correspond exactly): - Feature branch name: feature-a11y-labels - Base branch name: main - File path: lib/a11y/semantics.dart - File content (exact; SINGLE trailing newline only): /// Accessibility semantics for key buttons class A11yLabels { static const String addBudget = 'Add budget'; static const String viewReports = 'View reports'; } - Commit message: feat(a11y): add semantic labels for primary actions - Issue to label and close: 22 - Label to add: a11y - Pre-PR issue comment: Adding semantic labels for primary buttons; PR will close this issue. - PR title: Add a11y semantic labels for primary actions - PR body: Closes # 22 - PR review outcome: approved - Release version: v1.3.0-a11y - Post-release note: Accessibility labels included in 'v1.3.0-a11y'
    ),
        actions=[
            # Authentication and repository context
            Action(name="GetMe", kwargs={"username": "app-developer"}),
            Action(name="GetRepository", kwargs={"repo_name": "flutter-finance-app"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "flutter-finance-app"}),
            Action(name="GetHeadSha", kwargs={"repo_name": "flutter-finance-app", "branch": "main"}),

            # Development branch
            Action(name="CreateBranch", kwargs={"repo_name": "flutter-finance-app", "new_branch": "feature-a11y-labels", "source_branch": "main"}),

            # Modify the changes in the feature branch.
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "flutter-finance-app",
                "branch": "feature-a11y-labels",
                "path": "lib/a11y/semantics.dart",
                "content": "/// Accessibility semantics for key buttons\nclass A11yLabels {\n  static const String addBudget = 'Add budget';\n  static const String viewReports = 'View reports';\n}\n",
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "flutter-finance-app",
                "branch": "feature-a11y-labels",
                "commit_message": "feat(a11y): add semantic labels for primary actions",
            }),

            # Work existing issue # Address the current issue #22 in a deterministic manner.
            Action(name="AddLabelToIssue", kwargs={"repo_name": "flutter-finance-app", "issue_number": 22, "label": "a11y"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "flutter-finance-app", "issue_number": 22, "comment": "Adding semantic labels for primary buttons; PR will close this issue."}),

            # Pull request from feature branch to main branch.
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "flutter-finance-app",
                "title": "Add a11y semantic labels for primary actions",
                "body": "Closes # 22 inches,
                "head": "feature-a11y-labels",
                "base": "main",
            }),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "flutter-finance-app", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "flutter-finance-app", "pr_number": 1}),

            # Explicitly resolve the issue.
            Action(name="UpdateIssue", kwargs={"repo_name": "flutter-finance-app", "issue_number": 22, "state": "closed"}),

            # Publish and tag the issue.
            Action(name="CreateRelease", kwargs={"repo_name": "flutter-finance-app", "tag": "v1.3.0-a11y"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "flutter-finance-app", "issue_number": 22, "comment": "Accessibility labels shipped in 'v1.3.0-a11y'"}),
        ],
        outputs=[
            '"message": "Accessibility labels merged and released", "repo_name": "flutter-finance-app"',
            '"pr_number": 1, "closed_issue": 22, "release_tag": "v1.3.0-a11y"',
        ],
    ),

    # 94. (bob-dev) Include TypeScript declarations → PR merged → issue resolved → release + note (fixed: base=master)
    Task(
        annotator='0',
        user_id="task_94",
    instruction=(
        "As 'ryan-dev', your task within the 'utils-js' repository is to implement TypeScript declaration support in a manner that ultimately aligns the repository with ALL specified acceptance criteria, utilizing provided constants precisely. This is an outline of required results and literals, NOT a procedural guide. ACCEPTANCE CRITERIA (the final status must encapsulate all conditions): • A feature branch is present that includes a TypeScript declaration file for the library. • Issue number 4 has been resolved and closed. • A pull request (being the first after repository reset) merges into the default branch. • A release exists with the precise tag mentioned below. • The closed issue contains the specified post-release comment verbatim. CONSTANTS TO USE VERBATIM (all literals must precisely mirror the following): - Feature branch name: feature-ts-decls - Base branch name: master - File path: types/index.d.ts - File content (exact; SINGLE trailing newline only): declare module 'utils-js' { export function formatCurrency(value: number): string; } - Commit message: feat(types): add TypeScript declaration file - Issue to label and close: 4 - Label to add: typescript - Pre-PR issue comment: Adding TypeScript declaration file; PR will close this issue. - PR title: Add TypeScript declaration file - PR body: Closes # 4 - Pull request review outcome: approved - Release version: v1.1.0-types - Post-release issue note: TypeScript support included in 'v1.1.0-types'
    ),
        actions=[
            # Authentication and repository context
            Action(name="GetMe", kwargs={"username": "ryan-dev"}),
            Action(name="GetRepository", kwargs={"repo_name": "utils-js"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "utils-js"}),
            Action(name="GetHeadSha", kwargs={"repo_name": "utils-js", "branch": "master"}),

            # Create a feature branch off the master branch.
            Action(name="CreateBranch", kwargs={"repo_name": "utils-js", "new_branch": "feature-ts-decls", "source_branch": "master"}),

            # Modify the set in the feature branch.
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "utils-js",
                "branch": "feature-ts-decls",
                "path": "types/index.d.ts",
                "content": "declare module 'utils-js' {\n  export function formatCurrency(value: number): string;\n}\n",
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "utils-js",
                "branch": "feature-ts-decls",
                "commit_message": "feat(types): add TypeScript declaration file",
            }),

            # Work existing issue # Address issue #4 in a deterministic manner.
            Action(name="AddLabelToIssue", kwargs={"repo_name": "utils-js", "issue_number": 4, "label": "typescript"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "utils-js", "issue_number": 4, "comment": "Adding TypeScript declaration file; PR will close this issue."}),

            # Merge request from feature branch to master branch.
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "utils-js",
                "title": "Add TypeScript declaration file",
                "body": "Closes # 4 inches,
                "head": "feature-ts-decls",
                "base": "master",
            }),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "utils-js", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "utils-js", "pr_number": 1}),

            # Explicitly resolve the issue.
            Action(name="UpdateIssue", kwargs={"repo_name": "utils-js", "issue_number": 4, "state": "closed"}),

            # Publish and label the issue.
            Action(name="CreateRelease", kwargs={"repo_name": "utils-js", "tag": "v1.1.0-types"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "utils-js", "issue_number": 4, "comment": "TypeScript support shipped in 'v1.1.0-types'"}),
        ],
        outputs=[
            '"repo_name": "utils-js"',
            '"pr_number": 1, "closed_issue": 4, "release_tag": "v1.1.0-types"',
        ],
    ),

    # 95. (devops-lead) ServiceMonitor for custom applications → PR integrated → issue resolved → release + note
    Task(
        annotator='0',
        user_id="task_95",
    instruction=(
        "As 'infra-lead' working on the 'k8s-monitoring' repository, your objective is to establish custom application monitoring so that, upon completion, the repository meets ALL specified acceptance criteria, utilizing the exact constants provided. Consider this a statement of necessary results and literals, NOT procedural instructions. ACCEPTANCE CRITERIA (the final state must fulfill all stated criteria): • A feature branch includes a Prometheus ServiceMonitor dedicated to custom applications. • Issue number 37 is resolved and closed. • The initial pull request (after repository reset) is merged into the default branch. • There is a release tagged exactly as cited below. • The resolved issue contains the exact post-release comment specified. CONSTANTS TO USE VERBATIM (all literals must replicate the following precisely): - Feature branch name: feature-servicemonitor-apps - Base branch name: main - File path: prometheus/servicemonitor-apps.yaml - File content (exact; SINGLE trailing newline only): apiVersion: monitoring.coreos.com/v1 kind: ServiceMonitor metadata: name: apps-servicemonitor namespace: monitoring spec: selector: matchLabels: app.kubernetes.io/part-of: custom-apps namespaceSelector: any: true endpoints: - port: http-metrics interval: 30s - Commit message: feat(prometheus): add ServiceMonitor for custom applications - Issue to label and close: 37 - Label to add: monitoring - Pre-PR issue comment: Adding ServiceMonitor for custom apps; PR will close this issue. - PR title: Add ServiceMonitor for custom applications - PR body: Closes # 37 - PR review outcome: approved - Release version: v0.10.0-servicemonitor - Post-release note: Custom application monitoring introduced in 'v0.10.0-servicemonitor'
    ),
        actions=[
            # Authentication and repository context
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
            Action(name="GetRepository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="GetHeadSha", kwargs={"repo_name": "k8s-monitoring", "branch": "main"}),

            # Development branch
            Action(name="CreateBranch", kwargs={"repo_name": "k8s-monitoring", "new_branch": "feature-servicemonitor-apps", "source_branch": "main"}),

            # Modify the changes in the feature branch.
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "k8s-monitoring",
                "branch": "feature-servicemonitor-apps",
                "path": "prometheus/servicemonitor-apps.yaml",
                "content": "apiVersion: monitoring.coreos.com/v1\nkind: ServiceMonitor\nmetadata:\n  name: apps-servicemonitor\n  namespace: monitoring\nspec:\n  selector:\n    matchLabels:\n      app.kubernetes.io/part-of: custom-apps\n  namespaceSelector:\n    any: true\n  endpoints:\n  - port: http-metrics\n    interval: 30s\n",
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "k8s-monitoring",
                "branch": "feature-servicemonitor-apps",
                "commit_message": "feat(prometheus): add ServiceMonitor for custom applications",
            }),

            # Work existing issue # Address issue #37 in a deterministic manner.
            Action(name="AddLabelToIssue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 37, "label": "monitoring"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "k8s-monitoring", "issue_number": 37, "comment": "Adding ServiceMonitor for custom apps; PR will close this issue."}),

            # Pull request from feature branch to main branch.
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Add ServiceMonitor for custom applications",
                "body": "Closes # 37 inches,
                "head": "feature-servicemonitor-apps",
                "base": "main",
            }),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "k8s-monitoring", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "k8s-monitoring", "pr_number": 1}),

            # Explicitly resolve the issue.
            Action(name="UpdateIssue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 37, "state": "closed"}),

            # Publish and label the issue.
            Action(name="CreateRelease", kwargs={"repo_name": "k8s-monitoring", "tag": "v0.10.0-servicemonitor"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "k8s-monitoring", "issue_number": 37, "comment": "Custom app monitoring added in 'v0.10.0-servicemonitor'"}),
        ],
        outputs=[
            '"pr_number": 1, "closed_issue": 37, "release_tag": "v0.10.0-servicemonitor"'
        ],
    ),

    # 96. (nlp-labs) Memory optimization training → PR integrated → issue resolved → release + note
    Task(
        annotator='0',
        user_id="task_96",
    instruction=(
        "As the user 'language-ai' involved in the 'nlp-models' repository, oversee delivery of a training memory optimization ensuring the repository ultimately meets all specified acceptance criteria and uses the exact constants. Regard this as specifying outcomes and literals, without offering step-by-step instructions. ACCEPTANCE CRITERIA (the final state must encompass all of these): • A feature branch is present containing a configuration for memory-efficient training. • Issue number 12 is resolved. • A pull request (which is number 1 after the repository reset) has been integrated into the default branch. • A release with the precise tag below is in place. • The resolved issue has the specified post-release comment included. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: feat-memory-optim - Base branch name: main - File path: configs/training/memory.yaml - File content (exact; SINGLE trailing newline only): training: gradient_accumulation_steps: 4 batch_size: 8 mixed_precision: fp16 - Commit message: feat(train): add memory-optimized training config - Issue to label and close: 12 - Label to add: memory - Pre-PR issue comment: Adding memory-optimized training config; PR will close this issue. - PR title: Add memory-optimized training configuration - PR body: Closes # 12 - Pull request review outcome: approved - Release tag: v0.8.0-memory - Post-release issue note: Memory optimization included in 'v0.8.0-memory'
    ),
        actions=[
            # Authentication and repository context
            Action(name="GetMe", kwargs={"username": "language-ai"}),
            Action(name="GetRepository", kwargs={"repo_name": "nlp-models"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "nlp-models"}),
            Action(name="GetHeadSha", kwargs={"repo_name": "nlp-models", "branch": "main"}),

            # Development branch
            Action(name="CreateBranch", kwargs={"repo_name": "nlp-models", "new_branch": "feat-memory-optim", "source_branch": "main"}),

            # Modify the changes on the feature branch.
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "nlp-models",
                "branch": "feat-memory-optim",
                "path": "configs/training/memory.yaml",
                "content": "training:\n  gradient_accumulation_steps: 4\n  batch_size: 8\n  mixed_precision: fp16\n",
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "nlp-models",
                "branch": "feat-memory-optim",
                "commit_message": "feat(train): add memory-optimized training config",
            }),

            # Work existing issue # Address issue #12 in a deterministic manner.
            Action(name="AddLabelToIssue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "label": "memory"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "nlp-models", "issue_number": 12, "comment": "Adding memory-optimized training config; PR will close this issue."}),

            # Pull request from feature branch to main branch.
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "nlp-models",
                "title": "Add memory-optimized training configuration",
                "body": "Closes # 12 inches,
                "head": "feat-memory-optim",
                "base": "main",
            }),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "nlp-models", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "nlp-models", "pr_number": 1}),

            # Explicitly resolve the issue.
            Action(name="UpdateIssue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "state": "closed"}),

            # Publish and label the issue.
            Action(name="CreateRelease", kwargs={"repo_name": "nlp-models", "tag": "v0.8.0-memory"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "nlp-models", "issue_number": 12, "comment": "Memory optimization available in 'v0.8.0-memory'"}),
        ],
        outputs=[
            '"message": "Memory optimization merged and released", "repo_name": "nlp-models"',
            '"pr_number": 1, "closed_issue": 12, "release_tag": "v0.8.0-memory"',
        ],
    ),

    # 97. (alice-w) Enhanced fastpath performance → PR integrated → issue resolved → release + note
    Task(
        annotator='0',
        user_id="task_97",
    instruction=(
        "Acting as 'maya-w' within the 'acme-webapp' repository, coordinate a fastpath performance enhancement to ensure the repository ultimately fulfills all acceptance criteria laid out below and employs the exact constants specified. Interpret this as detailing outcomes and literals, not a procedural guide. ACCEPTANCE CRITERIA (the final state must demonstrate all of these): • A feature branch exists that incorporates an algorithm implementation for fastpath on large datasets. • Issue number 3 is marked as closed. • A pull request (which is number 1 after the repository reset) has been merged into the default branch. • A release with the specified tag detailed below is created. • The closed issue includes the specified post-release comment. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: feature-perf-fastpath - Base branch name: main - File path: src/opt/fastpath.js - File content (exact; SINGLE trailing newline only): export function fastpath(items) { if (!Array.isArray(items) || items.length === 0) return []; const seen = new Set(); const out = []; for (let i = 0; i < items.length; i++) { const v = items[i]; if (!seen.has(v)) { seen.add(v); out.push(v); } } return out; } - Commit message: perf: introduce fastpath algorithm for large datasets - Issue to label and close: 3 - Label to add: performance - Pre-PR issue comment: Implementing fastpath algorithm; PR will close this issue. - PR title: Introduce fastpath algorithm for performance - PR body: Closes # 3 - Pull request review outcome: approved - Release version: v0.2.0-perf - Post-release issue note: Performance enhancements delivered in 'v0.2.0-perf'
    ),
        actions=[
            # Authentication and repository context
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="GetRepository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "acme-webapp"}),
            Action(name="GetHeadSha", kwargs={"repo_name": "acme-webapp", "branch": "main"}),

            # Development branch
            Action(name="CreateBranch", kwargs={"repo_name": "acme-webapp", "new_branch": "feature-perf-fastpath", "source_branch": "main"}),

            # Modify the changes in the feature branch.
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-perf-fastpath",
                "path": "src/opt/fastpath.js",
                "content": "export function fastpath(items) {\n  if (!Array.isArray(items) || items.length === 0) return [];\n  const seen = new Set();\n  const out = [];\n  for (let i = 0; i < items.length; i++) {\n    const v = items[i];\n    if (!seen.has(v)) { seen.add(v); out.push(v); }\n  }\n  return out;\n}\n",
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-perf-fastpath",
                "commit_message": "perf: introduce fastpath algorithm for large datasets",
            }),

            # Work existing issue # Address the current issue #3 in a deterministic manner.
            Action(name="AddLabelToIssue", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "label": "performance"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "comment": "Implementing fastpath algorithm; PR will close this issue."}),

            # Pull request from feature branch to main branch
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "acme-webapp",
                "title": "Introduce fastpath algorithm for performance",
                "body": "Closes # 3 inches,
                "head": "feature-perf-fastpath",
                "base": "main",
            }),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "acme-webapp", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "acme-webapp", "pr_number": 1}),

            # Explicitly resolve the issue.
            Action(name="UpdateIssue", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "state": "closed"}),

            # Publish and note the issue.
            Action(name="CreateRelease", kwargs={"repo_name": "acme-webapp", "tag": "v0.2.0-perf"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "comment": "Performance improvements shipped in 'v0.2.0-perf'"}),
        ],
        outputs=[
            '"message": "Fastpath performance improvement merged and released", "repo_name": "acme-webapp"',
            '"pr_number": 1, "closed_issue": 3, "release_tag": "v0.2.0-perf"',
        ],
    ),

    # 98
    Task(
        annotator='0',
        user_id="task_98",
    instruction=(
        "Your role is 'platform-team'. Manage the process to have a pull request merged into the default branch 'main' within the repository 'infra-terraform' from a feature branch named 'feature-docs-refresh'. Ensure this pull request precisely adds two new files: - 'docs/CHANGELOG.md' featuring the text: ## Changelog - 2025-08-21: Initial changelog entry. - 'docs/REFRESH.md' featuring the text: # # Changelog - 2025-08-21: Created initial changelog entry. - 'docs/REFRESH.md' includes the section: # Infra Terraform modules. Operational note: documentation updated on 2025-08-21. Use 'docs: add CHANGELOG and refresh note' for the commit message. Title the pull request 'Docs refresh: add CHANGELOG and REFRESH.md'. In the pull request description, include 'Automated docs refresh.' Request reviews from 'security-group
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "platform-team"}),
            Action(name="GetRepository", kwargs={"repo_name": "infra-terraform"}),

            Action(name="CreateBranch", kwargs={
                "repo_name": "infra-terraform",
                "source_branch": "main",
                "new_branch": "feature-docs-refresh"
            }),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "infra-terraform",
                "branch": "feature-docs-refresh",
                "path": "docs/CHANGELOG.md",
                "content": "## Changelog\n\n- 2025-08-21: First entry in the changelog.\n
            }),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "infra-terraform",
                "branch": "feature-docs-refresh",
                "path": "docs/REFRESH.md",
                "content": "# Infra\n\nTerraform modules.\n\nOps note: refreshed docs on 2025-08-21.\n"
            }),

            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "infra-terraform",
                "branch": "feature-docs-refresh",
                "commit_message": "docs: add CHANGELOG and refresh note"
            }),

            Action(name="CreatePullRequest", kwargs={
                "repo_name": "infra-terraform",
                "title": "Docs refresh: add CHANGELOG and REFRESH.md",
                "body": "Automated docs refresh.",
                "base": "main",
                "head": "feature-docs-refresh"
            }),

            Action(name="ListPullRequestFiles", kwargs={
                "repo_name": "infra-terraform",
                "pr_number": 1
            }),

            Action(name="RequestPullRequestReviewers", kwargs={
                "repo_name": "infra-terraform",
                "pr_number": 1,
                "reviewers": ["security-group", "infra-lead"]
            }),

            Action(name="MergePullRequest", kwargs={
                "repo_name": "infra-terraform",
                "pr_number": 1
            }),

            Action(name="GetHeadSha", kwargs={
                "repo_name": "infra-terraform",
                "branch": "main"
            }),
        ],
        outputs=[
            '"merged_pr_number": 1',
            '"changed_files_reported_by_pr": ["docs/CHANGELOG.md", "docs/REFRESH.md"]',
            '"main_branch_sha_after_merge": "sha_0000000000000000000000000000000000000000"'
        ],
    ),

    # 99. (frontend-dev) Submit a hardening pull request including policy and changelog, and monitor the state after merging.
    Task(
        annotator='0',
        user_id="task_99",
    instruction=(
        "As 'ui-developer', your task is to coordinate a hardening update to the repository 'react-dashboard'. This update should entail two files: `kubernetes/policy.yaml` which should contain a Kubernetes network policy, and `docs/changelog.md` for documenting the change. The policy file must include exactly: ``` apiVersion: v1 kind: NetworkPolicy metadata: name: baseline spec: podSelector: {} policyTypes: [\"Ingress\",\"Egress\"] ``` The changelog should contain: ``` # Changelog - task_01: baseline policies and docs (deterministic). ``` Use the branch name `feature-hardening` and commit message `Add baseline policies [task_01]`. The modifications must be submitted through a pull request with the title 'Harden defaults [task_01]' and the body 'Baseline policies and changelog.', requiring review by 'security-group' and 'qa-erin'. Ensure it receives approval with the comment 'LGTM [task_01]' and includes the review note 'Please review — deterministic run [task_01].'. Provide the list of altered files from the PR, the last SHA of the default branch after merging, and the end message: 'Merged PR # Changelog - task_01: baseline policies and documentation (deterministic). ``` Utilize the branch name `feature-hardening` and the commit message `Add baseline policies [task_01]`. Submit the changes via a pull request titled 'Harden defaults [task_01]' with the description 'Baseline policies and changelog.', requiring review from 'security-group' and 'qa-erin'. Ensure it obtains approval with the comment 'LGTM [task_01]' and includes the review note
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "ui-developer"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "react-dashboard"}),

            Action(name="CreateBranch", kwargs={"repo_name": "react-dashboard", "source_branch": "main", "new_branch": "feature-hardening"}),

            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "react-dashboard",
                "branch": "feature-hardening",
                "path": "kubernetes/policy.yaml",
                "content": "apiVersion: v1\nkind: NetworkPolicy\nmetadata:\n  name: baseline\nspec:\n  podSelector: {}\n  policyTypes: [\"Ingress\",\"Egress\"]\n"
            }),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "react-dashboard",
                "branch": "feature-hardening",
                "path": "docs/changelog.md",
                "content": "# Changelog\n\n- task_01: baseline policies and docs (deterministic).\n"
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "react-dashboard",
                "branch": "feature-hardening",
                "commit_message": "Add baseline policies [task_01]"
            }),

            Action(name="InitializePullRequestsBlock", kwargs={"repo_name": "react-dashboard"}),
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "react-dashboard",
                "title": "Harden defaults [task_01]",
                "body": "Baseline policies and changelog.",
                "base": "main",
                "head": "feature-hardening"
            }),
            Action(name="RequestPullRequestReviewers", kwargs={
                "repo_name": "react-dashboard",
                "pr_number": 1,
                "reviewers": ["security-group", "qa-erin"]
            }),
            Action(name="CommentOnPullRequest", kwargs={
                "repo_name": "react-dashboard",
                "pr_number": 1,
                "comment": "Please review — deterministic run [task_01]."
            }),
            Action(name="CreatePullRequestReview", kwargs={
                "repo_name": "react-dashboard",
                "pr_number": 1,
                "review_decision": "approve",
                "comment": "LGTM [task_01]"
            }),
            Action(name="MergePullRequest", kwargs={"repo_name": "react-dashboard", "pr_number": 1}),

            Action(name="GetHeadSha", kwargs={"repo_name": "react-dashboard", "branch": "main"}),
            Action(name="ListPullRequestFiles", kwargs={"repo_name": "react-dashboard", "pr_number": 1}),
            Action(name="AppendTerminal", kwargs={
                "message": "Merged PR # Merge branch 'task_01' into main for react-dashboard.
            }),
        ],
        outputs=[
            '"merged": "true"',
            '"sha": "sha_0000000000000000000000000000000000000000"',
            '"files": ["docs/changelog.md", "kubernetes/policy.yaml"]',
            '"message": "Merged PR # Merge task_01 into the main branch for the react-dashboard.
        ],
    ),

    # One hundred
    Task(
        annotator='0',
        user_id="task_100",
    instruction=(
        "As 'platform-team', within the repository 'infra-terraform', ensure the following final condition: An issue exists with the title 'Stabilize ops runbook' and the body 'Document the on-call escalation steps for staging and production.'—both precisely. This issue should be closed and possess exactly the labels 'operations' and 'documentation', with the comment 'Ack: logged by ops-bot.'. Lastly, present the results after examining issues for the term 'operations'."
    ),
        actions=[
            Action(name="GetMe", kwargs={"username": "platform-team"}),
            Action(name="GetRepository", kwargs={"repo_name": "infra-terraform"}),

            Action(name="CreateIssue", kwargs={
                "repo_name": "infra-terraform",
                "title": "Stabilize ops runbook",
                "body": "Document the on-call escalation steps for staging and production."
            }),

            Action(name="AddLabelToIssue", kwargs={
                "repo_name": "infra-terraform",
                "issue_number": 1,
                "label": "operations"
            }),
            Action(name="AddLabelToIssue", kwargs={
                "repo_name": "infra-terraform",
                "issue_number": 1,
                "label": "documentation"
            }),

            Action(name="AddIssueComment", kwargs={
                "repo_name": "infra-terraform",
                "issue_number": 1,
                "comment": "Ack: logged by ops-bot."
            }),

            Action(name="UpdateIssue", kwargs={
                "repo_name": "infra-terraform",
                "issue_number": 1,
                "state": "closed"
            }),

            Action(name="SearchIssues", kwargs={
                "query": "operations"
            }),
        ],
        outputs=[
            '"search_results_for_operations": [1]'
        ]

    ),

    # 20
    Task(
        annotator="0",
        user_id="task_20",
    instruction=(
        "As 'app-developer', in the repository 'flutter-finance-app', establish the following final condition with all values exact and case-sensitive: • A branch named 'hotfix-1.2.1' is present. Within this branch, the 'CHANGELOG.md' file includes precisely '## 1.2.1 - hotfix'. • The latest commit on 'hotfix-1.2.1' has the message 'Add CHANGELOG for v1.2.1'. • There is a release tagged 'v1.2.1', named 'v1.2.1 [task_101]', with the description 'body-[task_101]'. Furthermore, the latest release aligns with the tag 'v1.2.1'. • An issue titled 'Release
    ),
        actions=[
        Action(name="GetMe", kwargs={"username": "app-developer"}),
        Action(name="GetRepository", kwargs={"repo_name": "flutter-finance-app"}),
        Action(name="CreateBranch", kwargs={"repo_name": "flutter-finance-app", "source_branch": "main", "new_branch": "hotfix-1.2.1"}),
        Action(name="WriteFileToBranch", kwargs={"repo_name": "flutter-finance-app", "branch": "hotfix-1.2.1", "path": "CHANGELOG.md", "content": "## 1.2.1 - patch"}),
        Action(name="CommitChangesToBranch", kwargs={"repo_name": "flutter-finance-app", "branch": "hotfix-1.2.1", "commit_message": "Add CHANGELOG for v1.2.1"}),
        Action(name="CreateRelease", kwargs={"repo_name": "flutter-finance-app", "tag": "v1.2.1", "title": "v1.2.1 [task_101]", "body": "body-[task_101]"}),
        Action(name="GetLatestRelease", kwargs={"repo_name": "flutter-finance-app"}),
        Action(name="CreateIssue", kwargs={"repo_name": "flutter-finance-app", "title": "Release v1.2.1 note [task_101]", "body": "body-[task_101]", "labels": ["release-log"]}),
        Action(name="AppendTerminal", kwargs={"message": "Release v1.2.1 created in flutter-finance-app [task_101]"}),
        ],
        outputs=[
        '"message": "Branch created", "new_branch": "hotfix-1.2.1"',
        '"message": "Committed to branch", "commit_message": "Add CHANGELOG for v1.2.1"',
        '"message": "Release created.", "repo_name": "flutter-finance-app", "tag_name": "v1.2.1"',
        '"tag_name": "v1.2.1"', # from retrieve_most_recent_release
        '"labels": ["release-log"]',
        '"message": "Release v1.2.1 created in flutter-finance-app [task_101]"',
        ],
    )
]