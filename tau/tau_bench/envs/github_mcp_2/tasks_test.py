from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator='0',
        user_id="task_28",
        instruction=(
            "You act as 'app-developer'. In 'flutter-finance-app', assess Issue #18 along with PR #18 in conjunction with PR #26. Approve the PR with the comment: 'Please verify rendering on actual devices for iOS 14 and 15,' requesting confirmation for iOS 14/15, and label the issue as 'ios1'. Obtain the latest terminal message, then append 'flutter-finance-app iOS charts fix in validation.'"
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
    ),

    # 45
    Task(
        annotator="0",
        user_id="task_45",
        instruction=(
            "You take on the role of 'infra-lead'. Your task is to bring about the following definitive state, with every value exact and adhering to case sensitivity: • A repository titled 'observability-ops' should be in place under your ownership; its visibility set as 'private', which you must switch to 'public', its principal branch being 'main', and it should include the topic 'kubernetes'. • A branch 'feature-initial-config' is present. On that branch, the file 'kubernetes/alertmanager.yaml' is required to contain exactly 'alertmanager: config: placeholder-v1', and the file 'kubernetes/prometheus.yaml' must have exactly 'prometheus: config: placeholder-v1'. • The most recent commit on 'feature-initial-config' includes the message 'Add initial Prometheus/Alertmanager manifests'. • Pull request #1 targets the base 'main' from the head 'feature-initial-config' with the title 'Add initial Kubernetes monitoring stack' and content 'Bootstrap Prometheus and Alertmanager manifests.', it is approved, and has been merged. • A release exists on 'observability-ops' labeled 'v0.1.0', with the title 'Initial monitoring stack', and description 'First version of monitoring components.'. • The terminal log must include precisely one additional entry stating 'observability-ops v0.1.0 released.'."
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
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
            '"message": "Repository created", "repo_name": "observability-ops"',
            '"message": "Pull request opened", "title": "Add initial Kubernetes monitoring stack", "pr_number": 1',
            '"message": "Pull request merged."',
            '"message": "Release created.", "repo_name": "observability-ops", "tag_name": "v0.1.0"',
            '"message": "observability-ops v0.1.0 released."',
        ],
    ),

    # 23
    Task(
        annotator='0',
        user_id="task_23",
        instruction=(
            "You are 'maya-w'. In 'acme-webapp', handle the reconciliation of the code scanning alert that mentions 'feature-auth' using the merged PR #5 from that branch. Check the current branches, details of PR #5 from the specified branch. Review the existing branches, the specifics of PR #5, and the modified files. Create an issue titled 'Reconcile alert ref: feature-auth' and apply the labels ['investigate', 'security'], including the description 'Alert references feature-auth which has been merged, but the branch is absent in the current snapshot; confirm lineage and correct metadata'. Subsequently, document this terminal entry: 'acme-webapp alert ref reconciliation recorded'."
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
            Action(name="SearchIssues", kwargs={"query": "triage-urgent"}),
            Action(name="AppendTerminal", kwargs={
                "message": "Issue closed with triage-urgent label in acme-webapp [task_66]"
            }),
        ],
        outputs=[
            '"message": "Label \'triage-urgent\' added."',
            '"state": "closed"',
            '"results": [1]',
            '"message": "Issue closed with triage-urgent label in acme-webapp [task_66]"',
        ],
    ),

    # 04
    Task(
        annotator='0',
        user_id="task_04",
        instruction=(
            "You are user 'maya-w'. Examine the repository 'acme-webapp' for any pending PRs. Provide comments on PR #5 twice using feedbacks 'Looks good overall' and 'Please add more tests', then summarize your actions in the terminal with the message 'Comments added and PR #5 reviewed.'."
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="GetRepository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="ListOpenPullRequests", kwargs={"repo_name": "acme-webapp"}),
            Action(name="CommentOnPullRequest", kwargs={"repo_name": "acme-webapp", "pr_number": 5, "comment": "Looks good overall"}),
            Action(name="CommentOnPullRequest", kwargs={"repo_name": "acme-webapp", "pr_number": 5, "comment": "Please add more tests"}),
            Action(name="AppendTerminal", kwargs={"message": "Comments added and PR #5 evaluated."}),
        ],
        outputs=[
            '"message": "Comments added and PR #5 evaluated."',
        ],
    ),

    # 36
    Task(
        annotator='0',
        user_id="task_36",
        instruction=(
            "You are 'maya-w' and required to operate solely through the provided tools. Verify that the final state of the repository 'acme-webapp' meets ALL the acceptance criteria listed below. Consider these as outcomes/specifications—not step-by-step instructions. ACCEPTANCE CRITERIA (all must be satisfied): • A branch named 'file-crud' is present, originating from 'main'. • The file docs/note.txt is present on branch 'file-crud' and its final content is exactly: 'Hello v2'. • During the operation, the content 'Hello v1' was recorded in docs/note.txt and successfully read back once (include the read result in outputs). • The modification is committed with the exact commit message: 'docs(note): update to v2'. • A pull request is made from 'file-crud' into 'main' titled 'File CRUD update' with the body 'Promote CRUD change for docs/note.txt', and the PR indicates docs/note.txt as a modified file."
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="CreateBranch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "file-crud"
            }),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "file-crud",
                "path": "docs/note.txt",
                "content": "Hello v1"
            }),
            Action(name="GetFileContents", kwargs={
                "repo_name": "acme-webapp",
                "branch": "file-crud",
                "path": "docs/note.txt"
            }),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "file-crud",
                "path": "docs/note.txt",
                "content": "Hello v2"
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "file-crud",
                "commit_message": "docs(note): update to v2"
            }),
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "acme-webapp",
                "title": "File CRUD update",
                "body": "Promote CRUD change for docs/note.txt",
                "head": "file-crud",
                "base": "main"
            }),
            Action(name="ListPullRequestFiles", kwargs={
                "repo_name": "acme-webapp",
                "pr_number": 1
            }),
        ],
        outputs=[
            '"message": "Branch created"',
            '"path": "docs/note.txt", "content": "Hello v1"',
            '"docs/note.txt"',
        ],
    ),

    # 79
    Task(
        annotator='0',
        user_id="task_79",
        instruction=(
            "As a 'infra-lead', it is your role to assess a shell script amendment prior to its integration. Within the public repository 'acme-scripts', monitor modifications on a feature branch 'fix-script' derived from the 'main' branch, focusing on updates made to the script 'scripts/run.sh'. Initially, the script displays 'HELLO', with an adjustment later to also reveal 'WORLD'. During the process, capture a terminal log halfway with the message 'RUN'. After committing changes and initiating a pull request, examine both the file differences and the log results. Refer to these file content details: - Initial: '#!/usr/bin/env bash\\necho HELLO\\n' - Final: '#!/usr/bin/env bash\\necho HELLO\\necho WORLD\\n' - Commit messages: 'feat: add run script' and 'fix: append WORLD echo' - PR title: 'Fix run script', body: 'Append WORLD echo to run.sh' Provide the ultimate terminal log along with the list of modified files in the PR."
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
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
            '"timestamp": "2025-08-21T12:00:00Z", "message": "RUN"',
            '"scripts/run.sh"',
        ],
    ),

    # 39
    Task(
        annotator='0',
        user_id="task_39",
        instruction=(
            "Your task as a 'ui-developer' is to work solely with the tools at your disposal. Confirm that the 'react-dashboard' repository fulfills ALL the acceptance criteria outlined below. These should be viewed as objectives/specifications—not as procedural instructions. ACCEPTANCE CRITERIA (all conditions must be satisfied): • An issue must be present with the title 'Build pipeline audit [task_69]' and the body 'Verify CI stages and artifacts for reproducibility. [task_69]'. • This issue should bear the label 'ci-audit', incorporate the precise comment 'Checklist prepared. [task_69]', and be marked 'closed'. • It should be possible to confirm via a search that an issue with the label 'ci-audit' is available in 'react-dashboard'. • There should be a terminal log stating exactly: 'Issue closed with ci-audit label in react-dashboard [task_69]'."
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "ui-developer"}),
            Action(
                name="CreateIssue",
                kwargs={
                    "repo_name": "react-dashboard",
                    "title": "Build pipeline audit [task_69]",
                    "body": "Verify CI stages and artifacts for reproducibility. [task_69]",
                    "labels": []
                },
            ),
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
            Action(
                name="UpdateIssue",
                kwargs={"repo_name": "react-dashboard", "issue_number": 1, "state": "closed"},
            ),
            Action(
                name="SearchIssues",
                kwargs={"query": "ci-audit"},
            ),
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

    # 32
    Task(
        annotator='0',
        user_id="task_32",
        instruction=(
            "Operate as 'maya-w' using solely the available tools. Confirm that the final state of the repository 'acme-webapp' meets ALL the acceptance criteria detailed below. Consider these as outcomes/specification—not procedural instructions. ACCEPTANCE CRITERIA (all must be satisfied): • An issue is present titled 'Nightly job failed on main' with the body \"CI job 'nightly-build' failed due to timeout.\". • The issue possesses the label 'ops', includes the precise comment 'Investigating: rerun queued.', and is in the 'closed' state. • The latest terminal log is specifically: 'Issue #1 closed: Nightly job failed on main'."
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
                "message": "Issue #1 closed: Nightly job failed on main"
            }),
            Action(name="ListTerminalLastMessage", kwargs={}),
        ],
        outputs=[
            '"message": "Issue created", "number": 1',
            '"message": "Label \'ops\' added."',
            '"timestamp": "2025-08-21T12:00:00Z", "message": "Issue #1 closed: Nightly job failed on main"',
        ],
    ),

    # 78
    Task(
        annotator='0',
        user_id="task_78",
        instruction=(
            "Act as 'security-group' and engage only via the available tools. Verify that the ending state of the repository 'security-scanner' fulfills ALL the acceptance criteria outlined below. These should be seen as outcomes/specification—not step-by-step directives. ACCEPTANCE CRITERIA (all conditions must be met): • A branch named 'sec-checks' has been created, branching from the default branch. • Within that branch, ensure the file '.github/workflows/security.yml' is present and its contents are exactly: on: [push] jobs: scan: runs-on: ubuntu-latest steps: - name: Security scan run: echo SCAN • The commit message is: 'chore: add security workflow'. • A pull request exists with the title 'Add security workflow' and the body 'Adds a basic GitHub Actions scan workflow.' from 'sec-checks' into the default branch. • Outputs should comprise the list of files changed in that pull request and any open code scanning alerts bearing the 'critical' severity."
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
            '".github/workflows/security.yml"',
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

    # 40
    Task(
        annotator='0',
        user_id="task_40",
        instruction=(
            "You are 'maya-w' and must manage tasks solely through the provided tools. Verify that the final repository condition in 'acme-webapp' meets ALL the acceptance criteria outlined below. Consider these as outcomes/specification—not a step-by-step process. ACCEPTANCE CRITERIA (all must be met): • A feature branch called 'temp-pr' is established from the default branch and holds a file located at 'docs/pr_demo.txt' with the content precisely: 'temporary PR'. • A pull request is present titled 'Temp PR demo' with the body 'Demonstration of temporary PR lifecycle.' originating from head 'temp-pr' into the default branch. • The pull request is subsequently canceled by removing its head branch: the branch 'temp-pr' is no longer present. • A terminal log is created containing the message exactly: 'PR Temp PR demo withdrawn in acme-webapp.'. • Return the pull request title in outputs."
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
            Action(name="GetMe", kwargs={"username": "ryan-dev"}),
            Action(
                name="CreateIssue",
                kwargs={
                    "repo_name": "utils-js",
                    "title": "Utilities module audit [task_73]",
                    "body": "Review currency formatting and TypeScript support. [task_73]",
                    "labels": []
                },
            ),
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
            Action(
                name="UpdateIssue",
                kwargs={"repo_name": "utils-js", "issue_number": 1, "state": "closed"},
            ),
            Action(
                name="SearchIssues",
                kwargs={"query": "module-audit"},
            ),
            Action(
                name="GetIssue",
                kwargs={"repo_name": "utils-js", "issue_number": 1},
            ),
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
            '"message": "Label \'module-audit\' added."',
            '"state": "closed"',
            '"results": [1]',
            '"title": "Utilities module audit [task_73]"',
            '"labels": ["module-audit"]',
            '"message": "Issue closed with module-audit label in utils-js [task_73]"',
        ],
    ),

    # 82
    Task(
        annotator='0',
        user_id="task_82",
        instruction=(
            "Operate as 'design-team' exclusively using the designated tools. Guarantee the ultimate repository state in 'ui-kit' meets ALL acceptance criteria detailed below, treating these as specification outcomes, not procedural steps. ACCEPTANCE CRITERIA (all criteria must be fulfilled): • Existence of a branch named 'feature-validate' that diverges from 'main' by appending a file at path 'docs/validation.md' with content precisely: 'Validation test: head==base should not merge.'. • Presence of a commit on 'feature-validate' with the exact message: 'Add docs/validation.md for merge validation test'. • A pull request #1 present in repository 'ui-kit' titled 'Validate merge blocking when head==base' with body 'This PR intentionally uses the same branch for head and base to verify merge validation.', both head and base on 'feature-validate'. • Rejection of an attempt to merge the pull request, with message 'Pull request rejected.' citing 'head and base branch are the same', alongside a false merged indicator. • An ending entry containing the specific message: 'PR #1 rejected in ui-kit: head equals base (validation).'."
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
                "message": "PR #1 rejected in ui-kit: head equals base (validation)."
            }),
        ],
        outputs=[
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
            "As 'maya-w', work solely utilizing the tools provided. Ensure the ultimate condition of the repository 'acme-webapp' meets ALL acceptance criteria below; these should be viewed as outcomes/specification, not as step-by-step instructions. ACCEPTANCE CRITERIA (all must be fulfilled): • An open issue exists with the title 'Fix crash on startup' and content 'Application crashes due to missing env var check', that tracks the application startup crash. • The default branch contains a branch called 'fix-startup', and 'src/main.py' includes the line: 'assert ENV_VAR is not None'. This change is committed with the message 'fix: guard against missing ENV_VAR'. • A pull request has been initiated from 'fix-startup' to the default branch, titled 'Fix startup crash', with content 'Adds env var guard clause', and this pull request is merged. • Provide the issue metadata and the pull request title in outputs."
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
            Action(name="GetIssue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1
            }),
        ],
        outputs=[
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
            "Act as 'design-team'. In the 'ui-kit' repository, there needs to be a pull request #11 entitled 'Introduce Theme Provider'. Submit the precise review comment 'Theme reviewed. [task_74]' on it, then approve and merge it. Provide the PR number, its final status 'merged', and a terminal entry that reads 'PR #11 merged with review in ui-kit [task_74]'."
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "design-team"}),
            Action(name="GetPullRequest", kwargs={"repo_name": "ui-kit", "pr_number": 11}),
            Action(
                name="CreatePullRequestReview",
                kwargs={
                    "repo_name": "ui-kit",
                    "pr_number": 11,
                    "review_decision": "approve",
                    "comment": "Theme reviewed. [task_74]"
                },
            ),
            Action(
                name="MergePullRequest",
                kwargs={"repo_name": "ui-kit", "pr_number": 11},
            ),
            Action(
                name="AppendTerminal",
                kwargs={"message": "PR #11 merged with review in ui-kit [task_74]"},
            ),
        ],
        outputs=[
            '"pr_number": 11',
            '"state": "merged"',
            '"message": "PR #11 merged with review in ui-kit [task_74]"',
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
            "You hold the role of 'infra-lead'. Within 'k8s-monitoring', confirm the default branch and merely list the commits in branch 'upgrade-prometheus'. Check open alerts by listing them to ensure Alert #45 remains open; subsequently, initiate an issue titled 'Harden TLS for Prometheus scrape' with labels ['security','prometheus'] and body: 'Alert #45 remains active after the v2.45.0 upgrade; implement updated ciphers and TLS versions.'. Append to the terminal: 'k8s-monitoring TLS hardening tracked after upgrade.'."
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
                "body": "Alert #45 remains active after the v2.45.0 upgrade; implement updated ciphers and TLS versions.",
                "labels": ["security", "prometheus"],
            }),
            Action(name="AppendTerminal", kwargs={"message": "k8s-monitoring TLS hardening tracked after upgrade"}),
        ],
        outputs=['"message": "k8s-monitoring TLS hardening tracked after upgrade"'],
    ),

    # 84
    Task(
        annotator='0',
        user_id="task_84",
        instruction=(
            "Your task is 'server-main'. Within 'payments-service', synchronize PR #21 with Issue #13 (3DS). Examine the repository, the issue, and the PR, and detail any existing code scanning alerts. Tag Issue #13 with 'needs-tests', comment as follows: 'PR #21 implements 3DS; please add unit tests for fallback coverage prior to merging.' Provide a PR review with 'request_changes' and add the comment: 'Unit tests for 3DS fallback flows are required.' End with: 'payments-service 3DS alignment and test gating acknowledged.'."
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "server-main"}),
            Action(name="GetRepository", kwargs={"repo_name": "payments-service"}),
            Action(name="GetIssue", kwargs={"repo_name": "payments-service", "issue_number": 13}),
            Action(name="GetPullRequest", kwargs={"repo_name": "payments-service", "pr_number": 21}),
            Action(name="ListCodeScanningAlerts", kwargs={"repo_name": "payments-service"}),
            Action(name="AddLabelToIssue", kwargs={"repo_name": "payments-service", "issue_number": 13, "label": "needs-tests"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "payments-service", "issue_number": 13, "comment": "PR #21 implements 3DS; please add unit tests for fallback coverage prior to merging."}),
            Action(
                name="CreatePullRequestReview",
                kwargs={
                    "repo_name": "payments-service",
                    "pr_number": 21,
                    "review_decision": "request_changes",
                    "comment": "Please include unit tests for 3DS fallback flows.",
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

    # 34
    Task(
        annotator='0',
        user_id="task_34",
        instruction=(
            "You are 'maya-w' and must function only through the specified tools. YOUR OBJECTIVE • In repository 'acme-webapp', make an issue utilizing the exact title and body literals, apply the exact label literal, insert the exact comment literal, finalize the issue, and confirm the most recent terminal entry is identical to the exact message literal. LITERALS (use verbatim) - repo: acme-webapp - issue title: CI gate: add test matrix - issue body: Add unit + integration test matrix - label to add: ready-for-ci - comment to post: Triage complete: scheduled for CI gate - terminal message: Issue #1 resolved in acme-webapp: CI readiness triage finished"
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
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
            Action(name="AppendTerminal", kwargs={
                "message": "Issue #1 resolved in acme-webapp: CI readiness triage finished"
            }),
            Action(name="ListTerminalLastMessage", kwargs={}),
        ],
        outputs=[
            '"message": "Issue created", "number": 1',
            '"message": "Label \'ready-for-ci\' added."',
            '"entries": {"printed_ts": "2025-08-21T12:00:00Z", "message": "Issue #1 resolved in acme-webapp: CI readiness triage finished"}',
        ],
    ),

    # 91
    Task(
        annotator='0',
        user_id="task_91",
        instruction=(
            "You are 'security-group' tasked with working in repository 'security-scanner'. Implement an XSS rule modification ensuring that, once completed, the repository state meets ALL acceptance criteria outlined below, utilizing the exact constants provided. View this as a specification of outcomes and literals, NOT a step-by-step process. ACCEPTANCE CRITERIA (final state must reflect all of these): • A feature branch is created containing a relaxed XSS rule to minimize false positives on template literals. • Close issue number 5. • Merge a pull request (number 1 after reset for this repo) into the default branch. • Ensure a release with the exact tag below is present. • The closed issue comprises the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: fix-xss-false-positives - Base branch name: main - File path: rules/xss/relaxed-template-rule.yml - File content (exact; SINGLE trailing newline only): id: xss-template-relaxed severity: medium pattern: disallow-unsafe-innerHTML allow_template_literals: true - Commit message: fix(xss): relax rule for template literals to reduce false positives - Issue to label and close: 5 - Label to add: xss - Pre-PR issue comment: Relaxing XSS rule for template literals; PR will close this issue. - PR title: Relax XSS rule to reduce false positives on template literals - PR body: Closes #5 - Pull request review status: approved - Release version: v1.3.1-xss-fp - Post-release issue note: Resolved in 'v1.3.1-xss-fp' (decreased false positives)"
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "security-group"}),
            Action(name="GetRepository", kwargs={"repo_name": "security-scanner"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "security-scanner"}),
            Action(name="GetHeadSha", kwargs={"repo_name": "security-scanner", "branch": "main"}),
            Action(name="CreateBranch", kwargs={"repo_name": "security-scanner", "new_branch": "fix-xss-false-positives", "source_branch": "main"}),
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
            Action(name="AddLabelToIssue", kwargs={"repo_name": "security-scanner", "issue_number": 5, "label": "xss"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "security-scanner", "issue_number": 5, "comment": "Relaxing XSS rule for template literals; PR will close this issue."}),
            Action(name="CreatePullRequest", kwargs={
                "repo_name": "security-scanner",
                "title": "Relax XSS rule to reduce false positives on template literals",
                "body": "Closes #5",
                "head": "fix-xss-false-positives",
                "base": "main",
            }),
            Action(name="CreatePullRequestReview", kwargs={"repo_name": "security-scanner", "pr_number": 1, "review_decision": "approve"}),
            Action(name="MergePullRequest", kwargs={"repo_name": "security-scanner", "pr_number": 1}),
            Action(name="UpdateIssue", kwargs={"repo_name": "security-scanner", "issue_number": 5, "state": "closed"}),
            Action(name="CreateRelease", kwargs={"repo_name": "security-scanner", "tag": "v1.3.1-xss-fp"}),
            Action(name="AddIssueComment", kwargs={"repo_name": "security-scanner", "issue_number": 5, "comment": "Fixed in 'v1.3.1-xss-fp' (reduced false positives)"}),
        ],
        outputs=[
            '"repo_name": "security-scanner"',
            '"pr_number": 1, "closed_issue": 5, "release_tag": "v1.3.1-xss-fp"',
        ],
    ),

    # 01
    Task(
        annotator='0',
        user_id="task_01",
        instruction=(
            "You belong to 'design-team'. Validate that the 'main' branch of 'ui-kit' is safeguarded and verify its current protection status. Document the modification by creating an audit issue titled 'Protect main branch' with body 'Branch protection for main enabled.' and label 'ops', and record the precise terminal entry 'Branch main protection enabled in ui-kit.'."
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

    # 02
    Task(
        annotator='0',
        user_id="task_02",
        instruction=(
            "You represent 'security-group'. Issue a release in 'security-scanner' with tag 'v0.4.0', title 'Performance release', and body 'Performance optimizations and SARIF format support.' Afterwards, verify the latest release. Register an audit by opening an issue titled 'Release v0.4.0 created' with body 'Release published successfully.' labeled 'release', and enter the exact terminal entry 'security-scanner v0.4.0 released.'."
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

    # 03
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
            Action(
                name="AppendTerminal",
                kwargs={
                    "message": "Issue #1 created to track code scanning alerts in k8s-monitoring",
                },
            ),
        ],
        outputs=[
            "'message': '{\"message\": \"Code alerts retrieved.\", \"repo_name\": \"k8s-monitoring\", \"alert_count\": 3, \"alert_numbers\": [42, 45, 48], \"severities\": [\"high\", \"medium\", \"low\"]}'",
            '"message": "Issue #1 created to track code scanning alerts in k8s-monitoring"',
        ],
    ),

    # 06
    Task(
        annotator='0',
        user_id="task_06",
        instruction=(
            "As 'infra-lead', oversee the review of all merged pull requests across these repositories: 'acme-webapp', 'utils-js', 'nlp-models', 'security-scanner', 'flutter-finance-app', 'react-dashboard', and 'k8s-monitoring'. For every merged PR, compile the list of modified files and log a terminal audit entry as follows: 'Merged PR #{number} in {repo_name}: {list of files separated by commas}'."
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
            '"message": "Merged PR #7 in acme-webapp: src/logger.py"',
            '"message": "Merged PR #16 in utils-js: src/utils/format.js, test/format.test.js"',
            '"message": "Merged PR #22 in nlp-models: src/evaluation.py, scripts/checkpoint.py"',
            '"message": "Merged PR #23 in security-scanner: src/cache.rs, src/scanner.rs, Cargo.toml"',
            '"message": "Merged PR #24 in flutter-finance-app: lib/theme/dark_theme.dart, lib/main.dart, pubspec.yaml"',
            '"message": "Merged PR #30 in react-dashboard: src/styles/global.css, src/theme/dark.css, src/hooks/useTheme.ts"',
            '"message": "Merged PR #32 in k8s-monitoring: kubernetes/alertmanager.yaml, config/alertmanager.yml, docker-compose.yml"',
            '"message": "Merged PR #34 in k8s-monitoring: kubernetes/prometheus.yaml, config/prometheus.yml, docs/MONITORING.md"',
        ],
    ),

    # 07
    Task(
        annotator='0',
        user_id="task_07",
        instruction=(
            "Taking on the role of 'server-main', gather the entire commit history from the 'payments-service' repository and assess commit authors alongside their frequencies. Include the complete record and specifically check the 'main' branch for branch-level statistics. Document the audit by opening an issue named 'Commit authors frequency audit' with the message 'Collected authors and commit counts from full history and main branch.' and the label 'audit', then enter the terminal note 'Authors frequency audit for payments-service completed'."
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "server-main"}),
            Action(name="SearchRepositories", kwargs={"owner": "server-main"}),
            Action(name="ListCommits", kwargs={"repo_name": "payments-service"}),
            Action(name="ListCommits", kwargs={"repo_name": "payments-service", "branch": "main"}),
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
            "Act as 'infra-lead'. In the context of 'k8s-monitoring', verify merged PRs #32 and #34, with a final note confirming that upgrade and alerting configuration have been jointly validated."
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
            "Function as 'ui-developer'. Within 'react-dashboard', enumerate open PRs, examine the conflicted PR #28, and comment on Issue #25 with: 'Strategy: implement useEffect cleanup and WebSocket closure on unmount; check heap snapshots.' Update terminal with: 'memory leak investigation for react-dashboard scheduled.'."
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

    # 13
    Task(
        annotator='0',
        user_id="task_13",
        instruction=(
            "You are 'maya-w' managing the repository 'acme-webapp'. Verify that the repository's final state meets ALL acceptance criteria listed below, utilizing the precise literals given. Approach this as outcomes/specification, not detailed guidance. ACCEPTANCE CRITERIA (all must be met in the end): • Issue #3 has the label: triage-urgent • Issue #3 state is exactly: closed • Issue #3 includes the comment: Labels applied: triage-urgent, quality."
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

    # 14
    Task(
        annotator='0',
        user_id="task_14",
        instruction=(
            "You are 'ryan-dev' overseeing the repository 'utils-js'. Confirm that the final state satisfies ALL acceptance criteria outlined below, approaching this as a specification (not detailed instructions). ACCEPTANCE CRITERIA: • Issue #4 has the label: needs-triage • Issue #4 contains the exact new comment: Triaged and scheduled for next minor. • Issue #4 status is: closed."
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

    # 15
    Task(
        annotator='0',
        user_id="task_15",
        instruction=(
            "As 'ui-developer', you are working in repository 'react-dashboard'. Ensure that the final outcome fulfills ALL acceptance criteria below, treating this as a specification rather than step-by-step guidance. ACCEPTANCE CRITERIA: • Issue #25 must have the label: investigate • Issue #25 should include the precise new comment: Triaged; assigning to next sprint. • Issue #25 status must be: closed."
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

    # 16
    Task(
        annotator='0',
        user_id="task_16",
        instruction=(
            "As a member of 'language-ai', ensure that while working in the repository 'nlp-models', the end state complies with ALL acceptance criteria listed below, using this as a specification instead of step-by-step guidance. ACCEPTANCE CRITERIA: • Issue #12 should bear the label: investigate-oom • Issue #12 is required to contain the exact new comment: Initial triage: OOM under training; mitigation underway. • Issue #12 must be set to the state: closed."
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

    # 17
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

    # 18
    Task(
        annotator='0',
        user_id="task_18",
        instruction=(
            "You are 'maya-w' and need to use only the available tools. YOUR GOAL • Change the name of the 'acme-webapp' repository to match the exact new name literal. • Adjust the renamed repository's visibility to the exact value literal. • Incorporate the exact topic literal into the renamed repository and confirm the topics. • Verify that the renamed repository is included in your list of owned repositories. • Ensure the most recent terminal entry corresponds exactly to the message literal. LITERALS (use verbatim) - old repo name: acme-webapp - new repo name: acme-webapp-qa - visibility: private - topic to add: qa-ready - terminal message: Repository acme-webapp renamed to acme-webapp-qa and set private; topic qa-ready added"
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="RenameRepository", kwargs={"old_name": "acme-webapp", "new_name": "acme-webapp-qa"}),
            Action(name="SetRepositoryVisibility", kwargs={"repo_name": "acme-webapp-qa", "visibility": "private"}),
            Action(name="AddRepoTopic", kwargs={"repo_name": "acme-webapp-qa", "topic": "qa-ready"}),
            Action(name="ListRepoTopics", kwargs={"repo_name": "acme-webapp-qa"}),
            Action(name="ListRepositories", kwargs={}),
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

    # 19
    Task(
        annotator='0',
        user_id="task_19",
        instruction=(
            "You are 'maya-w' and you should operate solely through the available tools. PERFORM THESE ACTIONS • Apply branch protection to the default branch of the repository 'acme-webapp' using the precise rule literal. • Confirm that protection is active for that branch. • Add the specified terminal message literal and make certain it is the most recent entry. LITERALS (use verbatim) - repo: acme-webapp - branch literal: main - protected flag: 'true' - rules object: {\"require_code_owner_reviews\": True} - terminal message: Branch protection enabled on acme-webapp main"
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "acme-webapp"}),
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
            '"message": "Branch protection enabled."',
            '"timestamp": "2025-08-21T12:00:00Z", "message": "Branch protection enabled on acme-webapp main"',
        ],
    ),

    # 21
    Task(
        annotator='0',
        user_id="task_21",
        instruction=(
            "You are 'design-team'. Review the open PRs in 'ui-kit', provide two comments on PR #11 with feedback 'Looks great overall!' and 'Can we optimize the load time?', retrieve details of PR #12, label issue #6 as 'reviewed', and log your feedback in the terminal."
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "design-team"}),
            Action(name="GetRepository", kwargs={"repo_name": "ui-kit"}),
            Action(name="ListOpenPullRequests", kwargs={"repo_name": "ui-kit"}),
            Action(name="CommentOnPullRequest", kwargs={"repo_name": "ui-kit", "pr_number": 11, "comment": "Looks great overall!"}),
            Action(name="CommentOnPullRequest", kwargs={"repo_name": "ui-kit", "pr_number": 11, "comment": "Can we optimize the load time?"}),
            Action(name="GetPullRequest", kwargs={"repo_name": "ui-kit", "pr_number": 12}),
            Action(name="AddLabelToIssue", kwargs={"repo_name": "ui-kit", "issue_number": 6, "label": "reviewed"}),
            Action(name="AppendTerminal", kwargs={"message": "PR #11 reviewed and issue #6 marked as reviewed"}),
        ],
        outputs=[
            '"message": "PR #11 reviewed and issue #6 marked as reviewed"',
        ],
    ),

    # 22
    Task(
        annotator='0',
        user_id="task_22",
        instruction=(
            "As 'infra-lead', evaluate merged pull requests in 'k8s-monitoring'. For each PR that has been merged, provide the list of altered files and the commit authors. PR #32 was integrated from the branch 'feature-alertmanager', and PR #34 from 'upgrade-prometheus'. In case any PR alters files within the 'config/' folder, create an issue titled 'Audit config changes' with the content 'Merged PRs modified files under config/ directory. Review needed.' Then add to the terminal log exactly: Audit results: PR #32 files: ['kubernetes/alertmanager.yaml', 'config/alertmanager.yml', 'docker-compose.yml'], authors: ['infra-lead'] PR #34 files: ['kubernetes/prometheus.yaml', 'config/prometheus.yml', 'docs/MONITORING.md'], authors: ['infra-lead']"
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "infra-lead"}),
            Action(name="GetRepository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="ListPullRequests", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="ListPullRequestFiles", kwargs={"repo_name": "k8s-monitoring", "pr_number": 32}),
            Action(name="ListCommits", kwargs={"repo_name": "k8s-monitoring", "branch": "feature-alertmanager"}),
            Action(name="ListPullRequestFiles", kwargs={"repo_name": "k8s-monitoring", "pr_number": 34}),
            Action(name="ListCommits", kwargs={"repo_name": "k8s-monitoring", "branch": "upgrade-prometheus"}),
            Action(name="CreateIssue", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Audit config changes",
                "body": "Merged PRs modified files under config/ directory. Review needed.",
            }),
            Action(name="AppendTerminal", kwargs={
                "message": (
                    "Audit results:\n"
                    "PR #32 files: ['kubernetes/alertmanager.yaml', 'config/alertmanager.yml', 'docker-compose.yml'], "
                    "authors: ['infra-lead']\n"
                    "PR #34 files: ['kubernetes/prometheus.yaml', 'config/prometheus.yml', 'docs/MONITORING.md'], "
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
            "As 'design-team', check that Alert #4 dismissal in 'ui-kit' is consistent with the latest commits on 'feature-theme'. Examine branch commits and the current alerts, inspect Issue #6, and add a review comment on PR #11 regarding security status. Append terminal: 'ui-kit XSS dismissal confirmed with feature-theme commits'."
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "design-team"}),
            Action(name="GetRepository", kwargs={"repo_name": "ui-kit"}),
            Action(name="ListCommits", kwargs={"repo_name": "ui-kit", "branch": "feature-theme"}),
            Action(name="ListCodeScanningAlerts", kwargs={"repo_name": "ui-kit"}),
            Action(name="GetIssue", kwargs={"repo_name": "ui-kit", "issue_number": 6}),
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
            "You are 'security-group'. For 'security-scanner', confirm the resolution of Issue #11 through PR #23 and examine the commits on 'perf-optimizations'. Develop a release called 'v0.3.1 Performance optimization' containing the text: 'Implements file system cache; closes #11; approximately 70% performance improvement.'. Add terminal note: 'Security scanner performance fix validated and released'."
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
                "body": "Implements file system cache; closes #11; ~70% perf improvement.",
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
            "You are 'language-ai'. Within 'nlp-models', ensure that PR #22 was merged for Issue #16 and examine Issue #12 concerning memory. Enumerate commits on the 'exp-transformer' branch to establish investigation context. Subsequently, comment on Issue #12 stating: 'Analyzed gradient accumulation commits on exp-transformer for memory optimization guidance.' Add terminal note: 'nlp-models checkpoint fix confirmed; memory follow-up acknowledged.'."
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
            "Assume the role of 'ui-developer'. For 'react-dashboard', ensure that PR #30 successfully closed Issue #27. Compile a list of open PRs and request changes on PR #28 by commenting: 'Resolve merge conflicts before merge.' Add the label 'investigate' to Issue #25. Append terminal: 'react-dashboard dark mode confirmed; realtime PR gated.'."
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
            "Serve as 'platform-team'. In the 'infra-terraform' project, review files on the 'feat-alb' branch, refer to Issue #9, and initiate a pull request from 'feat-alb' to 'main' titled 'Increase ALB health check timeout' with the body 'Addresses #9 by increasing target health check thresholds.' Subsequently, comment on Issue #9 stating: 'PR created to modify ALB health check duration and configuration.' Add to terminal: 'infra-terraform PR created to improve ALB health checks.'."
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
                "body": "Addresses #9 by raising the thresholds for target health checks.",
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
            "You are 'ml-engineer'. Within 'ml-pipeline', identify the commits in 'feature-mlflow-tracking' and examine the file content there. Update Issue #31 with the comment: 'Next step is drift detection.' End the terminal with: 'ml-pipeline MLflow integration reviewed; validation roadmap updated.'."
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
            "You are 'security-group'. Within 'security-scanner', evaluate open PR #25 and list the existing alerts. Comment on the PR: 'Verify SARIF schema v2.1.0 and CI upload procedure.' Next, open an issue titled 'SARIF configuration refinement' with the label 'enhancement' and the description: 'Refine schema validation and CI upload settings.' Conclude the terminal with: 'Security scanner SARIF review and configuration follow-up initiated.'."
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

    # 33
    Task(
        annotator='0',
        user_id="task_33",
        instruction=(
            "You are 'maya-w' and must function using only the provided tools. YOUR OBJECTIVE • In the 'acme-webapp' repository, formulate a new branch from the literal source branch indicated, incorporate a release-notes file with the exact literal content, perform a commit with the exact literal message, and authenticate the file's presence on the newly created branch. • Verify the latest terminal entry matches the exact literal message outlined below. LITERALS (use verbatim) - repo: acme-webapp - source branch: main - new branch: feature-banners - file path: docs/release-notes.md - file content: ## Release notes\\n- Seed entry\\n - commit message: docs: include release notes seed - terminal message: Release notes committed on feature-banners in acme-webapp"
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "acme-webapp"}),
            Action(name="CreateBranch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "feature-banners"
            }),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-banners",
                "path": "docs/release-notes.md",
                "content": "## Changelog\n- Initial data insertion\n"
            }),
            Action(name="CommitChangesToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-banners",
                "commit_message": "docs: add release notes seed"
            }),
            Action(name="ListFiles", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-banners"
            }),
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

    # 35
    Task(
        annotator='0',
        user_id="task_35",
        instruction=(
            "You are 'ui-developer'. You must implement baseline hardening on the default branch of the 'react-dashboard' repository and disseminate that fortified state as a lightweight release. The default branch has to be protected with the attribute set to 'true' and rules precisely as follows: { \"required_reviews\": 1, \"enforce_admins\": true }. Incorporate the repository topic 'security-hardening'. Launch a release with the tag 'task_65-hardened' and body 'Hardening rules applied [task_65]'. Provide the branch protection status and guidelines for the default branch, and include the terminal audit entry: 'Protection enabled and release task_65-hardened published for react-dashboard [task_65]'."
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "ui-developer"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "react-dashboard"}),
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
            Action(name="GetBranchProtection", kwargs={"repo_name": "react-dashboard", "branch": "main"}),
            Action(
                name="AppendTerminal",
                kwargs={"message": "Protection enabled and release task_65-hardened published for react-dashboard [task_65]"},
            ),
        ],
        outputs=[
            '"protected": "true", "rules": {"required_reviews": 1, "enforce_admins": true}',
            '"message": "Protection enabled and release task_65-hardened published for react-dashboard [task_65]"',
        ],
    ),

    # 37
    Task(
        annotator='0',
        user_id="task_37",
        instruction=(
            "You are 'maya-w', tasked with operations in 'acme-webapp'. Illustrate the process of managing a short-term working branch. Create a temporary branch named 'temp-branch' based on the repository's default branch. Use this branch to store a transient note at 'docs/tmp.txt' with the content 'temp work'. Verify that the note remains accessible as long as the branch is active, then retire the branch. When retiring the branch, log the action with the message: 'Branch temp-branch deleted in acme-webapp.'. Finally, list the branches left post-retirement. Return: (a) the file content obtained, (b) the audit message, and (c) the final list of branches."
        ),
        actions=[
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(name="GetDefaultBranch", kwargs={"repo_name": "acme-webapp"}),
            Action(name="CreateBranch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "temp-branch"
            }),
            Action(name="WriteFileToBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "temp-branch",
                "path": "docs/tmp.txt",
                "content": "temp work"
            }),
            Action(name="GetFileContents", kwargs={
                "repo_name": "acme-webapp",
                "branch": "temp-branch",
                "path": "docs/tmp.txt"
            }),
            Action(name="DeleteBranch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "temp-branch"
            }),
            Action(name="AppendTerminal", kwargs={
                "message": "Branch temp-branch deleted in acme-webapp."
            }),
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
            Action(name="GetMe", kwargs={"username": "maya-w"}),
            Action(
                name="CreateIssue",
                kwargs={
                    "repo_name": "acme-webapp",
                    "title": "Security audit [task_01]",
                    "body": "Check SQL injection handling paths. [task_01]",
                    "labels": []
                },
            ),
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
            Action(
                name="UpdateIssue",
                kwargs={"repo_name": "acme-webapp", "issue_number": 1, "state": "closed"},
            ),
            Action(
                name="SearchIssues",
                kwargs={"query": "security-check"},
            ),
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
            Action(name="GetMe", kwargs={"username": "ui-developer"}),
            Action(
                name="CreateIssue",
                kwargs={
                    "repo_name": "react-dashboard",
                    "title": "Build pipeline audit [task_72]",
                    "body": "Verify CI stages and artifacts for reproducibility. [task_72]",
                    "labels": []
                },
            ),
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
            Action(
                name="UpdateIssue",
                kwargs={"repo_name": "react-dashboard", "issue_number": 1, "state": "closed"},
            ),
            Action(
                name="SearchIssues",
                kwargs={"query": "ci-audit"},
            ),
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
            "You are part of the 'security-group'. Ensure the end state as specified, with precision in all values and case-sensitivity: • You own a repository called 'security-scanner-pro', its visibility set to 'public' and the default branch named 'main'. • Repository topics should include both 'security' and 'sarif'. • A branch named 'feature-sarif' must be established. On this branch, ensure 'src/scanner.py' reads exactly 'print('sarif-v1')' and 'README.md' shows precisely '# security-scanner-pro'. • The most recent commit on 'feature-sarif' should convey the message 'Add SARIF support scaffolding'. • Pull request #1 must switch from head 'feature-sarif' to base 'main', with title 'Add SARIF output support' and body 'Introduce SARIF output skeleton.', including requested reviewers 'qa-mike' and 'dev-sue', and undergo approval and merging. • A release for 'security-scanner-pro' must be created with tag 'v0.5.0', title 'SARIF support', and body 'Initial SARIF output format release.', with the latest release linked to tag 'v0.5.0'."
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
            "Assume the role of 'infra-lead'. Fulfill the following final state, ensuring all values are precise and case-sensitive: • A repository identified as 'k8s-ci-pipelines' is present and owned by you; it's set to 'public' visibility, with 'main' as the default branch. The repository topics must contain 'kubernetes'. • Ensure a branch named 'feature-alerts' is available. Within this branch, the file 'kubernetes/alerts.yaml' holds exactly 'alertmanager: routes: placeholder-v2', and 'docs/alerts.md' has precisely '# Alerts Runbook'. • The latest commit on 'feature-alerts' should bear the message 'Add alert routing and runbook'. • Submit pull request #1 targeting the main branch from the feature-alerts head, with the title 'Introduce alert routing' and body 'Add Alertmanager routes and docs.', ensuring approval and merging. • Activate branch protection on 'main' with the rule {'required_reviews': 1}. • An issue named 'Branch protection enabled on main' must exist with the body 'Required reviews set to 1.' and tagged 'security'. • The terminal log should contain a single new entry stating 'k8s-ci-pipelines protection enabled on main.'."
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

    # 20
    Task(
        annotator="0",
        user_id="task_20",
        instruction=(
            "As 'app-developer', in the repository 'flutter-finance-app', establish the following final condition with all values exact and case-sensitive: • A branch named 'hotfix-1.2.1' is present. Within this branch, the 'CHANGELOG.md' file includes precisely '## 1.2.1 - hotfix'. • The latest commit on 'hotfix-1.2.1' has the message 'Add CHANGELOG for v1.2.1'. • There is a release tagged 'v1.2.1', named 'v1.2.1 [task_101]', with the description 'body-[task_101]'. Furthermore, the latest release aligns with the tag 'v1.2.1'. • An issue titled 'Release v1.2.1 note [task_101]' exists with body 'body-[task_101]' and label 'release-log'. • The terminal log contains exactly: 'Release v1.2.1 created in flutter-finance-app [task_101]'."
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
            '"tag_name": "v1.2.1"',
            '"labels": ["release-log"]',
            '"message": "Release v1.2.1 created in flutter-finance-app [task_101]"',
        ],
    ),
]
