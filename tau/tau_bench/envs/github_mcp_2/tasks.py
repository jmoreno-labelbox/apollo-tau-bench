
tasks = [
    {
        "annotator": 0,
        "user_id": "task_28",
        "instruction": "You act as 'app-developer'. In 'flutter-finance-app', assess Issue #18 along with PR #26. Sanction the PR with the comment: 'Please confirm rendering on iOS 14 and 15 real devices.' which solicits validation on iOS 14/15, and mark the issue with 'ios1'. Retrieve the last terminal message, then add 'flutter-finance-app iOS charts fix under validation'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "app-developer"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "flutter-finance-app"
                },
            },
            {
                "name": "GetIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "issue_number": 18
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "pr_number": 26
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "pr_number": 26,
                    "review_decision": "approve",
                    "comment": "Please confirm rendering on iOS 14 and 15 real devices."
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "issue_number": 18,
                    "label": "ios1"
                },
            },
            {
                "name": "ListTerminalLastMessage",
                "arguments": {
                {}
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "flutter-finance-app iOS charts fix under validation"
                }
            }
        ],
        "outputs": [
                {"message": "flutter-finance-app iOS charts fix under validation"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_45",
        "instruction": "You take on the role of 'infra-lead'. Your task is to bring about the following definitive state, with every value exact and adhering to case sensitivity: \u2022 A repository titled 'observability-ops' should be in place under your ownership; its visibility set as 'private', which you must switch to 'public', its principal branch being 'main', and it should include the topic 'kubernetes'. \u2022 A branch 'feature-initial-config' is present. On that branch, the file 'kubernetes/alertmanager.yaml' is required to contain exactly 'alertmanager: config: placeholder-v1', and the file 'kubernetes/prometheus.yaml' must have exactly 'prometheus: config: placeholder-v1'. \u2022 The most recent commit on 'feature-initial-config' includes the message 'Add initial Prometheus/Alertmanager manifests'. \u2022 Pull request #1 aims at the base 'main' from the head 'feature-initial-config' with the heading 'Add initial Kubernetes monitoring stack' and content 'Bootstrap Prometheus and Alertmanager manifests.', it is sanctioned, and has been amalgamated. \u2022 A release is present on 'observability-ops' tagged as 'v0.1.0', with the headline 'Initial monitoring stack', and description 'First cut of monitoring components.'. \u2022 The terminal log must have exactly one additional entry with the note 'observability-ops v0.1.0 released.' Ensure all mandates are met during a new database execution; utilize deterministic values exclusively.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "observability-ops",
                    "visibility": "private",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "observability-ops",
                    "topic": "kubernetes"
                },
            },
            {
                "name": "SetRepositoryVisibility",
                "arguments": {
                    "repo_name": "observability-ops",
                    "visibility": "public"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "observability-ops",
                    "source_branch": "main",
                    "new_branch": "feature-initial-config"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "observability-ops",
                    "branch": "feature-initial-config",
                    "path": "kubernetes/alertmanager.yaml",
                    "content": "alertmanager: config: placeholder-v1"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "observability-ops",
                    "branch": "feature-initial-config",
                    "path": "kubernetes/prometheus.yaml",
                    "content": "prometheus: config: placeholder-v1"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "observability-ops",
                    "branch": "feature-initial-config",
                    "commit_message": "Add initial Prometheus/Alertmanager manifests"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "observability-ops",
                    "title": "Add initial Kubernetes monitoring stack",
                    "body": "Bootstrap Prometheus and Alertmanager manifests.",
                    "base": "main",
                    "head": "feature-initial-config"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "observability-ops",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "observability-ops",
                    "pr_number": 1
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "observability-ops",
                    "tag": "v0.1.0",
                    "title": "Initial monitoring stack",
                    "body": "First cut of monitoring components."
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "observability-ops v0.1.0 released."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "observability-ops""},
                {"message": "Pull request opened", "title": ""Add initial Kubernetes monitoring stack", "pr_number": 1"},
                {"message": "Pull request merged."},
                {"message": "Release created.", "repo_name": ""observability-ops", "tag_name": "v0.1.0""},
                {"message": "observability-ops v0.1.0 released."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_23",
        "instruction": "You are 'maya-w'. In 'acme-webapp', handle the reconciliation of the code scanning alert that mentions 'feature-auth' using the merged PR #5 from that branch. Check the current branches, details of PR #5, and the altered files. Open an issue with the title 'Reconcile alert ref: feature-auth' and use labels ['investigate','security'] with the description 'Alert points to feature-auth which was merged and branch is missing in current snapshot; verify lineage and fix metadata'. After that, record this terminal entry: 'acme-webapp alert ref reconciliation recorded'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "ListBranches",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "ListCodeScanningAlerts",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "ListPullRequests",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 5
                },
            },
            {
                "name": "ListPullRequestFiles",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 5
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Reconcile alert ref: feature-auth",
                    "body": "Alert points to feature-auth which was merged and branch is missing in current snapshot; verify lineage and fix metadata",
                    "labels": [
                        {investigate},
                        {security}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "acme-webapp alert ref reconciliation recorded"
                }
            }
        ],
        "outputs": [
                {"message": "acme-webapp alert ref reconciliation recorded"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_38",
        "instruction": "You are 'maya-w'. In the repository 'acme-webapp', initiate a new issue titled 'Security triage [task_66]' with the contents 'Investigate dependency exposure paths. [task_66]'. This issue should have the label 'triage-urgent', include the precise comment 'Initial triage note recorded. [task_66]', and must be 'closed' as its final status. Confirm the label's assignment, the issue's final state, and provide a search result that verifies the presence of the issue with the label 'triage-urgent'. Additionally, record this in the terminal audit line: 'Issue closed with triage-urgent label in acme-webapp [task_66]'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Security triage [task_66]",
                    "body": "Investigate dependency exposure paths. [task_66]",
                    "labels": []
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "label": "triage-urgent"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "comment": "Initial triage note recorded. [task_66]"
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "state": "closed"
                },
            },
            {
                "name": "SearchIssues",
                "arguments": {
                    "query": "triage-urgent"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Issue closed with triage-urgent label in acme-webapp [task_66]"
                }
            }
        ],
        "outputs": [
                {"message": "Label 'triage-urgent' added."},
                {"state": "closed"},
                {\}results": [1]",
                {"message": "Issue closed with triage-urgent label in acme-webapp [task_66]"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_04",
        "instruction": "You are user 'maya-w'. Examine the repository 'acme-webapp' for any pending PRs. Provide comments on PR #5 twice using feedbacks 'Looks good overall' and 'Please add more tests', then summarize your actions in the terminal with the message 'Comments added and PR #5 reviewed.'",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "ListOpenPullRequests",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "CommentOnPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 5,
                    "comment": "Looks good overall"
                },
            },
            {
                "name": "CommentOnPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 5,
                    "comment": "Please add more tests"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Comments added and PR #5 reviewed."
                }
            }
        ],
        "outputs": [
                {Comments added and PR #5 reviewed.}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_36",
        "instruction": "You are 'maya-w' and required to operate solely through the provided tools. Verify that the final state of the repository 'acme-webapp' meets ALL the acceptance criteria listed below. Consider these as outcomes/specifications\u2014not step-by-step instructions. ACCEPTANCE CRITERIA (all must be satisfied): \u2022 A branch named 'file-crud' is present, originating from 'main'. \u2022 The file docs/note.txt is present on branch 'file-crud' and its final content is exactly: 'Hello v2'. \u2022 During the operation, the content 'Hello v1' was recorded in docs/note.txt and successfully read back once (include the read result in outputs). \u2022 The modification is committed with the exact commit message: 'docs(note): update to v2'. \u2022 A pull request is made from 'file-crud' into 'main' titled 'File CRUD update' with the body 'Promote CRUD change for docs/note.txt', and the PR indicates docs/note.txt as a modified file. LITERALS TO USE VERBATIM: - repo: acme-webapp - source branch: main - new branch: file-crud - path: docs/note.txt - v1 content: Hello v1 - v2 content: Hello v2 - commit message: docs(note): update to v2 - PR title: File CRUD update - PR body: Promote CRUD change for docs/note.txt",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "source_branch": "main",
                    "new_branch": "file-crud"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "file-crud",
                    "path": "docs/note.txt",
                    "content": "Hello v1"
                },
            },
            {
                "name": "GetFileContents",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "file-crud",
                    "path": "docs/note.txt"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "file-crud",
                    "path": "docs/note.txt",
                    "content": "Hello v2"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "file-crud",
                    "commit_message": "docs(note): update to v2"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "File CRUD update",
                    "body": "Promote CRUD change for docs/note.txt",
                    "head": "file-crud",
                    "base": "main"
                },
            },
            {
                "name": "ListPullRequestFiles",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 1
                }
            }
        ],
        "outputs": [
                {"message": "Branch created"},
                {"path": "docs/note.txt", "content": "Hello v1""},
                {\}docs/note.txt""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_79",
        "instruction": "As a 'infra-lead', it is your role to assess a shell script amendment prior to its integration. Within the public repository 'acme-scripts', monitor modifications on a feature branch 'fix-script' derived from the 'main' branch, focusing on updates made to the script 'scripts/run.sh'. Initially, the script displays 'HELLO', with an adjustment later to also reveal 'WORLD'. During the process, capture a terminal log halfway with the message 'RUN'. After committing changes and initiating a pull request, examine both the file differences and the log results. Refer to these file content details: - Initial: '#!/usr/bin/env bash\necho HELLO\n' - Final: '#!/usr/bin/env bash\necho HELLO\necho WORLD\n' - Commit messages: 'feat: add run script' and 'fix: append WORLD echo' - PR title: 'Fix run script', body: 'Append WORLD echo to run.sh' Provide the ultimate terminal log along with the list of modified files in the PR.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "acme-scripts",
                    "visibility": "public"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "acme-scripts",
                    "source_branch": "main",
                    "new_branch": "fix-script"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-scripts",
                    "branch": "fix-script",
                    "path": "scripts/run.sh",
                    "content": "#!/usr/bin/env bash\necho HELLO\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-scripts",
                    "branch": "fix-script",
                    "commit_message": "feat: add run script"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "RUN"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-scripts",
                    "branch": "fix-script",
                    "path": "scripts/run.sh",
                    "content": "#!/usr/bin/env bash\necho HELLO\necho WORLD\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-scripts",
                    "branch": "fix-script",
                    "commit_message": "fix: append WORLD echo"
                },
            },
            {
                "name": "InitializePullRequestsBlock",
                "arguments": {
                    "repo_name": "acme-scripts"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "acme-scripts",
                    "title": "Fix run script",
                    "body": "Append WORLD echo to run.sh",
                    "head": "fix-script",
                    "base": "main"
                },
            },
            {
                "name": "ListPullRequestFiles",
                "arguments": {
                    "repo_name": "acme-scripts",
                    "pr_number": 1
                },
            },
            {
                "name": "ListTerminalLastMessage",
                "arguments": {
                {}
                }
            }
        ],
        "outputs": [
                {"timestamp": "2025-08-21T12:00:00Z", "message": "RUN""},
                {\}scripts/run.sh""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_39",
        "instruction": "Your task as a 'ui-developer' is to work solely with the tools at your disposal. Confirm that the 'react-dashboard' repository fulfills ALL the acceptance criteria outlined below. These should be viewed as objectives/specifications\u2014not as procedural instructions. ACCEPTANCE CRITERIA (all conditions must be satisfied): \u2022 An issue must be present with the title 'Build pipeline audit [task_69]' and the body 'Verify CI stages and artifacts for reproducibility. [task_69]'. \u2022 This issue should bear the label 'ci-audit', incorporate the precise comment 'Checklist prepared. [task_69]', and be marked 'closed'. \u2022 It should be possible to confirm via a search that an issue with the label 'ci-audit' is available in 'react-dashboard'. \u2022 There should be a terminal log stating exactly: 'Issue closed with ci-audit label in react-dashboard [task_69]'. LITERALS TO USE VERBATIM: - repo: react-dashboard - issue title: Build pipeline audit [task_69] - issue body: Verify CI stages and artifacts for reproducibility. [task_69] - label: ci-audit - comment: Checklist prepared. [task_69] - terminal message: Issue closed with ci-audit label in react-dashboard [task_69]",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ui-developer"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "title": "Build pipeline audit [task_69]",
                    "body": "Verify CI stages and artifacts for reproducibility. [task_69]",
                    "labels": []
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 1,
                    "label": "ci-audit"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 1,
                    "comment": "Checklist prepared. [task_69]"
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 1,
                    "state": "closed"
                },
            },
            {
                "name": "SearchIssues",
                "arguments": {
                    "query": "ci-audit"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Issue closed with ci-audit label in react-dashboard [task_69]"
                }
            }
        ],
        "outputs": [
                {"message": "Label 'ci-audit' added."},
                {"state": "closed"},
                {\}results": [1]",
                {"message": "Issue closed with ci-audit label in react-dashboard [task_69]"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_32",
        "instruction": "Operate as 'maya-w' using solely the available tools. Confirm that the final state of the repository 'acme-webapp' meets ALL the acceptance criteria detailed below. Consider these as outcomes/specification\u2014not procedural instructions. ACCEPTANCE CRITERIA (all must be satisfied): \u2022 An issue is present titled 'Nightly job failed on main' with the body \"CI job 'nightly-build' failed due to timeout.\". \u2022 The issue possesses the label 'ops', includes the precise comment 'Investigating: rerun queued.', and is in the 'closed' state. \u2022 The latest terminal log is specifically: 'Issue #1 closed: Nightly job failed on main'. LITERALS TO USE VERBATIM: - repo: acme-webapp - issue title: Nightly job failed on main - issue body: CI job 'nightly-build' failed due to timeout. - label to add: ops - issue comment: Investigating: rerun queued. - terminal message: Issue #1 closed: Nightly job failed on main",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Nightly job failed on main",
                    "body": "CI job 'nightly-build' failed due to timeout."
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "label": "ops"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "comment": "Investigating: rerun queued."
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "state": "closed"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Issue #1 closed: Nightly job failed on main"
                },
            },
            {
                "name": "ListTerminalLastMessage",
                "arguments": {
                {}
                }
            }
        ],
        "outputs": [
                {"message": "Issue created", "number": 1"},
                {"message": "Label 'ops' added."},
                {"timestamp": "2025-08-21T12:00:00Z", "message": "Issue #1 closed: Nightly job failed on main""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_78",
        "instruction": "Act as 'security-group' and engage only via the available tools. Verify that the ending state of the repository 'security-scanner' fulfills ALL the acceptance criteria outlined below. These should be seen as outcomes/specification\u2014not step-by-step directives. ACCEPTANCE CRITERIA (all conditions must be met): \u2022 A branch named 'sec-checks' has been created, branching from the default branch. \u2022 Within that branch, ensure the file '.github/workflows/security.yml' is present and its contents are exactly: on: [push] jobs: scan: runs-on: ubuntu-latest steps: - name: Security scan run: echo SCAN \u2022 The commit message is: 'chore: add security workflow'. \u2022 A pull request exists with the title 'Add security workflow' and the body 'Adds a basic GitHub Actions scan workflow.' from 'sec-checks' into the default branch. \u2022 Outputs should comprise the list of files changed in that pull request and any open code scanning alerts bearing the 'critical' severity. LITERALS TO USE VERBATIM: - repo: security-scanner - branch: sec-checks - path: .github/workflows/security.yml - workflow content: on: [push]\njobs:\n scan:\n runs-on: ubuntu-latest\n steps:\n - name: Security scan\n run: echo SCAN - commit message: chore: add security workflow - PR title: Add security workflow - PR body: Adds a basic GitHub Actions scan workflow. - severity: critical",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "security-group"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "source_branch": "main",
                    "new_branch": "sec-checks"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "sec-checks",
                    "path": ".github/workflows/security.yml",
                    "content": "on: [push]\njobs:\n  scan:\n    runs-on: ubuntu-latest\n    steps:\n      - name: Security scan\n        run: echo SCAN"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "sec-checks",
                    "commit_message": "chore: add security workflow"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Add security workflow",
                    "body": "Adds a basic GitHub Actions scan workflow.",
                    "head": "sec-checks",
                    "base": "main"
                },
            },
            {
                "name": "ListPullRequestFiles",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 1
                },
            },
            {
                "name": "ListCodeScanningAlerts",
                "arguments": {
                    "repo_name": "security-scanner",
                    "severity": "critical"
                }
            }
        ],
        "outputs": [
                {\}.github/workflows/security.yml"",
                {"severity": "critical"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_83",
        "instruction": "You are maya-w. Within the 'acme-webapp' repository, initiate a branch titled 'feature-codeowners' stemming from the default branch. Introduce a file at the location '.github/CODEOWNERS' with the precise content: * @alice-w src/ @dev-sue tests/ @qa-mike Submit this file with the commit message 'chore: add CODEOWNERS'. Subsequently, set up a pull request to merge 'feature-codeowners' into the default branch with the title 'Add CODEOWNERS' and the body 'CODEOWNERS file added for ownership mapping.'. Add a pull request review comment stating 'Please review CODEOWNERS ownership setup.' Lastly, provide the list of files changed in that PR.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "new_branch": "feature-codeowners",
                    "source_branch": "main"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature-codeowners",
                    "path": ".github/CODEOWNERS",
                    "content": "* @alice-w\nsrc/ @dev-sue\ntests/ @qa-mike\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature-codeowners",
                    "commit_message": "chore: add CODEOWNERS"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Add CODEOWNERS",
                    "body": "CODEOWNERS file added for ownership mapping.",
                    "head": "feature-codeowners",
                    "base": "main"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 1,
                    "review_decision": "comment",
                    "body": "Please review CODEOWNERS ownership setup."
                },
            },
            {
                "name": "ListPullRequestFiles",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 1
                }
            }
        ],
        "outputs": [
                {{\}files": [".github/CODEOWNERS"]}"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_40",
        "instruction": "You are 'maya-w' and must manage tasks solely through the provided tools. Verify that the final repository condition in 'acme-webapp' meets ALL the acceptance criteria outlined below. Consider these as outcomes/specification\u2014not a step-by-step process. ACCEPTANCE CRITERIA (all must be met): \u2022 A feature branch called 'temp-pr' is established from the default branch and holds a file located at 'docs/pr_demo.txt' with the content precisely: 'temporary PR'. \u2022 A pull request is present titled 'Temp PR demo' with the body 'Demonstration of temporary PR lifecycle.' originating from head 'temp-pr' into the default branch. \u2022 The pull request is subsequently canceled by removing its head branch: the branch 'temp-pr' is no longer present. \u2022 A terminal log is created containing the message exactly: 'PR Temp PR demo withdrawn in acme-webapp.'. \u2022 Return the pull request title in outputs. LITERALS TO USE VERBATIM: - repo: acme-webapp - base branch: main - head branch: temp-pr - path: docs/pr_demo.txt - file content: temporary PR - PR title: Temp PR demo - PR body: Demonstration of temporary PR lifecycle. - terminal message: PR Temp PR demo withdrawn in acme-webapp.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "source_branch": "main",
                    "new_branch": "temp-pr"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "temp-pr",
                    "path": "docs/pr_demo.txt",
                    "content": "temporary PR"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Temp PR demo",
                    "body": "Demonstration of temporary PR lifecycle.",
                    "head": "temp-pr",
                    "base": "main"
                },
            },
            {
                "name": "DeleteBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "temp-pr"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "PR Temp PR demo withdrawn in acme-webapp."
                }
            }
        ],
        "outputs": [
                {"title": "Temp PR demo"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_43",
        "instruction": "Act as 'ryan-dev'. Within the 'utils-js' repository, generate a new issue named 'Utilities module audit [task_73]' including the body 'Review currency formatting and TypeScript support. [task_73]'. Ensure the issue bears the label 'module-audit', contains the exact comment 'Audit completed. [task_73]', and its final status is 'closed'. Provide verification of the label application, the issue's concluding status, and a search result entry confirming an issue with the label 'module-audit' is present. Incorporate this terminal audit statement: 'Issue closed with module-audit label in utils-js [task_73]'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ryan-dev"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "Utilities module audit [task_73]",
                    "body": "Review currency formatting and TypeScript support. [task_73]",
                    "labels": []
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 1,
                    "label": "module-audit"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 1,
                    "comment": "Audit completed. [task_73]"
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 1,
                    "state": "closed"
                },
            },
            {
                "name": "SearchIssues",
                "arguments": {
                    "query": "module-audit"
                },
            },
            {
                "name": "GetIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 1
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Issue closed with module-audit label in utils-js [task_73]"
                },
            },
            {
                "name": "ListTerminalLastMessage",
                "arguments": {
                {}
                }
            }
        ],
        "outputs": [
                {"message": "Label 'module-audit' added."},
                {"state": "closed"},
                {\}results": [1]",
                {"title": "Utilities module audit [task_73]"},
                {"labels": [\module-audit"]"},
                {"message": "Issue closed with module-audit label in utils-js [task_73]"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_82",
        "instruction": "Operate as 'design-team' exclusively using the designated tools. Guarantee the ultimate repository state in 'ui-kit' meets ALL acceptance criteria detailed below, treating these as specification outcomes, not procedural steps. ACCEPTANCE CRITERIA (all criteria must be fulfilled): \u2022 Existence of a branch named 'feature-validate' that diverges from 'main' by appending a file at path 'docs/validation.md' with content precisely: 'Validation test: head==base should not merge.'. \u2022 Presence of a commit on 'feature-validate' with the exact message: 'Add docs/validation.md for merge validation test'. \u2022 A pull request #1 present in repository 'ui-kit' titled 'Validate merge blocking when head==base' with body 'This PR intentionally uses the same branch for head and base to verify merge validation.', both head and base on 'feature-validate'. \u2022 Rejection of an attempt to merge the pull request, with message 'Pull request rejected.' citing 'head and base branch are the same', alongside a false merged indicator. \u2022 An ending entry containing the specific message: 'PR #1 rejected in ui-kit: head equals base (validation).' STRINGS TO USE EXACTLY: - repo: ui-kit - source branch: main - working branch: feature-validate - path: docs/validation.md - file content: Validation test: head==base should not merge. - commit message: Add docs/validation.md for merge validation test - PR number: 1 - PR title: Validate merge blocking when head==base - PR body: This PR intentionally uses the same branch for head and base to verify merge validation. - terminal message: PR #1 rejected in ui-kit: head equals base (validation).",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "design-team"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "source_branch": "main",
                    "new_branch": "feature-validate"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature-validate",
                    "path": "docs/validation.md",
                    "content": "Validation test: head==base should not merge."
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature-validate",
                    "commit_message": "Add docs/validation.md for merge validation test"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Validate merge blocking when head==base",
                    "body": "This PR intentionally uses the same branch for head and base to verify merge validation.",
                    "base": "feature-validate",
                    "head": "feature-validate"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 1
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "PR #1 rejected in ui-kit: head equals base (validation)."
                }
            }
        ],
        "outputs": [
                {"message": "Pull request rejected."},
                {"reason": "head and base branch are the same"},
                {"merged": "false"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_80",
        "instruction": "As 'maya-w', work solely utilizing the tools provided. Ensure the ultimate condition of the repository 'acme-webapp' meets ALL acceptance criteria below; these should be viewed as outcomes/specification, not as step-by-step instructions. ACCEPTANCE CRITERIA (all must be fulfilled): \u2022 An open issue exists with the title 'Fix crash on startup' and content 'Application crashes due to missing env var check', that tracks the application startup crash. \u2022 The default branch contains a branch called 'fix-startup', and 'src/main.py' includes the line: 'assert ENV_VAR is not None'. This change is committed with the message 'fix: guard against missing ENV_VAR'. \u2022 A pull request has been initiated from 'fix-startup' to the default branch, titled 'Fix startup crash', with content 'Adds env var guard clause', and this pull request is merged. \u2022 Provide the issue metadata and the pull request title in outputs. LITERALS TO USE VERBATIM: - repo: acme-webapp - issue title: Fix crash on startup - issue body: Application crashes due to missing env var check - branch: fix-startup - path: src/main.py - code line: assert ENV_VAR is not None - commit message: fix: guard against missing ENV_VAR - PR title: Fix startup crash - PR body: Adds env var guard clause",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Fix crash on startup",
                    "body": "Application crashes due to missing env var check"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "source_branch": "main",
                    "new_branch": "fix-startup"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "fix-startup",
                    "path": "src/main.py",
                    "content": "assert ENV_VAR is not None"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "fix-startup",
                    "commit_message": "fix: guard against missing ENV_VAR"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Fix startup crash",
                    "body": "Adds env var guard clause",
                    "head": "fix-startup",
                    "base": "main"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 1
                },
            },
            {
                "name": "GetIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1
                }
            }
        ],
        "outputs": [
                {"number": 1},
                {"title": "Fix crash on startup"},
                {"state": "open"},
                {"title": "Fix startup crash"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_44",
        "instruction": "Act as 'design-team'. In the 'ui-kit' repository, there needs to be a pull request #11 entitled 'Introduce Theme Provider'. Submit the precise review comment 'Theme reviewed. [task_74]' on it, then approve and merge it. Provide the PR number, its final status 'merged', and a terminal entry that reads 'PR #11 merged with review in ui-kit [task_74]'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "design-team"
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 11
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 11,
                    "review_decision": "approve",
                    "comment": "Theme reviewed. [task_74]"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 11
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "PR #11 merged with review in ui-kit [task_74]"
                }
            }
        ],
        "outputs": [
                {"pr_number": 11},
                {"state": "merged"},
                {"message": "PR #11 merged with review in ui-kit [task_74]"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_58",
        "instruction": "As 'server-main', you're required to finalize tasks on the repository state for 'payments-service', ensuring ALL of the following conditions are met: \u2022 There must be a documentation file located at 'docs/RETRY_POLICY.md' on the 'main' branch, containing the PRECISE text 'Retries: up to 2 attempts with exponential backoff starting at 250ms. Idempotency required for POST.'. \u2022 This revision should start from a branch named 'feature-retry-policy' and be represented by a commit whose message is EXACTLY 'Add retry policy documentation'. \u2022 Ensure the modification is introduced into 'main' through a reviewed pull request titled 'Add retry policy docs'; a review request must be sent to 'qa-erin', and an approving review with the exact comment 'LGTM' should be recorded. \u2022 A release tagged as 'v0.3.0', titled 'Retry policy docs', and with the body 'Publish retry policy documentation.' must exist, with the latest release showing tag 'v0.3.0'. \u2022 An issue must exist with the title 'Retry policy published' and body 'Docs merged and released as v0.3.0.' carrying the label 'documentation'. \u2022 The terminal audit log must contain the EXACT entry 'payments-service retry policy docs published and released as v0.3.0.'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "server-main"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "payments-service"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "source_branch": "main",
                    "new_branch": "feature-retry-policy"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "feature-retry-policy",
                    "path": "docs/RETRY_POLICY.md",
                    "content": "Retries: up to 2 attempts with exponential backoff starting at 250ms. Idempotency required for POST."
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "feature-retry-policy",
                    "commit_message": "Add retry policy documentation"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Add retry policy docs",
                    "base": "main",
                    "head": "feature-retry-policy"
                },
            },
            {
                "name": "RequestPullRequestReviewers",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 1,
                    "reviewers": [
                        {qa-erin}
                    ]
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 1,
                    "review_decision": "approve",
                    "comment": "LGTM"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 1
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "payments-service",
                    "tag": "v0.3.0",
                    "title": "Retry policy docs",
                    "body": "Publish retry policy documentation."
                },
            },
            {
                "name": "GetLatestRelease",
                "arguments": {
                    "repo_name": "payments-service"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Retry policy published",
                    "body": "Docs merged and released as v0.3.0.",
                    "labels": [
                        {documentation}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "payments-service retry policy docs published and released as v0.3.0."
                }
            }
        ],
        "outputs": [
                {"message": "Branch created", "new_branch": ""feature-retry-policy", "from": "main""},
                {"message": "Committed to branch", "repo": ""payments-service", "branch": ""feature-retry-policy", "commit_sha": "sha_0000000000000000000000000000000000000000""},
                {"message": "Pull request opened", "title": ""Add retry policy docs", "base": ""main", "head": ""feature-retry-policy", "pr_number": 1"},
                {"message": "Reviewers requested.", "pr_number": 1"},
                {"message": "Review submitted."},
                {"message": "Pull request merged.", "merged": ""true", "merge_method": "merge""},
                {"message": "Release created.", "repo_name": ""payments-service", "tag_name": ""v0.3.0", "title": "Retry policy docs""},
                {"tag_name": "v0.3.0", "body": "Publish retry policy documentation.""},
                {"message": "Issue created", "number": 1"},
                {"printed_ts": "2025-08-21T12:00:00Z", "message": "payments-service retry policy docs published and released as v0.3.0.""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_08",
        "instruction": "You hold the role of 'infra-lead'. Within 'k8s-monitoring', confirm the default branch and merely list the commits in branch 'upgrade-prometheus'. Check open alerts by listing them to ensure Alert #45 remains open; subsequently, initiate an issue titled 'Harden TLS for Prometheus scrape' with labels ['security','prometheus'] and body: 'Alert #45 still open after v2.45.0 upgrade; enforce modern ciphers and TLS versions.'. Add to the terminal: 'k8s-monitoring TLS hardening tracked post-upgrade'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "ListCommits",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "upgrade-prometheus"
                },
            },
            {
                "name": "ListCodeScanningAlerts",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Harden TLS for Prometheus scrape",
                    "body": "Alert #45 still open after v2.45.0 upgrade; enforce modern ciphers and TLS versions.",
                    "labels": [
                        {security},
                        {prometheus}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "k8s-monitoring TLS hardening tracked post-upgrade"
                }
            }
        ],
        "outputs": [
                {"message": "k8s-monitoring TLS hardening tracked post-upgrade"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_84",
        "instruction": "Your task is 'server-main'. Within 'payments-service', synchronize PR #21 with Issue #13 (3DS). Examine the repository, the issue, and the PR, and detail any existing code scanning alerts. Tag Issue #13 with 'needs-tests', comment as follows: 'PR #21 implements 3DS; add unit tests for fallback coverage before merging.', and provide a PR review to 'request_changes' accompanied by the comment: 'Please include unit tests for 3DS fallback flows.'. Conclude with terminal: 'payments-service 3DS alignment and test gating noted'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "server-main"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "payments-service"
                },
            },
            {
                "name": "GetIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 13
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 21
                },
            },
            {
                "name": "ListCodeScanningAlerts",
                "arguments": {
                    "repo_name": "payments-service"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 13,
                    "label": "needs-tests"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 13,
                    "comment": "PR #21 implements 3DS; add unit tests for fallback coverage before merge."
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 21,
                    "review_decision": "request_changes",
                    "comment": "Please include unit tests for 3DS fallback flows."
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "payments-service 3DS alignment and test gating noted"
                }
            }
        ],
        "outputs": [
                {"message": "payments-service 3DS alignment and test gating noted"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_60",
        "instruction": "Your role is 'design-team'. Make sure that once your task is finalized, the 'ui-kit' repository should uphold ALL the following conditions: \u2022 A documentation file is present at 'docs/ACCESSIBILITY.md' containing the EXACT text 'All UI components must meet WCAG 2.1 AA. Provide ARIA labels for interactive elements. Keyboard navigation required.'. \u2022 The update starts from a branch known as 'feature-accessibility-docs' and is documented by a commit with the EXACT message 'Add accessibility documentation'. \u2022 This update is integrated into 'main' through a reviewed pull request titled 'Accessibility docs'; a review is requested from 'design-lead', and an approval review with the precise comment 'Approved for accessibility' is cataloged. \u2022 The repository is tagged with the subject 'accessibility'. \u2022 A release is marked with tag 'v2.0.0', title 'Accessibility docs', and a body that states 'Add accessibility documentation.', with the most recent release showing tag 'v2.0.0'. \u2022 There exists an issue termed 'Accessibility docs published' with the content 'Docs merged and released as v2.0.0.' tagged 'documentation'. \u2022 The terminal audit log has the EXACT note 'ui-kit accessibility docs published and released as v2.0.0.'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "design-team"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "source_branch": "main",
                    "new_branch": "feature-accessibility-docs"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature-accessibility-docs",
                    "path": "docs/ACCESSIBILITY.md",
                    "content": "All UI components must meet WCAG 2.1 AA. Provide ARIA labels for interactive elements. Keyboard navigation required."
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature-accessibility-docs",
                    "commit_message": "Add accessibility documentation"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Accessibility docs",
                    "base": "main",
                    "head": "feature-accessibility-docs"
                },
            },
            {
                "name": "RequestPullRequestReviewers",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 1,
                    "reviewers": [
                        {design-lead}
                    ]
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 1,
                    "review_decision": "approve",
                    "comment": "Approved for accessibility"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 1
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "ui-kit",
                    "topic": "accessibility"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "ui-kit",
                    "tag": "v2.0.0",
                    "title": "Accessibility docs",
                    "body": "Add accessibility documentation."
                },
            },
            {
                "name": "GetLatestRelease",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Accessibility docs published",
                    "body": "Docs merged and released as v2.0.0.",
                    "labels": [
                        {documentation}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "ui-kit accessibility docs published and released as v2.0.0."
                }
            }
        ],
        "outputs": [
                {"message": "Branch created", "new_branch": ""feature-accessibility-docs", "from": "main""},
                {"message": "Committed to branch", "repo": ""ui-kit", "branch": ""feature-accessibility-docs", "commit_sha": "sha_0000000000000000000000000000000000000000""},
                {"message": "Pull request opened", "title": ""Accessibility docs", "base": ""main", "head": ""feature-accessibility-docs", "pr_number": 1"},
                {"message": "Reviewers requested.", "pr_number": 1"},
                {"message": "Review submitted."},
                {"message": "Pull request merged.", "merged": ""true", "merge_method": "merge""},
                {"message": "Topic 'accessibility' added."},
                {"message": "Release created.", "repo_name": ""ui-kit", "tag_name": ""v2.0.0", "title": "Accessibility docs""},
                {"tag_name": "v2.0.0", "body": "Add accessibility documentation.""},
                {"message": "Issue created", "number": 1"},
                {"printed_ts": "2025-08-21T12:00:00Z", "message": "ui-kit accessibility docs published and released as v2.0.0.""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_34",
        "instruction": "You are 'maya-w' and must function only through the specified tools. YOUR OBJECTIVE \u2022 In repository 'acme-webapp', make an issue utilizing the exact title and body literals, apply the exact label literal, insert the exact comment literal, finalize the issue, and confirm the most recent terminal entry is identical to the exact message literal. LITERALS (use verbatim) - repo: acme-webapp - issue title: CI gate: add test matrix - issue body: Add unit + integration test matrix - label to add: ready-for-ci - comment to post: Triage complete: scheduled for CI gate - terminal message: Issue #1 closed in acme-webapp: ready-for-ci triage complete",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "CI gate: add test matrix",
                    "body": "Add unit + integration test matrix"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "label": "ready-for-ci"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "comment": "Triage complete: scheduled for CI gate"
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "state": "closed"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Issue #1 closed in acme-webapp: ready-for-ci triage complete"
                },
            },
            {
                "name": "ListTerminalLastMessage",
                "arguments": {
                {}
                }
            }
        ],
        "outputs": [
                {"message": "Issue created", "number": 1},
                {"message": "Label 'ready-for-ci' added."},
                {"entries": {"printed_ts": "2025-08-21T12:00:00Z", "message": "Issue #1 closed in acme-webapp: ready-for-ci triage complete"}}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_91",
        "instruction": "You are 'security-group' tasked with working in repository 'security-scanner'. Implement an XSS rule modification ensuring that, once completed, the repository state meets ALL acceptance criteria outlined below, utilizing the exact constants provided. View this as a specification of outcomes and literals, NOT a step-by-step process. ACCEPTANCE CRITERIA (final state must reflect all of these): \u2022 A feature branch is created containing a relaxed XSS rule to minimize false positives on template literals. \u2022 Close issue number 5. \u2022 Merge a pull request (number 1 after reset for this repo) into the default branch. \u2022 Ensure a release with the exact tag below is present. \u2022 The closed issue comprises the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: fix-xss-false-positives - Base branch name: main - File path: rules/xss/relaxed-template-rule.yml - File content (exact; SINGLE trailing newline only): id: xss-template-relaxed severity: medium pattern: disallow-unsafe-innerHTML allow_template_literals: true - Commit message: fix(xss): relax rule for template literals to reduce false positives - Issue to label and close: 5 - Label to add: xss - Pre-PR issue comment: Relaxing XSS rule for template literals; PR will close this issue. - PR title: Relax XSS rule to reduce false positives on template literals - PR body: Closes #5 - Pull request review decision: approve - Release tag: v1.3.1-xss-fp - Post-release issue comment: Fixed in 'v1.3.1-xss-fp' (reduced false positives)",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "security-group"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "GetHeadSha",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "main"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "new_branch": "fix-xss-false-positives",
                    "source_branch": "main"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "fix-xss-false-positives",
                    "path": "rules/xss/relaxed-template-rule.yml",
                    "content": "id: xss-template-relaxed\nseverity: medium\npattern: disallow-unsafe-innerHTML\nallow_template_literals: true\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "fix-xss-false-positives",
                    "commit_message": "fix(xss): relax rule for template literals to reduce false positives"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 5,
                    "label": "xss"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 5,
                    "comment": "Relaxing XSS rule for template literals; PR will close this issue."
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Relax XSS rule to reduce false positives on template literals",
                    "body": "Closes #5",
                    "head": "fix-xss-false-positives",
                    "base": "main"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 1
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 5,
                    "state": "closed"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "security-scanner",
                    "tag": "v1.3.1-xss-fp"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 5,
                    "comment": "Fixed in 'v1.3.1-xss-fp' (reduced false positives)"
                }
            }
        ],
        "outputs": [
                {"repo_name": "security-scanner"},
                {\}pr_number": 1, "closed_issue": 5, "release_tag": "v1.3.1-xss-fp""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_01",
        "instruction": "You belong to 'design-team'. Validate that the 'main' branch of 'ui-kit' is safeguarded and verify its current protection status. Document the modification by creating an audit issue titled 'Protect main branch' with body 'Branch protection for main enabled.' and label 'ops', and record the precise terminal entry 'Branch main protection enabled in ui-kit.'",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "design-team"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "main",
                    "protected": true
                },
            },
            {
                "name": "GetBranchProtection",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Protect main branch",
                    "body": "Branch protection for main enabled.",
                    "labels": [
                        {ops}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Branch main protection enabled in ui-kit."
                }
            }
        ],
        "outputs": [
                {"message": "Branch protection enabled.", "repo_name": ""ui-kit", "branch": ""main", "protected": true"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_02",
        "instruction": "You represent 'security-group'. Issue a release in 'security-scanner' with tag 'v0.4.0', title 'Performance release', and body 'Performance optimizations and SARIF format support.' Afterwards, verify the latest release. Register an audit by opening an issue titled 'Release v0.4.0 created' with body 'Release published successfully.' labeled 'release', and enter the exact terminal entry 'security-scanner v0.4.0 released.'",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "security-group"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "security-scanner",
                    "tag": "v0.4.0",
                    "title": "Performance release",
                    "body": "Performance optimizations and SARIF format support."
                },
            },
            {
                "name": "GetLatestRelease",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Release v0.4.0 created",
                    "body": "Release published successfully.",
                    "labels": [
                        {release}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "security-scanner v0.4.0 released."
                }
            }
        ],
        "outputs": [
                {"message": "Release created.", "repo_name": ""security-scanner", "tag_name": ""v0.4.0", "title": "Performance release""},
                {"tag_name": "v0.4.0", "title": "Performance release""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_03",
        "instruction": "You are 'server-main'. Generate an auditable security snapshot for 'payments-service' which should achieve the following: \u2022 establish a new issue labeled 'Security alerts summary' with the body 'Tracking current code scanning findings and severities.' marked 'security'; \u2022 ensure the terminal log includes exactly this entry: {\"message\": ""Alerts retrieved.", "repo_name\": ""payments-service", "alert_count\": 1, \"alert_numbers\": [7], \"severities\": [\"high\"]} and the results must match the current code scanning alert summary data.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "server-main"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "payments-service"
                },
            },
            {
                "name": "ListCodeScanningAlerts",
                "arguments": {
                    "repo_name": "payments-service"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Security alerts summary",
                    "body": "Tracking current code scanning findings and severities.",
                    "labels": [
                        {security}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "{\"message\": ""Alerts retrieved.", "repo_name\": ""payments-service", "alert_count\": 1, \"alert_numbers\": [7], \"severities\": [\"high\"]}"
                }
            }
        ],
        "outputs": [
                {"message": "Alerts retrieved.", "repo_name": ""payments-service", "alert_count": 1, "alert_numbers": [7], "severities": ["high"]"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_05",
        "instruction": "You are 'infra-lead'. Within the 'k8s-monitoring' repository, display all code scanning alerts in the terminal. Subsequently, open an issue titled 'Track code scanning alerts' with the description 'Investigating code scanning alerts for identified issue numbers' and labels ['code-scan', 'security', 'infrastructure']. In conclusion, log a terminal message indicating the issue has been created.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "ListCodeScanningAlerts",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "{\"message\": ""Code alerts retrieved.", "repo_name\": ""k8s-monitoring", "alert_count\": 3, \"alert_numbers\": [42, 45, 48], \"severities\": [\"high\", \"medium\", \"low\"]}"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Track code scanning alerts",
                    "body": "Investigating code scanning alerts for identified issue numbers",
                    "labels": [
                        {code-scan},
                        {security},
                        {infrastructure}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Issue #1 created to track code scanning alerts in k8s-monitoring."
                }
            }
        ],
        "outputs": [
                {'message': '{'message': 'Code alerts retrieved.', 'repo_name': 'k8s-monitoring', 'alert_count': 3, 'alert_numbers': [42, 45, 48], 'severities': ['high', 'medium', 'low']}},
                {Issue #1 created to track code scanning alerts in k8s-monitoring.}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_06",
        "instruction": "As 'infra-lead', oversee the review of all merged pull requests across these repositories: 'acme-webapp', 'utils-js', 'nlp-models', 'security-scanner', 'flutter-finance-app', 'react-dashboard', and 'k8s-monitoring'. For every merged PR, compile the list of modified files and log a terminal audit entry as follows: 'Merged PR #{number} in {repo_name}: {comma-separated list of files}'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "ListPullRequests",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "ListPullRequests",
                "arguments": {
                    "repo_name": "utils-js"
                },
            },
            {
                "name": "ListPullRequests",
                "arguments": {
                    "repo_name": "nlp-models"
                },
            },
            {
                "name": "ListPullRequests",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "ListPullRequests",
                "arguments": {
                    "repo_name": "flutter-finance-app"
                },
            },
            {
                "name": "ListPullRequests",
                "arguments": {
                    "repo_name": "react-dashboard"
                },
            },
            {
                "name": "ListPullRequests",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Merged PR #7 in acme-webapp: src/logger.py"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Merged PR #16 in utils-js: src/utils/format.js, test/format.test.js"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Merged PR #22 in nlp-models: src/evaluation.py, scripts/checkpoint.py"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Merged PR #23 in security-scanner: src/cache.rs, src/scanner.rs, Cargo.toml"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Merged PR #24 in flutter-finance-app: lib/theme/dark_theme.dart, lib/main.dart, pubspec.yaml"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Merged PR #30 in react-dashboard: src/styles/global.css, src/theme/dark.css, src/hooks/useTheme.ts"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Merged PR #32 in k8s-monitoring: kubernetes/alertmanager.yaml, config/alertmanager.yml, docker-compose.yml"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Merged PR #34 in k8s-monitoring: kubernetes/prometheus.yaml, config/prometheus.yml, docs/MONITORING.md"
                }
            }
        ],
        "outputs": [
                {"message": "Merged PR #7 in acme-webapp: src/logger.py"},
                {"message": "Merged PR #16 in utils-js: src/utils/format.js, test/format.test.js"},
                {"message": "Merged PR #22 in nlp-models: src/evaluation.py, scripts/checkpoint.py"},
                {"message": "Merged PR #23 in security-scanner: src/cache.rs, src/scanner.rs, Cargo.toml"},
                {"message": "Merged PR #24 in flutter-finance-app: lib/theme/dark_theme.dart, lib/main.dart, pubspec.yaml"},
                {"message": "Merged PR #30 in react-dashboard: src/styles/global.css, src/theme/dark.css, src/hooks/useTheme.ts"},
                {"message": "Merged PR #32 in k8s-monitoring: kubernetes/alertmanager.yaml, config/alertmanager.yml, docker-compose.yml"},
                {"message": "Merged PR #34 in k8s-monitoring: kubernetes/prometheus.yaml, config/prometheus.yml, docs/MONITORING.md"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_07",
        "instruction": "Taking on the role of 'server-main', gather the entire commit history from the 'payments-service' repository and assess commit authors alongside their frequencies. Include the complete record and specifically check the 'main' branch for branch-level statistics. Document the audit by opening an issue named 'Commit authors frequency audit' with the message 'Collected authors and commit counts from full history and main branch.' and the label 'audit', then enter the terminal note 'Authors frequency audit for payments-service completed'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "server-main"
                },
            },
            {
                "name": "SearchRepositories",
                "arguments": {
                    "owner": "server-main"
                },
            },
            {
                "name": "ListCommits",
                "arguments": {
                    "repo_name": "payments-service"
                },
            },
            {
                "name": "ListCommits",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Commit authors frequency audit",
                    "body": "Collected authors and commit counts from full history and main branch.",
                    "labels": [
                        {audit}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Authors frequency audit for payments-service completed"
                }
            }
        ],
        "outputs": [
                {"message": "Authors frequency audit for payments-service completed"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_09",
        "instruction": "You are 'intern-emma'. Within 'portfolio-site', initiate a task for an accessibility audit following the last update. Confirm repository contents, and then open an issue titled 'Accessibility audit (WCAG)' with the label 'a11y', including the body 'Run Lighthouse + manual checks for keyboard navigation and color contrast.' Add to terminal: 'portfolio-site accessibility audit opened'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "intern-emma"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "portfolio-site"
                },
            },
            {
                "name": "ListFiles",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "title": "Accessibility audit (WCAG)",
                    "body": "Run Lighthouse + manual checks for keyboard navigation and color contrast.",
                    "labels": [
                        {a11y}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "portfolio-site accessibility audit opened"
                }
            }
        ],
        "outputs": [
                {"message": "portfolio-site accessibility audit opened"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_10",
        "instruction": "You are 'maya-w'. In 'acme-webapp', enumerate current alerts and branches, examine 'feature-update' files, and initiate an issue named 'Post-merge security sweep' with labels ['security','audit'] along with the body: 'Review SQLi alert and ensure tests and sanitization on main.' Add to terminal: 'acme-webapp post-merge security sweep initiated'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "ListCodeScanningAlerts",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "ListBranches",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "ListFiles",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature-update"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Post-merge security sweep",
                    "body": "Review SQLi alert and ensure tests and sanitization on main.",
                    "labels": [
                        {security},
                        {audit}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "acme-webapp post-merge security sweep initiated"
                }
            }
        ],
        "outputs": [
                {"message": "acme-webapp post-merge security sweep initiated"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_11",
        "instruction": "Act as 'infra-lead'. In the context of 'k8s-monitoring', verify merged PRs #32 and #34, subsequently outline the commits on 'feature-alertmanager', and place a terminal note stating that upgrade and alerting configuration are verified jointly.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 32
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 34
                },
            },
            {
                "name": "ListCommits",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "feature-alertmanager"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "k8s-monitoring merged PRs verified: alertmanager + prometheus upgrade"
                }
            }
        ],
        "outputs": [
                {"message": "k8s-monitoring merged PRs verified: alertmanager + prometheus upgrade"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_12",
        "instruction": "Function as 'ui-developer'. Within 'react-dashboard', enumerate open PRs, examine the conflicted PR #28, and add a comment to Issue #25 with this message: 'Plan: add useEffect cleanup + ws close on unmount; verify heap snapshots.' Add to terminal: 'react-dashboard memory leak investigation planned'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ui-developer"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "react-dashboard"
                },
            },
            {
                "name": "ListOpenPullRequests",
                "arguments": {
                    "repo_name": "react-dashboard"
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 28
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 25,
                    "comment": "Plan: add useEffect cleanup + ws close on unmount; verify heap snapshots."
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "react-dashboard memory leak investigation planned"
                }
            }
        ],
        "outputs": [
                {"message": "react-dashboard memory leak investigation planned"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_13",
        "instruction": "You are 'maya-w' managing the repository 'acme-webapp'. Verify that the repository's final state meets ALL acceptance criteria listed below, utilizing the precise literals given. Approach this as outcomes/specification, not detailed guidance. ACCEPTANCE CRITERIA (all must be met in the end): \u2022 Issue #3 has the label: triage-urgent \u2022 Issue #3 state is exactly: closed \u2022 Issue #3 contains the exact new comment: Labels applied: triage-urgent, quality. LITERALS TO USE VERBATIM: - repo: acme-webapp - issue number: 3 - label: triage-urgent - comment: Labels applied: triage-urgent, quality. - closed state literal: closed",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 3,
                    "label": "triage-urgent"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 3,
                    "comment": "Labels applied: triage-urgent, quality."
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 3,
                    "state": "closed"
                }
            }
        ],
        "outputs": [
                {"message": "Label 'triage-urgent' added."},
                {"message": "Comment added."},
                {"message": \Issue updated", "number": 3, "state": "closed""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_14",
        "instruction": "You are 'ryan-dev' overseeing the repository 'utils-js'. Confirm that the final state satisfies ALL acceptance criteria outlined below, approaching this as a specification (not detailed instructions). ACCEPTANCE CRITERIA: \u2022 Issue #4 has the label: needs-triage \u2022 Issue #4 contains the exact new comment: Triaged and scheduled for next minor. \u2022 Issue #4 state is exactly: closed LITERALS TO USE VERBATIM: - repo: utils-js - issue number: 4 - label: needs-triage - comment: Triaged and scheduled for next minor. - closed state literal: closed",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ryan-dev"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "utils-js"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 4,
                    "label": "needs-triage"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 4,
                    "comment": "Triaged and scheduled for next minor."
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 4,
                    "state": "closed"
                }
            }
        ],
        "outputs": [
                {"message": "Label 'needs-triage' added."},
                {"message": "Comment added."},
                {"message": \Issue updated", "number": 4, "state": "closed""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_15",
        "instruction": "As 'ui-developer', you are working in repository 'react-dashboard'. Ensure that the final outcome fulfills ALL acceptance criteria below, treating this as a specification rather than step-by-step guidance. ACCEPTANCE CRITERIA: \u2022 Issue #25 must have the label: investigate \u2022 Issue #25 should include the precise new comment: Triaged; assigning to next sprint. \u2022 Issue #25 should be exactly in the state: closed LITERALS TO USE VERBATIM: - repo: react-dashboard - issue number: 25 - label: investigate - comment: Triaged; assigning to next sprint. - closed state literal: closed",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ui-developer"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "react-dashboard"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 25,
                    "label": "investigate"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 25,
                    "comment": "Triaged; assigning to next sprint."
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 25,
                    "state": "closed"
                }
            }
        ],
        "outputs": [
                {"message": "Label 'investigate' added."},
                {"message": "Comment added."},
                {"message": \Issue updated", "number": 25, "state": "closed""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_16",
        "instruction": "As a member of 'language-ai', ensure that while working in the repository 'nlp-models', the end state complies with ALL acceptance criteria listed below, using this as a specification instead of step-by-step guidance. ACCEPTANCE CRITERIA: \u2022 Issue #12 should bear the label: investigate-oom \u2022 Issue #12 is required to contain the exact new comment: Initial triage: OOM under training; mitigation underway. \u2022 Issue #12 needs to be in the state exactly as: closed LITERALS TO USE VERBATIM: - repo: nlp-models - issue number: 12 - label: investigate-oom - comment: Initial triage: OOM under training; mitigation underway. - closed state literal: closed",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "language-ai"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "nlp-models"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "label": "investigate-oom"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "comment": "Initial triage: OOM under training; mitigation underway."
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "state": "closed"
                }
            }
        ],
        "outputs": [
                {"message": "Label 'investigate-oom' added."},
                {"message": "Comment added."},
                {"message": \Issue updated", "number": 12, "state": "closed""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_17",
        "instruction": "You are 'maya-w' and need to utilize only the available tools. YOUR GOAL \u2022 In the 'acme-webapp' repository, confirm the repository topics contain the precise topic literal below. \u2022 Confirm the latest terminal entry matches the message literal below exactly (branch name included). LITERALS (use verbatim) - repo: acme-webapp - topic to add: quality-gates - terminal message: Topic updated: quality-gates added to acme-webapp on branch main",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "topic": "quality-gates"
                },
            },
            {
                "name": "ListRepoTopics",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Topic updated: quality-gates added to acme-webapp on branch main"
                },
            },
            {
                "name": "ListTerminalLastMessage",
                "arguments": {
                {}
                }
            }
        ],
        "outputs": [
                {"message": "Topic 'quality-gates' added."},
                {"entries": {\printed_ts": ""2025-08-21T12:00:00Z", "message": "Topic updated: quality-gates added to acme-webapp on branch main"}"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_18",
        "instruction": "You are 'maya-w' and need to use only the available tools. YOUR GOAL \u2022 Change the name of the 'acme-webapp' repository to match the exact new name literal. \u2022 Adjust the renamed repository's visibility to the exact value literal. \u2022 Incorporate the exact topic literal into the renamed repository and confirm the topics. \u2022 Verify that the renamed repository is included in your list of owned repositories. \u2022 Ensure the most recent terminal entry corresponds exactly to the message literal. LITERALS (use verbatim) - old repo name: acme-webapp - new repo name: acme-webapp-qa - visibility: private - topic to add: qa-ready - terminal message: Repository acme-webapp renamed to acme-webapp-qa and set private; topic qa-ready added",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "RenameRepository",
                "arguments": {
                    "old_name": "acme-webapp",
                    "new_name": "acme-webapp-qa"
                },
            },
            {
                "name": "SetRepositoryVisibility",
                "arguments": {
                    "repo_name": "acme-webapp-qa",
                    "visibility": "private"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "acme-webapp-qa",
                    "topic": "qa-ready"
                },
            },
            {
                "name": "ListRepoTopics",
                "arguments": {
                    "repo_name": "acme-webapp-qa"
                },
            },
            {
                "name": "ListRepositories",
                "arguments": {
                {}
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Repository acme-webapp renamed to acme-webapp-qa and set private; topic qa-ready added"
                },
            },
            {
                "name": "ListTerminalLastMessage",
                "arguments": {
                {}
                }
            }
        ],
        "outputs": [
                {"message": "Repository renamed", "new_name": "acme-webapp-qa""},
                {"message": "Visibility updated", "repo_name": ""acme-webapp-qa", "visibility": "private""},
                {"message": "Topic 'qa-ready' added."},
                {"entries": {\printed_ts": ""2025-08-21T12:00:00Z", "message": "Repository acme-webapp renamed to acme-webapp-qa and set private; topic qa-ready added"}"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_19",
        "instruction": "You are 'maya-w' and you should operate solely through the available tools. PERFORM THESE ACTIONS \u2022 Apply branch protection to the default branch of the repository 'acme-webapp' using the precise rule literal. \u2022 Confirm that protection is active for that branch. \u2022 Add the specified terminal message literal and make certain it is the most recent entry. LITERALS (use verbatim) - repo: acme-webapp - branch literal: main - protected flag: 'true' - rules object: {\"require_code_owner_reviews\": True} - terminal message: Branch protection enabled on acme-webapp main",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "require_code_owner_reviews": true
                    }
                },
            },
            {
                "name": "GetBranchProtection",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "main"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Branch protection enabled on acme-webapp main"
                },
            },
            {
                "name": "ListTerminalLastMessage",
                "arguments": {
                {}
                }
            }
        ],
        "outputs": [
                {"message": "Branch protection enabled."},
                {"timestamp": "2025-08-21T12:00:00Z", "message": "Branch protection enabled on acme-webapp main""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_21",
        "instruction": "You are 'design-team'. Review the open PRs in 'ui-kit', provide two comments on PR #11 with feedback 'Looks great overall!' and 'Can we optimize the load time?', retrieve details of PR #12, label issue #6 as 'reviewed', and log your review in the terminal.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "design-team"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "ListOpenPullRequests",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "CommentOnPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 11,
                    "comment": "Looks great overall!"
                },
            },
            {
                "name": "CommentOnPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 11,
                    "comment": "Can we optimize the load time?"
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 12
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 6,
                    "label": "reviewed"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "PR #11 reviewed and issue #6 labeled as reviewed."
                }
            }
        ],
        "outputs": [
                {"message": "PR #11 reviewed and issue #6 labeled as reviewed."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_22",
        "instruction": "As 'infra-lead', evaluate merged pull requests in 'k8s-monitoring'. For each PR that has been merged, provide the list of altered files and the commit authors. PR #32 was integrated from the branch 'feature-alertmanager', and PR #34 from 'upgrade-prometheus'. In case any PR alters files within the 'config/' folder, create an issue titled 'Audit config changes' with the content 'Merged PRs modified files under config/ directory. Review needed.' Then add to the terminal log exactly: Audit results: PR #32 files: ['kubernetes/alertmanager.yaml', 'config/alertmanager.yml', 'docker-compose.yml'], authors: ['infra-lead'] PR #34 files: ['kubernetes/prometheus.yaml', 'config/prometheus.yml', 'docs/MONITORING.md'], authors: ['infra-lead']",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "ListPullRequests",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "ListPullRequestFiles",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 32
                },
            },
            {
                "name": "ListCommits",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "feature-alertmanager"
                },
            },
            {
                "name": "ListPullRequestFiles",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 34
                },
            },
            {
                "name": "ListCommits",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "upgrade-prometheus"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Audit config changes",
                    "body": "Merged PRs modified files under config/ directory. Review needed."
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Audit results:\nPR #32 files: ['kubernetes/alertmanager.yaml', 'config/alertmanager.yml', 'docker-compose.yml'], authors: ['infra-lead']\nPR #34 files: ['kubernetes/prometheus.yaml', 'config/prometheus.yml', 'docs/MONITORING.md'], authors: ['infra-lead']"
                }
            }
        ],
        "outputs": [
                {{'32': {'files': ['kubernetes/alertmanager.yaml', 'config/alertmanager.yml', 'docker-compose.yml'], 'authors': ['infra-lead']}, '34': {'files': ['kubernetes/prometheus.yaml', 'config/prometheus.yml', 'docs/MONITORING.md'], 'authors': ['infra-lead']}}}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_24",
        "instruction": "As 'design-team', check that Alert #4 dismissal in 'ui-kit' is consistent with the latest commits on 'feature-theme'. Examine branch commits and the current alerts, inspect Issue #6, and add a PR review comment on PR #11 mentioning the security status. Append terminal: 'ui-kit XSS dismissal validated against feature-theme commits'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "design-team"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "ListCommits",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature-theme"
                },
            },
            {
                "name": "ListCodeScanningAlerts",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "GetIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 6
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 11
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 11,
                    "review_decision": "comment",
                    "comment": "ui-kit XSS dismissal validated against feature-theme commits"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "ui-kit XSS dismissal validated against feature-theme commits"
                }
            }
        ],
        "outputs": [
                {"message": "ui-kit XSS dismissal validated against feature-theme commits"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_25",
        "instruction": "You are 'security-group'. For 'security-scanner', confirm the resolution of Issue #11 through PR #23 and examine the commits on 'perf-optimizations'. Develop a release called 'v0.3.1 Performance optimization' containing the text: 'Implements file system cache; closes #11; ~70% performance gain.'. Append terminal: 'security-scanner perf fix validated and released'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "security-group"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "GetIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 11
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 23
                },
            },
            {
                "name": "ListCommits",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "perf-optimizations"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "security-scanner",
                    "tag": "v0.3.1",
                    "name": "v0.3.1 Performance optimization",
                    "body": "Implements file system cache; closes #11; ~70% performance gain."
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "security-scanner perf fix validated and released"
                }
            }
        ],
        "outputs": [
                {"message": "security-scanner perf fix validated and released"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_26",
        "instruction": "You are 'language-ai'. Within 'nlp-models', ensure that PR #22 was merged for Issue #16 and examine Issue #12 concerning memory. Enumerate commits on the 'exp-transformer' branch to establish investigation context. Subsequently, comment on Issue #12 with: 'Reviewed gradient accumulation commits on exp-transformer for memory tuning direction.' Append terminal: 'nlp-models checkpoint fix verified; memory follow-up noted'",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "language-ai"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "nlp-models"
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 22
                },
            },
            {
                "name": "GetIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 16
                },
            },
            {
                "name": "GetIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12
                },
            },
            {
                "name": "ListCommits",
                "arguments": {
                    "repo_name": "nlp-models",
                    "branch": "exp-transformer"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "comment": "Reviewed gradient accumulation commits on exp-transformer for memory tuning direction."
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "nlp-models checkpoint fix verified; memory follow-up noted"
                }
            }
        ],
        "outputs": [
                {"message": "nlp-models checkpoint fix verified; memory follow-up noted"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_27",
        "instruction": "Assume the role of 'ui-developer'. For 'react-dashboard', ensure that PR #30 successfully closed Issue #27. Compile a list of open PRs and request changes on PR #28 by commenting: 'Resolve merge conflicts before merge.' Add the label 'investigate' to Issue #25. Append terminal: 'react-dashboard dark mode verified; realtime PR gated'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ui-developer"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "react-dashboard"
                },
            },
            {
                "name": "GetIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 27
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 30
                },
            },
            {
                "name": "ListOpenPullRequests",
                "arguments": {
                    "repo_name": "react-dashboard"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 28,
                    "review_decision": "request_changes",
                    "body": "Resolve merge conflicts before merge."
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 25,
                    "label": "investigate"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "react-dashboard dark mode verified; realtime PR gated"
                }
            }
        ],
        "outputs": [
                {"message": "react-dashboard dark mode verified; realtime PR gated"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_29",
        "instruction": "Serve as 'platform-team'. In the 'infra-terraform' project, review files on the 'feat-alb' branch, refer to Issue #9, and initiate a pull request from 'feat-alb' to 'main' titled 'Increase ALB health check timeout' with the body 'Addresses #9 by increasing target health check thresholds.' Subsequently, comment on Issue #9 saying: 'Opened PR to adjust ALB health check timing and config.' Append terminal: 'infra-terraform PR opened to address ALB health checks'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "platform-team"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "infra-terraform"
                },
            },
            {
                "name": "ListFiles",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "feat-alb"
                },
            },
            {
                "name": "GetIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 9
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "head": "feat-alb",
                    "base": "main",
                    "title": "Increase ALB health check timeout",
                    "body": "Addresses #9 by increasing target health check thresholds."
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 9,
                    "comment": "Opened PR to adjust ALB health check timing and config."
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "infra-terraform PR opened to address ALB health checks"
                }
            }
        ],
        "outputs": [
                {"message": "infra-terraform PR opened to address ALB health checks"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_30",
        "instruction": "You are 'ml-engineer'. Within 'ml-pipeline', identify the commits in 'feature-mlflow-tracking' and examine the file content there. Update Issue #31 by adding the comment: 'Next step is drift detection.' Conclude terminal with: 'ml-pipeline MLflow integration reviewed; validation roadmap updated'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ml-engineer"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "ml-pipeline"
                },
            },
            {
                "name": "ListCommits",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "branch": "feature-mlflow-tracking"
                },
            },
            {
                "name": "ListFiles",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "branch": "feature-mlflow-tracking"
                },
            },
            {
                "name": "GetFileContents",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "branch": "feature-mlflow-tracking",
                    "path": "config/model_config.yaml"
                },
            },
            {
                "name": "GetIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "issue_number": 31
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "issue_number": 31,
                    "comment": "Next step is drift detection."
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "ml-pipeline MLflow integration reviewed; validation roadmap updated"
                }
            }
        ],
        "outputs": [
                {"message": "ml-pipeline MLflow integration reviewed; validation roadmap updated"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_31",
        "instruction": "You are 'security-group'. Within 'security-scanner', evaluate open PR #25 for SARIF output and enumerate the current alerts. Comment on the PR stating: 'Confirm SARIF schema v2.1.0 and CI upload step.' Then initiate an issue entitled 'SARIF config polish' with the label 'enhancement' and content: 'Tighten schema validation and CI upload parameters.' Finalize terminal with: 'security-scanner SARIF review and config follow-up created'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "security-group"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 25
                },
            },
            {
                "name": "ListCodeScanningAlerts",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "CommentOnPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 25,
                    "comment": "Confirm SARIF schema v2.1.0 and CI upload step."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "SARIF config polish",
                    "body": "Tighten schema validation and CI upload parameters.",
                    "labels": [
                        {enhancement}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "security-scanner SARIF review and config follow-up created"
                }
            }
        ],
        "outputs": [
                {"message": "security-scanner SARIF review and config follow-up created"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_33",
        "instruction": "You are 'maya-w' and must function using only the provided tools. YOUR OBJECTIVE \u2022 In the 'acme-webapp' repository, formulate a new branch from the literal source branch indicated, incorporate a release-notes file with the exact literal content, perform a commit with the exact literal message, and authenticate the file's presence on the newly created branch. \u2022 Verify the latest terminal entry matches the exact literal message outlined below. LITERALS (use verbatim) - repo: acme-webapp - source branch: main - new branch: feature-banners - file path: docs/release-notes.md - file content: ## Release notes\n- Seed entry\n - commit message: docs: add release notes seed - terminal message: Release notes committed on feature-banners in acme-webapp",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "source_branch": "main",
                    "new_branch": "feature-banners"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature-banners",
                    "path": "docs/release-notes.md",
                    "content": "## Release notes\n- Seed entry\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature-banners",
                    "commit_message": "docs: add release notes seed"
                },
            },
            {
                "name": "ListFiles",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature-banners"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Release notes committed on feature-banners in acme-webapp"
                },
            },
            {
                "name": "ListTerminalLastMessage",
                "arguments": {
                {}
                }
            }
        ],
        "outputs": [
                {"message": "Branch created", "new_branch": "feature-banners""},
                {"message": "Committed to branch", "branch": "feature-banners""},
                {"entries": {\printed_ts": ""2025-08-21T12:00:00Z", "message": "Release notes committed on feature-banners in acme-webapp"}"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_35",
        "instruction": "You are 'ui-developer. You must implement baseline hardening on the default branch of the 'react-dashboard' repository and disseminate that fortified state as a lightweight release. The default branch has to be protected with the attribute set to 'true' and rules precisely as follows: { \"required_reviews\": 1, \"enforce_admins\": true }. Incorporate the repository topic 'security-hardening'. Launch a release with the tag 'task_65-hardened' and body 'Hardening rules applied [task_65]'. Provide the branch protection status and guidelines for the default branch, and include the terminal audit entry: 'Protection enabled and release task_65-hardened published for react-dashboard [task_65]'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ui-developer"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "react-dashboard"
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "required_reviews": 1,
                        "enforce_admins": true
                    }
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "topic": "security-hardening"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "tag": "task_65-hardened",
                    "body": "Hardening rules applied [task_65]"
                },
            },
            {
                "name": "GetBranchProtection",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "main"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Protection enabled and release task_65-hardened published for react-dashboard [task_65]"
                }
            }
        ],
        "outputs": [
                {"protected": "true", "rules": {"required_reviews": 1, "enforce_admins": true}"},
                {"message": "Protection enabled and release task_65-hardened published for react-dashboard [task_65]"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_37",
        "instruction": "You are 'maya-w', tasked with operations in 'acme-webapp'. Illustrate the process of managing a short-term working branch. Create a temporary branch named 'temp-branch' based on the repository's default branch. Use this branch to store a transient note at 'docs/tmp.txt' with the content 'temp work'. Verify that the note remains accessible as long as the branch is active, then retire the branch. When retiring the branch, log the action with the message: 'Branch temp-branch deleted in acme-webapp.'. Finally, list the branches left post-retirement. Return: (a) the file content obtained, (b) the audit message, and (c) the final list of branches.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "source_branch": "main",
                    "new_branch": "temp-branch"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "temp-branch",
                    "path": "docs/tmp.txt",
                    "content": "temp work"
                },
            },
            {
                "name": "GetFileContents",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "temp-branch",
                    "path": "docs/tmp.txt"
                },
            },
            {
                "name": "DeleteBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "temp-branch"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Branch temp-branch deleted in acme-webapp."
                },
            },
            {
                "name": "ListBranches",
                "arguments": {
                    "repo_name": "acme-webapp"
                }
            }
        ],
        "outputs": [
                {'file_content': 'temp work'},
                {'terminal_message': 'Branch temp-branch deleted in acme-webapp.'},
                {'branches': ['main', 'feature-update']}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_41",
        "instruction": "You are 'maya-w'. Within the 'acme-webapp' repository, initiate a new issue titled 'Security audit [task_01]' with the body 'Check SQL injection handling paths. [task_01]'. Ensure the issue has the label 'security-check', contains the comment 'Audit logged. [task_01]', and conclude with the issue state as 'closed'. Provide confirmation that the label was applied, the issue's closure status, and results from a search demonstrating an issue labeled 'security-check' is present. Also, include this final audit message: 'Issue closed with security-check label in acme-webapp [task_01]'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Security audit [task_01]",
                    "body": "Check SQL injection handling paths. [task_01]",
                    "labels": []
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "label": "security-check"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "comment": "Audit logged. [task_01]"
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "state": "closed"
                },
            },
            {
                "name": "SearchIssues",
                "arguments": {
                    "query": "security-check"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Issue closed with security-check label in acme-webapp [task_01]"
                }
            }
        ],
        "outputs": [
                {"message": "Label 'security-check' added."},
                {"state": "closed"},
                {"results": [},
                {"title": "Security audit [task_01]"},
                {"labels": [\security-check"]"},
                {"message": "Issue closed with security-check label in acme-webapp [task_01]"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_42",
        "instruction": "As 'ui-developer', proceed within the 'react-dashboard' repository to create a new issue titled 'Build pipeline audit [task_72]' including the body 'Verify CI stages and artifacts for reproducibility. [task_72]'. Ensure this issue is marked with the label 'ci-audit', contains the exact comment 'Checklist prepared. [task_72]', and concludes in the 'closed' state. Confirm the presence of the label, the issue's final condition, and provide a search result entry verifying an issue with label 'ci-audit' is present. Incorporate this closing audit line: 'Issue closed with ci-audit label in react-dashboard [task_72]'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ui-developer"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "title": "Build pipeline audit [task_72]",
                    "body": "Verify CI stages and artifacts for reproducibility. [task_72]",
                    "labels": []
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 1,
                    "label": "ci-audit"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 1,
                    "comment": "Checklist prepared. [task_72]"
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 1,
                    "state": "closed"
                },
            },
            {
                "name": "SearchIssues",
                "arguments": {
                    "query": "ci-audit"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Issue closed with ci-audit label in react-dashboard [task_72]"
                }
            }
        ],
        "outputs": [
                {"message": "Label 'ci-audit' added."},
                {"state": "closed"},
                {"results": [},
                {"title": "Build pipeline audit [task_72]"},
                {"labels": [\ci-audit"]"},
                {"message": "Issue closed with ci-audit label in react-dashboard [task_72]"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_46",
        "instruction": "You are part of the 'security-group'. Ensure the end state as specified, with precision in all values and case-sensitivity: \u2022 You own a repository called 'security-scanner-pro', its visibility set to 'public' and the default branch named 'main'. \u2022 Repository topics should include both 'security' and 'sarif'. \u2022 A branch named 'feature-sarif' must be established. On this branch, ensure 'src/scanner.py' reads exactly 'print('sarif-v1')' and 'README.md' shows precisely '# security-scanner-pro'. \u2022 The most recent commit on 'feature-sarif' should convey the message 'Add SARIF support scaffolding'. \u2022 Pull request #1 must alternate from head 'feature-sarif' targeting base 'main', titled 'Add SARIF output support' with the body 'Introduce SARIF output skeleton.', enlisted with requested reviewers 'qa-mike' and 'dev-sue', and processed with approval and merge. \u2022 A release for 'security-scanner-pro' should exist bearing tag 'v0.5.0', title 'SARIF support', and body 'Initial SARIF output format release.', with the latest release associated with tag 'v0.5.0'. \u2022 There should be an issue titled 'Post-release verification' articulated with body 'Validate SARIF output end-to-end.' and labeled 'release'. \u2022 Append a terminal log entry reading 'security-scanner-pro v0.5.0 released.' Fulfill all stipulations within a new database run, utilizing only predictable values.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "security-group"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "security-scanner-pro",
                    "visibility": "public",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "security-scanner-pro",
                    "topic": "security"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "security-scanner-pro",
                    "topic": "sarif"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "security-scanner-pro",
                    "source_branch": "main",
                    "new_branch": "feature-sarif"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "security-scanner-pro",
                    "branch": "feature-sarif",
                    "path": "src/scanner.py",
                    "content": "print('sarif-v1')"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "security-scanner-pro",
                    "branch": "feature-sarif",
                    "path": "README.md",
                    "content": "# security-scanner-pro"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "security-scanner-pro",
                    "branch": "feature-sarif",
                    "commit_message": "Add SARIF support scaffolding"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "security-scanner-pro",
                    "title": "Add SARIF output support",
                    "body": "Introduce SARIF output skeleton.",
                    "base": "main",
                    "head": "feature-sarif"
                },
            },
            {
                "name": "RequestPullRequestReviewers",
                "arguments": {
                    "repo_name": "security-scanner-pro",
                    "pr_number": 1,
                    "reviewers": [
                        {qa-mike},
                        {dev-sue}
                    ]
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner-pro",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner-pro",
                    "pr_number": 1
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "security-scanner-pro",
                    "tag": "v0.5.0",
                    "title": "SARIF support",
                    "body": "Initial SARIF output format release."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner-pro",
                    "title": "Post-release verification",
                    "body": "Validate SARIF output end-to-end.",
                    "labels": [
                        {release}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "security-scanner-pro v0.5.0 released."
                },
            },
            {
                "name": "GetLatestRelease",
                "arguments": {
                    "repo_name": "security-scanner-pro"
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "security-scanner-pro""},
                {"message": "Pull request opened", "title": ""Add SARIF output support", "pr_number": 1"},
                {"message": "Reviewers requested.", "requested_reviewers": ["dev-sue", "qa-mike"]"},
                {"message": "Pull request merged.", "merged": "true""},
                {"message": "Release created.", "repo_name": ""security-scanner-pro", "tag_name": "v0.5.0""},
                {"tag_name": "v0.5.0", "title": "SARIF support""},
                {"message": \Issue created", "number": 1"},
                {"message": "security-scanner-pro v0.5.0 released."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_47",
        "instruction": "Assume the role of 'infra-lead'. Fulfill the following final state, ensuring all values are precise and case-sensitive: \u2022 A repository identified as 'k8s-ci-pipelines' is present and owned by you; it's set to 'public' visibility, with 'main' as the default branch. The repository topics must contain 'kubernetes'. \u2022 Ensure a branch named 'feature-alerts' is available. Within this branch, the file 'kubernetes/alerts.yaml' holds exactly 'alertmanager: routes: placeholder-v2', and 'docs/alerts.md' has precisely '# Alerts Runbook'. \u2022 The latest commit on 'feature-alerts' should bear the message 'Add alert routing and runbook'. \u2022 Submit pull request #1 targeting base 'main' from head 'feature-alerts' with title 'Introduce alert routing' and body 'Add Alertmanager routes and docs.', ensuring it is approved and merged. \u2022 Enable branch protection on 'main' with rules exactly {'required_reviews': 1}. \u2022 An issue titled 'Branch protection enabled on main' must be present with body 'Required reviews set to 1.', and it should be tagged 'security'. \u2022 The terminal log should only have one new entry with the message 'k8s-ci-pipelines protection enabled on main.' All these criteria must be met in a clear database scenario; apply only deterministic values.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "k8s-ci-pipelines",
                    "visibility": "public",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "k8s-ci-pipelines",
                    "topic": "kubernetes"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "k8s-ci-pipelines",
                    "source_branch": "main",
                    "new_branch": "feature-alerts"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "k8s-ci-pipelines",
                    "branch": "feature-alerts",
                    "path": "kubernetes/alerts.yaml",
                    "content": "alertmanager: routes: placeholder-v2"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "k8s-ci-pipelines",
                    "branch": "feature-alerts",
                    "path": "docs/alerts.md",
                    "content": "# Alerts Runbook"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "k8s-ci-pipelines",
                    "branch": "feature-alerts",
                    "commit_message": "Add alert routing and runbook"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "k8s-ci-pipelines",
                    "title": "Introduce alert routing",
                    "body": "Add Alertmanager routes and docs.",
                    "base": "main",
                    "head": "feature-alerts"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "k8s-ci-pipelines",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "k8s-ci-pipelines",
                    "pr_number": 1
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "k8s-ci-pipelines",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "required_reviews": 1
                    }
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "k8s-ci-pipelines",
                    "title": "Branch protection enabled on main",
                    "body": "Required reviews set to 1.",
                    "labels": [
                        {security}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "k8s-ci-pipelines protection enabled on main."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "k8s-ci-pipelines""},
                {"message": "Pull request opened", "title": ""Introduce alert routing", "pr_number": 1"},
                {"message": "Pull request merged.", "merged": "true""},
                {"message": "Branch protection enabled."},
                {"message": \Issue created", "number": 1"},
                {"message": "k8s-ci-pipelines protection enabled on main."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_48",
        "instruction": "Take on the responsibility of 'ui-developer'. Achieve the following end result, ensuring all data is exact and case-sensitive: \u2022 A repository known as 'react-dashboard-pro' should be available and managed by you; its visibility set to 'public', with 'main' as the default branch. The repository topics are to include 'frontend' and 'react'. \u2022 Confirm the existence of a branch 'feature-dark-mode'. On this branch, 'src/theme/dark.js' must contain exactly 'export const theme = 'dark';', while 'docs/dark-mode.md' should precisely be '# Dark mode user guide'. \u2022 The most recent commit on 'feature-dark-mode' must carry the message 'Implement dark mode theme'. \u2022 Establish pull request #1 directing base 'main' from head 'feature-dark-mode' with title 'Add dark mode theme' and body 'Introduce dark mode option for dashboard.', having 'qa-mike' and 'design-team' as requested reviewers, ensuring its approval and merging. \u2022 Verify the presence of a release on 'react-dashboard-pro' with tag 'v2.0.0', title 'Dark mode release', and body 'Dark mode theme is now available.'. The latest release must point to tag 'v2.0.0'. \u2022 There must be an issue titled 'Dark mode documentation' with body 'Add instructions for enabling dark mode in user guide.' carrying the label 'docs'. \u2022 Implement branch protection on 'main' with precise rules {'required_reviews': 2}. \u2022 The terminal log should feature only one appended entry bearing the message 'react-dashboard-pro v2.0.0 released with dark mode.' All specifications must be fulfilled in a new database run; utilize only certain values.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ui-developer"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "react-dashboard-pro",
                    "visibility": "public",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "react-dashboard-pro",
                    "topic": "frontend"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "react-dashboard-pro",
                    "topic": "react"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "react-dashboard-pro",
                    "source_branch": "main",
                    "new_branch": "feature-dark-mode"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "react-dashboard-pro",
                    "branch": "feature-dark-mode",
                    "path": "src/theme/dark.js",
                    "content": "export const theme = 'dark';"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "react-dashboard-pro",
                    "branch": "feature-dark-mode",
                    "path": "docs/dark-mode.md",
                    "content": "# Dark mode user guide"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "react-dashboard-pro",
                    "branch": "feature-dark-mode",
                    "commit_message": "Implement dark mode theme"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "react-dashboard-pro",
                    "title": "Add dark mode theme",
                    "body": "Introduce dark mode option for dashboard.",
                    "base": "main",
                    "head": "feature-dark-mode"
                },
            },
            {
                "name": "RequestPullRequestReviewers",
                "arguments": {
                    "repo_name": "react-dashboard-pro",
                    "pr_number": 1,
                    "reviewers": [
                        {qa-mike},
                        {design-team}
                    ]
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "react-dashboard-pro",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "react-dashboard-pro",
                    "pr_number": 1
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "react-dashboard-pro",
                    "tag": "v2.0.0",
                    "title": "Dark mode release",
                    "body": "Dark mode theme is now available."
                },
            },
            {
                "name": "GetLatestRelease",
                "arguments": {
                    "repo_name": "react-dashboard-pro"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "react-dashboard-pro",
                    "title": "Dark mode documentation",
                    "body": "Add instructions for enabling dark mode in user guide.",
                    "labels": [
                        {docs}
                    ]
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "react-dashboard-pro",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "required_reviews": 2
                    }
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "react-dashboard-pro v2.0.0 released with dark mode."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "react-dashboard-pro""},
                {"message": "Pull request opened", "title": ""Add dark mode theme", "pr_number": 1"},
                {"message": "Reviewers requested.", "requested_reviewers": ["qa-mike", "design-team"]"},
                {"message": "Pull request merged.", "merged": "true""},
                {"message": "Release created.", "repo_name": ""react-dashboard-pro", "tag_name": "v2.0.0""},
                {"tag_name": "v2.0.0", "title": "Dark mode release""},
                {"message": \Issue created", "number": 1"},
                {"message": "Branch protection enabled."},
                {"message": "react-dashboard-pro v2.0.0 released with dark mode."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_49",
        "instruction": "Your team name is 'platform-team'. Ensure the following final state, maintaining all values precisely and case-sensitive: \u2022 A repository called 'infra-containers' must be present and owned by your team; its visibility should be 'public' and its default branch 'main'. The repository should have 'docker' as one of its topics. \u2022 A branch termed 'feature-registry' should be present. Within that branch, ensure the file 'docker-compose.yml' includes exactly 'services: placeholder-v1' and 'docs/registry.md' contains precisely '# Private registry setup'. \u2022 The latest commit on 'feature-registry' should have the message 'Add registry compose and docs'. \u2022 Pull request #1 should target base 'main' from head 'feature-registry' with the title 'Add container registry' and body 'Introduce docker-compose for registry and docs.', must be approved, and merged. \u2022 A release labeled 'v0.3.0', with the title 'Registry compose' and body 'Adds docker-compose and docs.' should exist on 'infra-containers'. \u2022 An issue labeled 'ops' titled 'Track registry rollout' must exist with the body 'Coordinate rollout with ops.'. \u2022 Branch protection on branch 'main' must be enabled with rules exactly {'required_reviews': 1}. \u2022 The terminal log should have precisely one appended entry with the message 'infra-containers v0.3.0 released.' All conditions must be met in a new database run; only utilize deterministic values.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "platform-team"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "infra-containers",
                    "visibility": "public",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "infra-containers",
                    "topic": "docker"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "infra-containers",
                    "source_branch": "main",
                    "new_branch": "feature-registry"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "infra-containers",
                    "branch": "feature-registry",
                    "path": "docker-compose.yml",
                    "content": "services: placeholder-v1"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "infra-containers",
                    "branch": "feature-registry",
                    "path": "docs/registry.md",
                    "content": "# Private registry setup"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "infra-containers",
                    "branch": "feature-registry",
                    "commit_message": "Add registry compose and docs"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "infra-containers",
                    "title": "Add container registry",
                    "body": "Introduce docker-compose for registry and docs.",
                    "base": "main",
                    "head": "feature-registry"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "infra-containers",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "infra-containers",
                    "pr_number": 1
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "infra-containers",
                    "tag": "v0.3.0",
                    "title": "Registry compose",
                    "body": "Adds docker-compose and docs."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "infra-containers",
                    "title": "Track registry rollout",
                    "body": "Coordinate rollout with ops.",
                    "labels": [
                        {ops}
                    ]
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "infra-containers",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "required_reviews": 1
                    }
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "infra-containers v0.3.0 released."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "infra-containers""},
                {"message": "Pull request opened", "title": ""Add container registry", "pr_number": 1"},
                {"message": "Pull request merged.", "merged": "true""},
                {"message": "Release created.", "repo_name": ""infra-containers", "tag_name": "v0.3.0""},
                {"message": \Issue created", "number": 1"},
                {"message": "Branch protection enabled."},
                {"message": "infra-containers v0.3.0 released."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_50",
        "instruction": "Your team is 'server-main'. Achieve the following final state, ensuring all values are precise and case-sensitive: \u2022 A repository titled 'backend-payment-service' needs to exist, owned by you; its visibility set to 'public' with 'main' as the default branch. The repository should have the topics 'payments' and 'backend'. \u2022 A branch named 'feature-payment-webhooks' must exist. Within this branch, 'src/webhooks.py' should contain exactly 'print('webhooks-v1')' and 'docs/webhooks.md' should have exactly '# Webhooks guide'. \u2022 The latest commit on 'feature-payment-webhooks' should feature the message 'Implement payment webhooks'. \u2022 Pull request #1 should target the 'main' base from the 'feature-payment-webhooks' head with the title 'Add payment webhooks' and body 'Introduce webhook handlers and docs.', with reviewers 'qa-erin' and 'payments-lead', approved and merged. \u2022 Enable branch protection on 'main' with rules exactly {'required_reviews': 2}. \u2022 A release labeled 'v1.3.0', titled 'Payment webhooks' and with the body 'Initial webhook support.' should be available, with the latest release pointing to tag 'v1.3.0'. \u2022 An issue called 'Post-deploy checklist' should exist with the body 'Validate webhook delivery and retries.' tagged 'release'. \u2022 The terminal log must include exactly one added entry with the message 'backend-payment-service v1.3.0 released.' All conditions need to be fulfilled in a new database run; apply deterministic values exclusively.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "server-main"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "backend-payment-service",
                    "visibility": "public",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "backend-payment-service",
                    "topic": "payments"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "backend-payment-service",
                    "topic": "backend"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "backend-payment-service",
                    "source_branch": "main",
                    "new_branch": "feature-payment-webhooks"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "backend-payment-service",
                    "branch": "feature-payment-webhooks",
                    "path": "src/webhooks.py",
                    "content": "print('webhooks-v1')"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "backend-payment-service",
                    "branch": "feature-payment-webhooks",
                    "path": "docs/webhooks.md",
                    "content": "# Webhooks guide"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "backend-payment-service",
                    "branch": "feature-payment-webhooks",
                    "commit_message": "Implement payment webhooks"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "backend-payment-service",
                    "title": "Add payment webhooks",
                    "body": "Introduce webhook handlers and docs.",
                    "base": "main",
                    "head": "feature-payment-webhooks"
                },
            },
            {
                "name": "RequestPullRequestReviewers",
                "arguments": {
                    "repo_name": "backend-payment-service",
                    "pr_number": 1,
                    "reviewers": [
                        {qa-erin},
                        {payments-lead}
                    ]
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "backend-payment-service",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "backend-payment-service",
                    "pr_number": 1
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "backend-payment-service",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "required_reviews": 2
                    }
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "backend-payment-service",
                    "tag": "v1.3.0",
                    "title": "Payment webhooks",
                    "body": "Initial webhook support."
                },
            },
            {
                "name": "GetLatestRelease",
                "arguments": {
                    "repo_name": "backend-payment-service"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "backend-payment-service",
                    "title": "Post-deploy checklist",
                    "body": "Validate webhook delivery and retries.",
                    "labels": [
                        {release}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "backend-payment-service v1.3.0 released."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "backend-payment-service""},
                {"message": "Pull request opened", "title": ""Add payment webhooks", "pr_number": 1"},
                {"message": "Reviewers requested.", "requested_reviewers": ["payments-lead", "qa-erin"]"},
                {"message": "Pull request merged.", "merged": "true""},
                {"message": "Branch protection enabled."},
                {"message": "Release created.", "repo_name": ""backend-payment-service", "tag_name": "v1.3.0""},
                {"tag_name": "v1.3.0", "title": "Payment webhooks""},
                {"message": \Issue created", "number": 1"},
                {"message": "backend-payment-service v1.3.0 released."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_51",
        "instruction": "Identify yourself as 'maya-w'. Achieve the following end result, ensuring all values are precise and maintain case sensitivity: \u2022 A repository called 'acme-sql-service' is in existence and owned by you; it is set to 'public' visibility and its default branch is 'main'. The repository topics must include 'database'. \u2022 The branch 'feature-sanitize-input' is available. On this branch, the 'src/sanitize.py' file must contain exactly 'def sanitize(v): return str(v)' and the 'docs/security.md' file must exactly include '# SQL sanitization patch'. \u2022 The latest commit on 'feature-sanitize-input' bears the message 'Add input sanitization helper'. \u2022 Pull request #1, which targets base 'main' from head 'feature-sanitize-input', is approved and merged with the title 'Add SQL sanitization' and body 'Introduce helper to sanitize SQL input.'. \u2022 A release is present on 'acme-sql-service' marked with tag 'v0.2.0', titled 'Sanitization patch', and contains the body 'Helper added for SQL sanitization.'. \u2022 An issue with the title 'Review sanitization helper' is open, having the body 'Validate new helper across services.' and labeled as 'security'. \u2022 The terminal log has one specific appended entry with the message 'acme-sql-service v0.2.0 released.' Every requirement must be fulfilled in a new database execution; utilize only deterministic values.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "acme-sql-service",
                    "visibility": "public",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "acme-sql-service",
                    "topic": "database"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "acme-sql-service",
                    "source_branch": "main",
                    "new_branch": "feature-sanitize-input"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-sql-service",
                    "branch": "feature-sanitize-input",
                    "path": "src/sanitize.py",
                    "content": "def sanitize(v): return str(v)"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-sql-service",
                    "branch": "feature-sanitize-input",
                    "path": "docs/security.md",
                    "content": "# SQL sanitization patch"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-sql-service",
                    "branch": "feature-sanitize-input",
                    "commit_message": "Add input sanitization helper"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "acme-sql-service",
                    "title": "Add SQL sanitization",
                    "body": "Introduce helper to sanitize SQL input.",
                    "base": "main",
                    "head": "feature-sanitize-input"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "acme-sql-service",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "acme-sql-service",
                    "pr_number": 1
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "acme-sql-service",
                    "tag": "v0.2.0",
                    "title": "Sanitization patch",
                    "body": "Helper added for SQL sanitization."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-sql-service",
                    "title": "Review sanitization helper",
                    "body": "Validate new helper across services.",
                    "labels": [
                        {security}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "acme-sql-service v0.2.0 released."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "acme-sql-service""},
                {"message": "Pull request opened", "title": ""Add SQL sanitization", "pr_number": 1"},
                {"message": "Pull request merged.", "merged": "true""},
                {"message": "Release created.", "repo_name": ""acme-sql-service", "tag_name": "v0.2.0""},
                {"message": \Issue created", "number": 1"},
                {"message": "acme-sql-service v0.2.0 released."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_52",
        "instruction": "Identify yourself as 'server-main'. Upon task completion, the repository 'payments-service' must meet ALL of the following conditions: \u2022 A documentation file resides at 'docs/TIMEOUT_POLICY.md' containing EXACT text 'Default request timeout is 60s. 3DS flows may extend to 90s. Retries: none.'. \u2022 This update starts from a branch named 'feature-timeout-policy' and is documented by a commit with the message precisely 'Document timeout policy'. \u2022 The modification is incorporated into 'main' via a reviewed pull request titled 'Document timeout policy', with a review request directed to 'qa-erin', and it has been merged. \u2022 A release is available with tag 'v0.2.1', title 'Timeout policy docs', and body 'Publish timeout policy documentation.', with the most recent release showing tag 'v0.2.1'. \u2022 There is an existing issue titled 'Timeout policy docs published' with body 'Docs merged and released as v0.2.1.' bearing the 'documentation' label. \u2022 The terminal audit log must include the EXACT message 'payments-service timeout policy docs published and released as v0.2.1.'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "server-main"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "payments-service"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "source_branch": "main",
                    "new_branch": "feature-timeout-policy"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "feature-timeout-policy",
                    "path": "docs/TIMEOUT_POLICY.md",
                    "content": "Default request timeout is 60s. 3DS flows may extend to 90s. Retries: none."
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "feature-timeout-policy",
                    "commit_message": "Document timeout policy"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Document timeout policy",
                    "base": "main",
                    "head": "feature-timeout-policy"
                },
            },
            {
                "name": "RequestPullRequestReviewers",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 1,
                    "reviewers": [
                        {qa-erin}
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 1
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "payments-service",
                    "tag": "v0.2.1",
                    "title": "Timeout policy docs",
                    "body": "Publish timeout policy documentation."
                },
            },
            {
                "name": "GetLatestRelease",
                "arguments": {
                    "repo_name": "payments-service"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Timeout policy docs published",
                    "body": "Docs merged and released as v0.2.1.",
                    "labels": [
                        {documentation}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "payments-service timeout policy docs published and released as v0.2.1."
                }
            }
        ],
        "outputs": [
                {"message": "Branch created", "new_branch": ""feature-timeout-policy", "from": "main""},
                {"message": "Committed to branch", "repo": ""payments-service", "branch": ""feature-timeout-policy", "commit_sha": "sha_0000000000000000000000000000000000000000""},
                {"message": "Pull request opened", "title": ""Document timeout policy", "base": ""main", "head": ""feature-timeout-policy", "pr_number": 1"},
                {"message": "Reviewers requested.", "pr_number": 1"},
                {"message": "Pull request merged.", "merged": ""true", "merge_method": "merge""},
                {"message": "Release created.", "repo_name": ""payments-service", "tag_name": ""v0.2.1", "title": "Timeout policy docs""},
                {"tag_name": "v0.2.1", "title": "Timeout policy docs""},
                {"message": \Issue created", "number": 1"},
                {"timestamp": "2025-08-21T12:00:00Z", "message": "payments-service timeout policy docs published and released as v0.2.1.""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_53",
        "instruction": "You are 'docs-sophia'. Manage the following final outcome, ensuring all values are precise and maintain case sensitivity: \u2022 A repository under the name 'product-docs' is present and is owned by you; its visibility setting is 'public', and its default branch is named 'main'. The repository should have 'docs' and 'markdown' as topics. \u2022 Implement branch protection on the branch 'main' with strictly these rules {'required_reviews': 1}. \u2022 There is a release on 'product-docs' identified by tag 'v1.0.0', with title 'Initial documentation', and the body 'Bootstrap product documentation.'. \u2022 Create an issue with the title 'Add onboarding guide' having the body 'Create onboarding section in docs.' and tagged 'docs'. \u2022 The terminal log must contain exactly one newly added entry that says 'product-docs v1.0.0 published.' Every condition must be met in a clean database environment; employ deterministic values only.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "docs-sophia"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "product-docs",
                    "visibility": "public",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "product-docs",
                    "topic": "docs"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "product-docs",
                    "topic": "markdown"
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "product-docs",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "required_reviews": 1
                    }
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "product-docs",
                    "tag": "v1.0.0",
                    "title": "Initial documentation",
                    "body": "Bootstrap product documentation."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "product-docs",
                    "title": "Add onboarding guide",
                    "body": "Create onboarding section in docs.",
                    "labels": [
                        {docs}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "product-docs v1.0.0 published."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "product-docs""},
                {"message": "Branch protection enabled."},
                {"message": "Release created.", "repo_name": ""product-docs", "tag_name": "v1.0.0""},
                {"message": \Issue created", "number": 1"},
                {"message": "product-docs v1.0.0 published."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_54",
        "instruction": "You are 'infra-lead'. Verify that 'k8s-monitoring' has published and consolidated documentation regarding the Prometheus retention policy. This documentation should be located at 'docs/RETENTION_POLICY.md' and must contain the exact text 'Prometheus retention is 30 days. Compaction enabled. Storage class: gp3.'. Implement this change on a branch called 'feature-retention-policy', merge it into 'main' through a reviewed pull request titled 'Document Prometheus retention' (request review from 'platform-team'). Utilize the specific commit message 'Document 30-day Prometheus retention'. Confirm completion by creating an issue titled 'Prometheus retention policy documented' with the body 'Retention set to 30 days and documented.' labeled 'documentation', and enter the exact terminal audit note 'k8s-monitoring retention policy docs merged and recorded.'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "source_branch": "main",
                    "new_branch": "feature-retention-policy"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "feature-retention-policy",
                    "path": "docs/RETENTION_POLICY.md",
                    "content": "Prometheus retention is 30 days. Compaction enabled. Storage class: gp3."
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "feature-retention-policy",
                    "commit_message": "Document 30-day Prometheus retention"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Document Prometheus retention",
                    "base": "main",
                    "head": "feature-retention-policy"
                },
            },
            {
                "name": "RequestPullRequestReviewers",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 1,
                    "reviewers": [
                        {platform-team}
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 1
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Prometheus retention policy documented",
                    "body": "Retention set to 30 days and documented.",
                    "labels": [
                        {documentation}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "k8s-monitoring retention policy docs merged and recorded."
                }
            }
        ],
        "outputs": [
                {"message": "Branch created", "new_branch": ""feature-retention-policy", "from": "main""},
                {"message": "Committed to branch", "repo": ""k8s-monitoring", "branch": ""feature-retention-policy", "commit_sha": "sha_0000000000000000000000000000000000000000""},
                {"message": "Pull request opened", "title": ""Document Prometheus retention", "base": ""main", "head": ""feature-retention-policy", "pr_number": 1"},
                {"message": "Reviewers requested.", "pr_number": 1"},
                {"message": "Pull request merged.", "merged": ""true", "merge_method": "merge""},
                {"message": \Issue created", "number": 1"},
                {"timestamp": "2025-08-21T12:00:00Z", "message": "k8s-monitoring retention policy docs merged and recorded.""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_55",
        "instruction": "You are 'qa-mike'. Ensure the following final state, with all specifics precise and case-sensitive: \u2022 A repository named 'qa-tests' is present and owned by you; its visibility must be 'public' and its default branch should be 'main'. The repository topics include 'qa'. \u2022 A release is available on 'qa-tests' with tag 'v0.1.0', title 'Initial QA setup', and body 'Bootstrap test repository.'. \u2022 There is an issue titled 'Write first test cases' with body 'Add login and signup test coverage.' labeled 'qa'. \u2022 The terminal log should have exactly one appended entry with the message 'qa-tests v0.1.0 created.' All criteria must be met during a clean database execution; use deterministic values only.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "qa-mike"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "qa-tests",
                    "visibility": "public",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "qa-tests",
                    "topic": "qa"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "qa-tests",
                    "tag": "v0.1.0",
                    "title": "Initial QA setup",
                    "body": "Bootstrap test repository."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "qa-tests",
                    "title": "Write first test cases",
                    "body": "Add login and signup test coverage.",
                    "labels": [
                        {qa}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "qa-tests v0.1.0 created."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "qa-tests""},
                {"message": "Release created.", "repo_name": ""qa-tests", "tag_name": "v0.1.0""},
                {"message": \Issue created", "number": 1"},
                {"message": "qa-tests v0.1.0 created."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_56",
        "instruction": "You are 'design-team'. Your task is to handle the repository 'ui-kit' and accomplish the tasks detailed as follows: 1) Branch 'main' is safeguarded with rules exactly {\"require_reviews\": true, \"enforce_admins\": true}. 2) The file 'docs/THEME_PROVIDER.md' is present on 'main' with the exact content 'Use ThemeProvider at the app root. Props: theme (required). Example: <ThemeProvider theme={Theme}>'. This modification originates on a branch called 'feature-theme-docs' and is represented by a commit whose message is exactly 'Add ThemeProvider documentation'. The edit is merged into 'main' through a reviewed pull request titled 'ThemeProvider docs'; a review request is made to 'ui-dev', and an approval review with the exact comment 'LGTM' is documented. 3) A release is available with tag 'v1.0.1', title 'Theme docs', and body 'Add ThemeProvider documentation.', and the most recent release shows tag 'v1.0.1'. 4) An issue is titled 'ThemeProvider docs published' with body 'Docs merged and released as v1.0.1.' labeled 'documentation'. 5) The terminal audit includes the exact record 'ui-kit ThemeProvider docs published and released as v1.0.1.'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "design-team"
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "require_reviews": "true",
                        "enforce_admins": "true"
                    }
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "source_branch": "main",
                    "new_branch": "feature-theme-docs"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature-theme-docs",
                    "path": "docs/THEME_PROVIDER.md",
                    "content": "Use ThemeProvider at the app root. Props: theme (required). Example: <ThemeProvider theme={Theme}>"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature-theme-docs",
                    "commit_message": "Add ThemeProvider documentation"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "ThemeProvider docs",
                    "base": "main",
                    "head": "feature-theme-docs"
                },
            },
            {
                "name": "RequestPullRequestReviewers",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 1,
                    "reviewers": [
                        {ui-dev}
                    ]
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 1,
                    "review_decision": "approve",
                    "comment": "LGTM"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 1
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "ui-kit",
                    "tag": "v1.0.1",
                    "title": "Theme docs",
                    "body": "Add ThemeProvider documentation."
                },
            },
            {
                "name": "GetLatestRelease",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "ThemeProvider docs published",
                    "body": "Docs merged and released as v1.0.1.",
                    "labels": [
                        {documentation}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "ui-kit ThemeProvider docs published and released as v1.0.1."
                }
            }
        ],
        "outputs": [
                {"message": "Branch protection enabled.", "repo_name": ""ui-kit", "branch": ""main", "protected": "true""},
                {"message": "Branch created", "new_branch": ""feature-theme-docs", "from": "main""},
                {"message": "Committed to branch", "repo": ""ui-kit", "branch": ""feature-theme-docs", "commit_sha": "sha_0000000000000000000000000000000000000000""},
                {"message": "Pull request opened", "title": ""ThemeProvider docs", "base": ""main", "head": ""feature-theme-docs", "pr_number": 1"},
                {"message": "Reviewers requested.", "pr_number": 1"},
                {"message": "Review submitted."},
                {"message": "Pull request merged.", "merged": ""true", "merge_method": "merge""},
                {"message": "Release created.", "repo_name": ""ui-kit", "tag_name": ""v1.0.1", "title": "Theme docs""},
                {"tag_name": "v1.0.1", "body": "Add ThemeProvider documentation.""},
                {"message": \Issue created", "number": 1"},
                {"printed_ts": "2025-08-21T12:00:00Z", "message": "ui-kit ThemeProvider docs published and released as v1.0.1.""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_57",
        "instruction": "You are 'maintainer-tom'. Coordinate achieving the following end state, with all values precise and case\u2011sensitive: \u2022 A repository named 'tooling-maintenance' must exist and be owned by you; its visibility should be 'public' and its default branch 'main'. \u2022 Ensure a release exists on 'tooling-maintenance' with tag 'v0.1.0', title 'Initial maintenance setup', and body 'Bootstrap maintenance repo.'. \u2022 There should be an issue titled 'Create weekly maintenance checklist' with body 'Define checklist template for weekly runs.' labeled 'maintenance'. \u2022 Confirm the terminal log has exactly one appended entry with the message 'tooling-maintenance v0.1.0 created.' All conditions need to be fulfilled in a fresh database run; apply deterministic values only.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maintainer-tom"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "tooling-maintenance",
                    "visibility": "public",
                    "default_branch": "main"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "tooling-maintenance",
                    "tag": "v0.1.0",
                    "title": "Initial maintenance setup",
                    "body": "Bootstrap maintenance repo."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "tooling-maintenance",
                    "title": "Create weekly maintenance checklist",
                    "body": "Define checklist template for weekly runs.",
                    "labels": [
                        {maintenance}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "tooling-maintenance v0.1.0 created."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "tooling-maintenance""},
                {"message": "Release created.", "repo_name": ""tooling-maintenance", "tag_name": "v0.1.0""},
                {"message": \Issue created", "number": 1"},
                {"message": "tooling-maintenance v0.1.0 created."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_59",
        "instruction": "You are 'tech-lead-tara'. Handle achieving the following end state, with all values precise and case\u2011sensitive: \u2022 A repository named 'automation-ci' must exist and be owned by you; its visibility should be 'public' and its default branch 'main'. The repository topics need to include both 'automation' and 'ci'. \u2022 Ensure the existence of a branch 'feature-ci-config'. On that branch, verify the file '.github/workflows/ci.yml' contains exactly 'name: ci'. \u2022 Confirm the latest commit on 'feature-ci-config' includes the message 'Add CI workflow'. \u2022 Branch protection is activated on branch 'main' with rules precisely {'required_reviews': 1}. \u2022 A release must exist on 'automation-ci' with tag 'v0.1.0', title 'CI bootstrap', and body 'Adds initial CI workflow.'. \u2022 An issue titled 'Expand CI matrix' should exist with body 'Add Python and Node matrix to CI.' labeled 'ci'. \u2022 Verify the terminal log has exactly one appended entry with the message 'automation-ci v0.1.0 released.' All conditions need to be fulfilled in a fresh database run; apply deterministic values only.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "tech-lead-tara"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "automation-ci",
                    "visibility": "public",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "automation-ci",
                    "topic": "automation"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "automation-ci",
                    "topic": "ci"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "automation-ci",
                    "source_branch": "main",
                    "new_branch": "feature-ci-config"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "automation-ci",
                    "branch": "feature-ci-config",
                    "path": ".github/workflows/ci.yml",
                    "content": "name: ci"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "automation-ci",
                    "branch": "feature-ci-config",
                    "commit_message": "Add CI workflow"
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "automation-ci",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "required_reviews": 1
                    }
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "automation-ci",
                    "tag": "v0.1.0",
                    "title": "CI bootstrap",
                    "body": "Adds initial CI workflow."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "automation-ci",
                    "title": "Expand CI matrix",
                    "body": "Add Python and Node matrix to CI.",
                    "labels": [
                        {ci}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "automation-ci v0.1.0 released."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "automation-ci""},
                {"message": "Branch protection enabled."},
                {"message": "Release created.", "repo_name": ""automation-ci", "tag_name": "v0.1.0""},
                {"message": \Issue created", "number": 1"},
                {"message": "automation-ci v0.1.0 released."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_61",
        "instruction": "You are appointed as 'design-lead'. Accomplish the final outcomes, ensuring all values are precise and case-sensitive: \u2022 Initially, create a repository named 'design-system' privately with the default branch as 'main', then change its name to 'design-system-pro' and set its visibility to 'public'. Include 'design' as the repository topic. \u2022 Confirm the existence of a branch called 'feature-guidelines', where the file 'docs/guidelines.md' contains exactly '# Design guidelines' and the file 'tokens/colors.json' has precisely '{'brand':'blue'}'. \u2022 The newest commit on 'feature-guidelines' should be noted with the message 'Add initial guidelines and tokens'. \u2022 Release on 'design-system-pro' should be present, with tag 'v1.0.0', title 'Design system v1', and body text 'Initial guidelines and tokens.'. \u2022 Ensure the creation of an issue titled 'Track design system adoption' with the description 'Roll out across products.' and labeled as 'design'. \u2022 In the terminal log, add exactly one new entry with the content 'design-system-pro v1.0.0 published.' Complete all tasks using a new database run with deterministic specifications only.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "design-lead"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "design-system",
                    "visibility": "private",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "design-system",
                    "topic": "design"
                },
            },
            {
                "name": "RenameRepository",
                "arguments": {
                    "old_name": "design-system",
                    "new_name": "design-system-pro"
                },
            },
            {
                "name": "SetRepositoryVisibility",
                "arguments": {
                    "repo_name": "design-system-pro",
                    "visibility": "public"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "design-system-pro",
                    "source_branch": "main",
                    "new_branch": "feature-guidelines"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "design-system-pro",
                    "branch": "feature-guidelines",
                    "path": "docs/guidelines.md",
                    "content": "# Design guidelines"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "design-system-pro",
                    "branch": "feature-guidelines",
                    "path": "tokens/colors.json",
                    "content": "{'brand':'blue'}"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "design-system-pro",
                    "branch": "feature-guidelines",
                    "commit_message": "Add initial guidelines and tokens"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "design-system-pro",
                    "tag": "v1.0.0",
                    "title": "Design system v1",
                    "body": "Initial guidelines and tokens."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "design-system-pro",
                    "title": "Track design system adoption",
                    "body": "Roll out across products.",
                    "labels": [
                        {design}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "design-system-pro v1.0.0 published."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "design-system""},
                {"message": "Repository renamed", "new_name": "design-system-pro""},
                {"message": "Visibility updated", "repo_name": ""design-system-pro", "visibility": "public""},
                {"message": "Committed to branch", "commit_message": "Add initial guidelines and tokens""},
                {"message": "Release created.", "repo_name": ""design-system-pro", "tag_name": "v1.0.0""},
                {"message": \Issue created", "number": 1"},
                {"message": "design-system-pro v1.0.0 published."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_62",
        "instruction": "You are assigned as 'infra-lead'. Once you conclude the task, verify that the repository state for 'k8s-monitoring' fulfills ALL these criteria: \u2022 Ensure a documentation file located at 'docs/LOGGING.md' with the EXACT content 'Centralized logging with Fluent Bit. Logs shipped to Elasticsearch. Retention: 14 days.'. \u2022 This amendment should begin on a branch titled 'feature-logging-docs', represented by a commit with the precise message 'Add logging documentation'. \u2022 Changes must be integrated into 'main' through a reviewed pull request titled 'Logging docs'; ensure a review request to 'platform-team' and an approval review with the comment 'Approved for observability'. \u2022 Assign the topic 'observability' to the repository. \u2022 There must be a release with tag 'v1.5.0', title 'Logging docs', and body 'Add logging documentation.', and the latest release must show the tag 'v1.5.0'. \u2022 Ensure the presence of an issue titled 'Logging docs published' with content 'Docs merged and released as v1.5.0.' and label it 'documentation'. \u2022 The terminal audit log should have the EXACT entry 'k8s-monitoring logging docs published and released as v1.5.0.'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "source_branch": "main",
                    "new_branch": "feature-logging-docs"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "feature-logging-docs",
                    "path": "docs/LOGGING.md",
                    "content": "Centralized logging with Fluent Bit. Logs shipped to Elasticsearch. Retention: 14 days."
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "feature-logging-docs",
                    "commit_message": "Add logging documentation"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Logging docs",
                    "base": "main",
                    "head": "feature-logging-docs"
                },
            },
            {
                "name": "RequestPullRequestReviewers",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 1,
                    "reviewers": [
                        {platform-team}
                    ]
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 1,
                    "review_decision": "approve",
                    "comment": "Approved for observability"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 1
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "topic": "observability"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "tag": "v1.5.0",
                    "title": "Logging docs",
                    "body": "Add logging documentation."
                },
            },
            {
                "name": "GetLatestRelease",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Logging docs published",
                    "body": "Docs merged and released as v1.5.0.",
                    "labels": [
                        {documentation}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "k8s-monitoring logging docs published and released as v1.5.0."
                }
            }
        ],
        "outputs": [
                {"message": "Branch created", "new_branch": ""feature-logging-docs", "from": "main""},
                {"message": "Committed to branch", "repo": ""k8s-monitoring", "branch": ""feature-logging-docs", "commit_sha": "sha_0000000000000000000000000000000000000000""},
                {"message": "Pull request opened", "title": ""Logging docs", "base": ""main", "head": ""feature-logging-docs", "pr_number": 1"},
                {"message": "Reviewers requested.", "pr_number": 1"},
                {"message": "Review submitted."},
                {"message": "Pull request merged.", "merged": ""true", "merge_method": "merge""},
                {"message": "Topic 'observability' added."},
                {"message": "Release created.", "repo_name": ""k8s-monitoring", "tag_name": ""v1.5.0", "title": "Logging docs""},
                {"tag_name": "v1.5.0", "body": "Add logging documentation.""},
                {"message": \Issue created", "number": 1"},
                {"printed_ts": "2025-08-21T12:00:00Z", "message": "k8s-monitoring logging docs published and released as v1.5.0.""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_63",
        "instruction": "You are 'ml-engineer'. Ensure the following final state, with all values precise and case\u2011sensitive: \u2022 A repository named 'ml-ops-pipeline' is established and is owned by you; its visibility is 'public' with its default branch as 'main'. 'mlops' and 'pipeline' are included in the repository topics. \u2022 A branch named 'feature-training-job' must exist. On that branch, have the file 'pipelines/train.py' contain exactly 'print('train-v1')' and ensure the file 'kubernetes/job.yaml' holds precisely 'kind: Job'. \u2022 The most recent commit on 'feature-training-job' has the message 'Add training job and pipeline stub'. \u2022 Pull request #1 should target base 'main' from head 'feature-training-job' with the title 'Add training pipeline' and body 'Introduce training job and pipeline stub.', request 'qa-mike' and 'dev-sue' as reviewers, and make sure it is approved and merged. \u2022 Enable branch protection on 'main' with rules set exactly at {'required_reviews': 2}. \u2022 A release on 'ml-ops-pipeline' should exist with tag 'v0.8.0', titled 'Training pipeline', and having the body 'Initial training job and pipeline stub.', ensuring the latest release points to tag 'v0.8.0'. \u2022 An issue titled 'Validate training pipeline' must exist with body 'Run end\u2011to\u2011end training and verify outputs.' and labeled 'mlops'. \u2022 The terminal log must include precisely one additional entry that reads 'ml-ops-pipeline v0.8.0 released.' Satisfy all criteria in a fresh database run, using only deterministic values.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ml-engineer"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "ml-ops-pipeline",
                    "visibility": "public",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "ml-ops-pipeline",
                    "topic": "mlops"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "ml-ops-pipeline",
                    "topic": "pipeline"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "ml-ops-pipeline",
                    "source_branch": "main",
                    "new_branch": "feature-training-job"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "ml-ops-pipeline",
                    "branch": "feature-training-job",
                    "path": "pipelines/train.py",
                    "content": "print('train-v1')"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "ml-ops-pipeline",
                    "branch": "feature-training-job",
                    "path": "kubernetes/job.yaml",
                    "content": "kind: Job"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "ml-ops-pipeline",
                    "branch": "feature-training-job",
                    "commit_message": "Add training job and pipeline stub"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "ml-ops-pipeline",
                    "title": "Add training pipeline",
                    "body": "Introduce training job and pipeline stub.",
                    "base": "main",
                    "head": "feature-training-job"
                },
            },
            {
                "name": "RequestPullRequestReviewers",
                "arguments": {
                    "repo_name": "ml-ops-pipeline",
                    "pr_number": 1,
                    "reviewers": [
                        {qa-mike},
                        {dev-sue}
                    ]
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "ml-ops-pipeline",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ml-ops-pipeline",
                    "pr_number": 1
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "ml-ops-pipeline",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "required_reviews": 2
                    }
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "ml-ops-pipeline",
                    "tag": "v0.8.0",
                    "title": "Training pipeline",
                    "body": "Initial training job and pipeline stub."
                },
            },
            {
                "name": "GetLatestRelease",
                "arguments": {
                    "repo_name": "ml-ops-pipeline"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ml-ops-pipeline",
                    "title": "Validate training pipeline",
                    "body": "Run end‑to‑end training and verify outputs.",
                    "labels": [
                        {mlops}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "ml-ops-pipeline v0.8.0 released."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "ml-ops-pipeline""},
                {"message": "Pull request opened", "title": ""Add training pipeline", "pr_number": 1"},
                {"message": "Reviewers requested.", "requested_reviewers": ["dev-sue", "qa-mike"]"},
                {"message": "Pull request merged.", "merged": "true""},
                {"message": "Branch protection enabled."},
                {"message": "Release created.", "repo_name": ""ml-ops-pipeline", "tag_name": "v0.8.0""},
                {"tag_name": "v0.8.0", "title": "Training pipeline""},
                {"message": \Issue created", "number": 1"},
                {"message": "ml-ops-pipeline v0.8.0 released."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_64",
        "instruction": "You are 'security-group'. Upon completing the task, the repository condition for 'security-scanner' must meet ALL of the following: \u2022 'main' branch is protected with rules exactly {\"require_reviews\": true, \"require_status_checks\": true, \"enforce_admins\": true}. \u2022 There is an issue titled 'Security audit required' with the body 'Run compliance checks on encryption and password policies.' and labeled 'security'. \u2022 All code scanning alerts for the repository are listed. \u2022 The terminal audit log includes the EXACT entry 'security-scanner security audit scheduled with branch protection enforced.'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "security-group"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "require_reviews": "true",
                        "require_status_checks": "true",
                        "enforce_admins": "true"
                    }
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Security audit required",
                    "body": "Run compliance checks on encryption and password policies.",
                    "labels": [
                        {security}
                    ]
                },
            },
            {
                "name": "ListCodeScanningAlerts",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "security-scanner security audit scheduled with branch protection enforced."
                }
            }
        ],
        "outputs": [
                {"message": "Branch protection enabled.", "repo_name": ""security-scanner", "branch": ""main", "protected": "true""},
                {"message": \Issue created", "number": 1"},
                {"alerts": [{\alert_number": 18, "severity": ""critical", "state": ""open", "description": "Unsafe deserialization in rule configuration parser"}, { "alert_number": 21, "severity": ""high", "state": ""open", "description": "Potential buffer overflow in string handling"}, {"alert_number": 24, "severity": ""medium", "state": ""fixed", "description": "Use of deprecated crypto functions"}, { "alert_number": 27, "severity": ""low", "state": ""dismissed", "description": "Missing input validation in CLI arguments"}]"},
                {"printed_ts": "2025-08-21T12:00:00Z", "message": "security-scanner security audit scheduled with branch protection enforced.""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_65",
        "instruction": "As 'ryan-dev', ensure the final state is delivered with all values being exact and case-sensitive: \u2022 Verify the creation of a repository named 'log-analyzer' which you own, ensuring its visibility is set to 'public' and the default branch is 'main'. The repository topics must include 'logs' and 'analysis'. \u2022 Confirm the existence of a branch named 'feature-alerts'. This branch must have the file 'src/alerts.py' with the exact content 'print('alert-v1')' and 'docs/alerts.md' with '# Log alerts'. \u2022 Ensure the most recent commit on 'feature-alerts' contains the message 'Add log alerting support'. \u2022 There should be a pull request numbered #1, which targets 'main' from 'feature-alerts', with the title 'Introduce log alerting' and the body 'Add alerting support and docs.', which is approved and merged. \u2022 Branch protection rules must be enabled on 'main' with exactly {'required_reviews': 1}. \u2022 Confirm a release with tag 'v1.2.0', titled 'Log alerting', and body 'Adds alerting support for log analyzer.' exists. \u2022 An issue titled 'Refine alert thresholds' should be present with the body 'Tune thresholds for production logs.' labeled 'alerts'. \u2022 The terminal log must have one appended entry reading 'log-analyzer v1.2.0 released.' All these must be met in a new database run, using only deterministic values.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ryan-dev"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "log-analyzer",
                    "visibility": "public",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "log-analyzer",
                    "topic": "logs"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "log-analyzer",
                    "topic": "analysis"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "log-analyzer",
                    "source_branch": "main",
                    "new_branch": "feature-alerts"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "log-analyzer",
                    "branch": "feature-alerts",
                    "path": "src/alerts.py",
                    "content": "print('alert-v1')"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "log-analyzer",
                    "branch": "feature-alerts",
                    "path": "docs/alerts.md",
                    "content": "# Log alerts"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "log-analyzer",
                    "branch": "feature-alerts",
                    "commit_message": "Add log alerting support"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "log-analyzer",
                    "title": "Introduce log alerting",
                    "body": "Add alerting support and docs.",
                    "base": "main",
                    "head": "feature-alerts"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "log-analyzer",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "log-analyzer",
                    "pr_number": 1
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "log-analyzer",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "required_reviews": 1
                    }
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "log-analyzer",
                    "tag": "v1.2.0",
                    "title": "Log alerting",
                    "body": "Adds alerting support for log analyzer."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "log-analyzer",
                    "title": "Refine alert thresholds",
                    "body": "Tune thresholds for production logs.",
                    "labels": [
                        {alerts}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "log-analyzer v1.2.0 released."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "log-analyzer""},
                {"message": "Pull request opened", "title": ""Introduce log alerting", "pr_number": 1"},
                {"message": "Pull request merged.", "merged": "true""},
                {"message": "Branch protection enabled."},
                {"message": "Release created.", "repo_name": ""log-analyzer", "tag_name": "v1.2.0""},
                {"message": \Issue created", "number": 1"},
                {"message": "log-analyzer v1.2.0 released."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_66",
        "instruction": "As 'security-group', upon concluding the task, verify that the 'security-scanner' repository state meets ALL of the following: \u2022 'Main' branch must have protection with rules exactly as {\"require_reviews\": ""true", "require_status_checks\": ""true", "enforce_admins\": \"true\"}. \u2022 The visibility of the repository must remain 'private'. \u2022 Ensure 'compliance' is included in the repository topics. \u2022 There should be an issue titled 'Annual compliance baseline' with the body 'Baseline checks for encryption and password rotation.' carrying the labels ['security','compliance'], along with a comment that matches exactly 'Baseline scheduled for Q4.' \u2022 Verify the Terminal audit log contains the exact entry 'security-scanner compliance baseline scheduled with protections enforced.'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "security-group"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "require_reviews": "true",
                        "require_status_checks": "true",
                        "enforce_admins": "true"
                    }
                },
            },
            {
                "name": "SetRepositoryVisibility",
                "arguments": {
                    "repo_name": "security-scanner",
                    "visibility": "private"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "security-scanner",
                    "topic": "compliance"
                },
            },
            {
                "name": "ListRepoTopics",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Annual compliance baseline",
                    "body": "Baseline checks for encryption and password rotation.",
                    "labels": [
                        {security},
                        {compliance}
                    ]
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 1,
                    "comment": "Baseline scheduled for Q4."
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "security-scanner compliance baseline scheduled with protections enforced."
                }
            }
        ],
        "outputs": [
                {"message": "Branch protection enabled.", "repo_name": ""security-scanner", "branch": ""main", "protected": "true""},
                {"message": "Visibility updated", "repo_name": ""security-scanner", "visibility": "private""},
                {"message": "Topic 'compliance' added."},
                {"topics": [},
                {"message": \Issue created", "number": 1"},
                {"message": "Comment added."},
                {"printed_ts": "2025-08-21T12:00:00Z", "message": "security-scanner compliance baseline scheduled with protections enforced.""}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_67",
        "instruction": "You are 'qa-erin'. Ensure the following outcome, adhering to all values being exact and case-sensitive: \u2022 You must have created a repository named 'automation-tests', which is 'public' and the default branch is 'main'. The repository topics must include 'tests' and 'automation'. \u2022 Establish a branch named 'feature-selenium'. On this branch, the file 'tests/selenium_test.py' should contain the line 'print('selenium-v1')' exactly, and 'docs/tests.md' must include '# Selenium tests' precisely. \u2022 The newest commit on 'feature-selenium' must bear the message 'Add selenium test suite'. \u2022 Pull request #1 should be targeting the base 'main' from head 'feature-selenium', titled 'Add selenium tests', with the body 'Introduce selenium test automation.', should be approved and merged. \u2022 Enable branch protection on 'main' that follows the rules {'required_reviews': 1}. \u2022 A release needs to be on 'automation-tests' with tag 'v0.5.0', title 'Selenium suite', and body 'Initial selenium automation suite.'. \u2022 An issue named 'Expand selenium coverage' must be present with the body 'Add cross-browser tests.', carrying the label 'qa'. \u2022 The terminal log must exactly include one new entry with 'automation-tests v0.5.0 released.' Every condition must be fulfilled in a new database instance; use only deterministic values.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "qa-erin"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "automation-tests",
                    "visibility": "public",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "automation-tests",
                    "topic": "tests"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "automation-tests",
                    "topic": "automation"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "automation-tests",
                    "source_branch": "main",
                    "new_branch": "feature-selenium"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "automation-tests",
                    "branch": "feature-selenium",
                    "path": "tests/selenium_test.py",
                    "content": "print('selenium-v1')"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "automation-tests",
                    "branch": "feature-selenium",
                    "path": "docs/tests.md",
                    "content": "# Selenium tests"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "automation-tests",
                    "branch": "feature-selenium",
                    "commit_message": "Add selenium test suite"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "automation-tests",
                    "title": "Add selenium tests",
                    "body": "Introduce selenium test automation.",
                    "base": "main",
                    "head": "feature-selenium"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "automation-tests",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "automation-tests",
                    "pr_number": 1
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "automation-tests",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "required_reviews": 1
                    }
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "automation-tests",
                    "tag": "v0.5.0",
                    "title": "Selenium suite",
                    "body": "Initial selenium automation suite."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "automation-tests",
                    "title": "Expand selenium coverage",
                    "body": "Add cross-browser tests.",
                    "labels": [
                        {qa}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "automation-tests v0.5.0 released."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "automation-tests""},
                {"message": "Pull request opened", "title": ""Add selenium tests", "pr_number": 1"},
                {"message": "Pull request merged.", "merged": "true""},
                {"message": "Branch protection enabled."},
                {"message": "Release created.", "repo_name": ""automation-tests", "tag_name": "v0.5.0""},
                {"message": \Issue created", "number": 1"},
                {"message": "automation-tests v0.5.0 released."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_68",
        "instruction": "You are 'release-manager'. Establish the following situation, ensuring all values are maintained exactly as case-sensitive: \u2022 A repository should initially be created by you named 'release-runbooks', marked as 'private' with a default branch of 'main', and then renamed to 'release-ops', shifting visibility to 'public'. The ending topics of the repository should be exactly ['release'], with 'runbooks' topic appearing earlier but removed eventually. \u2022 Develop a branch called 'feature-runbooks'. On this branch, 'docs/runbook.md' must include '# Release runbook v1' accurately. \u2022 The last commit on 'feature-runbooks' should have the message 'Add initial release runbook'. \u2022 Issue #1 must exist in 'release-ops', named 'Prepare v1.0 checklist' with the body 'Checklist for release v1.0.', labeled 'release' and 'checklist', and must include exactly one comment saying 'Checklist created.' \u2022 Branch protection for 'main' needs to be active, following the rules {'required_reviews': 1}. \u2022 A release should be on 'release-ops' with tag 'v1.0.0', title 'Release operations v1', and body 'Initial runbooks.'. \u2022 The terminal log should precisely display one new entry with the message 'release-ops v1.0.0 published.' All criteria must be met in a fresh database iteration; ensure usage of deterministic values only.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "release-manager"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "release-runbooks",
                    "visibility": "private",
                    "default_branch": "main"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "release-runbooks",
                    "topic": "release"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "release-runbooks",
                    "topic": "runbooks"
                },
            },
            {
                "name": "RenameRepository",
                "arguments": {
                    "old_name": "release-runbooks",
                    "new_name": "release-ops"
                },
            },
            {
                "name": "SetRepositoryVisibility",
                "arguments": {
                    "repo_name": "release-ops",
                    "visibility": "public"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "release-ops",
                    "source_branch": "main",
                    "new_branch": "feature-runbooks"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "release-ops",
                    "branch": "feature-runbooks",
                    "path": "docs/runbook.md",
                    "content": "# Release runbook v1"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "release-ops",
                    "branch": "feature-runbooks",
                    "commit_message": "Add initial release runbook"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "release-ops",
                    "title": "Prepare v1.0 checklist",
                    "body": "Checklist for release v1.0.",
                    "labels": [
                        {release}
                    ]
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "release-ops",
                    "issue_number": 1,
                    "comment": "Checklist created."
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "release-ops",
                    "issue_number": 1,
                    "label": "checklist"
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "release-ops",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "required_reviews": 1
                    }
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "release-ops",
                    "tag": "v1.0.0",
                    "title": "Release operations v1",
                    "body": "Initial runbooks."
                },
            },
            {
                "name": "RemoveRepoTopic",
                "arguments": {
                    "repo_name": "release-ops",
                    "topic": "runbooks"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "release-ops v1.0.0 published."
                }
            }
        ],
        "outputs": [
                {"message": "Repository created", "repo_name": "release-runbooks""},
                {"message": "Repository renamed", "new_name": "release-ops""},
                {"message": "Visibility updated", "repo_name": ""release-ops", "visibility": "public""},
                {"message": "Committed to branch", "commit_message": "Add initial release runbook""},
                {"message": "Comment added."},
                {"message": \Label "checklist" added.""},
                {"message": "Branch protection enabled."},
                {"message": "Release created.", "repo_name": ""release-ops", "tag_name": "v1.0.0""},
                {"message": \Topic "runbooks" removed.""},
                {"message": "release-ops v1.0.0 published."}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_69",
        "instruction": "Your responsibility is as 'design-team'. Within 'ui-kit', initiate two feature branches originating from 'main', and set up two PRs, then enumerate open PRs. Branches & files: - feature-a: docs/featA.md = '# Feat A\n' - feature-b: docs/featB.md = '# Feat B\n' PRs: - title 'Add feature A docs' (head=feature-a -> base=main) - title 'Add feature B docs' (head=feature-b -> base=main) Provide both PR titles and titles from the list_open_pull_requests.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "design-team"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "source_branch": "main",
                    "new_branch": "feature-a"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature-a",
                    "path": "docs/featA.md",
                    "content": "# Feat A\n",
                    "commit_message": "Add feature A docs"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Add feature A docs",
                    "head": "feature-a",
                    "base": "main"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "source_branch": "main",
                    "new_branch": "feature-b"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature-b",
                    "path": "docs/featB.md",
                    "content": "# Feat B\n",
                    "commit_message": "Add feature B docs"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Add feature B docs",
                    "head": "feature-b",
                    "base": "main"
                },
            },
            {
                "name": "ListOpenPullRequests",
                "arguments": {
                    "repo_name": "ui-kit"
                }
            }
        ],
        "outputs": [
                {"message": "Pull request opened", "title": ""Add feature A docs", "base": ""main", "head": "feature-a""},
                {"message": "Pull request opened", "title": ""Add feature B docs", "base": ""main", "head": "feature-b""},
                {"open_pr_titles": [\Introduce Theme Provider", "Release 1.0 prep", "Add feature A docs", "Add feature B docs"]"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_70",
        "instruction": "As 'platform-team', in the 'infra-terraform' repository, guarantee this finalized state: There must be precisely one open pull request directed at the default branch 'main'. PR #1 should utilize the head branch 'feature-docs-a' and contain a sole file 'docs/A.md' with the precise content '# Doc A\n'; its definitive title should be 'Docs: add A' and the definite body 'Adds docs/A.md.'. In conclusion, you submit the precise tool outcome of listing open pull requests for 'infra-terraform', along with the tool output listing the files altered in the latest opened PR.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "platform-team"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "infra-terraform"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "infra-terraform"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "source_branch": "main",
                    "new_branch": "feature-docs-a"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "feature-docs-a",
                    "path": "docs/A.md",
                    "content": "# Doc A\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "feature-docs-a",
                    "commit_message": "Docs: add A"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "Docs: add A",
                    "body": "Adds docs/A.md.",
                    "base": "main",
                    "head": "feature-docs-a"
                },
            },
            {
                "name": "ListOpenPullRequests",
                "arguments": {
                    "repo_name": "infra-terraform"
                },
            },
            {
                "name": "ListPullRequestFiles",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 1
                }
            }
        ],
        "outputs": [
                {"pull_requests": [{number": 1, "title": ""Docs: add A", "state": ""open", "base": ""main", "head": "feature-docs-a"}]"},
                {"most_recent_pr_files": \files": ["docs/A.md"]"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_71",
        "instruction": "You are 'maya-w'. Handle the delivery of a pull request in 'acme-webapp' from branch 'feature-security-doc' into 'main'. This should add a new file named SECURITY.md with the precise content: # Security Policy To report vulnerabilities, email security@enterprise.com. We aim to triage within 2 business days. Use PR title 'Add SECURITY.md', body 'Introduces a basic security policy and disclosure contact.', and commit message 'docs: add SECURITY.md with contact and triage info'. Provide a return of that PR\u2019s file list.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "source_branch": "main",
                    "new_branch": "feature-security-doc"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature-security-doc",
                    "path": "SECURITY.md",
                    "content": "# Security Policy\n\nTo report vulnerabilities, email security@enterprise.com.\nWe aim to triage within 2 business days.",
                    "commit_message": "docs: add SECURITY.md with contact and triage info"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Add SECURITY.md",
                    "body": "Introduces a basic security policy and disclosure contact.",
                    "head": "feature-security-doc",
                    "base": "main"
                },
            },
            {
                "name": "ListPullRequestFiles",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 1
                }
            }
        ],
        "outputs": [
                {"message": "Pull request opened", "title": ""Add SECURITY.md", "base": ""main", "head": "feature-security-doc""},
                {"files": [\SECURITY.md"]"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_72",
        "instruction": "Your role is 'maya-w'. In 'acme-webapp', coordinate the application of the label 'triage-urgent' to issues #3 and #8. Afterward, post the exact comment 'Labels applied: triage-urgent, quality.' on both issues, and return the list of issue numbers that possess the label 'triage-urgent'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 3,
                    "label": "triage-urgent"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 8,
                    "label": "triage-urgent"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 3,
                    "comment": "Labels applied: triage-urgent, quality."
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 8,
                    "comment": "Labels applied: triage-urgent, quality."
                },
            },
            {
                "name": "ListIssuesByLabel",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "label": "triage-urgent"
                }
            }
        ],
        "outputs": [
                {\}issues_with_label_triage-urgent": [3, 8]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_73",
        "instruction": "You serve as 'infra-lead'. Within 'k8s-monitoring', generate a new feature branch named 'feature-docs', insert a file 'docs/USAGE.md' containing '# Usage Guide This file explains how to use the monitoring stack.', initiate a pull request into 'main' with the 'title' 'Add usage docs' and body 'Introduces usage documentation.', then eliminate the feature branch post-merge.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "new_branch": "feature-docs",
                    "source_branch": "main"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "feature-docs",
                    "path": "docs/USAGE.md",
                    "content": "# Usage Guide\n\nThis file explains how to use the monitoring stack."
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Add usage docs",
                    "body": "Introduces usage documentation.",
                    "base": "main",
                    "head": "feature-docs"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 1
                },
            },
            {
                "name": "DeleteBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "feature-docs"
                }
            }
        ],
        "outputs": [
                {"message": "Pull request opened", "title": ""Add usage docs", "base": ""main", "head": "feature-docs""},
                {\}merged": true,"merge_method": "merge"",
                {"status": "ok"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_74",
        "instruction": "You act as 'design-team'. For 'ui-kit', establish a branch 'feature-license-update', revise the LICENSE file with the precise text 'MIT License updated', and commit it with the message 'chore: update license'. Next, create a pull request into 'main' titled 'Update LICENSE' with the body 'Switch project to MIT license.', and provide the list of files altered in the PR.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "design-team"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "source_branch": "main",
                    "new_branch": "feature-license-update"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature-license-update",
                    "path": "LICENSE",
                    "content": "MIT License updated",
                    "commit_message": "chore: update license"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Update LICENSE",
                    "body": "Switch project to MIT license.",
                    "head": "feature-license-update",
                    "base": "main"
                },
            },
            {
                "name": "ListPullRequestFiles",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 1
                }
            }
        ],
        "outputs": [
                {"message": "Pull request opened", "title": ""Update LICENSE", "base": ""main", "head": "feature-license-update""},
                {"files": [\LICENSE"]"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_75",
        "instruction": "Assume the role of 'infra-lead'. Handle the preparation of the 'acme-bootstrap' repository for team onboarding. Make sure it includes a protected default branch called 'main', a working branch termed 'setup-work' that contains initial project files, and that a triage issue is established to coordinate setup tasks. Adhere to these precise specifications: - Files: 'README.md' with content '# Bootstrap repository.' and '.gitignore' with content '.DS_Store\nnode_modules/\n__pycache__/\n' - Branch protection on 'main': require_pull_request_reviews=true, dismiss_stale_reviews=true, enforce_admins=true, required_status_checks=['build'] - Issue: title='Initial setup checklist', body='Track bootstrap tasks for this repo.', labels=['triage', 'setup'] - Commit messages: 'add README.md', 'add .gitignore' Provide: (1) the protection rule block for 'main', and (2) the complete issue object with its labels",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "acme-bootstrap",
                    "default_branch": "main"
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "acme-bootstrap",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "require_pull_request_reviews": "true",
                        "dismiss_stale_reviews": "true",
                        "enforce_admins": "true",
                        "required_status_checks": [
                            {build}
                        ]
                    }
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "acme-bootstrap",
                    "source_branch": "main",
                    "new_branch": "setup-work"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-bootstrap",
                    "branch": "setup-work",
                    "path": "README.md",
                    "content": "# Bootstrap repository."
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-bootstrap",
                    "branch": "setup-work",
                    "commit_message": "add README.md"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-bootstrap",
                    "branch": "setup-work",
                    "path": ".gitignore",
                    "content": ".DS_Store\\nnode_modules/\\n__pycache__/\\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-bootstrap",
                    "branch": "setup-work",
                    "commit_message": "add .gitignore"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-bootstrap",
                    "title": "Initial setup checklist",
                    "body": "Track bootstrap tasks for this repo.",
                    "labels": [
                        {triage},
                        {setup}
                    ]
                },
            },
            {
                "name": "GetBranchProtection",
                "arguments": {
                    "repo_name": "acme-bootstrap",
                    "branch": "main"
                },
            },
            {
                "name": "GetIssue",
                "arguments": {
                    "repo_name": "acme-bootstrap",
                    "issue_number": 1
                }
            }
        ],
        "outputs": [
                {{'require_pull_request_reviews': 'true', 'dismiss_stale_reviews': 'true', 'enforce_admins': 'true', 'required_status_checks': ['build']}},
                {{'number': 1, 'title': 'Initial setup checklist', 'labels': ['triage', 'setup'], 'state': 'open'}}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_76",
        "instruction": "You are 'maya-w' developing the 'acme-webapp' service. Coordinate the submission of a pull request from a feature branch titled 'feat-auth' into the primary 'main' branch. The PR must introduce these specific files: \u2022 api/__init__.py with content 'main()' \u2022 api/auth.py with content 'class Auth: pass' \u2022 tests/test_auth.py with content 'def test_stub(): assert True' Use commit message: 'feat-auth: scaffolding and tests' Apply PR title: 'Add auth scaffolding' and body: 'Introduce basic auth module skeleton.' Provide the catalog of files altered in the PR.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "source_branch": "main",
                    "new_branch": "feat-auth"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feat-auth",
                    "path": "api/__init__.py",
                    "content": "main()"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feat-auth",
                    "commit_message": "feat-auth: scaffolding and tests"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feat-auth",
                    "path": "api/auth.py",
                    "content": "class Auth: pass"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feat-auth",
                    "commit_message": "feat-auth: scaffolding and tests"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feat-auth",
                    "path": "tests/test_auth.py",
                    "content": "def test_stub(): assert True"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feat-auth",
                    "commit_message": "feat-auth: scaffolding and tests"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Add auth scaffolding",
                    "body": "Introduce basic auth module skeleton.",
                    "head": "feat-auth",
                    "base": "main"
                },
            },
            {
                "name": "ListPullRequestFiles",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 1
                }
            }
        ],
        "outputs": [
                {{'files': ['api/__init__.py', 'api/auth.py', 'tests/test_auth.py']}}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_77",
        "instruction": "You are 'maya-w', preparing to launch the initial release for the existing public repository 'acme-webapp'. After setting up the build pipeline and changelog on the default branch 'main', publish version 'v0.1.0' as the inaugural release, ensuring to include appropriate metadata. Use the following specifics: - Ensure '.github/workflows/ci.yml' contains: 'Triggers CI workflows' - Ensure 'CHANGELOG.md' includes: '# Changelog ## v0.1.0 - Initial release' - Commit message to be used: 'ci+docs: add CI workflow and CHANGELOG' - Release details: \u2022 Tag: 'v0.1.0' \u2022 Title: 'v0.1.0' \u2022 Body: 'Initial release' Return the release metadata as generated by the release tool.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "main",
                    "path": ".github/workflows/ci.yml",
                    "content": "Triggers CI workflows"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "main",
                    "path": "CHANGELOG.md",
                    "content": "# Changelog  ## v0.1.0 - Initial release"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "main",
                    "commit_message": "ci+docs: add CI workflow and CHANGELOG"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "tag": "v0.1.0",
                    "title": "v0.1.0",
                    "body": "Initial release"
                },
            },
            {
                "name": "GetLatestRelease",
                "arguments": {
                    "repo_name": "acme-webapp"
                }
            }
        ],
        "outputs": [
                {{'tag_name': 'v0.1.0', 'body': 'Initial release'}}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_81",
        "instruction": "You are 'infra-lead' setting up a new repository 'infra-runbooks'. Deliver a setup for an incident runbook in such a way that, once finished, the repository state meets ALL the acceptance criteria outlined below, utilizing the specified constants as provided. This is a statement of desired results and literals, NOT a step-by-step plan. ACCEPTANCE CRITERIA (the final state must adhere to all of these conditions): \u2022 A 'infra-runbooks' repository exists (public) with its default branch as 'main'. \u2022 A feature branch contains a committed incident runbook file with the exact content below. \u2022 Repository topics include exactly the listed topic. \u2022 Branch protection is enabled on the default branch 'main', with the exact protected flag and rules JSON provided below. \u2022 Issue number 1 must be closed and must include the exact pre-PR and post-release comments outlined below. \u2022 A pull request (number 1 post-reset) from the feature branch into 'main' must be merged. \u2022 A release with the specified tag below must be present. CONSTANTS TO USE VERBATIM (all literals must match precisely): - Repository visibility: public - Default branch name: main - Feature branch name: feature-incident-101 - File path: docs/incidents/101.md - File content (exact; SINGLE trailing newline only): # Incident 101: First Response Steps: 1. Page on-call 2. Gather logs 3. Mitigate blast radius Owner: SRE - Commit message: docs: add incident 101 guide - Repository topic to add: runbooks - Branch protection target: main - Branch protection 'protected' value: \"true\" - Branch protection rules JSON (use exactly this object): {\"required_status_checks\": [\"ci\"], \"enforce_admins\": \"true\"} - Issue to create/label/close: 1 - Issue title: Add incident 101 runbook - Issue body: Track and document initial incident response. - Label to add: documentation - Pre-PR issue comment: Runbook authored; PR will close this issue. - PR title: Add incident 101 runbook - PR body: Closes #1 - Pull request review decision: approve - Release tag: v1.0.0-incidents - Release body: First incident runbook. - Post-release issue comment: Shipped in 'v1.0.0-incidents'",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "visibility": "public",
                    "default_branch": "main"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "infra-runbooks"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "new_branch": "feature-incident-101",
                    "source_branch": "main"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "branch": "feature-incident-101",
                    "path": "docs/incidents/101.md",
                    "content": "# Incident 101: First Response\n\nSteps:\n1. Page on-call\n2. Gather logs\n3. Mitigate blast radius\n\nOwner: SRE\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "branch": "feature-incident-101",
                    "commit_message": "docs: add incident 101 guide"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "topic": "runbooks"
                },
            },
            {
                "name": "SetBranchProtection",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "branch": "main",
                    "protected": "true",
                    "rules": {
                        "required_status_checks": [
                            {ci}
                        ],
                        "enforce_admins": "true"
                    }
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "title": "Add incident 101 runbook",
                    "body": "Track and document initial incident response."
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "issue_number": 1,
                    "label": "documentation"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "issue_number": 1,
                    "comment": "Runbook authored; PR will close this issue."
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "title": "Add incident 101 runbook",
                    "body": "Closes #1",
                    "head": "feature-incident-101",
                    "base": "main"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "pr_number": 1
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "issue_number": 1,
                    "state": "closed"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "tag": "v1.0.0-incidents",
                    "body": "First incident runbook."
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "infra-runbooks",
                    "issue_number": 1,
                    "comment": "Shipped in 'v1.0.0-incidents'"
                }
            }
        ],
        "outputs": [
                {"message": "Incident runbook merged and released", "repo_name": "infra-runbooks""},
                {\}pr_number": 1, "closed_issue": 1, "release_tag": "v1.0.0-incidents""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_85",
        "instruction": "You are 'ryan-dev'. Within 'utils-js', ensure that PR #16 addressing Issue #7 has been integrated. Monitor TypeScript declaration support in PR #14 by leaving a comment: 'Tracking TypeScript declarations in PR #14'. Assign a repository topic 'typescript' and write a post on Issue #4: 'TS support is tracked in PR #14'. Add a note to the terminal: 'utils-js TS support tracked and negative currency fix verified'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ryan-dev"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "utils-js"
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 16
                },
            },
            {
                "name": "GetIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 7
                },
            },
            {
                "name": "GetPullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 14
                },
            },
            {
                "name": "CommentOnPullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 14,
                    "comment": "Tracking TypeScript declarations in PR #14"
                },
            },
            {
                "name": "AddRepoTopic",
                "arguments": {
                    "repo_name": "utils-js",
                    "topic": "typescript"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 4,
                    "comment": "TS support is tracked in PR #14"
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "utils-js TS support tracked and negative currency fix verified"
                }
            }
        ],
        "outputs": [
                {"message": "utils-js TS support tracked and negative currency fix verified"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_86",
        "instruction": "You are 'maya-w' assigned to the 'acme-webapp' repository. Your role is to deploy a CI/security update, ensuring that upon completion, the repository's condition meets ALL the acceptance criteria below, using the exact constants specified. Refrain from interpreting this as step-by-step instructions; it is a specification of outcomes and literals. ACCEPTANCE CRITERIA (the final state should incorporate all of these): \u2022 A feature branch is established, containing the change set. \u2022 A new issue (number 1 after reset) is resolved and closed. \u2022 A pull request (number 1 after reset) is successfully merged into the default branch. \u2022 A release bearing the exact tag below is present. \u2022 The closed issue includes the precise post-release comment. CONSTANTS TO USE VERBATIM (ensure all literals match precisely): - Feature branch name: feature-ci-policy - Base branch name: main - File path #1: SECURITY.md - File content #1 (exact; SINGLE trailing newline only): # Security Policy Report: security@enterprise.com Triage: 2 business days - File path #2: .github/workflows/ci.yml - File content #2 (exact): name: CI on: [push, pull_request] jobs: build: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - run: echo Build OK - Commit message: ci: add SECURITY.md and CI workflow - Issue title: Enforce CI and security policy - Issue body: Track CI rollout for branch feature-ci-policy. - Label to add: compliance - Pre-PR issue comment: PR will reference and close this issue. - PR title: CI: add security policy and workflow - PR body: Closes #1 - Release tag: v0.1.0-ci - Post-release issue comment: Released in 'v0.1.0-ci'",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "GetHeadSha",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "main"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "new_branch": "feature-ci-policy",
                    "source_branch": "main"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature-ci-policy",
                    "path": "SECURITY.md",
                    "content": "# Security Policy\n\nReport: security@enterprise.com\nTriage: 2 business days\n"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature-ci-policy",
                    "path": ".github/workflows/ci.yml",
                    "content": "name: CI\non: [push, pull_request]\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - run: echo Build OK\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature-ci-policy",
                    "commit_message": "ci: add SECURITY.md and CI workflow"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Enforce CI and security policy",
                    "body": "Track CI rollout for branch feature-ci-policy."
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "label": "compliance"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "comment": "PR will reference and close this issue."
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "CI: add security policy and workflow",
                    "body": "Closes #1",
                    "head": "feature-ci-policy",
                    "base": "main"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 1
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "state": "closed"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "tag": "v0.1.0-ci"
                },
            },
            {
                "name": "GetLatestRelease",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "comment": "Released in 'v0.1.0-ci'"
                }
            }
        ],
        "outputs": [
                {"message": "Pull request merged", "repo_name": "acme-webapp""},
                {\}pr_number": 1, "issue_number": 1, "release_tag": "v0.1.0-ci""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_87",
        "instruction": "As 'server-main', assigned to the 'payments-service' repository, handle the delivery of a 3DS feature update ensuring that, upon completion, the repository's state meets ALL outlined acceptance criteria with exact usage of the provided constants. Consider this a specification for outcomes and literals, not a step-by-step agenda. ACCEPTANCE CRITERIA (final state must reflect all of these): \u2022 A feature branch exists that contains the 3DS configuration change. \u2022 Issue number 13 is closed. \u2022 A pull request (number 1 after reset for this repo context) is merged into the default branch. \u2022 A release with the exact tag below exists. \u2022 The closed issue contains the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: feature-3ds-flow - Base branch name: main - File path: src/payments/three_ds.ts - File content (exact; SINGLE trailing newline only): export const ENABLE_3DS = true; - Commit message: feat(3ds): enable 3DS flow configuration - Issue to label and close: 13 - Label to add: 3ds - Pre-PR issue comment: Implementing 3DS; PR will close this issue. - PR title: Enable 3DS flow configuration - PR body: Closes #13 - Pull request review decision: approve - Release tag: v0.2.0-3ds - Post-release issue comment: Released in 'v0.2.0-3ds' (3DS enabled)",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "server-main"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "payments-service"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "payments-service"
                },
            },
            {
                "name": "GetHeadSha",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "main"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "new_branch": "feature-3ds-flow",
                    "source_branch": "main"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "feature-3ds-flow",
                    "path": "src/payments/three_ds.ts",
                    "content": "export const ENABLE_3DS = true;\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "feature-3ds-flow",
                    "commit_message": "feat(3ds): enable 3DS flow configuration"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 13,
                    "label": "3ds"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 13,
                    "comment": "Implementing 3DS; PR will close this issue."
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Enable 3DS flow configuration",
                    "body": "Closes #13",
                    "head": "feature-3ds-flow",
                    "base": "main"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 1
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 13,
                    "state": "closed"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "payments-service",
                    "tag": "v0.2.0-3ds"
                },
            },
            {
                "name": "GetLatestRelease",
                "arguments": {
                    "repo_name": "payments-service"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 13,
                    "comment": "Released in 'v0.2.0-3ds' (3DS enabled)"
                }
            }
        ],
        "outputs": [
                {"message": "3DS flow merged and released", "repo_name": "payments-service""},
                {\}pr_number": 1, "closed_issue": 13, "release_tag": "v0.2.0-3ds""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_88",
        "instruction": "As 'ui-developer', responsible for the 'react-dashboard' repository, coordinate the implementation of a WebSocket leak fix, ensuring that upon completion, the repository's state adheres to ALL specified acceptance criteria using the exact constants provided. Regard this as a specification of outcomes and literals, NOT a step-by-step guide. ACCEPTANCE CRITERIA (final state must reflect all of these): \u2022 A feature branch exists that contains the fix for a WebSocket cleanup-related memory leak. \u2022 Issue number 25 is closed. \u2022 A pull request (number 1 after reset for this repo) is merged into the default branch. \u2022 A release with the exact tag below exists. \u2022 The closed issue contains the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: fix-memory-leak-ws - Base branch name: main - File path: src/hooks/useLiveSocket.ts - File content (exact; SINGLE trailing newline only): import { useEffect } from 'react'; export function useLiveSocket(url: string) { useEffect(() => { const ws = new WebSocket(url); return () => { ws.close(); }; }, [url]); } - Commit message: fix(ws): ensure cleanup to prevent memory leak - Issue to label and close: 25 - Label to add: memory-leak - Pre-PR issue comment: Fix adds cleanup for WebSocket in useEffect. - PR title: Fix memory leak in WebSocket cleanup - PR body: Closes #25 - Pull request review decision: approve - Release tag: v2.2.1-leakfix - Post-release issue comment: Patched in 'v2.2.1-leakfix'",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ui-developer"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "react-dashboard"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "react-dashboard"
                },
            },
            {
                "name": "GetHeadSha",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "main"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "new_branch": "fix-memory-leak-ws",
                    "source_branch": "main"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "fix-memory-leak-ws",
                    "path": "src/hooks/useLiveSocket.ts",
                    "content": "import { useEffect } from 'react';\n\nexport function useLiveSocket(url: string) {\n  useEffect(() => {\n    const ws = new WebSocket(url);\n    return () => {\n      ws.close();\n    };\n  }, [url]);\n}\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "fix-memory-leak-ws",
                    "commit_message": "fix(ws): ensure cleanup to prevent memory leak"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 25,
                    "label": "memory-leak"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 25,
                    "comment": "Fix adds cleanup for WebSocket in useEffect."
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "title": "Fix memory leak in WebSocket cleanup",
                    "body": "Closes #25",
                    "head": "fix-memory-leak-ws",
                    "base": "main"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 1
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 25,
                    "state": "closed"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "tag": "v2.2.1-leakfix"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 25,
                    "comment": "Patched in 'v2.2.1-leakfix'"
                }
            }
        ],
        "outputs": [
                {"message": "WebSocket leak fix merged and released", "repo_name": "react-dashboard""},
                {\}pr_number": 1, "closed_issue": 25, "release_tag": "v2.2.1-leakfix""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_89",
        "instruction": "Handle the role of 'design-team' in the 'ui-kit' repository to provide an icon-pack update. Ensure that upon finishing, the repository state meets ALL acceptance criteria detailed below, utilizing the exact constants given. Consider this a specification of outcomes and literals, NOT a step-by-step process. ACCEPTANCE CRITERIA (the final state must embody all of these): \u2022 A feature branch exists that includes two new SVG icons. \u2022 Issue number 6 is closed. \u2022 A pull request (number 1 after a reset for this repo) is merged into the default branch. \u2022 A release with the precise tag below exists. \u2022 The closed issue contains the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: feature-icons-pack - Base branch name: main - File path #1: src/icons/email.svg - File content #1 (exact; SINGLE trailing newline only): <svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M2 6h20v12H2z'/><path d='M2 6l10 7L22 6'/></svg> - File path #2: src/icons/phone.svg - File content #2 (exact; SINGLE trailing newline only): <svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M6 2h12v20H6z'/><path d='M9 18h6'/></svg> - Commit message: feat(icons): add email and phone SVGs - Issue to label and close: 6 - Label to add: icons - Pre-PR issue comment: Adding email and phone icons; PR will close this issue. - PR title: Add email and phone icons - PR body: Closes #6 - Pull request review decision: approve - Release tag: v1.1.0-icons - Post-release issue comment: Shipped in 'v1.1.0-icons'",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "design-team"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "GetHeadSha",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "main"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "new_branch": "feature-icons-pack",
                    "source_branch": "main"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature-icons-pack",
                    "path": "src/icons/email.svg",
                    "content": "<svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M2 6h20v12H2z'/><path d='M2 6l10 7L22 6'/></svg>\n"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature-icons-pack",
                    "path": "src/icons/phone.svg",
                    "content": "<svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M6 2h12v20H6z'/><path d='M9 18h6'/></svg>\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature-icons-pack",
                    "commit_message": "feat(icons): add email and phone SVGs"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 6,
                    "label": "icons"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 6,
                    "comment": "Adding email and phone icons; PR will close this issue."
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Add email and phone icons",
                    "body": "Closes #6",
                    "head": "feature-icons-pack",
                    "base": "main"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 1
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 6,
                    "state": "closed"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "ui-kit",
                    "tag": "v1.1.0-icons"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 6,
                    "comment": "Shipped in 'v1.1.0-icons'"
                }
            }
        ],
        "outputs": [
                {"message": "Icon pack merged and released", "repo_name": "ui-kit""},
                {\}pr_number": 1, "closed_issue": 6, "release_tag": "v1.1.0-icons""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_90",
        "instruction": "Coordinate the responsibilities of 'infra-lead' within the 'k8s-monitoring' repository to implement a Grafana performance improvement. Ensure that when completed, the repository\u2019s condition adheres to ALL acceptance criteria outlined below, using the precise constants provided. Consider this a specification of outcomes and literals, NOT a step-by-step method. ACCEPTANCE CRITERIA (the final state must demonstrate all of these): \u2022 A feature branch exists featuring a documented performance optimization for Grafana dashboards. \u2022 Issue number 35 is closed. \u2022 A pull request (number 1 after a reset for this repo) is merged into the default branch. \u2022 A release with the specific tag below is present. \u2022 The closed issue carries the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: fix-grafana-performance - Base branch name: main - File path: grafana/dashboards/perf-optimization.md - File content (exact; SINGLE trailing newline only): ## Grafana Dashboard Performance - Reduce panel refresh to 30s - Prefer $__interval for rate() - Limit table rows to 200 - Commit message: perf(grafana): optimize dashboard refresh and query patterns - Issue to label and close: 35 - Label to add: performance - Pre-PR issue comment: Applying dashboard optimizations; PR will close this issue. - PR title: Optimize Grafana dashboard performance - PR body: Closes #35 - Pull request review decision: approve - Release tag: v0.9.1-perf - Post-release issue comment: Improvements shipped in 'v0.9.1-perf'",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "GetHeadSha",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "main"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "new_branch": "fix-grafana-performance",
                    "source_branch": "main"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "fix-grafana-performance",
                    "path": "grafana/dashboards/perf-optimization.md",
                    "content": "## Grafana Dashboard Performance\n\n- Reduce panel refresh to 30s\n- Prefer $__interval for rate()\n- Limit table rows to 200\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "fix-grafana-performance",
                    "commit_message": "perf(grafana): optimize dashboard refresh and query patterns"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 35,
                    "label": "performance"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 35,
                    "comment": "Applying dashboard optimizations; PR will close this issue."
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Optimize Grafana dashboard performance",
                    "body": "Closes #35",
                    "head": "fix-grafana-performance",
                    "base": "main"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 1
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 35,
                    "state": "closed"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "tag": "v0.9.1-perf"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 35,
                    "comment": "Improvements shipped in 'v0.9.1-perf'"
                }
            }
        ],
        "outputs": [
                {"message": "Grafana performance fix merged and released", "repo_name": "k8s-monitoring""},
                {\}pr_number": 1, "closed_issue": 35, "release_tag": "v0.9.1-perf""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_92",
        "instruction": "As a 'ml-engineer' in the 'ml-pipeline' repository, ensure the delivery of an MLflow connectivity fortification update. At the conclusion, the repository must fulfill ALL of the following acceptance criteria with the specific constants provided. This is a definition of outcomes and literals, NOT procedural instructions. ACCEPTANCE CRITERIA (final state must include all of these): \u2022 A feature branch is present, containing a retry-based MLflow client setup. \u2022 Issue number 29 should be marked as closed. \u2022 A pull request (first since repo reset) is integrated into the default branch. \u2022 A release with the precise tag as mentioned exists. \u2022 The closed issue features the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must match precisely): - Feature branch name: fix-mlflow-retry - Base branch name: main - File path: pipeline/config/mlflow.yml - File content (exact; SINGLE trailing newline only): mlflow: tracking_uri: ${MLFLOW_TRACKING_URI} client: retries: 5 backoff_seconds: 2 - Commit message: fix(mlflow): add client retries for connectivity issues - Issue to label and close: 29 - Label to add: mlflow - Pre-PR issue comment: Adding retry settings for MLflow client; PR will close this issue. - PR title: Add MLflow client retries to mitigate connectivity issues - PR body: Closes #29 - Pull request review decision: approve - Release tag: v0.4.0-mlflow - Post-release issue comment: Released in 'v0.4.0-mlflow' (MLflow retries enabled)",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ml-engineer"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "ml-pipeline"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "ml-pipeline"
                },
            },
            {
                "name": "GetHeadSha",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "branch": "main"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "new_branch": "fix-mlflow-retry",
                    "source_branch": "main"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "branch": "fix-mlflow-retry",
                    "path": "pipeline/config/mlflow.yml",
                    "content": "mlflow:\n  tracking_uri: ${MLFLOW_TRACKING_URI}\n  client:\n    retries: 5\n    backoff_seconds: 2\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "branch": "fix-mlflow-retry",
                    "commit_message": "fix(mlflow): add client retries for connectivity issues"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "issue_number": 29,
                    "label": "mlflow"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "issue_number": 29,
                    "comment": "Adding retry settings for MLflow client; PR will close this issue."
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "title": "Add MLflow client retries to mitigate connectivity issues",
                    "body": "Closes #29",
                    "head": "fix-mlflow-retry",
                    "base": "main"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "pr_number": 1
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "issue_number": 29,
                    "state": "closed"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "tag": "v0.4.0-mlflow"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "issue_number": 29,
                    "comment": "Released in 'v0.4.0-mlflow' (MLflow retries enabled)"
                }
            }
        ],
        "outputs": [
                {"message": "MLflow retry configuration merged and released", "repo_name": "ml-pipeline""},
                {\}pr_number": 1, "closed_issue": 29, "release_tag": "v0.4.0-mlflow""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_93",
        "instruction": "As a 'app-developer' in the 'flutter-finance-app' repository, ensure the implementation of an accessibility enhancement. On completion, the repository should meet ALL of the following acceptance criteria using the exact constants provided. This is a specification of results and literals, NOT detailed guidance. ACCEPTANCE CRITERIA (final state must encompass all of these): \u2022 A feature branch exists encompassing accessibility (a11y) semantic labels for buttons. \u2022 Issue number 22 is marked as closed. \u2022 A pull request (1st post-reset) is incorporated into the default branch. \u2022 A release with the exact tag specified exists. \u2022 The closed issue includes the exact post-release comment. CONSTANTS TO USE VERBATIM (all literals must correspond exactly): - Feature branch name: feature-a11y-labels - Base branch name: main - File path: lib/a11y/semantics.dart - File content (exact; SINGLE trailing newline only): /// Accessibility semantics for key buttons class A11yLabels { static const String addBudget = 'Add budget'; static const String viewReports = 'View reports'; } - Commit message: feat(a11y): add semantic labels for primary actions - Issue to label and close: 22 - Label to add: a11y - Pre-PR issue comment: Adding semantic labels for primary buttons; PR will close this issue. - PR title: Add a11y semantic labels for primary actions - PR body: Closes #22 - Pull request review decision: approve - Release tag: v1.3.0-a11y - Post-release issue comment: Accessibility labels shipped in 'v1.3.0-a11y'",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "app-developer"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "flutter-finance-app"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "flutter-finance-app"
                },
            },
            {
                "name": "GetHeadSha",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "branch": "main"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "new_branch": "feature-a11y-labels",
                    "source_branch": "main"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "branch": "feature-a11y-labels",
                    "path": "lib/a11y/semantics.dart",
                    "content": "/// Accessibility semantics for key buttons\nclass A11yLabels {\n  static const String addBudget = 'Add budget';\n  static const String viewReports = 'View reports';\n}\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "branch": "feature-a11y-labels",
                    "commit_message": "feat(a11y): add semantic labels for primary actions"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "issue_number": 22,
                    "label": "a11y"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "issue_number": 22,
                    "comment": "Adding semantic labels for primary buttons; PR will close this issue."
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "title": "Add a11y semantic labels for primary actions",
                    "body": "Closes #22",
                    "head": "feature-a11y-labels",
                    "base": "main"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "pr_number": 1
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "issue_number": 22,
                    "state": "closed"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "tag": "v1.3.0-a11y"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "issue_number": 22,
                    "comment": "Accessibility labels shipped in 'v1.3.0-a11y'"
                }
            }
        ],
        "outputs": [
                {"message": "Accessibility labels merged and released", "repo_name": "flutter-finance-app""},
                {\}pr_number": 1, "closed_issue": 22, "release_tag": "v1.3.0-a11y""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_94",
        "instruction": "As 'ryan-dev', your task within the 'utils-js' repository is to implement TypeScript declaration support in a manner that ultimately aligns the repository with ALL specified acceptance criteria, utilizing provided constants precisely. This is an outline of required results and literals, NOT a procedural guide. ACCEPTANCE CRITERIA (the final status must encapsulate all conditions): \u2022 A feature branch is present that includes a TypeScript declaration file for the library. \u2022 Issue number 4 has been resolved and closed. \u2022 A pull request (being the first after repository reset) merges into the default branch. \u2022 A release exists with the precise tag mentioned below. \u2022 The closed issue contains the specified post-release comment verbatim. CONSTANTS TO USE VERBATIM (all literals must precisely mirror the following): - Feature branch name: feature-ts-decls - Base branch name: master - File path: types/index.d.ts - File content (exact; SINGLE trailing newline only): declare module 'utils-js' { export function formatCurrency(value: number): string; } - Commit message: feat(types): add TypeScript declaration file - Issue to label and close: 4 - Label to add: typescript - Pre-PR issue comment: Adding TypeScript declaration file; PR will close this issue. - PR title: Add TypeScript declaration file - PR body: Closes #4 - Pull request review decision: approve - Release tag: v1.1.0-types - Post-release issue comment: TypeScript support shipped in 'v1.1.0-types'",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ryan-dev"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "utils-js"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "utils-js"
                },
            },
            {
                "name": "GetHeadSha",
                "arguments": {
                    "repo_name": "utils-js",
                    "branch": "master"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "utils-js",
                    "new_branch": "feature-ts-decls",
                    "source_branch": "master"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "utils-js",
                    "branch": "feature-ts-decls",
                    "path": "types/index.d.ts",
                    "content": "declare module 'utils-js' {\n  export function formatCurrency(value: number): string;\n}\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "utils-js",
                    "branch": "feature-ts-decls",
                    "commit_message": "feat(types): add TypeScript declaration file"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 4,
                    "label": "typescript"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 4,
                    "comment": "Adding TypeScript declaration file; PR will close this issue."
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "Add TypeScript declaration file",
                    "body": "Closes #4",
                    "head": "feature-ts-decls",
                    "base": "master"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 1
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 4,
                    "state": "closed"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "utils-js",
                    "tag": "v1.1.0-types"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 4,
                    "comment": "TypeScript support shipped in 'v1.1.0-types'"
                }
            }
        ],
        "outputs": [
                {"repo_name": "utils-js"},
                {\}pr_number": 1, "closed_issue": 4, "release_tag": "v1.1.0-types""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_95",
        "instruction": "As 'infra-lead' working on the 'k8s-monitoring' repository, your objective is to establish custom application monitoring so that, upon completion, the repository meets ALL specified acceptance criteria, utilizing the exact constants provided. Consider this a statement of necessary results and literals, NOT procedural instructions. ACCEPTANCE CRITERIA (the final state must fulfill all stated criteria): \u2022 A feature branch includes a Prometheus ServiceMonitor dedicated to custom applications. \u2022 Issue number 37 is resolved and closed. \u2022 The initial pull request (after repository reset) is merged into the default branch. \u2022 There is a release tagged exactly as cited below. \u2022 The resolved issue contains the exact post-release comment specified. CONSTANTS TO USE VERBATIM (all literals must replicate the following precisely): - Feature branch name: feature-servicemonitor-apps - Base branch name: main - File path: prometheus/servicemonitor-apps.yaml - File content (exact; SINGLE trailing newline only): apiVersion: monitoring.coreos.com/v1 kind: ServiceMonitor metadata: name: apps-servicemonitor namespace: monitoring spec: selector: matchLabels: app.kubernetes.io/part-of: custom-apps namespaceSelector: any: true endpoints: - port: http-metrics interval: 30s - Commit message: feat(prometheus): add ServiceMonitor for custom applications - Issue to label and close: 37 - Label to add: monitoring - Pre-PR issue comment: Adding ServiceMonitor for custom apps; PR will close this issue. - PR title: Add ServiceMonitor for custom applications - PR body: Closes #37 - Pull request review decision: approve - Release tag: v0.10.0-servicemonitor - Post-release issue comment: Custom app monitoring added in 'v0.10.0-servicemonitor'",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "infra-lead"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "GetHeadSha",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "main"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "new_branch": "feature-servicemonitor-apps",
                    "source_branch": "main"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "feature-servicemonitor-apps",
                    "path": "prometheus/servicemonitor-apps.yaml",
                    "content": "apiVersion: monitoring.coreos.com/v1\nkind: ServiceMonitor\nmetadata:\n  name: apps-servicemonitor\n  namespace: monitoring\nspec:\n  selector:\n    matchLabels:\n      app.kubernetes.io/part-of: custom-apps\n  namespaceSelector:\n    any: true\n  endpoints:\n  - port: http-metrics\n    interval: 30s\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "feature-servicemonitor-apps",
                    "commit_message": "feat(prometheus): add ServiceMonitor for custom applications"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 37,
                    "label": "monitoring"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 37,
                    "comment": "Adding ServiceMonitor for custom apps; PR will close this issue."
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Add ServiceMonitor for custom applications",
                    "body": "Closes #37",
                    "head": "feature-servicemonitor-apps",
                    "base": "main"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 1
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 37,
                    "state": "closed"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "tag": "v0.10.0-servicemonitor"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 37,
                    "comment": "Custom app monitoring added in 'v0.10.0-servicemonitor'"
                }
            }
        ],
        "outputs": [
                {\}pr_number": 1, "closed_issue": 37, "release_tag": "v0.10.0-servicemonitor""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_96",
        "instruction": "As the user 'language-ai' involved in the 'nlp-models' repository, oversee delivery of a training memory optimization ensuring the repository ultimately meets all specified acceptance criteria and uses the exact constants. Regard this as specifying outcomes and literals, without offering step-by-step instructions. ACCEPTANCE CRITERIA (the final state must encompass all of these): \u2022 A feature branch is present containing a configuration for memory-efficient training. \u2022 Issue number 12 is resolved. \u2022 A pull request (which is number 1 after the repository reset) has been integrated into the default branch. \u2022 A release with the precise tag below is in place. \u2022 The resolved issue has the specified post-release comment included. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: feat-memory-optim - Base branch name: main - File path: configs/training/memory.yaml - File content (exact; SINGLE trailing newline only): training: gradient_accumulation_steps: 4 batch_size: 8 mixed_precision: fp16 - Commit message: feat(train): add memory-optimized training config - Issue to label and close: 12 - Label to add: memory - Pre-PR issue comment: Adding memory-optimized training config; PR will close this issue. - PR title: Add memory-optimized training configuration - PR body: Closes #12 - Pull request review decision: approve - Release tag: v0.8.0-memory - Post-release issue comment: Memory optimization available in 'v0.8.0-memory'",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "language-ai"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "nlp-models"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "nlp-models"
                },
            },
            {
                "name": "GetHeadSha",
                "arguments": {
                    "repo_name": "nlp-models",
                    "branch": "main"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "nlp-models",
                    "new_branch": "feat-memory-optim",
                    "source_branch": "main"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "nlp-models",
                    "branch": "feat-memory-optim",
                    "path": "configs/training/memory.yaml",
                    "content": "training:\n  gradient_accumulation_steps: 4\n  batch_size: 8\n  mixed_precision: fp16\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "nlp-models",
                    "branch": "feat-memory-optim",
                    "commit_message": "feat(train): add memory-optimized training config"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "label": "memory"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "comment": "Adding memory-optimized training config; PR will close this issue."
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "Add memory-optimized training configuration",
                    "body": "Closes #12",
                    "head": "feat-memory-optim",
                    "base": "main"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 1
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "state": "closed"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "nlp-models",
                    "tag": "v0.8.0-memory"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "comment": "Memory optimization available in 'v0.8.0-memory'"
                }
            }
        ],
        "outputs": [
                {"message": "Memory optimization merged and released", "repo_name": "nlp-models""},
                {\}pr_number": 1, "closed_issue": 12, "release_tag": "v0.8.0-memory""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_97",
        "instruction": "Acting as 'maya-w' within the 'acme-webapp' repository, coordinate a fastpath performance enhancement to ensure the repository ultimately fulfills all acceptance criteria laid out below and employs the exact constants specified. Interpret this as detailing outcomes and literals, not a procedural guide. ACCEPTANCE CRITERIA (the final state must demonstrate all of these): \u2022 A feature branch exists that incorporates an algorithm implementation for fastpath on large datasets. \u2022 Issue number 3 is marked as closed. \u2022 A pull request (which is number 1 after the repository reset) has been merged into the default branch. \u2022 A release with the specified tag detailed below is created. \u2022 The closed issue includes the specified post-release comment. CONSTANTS TO USE VERBATIM (all literals must match exactly): - Feature branch name: feature-perf-fastpath - Base branch name: main - File path: src/opt/fastpath.js - File content (exact; SINGLE trailing newline only): export function fastpath(items) { if (!Array.isArray(items) || items.length === 0) return []; const seen = new Set(); const out = []; for (let i = 0; i < items.length; i++) { const v = items[i]; if (!seen.has(v)) { seen.add(v); out.push(v); } } return out; } - Commit message: perf: introduce fastpath algorithm for large datasets - Issue to label and close: 3 - Label to add: performance - Pre-PR issue comment: Implementing fastpath algorithm; PR will close this issue. - PR title: Introduce fastpath algorithm for performance - PR body: Closes #3 - Pull request review decision: approve - Release tag: v0.2.0-perf - Post-release issue comment: Performance improvements shipped in 'v0.2.0-perf'",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "maya-w"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "GetHeadSha",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "main"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "new_branch": "feature-perf-fastpath",
                    "source_branch": "main"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature-perf-fastpath",
                    "path": "src/opt/fastpath.js",
                    "content": "export function fastpath(items) {\n  if (!Array.isArray(items) || items.length === 0) return [];\n  const seen = new Set();\n  const out = [];\n  for (let i = 0; i < items.length; i++) {\n    const v = items[i];\n    if (!seen.has(v)) { seen.add(v); out.push(v); }\n  }\n  return out;\n}\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature-perf-fastpath",
                    "commit_message": "perf: introduce fastpath algorithm for large datasets"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 3,
                    "label": "performance"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 3,
                    "comment": "Implementing fastpath algorithm; PR will close this issue."
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Introduce fastpath algorithm for performance",
                    "body": "Closes #3",
                    "head": "feature-perf-fastpath",
                    "base": "main"
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 1,
                    "review_decision": "approve"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 1
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 3,
                    "state": "closed"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "tag": "v0.2.0-perf"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 3,
                    "comment": "Performance improvements shipped in 'v0.2.0-perf'"
                }
            }
        ],
        "outputs": [
                {"message": "Fastpath performance improvement merged and released", "repo_name": "acme-webapp""},
                {\}pr_number": 1, "closed_issue": 3, "release_tag": "v0.2.0-perf""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_98",
        "instruction": "Your role is 'platform-team'. Manage the process to have a pull request merged into the default branch 'main' within the repository 'infra-terraform' from a feature branch named 'feature-docs-refresh'. Ensure this pull request precisely adds two new files: - 'docs/CHANGELOG.md' featuring the text: ## Changelog - 2025-08-21: Initial changelog entry. - 'docs/REFRESH.md' featuring the text: # Infra Terraform modules. Ops note: refreshed docs on 2025-08-21. Use 'docs: add CHANGELOG and refresh note' as the commit message. Use 'Docs refresh: add CHANGELOG and REFRESH.md' as the pull request title. Include 'Automated docs refresh.' in the pull request body. Request reviews from 'security-group' and 'infra-lead'. Finally, provide the merged PR number, the files identified as modified in the PR, and the latest commit SHA on branch 'main'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "platform-team"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "infra-terraform"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "source_branch": "main",
                    "new_branch": "feature-docs-refresh"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "feature-docs-refresh",
                    "path": "docs/CHANGELOG.md",
                    "content": "## Changelog\n\n- 2025-08-21: Initial changelog entry.\n"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "feature-docs-refresh",
                    "path": "docs/REFRESH.md",
                    "content": "# Infra\n\nTerraform modules.\n\nOps note: refreshed docs on 2025-08-21.\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "feature-docs-refresh",
                    "commit_message": "docs: add CHANGELOG and refresh note"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "Docs refresh: add CHANGELOG and REFRESH.md",
                    "body": "Automated docs refresh.",
                    "base": "main",
                    "head": "feature-docs-refresh"
                },
            },
            {
                "name": "ListPullRequestFiles",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 1
                },
            },
            {
                "name": "RequestPullRequestReviewers",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 1,
                    "reviewers": [
                        {security-group},
                        {infra-lead}
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 1
                },
            },
            {
                "name": "GetHeadSha",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "main"
                }
            }
        ],
        "outputs": [
                {"merged_pr_number": 1},
                {"changed_files_reported_by_pr": [\docs/CHANGELOG.md", "docs/REFRESH.md"]"},
                {"main_branch_sha_after_merge": "sha_0000000000000000000000000000000000000000"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_99",
        "instruction": "As 'ui-developer', your task is to coordinate a hardening update to the repository 'react-dashboard'. This update should entail two files: `kubernetes/policy.yaml` which should contain a Kubernetes network policy, and `docs/changelog.md` for documenting the change. The policy file must include exactly: ``` apiVersion: v1 kind: NetworkPolicy metadata: name: baseline spec: podSelector: {} policyTypes: [\"Ingress\",\"Egress\"] ``` The changelog should contain: ``` # Changelog - task_01: baseline policies and docs (deterministic). ``` Use the branch name `feature-hardening` and commit message `Add baseline policies [task_01]`. The modifications must be submitted through a pull request with the title 'Harden defaults [task_01]' and the body 'Baseline policies and changelog.', requiring review by 'security-group' and 'qa-erin'. Ensure it receives approval with the comment 'LGTM [task_01]' and includes the review note 'Please review \u2014 deterministic run [task_01].'. Provide the list of altered files from the PR, the last SHA of the default branch after merging, and the end message: 'Merged PR #1 into main for react-dashboard [task_01]'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "ui-developer"
                },
            },
            {
                "name": "GetDefaultBranch",
                "arguments": {
                    "repo_name": "react-dashboard"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "source_branch": "main",
                    "new_branch": "feature-hardening"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "feature-hardening",
                    "path": "kubernetes/policy.yaml",
                    "content": "apiVersion: v1\nkind: NetworkPolicy\nmetadata:\n  name: baseline\nspec:\n  podSelector: {}\n  policyTypes: [\"Ingress\",\"Egress\"]\n"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "feature-hardening",
                    "path": "docs/changelog.md",
                    "content": "# Changelog\n\n- task_01: baseline policies and docs (deterministic).\n"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "feature-hardening",
                    "commit_message": "Add baseline policies [task_01]"
                },
            },
            {
                "name": "InitializePullRequestsBlock",
                "arguments": {
                    "repo_name": "react-dashboard"
                },
            },
            {
                "name": "CreatePullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "title": "Harden defaults [task_01]",
                    "body": "Baseline policies and changelog.",
                    "base": "main",
                    "head": "feature-hardening"
                },
            },
            {
                "name": "RequestPullRequestReviewers",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 1,
                    "reviewers": [
                        {security-group},
                        {qa-erin}
                    ]
                },
            },
            {
                "name": "CommentOnPullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 1,
                    "comment": "Please review — deterministic run [task_01]."
                },
            },
            {
                "name": "CreatePullRequestReview",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 1,
                    "review_decision": "approve",
                    "comment": "LGTM [task_01]"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 1
                },
            },
            {
                "name": "GetHeadSha",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "main"
                },
            },
            {
                "name": "ListPullRequestFiles",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 1
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Merged PR #1 into main for react-dashboard [task_01]"
                }
            }
        ],
        "outputs": [
                {"merged": "true"},
                {"sha": "sha_0000000000000000000000000000000000000000"},
                {"files": [\docs/changelog.md", "kubernetes/policy.yaml"]"},
                {"message": "Merged PR #1 into main for react-dashboard [task_01]"}
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_100",
        "instruction": "As 'platform-team', within the repository 'infra-terraform', ensure the following final condition: An issue exists with the title 'Stabilize ops runbook' and the body 'Document the on-call escalation steps for staging and production.'\u2014both precisely. This issue should be closed and possess exactly the labels 'operations' and 'documentation', with the comment 'Ack: logged by ops-bot.'. Lastly, present the results after examining issues for the term 'operations'.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "platform-team"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "infra-terraform"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "Stabilize ops runbook",
                    "body": "Document the on-call escalation steps for staging and production."
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 1,
                    "label": "operations"
                },
            },
            {
                "name": "AddLabelToIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 1,
                    "label": "documentation"
                },
            },
            {
                "name": "AddIssueComment",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 1,
                    "comment": "Ack: logged by ops-bot."
                },
            },
            {
                "name": "UpdateIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 1,
                    "state": "closed"
                },
            },
            {
                "name": "SearchIssues",
                "arguments": {
                    "query": "operations"
                }
            }
        ],
        "outputs": [
                {\}search_results_for_operations": [1]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_20",
        "instruction": "As 'app-developer', in the repository 'flutter-finance-app', establish the following final condition with all values exact and case-sensitive: \u2022 A branch named 'hotfix-1.2.1' is present. Within this branch, the 'CHANGELOG.md' file includes precisely '## 1.2.1 - hotfix'. \u2022 The newest commit on 'hotfix-1.2.1' possesses the message 'Add CHANGELOG for v1.2.1'. \u2022 A release is there with the tag 'v1.2.1', titled 'v1.2.1 [task_101]', and has the body 'body-[task_101]'. Additionally, the most recent release corresponds to tag 'v1.2.1'. \u2022 An issue exists with the title 'Release v1.2.1 note [task_101]' and body 'body-[task_101]' carrying the label 'release-log'. \u2022 The terminal log shows precisely one added entry stating 'Release v1.2.1 created in flutter-finance-app [task_101]'. Produce the latest release tag from 'flutter-finance-app'. Each requirement must be achieved in a fresh database run; employ deterministic values only.",
        "actions": [
            {
                "name": "GetMe",
                "arguments": {
                    "username": "app-developer"
                },
            },
            {
                "name": "GetRepository",
                "arguments": {
                    "repo_name": "flutter-finance-app"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "source_branch": "main",
                    "new_branch": "hotfix-1.2.1"
                },
            },
            {
                "name": "WriteFileToBranch",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "branch": "hotfix-1.2.1",
                    "path": "CHANGELOG.md",
                    "content": "## 1.2.1 - hotfix"
                },
            },
            {
                "name": "CommitChangesToBranch",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "branch": "hotfix-1.2.1",
                    "commit_message": "Add CHANGELOG for v1.2.1"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "tag": "v1.2.1",
                    "title": "v1.2.1 [task_101]",
                    "body": "body-[task_101]"
                },
            },
            {
                "name": "GetLatestRelease",
                "arguments": {
                    "repo_name": "flutter-finance-app"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "title": "Release v1.2.1 note [task_101]",
                    "body": "body-[task_101]",
                    "labels": [
                        {release-log}
                    ]
                },
            },
            {
                "name": "AppendTerminal",
                "arguments": {
                    "message": "Release v1.2.1 created in flutter-finance-app [task_101]"
                }
            }
        ],
        "outputs": [
                {"message": "Branch created", "new_branch": "hotfix-1.2.1""},
                {"message": "Committed to branch", "commit_message": "Add CHANGELOG for v1.2.1""},
                {"message": "Release created.", "repo_name": ""flutter-finance-app", "tag_name": "v1.2.1""},
                {"tag_name": "v1.2.1"},
                {"labels": [\release-log"]"},
                {"message": "Release v1.2.1 created in flutter-finance-app [task_101]"}
        ]
    }
]
