from domains.dto import Task, Action

TASKS = [

    # # 20 (alice-w) acme-webapp: note high-severity alerts and tag repo
    # Task(
    #     annotator='0',
    #     user_id="task_20",
    #     instruction=(
    #         "You are 'alice-w' and must operate only through the available tools (single turn).\n\n"
    #         "YOU SHOULD:\n"
    #         "• In repository 'acme-webapp', add the exact topic literal below and ensure it is present in topics.\n"
    #         "• Produce a listing of HIGH-severity code scanning alerts for that repo.\n"
    #         "• Append the exact terminal message literal below and ensure it is the last terminal entry.\n\n"
    #         "LITERALS (use verbatim)\n"
    #         "- repo: acme-webapp\n"
    #         "- topic to add: security-audit\n"
    #         "- terminal message: Audit snapshot recorded for acme-webapp (high severity)\n"
    #     ),
    #     actions=[
    #         Action(name="get_me", kwargs={"username": "alice-w"}),

    #         # Read: repo context (safe & deterministic)
    #         Action(name="get_repository", kwargs={"repo_name": "acme-webapp"}),

    #         # Read: list only HIGH-severity alerts for this repo
    #         Action(name="list_code_scanning_alerts", kwargs={"repo_name": "acme-webapp", "severity": "high"}),

    #         # Write: add topic, then verify topics include it
    #         Action(name="add_repo_topic", kwargs={"repo_name": "acme-webapp", "topic": "security-audit"}),
    #         Action(name="list_repo_topics", kwargs={"repo_name": "acme-webapp"}),

    #         # Write: append terminal confirmation and verify it is last
    #         Action(name="append_terminal", kwargs={"message": "Audit snapshot recorded for acme-webapp (high severity)"}),
    #         Action(name="list_terminal_last_message", kwargs={}),
    #     ],
    #     outputs=[
    #         '"message": "Topic \'security-audit\' added."',
    #         '"entries": {"printed_ts": "2025-08-21T12:00:00Z", "message": "Audit snapshot recorded for acme-webapp (high severity)"}',
    #     ],
    # ),
    # 28
    Task(
        annotator='0',
        user_id="task_28",
        instruction=(
            "You are 'mobile-dev'. In 'flutter-finance-app', review Issue #18 and PR #26. "
            "Approve PR with comment: 'Please confirm rendering on iOS 14 and 15 real devices.' requesting validation on iOS 14/15 and label the issue with 'ios1'. "
            "Fetch the last terminal message, then append 'flutter-finance-app iOS charts fix under validation'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "mobile-dev"}),
            Action(name="get_repository", kwargs={"repo_name": "flutter-finance-app"}),
            Action(name="get_issue", kwargs={"repo_name": "flutter-finance-app", "issue_number": 18}),
            Action(name="get_pull_request", kwargs={"repo_name": "flutter-finance-app", "pr_number": 26}),
            Action(
                name="create_pull_request_review",
                kwargs={
                    "repo_name": "flutter-finance-app",
                    "pr_number": 26,
                    "review_decision": "approve",
                    "comment": "Please confirm rendering on iOS 14 and 15 real devices."
                }
            ),
            Action(name="add_label_to_issue", kwargs={"repo_name": "flutter-finance-app", "issue_number": 18, "label": "ios1"}),
            Action(name="list_terminal_last_message", kwargs={}),
            Action(name="append_terminal", kwargs={"message": "flutter-finance-app iOS charts fix under validation"}),
        ],
        outputs=['"message": "flutter-finance-app iOS charts fix under validation"'],
    ),

    # 45
    Task(
        annotator="0",
        user_id="task_45",
        instruction=(
            "You are 'devops-lead'. You must deliver the following end state, with all values exact and case-sensitive:\n"
            "• A repository named 'observability-ops' exists and is owned by you; its visibility is 'private', you need to change it to 'public', default branch is 'main', and it has the topic 'kubernetes'.\n"
            "• A branch 'feature-initial-config' exists. On that branch, the file 'kubernetes/alertmanager.yaml' contains exactly 'alertmanager: config: placeholder-v1' and the file 'kubernetes/prometheus.yaml' contains exactly 'prometheus: config: placeholder-v1'.\n"
            "• The latest commit on 'feature-initial-config' includes the message 'Add initial Prometheus/Alertmanager manifests'.\n"
            "• Pull request #1 targets base 'main' from head 'feature-initial-config' with title 'Add initial Kubernetes monitoring stack' and body 'Bootstrap Prometheus and Alertmanager manifests.', is approved, and is merged.\n"
            "• A release exists on 'observability-ops' with tag 'v0.1.0', title 'Initial monitoring stack', and body 'First cut of monitoring components.'.\n"
            "• The terminal log includes exactly one appended entry with the message 'observability-ops v0.1.0 released.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "devops-lead"}),

            # Create as PRIVATE per spec, then switch to PUBLIC once (no redundancy)
            Action(name="create_repository", kwargs={
                "repo_name": "observability-ops",
                "visibility": "private",
                "default_branch": "main"
            }),
            Action(name="add_repo_topic", kwargs={
                "repo_name": "observability-ops",
                "topic": "kubernetes"
            }),
            Action(name="set_repository_visibility", kwargs={
                "repo_name": "observability-ops",
                "visibility": "public"
            }),

            # Branch + files + commit
            Action(name="create_branch", kwargs={
                "repo_name": "observability-ops",
                "source_branch": "main",
                "new_branch": "feature-initial-config"
            }),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "observability-ops",
                "branch": "feature-initial-config",
                "path": "kubernetes/alertmanager.yaml",
                "content": "alertmanager: config: placeholder-v1"
            }),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "observability-ops",
                "branch": "feature-initial-config",
                "path": "kubernetes/prometheus.yaml",
                "content": "prometheus: config: placeholder-v1"
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "observability-ops",
                "branch": "feature-initial-config",
                "commit_message": "Add initial Prometheus/Alertmanager manifests"
            }),

            # PR: open → approve → merge
            Action(name="create_pull_request", kwargs={
                "repo_name": "observability-ops",
                "title": "Add initial Kubernetes monitoring stack",
                "body": "Bootstrap Prometheus and Alertmanager manifests.",
                "base": "main",
                "head": "feature-initial-config"
            }),
            Action(name="create_pull_request_review", kwargs={
                "repo_name": "observability-ops",
                "pr_number": 1,
                "review_decision": "approve"
            }),
            Action(name="merge_pull_request", kwargs={
                "repo_name": "observability-ops",
                "pr_number": 1
            }),

            # Release + terminal log
            Action(name="create_release", kwargs={
                "repo_name": "observability-ops",
                "tag": "v0.1.0",
                "title": "Initial monitoring stack",
                "body": "First cut of monitoring components."
            }),
            Action(name="append_terminal", kwargs={
                "message": "observability-ops v0.1.0 released."
            }),
        ],
        outputs=[
            # creation confirmation
            '"message": "Repository created", "repo_name": "observability-ops"',
            # PR opened confirmation (stable substring)
            '"message": "Pull request opened", "title": "Add initial Kubernetes monitoring stack", "pr_number": 1',
            # rely on the message field for merge success (avoids bool string/boolean mismatch)
            '"message": "Pull request merged."',
            # release created confirmation
            '"message": "Release created.", "repo_name": "observability-ops", "tag_name": "v0.1.0"',
            # terminal audit line
            '"message": "observability-ops v0.1.0 released."',
        ],
    ),

    # 23
    Task(
        annotator='0',
        user_id="task_23",
        instruction=(
            "You are 'alice-w'. In 'acme-webapp', reconcile the code scanning alert that references 'feature-auth' "
            "with the merged PR #5 from the same branch. Verify current branches, PR #5 details, and changed files. "
            "Open an issue titled 'Reconcile alert ref: feature-auth' with labels ['investigate','security'] and body "
            "'Alert points to feature-auth which was merged and branch is missing in current snapshot; verify lineage and fix metadata'. "
            "Then write the terminal entry 'acme-webapp alert ref reconciliation recorded'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="get_repository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="list_branches", kwargs={"repo_name": "acme-webapp"}),
            Action(name="list_code_scanning_alerts", kwargs={"repo_name": "acme-webapp"}),
            Action(name="list_pull_requests", kwargs={"repo_name": "acme-webapp"}),
            Action(name="get_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 5}),
            Action(name="list_pull_request_files", kwargs={"repo_name": "acme-webapp", "pr_number": 5}),
            Action(name="create_issue", kwargs={
                "repo_name": "acme-webapp",
                "title": "Reconcile alert ref: feature-auth",
                "body": "Alert points to feature-auth which was merged and branch is missing in current snapshot; verify lineage and fix metadata",
                "labels": ["investigate", "security"],
            }),
            Action(name="append_terminal", kwargs={"message": "acme-webapp alert ref reconciliation recorded"}),
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
            "You are 'alice-w'. In the repository 'acme-webapp', create a new issue titled "
            "'Security triage [task_66]' with body 'Investigate dependency exposure paths. [task_66]'. "
            "That issue must carry the label 'triage-urgent', have the exact comment "
            "'Initial triage note recorded. [task_66]', and its final state must be 'closed'. "
            "Return confirmation that the label was applied, the issue's final state, and a search result "
            "entry proving the issue with label 'triage-urgent' exists. Also include this terminal audit line: "
            "'Issue closed with triage-urgent label in acme-webapp [task_66]'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="create_issue", kwargs={
                "repo_name": "acme-webapp",
                "title": "Security triage [task_66]",
                "body": "Investigate dependency exposure paths. [task_66]",
                "labels": []
            }),
            Action(name="add_label_to_issue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "label": "triage-urgent"
            }),
            Action(name="add_issue_comment", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "comment": "Initial triage note recorded. [task_66]"
            }),
            Action(name="update_issue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "state": "closed"
            }),

            # Scope the search deterministically to the repo
            Action(name="search_issues", kwargs={"query": "triage-urgent"}),

            # # Fetch full metadata so outputs can include title + labels
            # Action(name="get_issue", kwargs={
            #     "repo_name": "acme-webapp",
            #     "issue_number": 1
            # }),

            Action(name="append_terminal", kwargs={
                "message": "Issue closed with triage-urgent label in acme-webapp [task_66]"
            }),
        ],
        outputs=[
            '"message": "Label \'triage-urgent\' added."',
            '"state": "closed"',
            # prove search hit deterministically
            '"results": [1]',
            # from get_issue — the judge wanted these explicitly
            # '"title": "Security triage [task_66]"',
            # '"labels": ["triage-urgent"]',
            # terminal audit line
            '"message": "Issue closed with triage-urgent label in acme-webapp [task_66]"',
        ],
    ),

    # 04
    Task(
        annotator='0',
        user_id="task_04",
        instruction=(
            "You are user 'alice-w'. Review the repository 'acme-webapp' for pending PRs. "
            "Comment on PR #5 twice with feedbacks 'Looks good overall' and 'Please add more tests', and summarize your actions in the terminal"
            "with the message 'Comments added and PR #5 reviewed.'"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="get_repository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="list_open_pull_requests", kwargs={"repo_name": "acme-webapp"}),
            Action(name="comment_on_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 5, "comment": "Looks good overall"}),
            Action(name="comment_on_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 5, "comment": "Please add more tests"}),
            # Action(name="get_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 5}),
            Action(name="append_terminal", kwargs={"message": "Comments added and PR #5 reviewed."}),
        ],
        outputs=[
            "Comments added and PR #5 reviewed.",
        ],
    ),

    # 36 (alice-w) File CRUD on a branch with soft-delete via empty content (Hard ~8–9 edges)
    Task(
        annotator='0',
        user_id="task_36",
        instruction=(
            "You are 'alice-w' and must operate only via the available tools.\n\n"
            "Ensure the final repository state in 'acme-webapp' satisfies ALL acceptance criteria below. "
            "Treat these as outcomes/specification—not step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (all must hold):\n"
            "• A branch named 'file-crud' exists, created from 'main'.\n"
            "• The file docs/note.txt exists on branch 'file-crud' and its final content is exactly: 'Hello v2'.\n"
            "• During the run, the content 'Hello v1' was written to docs/note.txt and successfully read back once "
            "(include that read result in outputs).\n"
            "• The change is committed with the exact commit message: 'docs(note): update to v2'.\n"
            "• A pull request exists from 'file-crud' into 'main' titled 'File CRUD update' with body "
            "'Promote CRUD change for docs/note.txt', and the PR shows docs/note.txt as a modified file.\n\n"
            "LITERALS TO USE VERBATIM:\n"
            "- repo: acme-webapp\n"
            "- source branch: main\n"
            "- new branch: file-crud\n"
            "- path: docs/note.txt\n"
            "- v1 content: Hello v1\n"
            "- v2 content: Hello v2\n"
            "- commit message: docs(note): update to v2\n"
            "- PR title: File CRUD update\n"
            "- PR body: Promote CRUD change for docs/note.txt\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),

            Action(name="create_branch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "file-crud"
            }),

            # CREATE (v1)
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "file-crud",
                "path": "docs/note.txt",
                "content": "Hello v1"
            }),

            # READ (capture v1)
            Action(name="get_file_contents", kwargs={
                "repo_name": "acme-webapp",
                "branch": "file-crud",
                "path": "docs/note.txt"
            }),

            # UPDATE (v2)
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "file-crud",
                "path": "docs/note.txt",
                "content": "Hello v2"
            }),

            # Commit once to reflect the change
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "file-crud",
                "commit_message": "docs(note): update to v2"
            }),

            # Open a PR to align with domain proposal richness
            Action(name="create_pull_request", kwargs={
                "repo_name": "acme-webapp",
                "title": "File CRUD update",
                "body": "Promote CRUD change for docs/note.txt",
                "head": "file-crud",
                "base": "main"
            }),

            # Verify the PR lists the modified file
            Action(name="list_pull_request_files", kwargs={
                "repo_name": "acme-webapp",
                "pr_number": 1
            }),
        ],
        outputs=[
            # from create_branch
            '"message": "Branch created"',
            # from get_file_contents (the v1 readback)
            '"path": "docs/note.txt", "content": "Hello v1"',
            # from list_pull_request_files (prove docs/note.txt is in the PR)
            '"docs/note.txt"',
        ],
    ),

    # 79. Terminal logs → fix script → PR diff verification (12 actions)
    Task(
        annotator='0',
        user_id="task_79",
        instruction=(
            "You are 'devops-lead' and need to validate a shell script fix before merge. In the public repository 'acme-scripts', track changes made on a feature branch 'fix-script' created from 'main' branch, where the script 'scripts/run.sh' is updated. The script originally prints 'HELLO', and later includes a fix to also print 'WORLD'. "
            "A terminal log is captured midway using the message 'RUN'. Once the changes are committed and a pull request is created, verify both the diff and the log output. "
            "Use these file contents:\n"
            "- Initial: '#!/usr/bin/env bash\\necho HELLO\\n'\n"
            "- Final: '#!/usr/bin/env bash\\necho HELLO\\necho WORLD\\n'\n"
            "- Commit messages: 'feat: add run script' and 'fix: append WORLD echo'\n"
            "- PR title: 'Fix run script', body: 'Append WORLD echo to run.sh'\n"
            "Return the final terminal log and list of changed files in the PR."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "devops-lead"}),

            # ❌ remove default_branch to avoid assuming a value not in instruction
            Action(name="create_repository", kwargs={
                "repo_name": "acme-scripts",
                "visibility": "public"
            }),

            Action(name="create_branch", kwargs={
                "repo_name": "acme-scripts",
                "source_branch": "main",
                "new_branch": "fix-script"
            }),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-scripts",
                "branch": "fix-script",
                "path": "scripts/run.sh",
                "content": "#!/usr/bin/env bash\necho HELLO\n"
            }),

            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "acme-scripts",
                "branch": "fix-script",
                "commit_message": "feat: add run script"
            }),

            Action(name="append_terminal", kwargs={"message": "RUN"}),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-scripts",
                "branch": "fix-script",
                "path": "scripts/run.sh",
                "content": "#!/usr/bin/env bash\necho HELLO\necho WORLD\n"
            }),

            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "acme-scripts",
                "branch": "fix-script",
                "commit_message": "fix: append WORLD echo"
            }),

            Action(name="initialize_pull_requests_block", kwargs={"repo_name": "acme-scripts"}),

            Action(name="create_pull_request", kwargs={
                "repo_name": "acme-scripts",
                "title": "Fix run script",
                "body": "Append WORLD echo to run.sh",
                "head": "fix-script",
                "base": "main"
            }),

            Action(name="list_pull_request_files", kwargs={
                "repo_name": "acme-scripts",
                "pr_number": 1
            }),

            Action(name="list_terminal_last_message", kwargs={}),
        ],
        outputs=[
            # ✅ mirror list_terminal_last_message (timestamp + message)
            '"timestamp": "2025-08-21T12:00:00Z", "message": "RUN"',
            # ✅ mirror list_pull_request_files by using a substring that will appear
            '"scripts/run.sh"',
        ],
    ),

    # 39
    Task(
        annotator='0',
        user_id="task_39",
        instruction=(
            "You are 'frontend-dev' and must operate only via the available tools.\n\n"
            "Ensure the final repository state in 'react-dashboard' satisfies ALL acceptance criteria below. "
            "Treat these as outcomes/specification—not step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (all must hold):\n"
            "• An issue exists with title 'Build pipeline audit [task_69]' and body "
            "'Verify CI stages and artifacts for reproducibility. [task_69]'.\n"
            "• That issue has the label 'ci-audit', contains the exact comment 'Checklist prepared. [task_69]', "
            "and its state is 'closed'.\n"
            "• A search proves that an issue with label 'ci-audit' exists in 'react-dashboard'.\n"
            "• A terminal entry exists with the exact message: "
            "'Issue closed with ci-audit label in react-dashboard [task_69]'.\n\n"
            "LITERALS TO USE VERBATIM:\n"
            "- repo: react-dashboard\n"
            "- issue title: Build pipeline audit [task_69]\n"
            "- issue body: Verify CI stages and artifacts for reproducibility. [task_69]\n"
            "- label: ci-audit\n"
            "- comment: Checklist prepared. [task_69]\n"
            "- terminal message: Issue closed with ci-audit label in react-dashboard [task_69]\n"
        ),
        actions=[
            # Identity
            Action(name="get_me", kwargs={"username": "frontend-dev"}),

            # Create deterministic issue (flat row)
            Action(
                name="create_issue",
                kwargs={
                    "repo_name": "react-dashboard",
                    "title": "Build pipeline audit [task_69]",
                    "body": "Verify CI stages and artifacts for reproducibility. [task_69]",
                    "labels": []
                },
            ),

            # Apply label + comment
            Action(
                name="add_label_to_issue",
                kwargs={"repo_name": "react-dashboard", "issue_number": 1, "label": "ci-audit"},
            ),
            Action(
                name="add_issue_comment",
                kwargs={
                    "repo_name": "react-dashboard",
                    "issue_number": 1,
                    "comment": "Checklist prepared. [task_69]"
                },
            ),

            # Close the issue
            Action(
                name="update_issue",
                kwargs={"repo_name": "react-dashboard", "issue_number": 1, "state": "closed"},
            ),

            # Deterministic search proof (scoped to repo)
            Action(
                name="search_issues",
                kwargs={"query": "ci-audit"},
            ),

            # Terminal audit
            Action(
                name="append_terminal",
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

    # 32 (alice-w) acme-webapp: create, label, comment, close an issue; confirm last terminal entry
    Task(
        annotator='0',
        user_id="task_32",
        instruction=(
            "You are 'alice-w' and must operate only via the available tools.\n\n"
            "Ensure the final repository state in 'acme-webapp' satisfies ALL acceptance criteria below. "
            "Treat these as outcomes/specification—not step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (all must hold):\n"
            "• An issue exists with title 'Nightly job failed on main' and body \"CI job 'nightly-build' failed due to timeout.\".\n"
            "• That issue has the label 'ops', contains the exact comment 'Investigating: rerun queued.', and its state is 'closed'.\n"
            "• The most recent terminal entry is exactly: 'Issue #1 closed: Nightly job failed on main'.\n\n"
            "LITERALS TO USE VERBATIM:\n"
            "- repo: acme-webapp\n"
            "- issue title: Nightly job failed on main\n"
            "- issue body: CI job 'nightly-build' failed due to timeout.\n"
            "- label to add: ops\n"
            "- issue comment: Investigating: rerun queued.\n"
            "- terminal message: Issue #1 closed: Nightly job failed on main\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="create_issue", kwargs={
                "repo_name": "acme-webapp",
                "title": "Nightly job failed on main",
                "body": "CI job 'nightly-build' failed due to timeout."
            }),
            Action(name="add_label_to_issue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "label": "ops"
            }),
            Action(name="add_issue_comment", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "comment": "Investigating: rerun queued."
            }),
            Action(name="update_issue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "state": "closed"
            }),
            Action(name="append_terminal", kwargs={
                "message": "Issue #1 closed: Nightly job failed on main"
            }),
            Action(name="list_terminal_last_message", kwargs={}),
        ],
        outputs=[
            # from create_issue
            '"message": "Issue created", "number": 1',
            # from add_label_to_issue
            '"message": "Label \'ops\' added."',
            # from list_terminal_last_message (uses timestamp + message)
            '"timestamp": "2025-08-21T12:00:00Z", "message": "Issue #1 closed: Nightly job failed on main"',
        ],
    ),

    # 78
    Task(
        annotator='0',
        user_id="task_78",
        instruction=(
            "You are 'security-team' and must operate only via the available tools.\n\n"
            "Ensure the final repository state in 'security-scanner' satisfies ALL acceptance criteria below. "
            "Treat these as outcomes/specification—not step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (all must hold):\n"
            "• A new branch named 'sec-checks' exists, created from the default branch.\n"
            "• On that branch, the file '.github/workflows/security.yml' exists and its content is exactly:\n"
            "  on: [push]\n"
            "  jobs:\n"
            "    scan:\n"
            "      runs-on: ubuntu-latest\n"
            "      steps:\n"
            "        - name: Security scan\n"
            "          run: echo SCAN\n"
            "• The change is committed with the message: 'chore: add security workflow'.\n"
            "• A pull request exists titled 'Add security workflow' with body "
            "'Adds a basic GitHub Actions scan workflow.' from 'sec-checks' into the default branch.\n"
            "• Outputs must include the list of changed files in that pull request and any open code scanning alerts "
            "with severity 'critical'.\n\n"
            "LITERALS TO USE VERBATIM:\n"
            "- repo: security-scanner\n"
            "- branch: sec-checks\n"
            "- path: .github/workflows/security.yml\n"
            "- workflow content: on: [push]\\njobs:\\n  scan:\\n    runs-on: ubuntu-latest\\n    steps:\\n      - name: Security scan\\n        run: echo SCAN\n"
            "- commit message: chore: add security workflow\n"
            "- PR title: Add security workflow\n"
            "- PR body: Adds a basic GitHub Actions scan workflow.\n"
            "- severity: critical\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "security-team"}),
            Action(name="get_default_branch", kwargs={"repo_name": "security-scanner"}),

            Action(name="create_branch", kwargs={
                "repo_name": "security-scanner",
                "source_branch": "main",
                "new_branch": "sec-checks"
            }),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "security-scanner",
                "branch": "sec-checks",
                "path": ".github/workflows/security.yml",
                "content": "on: [push]\njobs:\n  scan:\n    runs-on: ubuntu-latest\n    steps:\n      - name: Security scan\n        run: echo SCAN"
            }),

            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "security-scanner",
                "branch": "sec-checks",
                "commit_message": "chore: add security workflow"
            }),

            Action(name="create_pull_request", kwargs={
                "repo_name": "security-scanner",
                "title": "Add security workflow",
                "body": "Adds a basic GitHub Actions scan workflow.",
                "head": "sec-checks",
                "base": "main"
            }),

            Action(name="list_pull_request_files", kwargs={
                "repo_name": "security-scanner",
                "pr_number": 1
            }),

            Action(name="list_code_scanning_alerts", kwargs={
                "repo_name": "security-scanner",
                "severity": "critical"
            }),
        ],
        outputs=[
            # changed files list
            '".github/workflows/security.yml"',
            # critical code scanning alert (example shape)
            '"severity": "critical"',
        ],
    ),

    # 83
    Task(
        annotator='0',
        user_id="task_83",
        instruction=(
            "You are alice-w. In the 'acme-webapp' repository, create a branch named 'feature-codeowners' from the default branch. "
            "Add a file at path '.github/CODEOWNERS' containing exactly:\n"
            "* @alice-w\n"
            "src/ @dev-sue\n"
            "tests/ @qa-mike\n"
            "Commit this file with message 'chore: add CODEOWNERS'. "
            "Then open a pull request from 'feature-codeowners' into the default branch titled 'Add CODEOWNERS', "
            "with body 'CODEOWNERS file added for ownership mapping.'. "
            "Leave a pull request review comment saying 'Please review CODEOWNERS ownership setup.' "
            "Finally, return the list of files modified in that PR."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="get_default_branch", kwargs={"repo_name": "acme-webapp"}),
            Action(
                name="create_branch",
                kwargs={"repo_name": "acme-webapp", "new_branch": "feature-codeowners", "source_branch": "main"},
            ),
            Action(
                name="write_file_to_branch",
                kwargs={
                    "repo_name": "acme-webapp",
                    "branch": "feature-codeowners",
                    "path": ".github/CODEOWNERS",
                    "content": "* @alice-w\nsrc/ @dev-sue\ntests/ @qa-mike\n",
                },
            ),
            Action(
                name="commit_changes_to_branch",
                kwargs={"repo_name": "acme-webapp", "branch": "feature-codeowners", "commit_message": "chore: add CODEOWNERS"},
            ),
            Action(
                name="create_pull_request",
                kwargs={
                    "repo_name": "acme-webapp",
                    "title": "Add CODEOWNERS",
                    "body": "CODEOWNERS file added for ownership mapping.",
                    "head": "feature-codeowners",
                    "base": "main",
                },
            ),
            Action(
                name="create_pull_request_review",
                kwargs={
                    "repo_name": "acme-webapp",
                    "pr_number": 1,
                    "review_decision": "comment",
                    "body": "Please review CODEOWNERS ownership setup.",
                },
            ),
            Action(
                name="list_pull_request_files",
                kwargs={
                    "repo_name": "acme-webapp",
                    "pr_number": 1,
                },
            ),
        ],
        outputs=['{"files": [".github/CODEOWNERS"]}'],
    ),

    # 40 (alice-w) Create PR -> Withdraw PR by deleting head branch (Hard ~12–13 edges)
    Task(
        annotator='0',
        user_id="task_40",
        instruction=(
            "You are 'alice-w' and must operate only via the available tools.\n\n"
            "Ensure the final repository state in 'acme-webapp' satisfies ALL acceptance criteria below. "
            "Treat these as outcomes/specification—not step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (all must hold):\n"
            "• A feature branch named 'temp-pr' exists off the default branch and contains a file at path "
            "'docs/pr_demo.txt' with content exactly: 'temporary PR'.\n"
            "• A pull request exists titled 'Temp PR demo' with body 'Demonstration of temporary PR lifecycle.' "
            "from head 'temp-pr' into the default branch.\n"
            "• The pull request is then withdrawn by deleting its head branch: the branch 'temp-pr' no longer exists.\n"
            "• A terminal entry exists with the exact message: 'PR Temp PR demo withdrawn in acme-webapp.'.\n"
            "• Return the pull request title in outputs.\n\n"
            "LITERALS TO USE VERBATIM:\n"
            "- repo: acme-webapp\n"
            "- base branch: main\n"
            "- head branch: temp-pr\n"
            "- path: docs/pr_demo.txt\n"
            "- file content: temporary PR\n"
            "- PR title: Temp PR demo\n"
            "- PR body: Demonstration of temporary PR lifecycle.\n"
            "- terminal message: PR Temp PR demo withdrawn in acme-webapp.\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),

            Action(name="create_branch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "temp-pr"
            }),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "temp-pr",
                "path": "docs/pr_demo.txt",
                "content": "temporary PR"
            }),

            Action(name="create_pull_request", kwargs={
                "repo_name": "acme-webapp",
                "title": "Temp PR demo",
                "body": "Demonstration of temporary PR lifecycle.",
                "head": "temp-pr",
                "base": "main"
            }),

            Action(name="delete_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "temp-pr"
            }),

            Action(name="append_terminal", kwargs={
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
            "You are 'bob-dev'. In the repository 'utils-js', create a new issue titled "
            "'Utilities module audit [task_73]' with body 'Review currency formatting and TypeScript support. [task_73]'. "
            "That issue must carry the label 'module-audit', have the exact comment 'Audit completed. [task_73]', "
            "and its final state must be 'closed'. Return confirmation that the label was applied, the issue's final state, "
            "and a search result entry proving an issue with label 'module-audit' exists. Also include this terminal audit line: "
            "'Issue closed with module-audit label in utils-js [task_73]'."
        ),
        actions=[
            # Identity
            Action(name="get_me", kwargs={"username": "bob-dev"}),

            # Create deterministic issue
            Action(
                name="create_issue",
                kwargs={
                    "repo_name": "utils-js",
                    "title": "Utilities module audit [task_73]",
                    "body": "Review currency formatting and TypeScript support. [task_73]",
                    "labels": []
                },
            ),

            # Apply label + comment
            Action(
                name="add_label_to_issue",
                kwargs={"repo_name": "utils-js", "issue_number": 1, "label": "module-audit"},
            ),
            Action(
                name="add_issue_comment",
                kwargs={
                    "repo_name": "utils-js",
                    "issue_number": 1,
                    "comment": "Audit completed. [task_73]"
                },
            ),

            # Close the issue
            Action(
                name="update_issue",
                kwargs={"repo_name": "utils-js", "issue_number": 1, "state": "closed"},
            ),

            # Prove via search (returns issue number(s))
            Action(
                name="search_issues",
                kwargs={"query": "module-audit"},
            ),

            # Fetch full metadata (title + labels) for outputs
            Action(
                name="get_issue",
                kwargs={"repo_name": "utils-js", "issue_number": 1},
            ),

            # Terminal audit + verify last entry so output can mirror a tool response
            Action(
                name="append_terminal",
                kwargs={"message": "Issue closed with module-audit label in utils-js [task_73]"},
            ),
            Action(
                name="list_terminal_last_message",
                kwargs={},
            ),
        ],
        outputs=[
            # label applied
            '"message": "Label \'module-audit\' added."',
            # final state
            '"state": "closed"',
            # search proof (search_issues typically returns a numeric result list; using the exact substring)
            '"results": [1]',
            # fetched metadata proving title + labels
            '"title": "Utilities module audit [task_73]"',
            '"labels": ["module-audit"]',
            # terminal audit line from list_terminal_last_message
            '"message": "Issue closed with module-audit label in utils-js [task_73]"',
        ],
    ),

    # 82. (ui-team) Create branch->Commit->Raise PR->Reject via validation->Log
    Task(
        annotator='0',
        user_id="task_82",
        instruction=(
            "You are 'ui-team' and must operate only via the available tools.\n\n"
            "Ensure the final repository state in 'ui-kit' satisfies ALL acceptance criteria below. "
            "Treat these as outcomes/specification—not step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (all must hold):\n"
            "• A branch named 'feature-validate' exists and diverges from 'main' by adding a file at path "
            "'docs/validation.md' whose content is exactly: 'Validation test: head==base should not merge.'.\n"
            "• A commit exists on 'feature-validate' whose message is exactly: 'Add docs/validation.md for merge validation test'.\n"
            "• A pull request #1 exists in repository 'ui-kit' with title 'Validate merge blocking when head==base' and body "
            "'This PR intentionally uses the same branch for head and base to verify merge validation.', where the PR's head "
            "and base are both 'feature-validate'.\n"
            "• An attempt to merge that pull request is rejected with message 'Pull request rejected.' and reason "
            "'head and base branch are the same', and the merged flag is false.\n"
            "• A terminal entry exists with the exact message: 'PR #1 rejected in ui-kit: head equals base (validation).'\n\n"
            "LITERALS TO USE VERBATIM:\n"
            "- repo: ui-kit\n"
            "- source branch: main\n"
            "- working branch: feature-validate\n"
            "- path: docs/validation.md\n"
            "- file content: Validation test: head==base should not merge.\n"
            "- commit message: Add docs/validation.md for merge validation test\n"
            "- PR number: 1\n"
            "- PR title: Validate merge blocking when head==base\n"
            "- PR body: This PR intentionally uses the same branch for head and base to verify merge validation.\n"
            "- terminal message: PR #1 rejected in ui-kit: head equals base (validation).\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "ui-team"}),
            Action(name="get_repository", kwargs={"repo_name": "ui-kit"}),

            Action(name="create_branch", kwargs={
                "repo_name": "ui-kit",
                "source_branch": "main",
                "new_branch": "feature-validate"
            }),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "ui-kit",
                "branch": "feature-validate",
                "path": "docs/validation.md",
                "content": "Validation test: head==base should not merge."
            }),

            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "ui-kit",
                "branch": "feature-validate",
                "commit_message": "Add docs/validation.md for merge validation test"
            }),

            Action(name="create_pull_request", kwargs={
                "repo_name": "ui-kit",
                "title": "Validate merge blocking when head==base",
                "body": "This PR intentionally uses the same branch for head and base to verify merge validation.",
                "base": "feature-validate",
                "head": "feature-validate"
            }),

            Action(name="merge_pull_request", kwargs={
                "repo_name": "ui-kit",
                "pr_number": 1
            }),

            Action(name="append_terminal", kwargs={
                "message": "PR #1 rejected in ui-kit: head equals base (validation)."
            }),
        ],
        outputs=[
            # From merge_pull_request rejection; use boolean "false" to match tool output
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
            "You are 'alice-w' and must operate only via the available tools.\n\n"
            "Ensure the final repository state in 'acme-webapp' satisfies ALL acceptance criteria below. "
            "Treat these as outcomes/specification—not step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (all must hold):\n"
            "• There is an open issue tracking the startup crash with title 'Fix crash on startup' and body "
            "'Application crashes due to missing env var check'.\n"
            "• A branch named 'fix-startup' exists off the default branch and the file src/main.py contains exactly the line: "
            "'assert ENV_VAR is not None'. The change is committed with message 'fix: guard against missing ENV_VAR'.\n"
            "• A pull request exists from 'fix-startup' into the default branch titled 'Fix startup crash' with body "
            "'Adds env var guard clause', and it is merged.\n"
            "• Return the issue metadata and the pull request title in outputs.\n\n"
            "LITERALS TO USE VERBATIM:\n"
            "- repo: acme-webapp\n"
            "- issue title: Fix crash on startup\n"
            "- issue body: Application crashes due to missing env var check\n"
            "- branch: fix-startup\n"
            "- path: src/main.py\n"
            "- code line: assert ENV_VAR is not None\n"
            "- commit message: fix: guard against missing ENV_VAR\n"
            "- PR title: Fix startup crash\n"
            "- PR body: Adds env var guard clause\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),

            Action(name="create_issue", kwargs={
                "repo_name": "acme-webapp",
                "title": "Fix crash on startup",
                "body": "Application crashes due to missing env var check"
            }),

            Action(name="get_default_branch", kwargs={"repo_name": "acme-webapp"}),

            Action(name="create_branch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "fix-startup"
            }),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "fix-startup",
                "path": "src/main.py",
                "content": "assert ENV_VAR is not None"
            }),

            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "fix-startup",
                "commit_message": "fix: guard against missing ENV_VAR"
            }),

            Action(name="create_pull_request", kwargs={
                "repo_name": "acme-webapp",
                "title": "Fix startup crash",
                "body": "Adds env var guard clause",
                "head": "fix-startup",
                "base": "main"
            }),

            Action(name="merge_pull_request", kwargs={
                "repo_name": "acme-webapp",
                "pr_number": 1
            }),

            # Fetch issue metadata for outputs
            Action(name="get_issue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1
            }),
        ],
        outputs=[
            # Keep outputs as substrings that appear in actual tool responses
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
            "You are 'ui-team'. In the repository 'ui-kit', there must be a pull request #11 titled "
            "'Introduce Theme Provider'. Add the exact review comment 'Theme reviewed. [task_74]' on it, "
            "then approve and merge it. Return the PR number, its final state 'merged', "
            "and a terminal entry stating 'PR #11 merged with review in ui-kit [task_74]'."
        ),
        actions=[
            # Identity
            Action(name="get_me", kwargs={"username": "ui-team"}),

            # Retrieve PR
            Action(name="get_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 11}),

            # Approve review (with the required comment)
            Action(
                name="create_pull_request_review",
                kwargs={
                    "repo_name": "ui-kit",
                    "pr_number": 11,
                    "review_decision": "approve",
                    "comment": "Theme reviewed. [task_74]"
                },
            ),

            # Merge PR
            Action(
                name="merge_pull_request",
                kwargs={"repo_name": "ui-kit", "pr_number": 11},
            ),

            # Terminal log
            Action(
                name="append_terminal",
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
            "You are 'backend-core'. You need to complete the tasks on the repository state for 'payments-service' and must satisfy ALL of the "
            "following properties:\n"
            "• A documentation file exists at path 'docs/RETRY_POLICY.md' on 'main' with the EXACT content "
            "'Retries: up to 2 attempts with exponential backoff starting at 250ms. Idempotency required for POST.'.\n"
            "• This change originates on a branch named 'feature-retry-policy' and is represented by a commit whose message is "
            "EXACTLY 'Add retry policy documentation'.\n"
            "• The change is integrated into 'main' via a reviewed pull request titled 'Add retry policy docs'; a review request is made to "
            "'qa-erin', and an approval review containing the exact comment 'LGTM' is recorded.\n"
            "• A release exists with tag 'v0.3.0', title 'Retry policy docs', and body 'Publish retry policy documentation.', and the latest "
            "release reflects tag 'v0.3.0'.\n"
            "• An issue exists titled 'Retry policy published' with body 'Docs merged and released as v0.3.0.' labeled 'documentation'.\n"
            "• The terminal audit log contains the EXACT entry 'payments-service retry policy docs published and released as v0.3.0.'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "backend-core"}),
            Action(name="get_repository", kwargs={"repo_name": "payments-service"}),
            Action(name="create_branch", kwargs={"repo_name": "payments-service", "source_branch": "main", "new_branch": "feature-retry-policy"}),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "payments-service",
                "branch": "feature-retry-policy",
                "path": "docs/RETRY_POLICY.md",
                "content": "Retries: up to 2 attempts with exponential backoff starting at 250ms. Idempotency required for POST."
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "payments-service",
                "branch": "feature-retry-policy",
                "commit_message": "Add retry policy documentation"
            }),
            Action(name="create_pull_request", kwargs={
                "repo_name": "payments-service",
                "title": "Add retry policy docs",
                "base": "main",
                "head": "feature-retry-policy"
            }),
            Action(name="request_pull_request_reviewers", kwargs={
                "repo_name": "payments-service",
                "pr_number": 1,
                "reviewers": ["qa-erin"]
            }),
            Action(name="create_pull_request_review", kwargs={
                "repo_name": "payments-service",
                "pr_number": 1,
                "review_decision": "approve",
                "comment": "LGTM"
            }),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 1}),
            Action(name="create_release", kwargs={
                "repo_name": "payments-service",
                "tag": "v0.3.0",
                "title": "Retry policy docs",
                "body": "Publish retry policy documentation."
            }),
            Action(name="get_latest_release", kwargs={"repo_name": "payments-service"}),
            Action(name="create_issue", kwargs={
                "repo_name": "payments-service",
                "title": "Retry policy published",
                "body": "Docs merged and released as v0.3.0.",
                "labels": ["documentation"]
            }),
            Action(name="append_terminal", kwargs={
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
            "You are 'devops-lead'. In 'k8s-monitoring', confirm default branch and just list commits of branch 'upgrade-prometheus'."
            "Check open alerts by listing them (ensure Alert #45 remains open), then create an issue titled 'Harden TLS for Prometheus scrape' with labels ['security','prometheus'] "
            "and body: 'Alert #45 still open after v2.45.0 upgrade; enforce modern ciphers and TLS versions.'. "
            "Append terminal: 'k8s-monitoring TLS hardening tracked post-upgrade'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "devops-lead"}),
            Action(name="get_repository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="get_default_branch", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="list_commits", kwargs={"repo_name": "k8s-monitoring", "branch": "upgrade-prometheus"}),
            Action(name="list_code_scanning_alerts", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="create_issue", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Harden TLS for Prometheus scrape",
                "body": "Alert #45 still open after v2.45.0 upgrade; enforce modern ciphers and TLS versions.",
                "labels": ["security", "prometheus"],
            }),
            Action(name="append_terminal", kwargs={"message": "k8s-monitoring TLS hardening tracked post-upgrade"}),
        ],
        outputs=['"message": "k8s-monitoring TLS hardening tracked post-upgrade"'],
    ),

    # 84
    Task(
        annotator='0',
        user_id="task_84",
        instruction=(
            "You are 'backend-core'. In 'payments-service', align PR #21 with Issue #13 (3DS). "
            "Review repo, the issue and PR, and list current code scanning alerts. "
            "Label Issue #13 with 'needs-tests', comment: 'PR #21 implements 3DS; add unit tests for fallback coverage before merge.', "
            "and leave a PR review to 'request_changes' with comment: 'Please include unit tests for 3DS fallback flows.'. "
            "Append terminal: 'payments-service 3DS alignment and test gating noted'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "backend-core"}),
            Action(name="get_repository", kwargs={"repo_name": "payments-service"}),
            Action(name="get_issue", kwargs={"repo_name": "payments-service", "issue_number": 13}),
            Action(name="get_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 21}),
            Action(name="list_code_scanning_alerts", kwargs={"repo_name": "payments-service"}),
            Action(name="add_label_to_issue", kwargs={"repo_name": "payments-service", "issue_number": 13, "label": "needs-tests"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "payments-service", "issue_number": 13, "comment": "PR #21 implements 3DS; add unit tests for fallback coverage before merge."}),
            Action(
                name="create_pull_request_review",
                kwargs={
                    "repo_name": "payments-service",
                    "pr_number": 21,
                    "review_decision": "request_changes",
                    "comment": "Please include unit tests for 3DS fallback flows."
                },
            ),
            Action(name="append_terminal", kwargs={"message": "payments-service 3DS alignment and test gating noted"}),
        ],
        outputs=['"message": "payments-service 3DS alignment and test gating noted"'],
    ),

    # 60
    Task(
        annotator='0',
        user_id="task_60",
        instruction=(
            "You are 'ui-team'. After you complete the task, the repository state for 'ui-kit' must satisfy ALL of the following properties:\n"
            "• A documentation file exists at path 'docs/ACCESSIBILITY.md' with the EXACT content "
            "'All UI components must meet WCAG 2.1 AA. Provide ARIA labels for interactive elements. Keyboard navigation required.'.\n"
            "• This change originates on a branch named 'feature-accessibility-docs' and is represented by a commit whose message is "
            "EXACTLY 'Add accessibility documentation'.\n"
            "• The change is merged into 'main' via a reviewed pull request titled 'Accessibility docs'; a review request is made to "
            "'design-lead', and an approval review with the exact comment 'Approved for accessibility' is recorded.\n"
            "• The repository has the topic 'accessibility'.\n"
            "• A release exists with tag 'v2.0.0', title 'Accessibility docs', and body 'Add accessibility documentation.', and the latest "
            "release reflects tag 'v2.0.0'.\n"
            "• An issue exists titled 'Accessibility docs published' with body 'Docs merged and released as v2.0.0.' labeled 'documentation'.\n"
            "• The terminal audit log contains the EXACT entry 'ui-kit accessibility docs published and released as v2.0.0.'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "ui-team"}),
            Action(name="get_repository", kwargs={"repo_name": "ui-kit"}),
            Action(name="create_branch", kwargs={"repo_name": "ui-kit", "source_branch": "main", "new_branch": "feature-accessibility-docs"}),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "ui-kit",
                "branch": "feature-accessibility-docs",
                "path": "docs/ACCESSIBILITY.md",
                "content": "All UI components must meet WCAG 2.1 AA. Provide ARIA labels for interactive elements. Keyboard navigation required."
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "ui-kit",
                "branch": "feature-accessibility-docs",
                "commit_message": "Add accessibility documentation"
            }),
            Action(name="create_pull_request", kwargs={
                "repo_name": "ui-kit",
                "title": "Accessibility docs",
                "base": "main",
                "head": "feature-accessibility-docs"
            }),
            Action(name="request_pull_request_reviewers", kwargs={
                "repo_name": "ui-kit",
                "pr_number": 1,
                "reviewers": ["design-lead"]
            }),
            Action(name="create_pull_request_review", kwargs={
                "repo_name": "ui-kit",
                "pr_number": 1,
                "review_decision": "approve",
                "comment": "Approved for accessibility"
            }),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 1}),
            Action(name="add_repo_topic", kwargs={"repo_name": "ui-kit", "topic": "accessibility"}),
            Action(name="create_release", kwargs={
                "repo_name": "ui-kit",
                "tag": "v2.0.0",
                "title": "Accessibility docs",
                "body": "Add accessibility documentation."
            }),
            Action(name="get_latest_release", kwargs={"repo_name": "ui-kit"}),
            Action(name="create_issue", kwargs={
                "repo_name": "ui-kit",
                "title": "Accessibility docs published",
                "body": "Docs merged and released as v2.0.0.",
                "labels": ["documentation"]
            }),
            Action(name="append_terminal", kwargs={"message": "ui-kit accessibility docs published and released as v2.0.0."}),
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

    # 34 (alice-w) acme-webapp: create & triage an issue, then log closure
    Task(
        annotator='0',
        user_id="task_34",
        instruction=(
            "You are 'alice-w' and must operate only through the available tools.\n\n"
            "YOUR GOAL\n"
            "• In repository 'acme-webapp', create an issue using the exact title and body literals, add the exact label literal,\n"
            "  post the exact comment literal, close the issue, and ensure the most recent terminal entry equals the exact message literal.\n\n"
            "LITERALS (use verbatim)\n"
            "- repo: acme-webapp\n"
            "- issue title: CI gate: add test matrix\n"
            "- issue body: Add unit + integration test matrix\n"
            "- label to add: ready-for-ci\n"
            "- comment to post: Triage complete: scheduled for CI gate\n"
            "- terminal message: Issue #1 closed in acme-webapp: ready-for-ci triage complete\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),

            # Write: create issue, label it, comment, and close it
            Action(name="create_issue", kwargs={
                "repo_name": "acme-webapp",
                "title": "CI gate: add test matrix",
                "body": "Add unit + integration test matrix"
            }),
            Action(name="add_label_to_issue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "label": "ready-for-ci"
            }),
            Action(name="add_issue_comment", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "comment": "Triage complete: scheduled for CI gate"
            }),
            Action(name="update_issue", kwargs={
                "repo_name": "acme-webapp",
                "issue_number": 1,
                "state": "closed"
            }),

            # Write: append terminal confirmation and verify it's the latest
            Action(name="append_terminal", kwargs={
                "message": "Issue #1 closed in acme-webapp: ready-for-ci triage complete"
            }),
            Action(name="list_terminal_last_message", kwargs={}),
        ],
        outputs=[
            '"message": "Issue created", "number": 1',
            '"message": "Label \'ready-for-ci\' added."',
            '"entries": {"printed_ts": "2025-08-21T12:00:00Z", "message": "Issue #1 closed in acme-webapp: ready-for-ci triage complete"}',
        ],
    ),

    # 91. (security-team) Reduce XSS false positives → PR merged → issue closed → release + comment
    Task(
        annotator='0',
        user_id="task_91",
        instruction=(
            "You are 'security-team' working in repository 'security-scanner'. Deliver an XSS rule adjustment such that, "
            "after completion, the repository state satisfies ALL acceptance criteria below while using the exact constants provided. "
            "Treat this as a specification of outcomes and literals, NOT step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (final state must reflect all of these):\n"
            "• A feature branch exists that contains a relaxed XSS rule to reduce false positives on template literals.\n"
            "• Issue number 5 is closed.\n"
            "• A pull request (number 1 after reset for this repo) is merged into the default branch.\n"
            "• A release with the exact tag below exists.\n"
            "• The closed issue contains the exact post-release comment.\n\n"
            "CONSTANTS TO USE VERBATIM (all literals must match exactly):\n"
            "- Feature branch name: fix-xss-false-positives\n"
            "- Base branch name: main\n"
            "- File path: rules/xss/relaxed-template-rule.yml\n"
            "- File content (exact; SINGLE trailing newline only):\n"
            "id: xss-template-relaxed\nseverity: medium\npattern: disallow-unsafe-innerHTML\nallow_template_literals: true\n"
            "- Commit message: fix(xss): relax rule for template literals to reduce false positives\n"
            "- Issue to label and close: 5\n"
            "- Label to add: xss\n"
            "- Pre-PR issue comment: Relaxing XSS rule for template literals; PR will close this issue.\n"
            "- PR title: Relax XSS rule to reduce false positives on template literals\n"
            "- PR body: Closes #5\n"
            "- Pull request review decision: approve\n"
            "- Release tag: v1.3.1-xss-fp\n"
            "- Post-release issue comment: Fixed in 'v1.3.1-xss-fp' (reduced false positives)\n"
        ),
        actions=[
            # Auth & repo context
            Action(name="get_me", kwargs={"username": "security-team"}),
            Action(name="get_repository", kwargs={"repo_name": "security-scanner"}),
            Action(name="get_default_branch", kwargs={"repo_name": "security-scanner"}),
            Action(name="get_head_sha", kwargs={"repo_name": "security-scanner", "branch": "main"}),

            # Feature branch
            Action(name="create_branch", kwargs={"repo_name": "security-scanner", "new_branch": "fix-xss-false-positives", "source_branch": "main"}),

            # Change set on feature branch
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "security-scanner",
                "branch": "fix-xss-false-positives",
                "path": "rules/xss/relaxed-template-rule.yml",
                "content": "id: xss-template-relaxed\nseverity: medium\npattern: disallow-unsafe-innerHTML\nallow_template_literals: true\n",
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "security-scanner",
                "branch": "fix-xss-false-positives",
                "commit_message": "fix(xss): relax rule for template literals to reduce false positives",
            }),

            # Work existing issue #5 deterministically
            Action(name="add_label_to_issue", kwargs={"repo_name": "security-scanner", "issue_number": 5, "label": "xss"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "security-scanner", "issue_number": 5, "comment": "Relaxing XSS rule for template literals; PR will close this issue."}),

            # PR from feature → main
            Action(name="create_pull_request", kwargs={
                "repo_name": "security-scanner",
                "title": "Relax XSS rule to reduce false positives on template literals",
                "body": "Closes #5",
                "head": "fix-xss-false-positives",
                "base": "main",
            }),
            Action(name="create_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 1}),

            # Close the issue explicitly
            Action(name="update_issue", kwargs={"repo_name": "security-scanner", "issue_number": 5, "state": "closed"}),

            # Release & annotate the issue
            Action(name="create_release", kwargs={"repo_name": "security-scanner", "tag": "v1.3.1-xss-fp"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "security-scanner", "issue_number": 5, "comment": "Fixed in 'v1.3.1-xss-fp' (reduced false positives)"}),
        ],
        outputs=[
            '"repo_name": "security-scanner"',
            '"pr_number": 1, "closed_issue": 5, "release_tag": "v1.3.1-xss-fp"',
        ],
    ),










































    # 01. (ui-team) Protect main and record an audit entry (no redundant calls)
    Task(
        annotator='0',
        user_id="task_01",
        instruction=(
            "You are 'ui-team'. Ensure the 'main' branch of 'ui-kit' is protected and confirm its protection status. "
            "Record the change by opening an audit issue titled 'Protect main branch' with body "
            "'Branch protection for main enabled.' and label 'ops', and write the exact terminal entry "
            "'Branch main protection enabled in ui-kit.'"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "ui-team"}),
            Action(name="get_repository", kwargs={"repo_name": "ui-kit"}),
            Action(name="get_default_branch", kwargs={"repo_name": "ui-kit"}),
            Action(name="set_branch_protection", kwargs={"repo_name": "ui-kit", "branch": "main", "protected": True}),
            Action(name="get_branch_protection", kwargs={"repo_name": "ui-kit", "branch": "main"}),
            Action(
                name="create_issue",
                kwargs={
                    "repo_name": "ui-kit",
                    "title": "Protect main branch",
                    "body": "Branch protection for main enabled.",
                    "labels": ["ops"],
                },
            ),
            Action(name="append_terminal", kwargs={"message": "Branch main protection enabled in ui-kit."}),
        ],
        outputs=[
            '"message": "Branch protection enabled.", "repo_name": "ui-kit", "branch": "main", "protected": true',
        ],
    ),

    # 02. (security-team) Publish a specific release and confirm; also capture an audit trail
    Task(
        annotator='0',
        user_id="task_02",
        instruction=(
            "You are 'security-team'. Publish a release in 'security-scanner' with tag 'v0.4.0', title 'Performance release', "
            "and body 'Performance optimizations and SARIF format support.' Then confirm the latest release. "
            "Record an audit by opening an issue titled 'Release v0.4.0 created' with body 'Release published successfully.' "
            "labeled 'release', and write the exact terminal entry 'security-scanner v0.4.0 released.'"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "security-team"}),
            Action(name="get_repository", kwargs={"repo_name": "security-scanner"}),
            Action(
                name="create_release",
                kwargs={
                    "repo_name": "security-scanner",
                    "tag": "v0.4.0",
                    "title": "Performance release",
                    "body": "Performance optimizations and SARIF format support.",
                },
            ),
            Action(name="get_latest_release", kwargs={"repo_name": "security-scanner"}),
            Action(
                name="create_issue",
                kwargs={
                    "repo_name": "security-scanner",
                    "title": "Release v0.4.0 created",
                    "body": "Release published successfully.",
                    "labels": ["release"],
                },
            ),
            Action(name="append_terminal", kwargs={"message": "security-scanner v0.4.0 released."}),
        ],
        outputs=[
            '"message": "Release created.", "repo_name": "security-scanner", "tag_name": "v0.4.0", "title": "Performance release"',
            '"tag_name": "v0.4.0", "title": "Performance release"',
        ],
    ),

    # 03. (backend-core) Summarize alerts, create a deterministic tracking issue, log, and list by label
    Task(
        annotator='0',
        user_id="task_03",
        instruction=(
            "You are 'backend-core'. Produce an auditable security snapshot for 'payments-service' that results in: "
            "• a new issue titled 'Security alerts summary' with body 'Tracking current code scanning findings and severities.' labeled 'security'; "
            "• the terminal log containing exactly this entry:\n"
            "{\"message\": \"Alerts retrieved.\", \"repo_name\": \"payments-service\", \"alert_count\": 1, \"alert_numbers\": [7], \"severities\": [\"high\"]}\n"
            "and the outcome must reflect the current code scanning alert summary fields."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "backend-core"}),
            Action(name="get_repository", kwargs={"repo_name": "payments-service"}),
            Action(name="list_code_scanning_alerts", kwargs={"repo_name": "payments-service"}),
            Action(
                name="create_issue",
                kwargs={
                    "repo_name": "payments-service",
                    "title": "Security alerts summary",
                    "body": "Tracking current code scanning findings and severities.",
                    "labels": ["security"],
                },
            ),
            Action(
                name="append_terminal",
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
            "You are 'devops-lead'. In the 'k8s-monitoring' repository, list all code scanning alerts "
            "to the terminal. Then, create an issue titled 'Track code scanning alerts' with body 'Investigating code scanning alerts for identified issue numbers' "
            "and labels ['code-scan', 'security', 'infrastructure']. Finally, log a terminal message confirming issue creation."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "devops-lead"}),
            Action(name="get_repository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="list_code_scanning_alerts", kwargs={"repo_name": "k8s-monitoring"}),
            Action(
                name="append_terminal",
                kwargs={
                    "message": '{"message": "Code alerts retrieved.", "repo_name": "k8s-monitoring", "alert_count": 3, "alert_numbers": [42, 45, 48], "severities": ["high", "medium", "low"]}'
                },
            ),
            Action(
                name="create_issue",
                kwargs={
                    "repo_name": "k8s-monitoring",
                    "title": "Track code scanning alerts",
                    "body": "Investigating code scanning alerts for identified issue numbers",
                    "labels": ["code-scan", "security", "infrastructure"],
                },
            ),
            # Action(name="get_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 1}),
            Action(
                name="append_terminal",
                kwargs={
                    "message": "Issue #1 created to track code scanning alerts in k8s-monitoring."
                },
            ),
        ],
        outputs=[
            "'message': '{'message': 'Code alerts retrieved.', 'repo_name': 'k8s-monitoring', 'alert_count': 3, 'alert_numbers': [42, 45, 48], 'severities': ['high', 'medium', 'low']}",
            "Issue #1 created to track code scanning alerts in k8s-monitoring.",
        ],
    ),

    # 06. (devops-lead) Audit merged PRs across key repos and log changed files
    Task(
        annotator='0',
        user_id="task_06",
        instruction=(
            "You are 'devops-lead'. Review all merged pull requests across the following repositories: "
            "'acme-webapp', 'utils-js', 'nlp-models', 'security-scanner', 'flutter-finance-app', "
            "'react-dashboard', and 'k8s-monitoring'. For each merged PR, extract the list of changed files "
            "and record a terminal audit entry in the format: "
            "'Merged PR #{number} in {repo_name}: {comma-separated list of files}'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "devops-lead"}),
            Action(name="list_pull_requests", kwargs={"repo_name": "acme-webapp"}),
            Action(name="list_pull_requests", kwargs={"repo_name": "utils-js"}),
            Action(name="list_pull_requests", kwargs={"repo_name": "nlp-models"}),
            Action(name="list_pull_requests", kwargs={"repo_name": "security-scanner"}),
            Action(name="list_pull_requests", kwargs={"repo_name": "flutter-finance-app"}),
            Action(name="list_pull_requests", kwargs={"repo_name": "react-dashboard"}),
            Action(name="list_pull_requests", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="append_terminal", kwargs={"message": "Merged PR #7 in acme-webapp: src/logger.py"}),
            Action(name="append_terminal", kwargs={"message": "Merged PR #16 in utils-js: src/utils/format.js, test/format.test.js"}),
            Action(name="append_terminal", kwargs={"message": "Merged PR #22 in nlp-models: src/evaluation.py, scripts/checkpoint.py"}),
            Action(name="append_terminal", kwargs={"message": "Merged PR #23 in security-scanner: src/cache.rs, src/scanner.rs, Cargo.toml"}),
            Action(name="append_terminal", kwargs={"message": "Merged PR #24 in flutter-finance-app: lib/theme/dark_theme.dart, lib/main.dart, pubspec.yaml"}),
            Action(name="append_terminal", kwargs={"message": "Merged PR #30 in react-dashboard: src/styles/global.css, src/theme/dark.css, src/hooks/useTheme.ts"}),
            Action(name="append_terminal", kwargs={"message": "Merged PR #32 in k8s-monitoring: kubernetes/alertmanager.yaml, config/alertmanager.yml, docker-compose.yml"}),
            Action(name="append_terminal", kwargs={"message": "Merged PR #34 in k8s-monitoring: kubernetes/prometheus.yaml, config/prometheus.yml, docs/MONITORING.md"}),
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

    # 07. (backend-core) Collect commit history and author frequencies for payments-service
    Task(
        annotator='0',
        user_id="task_07",
        instruction=(
            "You are 'backend-core'. From the repository 'payments-service', collect the complete commit history and "
            "extract commit authors with their frequencies. Use the full history and also inspect the 'main' branch "
            "for branch-level counts. Record the audit by creating an issue titled 'Commit authors frequency audit' "
            "with body 'Collected authors and commit counts from full history and main branch.' and label 'audit', "
            "and write the terminal entry 'Authors frequency audit for payments-service completed'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "backend-core"}),
            # Ground repository context owned by backend-core
            Action(name="search_repositories", kwargs={"owner": "backend-core"}),
            # Retrieve commit history (full + per-branch) to derive author frequencies externally
            Action(name="list_commits", kwargs={"repo_name": "payments-service"}),
            Action(name="list_commits", kwargs={"repo_name": "payments-service", "branch": "main"}),
            # Record audit artifacts
            Action(
                name="create_issue",
                kwargs={
                    "repo_name": "payments-service",
                    "title": "Commit authors frequency audit",
                    "body": "Collected authors and commit counts from full history and main branch.",
                    "labels": ["audit"],
                },
            ),
            Action(name="append_terminal", kwargs={"message": "Authors frequency audit for payments-service completed"}),
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
            "You are 'intern-sarah'. In 'portfolio-site', open an accessibility audit task after the last update. "
            "Verify repository content, then create an issue 'Accessibility audit (WCAG)' with label 'a11y' and body "
            "'Run Lighthouse + manual checks for keyboard navigation and color contrast.' "
            "Append terminal: 'portfolio-site accessibility audit opened'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "intern-sarah"}),
            Action(name="get_repository", kwargs={"repo_name": "portfolio-site"}),
            Action(name="list_files", kwargs={"repo_name": "portfolio-site", "branch": "main"}),
            Action(name="create_issue", kwargs={
                "repo_name": "portfolio-site",
                "title": "Accessibility audit (WCAG)",
                "body": "Run Lighthouse + manual checks for keyboard navigation and color contrast.",
                "labels": ["a11y"],
            }),
            Action(name="append_terminal", kwargs={"message": "portfolio-site accessibility audit opened"}),
        ],
        outputs=['"message": "portfolio-site accessibility audit opened"'],
    ),

    # 10
    Task(
        annotator='0',
        user_id="task_10",
        instruction=(
            "You are 'alice-w'. In 'acme-webapp', list current alerts and branches, inspect 'feature-update' files, "
            "and open an issue titled 'Post-merge security sweep' with labels ['security','audit'] and body: "
            "'Review SQLi alert and ensure tests and sanitization on main.' "
            "Append terminal: 'acme-webapp post-merge security sweep initiated'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            # Action(name="get_repository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="list_code_scanning_alerts", kwargs={"repo_name": "acme-webapp"}),
            Action(name="list_branches", kwargs={"repo_name": "acme-webapp"}),
            Action(name="list_files", kwargs={"repo_name": "acme-webapp", "branch": "feature-update"}),
            Action(name="create_issue", kwargs={
                "repo_name": "acme-webapp",
                "title": "Post-merge security sweep",
                "body": "Review SQLi alert and ensure tests and sanitization on main.",
                "labels": ["security", "audit"],
            }),
            Action(name="append_terminal", kwargs={"message": "acme-webapp post-merge security sweep initiated"}),
        ],
        outputs=['"message": "acme-webapp post-merge security sweep initiated"'],
    ),

    # 11
    Task(
        annotator='0',
        user_id="task_11",
        instruction=(
            "You are 'devops-lead'. For 'k8s-monitoring', you need to check merged PRs #32 and #34, then list commits on 'feature-alertmanager', "
            "and leave a terminal note that upgrade and alerting configuration are verified together."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "devops-lead"}),
            Action(name="get_repository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="get_pull_request", kwargs={"repo_name": "k8s-monitoring", "pr_number": 32}),
            Action(name="get_pull_request", kwargs={"repo_name": "k8s-monitoring", "pr_number": 34}),
            Action(name="list_commits", kwargs={"repo_name": "k8s-monitoring", "branch": "feature-alertmanager"}),
            Action(name="append_terminal", kwargs={"message": "k8s-monitoring merged PRs verified: alertmanager + prometheus upgrade"}),
        ],
        outputs=['"message": "k8s-monitoring merged PRs verified: alertmanager + prometheus upgrade"'],
    ),

    # 12
    Task(
        annotator='0',
        user_id="task_12",
        instruction=(
            "You are 'frontend-dev'. In 'react-dashboard', list open PRs, inspect conflicted PR #28, "
            "and comment on Issue #25 with this message: 'Plan: add useEffect cleanup + ws close on unmount; verify heap snapshots.' "
            "Append terminal: 'react-dashboard memory leak investigation planned'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "frontend-dev"}),
            Action(name="get_repository", kwargs={"repo_name": "react-dashboard"}),
            Action(name="list_open_pull_requests", kwargs={"repo_name": "react-dashboard"}),
            Action(name="get_pull_request", kwargs={"repo_name": "react-dashboard", "pr_number": 28}),
            Action(
                name="add_issue_comment",
                kwargs={
                    "repo_name": "react-dashboard",
                    "issue_number": 25,
                    "comment": "Plan: add useEffect cleanup + ws close on unmount; verify heap snapshots.",
                },
            ),

            Action(name="append_terminal", kwargs={"message": "react-dashboard memory leak investigation planned"}),
        ],
        outputs=['"message": "react-dashboard memory leak investigation planned"'],
    ),

    # 13 (alice-w) Triage a single issue with label + comment and close it
    Task(
        annotator='0',
        user_id="task_13",
        instruction=(
            "You are 'alice-w' working in repository 'acme-webapp'. Ensure the final repository state satisfies ALL acceptance "
            "criteria below, using the exact literals provided. Treat this as outcomes/specification, not step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (must all hold in the end):\n"
            "• Issue #3 has the label: triage-urgent\n"
            "• Issue #3 state is exactly: closed\n"
            "• Issue #3 contains the exact new comment: Labels applied: triage-urgent, quality.\n\n"
            "LITERALS TO USE VERBATIM:\n"
            "- repo: acme-webapp\n"
            "- issue number: 3\n"
            "- label: triage-urgent\n"
            "- comment: Labels applied: triage-urgent, quality.\n"
            "- closed state literal: closed\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="add_label_to_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "label": "triage-urgent"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "comment": "Labels applied: triage-urgent, quality."}),
            Action(name="update_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "state": "closed"}),
        ],
        outputs=[
            '"message": "Label \'triage-urgent\' added."',
            '"message": "Comment added."',
            '"message": "Issue updated", "number": 3, "state": "closed"',
        ],
    ),

    # 14 (bob-dev) utils-js: label + comment + close one issue (outputs mirror tool returns)
    Task(
        annotator='0',
        user_id="task_14",
        instruction=(
            "You are 'bob-dev' working in repository 'utils-js'. Ensure the final state satisfies ALL acceptance criteria below, "
            "treating this as a specification (not step-by-step guidance).\n\n"
            "ACCEPTANCE CRITERIA:\n"
            "• Issue #4 has the label: needs-triage\n"
            "• Issue #4 contains the exact new comment: Triaged and scheduled for next minor.\n"
            "• Issue #4 state is exactly: closed\n\n"
            "LITERALS TO USE VERBATIM:\n"
            "- repo: utils-js\n"
            "- issue number: 4\n"
            "- label: needs-triage\n"
            "- comment: Triaged and scheduled for next minor.\n"
            "- closed state literal: closed\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "bob-dev"}),
            Action(name="get_repository", kwargs={"repo_name": "utils-js"}),

            Action(name="add_label_to_issue", kwargs={"repo_name": "utils-js", "issue_number": 4, "label": "needs-triage"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "utils-js", "issue_number": 4, "comment": "Triaged and scheduled for next minor."}),
            Action(name="update_issue", kwargs={"repo_name": "utils-js", "issue_number": 4, "state": "closed"}),
        ],
        outputs=[
            '"message": "Label \'needs-triage\' added."',
            '"message": "Comment added."',
            '"message": "Issue updated", "number": 4, "state": "closed"',
        ],
    ),

    # 15 (frontend-dev) react-dashboard: label + comment + close one issue (outputs mirror tool returns)
    Task(
        annotator='0',
        user_id="task_15",
        instruction=(
            "You are 'frontend-dev' working in repository 'react-dashboard'. Ensure the final state satisfies ALL acceptance criteria below, "
            "treating this as a specification (not step-by-step guidance).\n\n"
            "ACCEPTANCE CRITERIA:\n"
            "• Issue #25 has the label: investigate\n"
            "• Issue #25 contains the exact new comment: Triaged; assigning to next sprint.\n"
            "• Issue #25 state is exactly: closed\n\n"
            "LITERALS TO USE VERBATIM:\n"
            "- repo: react-dashboard\n"
            "- issue number: 25\n"
            "- label: investigate\n"
            "- comment: Triaged; assigning to next sprint.\n"
            "- closed state literal: closed\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "frontend-dev"}),
            Action(name="get_repository", kwargs={"repo_name": "react-dashboard"}),

            Action(name="add_label_to_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "label": "investigate"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "comment": "Triaged; assigning to next sprint."}),
            Action(name="update_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "state": "closed"}),
        ],
        outputs=[
            '"message": "Label \'investigate\' added."',
            '"message": "Comment added."',
            '"message": "Issue updated", "number": 25, "state": "closed"',
        ],
    ),

    # 16 (nlp-labs) nlp-models: label + comment + close one issue
    Task(
        annotator='0',
        user_id="task_16",
        instruction=(
            "You are 'nlp-labs' working in repository 'nlp-models'. Ensure the final state satisfies ALL acceptance criteria below, "
            "treating this as a specification (not step-by-step guidance).\n\n"
            "ACCEPTANCE CRITERIA:\n"
            "• Issue #12 has the label: investigate-oom\n"
            "• Issue #12 contains the exact new comment: Initial triage: OOM under training; mitigation underway.\n"
            "• Issue #12 state is exactly: closed\n\n"
            "LITERALS TO USE VERBATIM:\n"
            "- repo: nlp-models\n"
            "- issue number: 12\n"
            "- label: investigate-oom\n"
            "- comment: Initial triage: OOM under training; mitigation underway.\n"
            "- closed state literal: closed\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "nlp-labs"}),
            Action(name="get_repository", kwargs={"repo_name": "nlp-models"}),

            Action(name="add_label_to_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "label": "investigate-oom"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "nlp-models", "issue_number": 12, "comment": "Initial triage: OOM under training; mitigation underway."}),
            Action(name="update_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "state": "closed"}),
        ],
        outputs=[
            '"message": "Label \'investigate-oom\' added."',
            '"message": "Comment added."',
            '"message": "Issue updated", "number": 12, "state": "closed"',
        ],
    ),

    # 17 (alice-w) acme-webapp: add topic; confirm last terminal entry
    Task(
        annotator='0',
        user_id="task_17",
        instruction=(
            "You are 'alice-w' and must operate only through the available tools.\n\n"
            "YOUR GOAL\n"
            "• In repository 'acme-webapp', ensure the repository topics include the exact topic literal below.\n"
            "• Ensure the most recent terminal entry is exactly the message literal below (including the branch name).\n\n"
            "LITERALS (use verbatim)\n"
            "- repo: acme-webapp\n"
            "- topic to add: quality-gates\n"
            "- terminal message: Topic updated: quality-gates added to acme-webapp on branch main\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="get_repository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="get_default_branch", kwargs={"repo_name": "acme-webapp"}),

            Action(name="add_repo_topic", kwargs={"repo_name": "acme-webapp", "topic": "quality-gates"}),
            Action(name="list_repo_topics", kwargs={"repo_name": "acme-webapp"}),

            Action(name="append_terminal", kwargs={"message": "Topic updated: quality-gates added to acme-webapp on branch main"}),
            Action(name="list_terminal_last_message", kwargs={}),
        ],
        outputs=[
            '"message": "Topic \'quality-gates\' added."',
            '"entries": {"printed_ts": "2025-08-21T12:00:00Z", "message": "Topic updated: quality-gates added to acme-webapp on branch main"}',
        ],
    ),

    # 18 (alice-w) acme-webapp: rename, set private, add topic, verify listings, log confirmation
    Task(
        annotator='0',
        user_id="task_18",
        instruction=(
            "You are 'alice-w' and must operate only through the available tools.\n\n"
            "YOUR GOAL\n"
            "• Rename repository 'acme-webapp' to the exact new name literal.\n"
            "• Set the renamed repository's visibility to the exact value literal.\n"
            "• Add the exact topic literal to the renamed repository and verify topics.\n"
            "• Verify that your owned repositories list includes the renamed repository.\n"
            "• Ensure the most recent terminal entry equals the exact message literal.\n\n"
            "LITERALS (use verbatim)\n"
            "- old repo name: acme-webapp\n"
            "- new repo name: acme-webapp-qa\n"
            "- visibility: private\n"
            "- topic to add: qa-ready\n"
            "- terminal message: Repository acme-webapp renamed to acme-webapp-qa and set private; topic qa-ready added\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),

            # Rename, set visibility, and add topic to the renamed repo
            Action(name="rename_repository", kwargs={"old_name": "acme-webapp", "new_name": "acme-webapp-qa"}),
            Action(name="set_repository_visibility", kwargs={"repo_name": "acme-webapp-qa", "visibility": "private"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "acme-webapp-qa", "topic": "qa-ready"}),

            # Read-backs required by acceptance criteria
            Action(name="list_repo_topics", kwargs={"repo_name": "acme-webapp-qa"}),
            Action(name="list_repositories", kwargs={}),

            # Write confirmation to terminal and verify last entry
            Action(name="append_terminal", kwargs={
                "message": "Repository acme-webapp renamed to acme-webapp-qa and set private; topic qa-ready added"
            }),
            Action(name="list_terminal_last_message", kwargs={}),
        ],
        outputs=[
            '"message": "Repository renamed", "new_name": "acme-webapp-qa"',
            '"message": "Visibility updated", "repo_name": "acme-webapp-qa", "visibility": "private"',
            '"message": "Topic \'qa-ready\' added."',
            '"entries": {"printed_ts": "2025-08-21T12:00:00Z", "message": "Repository acme-webapp renamed to acme-webapp-qa and set private; topic qa-ready added"}',
        ],
    ),

    # 19 (alice-w) acme-webapp: enable branch protection and log confirmation
    Task(
        annotator='0',
        user_id="task_19",
        instruction=(
            "You are 'alice-w' and you must operate only through the available tools.\n\n"
            "DO THIS\n"
            "• Set branch protection on the default branch of repository 'acme-webapp' using the exact rule literal.\n"
            "• Verify protection is enabled for that branch.\n"
            "• Append the exact terminal message literal and ensure it is the most recent entry.\n\n"
            "LITERALS (use verbatim)\n"
            "- repo: acme-webapp\n"
            "- branch literal: main\n"
            "- protected flag: 'true'\n"
            "- rules object: {\"require_code_owner_reviews\": True}\n"
            "- terminal message: Branch protection enabled on acme-webapp main\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="get_default_branch", kwargs={"repo_name": "acme-webapp"}),

            # ✅ boolean true (not string)
            Action(
                name="set_branch_protection",
                kwargs={
                    "repo_name": "acme-webapp",
                    "branch": "main",
                    "protected": "true",
                    "rules": {"require_code_owner_reviews": True},
                },
            ),

            Action(name="get_branch_protection", kwargs={"repo_name": "acme-webapp", "branch": "main"}),
            Action(name="append_terminal", kwargs={"message": "Branch protection enabled on acme-webapp main"}),
            Action(name="list_terminal_last_message", kwargs={}),
        ],
        outputs=[
            # from set_branch_protection
            '"message": "Branch protection enabled."',

            # from list_terminal_last_message
            '"timestamp": "2025-08-21T12:00:00Z", "message": "Branch protection enabled on acme-webapp main"',
        ],
    ),

    # 21
    Task(
        annotator='0',
        user_id="task_21",
        instruction=(
            "You are 'ui-team'. Review open PRs in 'ui-kit', comment twice on PR #11 with feedback 'Looks great overall!'and 'Can we optimize the load time?', "
            "fetch PR #12 details, label issue #6 as 'reviewed', and record your review in the terminal."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "ui-team"}),
            Action(name="get_repository", kwargs={"repo_name": "ui-kit"}),
            Action(name="list_open_pull_requests", kwargs={"repo_name": "ui-kit"}),
            Action(name="comment_on_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 11, "comment": "Looks great overall!"}),
            Action(name="comment_on_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 11, "comment": "Can we optimize the load time?"}),
            Action(name="get_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 12}),
            Action(name="add_label_to_issue", kwargs={"repo_name": "ui-kit", "issue_number": 6, "label": "reviewed"}),
            Action(name="append_terminal", kwargs={"message": "PR #11 reviewed and issue #6 labeled as reviewed."}),
        ],
        outputs=[
            '"message": "PR #11 reviewed and issue #6 labeled as reviewed."'
        ],
    ),

    # 22
    Task(
        annotator='0',
        user_id="task_22",
        instruction=(
            "You are 'devops-lead' auditing merged pull requests in 'k8s-monitoring'. "
            "For each merged PR, return the list of changed files and commit authors. "
            "PR #32 was merged from the branch 'feature-alertmanager' and PR #34 from 'upgrade-prometheus'. "
            "If any PR modifies files under the 'config/' directory, open an issue titled 'Audit config changes' "
            "with body 'Merged PRs modified files under config/ directory. Review needed.' "
            "Then append to the terminal log exactly:\n"
            "Audit results:\n"
            "PR #32 files: ['kubernetes/alertmanager.yaml', 'config/alertmanager.yml', 'docker-compose.yml'], authors: ['devops-lead']\n"
            "PR #34 files: ['kubernetes/prometheus.yaml', 'config/prometheus.yml', 'docs/MONITORING.md'], authors: ['devops-lead']"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "devops-lead"}),
            Action(name="get_repository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="list_pull_requests", kwargs={"repo_name": "k8s-monitoring"}),
            # PR 32
            Action(name="list_pull_request_files", kwargs={"repo_name": "k8s-monitoring", "pr_number": 32}),
            Action(name="list_commits", kwargs={"repo_name": "k8s-monitoring", "branch": "feature-alertmanager"}),

            # PR 34
            Action(name="list_pull_request_files", kwargs={"repo_name": "k8s-monitoring", "pr_number": 34}),
            Action(name="list_commits", kwargs={"repo_name": "k8s-monitoring", "branch": "upgrade-prometheus"}),

            # ✅ DB-modifying action (if config/ is touched)
            Action(name="create_issue", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Audit config changes",
                "body": "Merged PRs modified files under config/ directory. Review needed.",
                # "labels": ["audit"]
            }),

            # Terminal log using **real values**
            Action(name="append_terminal", kwargs={
                "message": (
                    "Audit results:\n"
                    "PR #32 files: ['kubernetes/alertmanager.yaml', 'config/alertmanager.yml', 'docker-compose.yml'], "
                    "authors: ['devops-lead']\n"
                    "PR #34 files: ['kubernetes/prometheus.yaml', 'config/prometheus.yml', 'docs/MONITORING.md'], "
                    "authors: ['devops-lead']"
                )
            }),
        ],
        outputs=[
            "{'32': {'files': ['kubernetes/alertmanager.yaml', 'config/alertmanager.yml', 'docker-compose.yml'], 'authors': ['devops-lead']}, "
            "'34': {'files': ['kubernetes/prometheus.yaml', 'config/prometheus.yml', 'docs/MONITORING.md'], 'authors': ['devops-lead']}}"
        ],
    ),

    # 24
    Task(
        annotator='0',
        user_id="task_24",
        instruction=(
            "You are 'ui-team'. For 'ui-kit', confirm Alert #4 dismissal aligns with latest commits on 'feature-theme'. "
            "Review branch commits and current alerts, check Issue #6, and leave a PR review comment on PR #11 noting the security status. "
            "Append terminal: 'ui-kit XSS dismissal validated against feature-theme commits'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "ui-team"}),
            Action(name="get_repository", kwargs={"repo_name": "ui-kit"}),
            Action(name="list_commits", kwargs={"repo_name": "ui-kit", "branch": "feature-theme"}),
            Action(name="list_code_scanning_alerts", kwargs={"repo_name": "ui-kit"}),
            Action(name="get_issue", kwargs={"repo_name": "ui-kit", "issue_number": 6}),
            # Action(name="add_issue_comment", kwargs={"repo_name": "ui-kit", "issue_number": 6, "comment": "Security: Alert #4 dismissed post latest feature-theme commits."}),
            Action(name="get_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 11}),
            Action(name="create_pull_request_review", kwargs={
                "repo_name": "ui-kit",
                "pr_number": 11,
                "review_decision": "comment",
                "comment": "ui-kit XSS dismissal validated against feature-theme commits"
            }),
            Action(name="append_terminal", kwargs={"message": "ui-kit XSS dismissal validated against feature-theme commits"}),
        ],
        outputs=['"message": "ui-kit XSS dismissal validated against feature-theme commits"'],
    ),

    # 25
    Task(
        annotator='0',
        user_id="task_25",
        instruction=(
            "You are 'security-team'. For 'security-scanner', verify Issue #11 resolution via PR #23 and inspect commits on 'perf-optimizations'. "
            "Create a release named 'v0.3.1 Performance optimization' with body: 'Implements file system cache; closes #11; ~70% performance gain.'. "
            "Append terminal: 'security-scanner perf fix validated and released'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "security-team"}),
            Action(name="get_repository", kwargs={"repo_name": "security-scanner"}),
            Action(name="get_issue", kwargs={"repo_name": "security-scanner", "issue_number": 11}),
            Action(name="get_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 23}),
            Action(name="list_commits", kwargs={"repo_name": "security-scanner", "branch": "perf-optimizations"}),
            Action(name="create_release", kwargs={
                "repo_name": "security-scanner",
                "tag": "v0.3.1",
                "name": "v0.3.1 Performance optimization",
                "body": "Implements file system cache; closes #11; ~70% performance gain.",
            }),
            Action(name="append_terminal", kwargs={"message": "security-scanner perf fix validated and released"}),
        ],
        outputs=['"message": "security-scanner perf fix validated and released"'],
    ),

    # 26
    Task(
        annotator='0',
        user_id="task_26",
        instruction=(
            "You are 'nlp-labs'. In 'nlp-models', you should verify that PR #22 merged for Issue #16 and review Issue #12 about memory. List commits on branch " "'exp-transformer' for investigation context. Then comment on Issue #12 with: 'Reviewed gradient accumulation commits on " "exp-transformer for memory tuning direction.' Append terminal: 'nlp-models checkpoint fix verified; memory follow-up noted'"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "nlp-labs"}),
            Action(name="get_repository", kwargs={"repo_name": "nlp-models"}),
            Action(name="get_pull_request", kwargs={"repo_name": "nlp-models", "pr_number": 22}),
            Action(name="get_issue", kwargs={"repo_name": "nlp-models", "issue_number": 16}),
            Action(name="get_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12}),
            Action(name="list_commits", kwargs={"repo_name": "nlp-models", "branch": "exp-transformer"}),
            Action(
                name="add_issue_comment",
                kwargs={
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "comment": "Reviewed gradient accumulation commits on exp-transformer for memory tuning direction."
                }
            ),
            Action(name="append_terminal", kwargs={"message": "nlp-models checkpoint fix verified; memory follow-up noted"}),
        ],
        outputs=['"message": "nlp-models checkpoint fix verified; memory follow-up noted"'],
    ),

    # 27
    Task(
        annotator='0',
        user_id="task_27",
        instruction=(
            "You are 'frontend-dev'. For 'react-dashboard', verify that PR #30 closed Issue #27. "
            "List open PRs and request changes on PR #28 with comment: 'Resolve merge conflicts before merge.' "
            "Label Issue #25 with 'investigate'. "
            "Append terminal: 'react-dashboard dark mode verified; realtime PR gated'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "frontend-dev"}),
            Action(name="get_repository", kwargs={"repo_name": "react-dashboard"}),
            Action(name="get_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 27}),
            Action(name="get_pull_request", kwargs={"repo_name": "react-dashboard", "pr_number": 30}),
            Action(name="list_open_pull_requests", kwargs={"repo_name": "react-dashboard"}),
            Action(name="create_pull_request_review", kwargs={"repo_name": "react-dashboard", "pr_number": 28, "review_decision": "request_changes", "body": "Resolve merge conflicts before merge."}),
            Action(name="add_label_to_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "label": "investigate"}),
            Action(name="append_terminal", kwargs={"message": "react-dashboard dark mode verified; realtime PR gated"}),
        ],
        outputs=['"message": "react-dashboard dark mode verified; realtime PR gated"'],
    ),

    # 29
    Task(
        annotator='0',
        user_id="task_29",
        instruction=(
            "You are 'ops-team'. For 'infra-terraform', inspect files on branch 'feat-alb', reference Issue #9, and open a pull request  "
            "from 'feat-alb' to 'main' with title 'Increase ALB health check timeout' and body 'Addresses #9 by increasing target health check thresholds.' Then comment on Issue #9 with: 'Opened PR to adjust ALB health check timing and config.' "
            "Append terminal: 'infra-terraform PR opened to address ALB health checks'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "ops-team"}),
            Action(name="get_repository", kwargs={"repo_name": "infra-terraform"}),
            Action(name="list_files", kwargs={"repo_name": "infra-terraform", "branch": "feat-alb"}),
            Action(name="get_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 9}),
            Action(name="create_pull_request", kwargs={
                "repo_name": "infra-terraform",
                "head": "feat-alb",
                "base": "main",
                "title": "Increase ALB health check timeout",
                "body": "Addresses #9 by increasing target health check thresholds."
            }),
            Action(name="add_issue_comment", kwargs={"repo_name": "infra-terraform", "issue_number": 9, "comment": "Opened PR to adjust ALB health check timing and config."}),
            Action(name="append_terminal", kwargs={"message": "infra-terraform PR opened to address ALB health checks"}),
        ],
        outputs=['"message": "infra-terraform PR opened to address ALB health checks"'],
    ),

    # 30
    Task(
        annotator='0',
        user_id="task_30",
        instruction=(
            "You are 'data-scientist'. For 'ml-pipeline', list commits on 'feature-mlflow-tracking' and inspect files content there. "
            "Update Issue #31 by commenting: 'Next step is drift detection.' "
            "Append terminal: 'ml-pipeline MLflow integration reviewed; validation roadmap updated'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "data-scientist"}),
            Action(name="get_repository", kwargs={"repo_name": "ml-pipeline"}),
            Action(name="list_commits", kwargs={"repo_name": "ml-pipeline", "branch": "feature-mlflow-tracking"}),
            Action(name="list_files", kwargs={"repo_name": "ml-pipeline", "branch": "feature-mlflow-tracking"}),
            Action(name="get_file_contents", kwargs={
                "repo_name": "ml-pipeline",
                "branch": "feature-mlflow-tracking",
                "path": "config/model_config.yaml"
            }),
            Action(name="get_issue", kwargs={"repo_name": "ml-pipeline", "issue_number": 31}),
            Action(name="add_issue_comment", kwargs={
                "repo_name": "ml-pipeline",
                "issue_number": 31,
                "comment": "Next step is drift detection."
            }),
            Action(name="append_terminal", kwargs={"message": "ml-pipeline MLflow integration reviewed; validation roadmap updated"}),
        ],
        outputs=['"message": "ml-pipeline MLflow integration reviewed; validation roadmap updated"'],
    ),

    # 31
    Task(
        annotator='0',
        user_id="task_31",
        instruction=(
            "You are 'security-team'. In 'security-scanner', review open PR #25 for SARIF output and list current alerts. "
            "Comment on the PR with: 'Confirm SARIF schema v2.1.0 and CI upload step.' "
            "Then open an issue titled 'SARIF config polish' with label 'enhancement' and body: "
            "'Tighten schema validation and CI upload parameters.' "
            "Append terminal: 'security-scanner SARIF review and config follow-up created'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "security-team"}),
            Action(name="get_repository", kwargs={"repo_name": "security-scanner"}),
            Action(name="get_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 25}),
            Action(name="list_code_scanning_alerts", kwargs={"repo_name": "security-scanner"}),
            Action(name="comment_on_pull_request", kwargs={
                "repo_name": "security-scanner",
                "pr_number": 25,
                "comment": "Confirm SARIF schema v2.1.0 and CI upload step."
            }),
            Action(name="create_issue", kwargs={
                "repo_name": "security-scanner",
                "title": "SARIF config polish",
                "body": "Tighten schema validation and CI upload parameters.",
                "labels": ["enhancement"],
            }),
            Action(name="append_terminal", kwargs={"message": "security-scanner SARIF review and config follow-up created"}),
        ],
        outputs=['"message": "security-scanner SARIF review and config follow-up created"'],
    ),

    # 33 (alice-w) acme-webapp: create feature branch, add release notes, commit, and log confirmation
    Task(
        annotator='0',
        user_id="task_33",
        instruction=(
            "You are 'alice-w' and must operate only through the available tools.\n\n"
            "YOUR GOAL\n"
            "• In repository 'acme-webapp', create a new branch from the literal source branch below, add a release-notes file "
            "with the exact content literal, commit with the exact message literal, and ensure the file exists on that new branch.\n"
            "• Ensure the most recent terminal entry is exactly the message literal below.\n\n"
            "LITERALS (use verbatim)\n"
            "- repo: acme-webapp\n"
            "- source branch: main\n"
            "- new branch: feature-banners\n"
            "- file path: docs/release-notes.md\n"
            "- file content: ## Release notes\\n- Seed entry\\n\n"
            "- commit message: docs: add release notes seed\n"
            "- terminal message: Release notes committed on feature-banners in acme-webapp\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),

            # Read default branch to justify using the literal 'main' as the source branch
            Action(name="get_default_branch", kwargs={"repo_name": "acme-webapp"}),

            # Write: create feature branch and add + commit release notes
            Action(name="create_branch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "feature-banners"
            }),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-banners",
                "path": "docs/release-notes.md",
                "content": "## Release notes\n- Seed entry\n"
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-banners",
                "commit_message": "docs: add release notes seed"
            }),

            # Verify: file exists on the new branch
            Action(name="list_files", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-banners"
            }),

            # Write + verify: terminal confirmation
            Action(name="append_terminal", kwargs={
                "message": "Release notes committed on feature-banners in acme-webapp"
            }),
            Action(name="list_terminal_last_message", kwargs={}),
        ],
        outputs=[
            '"message": "Branch created", "new_branch": "feature-banners"',
            '"message": "Committed to branch", "branch": "feature-banners"',
            '"entries": {"printed_ts": "2025-08-21T12:00:00Z", "message": "Release notes committed on feature-banners in acme-webapp"}',
        ],
    ),

    # 35 (frontend-dev) Protect default branch, publish hardening release, and record audit
    Task(
        annotator='0',
        user_id="task_35",
        instruction=(
            "You are 'frontend-dev. You must enforce baseline hardening on default branch of the repository 'react-dashboard' and "
            "publish that hardened state as a lightweight release. The default branch must be protected with protected set to 'true' "
            "and rules exactly: { \"required_reviews\": 1, \"enforce_admins\": true }. Add the repository topic 'security-hardening'. "
            "Publish a release with tag 'task_65-hardened' and body 'Hardening rules applied [task_65]'.\n\n"
            "Return the branch protection status and rules for the default branch, and include the terminal audit line: "
            "'Protection enabled and release task_65-hardened published for react-dashboard [task_65]'."
        ),
        actions=[
            # Identity & default branch discovery (read-only)
            Action(name="get_me", kwargs={"username": "frontend-dev"}),
            Action(name="get_default_branch", kwargs={"repo_name": "react-dashboard"}),

            # Hardening changes (writes)
            Action(
                name="set_branch_protection",
                kwargs={
                    "repo_name": "react-dashboard",
                    "branch": "main",
                    "protected": "true",
                    "rules": {"required_reviews": 1, "enforce_admins": True},
                },
            ),
            Action(name="add_repo_topic", kwargs={"repo_name": "react-dashboard", "topic": "security-hardening"}),
            Action(
                name="create_release",
                kwargs={
                    "repo_name": "react-dashboard",
                    "tag": "task_65-hardened",
                    "body": "Hardening rules applied [task_65]",
                },
            ),

            # Single verification readback to keep complexity within 13–15
            Action(name="get_branch_protection", kwargs={"repo_name": "react-dashboard", "branch": "main"}),

            # Terminal audit
            Action(
                name="append_terminal",
                kwargs={"message": "Protection enabled and release task_65-hardened published for react-dashboard [task_65]"},
            ),
        ],
        outputs=[
            # Branch protection object per tool contract (protected is a string in the tool's response)
            '"protected": "true", "rules": {"required_reviews": 1, "enforce_admins": true}',
            # Terminal audit confirmation
            '"message": "Protection enabled and release task_65-hardened published for react-dashboard [task_65]"',
        ],
    ),

    # 37 (alice-w) Branch lifecycle with file ops + audit log (Hard ~13–14 edges)
    Task(
        annotator='0',
        user_id="task_37",
        instruction=(
            "You are 'alice-w', working in the repository 'acme-webapp'. Demonstrate handling of a short-lived working branch. "
            "Introduce a temporary branch named 'temp-branch' derived from the repository’s default branch. "
            "Use it to hold a transient note at 'docs/tmp.txt' containing exactly 'temp work'. "
            "Show that the note’s content is available while the branch exists, and then retire the branch. "
            "When retiring it, ensure the event is logged with the exact message: 'Branch temp-branch deleted in acme-webapp.'. "
            "Finally, provide the set of remaining branches after the retirement. "
            "Return: (a) the retrieved file content, (b) the audit message, and (c) the final branch list."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="get_default_branch", kwargs={"repo_name": "acme-webapp"}),

            # Create branch
            Action(name="create_branch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "temp-branch"
            }),

            # Write file
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "temp-branch",
                "path": "docs/tmp.txt",
                "content": "temp work"
            }),

            # Read file
            Action(name="get_file_contents", kwargs={
                "repo_name": "acme-webapp",
                "branch": "temp-branch",
                "path": "docs/tmp.txt"
            }),

            # Delete branch
            Action(name="delete_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "temp-branch"
            }),

            # Audit log
            Action(name="append_terminal", kwargs={
                "message": "Branch temp-branch deleted in acme-webapp."
            }),

            # List branches
            Action(name="list_branches", kwargs={
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
            "You are 'alice-w'. In the repository 'acme-webapp', create a new issue titled "
            "'Security audit [task_01]' with body 'Check SQL injection handling paths. [task_01]'. "
            "That issue must carry the label 'security-check', have the exact comment "
            "'Audit logged. [task_01]', and its final state must be 'closed'. "
            "Return confirmation that the label was applied, the issue's final state, "
            "and a search result entry proving an issue with label 'security-check' exists. "
            "Also include this terminal audit line: "
            "'Issue closed with security-check label in acme-webapp [task_01]'."
        ),
        actions=[
            # Identity
            Action(name="get_me", kwargs={"username": "alice-w"}),

            # Create deterministic issue
            Action(
                name="create_issue",
                kwargs={
                    "repo_name": "acme-webapp",
                    "title": "Security audit [task_01]",
                    "body": "Check SQL injection handling paths. [task_01]",
                    "labels": []
                },
            ),

            # Apply label + comment
            Action(
                name="add_label_to_issue",
                kwargs={"repo_name": "acme-webapp", "issue_number": 1, "label": "security-check"},
            ),
            Action(
                name="add_issue_comment",
                kwargs={
                    "repo_name": "acme-webapp",
                    "issue_number": 1,
                    "comment": "Audit logged. [task_01]"
                },
            ),

            # Close the issue
            Action(
                name="update_issue",
                kwargs={"repo_name": "acme-webapp", "issue_number": 1, "state": "closed"},
            ),

            # Verify via search
            Action(
                name="search_issues",
                kwargs={"query": "security-check"},
            ),

            # Terminal audit
            Action(
                name="append_terminal",
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
            "You are 'frontend-dev'. In the repository 'react-dashboard', you must create a new issue titled "
            "'Build pipeline audit [task_72]' with body 'Verify CI stages and artifacts for reproducibility. [task_72]'. "
            "That issue must carry the label 'ci-audit', have the exact comment 'Checklist prepared. [task_72]', "
            "and its final state must be 'closed'. Return confirmation that the label was applied, the issue's final state, "
            "and a search result entry proving an issue with label 'ci-audit' exists. Also include this terminal audit line: "
            "'Issue closed with ci-audit label in react-dashboard [task_72]'."
        ),
        actions=[
            # Identity
            Action(name="get_me", kwargs={"username": "frontend-dev"}),

            # Create deterministic issue (flat row)
            Action(
                name="create_issue",
                kwargs={
                    "repo_name": "react-dashboard",
                    "title": "Build pipeline audit [task_72]",
                    "body": "Verify CI stages and artifacts for reproducibility. [task_72]",
                    "labels": []
                },
            ),

            # Apply label + comment
            Action(
                name="add_label_to_issue",
                kwargs={"repo_name": "react-dashboard", "issue_number": 1, "label": "ci-audit"},
            ),
            Action(
                name="add_issue_comment",
                kwargs={
                    "repo_name": "react-dashboard",
                    "issue_number": 1,
                    "comment": "Checklist prepared. [task_72]"
                },
            ),

            # Close the issue
            Action(
                name="update_issue",
                kwargs={"repo_name": "react-dashboard", "issue_number": 1, "state": "closed"},
            ),

            # Verify via search
            Action(
                name="search_issues",
                kwargs={"query": "ci-audit"},
            ),

            # Terminal audit
            Action(
                name="append_terminal",
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
            "You are 'security-team'. Deliver the following end state, with all values exact and case‑sensitive:\n"
            "• A repository named 'security-scanner-pro' exists and is owned by you; its visibility is 'public' and its default branch is 'main'.\n"
            "• The repository topics include both 'security' and 'sarif'.\n"
            "• A branch 'feature-sarif' exists. On that branch, the file 'src/scanner.py' contains exactly 'print('sarif-v1')' and the file 'README.md' contains exactly '# security-scanner-pro'.\n"
            "• The latest commit on 'feature-sarif' includes the message 'Add SARIF support scaffolding'.\n"
            "• Pull request #1 targets base 'main' from head 'feature-sarif' with title 'Add SARIF output support' and body 'Introduce SARIF output skeleton.', has requested reviewers 'qa-mike' and 'dev-sue', is approved, and is merged.\n"
            "• A release exists on 'security-scanner-pro' with tag 'v0.5.0', title 'SARIF support', and body 'Initial SARIF output format release.', and the latest release resolves to tag 'v0.5.0'.\n"
            "• An issue titled 'Post-release verification' exists with body 'Validate SARIF output end-to-end.' labeled 'release'.\n"
            "• The terminal log includes exactly one appended entry with the message 'security-scanner-pro v0.5.0 released.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "security-team"}),
            Action(name="create_repository", kwargs={"repo_name": "security-scanner-pro", "visibility": "public", "default_branch": "main"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "security-scanner-pro", "topic": "security"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "security-scanner-pro", "topic": "sarif"}),
            Action(name="create_branch", kwargs={"repo_name": "security-scanner-pro", "source_branch": "main", "new_branch": "feature-sarif"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "security-scanner-pro", "branch": "feature-sarif", "path": "src/scanner.py", "content": "print('sarif-v1')"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "security-scanner-pro", "branch": "feature-sarif", "path": "README.md", "content": "# security-scanner-pro"}),
            Action(name="commit_changes_to_branch", kwargs={"repo_name": "security-scanner-pro", "branch": "feature-sarif", "commit_message": "Add SARIF support scaffolding"}),
            Action(name="create_pull_request", kwargs={"repo_name": "security-scanner-pro", "title": "Add SARIF output support", "body": "Introduce SARIF output skeleton.", "base": "main", "head": "feature-sarif"}),
            Action(name="request_pull_request_reviewers", kwargs={"repo_name": "security-scanner-pro", "pr_number": 1, "reviewers": ["qa-mike", "dev-sue"]}),
            Action(name="create_pull_request_review", kwargs={"repo_name": "security-scanner-pro", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner-pro", "pr_number": 1}),
            Action(name="create_release", kwargs={"repo_name": "security-scanner-pro", "tag": "v0.5.0", "title": "SARIF support", "body": "Initial SARIF output format release."}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner-pro", "title": "Post-release verification", "body": "Validate SARIF output end-to-end.", "labels": ["release"]}),
            Action(name="append_terminal", kwargs={"message": "security-scanner-pro v0.5.0 released."}),
            Action(name="get_latest_release", kwargs={"repo_name": "security-scanner-pro"}),
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
            "You are 'devops-lead'. Deliver the following end state, with all values exact and case‑sensitive:\n"
            "• A repository named 'k8s-ci-pipelines' exists and is owned by you; its visibility is 'public' and its default branch is 'main'. The repository topics include 'kubernetes'.\n"
            "• A branch 'feature-alerts' exists. On that branch, the file 'kubernetes/alerts.yaml' contains exactly 'alertmanager: routes: placeholder-v2' and the file 'docs/alerts.md' contains exactly '# Alerts Runbook'.\n"
            "• The latest commit on 'feature-alerts' includes the message 'Add alert routing and runbook'.\n"
            "• Pull request #1 targets base 'main' from head 'feature-alerts' with title 'Introduce alert routing' and body 'Add Alertmanager routes and docs.', is approved, and is merged.\n"
            "• Branch protection is enabled on branch 'main' with rules exactly {'required_reviews': 1}.\n"
            "• An issue titled 'Branch protection enabled on main' exists with body 'Required reviews set to 1.' labeled 'security'.\n"
            "• The terminal log includes exactly one appended entry with the message 'k8s-ci-pipelines protection enabled on main.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "devops-lead"}),
            Action(name="create_repository", kwargs={"repo_name": "k8s-ci-pipelines", "visibility": "public", "default_branch": "main"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "k8s-ci-pipelines", "topic": "kubernetes"}),
            Action(name="create_branch", kwargs={"repo_name": "k8s-ci-pipelines", "source_branch": "main", "new_branch": "feature-alerts"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "k8s-ci-pipelines", "branch": "feature-alerts", "path": "kubernetes/alerts.yaml", "content": "alertmanager: routes: placeholder-v2"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "k8s-ci-pipelines", "branch": "feature-alerts", "path": "docs/alerts.md", "content": "# Alerts Runbook"}),
            Action(name="commit_changes_to_branch", kwargs={"repo_name": "k8s-ci-pipelines", "branch": "feature-alerts", "commit_message": "Add alert routing and runbook"}),
            Action(name="create_pull_request", kwargs={"repo_name": "k8s-ci-pipelines", "title": "Introduce alert routing", "body": "Add Alertmanager routes and docs.", "base": "main", "head": "feature-alerts"}),
            Action(name="create_pull_request_review", kwargs={"repo_name": "k8s-ci-pipelines", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "k8s-ci-pipelines", "pr_number": 1}),
            Action(name="set_branch_protection", kwargs={"repo_name": "k8s-ci-pipelines", "branch": "main", "protected": "true", "rules": {"required_reviews": 1}}),
            Action(name="create_issue", kwargs={"repo_name": "k8s-ci-pipelines", "title": "Branch protection enabled on main", "body": "Required reviews set to 1.", "labels": ["security"]}),
            Action(name="append_terminal", kwargs={"message": "k8s-ci-pipelines protection enabled on main."}),
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
            "You are 'frontend-dev'. Deliver the following end state, with all values exact and case-sensitive:\n"
            "• A repository named 'react-dashboard-pro' exists and is owned by you; its visibility is 'public' and its default branch is 'main'. The repository topics include both 'frontend' and 'react'.\n"
            "• A branch 'feature-dark-mode' exists. On that branch, the file 'src/theme/dark.js' contains exactly 'export const theme = 'dark';' and the file 'docs/dark-mode.md' contains exactly '# Dark mode user guide'.\n"
            "• The latest commit on 'feature-dark-mode' includes the message 'Implement dark mode theme'.\n"
            "• Pull request #1 targets base 'main' from head 'feature-dark-mode' with title 'Add dark mode theme' and body 'Introduce dark mode option for dashboard.', has requested reviewers 'qa-mike' and 'ui-team', is approved, and is merged.\n"
            "• A release exists on 'react-dashboard-pro' with tag 'v2.0.0', title 'Dark mode release', and body 'Dark mode theme is now available.'. The latest release resolves to tag 'v2.0.0'.\n"
            "• An issue titled 'Dark mode documentation' exists with body 'Add instructions for enabling dark mode in user guide.' labeled 'docs'.\n"
            "• Branch protection is enabled on branch 'main' with rules exactly {'required_reviews': 2}.\n"
            "• The terminal log includes exactly one appended entry with the message 'react-dashboard-pro v2.0.0 released with dark mode.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "frontend-dev"}),
            Action(name="create_repository", kwargs={"repo_name": "react-dashboard-pro", "visibility": "public", "default_branch": "main"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "react-dashboard-pro", "topic": "frontend"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "react-dashboard-pro", "topic": "react"}),
            Action(name="create_branch", kwargs={"repo_name": "react-dashboard-pro", "source_branch": "main", "new_branch": "feature-dark-mode"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "react-dashboard-pro", "branch": "feature-dark-mode", "path": "src/theme/dark.js", "content": "export const theme = 'dark';"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "react-dashboard-pro", "branch": "feature-dark-mode", "path": "docs/dark-mode.md", "content": "# Dark mode user guide"}),
            Action(name="commit_changes_to_branch", kwargs={"repo_name": "react-dashboard-pro", "branch": "feature-dark-mode", "commit_message": "Implement dark mode theme"}),
            Action(name="create_pull_request", kwargs={"repo_name": "react-dashboard-pro", "title": "Add dark mode theme", "body": "Introduce dark mode option for dashboard.", "base": "main", "head": "feature-dark-mode"}),
            Action(name="request_pull_request_reviewers", kwargs={"repo_name": "react-dashboard-pro", "pr_number": 1, "reviewers": ["qa-mike", "ui-team"]}),
            Action(name="create_pull_request_review", kwargs={"repo_name": "react-dashboard-pro", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "react-dashboard-pro", "pr_number": 1}),
            Action(name="create_release", kwargs={"repo_name": "react-dashboard-pro", "tag": "v2.0.0", "title": "Dark mode release", "body": "Dark mode theme is now available."}),
            Action(name="get_latest_release", kwargs={"repo_name": "react-dashboard-pro"}),
            Action(name="create_issue", kwargs={"repo_name": "react-dashboard-pro", "title": "Dark mode documentation", "body": "Add instructions for enabling dark mode in user guide.", "labels": ["docs"]}),
            Action(name="set_branch_protection", kwargs={"repo_name": "react-dashboard-pro", "branch": "main", "protected": "true", "rules": {"required_reviews": 2}}),
            Action(name="append_terminal", kwargs={"message": "react-dashboard-pro v2.0.0 released with dark mode."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "react-dashboard-pro"',
            '"message": "Pull request opened", "title": "Add dark mode theme", "pr_number": 1',
            '"message": "Reviewers requested.", "requested_reviewers": ["qa-mike", "ui-team"]',
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
            "You are 'ops-team'. Deliver the following end state, with all values exact and case‑sensitive:\n"
            "• A repository named 'infra-containers' exists and is owned by you; its visibility is 'public' and its default branch is 'main'. The repository topics include 'docker'.\n"
            "• A branch 'feature-registry' exists. On that branch, the file 'docker-compose.yml' contains exactly 'services: placeholder-v1' and the file 'docs/registry.md' contains exactly '# Private registry setup'.\n"
            "• The latest commit on 'feature-registry' includes the message 'Add registry compose and docs'.\n"
            "• Pull request #1 targets base 'main' from head 'feature-registry' with title 'Add container registry' and body 'Introduce docker-compose for registry and docs.', is approved, and is merged.\n"
            "• A release exists on 'infra-containers' with tag 'v0.3.0', title 'Registry compose', and body 'Adds docker-compose and docs.'.\n"
            "• An issue titled 'Track registry rollout' exists with body 'Coordinate rollout with ops.' labeled 'ops'.\n"
            "• Branch protection is enabled on branch 'main' with rules exactly {'required_reviews': 1}.\n"
            "• The terminal log includes exactly one appended entry with the message 'infra-containers v0.3.0 released.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "ops-team"}),
            Action(name="create_repository", kwargs={"repo_name": "infra-containers", "visibility": "public", "default_branch": "main"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "infra-containers", "topic": "docker"}),
            Action(name="create_branch", kwargs={"repo_name": "infra-containers", "source_branch": "main", "new_branch": "feature-registry"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "infra-containers", "branch": "feature-registry", "path": "docker-compose.yml", "content": "services: placeholder-v1"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "infra-containers", "branch": "feature-registry", "path": "docs/registry.md", "content": "# Private registry setup"}),
            Action(name="commit_changes_to_branch", kwargs={"repo_name": "infra-containers", "branch": "feature-registry", "commit_message": "Add registry compose and docs"}),
            Action(name="create_pull_request", kwargs={"repo_name": "infra-containers", "title": "Add container registry", "body": "Introduce docker-compose for registry and docs.", "base": "main", "head": "feature-registry"}),
            Action(name="create_pull_request_review", kwargs={"repo_name": "infra-containers", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "infra-containers", "pr_number": 1}),
            Action(name="create_release", kwargs={"repo_name": "infra-containers", "tag": "v0.3.0", "title": "Registry compose", "body": "Adds docker-compose and docs."}),
            Action(name="create_issue", kwargs={"repo_name": "infra-containers", "title": "Track registry rollout", "body": "Coordinate rollout with ops.", "labels": ["ops"]}),
            Action(name="set_branch_protection", kwargs={"repo_name": "infra-containers", "branch": "main", "protected": "true", "rules": {"required_reviews": 1}}),
            Action(name="append_terminal", kwargs={"message": "infra-containers v0.3.0 released."}),
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
            "You are 'backend-core'. Deliver the following end state, with all values exact and case‑sensitive:\n"
            "• A repository named 'backend-payment-service' exists and is owned by you; its visibility is 'public' and its default branch is 'main'. The repository topics include both 'payments' and 'backend'.\n"
            "• A branch 'feature-payment-webhooks' exists. On that branch, the file 'src/webhooks.py' contains exactly 'print('webhooks-v1')' and the file 'docs/webhooks.md' contains exactly '# Webhooks guide'.\n"
            "• The latest commit on 'feature-payment-webhooks' includes the message 'Implement payment webhooks'.\n"
            "• Pull request #1 targets base 'main' from head 'feature-payment-webhooks' with title 'Add payment webhooks' and body 'Introduce webhook handlers and docs.', has requested reviewers 'qa-erin' and 'payments-lead', is approved, and is merged.\n"
            "• Branch protection is enabled on branch 'main' with rules exactly {'required_reviews': 2}.\n"
            "• A release exists on 'backend-payment-service' with tag 'v1.3.0', title 'Payment webhooks', and body 'Initial webhook support.', and the latest release resolves to tag 'v1.3.0'.\n"
            "• An issue titled 'Post-deploy checklist' exists with body 'Validate webhook delivery and retries.' labeled 'release'.\n"
            "• The terminal log includes exactly one appended entry with the message 'backend-payment-service v1.3.0 released.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "backend-core"}),
            Action(name="create_repository", kwargs={"repo_name": "backend-payment-service", "visibility": "public", "default_branch": "main"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "backend-payment-service", "topic": "payments"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "backend-payment-service", "topic": "backend"}),
            Action(name="create_branch", kwargs={"repo_name": "backend-payment-service", "source_branch": "main", "new_branch": "feature-payment-webhooks"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "backend-payment-service", "branch": "feature-payment-webhooks", "path": "src/webhooks.py", "content": "print('webhooks-v1')"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "backend-payment-service", "branch": "feature-payment-webhooks", "path": "docs/webhooks.md", "content": "# Webhooks guide"}),
            Action(name="commit_changes_to_branch", kwargs={"repo_name": "backend-payment-service", "branch": "feature-payment-webhooks", "commit_message": "Implement payment webhooks"}),
            Action(name="create_pull_request", kwargs={"repo_name": "backend-payment-service", "title": "Add payment webhooks", "body": "Introduce webhook handlers and docs.", "base": "main", "head": "feature-payment-webhooks"}),
            Action(name="request_pull_request_reviewers", kwargs={"repo_name": "backend-payment-service", "pr_number": 1, "reviewers": ["qa-erin", "payments-lead"]}),
            Action(name="create_pull_request_review", kwargs={"repo_name": "backend-payment-service", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "backend-payment-service", "pr_number": 1}),
            Action(name="set_branch_protection", kwargs={"repo_name": "backend-payment-service", "branch": "main", "protected": "true", "rules": {"required_reviews": 2}}),
            Action(name="create_release", kwargs={"repo_name": "backend-payment-service", "tag": "v1.3.0", "title": "Payment webhooks", "body": "Initial webhook support."}),
            Action(name="get_latest_release", kwargs={"repo_name": "backend-payment-service"}),
            Action(name="create_issue", kwargs={"repo_name": "backend-payment-service", "title": "Post-deploy checklist", "body": "Validate webhook delivery and retries.", "labels": ["release"]}),
            Action(name="append_terminal", kwargs={"message": "backend-payment-service v1.3.0 released."}),
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
            "You are 'alice-w'. Deliver the following end state, with all values exact and case-sensitive:\n"
            "• A repository named 'acme-sql-service' exists and is owned by you; its visibility is 'public' and its default branch is 'main'. The repository topics include 'database'.\n"
            "• A branch 'feature-sanitize-input' exists. On that branch, the file 'src/sanitize.py' contains exactly 'def sanitize(v): return str(v)' and the file 'docs/security.md' contains exactly '# SQL sanitization patch'.\n"
            "• The latest commit on 'feature-sanitize-input' includes the message 'Add input sanitization helper'.\n"
            "• Pull request #1 targets base 'main' from head 'feature-sanitize-input' with title 'Add SQL sanitization' and body 'Introduce helper to sanitize SQL input.', is approved, and is merged.\n"
            "• A release exists on 'acme-sql-service' with tag 'v0.2.0', title 'Sanitization patch', and body 'Helper added for SQL sanitization.'.\n"
            "• An issue titled 'Review sanitization helper' exists with body 'Validate new helper across services.' labeled 'security'.\n"
            "• The terminal log includes exactly one appended entry with the message 'acme-sql-service v0.2.0 released.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="create_repository", kwargs={"repo_name": "acme-sql-service", "visibility": "public", "default_branch": "main"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "acme-sql-service", "topic": "database"}),
            Action(name="create_branch", kwargs={"repo_name": "acme-sql-service", "source_branch": "main", "new_branch": "feature-sanitize-input"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "acme-sql-service", "branch": "feature-sanitize-input", "path": "src/sanitize.py", "content": "def sanitize(v): return str(v)"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "acme-sql-service", "branch": "feature-sanitize-input", "path": "docs/security.md", "content": "# SQL sanitization patch"}),
            Action(name="commit_changes_to_branch", kwargs={"repo_name": "acme-sql-service", "branch": "feature-sanitize-input", "commit_message": "Add input sanitization helper"}),
            Action(name="create_pull_request", kwargs={"repo_name": "acme-sql-service", "title": "Add SQL sanitization", "body": "Introduce helper to sanitize SQL input.", "base": "main", "head": "feature-sanitize-input"}),
            Action(name="create_pull_request_review", kwargs={"repo_name": "acme-sql-service", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "acme-sql-service", "pr_number": 1}),
            Action(name="create_release", kwargs={"repo_name": "acme-sql-service", "tag": "v0.2.0", "title": "Sanitization patch", "body": "Helper added for SQL sanitization."}),
            Action(name="create_issue", kwargs={"repo_name": "acme-sql-service", "title": "Review sanitization helper", "body": "Validate new helper across services.", "labels": ["security"]}),
            Action(name="append_terminal", kwargs={"message": "acme-sql-service v0.2.0 released."}),
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

    # 52. (backend-core) Timeout policy docs exist, were reviewed/merged, and are released
    Task(
        annotator='0',
        user_id="task_52",
        instruction=(
            "You are 'backend-core'. When you complete the task, the repository state for 'payments-service' must satisfy ALL of the "
            "following properties:\n"
            "• A documentation file exists at path 'docs/TIMEOUT_POLICY.md' with EXACT content "
            "'Default request timeout is 60s. 3DS flows may extend to 90s. Retries: none.'.\n"
            "• This change originates on a branch named 'feature-timeout-policy' and is represented by a commit whose "
            "message is EXACTLY 'Document timeout policy'.\n"
            "• The change is integrated into 'main' via a reviewed pull request titled 'Document timeout policy' with a "
            "review request made to 'qa-erin', and that pull request is merged.\n"
            "• A release exists with tag 'v0.2.1', title 'Timeout policy docs', and body 'Publish timeout policy documentation.', "
            "and the latest release reflects tag 'v0.2.1'.\n"
            "• An issue exists titled 'Timeout policy docs published' with body 'Docs merged and released as v0.2.1.' and "
            "label 'documentation'.\n"
            "• The terminal audit log contains the EXACT entry 'payments-service timeout policy docs published and released as v0.2.1.'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "backend-core"}),
            Action(name="get_repository", kwargs={"repo_name": "payments-service"}),
            Action(name="create_branch", kwargs={"repo_name": "payments-service", "source_branch": "main", "new_branch": "feature-timeout-policy"}),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "payments-service",
                "branch": "feature-timeout-policy",
                "path": "docs/TIMEOUT_POLICY.md",
                "content": "Default request timeout is 60s. 3DS flows may extend to 90s. Retries: none."
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "payments-service",
                "branch": "feature-timeout-policy",
                "commit_message": "Document timeout policy"
            }),
            Action(name="create_pull_request", kwargs={
                "repo_name": "payments-service",
                "title": "Document timeout policy",
                "base": "main",
                "head": "feature-timeout-policy"
            }),
            Action(name="request_pull_request_reviewers", kwargs={
                "repo_name": "payments-service",
                "pr_number": 1,
                "reviewers": ["qa-erin"]
            }),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 1}),
            Action(name="create_release", kwargs={
                "repo_name": "payments-service",
                "tag": "v0.2.1",
                "title": "Timeout policy docs",
                "body": "Publish timeout policy documentation."
            }),
            Action(name="get_latest_release", kwargs={"repo_name": "payments-service"}),
            Action(name="create_issue", kwargs={
                "repo_name": "payments-service",
                "title": "Timeout policy docs published",
                "body": "Docs merged and released as v0.2.1.",
                "labels": ["documentation"]
            }),
            Action(name="append_terminal", kwargs={
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
        "You are 'docs-amy'. Deliver the following end state, with all values exact and case-sensitive:\n"
        "• A repository named 'product-docs' exists and is owned by you; its visibility is 'public' and its default branch is 'main'. The repository topics include both 'docs' and 'markdown'.\n"
        "• Branch protection is enabled on branch 'main' with rules exactly {'required_reviews': 1}.\n"
        "• A release exists on 'product-docs' with tag 'v1.0.0', title 'Initial documentation', and body 'Bootstrap product documentation.'.\n"
        "• An issue titled 'Add onboarding guide' exists with body 'Create onboarding section in docs.' labeled 'docs'.\n"
        "• The terminal log includes exactly one appended entry with the message 'product-docs v1.0.0 published.'\n"
        "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
        Action(name="get_me", kwargs={"username": "docs-amy"}),
        Action(name="create_repository", kwargs={"repo_name": "product-docs", "visibility": "public", "default_branch": "main"}),
        Action(name="add_repo_topic", kwargs={"repo_name": "product-docs", "topic": "docs"}),
        Action(name="add_repo_topic", kwargs={"repo_name": "product-docs", "topic": "markdown"}),
        Action(name="set_branch_protection", kwargs={"repo_name": "product-docs", "branch": "main", "protected": "true", "rules": {"required_reviews": 1}}),
        Action(name="create_release", kwargs={"repo_name": "product-docs", "tag": "v1.0.0", "title": "Initial documentation", "body": "Bootstrap product documentation."}),
        Action(name="create_issue", kwargs={"repo_name": "product-docs", "title": "Add onboarding guide", "body": "Create onboarding section in docs.", "labels": ["docs"]}),
        Action(name="append_terminal", kwargs={"message": "product-docs v1.0.0 published."}),
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
            "You are 'devops-lead'. Ensure 'k8s-monitoring' has published and merged documentation of the Prometheus "
            "retention policy. The documentation must exist at 'docs/RETENTION_POLICY.md' with the exact content "
            "'Prometheus retention is 30 days. Compaction enabled. Storage class: gp3.'. The change must be introduced on "
            "a branch named 'feature-retention-policy', merged into 'main' via a reviewed pull request titled "
            "'Document Prometheus retention' (request review from 'ops-team'). Use the exact commit message "
            "'Document 30-day Prometheus retention'. Record completion by opening an issue titled "
            "'Prometheus retention policy documented' with body 'Retention set to 30 days and documented.' labeled "
            "'documentation', and add the exact terminal audit entry 'k8s-monitoring retention policy docs merged and recorded.'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "devops-lead"}),
            Action(name="get_repository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="create_branch", kwargs={"repo_name": "k8s-monitoring", "source_branch": "main", "new_branch": "feature-retention-policy"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "k8s-monitoring", "branch": "feature-retention-policy", "path": "docs/RETENTION_POLICY.md", "content": "Prometheus retention is 30 days. Compaction enabled. Storage class: gp3."}),
            Action(name="commit_changes_to_branch", kwargs={"repo_name": "k8s-monitoring", "branch": "feature-retention-policy", "commit_message": "Document 30-day Prometheus retention"}),
            Action(name="create_pull_request", kwargs={"repo_name": "k8s-monitoring", "title": "Document Prometheus retention", "base": "main", "head": "feature-retention-policy"}),
            Action(name="request_pull_request_reviewers", kwargs={"repo_name": "k8s-monitoring", "pr_number": 1, "reviewers": ["ops-team"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "k8s-monitoring", "pr_number": 1}),
            Action(name="create_issue", kwargs={"repo_name": "k8s-monitoring", "title": "Prometheus retention policy documented", "body": "Retention set to 30 days and documented.", "labels": ["documentation"]}),
            Action(name="append_terminal", kwargs={"message": "k8s-monitoring retention policy docs merged and recorded."}),
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
            "You are 'qa-mike'. Deliver the following end state, with all values exact and case-sensitive:\n"
            "• A repository named 'qa-tests' exists and is owned by you; its visibility is 'public' and its default branch is 'main'. The repository topics include 'qa'.\n"
            "• A release exists on 'qa-tests' with tag 'v0.1.0', title 'Initial QA setup', and body 'Bootstrap test repository.'.\n"
            "• An issue titled 'Write first test cases' exists with body 'Add login and signup test coverage.' labeled 'qa'.\n"
            "• The terminal log includes exactly one appended entry with the message 'qa-tests v0.1.0 created.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "qa-mike"}),
            Action(name="create_repository", kwargs={"repo_name": "qa-tests", "visibility": "public", "default_branch": "main"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "qa-tests", "topic": "qa"}),
            Action(name="create_release", kwargs={"repo_name": "qa-tests", "tag": "v0.1.0", "title": "Initial QA setup", "body": "Bootstrap test repository."}),
            Action(name="create_issue", kwargs={"repo_name": "qa-tests", "title": "Write first test cases", "body": "Add login and signup test coverage.", "labels": ["qa"]}),
            Action(name="append_terminal", kwargs={"message": "qa-tests v0.1.0 created."}),
        ],
        outputs=[
            '"message": "Repository created", "repo_name": "qa-tests"',
            '"message": "Release created.", "repo_name": "qa-tests", "tag_name": "v0.1.0"',
            '"message": "Issue created", "number": 1',
            '"message": "qa-tests v0.1.0 created."',
        ],
    ),

    # 56. (ui-team) Ship ThemeProvider docs under protection, release, and audit
    Task(
        annotator='0',
        user_id="task_56",
        instruction=(
            "You are 'ui-team'. You need to work on repository 'ui-kit' and carry out the tasks mentioned below: "
            "1) Branch 'main' is protected with rules exactly {\"require_reviews\": true, \"enforce_admins\": true}. "
            "2) The file 'docs/THEME_PROVIDER.md' exists on 'main' with the exact content "
            "'Use ThemeProvider at the app root. Props: theme (required). Example: <ThemeProvider theme={Theme}>'. "
            "   This change originates on a branch named 'feature-theme-docs' and is represented by a commit whose message is "
            "   exactly 'Add ThemeProvider documentation'. "
            "   The change is integrated into 'main' via a reviewed pull request titled 'ThemeProvider docs'; a review request is made to 'ui-dev', "
            "   and an approval review containing the exact comment 'LGTM' is recorded. "
            "3) A release exists with tag 'v1.0.1', title 'Theme docs', and body 'Add ThemeProvider documentation.', and "
            "   the latest release reflects tag 'v1.0.1'. "
            "4) An issue exists titled 'ThemeProvider docs published' with body 'Docs merged and released as v1.0.1.' labeled 'documentation'. "
            "5) The terminal audit includes the exact entry 'ui-kit ThemeProvider docs published and released as v1.0.1.'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "ui-team"}),
            Action(
                name="set_branch_protection",
                kwargs={
                    "repo_name": "ui-kit",
                    "branch": "main",
                    "protected": "true",
                    "rules": {"require_reviews": "true", "enforce_admins": "true"},
                },
            ),
            Action(name="create_branch", kwargs={"repo_name": "ui-kit", "source_branch": "main", "new_branch": "feature-theme-docs"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature-theme-docs", "path": "docs/THEME_PROVIDER.md", "content": "Use ThemeProvider at the app root. Props: theme (required). Example: <ThemeProvider theme={Theme}>"}),
            Action(name="commit_changes_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature-theme-docs", "commit_message": "Add ThemeProvider documentation"}),
            Action(name="create_pull_request", kwargs={"repo_name": "ui-kit", "title": "ThemeProvider docs", "base": "main", "head": "feature-theme-docs"}),
            Action(name="request_pull_request_reviewers", kwargs={"repo_name": "ui-kit", "pr_number": 1, "reviewers": ["ui-dev"]}),
            Action(name="create_pull_request_review", kwargs={"repo_name": "ui-kit", "pr_number": 1, "review_decision": "approve", "comment": "LGTM"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 1}),
            Action(name="create_release", kwargs={"repo_name": "ui-kit", "tag": "v1.0.1", "title": "Theme docs", "body": "Add ThemeProvider documentation."}),
            Action(name="get_latest_release", kwargs={"repo_name": "ui-kit"}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "ThemeProvider docs published", "body": "Docs merged and released as v1.0.1.", "labels": ["documentation"]}),
            Action(name="append_terminal", kwargs={"message": "ui-kit ThemeProvider docs published and released as v1.0.1."}),
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
            "You are 'maintainer-tom'. You need to deliver the following end state, with all values exact and case‑sensitive:\n"
            "• A repository named 'tooling-maintenance' exists and is owned by you; its visibility is 'public' and its default branch is 'main'.\n"
            "• A release exists on 'tooling-maintenance' with tag 'v0.1.0', title 'Initial maintenance setup', and body 'Bootstrap maintenance repo.'.\n"
            "• An issue titled 'Create weekly maintenance checklist' exists with body 'Define checklist template for weekly runs.' labeled 'maintenance'.\n"
            "• The terminal log includes exactly one appended entry with the message 'tooling-maintenance v0.1.0 created.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "maintainer-tom"}),
            Action(name="create_repository", kwargs={"repo_name": "tooling-maintenance", "visibility": "public", "default_branch": "main"}),
            Action(name="create_release", kwargs={"repo_name": "tooling-maintenance", "tag": "v0.1.0", "title": "Initial maintenance setup", "body": "Bootstrap maintenance repo."}),
            Action(name="create_issue", kwargs={"repo_name": "tooling-maintenance", "title": "Create weekly maintenance checklist", "body": "Define checklist template for weekly runs.", "labels": ["maintenance"]}),
            Action(name="append_terminal", kwargs={"message": "tooling-maintenance v0.1.0 created."}),
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
            "You are 'tech-lead-tara'. Deliver the following end state, with all values exact and case‑sensitive:\n"
            "• A repository named 'automation-ci' exists and is owned by you; its visibility is 'public' and its default branch is 'main'. The repository topics include both 'automation' and 'ci'.\n"
            "• A branch 'feature-ci-config' exists. On that branch, the file '.github/workflows/ci.yml' contains exactly 'name: ci'.\n"
            "• The latest commit on 'feature-ci-config' includes the message 'Add CI workflow'.\n"
            "• Branch protection is enabled on branch 'main' with rules exactly {'required_reviews': 1}.\n"
            "• A release exists on 'automation-ci' with tag 'v0.1.0', title 'CI bootstrap', and body 'Adds initial CI workflow.'.\n"
            "• An issue titled 'Expand CI matrix' exists with body 'Add Python and Node matrix to CI.' labeled 'ci'.\n"
            "• The terminal log includes exactly one appended entry with the message 'automation-ci v0.1.0 released.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "tech-lead-tara"}),
            Action(name="create_repository", kwargs={"repo_name": "automation-ci", "visibility": "public", "default_branch": "main"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "automation-ci", "topic": "automation"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "automation-ci", "topic": "ci"}),
            Action(name="create_branch", kwargs={"repo_name": "automation-ci", "source_branch": "main", "new_branch": "feature-ci-config"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "automation-ci", "branch": "feature-ci-config", "path": ".github/workflows/ci.yml", "content": "name: ci"}),
            Action(name="commit_changes_to_branch", kwargs={"repo_name": "automation-ci", "branch": "feature-ci-config", "commit_message": "Add CI workflow"}),
            Action(name="set_branch_protection", kwargs={"repo_name": "automation-ci", "branch": "main", "protected": "true", "rules": {"required_reviews": 1}}),
            Action(name="create_release", kwargs={"repo_name": "automation-ci", "tag": "v0.1.0", "title": "CI bootstrap", "body": "Adds initial CI workflow."}),
            Action(name="create_issue", kwargs={"repo_name": "automation-ci", "title": "Expand CI matrix", "body": "Add Python and Node matrix to CI.", "labels": ["ci"]}),
            Action(name="append_terminal", kwargs={"message": "automation-ci v0.1.0 released."}),
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
            "You are 'design-lead'. Deliver the following end state, with all values exact and case‑sensitive:\n"
            "• A repository initially named 'design-system' is created by you as 'private' with default branch 'main', then renamed to 'design-system-pro' and its visibility is 'public'. The repository topics include 'design'.\n"
            "• A branch 'feature-guidelines' exists. On that branch, the file 'docs/guidelines.md' contains exactly '# Design guidelines' and the file 'tokens/colors.json' contains exactly '{'brand':'blue'}'.\n"
            "• The latest commit on 'feature-guidelines' includes the message 'Add initial guidelines and tokens'.\n"
            "• A release exists on 'design-system-pro' with tag 'v1.0.0', title 'Design system v1', and body 'Initial guidelines and tokens.'.\n"
            "• An issue titled 'Track design system adoption' exists with body 'Roll out across products.' labeled 'design'.\n"
            "• The terminal log includes exactly one appended entry with the message 'design-system-pro v1.0.0 published.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "design-lead"}),
            Action(name="create_repository", kwargs={"repo_name": "design-system", "visibility": "private", "default_branch": "main"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "design-system", "topic": "design"}),
            Action(name="rename_repository", kwargs={"old_name": "design-system", "new_name": "design-system-pro"}),
            Action(name="set_repository_visibility", kwargs={"repo_name": "design-system-pro", "visibility": "public"}),
            Action(name="create_branch", kwargs={"repo_name": "design-system-pro", "source_branch": "main", "new_branch": "feature-guidelines"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "design-system-pro", "branch": "feature-guidelines", "path": "docs/guidelines.md", "content": "# Design guidelines"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "design-system-pro", "branch": "feature-guidelines", "path": "tokens/colors.json", "content": "{'brand':'blue'}"}),
            Action(name="commit_changes_to_branch", kwargs={"repo_name": "design-system-pro", "branch": "feature-guidelines", "commit_message": "Add initial guidelines and tokens"}),
            Action(name="create_release", kwargs={"repo_name": "design-system-pro", "tag": "v1.0.0", "title": "Design system v1", "body": "Initial guidelines and tokens."}),
            Action(name="create_issue", kwargs={"repo_name": "design-system-pro", "title": "Track design system adoption", "body": "Roll out across products.", "labels": ["design"]}),
            Action(name="append_terminal", kwargs={"message": "design-system-pro v1.0.0 published."}),
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
            "You are 'devops-lead'. When you complete the task, the repository state for 'k8s-monitoring' must satisfy ALL of the following properties:\n"
            "• A documentation file exists at 'docs/LOGGING.md' with the EXACT content "
            "'Centralized logging with Fluent Bit. Logs shipped to Elasticsearch. Retention: 14 days.'.\n"
            "• This change originates on a branch named 'feature-logging-docs' and is represented by a commit whose message is "
            "EXACTLY 'Add logging documentation'.\n"
            "• The change is merged into 'main' via a reviewed pull request titled 'Logging docs'; a review request is made to "
            "'ops-team', and an approval review with the exact comment 'Approved for observability' is recorded.\n"
            "• The repository has the topic 'observability'.\n"
            "• A release exists with tag 'v1.5.0', title 'Logging docs', and body 'Add logging documentation.', and the latest "
            "release reflects tag 'v1.5.0'.\n"
            "• An issue exists titled 'Logging docs published' with body 'Docs merged and released as v1.5.0.' labeled 'documentation'.\n"
            "• The terminal audit log contains the EXACT entry 'k8s-monitoring logging docs published and released as v1.5.0.'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "devops-lead"}),
            Action(name="get_repository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="create_branch", kwargs={"repo_name": "k8s-monitoring", "source_branch": "main", "new_branch": "feature-logging-docs"}),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "k8s-monitoring",
                "branch": "feature-logging-docs",
                "path": "docs/LOGGING.md",
                "content": "Centralized logging with Fluent Bit. Logs shipped to Elasticsearch. Retention: 14 days."
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "k8s-monitoring",
                "branch": "feature-logging-docs",
                "commit_message": "Add logging documentation"
            }),
            Action(name="create_pull_request", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Logging docs",
                "base": "main",
                "head": "feature-logging-docs"
            }),
            Action(name="request_pull_request_reviewers", kwargs={
                "repo_name": "k8s-monitoring",
                "pr_number": 1,
                "reviewers": ["ops-team"]
            }),
            Action(name="create_pull_request_review", kwargs={
                "repo_name": "k8s-monitoring",
                "pr_number": 1,
                "review_decision": "approve",
                "comment": "Approved for observability"
            }),
            Action(name="merge_pull_request", kwargs={"repo_name": "k8s-monitoring", "pr_number": 1}),
            Action(name="add_repo_topic", kwargs={"repo_name": "k8s-monitoring", "topic": "observability"}),
            Action(name="create_release", kwargs={
                "repo_name": "k8s-monitoring",
                "tag": "v1.5.0",
                "title": "Logging docs",
                "body": "Add logging documentation."
            }),
            Action(name="get_latest_release", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="create_issue", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Logging docs published",
                "body": "Docs merged and released as v1.5.0.",
                "labels": ["documentation"]
            }),
            Action(name="append_terminal", kwargs={"message": "k8s-monitoring logging docs published and released as v1.5.0."}),
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
            "You are 'ml-engineer'. Deliver the following end state, with all values exact and case‑sensitive:\n"
            "• A repository named 'ml-ops-pipeline' exists and is owned by you; its visibility is 'public' and its default branch is 'main'. The repository topics include both 'mlops' and 'pipeline'.\n"
            "• A branch 'feature-training-job' exists. On that branch, the file 'pipelines/train.py' contains exactly 'print('train-v1')' and the file 'kubernetes/job.yaml' contains exactly 'kind: Job'.\n"
            "• The latest commit on 'feature-training-job' includes the message 'Add training job and pipeline stub'.\n"
            "• Pull request #1 targets base 'main' from head 'feature-training-job' with title 'Add training pipeline' and body 'Introduce training job and pipeline stub.', has requested reviewers 'qa-mike' and 'dev-sue', is approved, and is merged.\n"
            "• Branch protection is enabled on branch 'main' with rules exactly {'required_reviews': 2}.\n"
            "• A release exists on 'ml-ops-pipeline' with tag 'v0.8.0', title 'Training pipeline', and body 'Initial training job and pipeline stub.', and the latest release resolves to tag 'v0.8.0'.\n"
            "• An issue titled 'Validate training pipeline' exists with body 'Run end‑to‑end training and verify outputs.' labeled 'mlops'.\n"
            "• The terminal log includes exactly one appended entry with the message 'ml-ops-pipeline v0.8.0 released.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "ml-engineer"}),
            Action(name="create_repository", kwargs={"repo_name": "ml-ops-pipeline", "visibility": "public", "default_branch": "main"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "ml-ops-pipeline", "topic": "mlops"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "ml-ops-pipeline", "topic": "pipeline"}),
            Action(name="create_branch", kwargs={"repo_name": "ml-ops-pipeline", "source_branch": "main", "new_branch": "feature-training-job"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "ml-ops-pipeline", "branch": "feature-training-job", "path": "pipelines/train.py", "content": "print('train-v1')"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "ml-ops-pipeline", "branch": "feature-training-job", "path": "kubernetes/job.yaml", "content": "kind: Job"}),
            Action(name="commit_changes_to_branch", kwargs={"repo_name": "ml-ops-pipeline", "branch": "feature-training-job", "commit_message": "Add training job and pipeline stub"}),
            Action(name="create_pull_request", kwargs={"repo_name": "ml-ops-pipeline", "title": "Add training pipeline", "body": "Introduce training job and pipeline stub.", "base": "main", "head": "feature-training-job"}),
            Action(name="request_pull_request_reviewers", kwargs={"repo_name": "ml-ops-pipeline", "pr_number": 1, "reviewers": ["qa-mike", "dev-sue"]}),
            Action(name="create_pull_request_review", kwargs={"repo_name": "ml-ops-pipeline", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ml-ops-pipeline", "pr_number": 1}),
            Action(name="set_branch_protection", kwargs={"repo_name": "ml-ops-pipeline", "branch": "main", "protected": "true", "rules": {"required_reviews": 2}}),
            Action(name="create_release", kwargs={"repo_name": "ml-ops-pipeline", "tag": "v0.8.0", "title": "Training pipeline", "body": "Initial training job and pipeline stub."}),
            Action(name="get_latest_release", kwargs={"repo_name": "ml-ops-pipeline"}),
            Action(name="create_issue", kwargs={"repo_name": "ml-ops-pipeline", "title": "Validate training pipeline", "body": "Run end‑to‑end training and verify outputs.", "labels": ["mlops"]}),
            Action(name="append_terminal", kwargs={"message": "ml-ops-pipeline v0.8.0 released."}),
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
            "You are 'security-team'. When you complete the task, the repository state for 'security-scanner' must satisfy ALL of the following:\n"
            "• Branch 'main' is protected with rules exactly {\"require_reviews\": true, \"require_status_checks\": true, \"enforce_admins\": true}.\n"
            "• An issue exists titled 'Security audit required' with body 'Run compliance checks on encryption and password policies.' labeled 'security'.\n"
            "• The repository's code scanning alerts are listed.\n"
            "• The terminal audit log contains the EXACT entry 'security-scanner security audit scheduled with branch protection enforced.'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "security-team"}),
            Action(name="get_repository", kwargs={"repo_name": "security-scanner"}),
            Action(name="set_branch_protection", kwargs={
                "repo_name": "security-scanner",
                "branch": "main",
                "protected": "true",
                "rules": {"require_reviews": "true", "require_status_checks": "true", "enforce_admins": "true"},
            }),
            Action(name="create_issue", kwargs={
                "repo_name": "security-scanner",
                "title": "Security audit required",
                "body": "Run compliance checks on encryption and password policies.",
                "labels": ["security"]
            }),
            Action(name="list_code_scanning_alerts", kwargs={"repo_name": "security-scanner"}),
            Action(name="append_terminal", kwargs={
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
            "You are 'bob-dev'. Deliver the following end state, with all values exact and case-sensitive:\n"
            "• A repository named 'log-analyzer' exists and is owned by you; its visibility is 'public' and its default branch is 'main'. The repository topics include both 'logs' and 'analysis'.\n"
            "• A branch 'feature-alerts' exists. On that branch, the file 'src/alerts.py' contains exactly 'print('alert-v1')' and the file 'docs/alerts.md' contains exactly '# Log alerts'.\n"
            "• The latest commit on 'feature-alerts' includes the message 'Add log alerting support'.\n"
            "• Pull request #1 targets base 'main' from head 'feature-alerts' with title 'Introduce log alerting' and body 'Add alerting support and docs.', is approved, and is merged.\n"
            "• Branch protection is enabled on branch 'main' with rules exactly {'required_reviews': 1}.\n"
            "• A release exists on 'log-analyzer' with tag 'v1.2.0', title 'Log alerting', and body 'Adds alerting support for log analyzer.'.\n"
            "• An issue titled 'Refine alert thresholds' exists with body 'Tune thresholds for production logs.' labeled 'alerts'.\n"
            "• The terminal log includes exactly one appended entry with the message 'log-analyzer v1.2.0 released.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "bob-dev"}),
            Action(name="create_repository", kwargs={"repo_name": "log-analyzer", "visibility": "public", "default_branch": "main"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "log-analyzer", "topic": "logs"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "log-analyzer", "topic": "analysis"}),
            Action(name="create_branch", kwargs={"repo_name": "log-analyzer", "source_branch": "main", "new_branch": "feature-alerts"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "log-analyzer", "branch": "feature-alerts", "path": "src/alerts.py", "content": "print('alert-v1')"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "log-analyzer", "branch": "feature-alerts", "path": "docs/alerts.md", "content": "# Log alerts"}),
            Action(name="commit_changes_to_branch", kwargs={"repo_name": "log-analyzer", "branch": "feature-alerts", "commit_message": "Add log alerting support"}),
            Action(name="create_pull_request", kwargs={"repo_name": "log-analyzer", "title": "Introduce log alerting", "body": "Add alerting support and docs.", "base": "main", "head": "feature-alerts"}),
            Action(name="create_pull_request_review", kwargs={"repo_name": "log-analyzer", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "log-analyzer", "pr_number": 1}),
            Action(name="set_branch_protection", kwargs={"repo_name": "log-analyzer", "branch": "main", "protected": "true", "rules": {"required_reviews": 1}}),
            Action(name="create_release", kwargs={"repo_name": "log-analyzer", "tag": "v1.2.0", "title": "Log alerting", "body": "Adds alerting support for log analyzer."}),
            Action(name="create_issue", kwargs={"repo_name": "log-analyzer", "title": "Refine alert thresholds", "body": "Tune thresholds for production logs.", "labels": ["alerts"]}),
            Action(name="append_terminal", kwargs={"message": "log-analyzer v1.2.0 released."}),
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
            "You are 'security-team'. When you complete the task, the repository state for 'security-scanner' must satisfy ALL of the following:\n"
            "• Branch 'main' is protected with rules exactly {\"require_reviews\": \"true\", \"require_status_checks\": \"true\", \"enforce_admins\": \"true\"}.\n"
            "• Repository visibility is 'private'.\n"
            "• Repository topics include 'compliance'.\n"
            "• An issue exists titled 'Annual compliance baseline' with body 'Baseline checks for encryption and password rotation.' labeled ['security','compliance'], and it has a comment exactly 'Baseline scheduled for Q4.'\n"
            "• The terminal audit log contains the EXACT entry 'security-scanner compliance baseline scheduled with protections enforced.'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "security-team"}),
            Action(name="get_repository", kwargs={"repo_name": "security-scanner"}),
            Action(name="set_branch_protection", kwargs={
                "repo_name": "security-scanner",
                "branch": "main",
                "protected": "true",
                "rules": {"require_reviews": "true", "require_status_checks": "true", "enforce_admins": "true"},
            }),
            Action(name="set_repository_visibility", kwargs={
                "repo_name": "security-scanner",
                "visibility": "private",
            }),
            Action(name="add_repo_topic", kwargs={
                "repo_name": "security-scanner",
                "topic": "compliance",
            }),
            Action(name="list_repo_topics", kwargs={"repo_name": "security-scanner"}),
            Action(name="create_issue", kwargs={
                "repo_name": "security-scanner",
                "title": "Annual compliance baseline",
                "body": "Baseline checks for encryption and password rotation.",
                "labels": ["security", "compliance"],
            }),
            Action(name="add_issue_comment", kwargs={
                "repo_name": "security-scanner",
                "issue_number": 1,
                "comment": "Baseline scheduled for Q4.",
            }),
            Action(name="append_terminal", kwargs={
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
            "You are 'qa-erin'. Deliver the following end state, with all values exact and case-sensitive:\n"
            "• A repository named 'automation-tests' exists and is owned by you; its visibility is 'public' and its default branch is 'main'. The repository topics include both 'tests' and 'automation'.\n"
            "• A branch 'feature-selenium' exists. On that branch, the file 'tests/selenium_test.py' contains exactly 'print('selenium-v1')' and the file 'docs/tests.md' contains exactly '# Selenium tests'.\n"
            "• The latest commit on 'feature-selenium' includes the message 'Add selenium test suite'.\n"
            "• Pull request #1 targets base 'main' from head 'feature-selenium' with title 'Add selenium tests' and body 'Introduce selenium test automation.', is approved, and is merged.\n"
            "• Branch protection is enabled on branch 'main' with rules exactly {'required_reviews': 1}.\n"
            "• A release exists on 'automation-tests' with tag 'v0.5.0', title 'Selenium suite', and body 'Initial selenium automation suite.'.\n"
            "• An issue titled 'Expand selenium coverage' exists with body 'Add cross-browser tests.' labeled 'qa'.\n"
            "• The terminal log includes exactly one appended entry with the message 'automation-tests v0.5.0 released.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "qa-erin"}),
            Action(name="create_repository", kwargs={"repo_name": "automation-tests", "visibility": "public", "default_branch": "main"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "automation-tests", "topic": "tests"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "automation-tests", "topic": "automation"}),
            Action(name="create_branch", kwargs={"repo_name": "automation-tests", "source_branch": "main", "new_branch": "feature-selenium"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "automation-tests", "branch": "feature-selenium", "path": "tests/selenium_test.py", "content": "print('selenium-v1')"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "automation-tests", "branch": "feature-selenium", "path": "docs/tests.md", "content": "# Selenium tests"}),
            Action(name="commit_changes_to_branch", kwargs={"repo_name": "automation-tests", "branch": "feature-selenium", "commit_message": "Add selenium test suite"}),
            Action(name="create_pull_request", kwargs={"repo_name": "automation-tests", "title": "Add selenium tests", "body": "Introduce selenium test automation.", "base": "main", "head": "feature-selenium"}),
            Action(name="create_pull_request_review", kwargs={"repo_name": "automation-tests", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "automation-tests", "pr_number": 1}),
            Action(name="set_branch_protection", kwargs={"repo_name": "automation-tests", "branch": "main", "protected": "true", "rules": {"required_reviews": 1}}),
            Action(name="create_release", kwargs={"repo_name": "automation-tests", "tag": "v0.5.0", "title": "Selenium suite", "body": "Initial selenium automation suite."}),
            Action(name="create_issue", kwargs={"repo_name": "automation-tests", "title": "Expand selenium coverage", "body": "Add cross-browser tests.", "labels": ["qa"]}),
            Action(name="append_terminal", kwargs={"message": "automation-tests v0.5.0 released."}),
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
            "You are 'release-manager'. Deliver the following end state, with all values exact and case-sensitive:\n"
            "• A repository initially named 'release-runbooks' is created by you as 'private' with default branch 'main', then renamed to 'release-ops' and its visibility is 'public'. The repository topics end up as exactly ['release'] (the topic 'runbooks' was present earlier but is not present at the end).\n"
            "• A branch 'feature-runbooks' exists. On that branch, the file 'docs/runbook.md' contains exactly '# Release runbook v1'.\n"
            "• The latest commit on 'feature-runbooks' includes the message 'Add initial release runbook'.\n"
            "• Issue #1 exists in 'release-ops' titled 'Prepare v1.0 checklist' with body 'Checklist for release v1.0.', labeled with both 'release' and 'checklist', and includes exactly one comment with the text 'Checklist created.'\n"
            "• Branch protection is enabled on branch 'main' with rules exactly {'required_reviews': 1}.\n"
            "• A release exists on 'release-ops' with tag 'v1.0.0', title 'Release operations v1', and body 'Initial runbooks.'.\n"
            "• The terminal log includes exactly one appended entry with the message 'release-ops v1.0.0 published.'\n"
            "All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "release-manager"}),
            Action(name="create_repository", kwargs={"repo_name": "release-runbooks", "visibility": "private", "default_branch": "main"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "release-runbooks", "topic": "release"}),
            Action(name="add_repo_topic", kwargs={"repo_name": "release-runbooks", "topic": "runbooks"}),
            Action(name="rename_repository", kwargs={"old_name": "release-runbooks", "new_name": "release-ops"}),
            Action(name="set_repository_visibility", kwargs={"repo_name": "release-ops", "visibility": "public"}),
            Action(name="create_branch", kwargs={"repo_name": "release-ops", "source_branch": "main", "new_branch": "feature-runbooks"}),
            Action(name="write_file_to_branch", kwargs={"repo_name": "release-ops", "branch": "feature-runbooks", "path": "docs/runbook.md", "content": "# Release runbook v1"}),
            Action(name="commit_changes_to_branch", kwargs={"repo_name": "release-ops", "branch": "feature-runbooks", "commit_message": "Add initial release runbook"}),
            Action(name="create_issue", kwargs={"repo_name": "release-ops", "title": "Prepare v1.0 checklist", "body": "Checklist for release v1.0.", "labels": ["release"]}),
            Action(name="add_issue_comment", kwargs={"repo_name": "release-ops", "issue_number": 1, "comment": "Checklist created."}),
            Action(name="add_label_to_issue", kwargs={"repo_name": "release-ops", "issue_number": 1, "label": "checklist"}),
            Action(name="set_branch_protection", kwargs={"repo_name": "release-ops", "branch": "main", "protected": "true", "rules": {"required_reviews": 1}}),
            Action(name="create_release", kwargs={"repo_name": "release-ops", "tag": "v1.0.0", "title": "Release operations v1", "body": "Initial runbooks."}),
            Action(name="remove_repo_topic", kwargs={"repo_name": "release-ops", "topic": "runbooks"}),
            Action(name="append_terminal", kwargs={"message": "release-ops v1.0.0 published."}),
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

    # 69. (ui-team) Two branches -> two PRs -> list open PRs  (Hard ~14 edges)
    Task(
        annotator='0',
        user_id="task_69",
        instruction=(
            "You are 'ui-team'. In 'ui-kit', create two feature branches from 'main' and open two PRs, then list open PRs.\n"
            "Branches & files:\n"
            " - feature-a: docs/featA.md = '# Feat A\\n'\n"
            " - feature-b: docs/featB.md = '# Feat B\\n'\n"
            "PRs:\n"
            " - title 'Add feature A docs' (head=feature-a -> base=main)\n"
            " - title 'Add feature B docs' (head=feature-b -> base=main)\n"
            "Return both PR titles and the titles from list_open_pull_requests."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "ui-team"}),

            # PR #1 path
            Action(name="create_branch", kwargs={"repo_name": "ui-kit", "source_branch": "main", "new_branch": "feature-a"}),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "ui-kit", "branch": "feature-a",
                "path": "docs/featA.md", "content": "# Feat A\n",
                "commit_message": "Add feature A docs",
            }),
            Action(name="create_pull_request", kwargs={
                "repo_name": "ui-kit",
                "title": "Add feature A docs",
                "head": "feature-a",
                "base": "main"
            }),

            # PR #2 path
            Action(name="create_branch", kwargs={"repo_name": "ui-kit", "source_branch": "main", "new_branch": "feature-b"}),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "ui-kit", "branch": "feature-b",
                "path": "docs/featB.md", "content": "# Feat B\n",
                "commit_message": "Add feature B docs",
            }),
            Action(name="create_pull_request", kwargs={
                "repo_name": "ui-kit",
                "title": "Add feature B docs",
                "head": "feature-b",
                "base": "main"
            }),

            # Summary
            Action(name="list_open_pull_requests", kwargs={"repo_name": "ui-kit"}),
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
            "You are 'ops-team'. In repository 'infra-terraform', you ensure this end state: "
            "There is exactly one open pull request targeting the default branch 'main'. "
            "PR #1 uses head branch 'feature-docs-a' and consists of a single file 'docs/A.md' "
            "with the exact content '# Doc A\\n'; its exact title is 'Docs: add A' and exact body is 'Adds docs/A.md.'. "
            "Finally, you return the exact tool result of listing open pull requests for 'infra-terraform', "
            "and the exact tool result listing the files changed in the most recently opened PR."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "ops-team"}),
            Action(name="get_repository", kwargs={"repo_name": "infra-terraform"}),
            Action(name="get_default_branch", kwargs={"repo_name": "infra-terraform"}),

            # PR #1
            Action(name="create_branch", kwargs={
                "repo_name": "infra-terraform", "source_branch": "main", "new_branch": "feature-docs-a"
            }),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "infra-terraform", "branch": "feature-docs-a",
                "path": "docs/A.md", "content": "# Doc A\n"
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "infra-terraform", "branch": "feature-docs-a",
                "commit_message": "Docs: add A"
            }),
            Action(name="create_pull_request", kwargs={
                "repo_name": "infra-terraform", "title": "Docs: add A",
                "body": "Adds docs/A.md.", "base": "main", "head": "feature-docs-a"
            }),

            # # PR #2
            # Action(name="create_branch", kwargs={
            #     "repo_name": "infra-terraform", "source_branch": "main", "new_branch": "feature-docs-b"
            # }),
            # Action(name="write_file_to_branch", kwargs={
            #     "repo_name": "infra-terraform", "branch": "feature-docs-b",
            #     "path": "docs/B.md", "content": "# Doc B\n"
            # }),
            # Action(name="commit_changes_to_branch", kwargs={
            #     "repo_name": "infra-terraform", "branch": "feature-docs-b",
            #     "commit_message": "Docs: add B"
            # }),
            # Action(name="create_pull_request", kwargs={
            #     "repo_name": "infra-terraform", "title": "Docs: add B",
            #     "body": "Adds docs/B.md.", "base": "main", "head": "feature-docs-b"
            # }),

            # Outputs
            Action(name="list_open_pull_requests", kwargs={"repo_name": "infra-terraform"}),

            Action(name="list_pull_request_files", kwargs={
                "repo_name": "infra-terraform",
                "pr_number": 1
            }),
        ],
        outputs=[
            '"pull_requests": [{"number": 1, "title": "Docs: add A", "state": "open", "base": "main", "head": "feature-docs-a"}]',
            '"most_recent_pr_files": "files": ["docs/A.md"]'
        ],
    ),

    # 71. (alice-w) Open a PR that introduces SECURITY.md and return the PR file list (deterministic)
    Task(
        annotator='0',
        user_id="task_71",
        instruction=(
            "You are 'alice-w'. Deliver a pull request in 'acme-webapp' from branch 'feature-security-doc' into 'main' "
            "that adds a new file named SECURITY.md with exactly this content:\n"
            "# Security Policy\n\n"
            "To report vulnerabilities, email security@enterprise.com.\n"
            "We aim to triage within 2 business days.\n"
            "Use PR title 'Add SECURITY.md', body 'Introduces a basic security policy and disclosure contact.', "
            "and commit message 'docs: add SECURITY.md with contact and triage info'. Return that PR’s file list."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="get_repository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="get_default_branch", kwargs={"repo_name": "acme-webapp"}),
            Action(
                name="create_branch",
                kwargs={"repo_name": "acme-webapp", "source_branch": "main", "new_branch": "feature-security-doc"},
            ),
            Action(
                name="write_file_to_branch",
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
                name="create_pull_request",
                kwargs={
                    "repo_name": "acme-webapp",
                    "title": "Add SECURITY.md",
                    "body": "Introduces a basic security policy and disclosure contact.",
                    "head": "feature-security-doc",
                    "base": "main",
                },
            ),
            # Validator will inject the accurate PR number if different.
            Action(name="list_pull_request_files", kwargs={"repo_name": "acme-webapp", "pr_number": 1}),
        ],
        outputs=[
            '"message": "Pull request opened",'
            '"title": "Add SECURITY.md",'
            '"base": "main",'
            '"head": "feature-security-doc"',
            # Our tool returns the full file set for the PR’s head branch.
            '"files": ["SECURITY.md"]',
        ],
    ),

    # 72. (alice-w) Apply the same label to issues #3 and #8, leave a deterministic note, then list by that label
    Task(
        annotator='0',
        user_id="task_72",
        instruction=(
            "You are 'alice-w'. In 'acme-webapp', apply the label 'triage-urgent' to issues #3 and #8, "
            "then post the exact comment 'Labels applied: triage-urgent, quality.' on both issues, "
            "and return the list of issue numbers that have label 'triage-urgent'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="get_repository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="add_label_to_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "label": "triage-urgent"}),
            Action(name="add_label_to_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 8, "label": "triage-urgent"}),
            Action(
                name="add_issue_comment",
                kwargs={"repo_name": "acme-webapp", "issue_number": 3, "comment": "Labels applied: triage-urgent, quality."},
            ),
            Action(
                name="add_issue_comment",
                kwargs={"repo_name": "acme-webapp", "issue_number": 8, "comment": "Labels applied: triage-urgent, quality."},
            ),
            Action(name="list_issues_by_label", kwargs={"repo_name": "acme-webapp", "label": "triage-urgent"}),
        ],
        outputs=[
            '"issues_with_label_triage-urgent": [3, 8]',
        ],
    ),

    # 73. (devops-lead) Open and merge a PR, then delete its branch
    Task(
        annotator='0',
        user_id="task_73",
        instruction=(
            "You are 'devops-lead'. In 'k8s-monitoring', create a new feature branch 'feature-docs', "
            "add a file 'docs/USAGE.md' with content '# Usage Guide\n\nThis file explains how to use the monitoring stack.', open a pull request into 'main' with 'title' as 'Add usage docs', body content as 'Introduces usage documentation.', "
            "and delete after merging the feature branch."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "devops-lead"}),
            Action(name="get_repository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="get_default_branch", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="create_branch", kwargs={"repo_name": "k8s-monitoring", "new_branch": "feature-docs", "source_branch": "main"}),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "k8s-monitoring",
                "branch": "feature-docs",
                "path": "docs/USAGE.md",
                "content": "# Usage Guide\n\nThis file explains how to use the monitoring stack."
            }),
            Action(name="create_pull_request", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Add usage docs",
                "body": "Introduces usage documentation.",
                "base": "main",
                "head": "feature-docs"
            }),
            Action(name="merge_pull_request", kwargs={
                "repo_name": "k8s-monitoring",
                "pr_number": 1  # We deterministically know this will be PR #1 in sandbox
            }),
            Action(name="delete_branch", kwargs={"repo_name": "k8s-monitoring", "branch": "feature-docs"}),
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
            "You are 'ui-team'. In 'ui-kit', create a branch 'feature-license-update', update the LICENSE file "
            "with the exact content 'MIT License updated', commit it with message 'chore: update license', then open "
            "a pull request into 'main' with title 'Update LICENSE' and body 'Switch project to MIT license.', "
            "and return the list of files modified in the PR."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "ui-team"}),
            Action(name="get_repository", kwargs={"repo_name": "ui-kit"}),
            Action(name="get_default_branch", kwargs={"repo_name": "ui-kit"}),
            Action(
                name="create_branch",
                kwargs={"repo_name": "ui-kit", "source_branch": "main", "new_branch": "feature-license-update"},
            ),
            Action(
                name="write_file_to_branch",
                kwargs={
                    "repo_name": "ui-kit",
                    "branch": "feature-license-update",
                    "path": "LICENSE",
                    "content": "MIT License updated",
                    "commit_message": "chore: update license",
                },
            ),
            Action(
                name="create_pull_request",
                kwargs={
                    "repo_name": "ui-kit",
                    "title": "Update LICENSE",
                    "body": "Switch project to MIT license.",
                    "head": "feature-license-update",
                    "base": "main",
                },
            ),
            Action(
                name="list_pull_request_files",
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
            "You are 'devops-lead'. You are preparing the 'acme-bootstrap' repository for team onboarding. Ensure that it has a protected default branch named 'main', a working branch named 'setup-work' with initial project files, and that a triage issue is created to coordinate setup tasks. "
            "Use these exact details:\n"
            "- Files: 'README.md' with content '# Bootstrap repository.' and '.gitignore' with content '.DS_Store\\nnode_modules/\\n__pycache__/\\n'\n"
            "- Branch protection on 'main': require_pull_request_reviews=true, dismiss_stale_reviews=true, enforce_admins=true, required_status_checks=['build']\n"
            "- Issue: title='Initial setup checklist', body='Track bootstrap tasks for this repo.', labels=['triage', 'setup']\n"
            "- Commit messages: 'add README.md', 'add .gitignore'\n"
            "Return: (1) the protection rule block for 'main', and (2) the final issue object with its labels"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "devops-lead"}),

            Action(name="create_repository", kwargs={
                "repo_name": "acme-bootstrap",
                "default_branch": "main"
            }),

            Action(name="set_branch_protection", kwargs={
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

            Action(name="create_branch", kwargs={
                "repo_name": "acme-bootstrap",
                "source_branch": "main",
                "new_branch": "setup-work"
            }),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-bootstrap",
                "branch": "setup-work",
                "path": "README.md",
                "content": "# Bootstrap repository."
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "acme-bootstrap",
                "branch": "setup-work",
                "commit_message": "add README.md"
            }),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-bootstrap",
                "branch": "setup-work",
                "path": ".gitignore",
                "content": ".DS_Store\\nnode_modules/\\n__pycache__/\\n"
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "acme-bootstrap",
                "branch": "setup-work",
                "commit_message": "add .gitignore"
            }),

            Action(name="create_issue", kwargs={
                "repo_name": "acme-bootstrap",
                "title": "Initial setup checklist",
                "body": "Track bootstrap tasks for this repo.",
                "labels": ["triage", "setup"]
            }),

            Action(name="get_branch_protection", kwargs={
                "repo_name": "acme-bootstrap",
                "branch": "main"
            }),
            Action(name="get_issue", kwargs={
                "repo_name": "acme-bootstrap",
                "issue_number": 1
            }),
        ],
        outputs=[
            "{'require_pull_request_reviews': 'true', 'dismiss_stale_reviews': 'true', 'enforce_admins': 'true', 'required_status_checks': ['build']}",
            "{'number': 1, 'title': 'Initial setup checklist', 'labels': ['triage', 'setup'], 'state': 'open'}",
        ],
    ),

    # 76. PR with multi-file changes + list PR files (9 actions) — FIXED
    Task(
        annotator='0',
        user_id="task_76",
        instruction=(
            "You are 'alice-w' working on the 'acme-webapp' service. Submit a pull request from a feature branch named 'feat-auth' into the default 'main' branch. "
            "The PR should introduce the following files:\n"
            "  • api/__init__.py with content 'main()'\n"
            "  • api/auth.py with content 'class Auth: pass'\n"
            "  • tests/test_auth.py with content 'def test_stub(): assert True'\n"
            "Use commit message: 'feat-auth: scaffolding and tests'\n"
            "Use PR title: 'Add auth scaffolding' and body: 'Introduce basic auth module skeleton.'\n"
            "Return the list of files changed in the PR."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="create_branch", kwargs={
                "repo_name": "acme-webapp",
                "source_branch": "main",
                "new_branch": "feat-auth"
            }),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-webapp", "branch": "feat-auth",
                "path": "api/__init__.py", "content": "main()"
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feat-auth",
                "commit_message": "feat-auth: scaffolding and tests"
            }),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-webapp", "branch": "feat-auth",
                "path": "api/auth.py", "content": "class Auth: pass"
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feat-auth",
                "commit_message": "feat-auth: scaffolding and tests"
            }),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-webapp", "branch": "feat-auth",
                "path": "tests/test_auth.py", "content": "def test_stub(): assert True"
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feat-auth",
                "commit_message": "feat-auth: scaffolding and tests"
            }),

            Action(name="create_pull_request", kwargs={
                "repo_name": "acme-webapp",
                "title": "Add auth scaffolding",
                "body": "Introduce basic auth module skeleton.",
                "head": "feat-auth",
                "base": "main"
            }),
            Action(name="list_pull_request_files", kwargs={
                "repo_name": "acme-webapp",
                "pr_number": 1
            }),
        ],
        outputs=[
            "{'files': ['api/__init__.py', 'api/auth.py', 'tests/test_auth.py']}",
        ],
    ),

    # 77. CI config + CHANGELOG + release publish + verify (10 actions)
    Task(
        annotator='0',
        user_id="task_77",
        instruction=(
            "You are 'alice-w' preparing the first release for the existing public repository 'acme-webapp'. "
            "After configuring the build pipeline and changelog on the default branch 'main', publish version 'v0.1.0' as an initial release with appropriate metadata. "
            "Use the following details:\n"
            "- File '.github/workflows/ci.yml' should contain: 'Triggers CI workflows'\n"
            "- File 'CHANGELOG.md' should contain: '# Changelog  ## v0.1.0 - Initial release'\n"
            "- Commit message: 'ci+docs: add CI workflow and CHANGELOG'\n"
            "- Release:\n"
            "  • Tag: 'v0.1.0'\n"
            "  • Title: 'v0.1.0'\n"
            "  • Body: 'Initial release'\n"
            "Return the release metadata as returned by the release tool."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "main",
                "path": ".github/workflows/ci.yml",
                "content": "Triggers CI workflows"
            }),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "main",
                "path": "CHANGELOG.md",
                "content": "# Changelog  ## v0.1.0 - Initial release"
            }),

            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "main",
                "commit_message": "ci+docs: add CI workflow and CHANGELOG"
            }),

            Action(name="create_release", kwargs={
                "repo_name": "acme-webapp",
                "tag": "v0.1.0",
                "title": "v0.1.0",
                "body": "Initial release"
            }),

            Action(name="get_latest_release", kwargs={"repo_name": "acme-webapp"}),
        ],
        outputs=[
            # Must exactly match the get_latest_release tool output schema
            "{'tag_name': 'v0.1.0', 'body': 'Initial release'}",
        ],
    ),

    # 81. (devops-lead) New repo + branch protection + runbook PR → issue closed → release + comment
    Task(
        annotator='0',
        user_id="task_81",
        instruction=(
            "You are 'devops-lead' working in a new repository 'infra-runbooks'. Deliver an incident runbook setup such that, "
            "after completion, the repository state satisfies ALL acceptance criteria below while using the exact constants provided. "
            "Treat this as a specification of outcomes and literals, NOT step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (final state must reflect all of these):\n"
            "• A repository named 'infra-runbooks' exists (public) with default branch 'main'.\n"
            "• A feature branch contains an incident runbook file with the exact content below and a committed change.\n"
            "• Repository topics include the exact topic listed.\n"
            "• The default branch 'main' has branch protection enabled with the exact protected flag and rules JSON below.\n"
            "• Issue number 1 is closed, and contains the exact pre-PR and post-release comments below.\n"
            "• A pull request (number 1 after reset) from the feature branch into 'main' is merged.\n"
            "• A release with the exact tag below exists.\n\n"
            "CONSTANTS TO USE VERBATIM (all literals must match exactly):\n"
            "- Repository visibility: public\n"
            "- Default branch name: main\n"
            "- Feature branch name: feature-incident-101\n"
            "- File path: docs/incidents/101.md\n"
            "- File content (exact; SINGLE trailing newline only):\n"
            "# Incident 101: First Response\n\nSteps:\n1. Page on-call\n2. Gather logs\n3. Mitigate blast radius\n\nOwner: SRE\n"
            "- Commit message: docs: add incident 101 guide\n"
            "- Repository topic to add: runbooks\n"
            "- Branch protection target: main\n"
            "- Branch protection 'protected' value: \"true\"\n"
            "- Branch protection rules JSON (use exactly this object): {\"required_status_checks\": [\"ci\"], \"enforce_admins\": \"true\"}\n"
            "- Issue to create/label/close: 1\n"
            "- Issue title: Add incident 101 runbook\n"
            "- Issue body: Track and document initial incident response.\n"
            "- Label to add: documentation\n"
            "- Pre-PR issue comment: Runbook authored; PR will close this issue.\n"
            "- PR title: Add incident 101 runbook\n"
            "- PR body: Closes #1\n"
            "- Pull request review decision: approve\n"
            "- Release tag: v1.0.0-incidents\n"
            "- Release body: First incident runbook.\n"
            "- Post-release issue comment: Shipped in 'v1.0.0-incidents'\n"
        ),
        actions=[
            # Auth & create repo
            Action(name="get_me", kwargs={"username": "devops-lead"}),
            Action(name="create_repository", kwargs={"repo_name": "infra-runbooks", "visibility": "public", "default_branch": "main"}),

            # Resolve default & create feature branch
            Action(name="get_default_branch", kwargs={"repo_name": "infra-runbooks"}),
            Action(name="create_branch", kwargs={"repo_name": "infra-runbooks", "new_branch": "feature-incident-101", "source_branch": "main"}),

            # Write and commit runbook
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "infra-runbooks",
                "branch": "feature-incident-101",
                "path": "docs/incidents/101.md",
                "content": "# Incident 101: First Response\n\nSteps:\n1. Page on-call\n2. Gather logs\n3. Mitigate blast radius\n\nOwner: SRE\n",
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "infra-runbooks",
                "branch": "feature-incident-101",
                "commit_message": "docs: add incident 101 guide",
            }),

            # Topic + branch protection
            Action(name="add_repo_topic", kwargs={"repo_name": "infra-runbooks", "topic": "runbooks"}),
            Action(name="set_branch_protection", kwargs={
                "repo_name": "infra-runbooks",
                "branch": "main",
                "protected": "true",
                "rules": {"required_status_checks": ["ci"], "enforce_admins": "true"},
            }),

            # Issue lifecycle
            Action(name="create_issue", kwargs={
                "repo_name": "infra-runbooks",
                "title": "Add incident 101 runbook",
                "body": "Track and document initial incident response.",
            }),
            Action(name="add_label_to_issue", kwargs={"repo_name": "infra-runbooks", "issue_number": 1, "label": "documentation"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "infra-runbooks", "issue_number": 1, "comment": "Runbook authored; PR will close this issue."}),

            # PR → review → merge
            Action(name="create_pull_request", kwargs={
                "repo_name": "infra-runbooks",
                "title": "Add incident 101 runbook",
                "body": "Closes #1",
                "head": "feature-incident-101",
                "base": "main",
            }),
            Action(name="create_pull_request_review", kwargs={"repo_name": "infra-runbooks", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "infra-runbooks", "pr_number": 1}),

            # Close issue, release, annotate
            Action(name="update_issue", kwargs={"repo_name": "infra-runbooks", "issue_number": 1, "state": "closed"}),
            Action(name="create_release", kwargs={"repo_name": "infra-runbooks", "tag": "v1.0.0-incidents", "body": "First incident runbook."}),
            Action(name="add_issue_comment", kwargs={"repo_name": "infra-runbooks", "issue_number": 1, "comment": "Shipped in 'v1.0.0-incidents'"}),
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
            "You are 'bob-dev'. In 'utils-js', confirm that PR #16 resolving Issue #7 is merged. Track TypeScript declaration support in PR #14 by commenting: 'Tracking TypeScript declarations in PR #14'. Add a repository topic 'typescript' and post on Issue #4: 'TS support is tracked in PR #14'. Append terminal: 'utils-js TS support tracked and negative currency fix verified'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "bob-dev"}),
            Action(name="get_repository", kwargs={"repo_name": "utils-js"}),
            Action(name="get_pull_request", kwargs={"repo_name": "utils-js", "pr_number": 16}),
            Action(name="get_issue", kwargs={"repo_name": "utils-js", "issue_number": 7}),
            Action(name="get_pull_request", kwargs={"repo_name": "utils-js", "pr_number": 14}),
            Action(name="comment_on_pull_request", kwargs={
                "repo_name": "utils-js",
                "pr_number": 14,
                "comment": "Tracking TypeScript declarations in PR #14"
            }),
            Action(name="add_repo_topic", kwargs={"repo_name": "utils-js", "topic": "typescript"}),
            Action(name="add_issue_comment", kwargs={
                "repo_name": "utils-js",
                "issue_number": 4,
                "comment": "TS support is tracked in PR #14"
            }),
            Action(name="append_terminal", kwargs={"message": "utils-js TS support tracked and negative currency fix verified"}),
        ],
        outputs=['"message": "utils-js TS support tracked and negative currency fix verified"'],
    ),

    # 86. (alice-w) CI + Security update (non-procedural; deterministic)
    Task(
        annotator='0',
        user_id="task_86",
        instruction=(
            "You are 'alice-w' working in repository 'acme-webapp'. You have to deliver a CI/security update such that, upon completion, "
            "the repository state satisfies ALL acceptance criteria below while using the exact constants provided. "
            "Avoid interpreting this text as step-by-step guidance; it is a specification of outcomes and literals.\n\n"
            "ACCEPTANCE CRITERIA (final state must reflect all of these):\n"
            "• A feature branch exists and the change set is present on that branch.\n"
            "• A new issue (number 1 after reset) is closed.\n"
            "• A pull request (number 1 after reset) is merged into the default branch.\n"
            "• A release with the exact tag below exists.\n"
            "• The closed issue contains the exact post-release comment.\n\n"
            "CONSTANTS TO USE VERBATIM (all literals must match exactly):\n"
            "- Feature branch name: feature-ci-policy\n"
            "- Base branch name: main\n"
            "- File path #1: SECURITY.md\n"
            "- File content #1 (exact; SINGLE trailing newline only):\n"
            "# Security Policy\n\nReport: security@enterprise.com\nTriage: 2 business days\n"
            "- File path #2: .github/workflows/ci.yml\n"
            "- File content #2 (exact text):\n"
            "name: CI\non: [push, pull_request]\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - run: echo Build OK\n"
            "- Commit message: ci: add SECURITY.md and CI workflow\n"
            "- Issue title: Enforce CI and security policy\n"
            "- Issue body: Track CI rollout for branch feature-ci-policy.\n"
            "- Label to add: compliance\n"
            "- Pre-PR issue comment: PR will reference and close this issue.\n"
            "- PR title: CI: add security policy and workflow\n"
            "- PR body: Closes #1\n"
            "- Release tag: v0.1.0-ci\n"
            "- Post-release issue comment: Released in 'v0.1.0-ci'\n"
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="get_repository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="get_default_branch", kwargs={"repo_name": "acme-webapp"}),
            Action(name="get_head_sha", kwargs={"repo_name": "acme-webapp", "branch": "main"}),

            Action(name="create_branch", kwargs={"repo_name": "acme-webapp", "new_branch": "feature-ci-policy", "source_branch": "main"}),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-ci-policy",
                "path": "SECURITY.md",
                "content": "# Security Policy\n\nReport: security@enterprise.com\nTriage: 2 business days\n",
            }),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-ci-policy",
                "path": ".github/workflows/ci.yml",
                "content": "name: CI\non: [push, pull_request]\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - run: echo Build OK\n",
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-ci-policy",
                "commit_message": "ci: add SECURITY.md and CI workflow",
            }),

            Action(name="create_issue", kwargs={
                "repo_name": "acme-webapp",
                "title": "Enforce CI and security policy",
                "body": "Track CI rollout for branch feature-ci-policy.",
            }),
            Action(name="add_label_to_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 1, "label": "compliance"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "acme-webapp", "issue_number": 1, "comment": "PR will reference and close this issue."}),

            Action(name="create_pull_request", kwargs={
                "repo_name": "acme-webapp",
                "title": "CI: add security policy and workflow",
                "body": "Closes #1",
                "head": "feature-ci-policy",
                "base": "main",
            }),
            Action(name="create_pull_request_review", kwargs={"repo_name": "acme-webapp", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 1}),

            Action(name="update_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 1, "state": "closed"}),

            Action(name="create_release", kwargs={"repo_name": "acme-webapp", "tag": "v0.1.0-ci"}),
            Action(name="get_latest_release", kwargs={"repo_name": "acme-webapp"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "acme-webapp", "issue_number": 1, "comment": "Released in 'v0.1.0-ci'"}),
        ],
        outputs=[
            '"message": "Pull request merged", "repo_name": "acme-webapp"',
            '"pr_number": 1, "issue_number": 1, "release_tag": "v0.1.0-ci"',
        ],
    ),

    # 87. (backend-core) 3DS flow: implement config, PR, merge, close issue, release
    Task(
        annotator='0',
        user_id="task_87",
        instruction=(
            "You are 'backend-core' working in repository 'payments-service'. Deliver a 3DS feature update such that, "
            "after completion, the repository state satisfies ALL acceptance criteria below while using the exact "
            "constants provided. Treat this as a specification of outcomes and literals, not step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (final state must reflect all of these):\n"
            "• A feature branch exists that contains the 3DS configuration change.\n"
            "• Issue number 13 is closed.\n"
            "• A pull request (number 1 after reset for this repo context) is merged into the default branch.\n"
            "• A release with the exact tag below exists.\n"
            "• The closed issue contains the exact post-release comment.\n\n"
            "CONSTANTS TO USE VERBATIM (all literals must match exactly):\n"
            "- Feature branch name: feature-3ds-flow\n"
            "- Base branch name: main\n"
            "- File path: src/payments/three_ds.ts\n"
            "- File content (exact; SINGLE trailing newline only):\n"
            "export const ENABLE_3DS = true;\n"
            "- Commit message: feat(3ds): enable 3DS flow configuration\n"
            "- Issue to label and close: 13\n"
            "- Label to add: 3ds\n"
            "- Pre-PR issue comment: Implementing 3DS; PR will close this issue.\n"
            "- PR title: Enable 3DS flow configuration\n"
            "- PR body: Closes #13\n"
            "- Pull request review decision: approve\n"
            "- Release tag: v0.2.0-3ds\n"
            "- Post-release issue comment: Released in 'v0.2.0-3ds' (3DS enabled)\n"
        ),
        actions=[
            # Auth & repo context
            Action(name="get_me", kwargs={"username": "backend-core"}),
            Action(name="get_repository", kwargs={"repo_name": "payments-service"}),
            Action(name="get_default_branch", kwargs={"repo_name": "payments-service"}),
            Action(name="get_head_sha", kwargs={"repo_name": "payments-service", "branch": "main"}),

            # Feature branch
            Action(name="create_branch", kwargs={"repo_name": "payments-service", "new_branch": "feature-3ds-flow", "source_branch": "main"}),

            # Change set on feature branch
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "payments-service",
                "branch": "feature-3ds-flow",
                "path": "src/payments/three_ds.ts",
                "content": "export const ENABLE_3DS = true;\n",
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "payments-service",
                "branch": "feature-3ds-flow",
                "commit_message": "feat(3ds): enable 3DS flow configuration",
            }),

            # Work the existing issue #13 deterministically (present in dataset after reset)
            Action(name="add_label_to_issue", kwargs={"repo_name": "payments-service", "issue_number": 13, "label": "3ds"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "payments-service", "issue_number": 13, "comment": "Implementing 3DS; PR will close this issue."}),

            # PR from feature → main, explicit body to close #13
            Action(name="create_pull_request", kwargs={
                "repo_name": "payments-service",
                "title": "Enable 3DS flow configuration",
                "body": "Closes #13",
                "head": "feature-3ds-flow",
                "base": "main",
            }),
            Action(name="create_pull_request_review", kwargs={"repo_name": "payments-service", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 1}),

            # Close the issue explicitly (dataset isn’t auto-mutated by PRs)
            Action(name="update_issue", kwargs={"repo_name": "payments-service", "issue_number": 13, "state": "closed"}),

            # Release & annotate the issue
            Action(name="create_release", kwargs={"repo_name": "payments-service", "tag": "v0.2.0-3ds"}),
            Action(name="get_latest_release", kwargs={"repo_name": "payments-service"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "payments-service", "issue_number": 13, "comment": "Released in 'v0.2.0-3ds' (3DS enabled)"}),
        ],
        outputs=[
            '"message": "3DS flow merged and released", "repo_name": "payments-service"',
            '"pr_number": 1, "closed_issue": 13, "release_tag": "v0.2.0-3ds"',
        ],
    ),

    # 88. (frontend-dev) Fix WebSocket memory leak → PR merged → issue closed → release + comment
    Task(
        annotator='0',
        user_id="task_88",
        instruction=(
            "You are 'frontend-dev' working in repository 'react-dashboard'. Deliver a WebSocket leak fix such that, "
            "after completion, the repository state satisfies ALL acceptance criteria below while using the exact "
            "constants provided. Treat this as a specification of outcomes and literals, NOT step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (final state must reflect all of these):\n"
            "• A feature branch exists that contains the fix for a WebSocket cleanup-related memory leak.\n"
            "• Issue number 25 is closed.\n"
            "• A pull request (number 1 after reset for this repo) is merged into the default branch.\n"
            "• A release with the exact tag below exists.\n"
            "• The closed issue contains the exact post-release comment.\n\n"
            "CONSTANTS TO USE VERBATIM (all literals must match exactly):\n"
            "- Feature branch name: fix-memory-leak-ws\n"
            "- Base branch name: main\n"
            "- File path: src/hooks/useLiveSocket.ts\n"
            "- File content (exact; SINGLE trailing newline only):\n"
            "import { useEffect } from 'react';\n\nexport function useLiveSocket(url: string) {\n  useEffect(() => {\n    const ws = new WebSocket(url);\n    return () => {\n      ws.close();\n    };\n  }, [url]);\n}\n"
            "- Commit message: fix(ws): ensure cleanup to prevent memory leak\n"
            "- Issue to label and close: 25\n"
            "- Label to add: memory-leak\n"
            "- Pre-PR issue comment: Fix adds cleanup for WebSocket in useEffect.\n"
            "- PR title: Fix memory leak in WebSocket cleanup\n"
            "- PR body: Closes #25\n"
            "- Pull request review decision: approve\n"
            "- Release tag: v2.2.1-leakfix\n"
            "- Post-release issue comment: Patched in 'v2.2.1-leakfix'\n"
        ),
        actions=[
            # Auth & repo context
            Action(name="get_me", kwargs={"username": "frontend-dev"}),
            Action(name="get_repository", kwargs={"repo_name": "react-dashboard"}),
            Action(name="get_default_branch", kwargs={"repo_name": "react-dashboard"}),
            Action(name="get_head_sha", kwargs={"repo_name": "react-dashboard", "branch": "main"}),

            # Feature branch
            Action(name="create_branch", kwargs={"repo_name": "react-dashboard", "new_branch": "fix-memory-leak-ws", "source_branch": "main"}),

            # Change set on feature branch
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "react-dashboard",
                "branch": "fix-memory-leak-ws",
                "path": "src/hooks/useLiveSocket.ts",
                "content": "import { useEffect } from 'react';\n\nexport function useLiveSocket(url: string) {\n  useEffect(() => {\n    const ws = new WebSocket(url);\n    return () => {\n      ws.close();\n    };\n  }, [url]);\n}\n",
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "react-dashboard",
                "branch": "fix-memory-leak-ws",
                "commit_message": "fix(ws): ensure cleanup to prevent memory leak",
            }),

            # Work existing issue #25 deterministically
            Action(name="add_label_to_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "label": "memory-leak"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "comment": "Fix adds cleanup for WebSocket in useEffect."}),

            # PR from feature → main
            Action(name="create_pull_request", kwargs={
                "repo_name": "react-dashboard",
                "title": "Fix memory leak in WebSocket cleanup",
                "body": "Closes #25",
                "head": "fix-memory-leak-ws",
                "base": "main",
            }),
            Action(name="create_pull_request_review", kwargs={"repo_name": "react-dashboard", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "react-dashboard", "pr_number": 1}),

            # Close the issue explicitly
            Action(name="update_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "state": "closed"}),

            # Release & annotate the issue
            Action(name="create_release", kwargs={"repo_name": "react-dashboard", "tag": "v2.2.1-leakfix"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "react-dashboard", "issue_number": 25, "comment": "Patched in 'v2.2.1-leakfix'"}),
        ],
        outputs=[
            '"message": "WebSocket leak fix merged and released", "repo_name": "react-dashboard"',
            '"pr_number": 1, "closed_issue": 25, "release_tag": "v2.2.1-leakfix"',
        ],
    ),

    # 89. (ui-team) Icon pack completion → PR merged → issue closed → release + comment
    Task(
        annotator='0',
        user_id="task_89",
        instruction=(
            "You are 'ui-team' working in repository 'ui-kit'. Deliver an icon-pack update such that, after completion, "
            "the repository state satisfies ALL acceptance criteria below while using the exact constants provided. "
            "Treat this as a specification of outcomes and literals, NOT step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (final state must reflect all of these):\n"
            "• A feature branch exists that contains two new SVG icons.\n"
            "• Issue number 6 is closed.\n"
            "• A pull request (number 1 after reset for this repo) is merged into the default branch.\n"
            "• A release with the exact tag below exists.\n"
            "• The closed issue contains the exact post-release comment.\n\n"
            "CONSTANTS TO USE VERBATIM (all literals must match exactly):\n"
            "- Feature branch name: feature-icons-pack\n"
            "- Base branch name: main\n"
            "- File path #1: src/icons/email.svg\n"
            "- File content #1 (exact; SINGLE trailing newline only):\n"
            "<svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M2 6h20v12H2z'/><path d='M2 6l10 7L22 6'/></svg>\n"
            "- File path #2: src/icons/phone.svg\n"
            "- File content #2 (exact; SINGLE trailing newline only):\n"
            "<svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M6 2h12v20H6z'/><path d='M9 18h6'/></svg>\n"
            "- Commit message: feat(icons): add email and phone SVGs\n"
            "- Issue to label and close: 6\n"
            "- Label to add: icons\n"
            "- Pre-PR issue comment: Adding email and phone icons; PR will close this issue.\n"
            "- PR title: Add email and phone icons\n"
            "- PR body: Closes #6\n"
            "- Pull request review decision: approve\n"
            "- Release tag: v1.1.0-icons\n"
            "- Post-release issue comment: Shipped in 'v1.1.0-icons'\n"
        ),
        actions=[
            # Auth & repo context
            Action(name="get_me", kwargs={"username": "ui-team"}),
            Action(name="get_repository", kwargs={"repo_name": "ui-kit"}),
            Action(name="get_default_branch", kwargs={"repo_name": "ui-kit"}),
            Action(name="get_head_sha", kwargs={"repo_name": "ui-kit", "branch": "main"}),

            # Feature branch
            Action(name="create_branch", kwargs={"repo_name": "ui-kit", "new_branch": "feature-icons-pack", "source_branch": "main"}),

            # Change set on feature branch (two SVGs)
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "ui-kit",
                "branch": "feature-icons-pack",
                "path": "src/icons/email.svg",
                "content": "<svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M2 6h20v12H2z'/><path d='M2 6l10 7L22 6'/></svg>\n",
            }),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "ui-kit",
                "branch": "feature-icons-pack",
                "path": "src/icons/phone.svg",
                "content": "<svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'><path d='M6 2h12v20H6z'/><path d='M9 18h6'/></svg>\n",
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "ui-kit",
                "branch": "feature-icons-pack",
                "commit_message": "feat(icons): add email and phone SVGs",
            }),

            # Work existing issue #6 deterministically
            Action(name="add_label_to_issue", kwargs={"repo_name": "ui-kit", "issue_number": 6, "label": "icons"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "ui-kit", "issue_number": 6, "comment": "Adding email and phone icons; PR will close this issue."}),

            # PR from feature → main
            Action(name="create_pull_request", kwargs={
                "repo_name": "ui-kit",
                "title": "Add email and phone icons",
                "body": "Closes #6",
                "head": "feature-icons-pack",
                "base": "main",
            }),
            Action(name="create_pull_request_review", kwargs={"repo_name": "ui-kit", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 1}),

            # Close the issue explicitly
            Action(name="update_issue", kwargs={"repo_name": "ui-kit", "issue_number": 6, "state": "closed"}),

            # Release & annotate the issue
            Action(name="create_release", kwargs={"repo_name": "ui-kit", "tag": "v1.1.0-icons"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "ui-kit", "issue_number": 6, "comment": "Shipped in 'v1.1.0-icons'"}),
        ],
        outputs=[
            '"message": "Icon pack merged and released", "repo_name": "ui-kit"',
            '"pr_number": 1, "closed_issue": 6, "release_tag": "v1.1.0-icons"',
        ],
    ),

    # 90. (devops-lead) Grafana performance tweak → PR merged → issue closed → release + comment
    Task(
        annotator='0',
        user_id="task_90",
        instruction=(
            "You are 'devops-lead' working in repository 'k8s-monitoring'. Deliver a Grafana performance improvement such that, "
            "after completion, the repository state satisfies ALL acceptance criteria below while using the exact constants provided. "
            "Treat this as a specification of outcomes and literals, NOT step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (final state must reflect all of these):\n"
            "• A feature branch exists that contains a documented performance optimization for Grafana dashboards.\n"
            "• Issue number 35 is closed.\n"
            "• A pull request (number 1 after reset for this repo) is merged into the default branch.\n"
            "• A release with the exact tag below exists.\n"
            "• The closed issue contains the exact post-release comment.\n\n"
            "CONSTANTS TO USE VERBATIM (all literals must match exactly):\n"
            "- Feature branch name: fix-grafana-performance\n"
            "- Base branch name: main\n"
            "- File path: grafana/dashboards/perf-optimization.md\n"
            "- File content (exact; SINGLE trailing newline only):\n"
            "## Grafana Dashboard Performance\n\n- Reduce panel refresh to 30s\n- Prefer $__interval for rate()\n- Limit table rows to 200\n"
            "- Commit message: perf(grafana): optimize dashboard refresh and query patterns\n"
            "- Issue to label and close: 35\n"
            "- Label to add: performance\n"
            "- Pre-PR issue comment: Applying dashboard optimizations; PR will close this issue.\n"
            "- PR title: Optimize Grafana dashboard performance\n"
            "- PR body: Closes #35\n"
            "- Pull request review decision: approve\n"
            "- Release tag: v0.9.1-perf\n"
            "- Post-release issue comment: Improvements shipped in 'v0.9.1-perf'\n"
        ),
        actions=[
            # Auth & repo context
            Action(name="get_me", kwargs={"username": "devops-lead"}),
            Action(name="get_repository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="get_default_branch", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="get_head_sha", kwargs={"repo_name": "k8s-monitoring", "branch": "main"}),

            # Feature branch
            Action(name="create_branch", kwargs={"repo_name": "k8s-monitoring", "new_branch": "fix-grafana-performance", "source_branch": "main"}),

            # Change set on feature branch
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "k8s-monitoring",
                "branch": "fix-grafana-performance",
                "path": "grafana/dashboards/perf-optimization.md",
                "content": "## Grafana Dashboard Performance\n\n- Reduce panel refresh to 30s\n- Prefer $__interval for rate()\n- Limit table rows to 200\n",
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "k8s-monitoring",
                "branch": "fix-grafana-performance",
                "commit_message": "perf(grafana): optimize dashboard refresh and query patterns",
            }),

            # Work existing issue #35 deterministically
            Action(name="add_label_to_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 35, "label": "performance"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "k8s-monitoring", "issue_number": 35, "comment": "Applying dashboard optimizations; PR will close this issue."}),

            # PR from feature → main
            Action(name="create_pull_request", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Optimize Grafana dashboard performance",
                "body": "Closes #35",
                "head": "fix-grafana-performance",
                "base": "main",
            }),
            Action(name="create_pull_request_review", kwargs={"repo_name": "k8s-monitoring", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "k8s-monitoring", "pr_number": 1}),

            # Close the issue explicitly
            Action(name="update_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 35, "state": "closed"}),

            # Release & annotate the issue
            Action(name="create_release", kwargs={"repo_name": "k8s-monitoring", "tag": "v0.9.1-perf"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "k8s-monitoring", "issue_number": 35, "comment": "Improvements shipped in 'v0.9.1-perf'"}),
        ],
        outputs=[
            '"message": "Grafana performance fix merged and released", "repo_name": "k8s-monitoring"',
            '"pr_number": 1, "closed_issue": 35, "release_tag": "v0.9.1-perf"',
        ],
    ),

    # 92. (data-scientist) MLflow connectivity retry → PR merged → issue closed → release + comment
    Task(
        annotator='0',
        user_id="task_92",
        instruction=(
            "You are 'data-scientist' working in repository 'ml-pipeline'. Deliver an MLflow connectivity hardening change such that, "
            "after completion, the repository state satisfies ALL acceptance criteria below while using the exact constants provided. "
            "Treat this as a specification of outcomes and literals, NOT step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (final state must reflect all of these):\n"
            "• A feature branch exists that contains a retry-based MLflow client configuration.\n"
            "• Issue number 29 is closed.\n"
            "• A pull request (number 1 after reset for this repo) is merged into the default branch.\n"
            "• A release with the exact tag below exists.\n"
            "• The closed issue contains the exact post-release comment.\n\n"
            "CONSTANTS TO USE VERBATIM (all literals must match exactly):\n"
            "- Feature branch name: fix-mlflow-retry\n"
            "- Base branch name: main\n"
            "- File path: pipeline/config/mlflow.yml\n"
            "- File content (exact; SINGLE trailing newline only):\n"
            "mlflow:\n  tracking_uri: ${MLFLOW_TRACKING_URI}\n  client:\n    retries: 5\n    backoff_seconds: 2\n"
            "- Commit message: fix(mlflow): add client retries for connectivity issues\n"
            "- Issue to label and close: 29\n"
            "- Label to add: mlflow\n"
            "- Pre-PR issue comment: Adding retry settings for MLflow client; PR will close this issue.\n"
            "- PR title: Add MLflow client retries to mitigate connectivity issues\n"
            "- PR body: Closes #29\n"
            "- Pull request review decision: approve\n"
            "- Release tag: v0.4.0-mlflow\n"
            "- Post-release issue comment: Released in 'v0.4.0-mlflow' (MLflow retries enabled)\n"
        ),
        actions=[
            # Auth & repo context
            Action(name="get_me", kwargs={"username": "data-scientist"}),
            Action(name="get_repository", kwargs={"repo_name": "ml-pipeline"}),
            Action(name="get_default_branch", kwargs={"repo_name": "ml-pipeline"}),
            Action(name="get_head_sha", kwargs={"repo_name": "ml-pipeline", "branch": "main"}),

            # Feature branch
            Action(name="create_branch", kwargs={"repo_name": "ml-pipeline", "new_branch": "fix-mlflow-retry", "source_branch": "main"}),

            # Change set on feature branch
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "ml-pipeline",
                "branch": "fix-mlflow-retry",
                "path": "pipeline/config/mlflow.yml",
                "content": "mlflow:\n  tracking_uri: ${MLFLOW_TRACKING_URI}\n  client:\n    retries: 5\n    backoff_seconds: 2\n",
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "ml-pipeline",
                "branch": "fix-mlflow-retry",
                "commit_message": "fix(mlflow): add client retries for connectivity issues",
            }),

            # Work existing issue #29 deterministically
            Action(name="add_label_to_issue", kwargs={"repo_name": "ml-pipeline", "issue_number": 29, "label": "mlflow"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "ml-pipeline", "issue_number": 29, "comment": "Adding retry settings for MLflow client; PR will close this issue."}),

            # PR from feature → main
            Action(name="create_pull_request", kwargs={
                "repo_name": "ml-pipeline",
                "title": "Add MLflow client retries to mitigate connectivity issues",
                "body": "Closes #29",
                "head": "fix-mlflow-retry",
                "base": "main",
            }),
            Action(name="create_pull_request_review", kwargs={"repo_name": "ml-pipeline", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ml-pipeline", "pr_number": 1}),

            # Close the issue explicitly
            Action(name="update_issue", kwargs={"repo_name": "ml-pipeline", "issue_number": 29, "state": "closed"}),

            # Release & annotate the issue
            Action(name="create_release", kwargs={"repo_name": "ml-pipeline", "tag": "v0.4.0-mlflow"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "ml-pipeline", "issue_number": 29, "comment": "Released in 'v0.4.0-mlflow' (MLflow retries enabled)"}),
        ],
        outputs=[
            '"message": "MLflow retry configuration merged and released", "repo_name": "ml-pipeline"',
            '"pr_number": 1, "closed_issue": 29, "release_tag": "v0.4.0-mlflow"',
        ],
    ),

    # 93. (mobile-dev) Accessibility labels → PR merged → issue closed → release + comment
    Task(
        annotator='0',
        user_id="task_93",
        instruction=(
            "You are 'mobile-dev' working in repository 'flutter-finance-app'. Deliver an accessibility improvement such that, "
            "after completion, the repository state satisfies ALL acceptance criteria below while using the exact constants provided. "
            "Treat this as a specification of outcomes and literals, NOT step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (final state must reflect all of these):\n"
            "• A feature branch exists that contains accessibility (a11y) semantic labels for buttons.\n"
            "• Issue number 22 is closed.\n"
            "• A pull request (number 1 after reset for this repo) is merged into the default branch.\n"
            "• A release with the exact tag below exists.\n"
            "• The closed issue contains the exact post-release comment.\n\n"
            "CONSTANTS TO USE VERBATIM (all literals must match exactly):\n"
            "- Feature branch name: feature-a11y-labels\n"
            "- Base branch name: main\n"
            "- File path: lib/a11y/semantics.dart\n"
            "- File content (exact; SINGLE trailing newline only):\n"
            "/// Accessibility semantics for key buttons\nclass A11yLabels {\n  static const String addBudget = 'Add budget';\n  static const String viewReports = 'View reports';\n}\n"
            "- Commit message: feat(a11y): add semantic labels for primary actions\n"
            "- Issue to label and close: 22\n"
            "- Label to add: a11y\n"
            "- Pre-PR issue comment: Adding semantic labels for primary buttons; PR will close this issue.\n"
            "- PR title: Add a11y semantic labels for primary actions\n"
            "- PR body: Closes #22\n"
            "- Pull request review decision: approve\n"
            "- Release tag: v1.3.0-a11y\n"
            "- Post-release issue comment: Accessibility labels shipped in 'v1.3.0-a11y'\n"
        ),
        actions=[
            # Auth & repo context
            Action(name="get_me", kwargs={"username": "mobile-dev"}),
            Action(name="get_repository", kwargs={"repo_name": "flutter-finance-app"}),
            Action(name="get_default_branch", kwargs={"repo_name": "flutter-finance-app"}),
            Action(name="get_head_sha", kwargs={"repo_name": "flutter-finance-app", "branch": "main"}),

            # Feature branch
            Action(name="create_branch", kwargs={"repo_name": "flutter-finance-app", "new_branch": "feature-a11y-labels", "source_branch": "main"}),

            # Change set on feature branch
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "flutter-finance-app",
                "branch": "feature-a11y-labels",
                "path": "lib/a11y/semantics.dart",
                "content": "/// Accessibility semantics for key buttons\nclass A11yLabels {\n  static const String addBudget = 'Add budget';\n  static const String viewReports = 'View reports';\n}\n",
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "flutter-finance-app",
                "branch": "feature-a11y-labels",
                "commit_message": "feat(a11y): add semantic labels for primary actions",
            }),

            # Work existing issue #22 deterministically
            Action(name="add_label_to_issue", kwargs={"repo_name": "flutter-finance-app", "issue_number": 22, "label": "a11y"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "flutter-finance-app", "issue_number": 22, "comment": "Adding semantic labels for primary buttons; PR will close this issue."}),

            # PR from feature → main
            Action(name="create_pull_request", kwargs={
                "repo_name": "flutter-finance-app",
                "title": "Add a11y semantic labels for primary actions",
                "body": "Closes #22",
                "head": "feature-a11y-labels",
                "base": "main",
            }),
            Action(name="create_pull_request_review", kwargs={"repo_name": "flutter-finance-app", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "flutter-finance-app", "pr_number": 1}),

            # Close the issue explicitly
            Action(name="update_issue", kwargs={"repo_name": "flutter-finance-app", "issue_number": 22, "state": "closed"}),

            # Release & annotate the issue
            Action(name="create_release", kwargs={"repo_name": "flutter-finance-app", "tag": "v1.3.0-a11y"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "flutter-finance-app", "issue_number": 22, "comment": "Accessibility labels shipped in 'v1.3.0-a11y'"}),
        ],
        outputs=[
            '"message": "Accessibility labels merged and released", "repo_name": "flutter-finance-app"',
            '"pr_number": 1, "closed_issue": 22, "release_tag": "v1.3.0-a11y"',
        ],
    ),

    # 94. (bob-dev) Add TypeScript declarations → PR merged → issue closed → release + comment (fixed: base=master)
    Task(
        annotator='0',
        user_id="task_94",
        instruction=(
            "You are 'bob-dev' working in repository 'utils-js'. Deliver TypeScript declaration support such that, "
            "after completion, the repository state satisfies ALL acceptance criteria below while using the exact "
            "constants provided. Treat this as a specification of outcomes and literals, NOT step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (final state must reflect all of these):\n"
            "• A feature branch exists that contains a TypeScript declaration file for the library.\n"
            "• Issue number 4 is closed.\n"
            "• A pull request (number 1 after reset for this repo) is merged into the default branch.\n"
            "• A release with the exact tag below exists.\n"
            "• The closed issue contains the exact post-release comment.\n\n"
            "CONSTANTS TO USE VERBATIM (all literals must match exactly):\n"
            "- Feature branch name: feature-ts-decls\n"
            "- Base branch name: master\n"
            "- File path: types/index.d.ts\n"
            "- File content (exact; SINGLE trailing newline only):\n"
            "declare module 'utils-js' {\n  export function formatCurrency(value: number): string;\n}\n"
            "- Commit message: feat(types): add TypeScript declaration file\n"
            "- Issue to label and close: 4\n"
            "- Label to add: typescript\n"
            "- Pre-PR issue comment: Adding TypeScript declaration file; PR will close this issue.\n"
            "- PR title: Add TypeScript declaration file\n"
            "- PR body: Closes #4\n"
            "- Pull request review decision: approve\n"
            "- Release tag: v1.1.0-types\n"
            "- Post-release issue comment: TypeScript support shipped in 'v1.1.0-types'\n"
        ),
        actions=[
            # Auth & repo context
            Action(name="get_me", kwargs={"username": "bob-dev"}),
            Action(name="get_repository", kwargs={"repo_name": "utils-js"}),
            Action(name="get_default_branch", kwargs={"repo_name": "utils-js"}),
            Action(name="get_head_sha", kwargs={"repo_name": "utils-js", "branch": "master"}),

            # Feature branch from master
            Action(name="create_branch", kwargs={"repo_name": "utils-js", "new_branch": "feature-ts-decls", "source_branch": "master"}),

            # Change set on feature branch
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "utils-js",
                "branch": "feature-ts-decls",
                "path": "types/index.d.ts",
                "content": "declare module 'utils-js' {\n  export function formatCurrency(value: number): string;\n}\n",
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "utils-js",
                "branch": "feature-ts-decls",
                "commit_message": "feat(types): add TypeScript declaration file",
            }),

            # Work existing issue #4 deterministically
            Action(name="add_label_to_issue", kwargs={"repo_name": "utils-js", "issue_number": 4, "label": "typescript"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "utils-js", "issue_number": 4, "comment": "Adding TypeScript declaration file; PR will close this issue."}),

            # PR from feature → master
            Action(name="create_pull_request", kwargs={
                "repo_name": "utils-js",
                "title": "Add TypeScript declaration file",
                "body": "Closes #4",
                "head": "feature-ts-decls",
                "base": "master",
            }),
            Action(name="create_pull_request_review", kwargs={"repo_name": "utils-js", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "utils-js", "pr_number": 1}),

            # Close the issue explicitly
            Action(name="update_issue", kwargs={"repo_name": "utils-js", "issue_number": 4, "state": "closed"}),

            # Release & annotate the issue
            Action(name="create_release", kwargs={"repo_name": "utils-js", "tag": "v1.1.0-types"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "utils-js", "issue_number": 4, "comment": "TypeScript support shipped in 'v1.1.0-types'"}),
        ],
        outputs=[
            '"repo_name": "utils-js"',
            '"pr_number": 1, "closed_issue": 4, "release_tag": "v1.1.0-types"',
        ],
    ),

    # 95. (devops-lead) ServiceMonitor for custom apps → PR merged → issue closed → release + comment
    Task(
        annotator='0',
        user_id="task_95",
        instruction=(
            "You are 'devops-lead' working in repository 'k8s-monitoring'. Deliver custom application monitoring such that, "
            "after completion, the repository state satisfies ALL acceptance criteria below while using the exact constants provided. "
            "Treat this as a specification of outcomes and literals, NOT step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (final state must reflect all of these):\n"
            "• A feature branch exists that contains a Prometheus ServiceMonitor for custom applications.\n"
            "• Issue number 37 is closed.\n"
            "• A pull request (number 1 after reset for this repo) is merged into the default branch.\n"
            "• A release with the exact tag below exists.\n"
            "• The closed issue contains the exact post-release comment.\n\n"
            "CONSTANTS TO USE VERBATIM (all literals must match exactly):\n"
            "- Feature branch name: feature-servicemonitor-apps\n"
            "- Base branch name: main\n"
            "- File path: prometheus/servicemonitor-apps.yaml\n"
            "- File content (exact; SINGLE trailing newline only):\n"
            "apiVersion: monitoring.coreos.com/v1\nkind: ServiceMonitor\nmetadata:\n  name: apps-servicemonitor\n  namespace: monitoring\nspec:\n  selector:\n    matchLabels:\n      app.kubernetes.io/part-of: custom-apps\n  namespaceSelector:\n    any: true\n  endpoints:\n  - port: http-metrics\n    interval: 30s\n"
            "- Commit message: feat(prometheus): add ServiceMonitor for custom applications\n"
            "- Issue to label and close: 37\n"
            "- Label to add: monitoring\n"
            "- Pre-PR issue comment: Adding ServiceMonitor for custom apps; PR will close this issue.\n"
            "- PR title: Add ServiceMonitor for custom applications\n"
            "- PR body: Closes #37\n"
            "- Pull request review decision: approve\n"
            "- Release tag: v0.10.0-servicemonitor\n"
            "- Post-release issue comment: Custom app monitoring added in 'v0.10.0-servicemonitor'\n"
        ),
        actions=[
            # Auth & repo context
            Action(name="get_me", kwargs={"username": "devops-lead"}),
            Action(name="get_repository", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="get_default_branch", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="get_head_sha", kwargs={"repo_name": "k8s-monitoring", "branch": "main"}),

            # Feature branch
            Action(name="create_branch", kwargs={"repo_name": "k8s-monitoring", "new_branch": "feature-servicemonitor-apps", "source_branch": "main"}),

            # Change set on feature branch
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "k8s-monitoring",
                "branch": "feature-servicemonitor-apps",
                "path": "prometheus/servicemonitor-apps.yaml",
                "content": "apiVersion: monitoring.coreos.com/v1\nkind: ServiceMonitor\nmetadata:\n  name: apps-servicemonitor\n  namespace: monitoring\nspec:\n  selector:\n    matchLabels:\n      app.kubernetes.io/part-of: custom-apps\n  namespaceSelector:\n    any: true\n  endpoints:\n  - port: http-metrics\n    interval: 30s\n",
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "k8s-monitoring",
                "branch": "feature-servicemonitor-apps",
                "commit_message": "feat(prometheus): add ServiceMonitor for custom applications",
            }),

            # Work existing issue #37 deterministically
            Action(name="add_label_to_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 37, "label": "monitoring"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "k8s-monitoring", "issue_number": 37, "comment": "Adding ServiceMonitor for custom apps; PR will close this issue."}),

            # PR from feature → main
            Action(name="create_pull_request", kwargs={
                "repo_name": "k8s-monitoring",
                "title": "Add ServiceMonitor for custom applications",
                "body": "Closes #37",
                "head": "feature-servicemonitor-apps",
                "base": "main",
            }),
            Action(name="create_pull_request_review", kwargs={"repo_name": "k8s-monitoring", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "k8s-monitoring", "pr_number": 1}),

            # Close the issue explicitly
            Action(name="update_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 37, "state": "closed"}),

            # Release & annotate the issue
            Action(name="create_release", kwargs={"repo_name": "k8s-monitoring", "tag": "v0.10.0-servicemonitor"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "k8s-monitoring", "issue_number": 37, "comment": "Custom app monitoring added in 'v0.10.0-servicemonitor'"}),
        ],
        outputs=[
            '"pr_number": 1, "closed_issue": 37, "release_tag": "v0.10.0-servicemonitor"'
        ],
    ),

    # 96. (nlp-labs) Training memory optimization → PR merged → issue closed → release + comment
    Task(
        annotator='0',
        user_id="task_96",
        instruction=(
            "You are user 'nlp-labs' working in repository 'nlp-models'. Deliver a training memory optimization such that, "
            "after completion, the repository state satisfies ALL acceptance criteria below while using the exact constants provided. "
            "Treat this as a specification of outcomes and literals, NOT step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (final state must reflect all of these):\n"
            "• A feature branch exists that contains a config enabling memory-friendly training.\n"
            "• Issue number 12 is closed.\n"
            "• A pull request (number 1 after reset for this repo) is merged into the default branch.\n"
            "• A release with the exact tag below exists.\n"
            "• The closed issue contains the exact post-release comment.\n\n"
            "CONSTANTS TO USE VERBATIM (all literals must match exactly):\n"
            "- Feature branch name: feat-memory-optim\n"
            "- Base branch name: main\n"
            "- File path: configs/training/memory.yaml\n"
            "- File content (exact; SINGLE trailing newline only):\n"
            "training:\n  gradient_accumulation_steps: 4\n  batch_size: 8\n  mixed_precision: fp16\n"
            "- Commit message: feat(train): add memory-optimized training config\n"
            "- Issue to label and close: 12\n"
            "- Label to add: memory\n"
            "- Pre-PR issue comment: Adding memory-optimized training config; PR will close this issue.\n"
            "- PR title: Add memory-optimized training configuration\n"
            "- PR body: Closes #12\n"
            "- Pull request review decision: approve\n"
            "- Release tag: v0.8.0-memory\n"
            "- Post-release issue comment: Memory optimization available in 'v0.8.0-memory'\n"
        ),
        actions=[
            # Auth & repo context
            Action(name="get_me", kwargs={"username": "nlp-labs"}),
            Action(name="get_repository", kwargs={"repo_name": "nlp-models"}),
            Action(name="get_default_branch", kwargs={"repo_name": "nlp-models"}),
            Action(name="get_head_sha", kwargs={"repo_name": "nlp-models", "branch": "main"}),

            # Feature branch
            Action(name="create_branch", kwargs={"repo_name": "nlp-models", "new_branch": "feat-memory-optim", "source_branch": "main"}),

            # Change set on feature branch
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "nlp-models",
                "branch": "feat-memory-optim",
                "path": "configs/training/memory.yaml",
                "content": "training:\n  gradient_accumulation_steps: 4\n  batch_size: 8\n  mixed_precision: fp16\n",
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "nlp-models",
                "branch": "feat-memory-optim",
                "commit_message": "feat(train): add memory-optimized training config",
            }),

            # Work existing issue #12 deterministically
            Action(name="add_label_to_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "label": "memory"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "nlp-models", "issue_number": 12, "comment": "Adding memory-optimized training config; PR will close this issue."}),

            # PR from feature → main
            Action(name="create_pull_request", kwargs={
                "repo_name": "nlp-models",
                "title": "Add memory-optimized training configuration",
                "body": "Closes #12",
                "head": "feat-memory-optim",
                "base": "main",
            }),
            Action(name="create_pull_request_review", kwargs={"repo_name": "nlp-models", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "nlp-models", "pr_number": 1}),

            # Close the issue explicitly
            Action(name="update_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "state": "closed"}),

            # Release & annotate the issue
            Action(name="create_release", kwargs={"repo_name": "nlp-models", "tag": "v0.8.0-memory"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "nlp-models", "issue_number": 12, "comment": "Memory optimization available in 'v0.8.0-memory'"}),
        ],
        outputs=[
            '"message": "Memory optimization merged and released", "repo_name": "nlp-models"',
            '"pr_number": 1, "closed_issue": 12, "release_tag": "v0.8.0-memory"',
        ],
    ),

    # 97. (alice-w) Fastpath performance improvement → PR merged → issue closed → release + comment
    Task(
        annotator='0',
        user_id="task_97",
        instruction=(
            "You are 'alice-w' working in repository 'acme-webapp'. Deliver a fastpath performance improvement such that, "
            "after completion, the repository state satisfies ALL acceptance criteria below while using the exact constants provided. "
            "Treat this as a specification of outcomes and literals, NOT step-by-step guidance.\n\n"
            "ACCEPTANCE CRITERIA (final state must reflect all of these):\n"
            "• A feature branch exists that contains a fastpath algorithm implementation for large datasets.\n"
            "• Issue number 3 is closed.\n"
            "• A pull request (number 1 after reset for this repo) is merged into the default branch.\n"
            "• A release with the exact tag below exists.\n"
            "• The closed issue contains the exact post-release comment.\n\n"
            "CONSTANTS TO USE VERBATIM (all literals must match exactly):\n"
            "- Feature branch name: feature-perf-fastpath\n"
            "- Base branch name: main\n"
            "- File path: src/opt/fastpath.js\n"
            "- File content (exact; SINGLE trailing newline only):\n"
            "export function fastpath(items) {\n  if (!Array.isArray(items) || items.length === 0) return [];\n  const seen = new Set();\n  const out = [];\n  for (let i = 0; i < items.length; i++) {\n    const v = items[i];\n    if (!seen.has(v)) { seen.add(v); out.push(v); }\n  }\n  return out;\n}\n"
            "- Commit message: perf: introduce fastpath algorithm for large datasets\n"
            "- Issue to label and close: 3\n"
            "- Label to add: performance\n"
            "- Pre-PR issue comment: Implementing fastpath algorithm; PR will close this issue.\n"
            "- PR title: Introduce fastpath algorithm for performance\n"
            "- PR body: Closes #3\n"
            "- Pull request review decision: approve\n"
            "- Release tag: v0.2.0-perf\n"
            "- Post-release issue comment: Performance improvements shipped in 'v0.2.0-perf'\n"
        ),
        actions=[
            # Auth & repo context
            Action(name="get_me", kwargs={"username": "alice-w"}),
            Action(name="get_repository", kwargs={"repo_name": "acme-webapp"}),
            Action(name="get_default_branch", kwargs={"repo_name": "acme-webapp"}),
            Action(name="get_head_sha", kwargs={"repo_name": "acme-webapp", "branch": "main"}),

            # Feature branch
            Action(name="create_branch", kwargs={"repo_name": "acme-webapp", "new_branch": "feature-perf-fastpath", "source_branch": "main"}),

            # Change set on feature branch
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-perf-fastpath",
                "path": "src/opt/fastpath.js",
                "content": "export function fastpath(items) {\n  if (!Array.isArray(items) || items.length === 0) return [];\n  const seen = new Set();\n  const out = [];\n  for (let i = 0; i < items.length; i++) {\n    const v = items[i];\n    if (!seen.has(v)) { seen.add(v); out.push(v); }\n  }\n  return out;\n}\n",
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "acme-webapp",
                "branch": "feature-perf-fastpath",
                "commit_message": "perf: introduce fastpath algorithm for large datasets",
            }),

            # Work existing issue #3 deterministically
            Action(name="add_label_to_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "label": "performance"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "comment": "Implementing fastpath algorithm; PR will close this issue."}),

            # PR from feature → main
            Action(name="create_pull_request", kwargs={
                "repo_name": "acme-webapp",
                "title": "Introduce fastpath algorithm for performance",
                "body": "Closes #3",
                "head": "feature-perf-fastpath",
                "base": "main",
            }),
            Action(name="create_pull_request_review", kwargs={"repo_name": "acme-webapp", "pr_number": 1, "review_decision": "approve"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 1}),

            # Close the issue explicitly
            Action(name="update_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "state": "closed"}),

            # Release & annotate the issue
            Action(name="create_release", kwargs={"repo_name": "acme-webapp", "tag": "v0.2.0-perf"}),
            Action(name="add_issue_comment", kwargs={"repo_name": "acme-webapp", "issue_number": 3, "comment": "Performance improvements shipped in 'v0.2.0-perf'"}),
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
            "You are 'ops-team'. In the repository 'infra-terraform', your goal is to deliver a merged pull request "
            "into the default branch 'main' from a feature branch called 'feature-docs-refresh'. "
            "This pull request must include exactly two added files:\n\n"
            "- 'docs/CHANGELOG.md' with content:\n"
            "  ## Changelog\n\n  - 2025-08-21: Initial changelog entry.\n\n"
            "- 'docs/REFRESH.md' with content:\n"
            "  # Infra\n\n  Terraform modules.\n\n  Ops note: refreshed docs on 2025-08-21.\n\n"
            "Use commit message: 'docs: add CHANGELOG and refresh note'.\n"
            "Use pull request title: 'Docs refresh: add CHANGELOG and REFRESH.md'.\n"
            "Use pull request body: 'Automated docs refresh.'.\n"
            "Request reviewers: 'security-team' and 'devops-lead'.\n"
            "Finally, return the merged PR number, the files reported as changed in the PR, "
            "and the latest commit SHA on branch 'main'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "ops-team"}),
            Action(name="get_repository", kwargs={"repo_name": "infra-terraform"}),

            Action(name="create_branch", kwargs={
                "repo_name": "infra-terraform",
                "source_branch": "main",
                "new_branch": "feature-docs-refresh"
            }),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "infra-terraform",
                "branch": "feature-docs-refresh",
                "path": "docs/CHANGELOG.md",
                "content": "## Changelog\n\n- 2025-08-21: Initial changelog entry.\n"
            }),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "infra-terraform",
                "branch": "feature-docs-refresh",
                "path": "docs/REFRESH.md",
                "content": "# Infra\n\nTerraform modules.\n\nOps note: refreshed docs on 2025-08-21.\n"
            }),

            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "infra-terraform",
                "branch": "feature-docs-refresh",
                "commit_message": "docs: add CHANGELOG and refresh note"
            }),

            Action(name="create_pull_request", kwargs={
                "repo_name": "infra-terraform",
                "title": "Docs refresh: add CHANGELOG and REFRESH.md",
                "body": "Automated docs refresh.",
                "base": "main",
                "head": "feature-docs-refresh"
            }),

            Action(name="list_pull_request_files", kwargs={
                "repo_name": "infra-terraform",
                "pr_number": 1
            }),

            Action(name="request_pull_request_reviewers", kwargs={
                "repo_name": "infra-terraform",
                "pr_number": 1,
                "reviewers": ["security-team", "devops-lead"]
            }),

            Action(name="merge_pull_request", kwargs={
                "repo_name": "infra-terraform",
                "pr_number": 1
            }),

            Action(name="get_head_sha", kwargs={
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

    # 99. (frontend-dev) Submit hardening PR with policy + changelog and track post-merge state
    Task(
        annotator='0',
        user_id="task_99",
        instruction=(
            "You are 'frontend-dev'. You must submit a hardening update must be submitted to the repository 'react-dashboard'. The update includes two files: "
            "`kubernetes/policy.yaml` containing a Kubernetes network policy, and `docs/changelog.md` documenting the change. "
            "The policy file must contain exactly:\n\n"
            "```\n"
            "apiVersion: v1\n"
            "kind: NetworkPolicy\n"
            "metadata:\n  name: baseline\n"
            "spec:\n  podSelector: {}\n  policyTypes: [\"Ingress\",\"Egress\"]\n"
            "```\n\n"
            "The changelog must contain:\n\n"
            "```\n"
            "# Changelog\n\n- task_01: baseline policies and docs (deterministic).\n"
            "```\n\n"
            "Use the branch name `feature-hardening` and commit message `Add baseline policies [task_01]`. "
            "The changes must be proposed via a pull request titled 'Harden defaults [task_01]' with body 'Baseline policies and changelog.', "
            "reviewed by 'security-team' and 'qa-erin'. It must be approved using the comment 'LGTM [task_01]' and include the review note "
            "'Please review — deterministic run [task_01].'.\n\n"
            "Return the list of changed files from the PR, the final SHA of the default branch after the merge, and the terminal message: "
            "'Merged PR #1 into main for react-dashboard [task_01]'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "frontend-dev"}),
            Action(name="get_default_branch", kwargs={"repo_name": "react-dashboard"}),

            Action(name="create_branch", kwargs={"repo_name": "react-dashboard", "source_branch": "main", "new_branch": "feature-hardening"}),

            Action(name="write_file_to_branch", kwargs={
                "repo_name": "react-dashboard",
                "branch": "feature-hardening",
                "path": "kubernetes/policy.yaml",
                "content": "apiVersion: v1\nkind: NetworkPolicy\nmetadata:\n  name: baseline\nspec:\n  podSelector: {}\n  policyTypes: [\"Ingress\",\"Egress\"]\n"
            }),
            Action(name="write_file_to_branch", kwargs={
                "repo_name": "react-dashboard",
                "branch": "feature-hardening",
                "path": "docs/changelog.md",
                "content": "# Changelog\n\n- task_01: baseline policies and docs (deterministic).\n"
            }),
            Action(name="commit_changes_to_branch", kwargs={
                "repo_name": "react-dashboard",
                "branch": "feature-hardening",
                "commit_message": "Add baseline policies [task_01]"
            }),

            Action(name="initialize_pull_requests_block", kwargs={"repo_name": "react-dashboard"}),
            Action(name="create_pull_request", kwargs={
                "repo_name": "react-dashboard",
                "title": "Harden defaults [task_01]",
                "body": "Baseline policies and changelog.",
                "base": "main",
                "head": "feature-hardening"
            }),
            Action(name="request_pull_request_reviewers", kwargs={
                "repo_name": "react-dashboard",
                "pr_number": 1,
                "reviewers": ["security-team", "qa-erin"]
            }),
            Action(name="comment_on_pull_request", kwargs={
                "repo_name": "react-dashboard",
                "pr_number": 1,
                "comment": "Please review — deterministic run [task_01]."
            }),
            Action(name="create_pull_request_review", kwargs={
                "repo_name": "react-dashboard",
                "pr_number": 1,
                "review_decision": "approve",
                "comment": "LGTM [task_01]"
            }),
            Action(name="merge_pull_request", kwargs={"repo_name": "react-dashboard", "pr_number": 1}),

            Action(name="get_head_sha", kwargs={"repo_name": "react-dashboard", "branch": "main"}),
            Action(name="list_pull_request_files", kwargs={"repo_name": "react-dashboard", "pr_number": 1}),
            Action(name="append_terminal", kwargs={
                "message": "Merged PR #1 into main for react-dashboard [task_01]"
            }),
        ],
        outputs=[
            '"merged": "true"',
            '"sha": "sha_0000000000000000000000000000000000000000"',
            '"files": ["docs/changelog.md", "kubernetes/policy.yaml"]',
            '"message": "Merged PR #1 into main for react-dashboard [task_01]"'
        ],
    ),

    # 100
    Task(
        annotator='0',
        user_id="task_100",
        instruction=(
            "You are 'ops-team'. In repository 'infra-terraform', you ensure the following end state: "
            "There exists exactly one issue with the exact title 'Stabilize ops runbook' and the exact body "
            "'Document the on-call escalation steps for staging and production.'. "
            "That issue is closed, has exactly the labels 'operations' and 'documentation', and it contains the exact comment "
            "'Ack: logged by ops-bot.'. Finally, you return the results of searching issues for the keyword 'operations'."
        ),
        actions=[
            Action(name="get_me", kwargs={"username": "ops-team"}),
            Action(name="get_repository", kwargs={"repo_name": "infra-terraform"}),

            Action(name="create_issue", kwargs={
                "repo_name": "infra-terraform",
                "title": "Stabilize ops runbook",
                "body": "Document the on-call escalation steps for staging and production."
            }),

            Action(name="add_label_to_issue", kwargs={
                "repo_name": "infra-terraform",
                "issue_number": 1,
                "label": "operations"
            }),
            Action(name="add_label_to_issue", kwargs={
                "repo_name": "infra-terraform",
                "issue_number": 1,
                "label": "documentation"
            }),

            Action(name="add_issue_comment", kwargs={
                "repo_name": "infra-terraform",
                "issue_number": 1,
                "comment": "Ack: logged by ops-bot."
            }),

            Action(name="update_issue", kwargs={
                "repo_name": "infra-terraform",
                "issue_number": 1,
                "state": "closed"
            }),

            Action(name="search_issues", kwargs={
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
        "You are 'mobile-dev'. In the repository 'flutter-finance-app', achieve the following end state with all values exact and case‑sensitive:\n"
        "• A branch named 'hotfix-1.2.1' exists. On that branch, the file 'CHANGELOG.md' contains exactly '## 1.2.1 - hotfix'.\n"
        "• The latest commit on 'hotfix-1.2.1' includes the message 'Add CHANGELOG for v1.2.1'.\n"
        "• A release exists with tag 'v1.2.1', title 'v1.2.1 [task_101]', and body 'body-[task_101]'; and the latest release resolves to tag 'v1.2.1'.\n"
        "• An issue exists titled 'Release v1.2.1 note [task_101]' with body 'body-[task_101]' labeled 'release-log'.\n"
        "• The terminal log includes exactly one appended entry with the message 'Release v1.2.1 created in flutter-finance-app [task_101]'.\n"
        "Return the latest release tag from 'flutter-finance-app'. All requirements must be satisfied in a fresh database run; use deterministic values only."
        ),
        actions=[
        Action(name="get_me", kwargs={"username": "mobile-dev"}),
        Action(name="get_repository", kwargs={"repo_name": "flutter-finance-app"}),
        Action(name="create_branch", kwargs={"repo_name": "flutter-finance-app", "source_branch": "main", "new_branch": "hotfix-1.2.1"}),
        Action(name="write_file_to_branch", kwargs={"repo_name": "flutter-finance-app", "branch": "hotfix-1.2.1", "path": "CHANGELOG.md", "content": "## 1.2.1 - hotfix"}),
        Action(name="commit_changes_to_branch", kwargs={"repo_name": "flutter-finance-app", "branch": "hotfix-1.2.1", "commit_message": "Add CHANGELOG for v1.2.1"}),
        Action(name="create_release", kwargs={"repo_name": "flutter-finance-app", "tag": "v1.2.1", "title": "v1.2.1 [task_101]", "body": "body-[task_101]"}),
        Action(name="get_latest_release", kwargs={"repo_name": "flutter-finance-app"}),
        Action(name="create_issue", kwargs={"repo_name": "flutter-finance-app", "title": "Release v1.2.1 note [task_101]", "body": "body-[task_101]", "labels": ["release-log"]}),
        Action(name="append_terminal", kwargs={"message": "Release v1.2.1 created in flutter-finance-app [task_101]"}),
        ],
        outputs=[
        '"message": "Branch created", "new_branch": "hotfix-1.2.1"',
        '"message": "Committed to branch", "commit_message": "Add CHANGELOG for v1.2.1"',
        '"message": "Release created.", "repo_name": "flutter-finance-app", "tag_name": "v1.2.1"',
        '"tag_name": "v1.2.1"', # from get_latest_release
        '"labels": ["release-log"]',
        '"message": "Release v1.2.1 created in flutter-finance-app [task_101]"',
        ],
    )
]
