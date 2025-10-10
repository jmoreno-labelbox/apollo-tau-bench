from domains.dto import Action, Task

TASKS = [
    Task(
    annotator="0",
    user_id="task_44",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to add contribution guidance to "
        "'acme-webapp' with a new file 'CONTRIBUTING.md' whose contents are exactly 'Please follow Conventional Commits.' "
        "authored by 'alice-w' on branch 'feature-branch', proposed via a pull request titled 'Add contributing guide' "
        "with body 'Introduce CONTRIBUTING.md' and merge it back, "
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "file_name": "CONTRIBUTING.md", "file_content": "Please follow Conventional Commits."}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "commit_message": "Add CONTRIBUTING.md", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_title": "Add contributing guide", "pr_body": "Introduce CONTRIBUTING.md", "head_branch_name": "feature-branch", "base_branch_name": "main", "head_sha": "commit_sha_101", "pr_files": ["CONTRIBUTING.md"]}),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "feature-branch", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-branch"}),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-branch' created in alice-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'CONTRIBUTING.md' to alice-w/acme-webapp@feature-branch.",
            "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@feature-branch.",
            "2025-08-21T12:00:00Z : Pull request #101 created for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'feature-branch' into 'main' for alice-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'feature-branch' deleted from alice-w/acme-webapp."
            ]
        }
    ]
),

    Task(
    annotator="0",
    user_id="task_30",
    instruction=(
        "You are 'bob-dev' with 'bob.martinez@devstudio.com' and auth key as "
        "'ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i'. Your mission is for the repository 'utils-js' to "
        "end with its default branch 'master' containing a new file 'docs/USAGE.md' whose contents are exactly "
        "'# Usage Guide Run npm start to launch the app.'. This change must originate from branch 'feature-docs', "
        "be authored by 'bob-dev' with the commit message and Pr title as 'Add docs/USAGE.md', and be proposed in a pull request "
        " with body 'Provide instructions for running the chat app.'"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "bob-dev",
            "email": "bob.martinez@devstudio.com",
            "auth_key": "ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i"
        }),
        Action(name="create_new_branch", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "base_branch": "master"
        }),
        Action(name="add_new_file_in_repo", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "file_name": "docs/USAGE.md",
            "file_content": "# Usage Guide Run npm start to launch the app."
        }),
        Action(name="initial_commit", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "commit_message": "Add docs/USAGE.md",
            "commit_author": "bob-dev"
        }),
        Action(name="create_pull_request", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "pr_title": "Add docs/USAGE.md",
            "pr_body": "Provide instructions for running the chat app.",
            "head_branch_name": "feature-docs",
            "base_branch_name": "master",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/USAGE.md"]
        }),
        Action(name="approve_pr", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "pr_number": 101
        }),
        Action(name="merge_branch", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "source_branch_name": "feature-docs",
            "target_branch_name": "master"
        }),
        Action(name="mark_pr_as_merged", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "pr_number": 101
        }),
        Action(name="delete_branch", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs"
        }),
        Action(name="list_all_terminal_message", kwargs={})
    ],
    outputs=[
        {
            "success": "PR #101 merged for bob-dev/utils-js.",
            "repo": "bob-dev/utils-js",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-docs' created in bob-dev/utils-js from 'master'.",
            "2025-08-21T12:00:00Z : Added 'docs/USAGE.md' to bob-dev/utils-js@feature-docs.",
            "2025-08-21T12:00:00Z : Initial commit added to bob-dev/utils-js@feature-docs.",
            "2025-08-21T12:00:00Z : Pull request #101 created for bob-dev/utils-js.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for bob-dev/utils-js.",
            "2025-08-21T12:30:00Z : Merged 'feature-docs' into 'master' for bob-dev/utils-js with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for bob-dev/utils-js.",
            "2025-08-21T12:30:00Z : Branch 'feature-docs' deleted from bob-dev/utils-js."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_31",
    instruction=(
        "You are 'bob-dev' with 'bob.martinez@devstudio.com' and auth key "
        "'ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i'. "
        "you want a nae feature branch 'feature-tel-input' for 'utils-js' (base: 'master') "
        "add 'src/utils/phone.js' with a simple code 'export const isPhone = 0;' and save it with message 'Add phone validator' and"
        " merge it back with  PR titled 'Add phone validation utility' and body 'Introduce simple phone number regex validator.'"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "bob-dev",
            "email": "bob.martinez@devstudio.com",
            "auth_key": "ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i"
        }),
        Action(name="create_new_branch", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-tel-input",
            "base_branch": "master"
        }),
        Action(name="add_new_file_in_repo", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-tel-input",
            "file_name": "src/utils/phone.js",
            "file_content": "export const isPhone = 0;"
        }),
        Action(name="initial_commit", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-tel-input",
            "commit_message": "Add phone validator",
            "commit_author": "bob-dev"
        }),
        Action(name="create_pull_request", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "pr_title": "Add phone validation utility",
            "pr_body": "Introduce simple phone number regex validator.",
            "head_branch_name": "feature-tel-input",
            "base_branch_name": "master",
            "head_sha": "commit_sha_101",
            "pr_files": ["src/utils/phone.js"]
        }),
        Action(name="approve_pr", kwargs={
            "owner": "bob-dev", "repo_name": "utils-js", "pr_number": 101
        }),
        Action(name="merge_branch", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "source_branch_name": "feature-tel-input",
            "target_branch_name": "master"
        }),
        Action(name="mark_pr_as_merged", kwargs={
            "owner": "bob-dev", "repo_name": "utils-js", "pr_number": 101
        }),
        Action(name="delete_branch", kwargs={
            "owner": "bob-dev", "repo_name": "utils-js", "branch_name": "feature-tel-input"
        }),
        Action(name="list_all_terminal_message", kwargs={})
    ],
    outputs=[
        {
            "success": "PR #101 merged for bob-dev/utils-js.",
            "repo": "bob-dev/utils-js",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
                "2025-08-21T12:00:00Z : Branch 'feature-tel-input' created in bob-dev/utils-js from 'master'.",
                "2025-08-21T12:00:00Z : Added 'src/utils/phone.js' to bob-dev/utils-js@feature-tel-input.",
                "2025-08-21T12:00:00Z : Initial commit added to bob-dev/utils-js@feature-tel-input.",
                "2025-08-21T12:00:00Z : Pull request #101 created for bob-dev/utils-js.",
                "2025-08-21T12:30:00Z : PR #101 marked APPROVE for bob-dev/utils-js.",
                "2025-08-21T12:30:00Z : Merged 'feature-tel-input' into 'master' for bob-dev/utils-js with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : PR #101 merged for bob-dev/utils-js.",
                "2025-08-21T12:30:00Z : Branch 'feature-tel-input' deleted from bob-dev/utils-js."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_32",
    instruction=(
        "You are 'backend-core' with 'backend@coreservices.io' and auth key "
        "'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. "
        "For 'payments-service', add a diagnostic comment 'Added extra 3DS telemetry to reproduce; monitoring for failures.' to issue #13 and close issue #15, "
        "and then list all issues for the repo."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "backend-core",
            "email": "backend@coreservices.io",
            "auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 13,
            "issue_comment": "Added extra 3DS telemetry to reproduce; monitoring for failures.",
            "issue_comment_user": "backend-core"
        }),
        Action(name="close_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 15
        }),
        Action(name="get_all_issues_for_repo", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service"
        })
    ],
    outputs=[
        {
            "owner": "backend-core",
            "repo_name": "payments-service",
            "count": 2,
            "issues": [
            {
                "number": 13,
                "title": "3DS fallback not triggered",
                "body": "On some cards, 3DS fallback is not invoked",
                "state": "open",
                "labels": [
                "bug",
                "payments"
                ],
                "assignees": [
                "payments-lead",
                "qa-erin"
                ],
                "comments": [
                "Adding logs to reproduce",
                "Added extra 3DS telemetry to reproduce; monitoring for failures."
                ],
                "comment_users": [
                "backend-core",
                "backend-core"
                ],
                "created_ts": "2023-12-03T13:00:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            },
            {
                "number": 15,
                "title": "Timeout too aggressive",
                "body": "Timeout should be 60s for long-running transactions",
                "state": "closed",
                "labels": [
                "bug",
                "priority-medium"
                ],
                "assignees": [
                "backend-core"
                ],
                "comments": [
                "Proposed patch incoming"
                ],
                "comment_users": [
                "backend-core"
                ],
                "created_ts": "2023-12-03T13:30:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            }
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_33",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your task is for the repository "
        "'ui-kit' to dismiss open medium-severity code scanning alerts on 'refs/heads/main'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "ui-team",
            "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "severity": "medium",
            "ref": "refs/heads/main"
        }),
        Action(name="dismiss_alert", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="get_alert_details", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "number": 2,
            "severity": "medium",
            "state": "dismissed",
            "description": "Potential XSS in button label",
            "ref": "refs/heads/main",
            "created_ts": "2023-12-03T12:00:00Z",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:30:00Z : Alert #2 dismissed for ui-team/ui-kit."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_35",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Delete 'docs/ARCHITECTURE.md' "
        "from 'acme-webapp' on 'main', then show branch contents, and terminal log."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "alice-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="delete_file_in_repo", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "branch_name": "main",
            "file_name": "docs/ARCHITECTURE.md"
        }),
        Action(name="get_branch_content", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "main"
        }),
        Action(name="list_all_terminal_message", kwargs={})
    ],
    outputs=[
        {
            "branch": "main",
            "branch_files": [
            "README.md",
            "LICENSE",
            ".gitignore",
            "requirements.txt",
            "src/main.py",
            "src/app.py",
            "src/utils.py",
            "src/config.py",
            "tests/test_app.py"
            ],
            "branch_contents": [
            "# Acme Webapp\n\nFlask-based demo application.",
            "MIT License\n\nCopyright (c) 2023",
            "__pycache__/\n.env\n*.pyc\n",
            "flask==2.3.2\nrequests==2.31.0\n",
            "print('Hello, World!')\n",
            "from flask import Flask\napp = Flask(__name__)\n@app.get('/')\ndef index():\n  return 'OK'\n",
            "def helper(x: int) -> int:\n  return x * 2\n",
            "DEBUG=True\nPORT=5000\n",
            "from src.app import app\n\ndef test_index():\n  client = app.test_client()\n  assert client.get('/').status_code == 200\n"
            ],
            "branch_sha": "a1b2c3d4e5f60718293a4b5c6d7e8f9012345678"
        },
        {
            "messages": [
            "2025-08-21T12:30:00Z : Deleted 'docs/ARCHITECTURE.md' from alice-w/acme-webapp@main."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_22",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co and auth key as 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'."
        " Your mission is for the repository 'ui-kit' to end in a state where its default branch 'main' contains the component file 'packages/alert/index.tsx' with"
        " contents exactly 'export const Alert = () => <div role='alert' />'. The change must originate on the branch 'feature-alert',"
        " be authored by 'ui-team' with the commit message 'Add packages/alert/index.tsx', and be represented by a pull request titled 'Add Alert component' with body 'Introduce basic Alert component.'"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="create_new_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "file_name": "packages/alert/index.tsx", "file_content": "export const Alert = () => <div role='alert' />"}),
        Action(name="initial_commit", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "commit_message": "Add packages/alert/index.tsx", "commit_author": "ui-team"}),
        Action(name="create_pull_request", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "pr_title": "Add Alert component",
            "pr_body": "Introduce basic Alert component.",
            "head_branch_name": "feature-alert",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["packages/alert/index.tsx"]
        }),
        Action(name="approve_pr", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "source_branch_name": "feature-alert", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert"}),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "success": "Branch 'feature-alert' deleted from ui-team/ui-kit.",
            "repo": "ui-team/ui-kit",
            "deleted_branch": "feature-alert",
            "removed_file_count": 11,
            "remaining_branches": [
            "main",
            "release-1.0",
            "feature-theme"
            ]
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-alert' created in ui-team/ui-kit from 'main'.",
            "2025-08-21T12:00:00Z : Added 'packages/alert/index.tsx' to ui-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Initial commit added to ui-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Pull request #101 created for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : Merged 'feature-alert' into 'main' for ui-team/ui-kit with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : Branch 'feature-alert' deleted from ui-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_98",
    instruction=(
        "You are 'bob-dev' with 'bob.martinez@devstudio.com' and auth key as "
        "'ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i'. Your mission is for the repository 'utils-js' to "
        "end with its default branch 'master' containing a new file 'docs/USAGE.md' whose contents are exactly "
        "'# Usage Guide Run npm start to launch the app.'. This change must originate from branch 'feature-docs', "
        "be authored by 'bob-dev' with the commit message and pr title as 'Add docs/USAGE.md', and be proposed in a pull request "
        " with body 'Provide instructions for running the chat app.'"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "bob-dev",
            "email": "bob.martinez@devstudio.com",
            "auth_key": "ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i"
        }),
        Action(name="create_new_branch", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "base_branch": "master"
        }),
        Action(name="add_new_file_in_repo", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "file_name": "docs/USAGE.md",
            "file_content": "# Usage Guide Run npm start to launch the app."
        }),
        Action(name="initial_commit", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "commit_message": "Add docs/USAGE.md",
            "commit_author": "bob-dev"
        }),
        Action(name="create_pull_request", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "pr_title": "Add docs/USAGE.md",
            "pr_body": "Provide instructions for running the chat app.",
            "head_branch_name": "feature-docs",
            "base_branch_name": "master",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/USAGE.md"]
        }),
        Action(name="approve_pr", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "pr_number": 101
        }),
        Action(name="merge_branch", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "source_branch_name": "feature-docs",
            "target_branch_name": "master"
        }),
        Action(name="mark_pr_as_merged", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "pr_number": 101
        }),
        Action(name="delete_branch", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs"
        }),
        Action(name="list_all_terminal_message", kwargs={})
    ],
    outputs=[
        {
            "success": "PR #101 merged for bob-dev/utils-js.",
            "repo": "bob-dev/utils-js",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-docs' created in bob-dev/utils-js from 'master'.",
            "2025-08-21T12:00:00Z : Added 'docs/USAGE.md' to bob-dev/utils-js@feature-docs.",
            "2025-08-21T12:00:00Z : Initial commit added to bob-dev/utils-js@feature-docs.",
            "2025-08-21T12:00:00Z : Pull request #101 created for bob-dev/utils-js.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for bob-dev/utils-js.",
            "2025-08-21T12:30:00Z : Merged 'feature-docs' into 'master' for bob-dev/utils-js with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for bob-dev/utils-js.",
            "2025-08-21T12:30:00Z : Branch 'feature-docs' deleted from bob-dev/utils-js."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_34",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. approve and merge pull request #12 for ui-kit repo."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "ui-team",
            "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="get_pr_details", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit", "pr_number": 12
        }),
        Action(name="approve_pr", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit", "pr_number": 12
        }),
        Action(name="merge_branch", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit",
            "source_branch_name": "release-1.0",
            "target_branch_name": "main"
        }),
        Action(name="mark_pr_as_merged", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit", "pr_number": 12
        }),
        Action(name="delete_branch", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit", "branch_name": "release-1.0"
        }),
        Action(name="get_repo_info_for_owner", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit"
        }),
        Action(name="list_all_terminal_message", kwargs={})
    ],
    outputs=[
        {
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "description": "Reusable UI components",
            "private": False,
            "auto_init": True,
            "default_branch": "main",
            "file_paths": [
            "README.md",
            "LICENSE",
            ".npmrc",
            "package.json",
            "packages/button/index.tsx",
            "packages/card/index.tsx",
            "docs/STYLEGUIDE.md",
            "CHANGELOG.md"
            ],
            "file_contents": [
            "# UI Kit\n\nComponent library.",
            "MIT License\n",
            "legacy-peer-deps=true\n",
            "{\n  \"name\": \"ui-kit\",\n  \"version\": \"1.0.0\"\n}",
            "export const Button = () => <button>Click</button>;\n",
            "export const Card = () => <div className='card' />;\n",
            "# Styleguide\n\nTypography, spacing, color.",
            "# Changelog\n- Init\n"
            ],
            "branches": [
            "main",
            "feature-theme"
            ],
            "branch_shas": [
            "merge_sha_101",
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            ],
            "created_ts": "2023-10-20T08:00:00Z",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
                "2025-08-21T12:30:00Z : PR #12 marked APPROVE for ui-team/ui-kit.",
                "2025-08-21T12:30:00Z : Merged 'release-1.0' into 'main' for ui-team/ui-kit with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : PR #12 merged for ui-team/ui-kit.",
                "2025-08-21T12:30:00Z : Branch 'release-1.0' deleted from ui-team/ui-kit."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_40",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your task is to ensure the repository 'ui-kit' reflects a new enhancement "
        "record whose title is 'Add accessible Tooltip component' and body is 'Create a Tooltip that meets WCAG 2.2 with keyboard focus management.' "
        "labeled with ['enhancement', 'accessibility'] and assigned to ['ui-team']. The record must include two remarks: "
        "'Spec approved.' by 'design' and 'Implemented basic prototype.' by 'ui-team'. "
        "The record should end in state 'closed' when complete."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="create_new_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "title": "Add accessible Tooltip component",
            "body": "Create a Tooltip that meets WCAG 2.2 with keyboard focus management.",
            "labels": ["enhancement", "accessibility"],
            "assignees": ["ui-team"]
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Spec approved.",
            "issue_comment_user": "design"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Implemented basic prototype.",
            "issue_comment_user": "ui-team"
        }),
        Action(name="close_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101
        }),
        # Action(name="get_all_issues_for_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit"}),
        # Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for ui-team/ui-kit.",
            "repo": "ui-team/ui-kit",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        }
    ]
),
    Task(
    annotator="0",
    user_id="task_45",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev and auth key as 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'."
        " Your mission is for the repository 'acme-webapp' to end in a state where its default branch 'main' contains the file 'examples/hello.txt' with contents exactly 'hello'."
        " The change must originate on the branch 'feature-example', be authored by 'alice-w' with the commit message 'Add examples/hello.txt',"
        " and merge it using a pull request titled 'Add example' with body 'Introduce a simple example file.'"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "base_branch": "main"}),
        Action(
                name="get_repo_info_for_owner",
                kwargs={"owner":"alice-w", "repo_name":"acme-webapp"},
            ),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "file_name": "examples/hello.txt", "file_content": "hello"}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "commit_message": "Add examples/hello.txt", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "pr_title": "Add example",
            "pr_body": "Introduce a simple example file.",
            "head_branch_name": "feature-example",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["examples/hello.txt"]
        }),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "feature-example", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example"}),
        Action(
                name="get_repo_info_for_owner",
                kwargs={"owner":"alice-w", "repo_name":"acme-webapp"},
            ),
    ],
    outputs=[
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "description": "A sample demonstration repository",
            "private": False,
            "auto_init": True,
            "default_branch": "main",
            "file_paths": [
            "README.md",
            "LICENSE",
            ".gitignore",
            "requirements.txt",
            "src/main.py",
            "src/app.py",
            "src/utils.py",
            "src/config.py",
            "tests/test_app.py",
            "docs/ARCHITECTURE.md",
            "examples/hello.txt"
            ],
            "file_contents": [
            "# Acme Webapp\n\nFlask-based demo application.",
            "MIT License\n\nCopyright (c) 2023",
            "__pycache__/\n.env\n*.pyc\n",
            "flask==2.3.2\nrequests==2.31.0\n",
            "print('Hello, World!')\n",
            "from flask import Flask\napp = Flask(__name__)\n@app.get('/')\ndef index():\n  return 'OK'\n",
            "def helper(x: int) -> int:\n  return x * 2\n",
            "DEBUG=True\nPORT=5000\n",
            "from src.app import app\n\ndef test_index():\n  client = app.test_client()\n  assert client.get('/').status_code == 200\n",
            "# Architecture\n\n- App layer\n- Utils layer\n- Config\n",
            "hello"
            ],
            "branches": [
            "main",
            "feature-update"
            ],
            "branch_shas": [
            "merge_sha_101",
            "c3d4e5f6a7b8091a2b3c4d5e6f708192a3b4c5d6"
            ],
            "created_ts": "2023-12-01T10:00:00Z",
            "updated_ts": "2025-08-21T12:30:00Z"
        }
    ]
),


    Task(
    annotator="0",
    user_id="task_01",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r',"
        " and your task is to add a new security policy to the existing repository 'acme-webapp' (description: 'A sample demonstration repository') by introducing a "
        "feature branch 'feature-security-policy' that contributes a file named 'SECURITY.md' at the repository root containing "
        "'## Security Policy. Please report vulnerabilities to security@acme.dev within 24 hours.'. Open a pull "
        "request into 'main' with title 'Add security policy' and body 'Introduce SECURITY.md with coordinated disclosure instructions.' for this change."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="create_new_branch",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-security-policy", "base_branch": "main"}
        ),
        Action(
            name="add_new_file_in_repo",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-security-policy", "file_name": "SECURITY.md", "file_content": "## Security Policy. Please report vulnerabilities to security@acme.dev within 24 hours."}
        ),
        Action(
            name="initial_commit",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-security-policy", "commit_message": "Add SECURITY.md", "commit_author": "alice-w"}
        ),
        Action(
            name="create_pull_request",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_title": "Add security policy", "pr_body": "Introduce SECURITY.md with coordinated disclosure instructions.", "head_branch_name": "feature-security-policy", "base_branch_name": "main", "head_sha": "commit_sha_101", "pr_files": ["SECURITY.md"]}
        ),
        Action(
            name="list_all_terminal_message",
            kwargs={}
        ),
    ],
    outputs=[
        {
            "success": "Branch 'feature-security-policy' created in alice-w/acme-webapp from 'main'.",
            "repo": "alice-w/acme-webapp",
            "created_branch": "feature-security-policy",
            "base_branch": "main",
            "branch_index": 2,
            "branch_sha": "branch_sha_101",
            "branch_file": [
            "README.md",
            "LICENSE",
            ".gitignore",
            "requirements.txt",
            "src/main.py",
            "src/app.py",
            "src/utils.py",
            "src/config.py",
            "tests/test_app.py",
            "docs/ARCHITECTURE.md"
            ]
        },
        {
            "success": "Pull request #101 created for alice-w/acme-webapp.",
            "pull_request": {
            "number": 101,
            "title": "Add security policy",
            "body": "Introduce SECURITY.md with coordinated disclosure instructions.",
            "state": "open",
            "base": "main",
            "head": "feature-security-policy",
            "head_sha": "commit_sha_101",
            "files": [
                "SECURITY.md"
            ],
            "created_ts": "2025-08-21T12:00:00Z",
            "updated_ts": "2025-08-21T12:00:00Z"
            }
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-security-policy' created in alice-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'SECURITY.md' to alice-w/acme-webapp@feature-security-policy.",
            "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@feature-security-policy.",
            "2025-08-21T12:00:00Z : Pull request #101 created for alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_02",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to assign john to pull request"
        "#5 in 'acme-webapp' repo and he made a comment 'Nice Job' and approved the PR."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
                name="get_pr_details",
                kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "pr_number":5},
            ),
        Action(
            name="assign_pull_request_reviewers",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 5, "reviewers": ["john"]}
        ),
        Action(
            name="add_pull_request_comment",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 5, "comment": "Nice Job", "comment_user": "john", "review_state": "COMMENT"}
        ),
        Action(
            name="approve_pr",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 5}
        ),
        Action(
            name="get_pr_details",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 5}
        ),
    ],
    outputs=[
        {
            "number": 5,
            "title": "Add authentication module",
            "body": "This PR adds basic authentication functionality",
            "state": "open",
            "base_branch": "main",
            "head_branch": "feature-auth",
            "head_sha": "d1e2f3a4b5c6",
            "mergeable": True,
            "merged": False,
            "files": [
            [
                "src/auth.py",
                "tests/test_auth.py"
            ]
            ],
            "comments": [
            [
                "Looks good overall",
                "Please add more tests",
                "Nice Job"
            ]
            ],
            "comment_users": [
            [
                "dev-sue",
                "qa-mike",
                "john"
            ]
            ],
            "reviewers": [
            [
                "dev-sue",
                "qa-mike",
                "john"
            ]
            ],
            "review_states": [
            [
                [
                "COMMENT",
                "APPROVE"
                ],
                [
                "REQUEST_CHANGES",
                "APPROVE"
                ],
                [
                "REQUESTED",
                "COMMENT",
                "APPROVE"
                ]
            ]
            ],
            "review_events": [
            [
                [
                "COMMENT",
                "APPROVE"
                ],
                [
                "REQUEST_CHANGES",
                "APPROVE"
                ],
                [
                "REQUESTED",
                "COMMENT",
                "APPROVE"
                ]
            ]
            ],
            "created_ts": "2023-12-02T09:00:00Z",
            "updated_ts": "2025-08-21T12:30:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_03",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s', and your task is to finalize the already-approved, "
        "mergeable pull request #11 for the repository 'ui-kit' so that the main line reflects the approved changes and the feature line is cleaned up."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}
        ),
        Action(
            name="get_pr_details",
            kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 11}
        ),
        Action(
            name="merge_branch",
            kwargs={"owner":"ui-team", "repo_name":"ui-kit", "source_branch_name":"feature-theme", "target_branch_name":"main"}
        ),
        Action(
            name="mark_pr_as_merged",
            kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 11}
        ),
        Action(
            name="delete_branch",
            kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-theme"}
        ),
        Action(
            name="get_repo_info_for_owner",
            kwargs={"owner": "ui-team", "repo_name": "ui-kit"}
        ),
        Action(
            name="list_all_terminal_message",
            kwargs={}
        ),
    ],
    outputs=[
        {
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "description": "Reusable UI components",
            "private": False,
            "auto_init": True,
            "default_branch": "main",
            "file_paths": [
            "README.md",
            "LICENSE",
            ".npmrc",
            "package.json",
            "packages/button/index.tsx",
            "packages/card/index.tsx",
            "packages/theme/index.ts",
            "docs/STYLEGUIDE.md",
            "docs/CONTRIBUTING.md",
            "CHANGELOG.md",
            "examples/theme-preview.tsx"
            ],
            "file_contents": [
            "# UI Kit\n\nComponent library.",
            "MIT License\n",
            "legacy-peer-deps=true\n",
            "{\n  \"name\": \"ui-kit\",\n  \"version\": \"1.0.0\"\n}",
            "export const Button = () => <button>Click</button>;\n",
            "export const Card = () => <div className='card' />;\n",
            "export const Theme = {};\n",
            "# Styleguide\n\nTypography, spacing, color.",
            "# Contributing\n\nPRs welcome. Follow conventional commits.",
            "# Changelog\n- Init\n",
            "export const Preview = () => <div />;\n"
            ],
            "branches": [
            "main",
            "release-1.0"
            ],
            "branch_shas": [
            "merge_sha_101",
            "0aaa999988887777666655554444333322221111"
            ],
            "created_ts": "2023-10-20T08:00:00Z",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
                "2025-08-21T12:30:00Z : Merged 'feature-theme' into 'main' for ui-team/ui-kit with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : PR #11 merged for ui-team/ui-kit.",
                "2025-08-21T12:30:00Z : Branch 'feature-theme' deleted from ui-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_04",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your task is for the repository "
        "'ui-kit' to dismiss open medium-severity code scanning alerts on 'refs/heads/main'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "ui-team",
            "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "severity": "medium",
            "ref": "refs/heads/main"
        }),
        Action(name="get_alert_details", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="dismiss_alert", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="get_alert_details", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "number": 2,
            "severity": "medium",
            "state": "dismissed",
            "description": "Potential XSS in button label",
            "ref": "refs/heads/main",
            "created_ts": "2023-12-03T12:00:00Z",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:30:00Z : Alert #2 dismissed for ui-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_05",
    instruction=(

        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to introduce a CLI entry point to "
        "'acme-webapp' via an isolated branch named 'feature-add-cli' adding the file 'cli/main.py' with contents "
        "\"print('Hello from CLI')\" and a commit message 'Add CLI entrypoint' authored by 'alice-w', and ensure "
        "this change is integrated into 'main' with the branch cleaned up afterwards."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="create_new_branch",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "base_branch": "main"}
        ),
        Action(
            name="add_new_file_in_repo",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "file_name": "cli/main.py", "file_content": "print('Hello from CLI')"}
        ),
        Action(
            name="initial_commit",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "commit_message": "Add CLI entrypoint", "commit_author": "alice-w"}
        ),
        Action(
                name="merge_branch",
                kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "source_branch_name":"feature-add-cli", "target_branch_name":"main"},
            ),
        # Action(
        #     name="mark_pr_as_merged",
        #     kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 11}
        # ),
        Action(
            name="delete_branch",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli"}
        ),
        # Action(
        #     name="create_pull_request",
        #     kwargs={
        #         "owner": "alice-w",
        #         "repo_name": "acme-webapp",
        #         "pr_title": "Add CLI tool",
        #         "pr_body": "Introduce simple CLI entrypoint.",
        #         "head_branch_name": "feature-add-cli",
        #         "base_branch_name": "main",
        #         "head_sha": "commit_sha_101",
        #         "pr_files": ["cli/main.py"]
        #     }
        # ),
        # Action(
        #     name="approve_pr",
        #     kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}
        # ),
        # Action(
        #     name="merge_pull_request",
        #     kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}
        # ),
        Action(
            name="get_repo_info_for_owner",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp"}
        ),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "description": "A sample demonstration repository",
            "private": False,
            "auto_init": True,
            "default_branch": "main",
            "file_paths": [
            "README.md",
            "LICENSE",
            ".gitignore",
            "requirements.txt",
            "src/main.py",
            "src/app.py",
            "src/utils.py",
            "src/config.py",
            "tests/test_app.py",
            "docs/ARCHITECTURE.md",
            "cli/main.py"
            ],
            "file_contents": [
            "# Acme Webapp\n\nFlask-based demo application.",
            "MIT License\n\nCopyright (c) 2023",
            "__pycache__/\n.env\n*.pyc\n",
            "flask==2.3.2\nrequests==2.31.0\n",
            "print('Hello, World!')\n",
            "from flask import Flask\napp = Flask(__name__)\n@app.get('/')\ndef index():\n  return 'OK'\n",
            "def helper(x: int) -> int:\n  return x * 2\n",
            "DEBUG=True\nPORT=5000\n",
            "from src.app import app\n\ndef test_index():\n  client = app.test_client()\n  assert client.get('/').status_code == 200\n",
            "# Architecture\n\n- App layer\n- Utils layer\n- Config\n",
            "print('Hello from CLI')"
            ],
            "branches": [
            "main",
            "feature-update"
            ],
            "branch_shas": [
            "merge_sha_101",
            "c3d4e5f6a7b8091a2b3c4d5e6f708192a3b4c5d6"
            ],
            "created_ts": "2023-12-01T10:00:00Z",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
                "2025-08-21T12:00:00Z : Branch 'feature-add-cli' created in alice-w/acme-webapp from 'main'.",
                "2025-08-21T12:00:00Z : Added 'cli/main.py' to alice-w/acme-webapp@feature-add-cli.",
                "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@feature-add-cli.",
                "2025-08-21T12:30:00Z : Merged 'feature-add-cli' into 'main' for alice-w/acme-webapp with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : Branch 'feature-add-cli' deleted from alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_06",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to add contribution guidance to "
        "'acme-webapp' with a new file 'CONTRIBUTING.md' whose contents are exactly 'Please follow Conventional Commits.' "
        "authored by 'alice-w' on branch 'feature-branch', proposed via a pull request titled 'Add contributing guide' "
        "with body 'Introduce CONTRIBUTING.md' and merge it back, "
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "file_name": "CONTRIBUTING.md", "file_content": "Please follow Conventional Commits."}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "commit_message": "Add CONTRIBUTING.md", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_title": "Add contributing guide", "pr_body": "Introduce CONTRIBUTING.md", "head_branch_name": "feature-branch", "base_branch_name": "main", "head_sha": "commit_sha_101", "pr_files": ["CONTRIBUTING.md"]}),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "feature-branch", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-branch"}),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
                                                                      "messages": [
                                                                        "2025-08-21T12:00:00Z : Branch 'feature-branch' created in alice-w/acme-webapp from 'main'.",
                                                                        "2025-08-21T12:00:00Z : Added 'CONTRIBUTING.md' to alice-w/acme-webapp@feature-branch.",
                                                                        "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@feature-branch.",
                                                                        "2025-08-21T12:00:00Z : Pull request #101 created for alice-w/acme-webapp.",
                                                                        "2025-08-21T12:30:00Z : PR #101 marked APPROVE for alice-w/acme-webapp.",
                                                                        "2025-08-21T12:30:00Z : Merged 'feature-branch' into 'main' for alice-w/acme-webapp with SHA merge_sha_101.",
                                                                        "2025-08-21T12:30:00Z : PR #101 merged for alice-w/acme-webapp.",
                                                                        "2025-08-21T12:30:00Z : Branch 'feature-branch' deleted from alice-w/acme-webapp."
                                                                      ]
                                                                    }
    ]
),
Task(
    annotator="0",
    user_id="task_07",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev and auth key as 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'."
        " Your mission is for the repository 'acme-webapp' to end in a state where its default branch 'main' contains the file 'examples/hello.txt' with contents exactly 'hello'."
        " The change must originate on the branch 'feature-example', be authored by 'alice-w' with the commit message 'Add examples/hello.txt',"
        " and merge it using a pull request titled 'Add example' with body 'Introduce a simple example file.' from 'feature-example' to 'main'"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "base_branch": "main"}),
        Action(
                name="get_repo_info_for_owner",
                kwargs={"owner":"alice-w", "repo_name":"acme-webapp"},
            ),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "file_name": "examples/hello.txt", "file_content": "hello"}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "commit_message": "Add examples/hello.txt", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "pr_title": "Add example",
            "pr_body": "Introduce a simple example file.",
            "head_branch_name": "feature-example",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["examples/hello.txt"]
        }),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "feature-example", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example"}),
        Action(
                name="get_repo_info_for_owner",
                kwargs={"owner":"alice-w", "repo_name":"acme-webapp"},
            ),
    ],
    outputs=[
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "description": "A sample demonstration repository",
            "private": False,
            "auto_init": True,
            "default_branch": "main",
            "file_paths": [
            "README.md",
            "LICENSE",
            ".gitignore",
            "requirements.txt",
            "src/main.py",
            "src/app.py",
            "src/utils.py",
            "src/config.py",
            "tests/test_app.py",
            "docs/ARCHITECTURE.md",
            "examples/hello.txt"
            ],
            "file_contents": [
            "# Acme Webapp\n\nFlask-based demo application.",
            "MIT License\n\nCopyright (c) 2023",
            "__pycache__/\n.env\n*.pyc\n",
            "flask==2.3.2\nrequests==2.31.0\n",
            "print('Hello, World!')\n",
            "from flask import Flask\napp = Flask(__name__)\n@app.get('/')\ndef index():\n  return 'OK'\n",
            "def helper(x: int) -> int:\n  return x * 2\n",
            "DEBUG=True\nPORT=5000\n",
            "from src.app import app\n\ndef test_index():\n  client = app.test_client()\n  assert client.get('/').status_code == 200\n",
            "# Architecture\n\n- App layer\n- Utils layer\n- Config\n",
            "hello"
            ],
            "branches": [
            "main",
            "feature-update"
            ],
            "branch_shas": [
            "merge_sha_101",
            "c3d4e5f6a7b8091a2b3c4d5e6f708192a3b4c5d6"
            ],
            "created_ts": "2023-12-01T10:00:00Z",
            "updated_ts": "2025-08-21T12:30:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_08",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to register a high-severity "
        "code scanning alert on the repository 'acme-webapp' describing 'Outdated library in authentication flow' "
        "for 'refs/heads/main', review the alert details, list open high-severity alerts, dismiss the new alert."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="create_code_scanning_alert",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "severity": "high", "description": "Outdated library in authentication flow", "ref": "refs/heads/main"}
        ),
        Action(
            name="get_alert_details",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
            name="list_open_alerts_for_repo",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "severity": "high"}
        ),
        Action(
            name="dismiss_alert",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
    ]
),
Task(
    annotator="0",
    user_id="task_09",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to register a high-severity "
        "code scanning alert on the repository 'acme-webapp' describing 'Outdated library in authentication flow' "
        "for 'refs/heads/main', review the alert details, list open high-severity alerts, dismiss the new alert."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="create_code_scanning_alert",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "severity": "high", "description": "Outdated library in authentication flow", "ref": "refs/heads/main"}
        ),
        Action(
            name="get_alert_details",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
            name="list_open_alerts_for_repo",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "severity": "high"}
        ),
        Action(
            name="dismiss_alert",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
    ]
),
Task(
    annotator="0",
    user_id="task_10",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure that the repository 'acme-webapp' ends up with "
        "its default branch 'main' containing a README whose contents are exactly 'Corrected README content.'. "
        "This change must originate from the branch named 'hotfix-typo', be authored by 'alice-w' with the commit message "
        "'Fix README typo', and be introduced via a pull request titled 'Hotfix: README typo' with body "
        "'Correct minor README punctuation.' by approving PR"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo", "base_branch": "main"}),
        Action(name="update_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo", "file_name": "README.md", "file_content": "Corrected README content."}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo", "commit_message": "Fix README typo", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_title": "Hotfix: README typo", "pr_body": "Correct minor README punctuation.", "head_branch_name": "hotfix-typo", "base_branch_name": "main", "head_sha": "commit_sha_101", "pr_files": ["README.md"]}),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "hotfix-typo", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo"}),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "success": "PR #101 merged for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'hotfix-typo' created in alice-w/acme-webapp from 'main'.",
            "2025-08-21T12:30:00Z : Updated 'README.md' in alice-w/acme-webapp@hotfix-typo.",
            "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@hotfix-typo.",
            "2025-08-21T12:00:00Z : Pull request #101 created for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'hotfix-typo' into 'main' for alice-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'hotfix-typo' deleted from alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_11",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' ends up with "
        "a new document at 'docs/RELEASE_NOTES_1.1.0.md' whose contents are exactly '## 1.1.0 - Minor fixes - Docs update'. "
        "This change must originate from the line named 'release-notes-1.1.0', be authored by 'alice-w', and be introduced via a pull request titled 'Docs: Release notes 1.1.0' with body "
        "'Add release notes for version 1.1.0.' The pull request must be reviewed by 'john'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "file_name": "docs/RELEASE_NOTES_1.1.0.md", "file_content": "## 1.1.0 - Minor fixes - Docs update"}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "commit_message": "Add docs/RELEASE_NOTES_1.1.0.md", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "pr_title": "Docs: Release notes 1.1.0",
            "pr_body": "Add release notes for version 1.1.0.",
            "head_branch_name": "release-notes-1.1.0",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/RELEASE_NOTES_1.1.0.md"]
        }),
        Action(name="assign_pull_request_reviewers", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101, "reviewers": ["john"]}),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "release-notes-1.1.0", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0"}),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'release-notes-1.1.0' created in alice-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/RELEASE_NOTES_1.1.0.md' to alice-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Pull request #101 created for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #101 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'release-notes-1.1.0' into 'main' for alice-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'release-notes-1.1.0' deleted from alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_12",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co and auth key as 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'."
        " Your mission is for the repository 'ui-kit' to end in a state where its default branch 'main' contains the component file 'packages/alert/index.tsx' with"
        " contents exactly 'export const Alert = () => <div role='alert' />'. The change must originate on the branch 'feature-alert',"
        " be authored by 'ui-team' with the commit message 'Add packages/alert/index.tsx', and be represented by a pull request titled 'Add Alert component' with body 'Introduce basic Alert component.'"
        " from 'feature-alert' to 'main' and approving the pr."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="create_new_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "file_name": "packages/alert/index.tsx", "file_content": "export const Alert = () => <div role='alert' />"}),
        Action(name="initial_commit", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "commit_message": "Add packages/alert/index.tsx", "commit_author": "ui-team"}),
        Action(name="create_pull_request", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "pr_title": "Add Alert component",
            "pr_body": "Introduce basic Alert component.",
            "head_branch_name": "feature-alert",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["packages/alert/index.tsx"]
        }),
        Action(name="approve_pr", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "source_branch_name": "feature-alert", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert"}),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "success": "Branch 'feature-alert' deleted from ui-team/ui-kit.",
            "repo": "ui-team/ui-kit",
            "deleted_branch": "feature-alert",
            "removed_file_count": 11,
            "remaining_branches": [
            "main",
            "release-1.0",
            "feature-theme"
            ]
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-alert' created in ui-team/ui-kit from 'main'.",
            "2025-08-21T12:00:00Z : Added 'packages/alert/index.tsx' to ui-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Initial commit added to ui-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Pull request #101 created for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : Merged 'feature-alert' into 'main' for ui-team/ui-kit with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : Branch 'feature-alert' deleted from ui-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_13",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' reflects a new bug "
        "record whose title is 'Login page fails on refresh' and body is 'Refreshing the login page causes a 500 error on first load after deployment.' "
        "labeled with ['bug', 'high-priority'] and assigned to ['frontend team', 'backend team']. The record must include two remarks: "
        "'Investigated client-side cache headers.' by 'frontend team' and 'Patched session middleware.' by 'backend team'. "
        "The record should end in state 'closed' when complete."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "title": "Login page fails on refresh",
            "body": "Refreshing the login page causes a 500 error on first load after deployment.",
            "labels": ["bug", "high-priority"],
            "assignees": ["frontend team", "backend team"]
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Investigated client-side cache headers.",
            "issue_comment_user": "frontend team"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Patched session middleware.",
            "issue_comment_user": "backend team"
        }),
        Action(name="close_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 101
        }),
        # Action(name="get_all_issues_for_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp"}),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Added issue #101 to existing bucket",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Issue #101 closed for alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_14",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your task is to ensure the repository 'ui-kit' reflects a new enhancement "
        "record whose title is 'Add accessible Tooltip component' and body is 'Create a Tooltip that meets WCAG 2.2 with keyboard focus management.' "
        "labeled with ['enhancement', 'accessibility'] and assigned to ['ui-team']. The record must include two remarks: "
        "'Spec approved.' by 'design' and 'Implemented basic prototype.' by 'ui-team'. "
        "The record should end in state 'closed' when complete."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="create_new_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "title": "Add accessible Tooltip component",
            "body": "Create a Tooltip that meets WCAG 2.2 with keyboard focus management.",
            "labels": ["enhancement", "accessibility"],
            "assignees": ["ui-team"]
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Spec approved.",
            "issue_comment_user": "design"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Implemented basic prototype.",
            "issue_comment_user": "ui-team"
        }),
        Action(name="close_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101
        }),
        # Action(name="get_all_issues_for_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit"}),
        # Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for ui-team/ui-kit.",
            "repo": "ui-team/ui-kit",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_15",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' ends up with "
        "an open code scanning alert recorded at ref 'refs/heads/main' having severity 'high' and description "
        "'SQL injection risk detected in src/db.py (user input concatenation).'. The alert must remain open and be "
        "retrievable by its details after creation."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "alice-w", "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="create_code_scanning_alert", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp",
            "severity": "high",
            "description": "SQL injection risk detected in src/db.py (user input concatenation).",
            "ref": "refs/heads/main"
        }),
        Action(name="get_alert_details", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp",
            "alert_number": 101
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp"
        }),
    ],
    outputs=[
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "count": 2,
            "alerts": [
            {
                "number": 9,
                "severity": "high",
                "state": "open",
                "description": "SQL injection vulnerability in user input handling",
                "ref": "refs/heads/main",
                "created_ts": "2023-12-02T14:30:00Z",
                "dismissed_ts": None
            },
            {
                "number": 101,
                "severity": "high",
                "state": "open",
                "description": "SQL injection risk detected in src/db.py (user input concatenation).",
                "ref": "refs/heads/main",
                "created_ts": "2025-08-21T12:00:00Z",
                "dismissed_ts": None
            }
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_16",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your task is to ensure the repository 'ui-kit' ends with a code "
        "scanning alert initially recorded at ref 'refs/heads/main' having severity 'medium' and description "
        "'Unsafe innerHTML assignment detected in packages/card/index.tsx.' which is then dismissed with reason "
        "'false_positive'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "ui-team", "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="create_code_scanning_alert", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit",
            "severity": "medium",
            "description": "Unsafe innerHTML assignment detected in packages/card/index.tsx.",
            "ref": "refs/heads/main"
        }),
        Action(name="get_alert_details", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit",
            "alert_number": 101
        }),
        Action(name="dismiss_alert", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit",
            "alert_number": 101,
            "dismiss_reason": "false_positive"
        }),
        # Action(name="list_open_alerts_for_repo", kwargs={
        #     "owner": "ui-team", "repo_name": "ui-kit"
        # }),
        Action(name="get_alert_details", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit",
            "alert_number": 101
        }),
    ],
    outputs=[
        {
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "number": 101,
            "severity": "medium",
            "state": "dismissed",
            "description": "Unsafe innerHTML assignment detected in packages/card/index.tsx.",
            "ref": "refs/heads/main",
            "created_ts": "2025-08-21T12:00:00Z",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_17",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' ends with no "
        "open code scanning alert after handling, record an alert at ref 'refs/heads/feature-hardening' "
        "with severity 'medium' and description 'Weak hashing algorithm (md5) used in src/utils.py.'. "
        "The alert must be dismissed with reason 'wontfix'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "alice-w", "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="create_code_scanning_alert", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp",
            "severity": "medium",
            "description": "Weak hashing algorithm (md5) used in src/utils.py.",
            "ref": "refs/heads/feature-hardening"
        }),
        Action(name="dismiss_alert", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp",
            "alert_number": 101,
            "dismiss_reason": "wontfix"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp"
        }),
        Action(name="dismiss_alert", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp",
            "alert_number": 9,
            "dismiss_reason": "wontfix"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp"
        }),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Alert #9 dismissed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "alert_number": 9,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "count": 0,
            "alerts": []
        }
    ]
),
Task(
    annotator="0",
    user_id="task_18",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to ensure the repository 'acme-webapp' ends with "
        "no open code scanning alerts. By completion, all alerts for 'acme-webapp' must be in a non-open state by dismissing reason 'wontfix', and the final open-alerts listing must be empty."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "alice-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp"
        }),
        # Action(name="get_alert_details", kwargs={
        #     "owner": "alice-w",
        #     "repo_name": "acme-webapp",
        #     "alert_number": 9
        # }),
        Action(name="dismiss_alert", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "alert_number": 9,
            "dismiss_reason": "wontfix"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp"
        }),
    ],
    outputs=[
        {
            "success": "Alert #9 dismissed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "alert_number": 9,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "count": 0,
            "alerts": []
        }
    ]
),
Task(
    annotator="0",
    user_id="task_19",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your mission is for the repository 'ui-kit' to solve "
        "all open issues. Each record must receive a remark prior to resolution: issue '6' add "
        "'Icons added for email and phone.' by 'ui-team'; issue '10' add 'Added ThemeProvider guide.' by 'ui-dev'. "
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="get_all_issues_for_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit"}),
        Action(name="add_comment_to_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 6, "issue_comment": "Icons added for email and phone.", "issue_comment_user": "ui-team"}),
        Action(name="add_comment_to_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 10, "issue_comment": "Added ThemeProvider guide.", "issue_comment_user": "ui-dev"}),
        Action(name="close_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 6}),
        Action(name="close_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 10}),
        Action(name="get_all_issues_for_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit"}),
    ],
    outputs=[
        {
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "count": 2,
            "issues": [
            {
                "number": 6,
                "title": "Icon set is incomplete",
                "body": "We are missing several common icons (email, phone)",
                "state": "closed",
                "labels": [
                "design",
                "help-wanted"
                ],
                "assignees": [
                "design-lead"
                ],
                "comments": [
                "Queued for next sprint",
                "Icons added for email and phone."
                ],
                "comment_users": [
                "prod-mgr",
                "ui-team"
                ],
                "created_ts": "2023-12-03T08:45:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            },
            {
                "number": 10,
                "title": "Docs need a theming section",
                "body": "Add a guide on ThemeProvider usage",
                "state": "closed",
                "labels": [
                "documentation"
                ],
                "assignees": [
                "ui-dev"
                ],
                "comments": [
                "Will add examples",
                "Added ThemeProvider guide."
                ],
                "comment_users": [
                "ui-dev",
                "ui-dev"
                ],
                "created_ts": "2023-12-04T10:00:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            }
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_20",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your mission is for the repository 'acme-webapp' to end with "
        "a new branch 'feature-batch-add' that contains exactly four new files with these contents: "
        "'docs/CONTRIBUTING.md' -> 'Contribute via PRs.', "
        "'docs/CODE_OF_CONDUCT.md' -> 'Be kind.', "
        "'examples/usage.ts' -> 'export function run(){return 42}', and "
        "'scripts/setup.sh' -> '#!/usr/bin/env bash echo setup'. "
        "These changes are authored by 'alice-w' with the commit message 'Add 4 files'. "
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "docs/CONTRIBUTING.md", "file_content": "Contribute via PRs."}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "docs/CODE_OF_CONDUCT.md", "file_content": "Be kind."}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "examples/usage.ts", "file_content": "export function run(){return 42}"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "scripts/setup.sh", "file_content": "#!/usr/bin/env bash echo setup"}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "commit_message": "Add 4 files", "commit_author": "alice-w"}),
        Action(
            name="list_all_terminal_message",
            kwargs={}
        ),
    ],
    outputs=[
        {
            "success": "Initial commit added to alice-w/acme-webapp@feature-batch-add.",
            "commit": {
            "sha": "commit_sha_101",
            "message": "Add 4 files",
            "author": "alice-w",
            "timestamp": "2025-08-21T12:00:00Z"
            },
            "branch_commit_count": 1
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-batch-add' created in alice-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/CONTRIBUTING.md' to alice-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'docs/CODE_OF_CONDUCT.md' to alice-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'examples/usage.ts' to alice-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'scripts/setup.sh' to alice-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@feature-batch-add."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_21",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your mission is for the repository 'acme-webapp' to end with "
        "a branch 'feature-setup' where the file 'docs/SETUP.md' containing 'Install dependencies and run'. "
        "and update the fils's content to 'Install dependencies and run. Start server' authored by "
        "'alice-w' using the commit message 'Add docs/SETUP.md', and later was modified by 'alice-w' using the commit message 'Update docs/SETUP.md'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "alice-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="create_new_branch", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "base_branch": "main"
        }),
        Action(name="add_new_file_in_repo", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "file_name": "docs/SETUP.md",
            "file_content": "Install dependencies and run"
        }),
        Action(name="initial_commit", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "commit_message": "Add docs/SETUP.md",
            "commit_author": "alice-w"
        }),
        Action(name="update_file_in_repo", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "file_name": "docs/SETUP.md",
            "file_content": "Install dependencies and run. Start server"
        }),
        Action(name="make_commit", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "commit_message": "Update docs/SETUP.md",
            "commit_author": "alice-w"
        }),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "success": "Updated 'docs/SETUP.md' in alice-w/acme-webapp@feature-setup.",
            "repo": "alice-w/acme-webapp",
            "branch": "feature-setup",
            "file": {
            "file_name": "docs/SETUP.md",
            "previous_content": "Install dependencies and run",
            "new_content": "Install dependencies and run. Start server"
            }
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-setup' created in alice-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/SETUP.md' to alice-w/acme-webapp@feature-setup.",
            "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@feature-setup.",
            "2025-08-21T12:30:00Z : Updated 'docs/SETUP.md' in alice-w/acme-webapp@feature-setup.",
            "2025-08-21T12:30:00Z : Commit added to alice-w/acme-webapp@feature-setup."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_23",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your mission is for the repository 'acme-webapp' to end with "
        "three issue records created and then resolved in state 'closed'. The records must be exactly: "
        "('Login button unresponsive', body 'Clicking “Login” does nothing on Safari 16', labels ['bug','ui'], assignees ['frontend team']); "
        "('Race condition in cache warmup', body 'Concurrent warmup tasks sometimes clobber entries', labels ['bug','backend'], assignees ['backend team']); "
        "and ('Add dark mode docs', body 'Document enabling dark mode in the README', labels ['docs','enhancement'], assignees ['docs team'])."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "alice-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="create_new_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "title": "Login button unresponsive",
            "body": "Clicking “Login” does nothing on Safari 16",
            "labels": ["bug", "ui"],
            "assignees": ["frontend team"]
        }),
        Action(name="create_new_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "title": "Race condition in cache warmup",
            "body": "Concurrent warmup tasks sometimes clobber entries",
            "labels": ["bug", "backend"],
            "assignees": ["backend team"]
        }),
        Action(name="create_new_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "title": "Add dark mode docs",
            "body": "Document enabling dark mode in the README",
            "labels": ["docs", "enhancement"],
            "assignees": ["docs team"]
        }),
        Action(name="close_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 101
        }),
        Action(name="close_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 102
        }),
        Action(name="close_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 103
        }),

    ],
    outputs=[
        {
            "success": "Issue #101 closed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #102 closed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "issue_number": 102,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #103 closed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "issue_number": 103,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_24",
    instruction=(
        "You are 'backend-core' with 'backend@coreservices.io' and auth key as "
        "'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. Your mission is for the repository 'payments-service' to end "
        "with its default branch 'main' containing the file 'src/server.ts' whose contents are exactly "
        "'This file sets the request timeout to 60 seconds.'. The change must originate from the branch "
        "'hotfix-timeout-60s', be authored by 'backend-core' with the commit message 'Increase request timeout to 60s', "
        "and be represented by a pull request titled 'Hotfix: increase timeout' with body 'Set request timeout to 60 seconds in server.ts' and then merge hte PR"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "backend-core",
            "email": "backend@coreservices.io",
            "auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
        }),
        Action(name="create_new_branch", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "branch_name": "hotfix-timeout-60s",
            "base_branch": "main"
        }),
        Action(name="update_file_in_repo", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "branch_name": "hotfix-timeout-60s",
            "file_name": "src/server.ts",
            "file_content": "This file sets the request timeout to 60 seconds."
        }),
        Action(name="initial_commit", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "branch_name": "hotfix-timeout-60s",
            "commit_message": "Increase request timeout to 60s",
            "commit_author": "backend-core"
        }),
        Action(name="create_pull_request", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "pr_title": "Hotfix: increase timeout",
            "pr_body": "Set request timeout to 60 seconds in server.ts",
            "head_branch_name": "hotfix-timeout-60s",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["src/server.ts"]
        }),
        Action(name="approve_pr", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "pr_number": 101
        }),
        Action(name="merge_branch", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "source_branch_name": "hotfix-timeout-60s",
            "target_branch_name": "main"
        }),
        Action(name="mark_pr_as_merged", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "pr_number": 101
        }),
        Action(name="delete_branch", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "branch_name": "hotfix-timeout-60s"
        }),
        Action(
            name="list_all_terminal_message",
            kwargs={},
        ),
    ],
    outputs=[
        {
            "success": "PR #101 merged for backend-core/payments-service.",
            "repo": "backend-core/payments-service",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'hotfix-timeout-60s' created in backend-core/payments-service from 'main'.",
            "2025-08-21T12:30:00Z : Updated 'src/server.ts' in backend-core/payments-service@hotfix-timeout-60s.",
            "2025-08-21T12:00:00Z : Initial commit added to backend-core/payments-service@hotfix-timeout-60s.",
            "2025-08-21T12:00:00Z : Pull request #101 created for backend-core/payments-service.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for backend-core/payments-service.",
            "2025-08-21T12:30:00Z : Merged 'hotfix-timeout-60s' into 'main' for backend-core/payments-service with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for backend-core/payments-service.",
            "2025-08-21T12:30:00Z : Branch 'hotfix-timeout-60s' deleted from backend-core/payments-service."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_25",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your mission is for the repository 'ui-kit' to end "
        "with its default branch 'main' containing the file 'docs/ACCESSIBILITY.md' whose contents are exactly "
        "'This document describes accessibility guidelines for UI components.' in new branch 'feature-a11y-docs', be authored by 'ui-team' with the commit message 'Add ACCESSIBILITY.md docs', "
        "and be represented by a pull request titled 'Add accessibility guidelines' with body 'Provide accessibility standards "
        "for all components.' and merge it back."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "ui-team",
            "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="create_new_branch", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "branch_name": "feature-a11y-docs",
            "base_branch": "main"
        }),
        Action(name="add_new_file_in_repo", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "branch_name": "feature-a11y-docs",
            "file_name": "docs/ACCESSIBILITY.md",
            "file_content": "This document describes accessibility guidelines for UI components."
        }),
        Action(name="initial_commit", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "branch_name": "feature-a11y-docs",
            "commit_message": "Add ACCESSIBILITY.md docs",
            "commit_author": "ui-team"
        }),
        Action(name="create_pull_request", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "pr_title": "Add accessibility guidelines",
            "pr_body": "Provide accessibility standards for all components.",
            "head_branch_name": "feature-a11y-docs",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/ACCESSIBILITY.md"]
        }),
        Action(name="approve_pr", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "pr_number": 101
        }),
        Action(name="merge_branch", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "source_branch_name": "feature-a11y-docs",
            "target_branch_name": "main"
        }),
        Action(name="mark_pr_as_merged", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "pr_number": 101
        }),
        Action(name="delete_branch", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "branch_name": "feature-a11y-docs"
        }),
        Action(
            name="list_all_terminal_message",
            kwargs={},
        ),
    ],
    outputs=[
        {
            "success": "PR #101 merged for ui-team/ui-kit.",
            "repo": "ui-team/ui-kit",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-a11y-docs' created in ui-team/ui-kit from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/ACCESSIBILITY.md' to ui-team/ui-kit@feature-a11y-docs.",
            "2025-08-21T12:00:00Z : Initial commit added to ui-team/ui-kit@feature-a11y-docs.",
            "2025-08-21T12:00:00Z : Pull request #101 created for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : Merged 'feature-a11y-docs' into 'main' for ui-team/ui-kit with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : Branch 'feature-a11y-docs' deleted from ui-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_26",
    instruction=(
        "You are 'backend-core' with 'backend@coreservices.io' and auth key as "
        "'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. Your mission is for the repository 'payments-service' to "
        "end with a new issue created titled 'Database connection leak' with body 'Investigate and fix connection "
        "pool not releasing connections properly.' with lable 'bug'. comments were made by "
        "'mobile-dev' of assigned 'db-team' with the message 'Monitoring shows spikes during peak load.', and finally resolved by closing it."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "backend-core",
            "email": "backend@coreservices.io",
            "auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
        }),
        Action(name="create_new_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "title": "Database connection leak",
            "body": "Investigate and fix connection pool not releasing connections properly.",
            "labels": ["bug"],
            "assignees": ["db-team"]
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 101,
            "issue_comment": "Monitoring shows spikes during peak load.",
            "issue_comment_user": "mobile-dev"
        }),
        Action(name="close_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 101
        }),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for backend-core/payments-service.",
            "repo": "backend-core/payments-service",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_27",
    instruction=(
        "You are 'backend-core' with 'backend@coreservices.io' and auth key as "
        "'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. Your mission is for the repository 'payments-service' to "
        "end with three new issues with label 'bug' created titled 'Color contrast issue', 'Missing ARIA labels', and 'Keyboard navigation bug', "
        "with respective bodies 'Ensure text meets WCAG contrast standards.', 'Add ARIA labels to form fields.', "
        "and 'Fix tab order in modal dialogs.' adding comments 'Verified issue during accessibility testing.','Confirmed missing ARIA labels on signup form.',"
        "'Reproduced bug when navigating modals with keyboard.' respectively from qa-team. and finally close all the issues"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "backend-core",
            "email": "backend@coreservices.io",
            "auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
        }),
        Action(name="create_new_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "title": "Color contrast issue",
            "body": "Ensure text meets WCAG contrast standards.",
            "labels": ["bug"],
            "assignees": ["qa-team"]
        }),
        Action(name="create_new_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "title": "Missing ARIA labels",
            "body": "Add ARIA labels to form fields.",
            "labels": ["bug"],
            "assignees": ["qa-team"]
        }),
        Action(name="create_new_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "title": "Keyboard navigation bug",
            "body": "Fix tab order in modal dialogs.",
            "labels": ["bug"],
            "assignees": ["qa-team"]
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 101,
            "issue_comment": "Verified issue during accessibility testing.",
            "issue_comment_user": "qa-team"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 102,
            "issue_comment": "Confirmed missing ARIA labels on signup form.",
            "issue_comment_user": "qa-team"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 103,
            "issue_comment": "Reproduced bug when navigating modals with keyboard.",
            "issue_comment_user": "qa-team"
        }),
        Action(name="close_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 101
        }),
        Action(name="close_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 102
        }),
        Action(name="close_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 103
        }),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for backend-core/payments-service.",
            "repo": "backend-core/payments-service",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #102 closed for backend-core/payments-service.",
            "repo": "backend-core/payments-service",
            "issue_number": 102,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #103 closed for backend-core/payments-service.",
            "repo": "backend-core/payments-service",
            "issue_number": 103,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
    ]
),
Task(
    annotator="0",
    user_id="task_28",
    instruction=(
        "You are 'mobile-dev' with 'mobile@appstudio.com' and auth key as "
        "'ghp_mob6y7u8i9o0p1qwertyuiopasdfghjklzxcvbnm'. Your mission is for the repository 'flutter-finance-app' to "
        "end with all of its open code scanning alerts dismissed. The repository currently has alerts of varying "
        "severity, and each must be marked dismissed with updated timestamps recorded."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "mobile-dev",
            "email": "mobile@appstudio.com",
            "auth_key": "ghp_mob6y7u8i9o0p1qwertyuiopasdfghjklzxcvbnm"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "mobile-dev",
            "repo_name": "flutter-finance-app"
        }),
        Action(name="dismiss_alert", kwargs={
            "owner": "mobile-dev",
            "repo_name": "flutter-finance-app",
            "alert_number": 57
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "mobile-dev",
            "repo_name": "flutter-finance-app"
        }),
    ],
    outputs=[
        {
            "success": "Alert #57 dismissed for mobile-dev/flutter-finance-app.",
            "repo": "mobile-dev/flutter-finance-app",
            "alert_number": 57,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "mobile-dev",
            "repo_name": "flutter-finance-app",
            "count": 0,
            "alerts": []
        }
    ]
),
Task(
    annotator="0",
    user_id="task_29",
    instruction=(
        "You are 'data-scientist' with 'ds@nlplabs.ai' and auth key as "
        "'ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj'. Your mission is for the repository 'ml-pipeline' to "
        "end with a newly raised code scanning alert 'Unvalidated redirect detected in checkout flow' of severity 'medium' "
        "on ref 'refs/heads/main', and then for that alert to be marked dismissed once triaged as not-exploitable."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "data-scientist",
            "email": "ds@nlplabs.ai",
            "auth_key": "ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj"
        }),
        Action(name="create_code_scanning_alert", kwargs={
            "owner": "data-scientist",
            "repo_name": "ml-pipeline",
            "severity": "medium",
            "description": "Unvalidated redirect detected in checkout flow",
            "ref": "refs/heads/main"
        }),
        # Action(name="get_alert_details", kwargs={
        #     "owner": "data-scientist",
        #     "repo_name": "ml-pipeline",
        #     "alert_number": 101
        # }),
        Action(name="dismiss_alert", kwargs={
            "owner": "data-scientist",
            "repo_name": "ml-pipeline",
            "alert_number": 101,
            "dismiss_reason": "not-exploitable"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "data-scientist",
            "repo_name": "ml-pipeline"
        }),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for data-scientist/ml-pipeline.",
            "repo": "data-scientist/ml-pipeline",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "data-scientist",
            "repo_name": "ml-pipeline",
            "count": 1,
            "alerts": [
            {
                "number": 36,
                "severity": "medium",
                "state": "open",
                "description": "Pickle deserialization security risk",
                "ref": "refs/heads/main",
                "created_ts": "2023-11-20T10:45:00Z",
                "dismissed_ts": None
            }
            ]
        }
    ]
),


Task(
    annotator="0",
    user_id="task_36",
    instruction=(
        "You are 'security-team' with 'security@enterprise.com' and auth key as "
        "'ghp_sec1q2w3e4r5t6y7u8i9o0pasdfghjklzxcvbn'. Your mission is for the repository 'security-scanner' "
        "to end with all open code scanning alerts dismissed"
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "security-team", "email": "security@enterprise.com", "auth_key": "ghp_sec1q2w3e4r5t6y7u8i9o0pasdfghjklzxcvbn"}
        ),
        Action(name="list_open_alerts_for_repo", kwargs={
        "owner": "security-team",
        "repo_name": "security-scanner"
        }),
        Action(name="dismiss_alert", kwargs={
        "owner": "security-team",
        "repo_name": "security-scanner",
        "alert_number": 18
        }),
        Action(name="dismiss_alert", kwargs={
        "owner": "security-team",
        "repo_name": "security-scanner",
        "alert_number": 21
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
        "owner": "security-team",
        "repo_name": "security-scanner"
        }),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
    {
        "success": "Alert #18 dismissed for security-team/security-scanner.",
        "repo": "security-team/security-scanner",
        "alert_number": 18,
        "state": "dismissed",
        "dismissed_ts": "2025-08-21T12:30:00Z"
    },
    {
        "success": "Alert #21 dismissed for security-team/security-scanner.",
        "repo": "security-team/security-scanner",
        "alert_number": 21,
        "state": "dismissed",
        "dismissed_ts": "2025-08-21T12:30:00Z"
    },
    {
    "messages": [
            "2025-08-21T12:30:00Z : Alert #18 dismissed for security-team/security-scanner.",
            "2025-08-21T12:30:00Z : Alert #21 dismissed for security-team/security-scanner."
    ]
    }
    ]
),
Task(
    annotator="0",
    user_id="task_37",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Merge the existing pull request #11 on 'ui-kit' repository"
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}
        ),
        Action(name="get_pr_details", kwargs={
        "owner": "ui-team",
        "repo_name": "ui-kit",
        "pr_number": 11
        }),
        Action(name="approve_pr", kwargs={
        "owner": "ui-team",
        "repo_name": "ui-kit",
        "pr_number": 11
        }),
        Action(name="merge_branch", kwargs={
        "owner": "ui-team",
        "repo_name": "ui-kit",
        "source_branch_name": "feature-theme",
        "target_branch_name": "main"
        }),
        Action(name="mark_pr_as_merged", kwargs={
        "owner": "ui-team",
        "repo_name": "ui-kit",
        "pr_number": 11
        }),
        Action(name="delete_branch", kwargs={
        "owner": "ui-team",
        "repo_name": "ui-kit",
        "branch_name": "feature-theme"
        }),
        Action(name="get_repo_info_for_owner", kwargs={
        "owner": "ui-team",
        "repo_name": "ui-kit"
        }),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
    {
        "owner": "ui-team",
        "repo_name": "ui-kit",
        "description": "Reusable UI components",
        "private": False,
        "auto_init": True,
        "default_branch": "main",
        "file_paths": [
        "README.md",
        "LICENSE",
        ".npmrc",
        "package.json",
        "packages/button/index.tsx",
        "packages/card/index.tsx",
        "packages/theme/index.ts",
        "docs/STYLEGUIDE.md",
        "docs/CONTRIBUTING.md",
        "CHANGELOG.md",
        "examples/theme-preview.tsx"
        ],
        "file_contents": [
        "# UI Kit\n\nComponent library.",
        "MIT License\n",
        "legacy-peer-deps=true\n",
        "{\n  \"name\": \"ui-kit\",\n  \"version\": \"1.0.0\"\n}",
        "export const Button = () => <button>Click</button>;\n",
        "export const Card = () => <div className='card' />;\n",
        "export const Theme = {};\n",
        "# Styleguide\n\nTypography, spacing, color.",
        "# Contributing\n\nPRs welcome. Follow conventional commits.",
        "# Changelog\n- Init\n",
        "export const Preview = () => <div />;\n"
        ],
        "branches": [
        "main",
        "release-1.0"
        ],
        "branch_shas": [
        "merge_sha_101",
        "0aaa999988887777666655554444333322221111"
        ],
        "created_ts": "2023-10-20T08:00:00Z",
        "updated_ts": "2025-08-21T12:30:00Z"
    },
    {
    "messages": [
        "2025-08-21T12:30:00Z : PR #11 marked APPROVE for ui-team/ui-kit.",
        "2025-08-21T12:30:00Z : Merged 'feature-theme' into 'main' for ui-team/ui-kit with SHA merge_sha_101.",
        "2025-08-21T12:30:00Z : PR #11 merged for ui-team/ui-kit.",
        "2025-08-21T12:30:00Z : Branch 'feature-theme' deleted from ui-team/ui-kit."
    ]
    }
    ]
),
Task(
    annotator="0",
    user_id="task_38",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your task is to ensure the repository 'ui-kit' reflects a new enhancement "
        "record whose title is 'Add accessible Tooltip component' and body is 'Create a Tooltip that meets WCAG 2.2 with keyboard focus management.' "
        "labeled with ['enhancement', 'accessibility'] and assigned to ['ui-team']. The record must include two remarks: "
        "'Spec approved.' by 'design' and 'Implemented basic prototype.' by 'ui-team'. "
        "The record should end in state 'closed' when complete."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="create_new_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "title": "Add accessible Tooltip component",
            "body": "Create a Tooltip that meets WCAG 2.2 with keyboard focus management.",
            "labels": ["enhancement", "accessibility"],
            "assignees": ["ui-team"]
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Spec approved.",
            "issue_comment_user": "design"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Implemented basic prototype.",
            "issue_comment_user": "ui-team"
        }),
        Action(name="close_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101
        }),
        # Action(name="get_all_issues_for_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit"}),
        # Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for ui-team/ui-kit.",
            "repo": "ui-team/ui-kit",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        }
    ]
),

Task(
    annotator="0",
    user_id="task_39",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev and auth key as 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'."
        " Your mission is for the repository 'acme-webapp' to end in a state where its default branch 'main' contains the file 'examples/hello.txt' with contents exactly 'hello'."
        " The change must originate on the branch 'feature-example', be authored by 'alice-w' with the commit message 'Add examples/hello.txt',"
        " and merge it using a pull request titled 'Add example' with body 'Introduce a simple example file.' from 'feature-example' to 'main'"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "base_branch": "main"}),
        Action(
                name="get_repo_info_for_owner",
                kwargs={"owner":"alice-w", "repo_name":"acme-webapp"},
            ),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "file_name": "examples/hello.txt", "file_content": "hello"}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "commit_message": "Add examples/hello.txt", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "pr_title": "Add example",
            "pr_body": "Introduce a simple example file.",
            "head_branch_name": "feature-example",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["examples/hello.txt"]
        }),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "feature-example", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example"}),
        Action(
                name="get_repo_info_for_owner",
                kwargs={"owner":"alice-w", "repo_name":"acme-webapp"},
            ),
    ],
    outputs=[
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "description": "A sample demonstration repository",
            "private": False,
            "auto_init": True,
            "default_branch": "main",
            "file_paths": [
            "README.md",
            "LICENSE",
            ".gitignore",
            "requirements.txt",
            "src/main.py",
            "src/app.py",
            "src/utils.py",
            "src/config.py",
            "tests/test_app.py",
            "docs/ARCHITECTURE.md",
            "examples/hello.txt"
            ],
            "file_contents": [
            "# Acme Webapp\n\nFlask-based demo application.",
            "MIT License\n\nCopyright (c) 2023",
            "__pycache__/\n.env\n*.pyc\n",
            "flask==2.3.2\nrequests==2.31.0\n",
            "print('Hello, World!')\n",
            "from flask import Flask\napp = Flask(__name__)\n@app.get('/')\ndef index():\n  return 'OK'\n",
            "def helper(x: int) -> int:\n  return x * 2\n",
            "DEBUG=True\nPORT=5000\n",
            "from src.app import app\n\ndef test_index():\n  client = app.test_client()\n  assert client.get('/').status_code == 200\n",
            "# Architecture\n\n- App layer\n- Utils layer\n- Config\n",
            "hello"
            ],
            "branches": [
            "main",
            "feature-update"
            ],
            "branch_shas": [
            "merge_sha_101",
            "c3d4e5f6a7b8091a2b3c4d5e6f708192a3b4c5d6"
            ],
            "created_ts": "2023-12-01T10:00:00Z",
            "updated_ts": "2025-08-21T12:30:00Z"
        }
    ]
),


Task(
    annotator="0",
    user_id="task_41",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s',"
        " and your task is to add a new security policy to the existing repository 'ui-kit' (description: 'A sample demonstration repository') by introducing a "
        "feature branch 'feature-security-policy' that contributes a file named 'SECURITY.md' at the repository root containing "
        "'## Security Policy. Please report vulnerabilities to security@acme.dev within 24 hours.'. Open a pull "
        "request into 'main' with title 'Add security policy' and body 'Introduce SECURITY.md with coordinated disclosure instructions.' for this change."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}
        ),
        Action(
            name="create_new_branch",
            kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-security-policy", "base_branch": "main"}
        ),
        Action(
            name="add_new_file_in_repo",
            kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-security-policy", "file_name": "SECURITY.md", "file_content": "## Security Policy. Please report vulnerabilities to security@acme.dev within 24 hours."}
        ),
        Action(
            name="initial_commit",
            kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-security-policy", "commit_message": "Add SECURITY.md", "commit_author": "ui-team"}
        ),
        Action(
            name="create_pull_request",
            kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_title": "Add security policy", "pr_body": "Introduce SECURITY.md with coordinated disclosure instructions.", "head_branch_name": "feature-security-policy", "base_branch_name": "main", "head_sha": "commit_sha_101", "pr_files": ["SECURITY.md"]}
        ),
        Action(
            name="list_all_terminal_message",
            kwargs={}
        ),
    ],
    outputs=[
        {
                                                                      "success": "Pull request #101 created for ui-team/ui-kit.",
                                                                      "pull_request": {
                                                                        "number": 101,
                                                                        "title": "Add security policy",
                                                                        "body": "Introduce SECURITY.md with coordinated disclosure instructions.",
                                                                        "state": "open",
                                                                        "base": "main",
                                                                        "head": "feature-security-policy",
                                                                        "head_sha": "commit_sha_101",
                                                                        "files": [
                                                                          "SECURITY.md"
                                                                        ],
                                                                        "created_ts": "2025-08-21T12:00:00Z",
                                                                        "updated_ts": "2025-08-21T12:00:00Z"
                                                                      }
                                                                    },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-security-policy' created in ui-team/ui-kit from 'main'.",
                                                                        "2025-08-21T12:00:00Z : Added 'SECURITY.md' to ui-team/ui-kit@feature-security-policy.",
                                                                        "2025-08-21T12:00:00Z : Initial commit added to ui-team/ui-kit@feature-security-policy.",
                                                                        "2025-08-21T12:00:00Z : Pull request #101 created for ui-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_42",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to assign john to pull request"
        "#5 in 'acme-webapp' repo and he made a comment 'Nice Job' and approved the PR."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
                name="get_pr_details",
                kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "pr_number":5},
            ),
        Action(
            name="assign_pull_request_reviewers",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 5, "reviewers": ["john"]}
        ),
        Action(
            name="add_pull_request_comment",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 5, "comment": "Nice Job", "comment_user": "john", "review_state": "COMMENT"}
        ),
        Action(
            name="approve_pr",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 5}
        ),
        Action(
            name="get_pr_details",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 5}
        ),
        Action(
            name="list_all_terminal_message",
            kwargs={},
        ),
    ],
    outputs=[
        {
            "number": 5,
            "title": "Add authentication module",
            "body": "This PR adds basic authentication functionality",
            "state": "open",
            "base_branch": "main",
            "head_branch": "feature-auth",
            "head_sha": "d1e2f3a4b5c6",
            "mergeable": True,
            "merged": False,
            "files": [
            [
                "src/auth.py",
                "tests/test_auth.py"
            ]
            ],
            "comments": [
            [
                "Looks good overall",
                "Please add more tests",
                "Nice Job"
            ]
            ],
            "comment_users": [
            [
                "dev-sue",
                "qa-mike",
                "john"
            ]
            ],
            "reviewers": [
            [
                "dev-sue",
                "qa-mike",
                "john"
            ]
            ],
            "review_states": [
            [
                [
                "COMMENT",
                "APPROVE"
                ],
                [
                "REQUEST_CHANGES",
                "APPROVE"
                ],
                [
                "REQUESTED",
                "COMMENT",
                "APPROVE"
                ]
            ]
            ],
            "review_events": [
            [
                [
                "COMMENT",
                "APPROVE"
                ],
                [
                "REQUEST_CHANGES",
                "APPROVE"
                ],
                [
                "REQUESTED",
                "COMMENT",
                "APPROVE"
                ]
            ]
            ],
            "created_ts": "2023-12-02T09:00:00Z",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #5 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Comment added to PR #5 for alice-w/acme-webapp; review state/event appended.",
            "2025-08-21T12:30:00Z : PR #5 marked APPROVE for alice-w/acme-webapp."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_43",
    instruction=(

        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to introduce a CLI entry point to "
        "'acme-webapp' via an isolated branch named 'feature-add-cli' adding the file 'cli/main.py' with contents "
        "\"print('Hello from CLI')\" and a commit message 'Add CLI entrypoint' authored by 'alice-w', and ensure "
        "this change is integrated into 'main' with the branch cleaned up afterwards."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="create_new_branch",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "base_branch": "main"}
        ),
        Action(
            name="add_new_file_in_repo",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "file_name": "cli/main.py", "file_content": "print('Hello from CLI')"}
        ),
        Action(
            name="initial_commit",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "commit_message": "Add CLI entrypoint", "commit_author": "alice-w"}
        ),
        Action(
                name="merge_branch",
                kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "source_branch_name":"feature-add-cli", "target_branch_name":"main"},
            ),
        # Action(
        #     name="mark_pr_as_merged",
        #     kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 11}
        # ),
        Action(
            name="delete_branch",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli"}
        ),

        Action(
            name="get_repo_info_for_owner",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp"}
        ),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "description": "A sample demonstration repository",
            "private": False,
            "auto_init": True,
            "default_branch": "main",
            "file_paths": [
            "README.md",
            "LICENSE",
            ".gitignore",
            "requirements.txt",
            "src/main.py",
            "src/app.py",
            "src/utils.py",
            "src/config.py",
            "tests/test_app.py",
            "docs/ARCHITECTURE.md",
            "cli/main.py"
            ],
            "file_contents": [
            "# Acme Webapp\n\nFlask-based demo application.",
            "MIT License\n\nCopyright (c) 2023",
            "__pycache__/\n.env\n*.pyc\n",
            "flask==2.3.2\nrequests==2.31.0\n",
            "print('Hello, World!')\n",
            "from flask import Flask\napp = Flask(__name__)\n@app.get('/')\ndef index():\n  return 'OK'\n",
            "def helper(x: int) -> int:\n  return x * 2\n",
            "DEBUG=True\nPORT=5000\n",
            "from src.app import app\n\ndef test_index():\n  client = app.test_client()\n  assert client.get('/').status_code == 200\n",
            "# Architecture\n\n- App layer\n- Utils layer\n- Config\n",
            "print('Hello from CLI')"
            ],
            "branches": [
            "main",
            "feature-update"
            ],
            "branch_shas": [
            "merge_sha_101",
            "c3d4e5f6a7b8091a2b3c4d5e6f708192a3b4c5d6"
            ],
            "created_ts": "2023-12-01T10:00:00Z",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
                "2025-08-21T12:00:00Z : Branch 'feature-add-cli' created in alice-w/acme-webapp from 'main'.",
                "2025-08-21T12:00:00Z : Added 'cli/main.py' to alice-w/acme-webapp@feature-add-cli.",
                "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@feature-add-cli.",
                "2025-08-21T12:30:00Z : Merged 'feature-add-cli' into 'main' for alice-w/acme-webapp with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : Branch 'feature-add-cli' deleted from alice-w/acme-webapp."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_46",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to register a high-severity "
        "code scanning alert on the repository 'acme-webapp' describing 'Outdated library in authentication flow' "
        "for 'refs/heads/main', review the alert details, list open high-severity alerts, dismiss the new alert."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="create_code_scanning_alert",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "severity": "high", "description": "Outdated library in authentication flow", "ref": "refs/heads/main"}
        ),
        Action(
            name="get_alert_details",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
            name="list_open_alerts_for_repo",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "severity": "high"}
        ),
        Action(
            name="dismiss_alert",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
    ]
),

Task(
    annotator="0",
    user_id="task_47",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' ends up with "
        "a new document at 'docs/RELEASE_NOTES_1.1.0.md' whose contents are exactly '## 1.1.0 - Minor fixes - Docs update'. "
        "This change must originate from the line named 'release-notes-1.1.0', be authored by 'alice-w', and be introduced via a pull request titled 'Docs: Release notes 1.1.0' with body "
        "'Add release notes for version 1.1.0.' The pull request must be reviewed by 'john'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "file_name": "docs/RELEASE_NOTES_1.1.0.md", "file_content": "## 1.1.0 - Minor fixes - Docs update"}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "commit_message": "Add docs/RELEASE_NOTES_1.1.0.md", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "pr_title": "Docs: Release notes 1.1.0",
            "pr_body": "Add release notes for version 1.1.0.",
            "head_branch_name": "release-notes-1.1.0",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/RELEASE_NOTES_1.1.0.md"]
        }),
        Action(name="assign_pull_request_reviewers", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101, "reviewers": ["john"]}),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "release-notes-1.1.0", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0"}),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'release-notes-1.1.0' created in alice-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/RELEASE_NOTES_1.1.0.md' to alice-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Pull request #101 created for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #101 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'release-notes-1.1.0' into 'main' for alice-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'release-notes-1.1.0' deleted from alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_48",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co and auth key as 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'."
        " Your mission is for the repository 'ui-kit' to end in a state where its default branch 'main' contains the component file 'packages/alert/index.tsx' with"
        " contents exactly 'export const Alert = () => <div role='alert' />'. The change must originate on the branch 'feature-alert',"
        " be authored by 'ui-team' with the commit message 'Add packages/alert/index.tsx', and be represented by a pull request titled 'Add Alert component' with body 'Introduce basic Alert component.'"
        " from 'feature-alert' to 'main' and approving the pr."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="create_new_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "file_name": "packages/alert/index.tsx", "file_content": "export const Alert = () => <div role='alert' />"}),
        Action(name="initial_commit", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "commit_message": "Add packages/alert/index.tsx", "commit_author": "ui-team"}),
        Action(name="create_pull_request", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "pr_title": "Add Alert component",
            "pr_body": "Introduce basic Alert component.",
            "head_branch_name": "feature-alert",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["packages/alert/index.tsx"]
        }),
        Action(name="approve_pr", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "source_branch_name": "feature-alert", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert"}),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "success": "Branch 'feature-alert' deleted from ui-team/ui-kit.",
            "repo": "ui-team/ui-kit",
            "deleted_branch": "feature-alert",
            "removed_file_count": 11,
            "remaining_branches": [
            "main",
            "release-1.0",
            "feature-theme"
            ]
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-alert' created in ui-team/ui-kit from 'main'.",
            "2025-08-21T12:00:00Z : Added 'packages/alert/index.tsx' to ui-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Initial commit added to ui-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Pull request #101 created for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : Merged 'feature-alert' into 'main' for ui-team/ui-kit with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : Branch 'feature-alert' deleted from ui-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_49",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' reflects a new bug "
        "record whose title is 'Login page fails on refresh' and body is 'Refreshing the login page causes a 500 error on first load after deployment.' "
        "labeled with ['bug', 'high-priority'] and assigned to ['frontend team', 'backend team']. The record must include two remarks: "
        "'Investigated client-side cache headers.' by 'frontend team' and 'Patched session middleware.' by 'backend team'. "
        "The record should end in state 'closed' when complete."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "title": "Login page fails on refresh",
            "body": "Refreshing the login page causes a 500 error on first load after deployment.",
            "labels": ["bug", "high-priority"],
            "assignees": ["frontend team", "backend team"]
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Investigated client-side cache headers.",
            "issue_comment_user": "frontend team"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Patched session middleware.",
            "issue_comment_user": "backend team"
        }),
        Action(name="close_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 101
        }),
        # Action(name="get_all_issues_for_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp"}),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Added issue #101 to existing bucket",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Issue #101 closed for alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_50",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your task is to ensure the repository 'ui-kit' reflects a new enhancement "
        "record whose title is 'Add accessible Tooltip component' and body is 'Create a Tooltip that meets WCAG 2.2 with keyboard focus management.' "
        "labeled with ['enhancement', 'accessibility'] and assigned to ['ui-team']. The record must include two remarks: "
        "'Spec approved.' by 'design' and 'Implemented basic prototype.' by 'ui-team'. "
        "The record should end in state 'closed' when complete."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="create_new_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "title": "Add accessible Tooltip component",
            "body": "Create a Tooltip that meets WCAG 2.2 with keyboard focus management.",
            "labels": ["enhancement", "accessibility"],
            "assignees": ["ui-team"]
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Spec approved.",
            "issue_comment_user": "design"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Implemented basic prototype.",
            "issue_comment_user": "ui-team"
        }),
        Action(name="close_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101
        }),
        # Action(name="get_all_issues_for_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit"}),
        # Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for ui-team/ui-kit.",
            "repo": "ui-team/ui-kit",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_51",
    instruction=(
        "You are 'backend-core' with 'backend@coreservices.io' and auth key as "
        "'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. Your mission is for the repository 'payments-service' to "
        "end with three new issues with lable 'bug' created titled 'Color contrast issue', 'Missing ARIA labels', and 'Keyboard navigation bug', "
        "with respective bodies 'Ensure text meets WCAG contrast standards.', 'Add ARIA labels to form fields.', "
        "and 'Fix tab order in modal dialogs.' adding comments 'Verified issue during accessibility testing.','Confirmed missing ARIA labels on signup form.',"
        "'Reproduced bug when navigating modals with keyboard.' respectively from qa-team. and finally close the issue"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "backend-core",
            "email": "backend@coreservices.io",
            "auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
        }),
        Action(name="create_new_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "title": "Color contrast issue",
            "body": "Ensure text meets WCAG contrast standards.",
            "labels": ["bug"],
            "assignees": ["qa-team"]
        }),
        Action(name="create_new_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "title": "Missing ARIA labels",
            "body": "Add ARIA labels to form fields.",
            "labels": ["bug"],
            "assignees": ["qa-team"]
        }),
        Action(name="create_new_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "title": "Keyboard navigation bug",
            "body": "Fix tab order in modal dialogs.",
            "labels": ["bug"],
            "assignees": ["qa-team"]
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 101,
            "issue_comment": "Verified issue during accessibility testing.",
            "issue_comment_user": "qa-team"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 102,
            "issue_comment": "Confirmed missing ARIA labels on signup form.",
            "issue_comment_user": "qa-team"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 103,
            "issue_comment": "Reproduced bug when navigating modals with keyboard.",
            "issue_comment_user": "qa-team"
        }),
        Action(name="close_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 101
        }),
        Action(name="close_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 102
        }),
        Action(name="close_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 103
        }),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for backend-core/payments-service.",
            "repo": "backend-core/payments-service",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #102 closed for backend-core/payments-service.",
            "repo": "backend-core/payments-service",
            "issue_number": 102,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #103 closed for backend-core/payments-service.",
            "repo": "backend-core/payments-service",
            "issue_number": 103,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
    ]
),
Task(
    annotator="0",
    user_id="task_52",
    instruction=(
        "You are 'mobile-dev' with 'mobile@appstudio.com' and auth key as "
        "'ghp_mob6y7u8i9o0p1qwertyuiopasdfghjklzxcvbnm'. Your mission is for the repository 'flutter-finance-app' to "
        "end with all of its open code scanning alerts dismissed. The repository currently has alerts of varying "
        "severity, and each must be marked dismissed with updated timestamps recorded."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "mobile-dev",
            "email": "mobile@appstudio.com",
            "auth_key": "ghp_mob6y7u8i9o0p1qwertyuiopasdfghjklzxcvbnm"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "mobile-dev",
            "repo_name": "flutter-finance-app"
        }),
        Action(name="dismiss_alert", kwargs={
            "owner": "mobile-dev",
            "repo_name": "flutter-finance-app",
            "alert_number": 57
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "mobile-dev",
            "repo_name": "flutter-finance-app"
        }),
    ],
    outputs=[
        {
            "success": "Alert #57 dismissed for mobile-dev/flutter-finance-app.",
            "repo": "mobile-dev/flutter-finance-app",
            "alert_number": 57,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "mobile-dev",
            "repo_name": "flutter-finance-app",
            "count": 0,
            "alerts": []
        }
    ]
),
Task(
    annotator="0",
    user_id="task_53",
    instruction=(
        "You are 'data-scientist' with 'ds@nlplabs.ai' and auth key as "
        "'ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj'. Your mission is for the repository 'ml-pipeline' to "
        "end with a newly raised code scanning alert 'Unvalidated redirect detected in checkout flow' of severity 'medium' "
        "on ref 'refs/heads/main', and then for that alert to be marked dismissed once triaged as not-exploitable."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "data-scientist",
            "email": "ds@nlplabs.ai",
            "auth_key": "ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj"
        }),
        Action(name="create_code_scanning_alert", kwargs={
            "owner": "data-scientist",
            "repo_name": "ml-pipeline",
            "severity": "medium",
            "description": "Unvalidated redirect detected in checkout flow",
            "ref": "refs/heads/main"
        }),
        # Action(name="get_alert_details", kwargs={
        #     "owner": "data-scientist",
        #     "repo_name": "ml-pipeline",
        #     "alert_number": 101
        # }),
        Action(name="dismiss_alert", kwargs={
            "owner": "data-scientist",
            "repo_name": "ml-pipeline",
            "alert_number": 101,
            "dismiss_reason": "not-exploitable"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "data-scientist",
            "repo_name": "ml-pipeline"
        }),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for data-scientist/ml-pipeline.",
            "repo": "data-scientist/ml-pipeline",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "data-scientist",
            "repo_name": "ml-pipeline",
            "count": 1,
            "alerts": [
            {
                "number": 36,
                "severity": "medium",
                "state": "open",
                "description": "Pickle deserialization security risk",
                "ref": "refs/heads/main",
                "created_ts": "2023-11-20T10:45:00Z",
                "dismissed_ts": None
            }
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_54",
    instruction=(
        "You are 'security-team' with 'security@enterprise.com' and auth key as "
        "'ghp_sec1q2w3e4r5t6y7u8i9o0pasdfghjklzxcvbn'. Your mission is for the repository 'security-scanner' "
        "to end with all open code scanning alerts dismissed"
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "security-team", "email": "security@enterprise.com", "auth_key": "ghp_sec1q2w3e4r5t6y7u8i9o0pasdfghjklzxcvbn"}
        ),
        Action(name="list_open_alerts_for_repo", kwargs={
        "owner": "security-team",
        "repo_name": "security-scanner"
        }),
        Action(name="dismiss_alert", kwargs={
        "owner": "security-team",
        "repo_name": "security-scanner",
        "alert_number": 18
        }),
        Action(name="dismiss_alert", kwargs={
        "owner": "security-team",
        "repo_name": "security-scanner",
        "alert_number": 21
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
        "owner": "security-team",
        "repo_name": "security-scanner"
        }),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
    {
        "success": "Alert #18 dismissed for security-team/security-scanner.",
        "repo": "security-team/security-scanner",
        "alert_number": 18,
        "state": "dismissed",
        "dismissed_ts": "2025-08-21T12:30:00Z"
    },
    {
        "success": "Alert #21 dismissed for security-team/security-scanner.",
        "repo": "security-team/security-scanner",
        "alert_number": 21,
        "state": "dismissed",
        "dismissed_ts": "2025-08-21T12:30:00Z"
    },
    {
    "messages": [
            "2025-08-21T12:30:00Z : Alert #18 dismissed for security-team/security-scanner.",
            "2025-08-21T12:30:00Z : Alert #21 dismissed for security-team/security-scanner."
    ]
    }
    ]
),

Task(
    annotator="0",
    user_id="task_55",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Merge the existing pull request #11 on 'ui-kit' repository"
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}
        ),
        Action(name="get_pr_details", kwargs={
        "owner": "ui-team",
        "repo_name": "ui-kit",
        "pr_number": 11
        }),
        Action(name="approve_pr", kwargs={
        "owner": "ui-team",
        "repo_name": "ui-kit",
        "pr_number": 11
        }),
        Action(name="merge_branch", kwargs={
        "owner": "ui-team",
        "repo_name": "ui-kit",
        "source_branch_name": "feature-theme",
        "target_branch_name": "main"
        }),
        Action(name="mark_pr_as_merged", kwargs={
        "owner": "ui-team",
        "repo_name": "ui-kit",
        "pr_number": 11
        }),
        Action(name="delete_branch", kwargs={
        "owner": "ui-team",
        "repo_name": "ui-kit",
        "branch_name": "feature-theme"
        }),
        Action(name="get_repo_info_for_owner", kwargs={
        "owner": "ui-team",
        "repo_name": "ui-kit"
        }),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
    {
        "owner": "ui-team",
        "repo_name": "ui-kit",
        "description": "Reusable UI components",
        "private": False,
        "auto_init": True,
        "default_branch": "main",
        "file_paths": [
        "README.md",
        "LICENSE",
        ".npmrc",
        "package.json",
        "packages/button/index.tsx",
        "packages/card/index.tsx",
        "packages/theme/index.ts",
        "docs/STYLEGUIDE.md",
        "docs/CONTRIBUTING.md",
        "CHANGELOG.md",
        "examples/theme-preview.tsx"
        ],
        "file_contents": [
        "# UI Kit\n\nComponent library.",
        "MIT License\n",
        "legacy-peer-deps=true\n",
        "{\n  \"name\": \"ui-kit\",\n  \"version\": \"1.0.0\"\n}",
        "export const Button = () => <button>Click</button>;\n",
        "export const Card = () => <div className='card' />;\n",
        "export const Theme = {};\n",
        "# Styleguide\n\nTypography, spacing, color.",
        "# Contributing\n\nPRs welcome. Follow conventional commits.",
        "# Changelog\n- Init\n",
        "export const Preview = () => <div />;\n"
        ],
        "branches": [
        "main",
        "release-1.0"
        ],
        "branch_shas": [
        "merge_sha_101",
        "0aaa999988887777666655554444333322221111"
        ],
        "created_ts": "2023-10-20T08:00:00Z",
        "updated_ts": "2025-08-21T12:30:00Z"
    },
    {
    "messages": [
        "2025-08-21T12:30:00Z : PR #11 marked APPROVE for ui-team/ui-kit.",
        "2025-08-21T12:30:00Z : Merged 'feature-theme' into 'main' for ui-team/ui-kit with SHA merge_sha_101.",
        "2025-08-21T12:30:00Z : PR #11 merged for ui-team/ui-kit.",
        "2025-08-21T12:30:00Z : Branch 'feature-theme' deleted from ui-team/ui-kit."
    ]
    }
    ]
),
Task(
    annotator="0",
    user_id="task_56",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your task is to ensure the repository 'ui-kit' ends with a code "
        "scanning alert initially recorded at ref 'refs/heads/main' having severity 'medium' and description "
        "'Unsafe innerHTML assignment detected in packages/card/index.tsx.' which is then dismissed with reason "
        "'false_positive'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "ui-team", "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="create_code_scanning_alert", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit",
            "severity": "medium",
            "description": "Unsafe innerHTML assignment detected in packages/card/index.tsx.",
            "ref": "refs/heads/main"
        }),
        Action(name="get_alert_details", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit",
            "alert_number": 101
        }),
        Action(name="dismiss_alert", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit",
            "alert_number": 101,
            "dismiss_reason": "false_positive"
        }),
        # Action(name="list_open_alerts_for_repo", kwargs={
        #     "owner": "ui-team", "repo_name": "ui-kit"
        # }),
        Action(name="get_alert_details", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit",
            "alert_number": 101
        }),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "number": 101,
            "severity": "medium",
            "state": "dismissed",
            "description": "Unsafe innerHTML assignment detected in packages/card/index.tsx.",
            "ref": "refs/heads/main",
            "created_ts": "2025-08-21T12:00:00Z",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Added alert #101 to existing bucket",
            "2025-08-21T12:30:00Z : Alert #101 dismissed for ui-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_57",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev and auth key as 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'."
        " Your mission is for the repository 'acme-webapp' to end in a state where its default branch 'main' contains the file 'examples/hello.txt' with contents exactly 'hello'."
        " The change must originate on the branch 'feature-example', be authored by 'alice-w' with the commit message 'Add examples/hello.txt',"
        " and merge it using a pull request titled 'Add example' with body 'Introduce a simple example file.' from 'feature-example' to 'main'"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "base_branch": "main"}),
        Action(
                name="get_repo_info_for_owner",
                kwargs={"owner":"alice-w", "repo_name":"acme-webapp"},
            ),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "file_name": "examples/hello.txt", "file_content": "hello"}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "commit_message": "Add examples/hello.txt", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "pr_title": "Add example",
            "pr_body": "Introduce a simple example file.",
            "head_branch_name": "feature-example",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["examples/hello.txt"]
        }),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "feature-example", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-example"}),
        Action(
                name="get_repo_info_for_owner",
                kwargs={"owner":"alice-w", "repo_name":"acme-webapp"},
            ),
    ],
    outputs=[
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "description": "A sample demonstration repository",
            "private": False,
            "auto_init": True,
            "default_branch": "main",
            "file_paths": [
            "README.md",
            "LICENSE",
            ".gitignore",
            "requirements.txt",
            "src/main.py",
            "src/app.py",
            "src/utils.py",
            "src/config.py",
            "tests/test_app.py",
            "docs/ARCHITECTURE.md",
            "examples/hello.txt"
            ],
            "file_contents": [
            "# Acme Webapp\n\nFlask-based demo application.",
            "MIT License\n\nCopyright (c) 2023",
            "__pycache__/\n.env\n*.pyc\n",
            "flask==2.3.2\nrequests==2.31.0\n",
            "print('Hello, World!')\n",
            "from flask import Flask\napp = Flask(__name__)\n@app.get('/')\ndef index():\n  return 'OK'\n",
            "def helper(x: int) -> int:\n  return x * 2\n",
            "DEBUG=True\nPORT=5000\n",
            "from src.app import app\n\ndef test_index():\n  client = app.test_client()\n  assert client.get('/').status_code == 200\n",
            "# Architecture\n\n- App layer\n- Utils layer\n- Config\n",
            "hello"
            ],
            "branches": [
            "main",
            "feature-update"
            ],
            "branch_shas": [
            "merge_sha_101",
            "c3d4e5f6a7b8091a2b3c4d5e6f708192a3b4c5d6"
            ],
            "created_ts": "2023-12-01T10:00:00Z",
            "updated_ts": "2025-08-21T12:30:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_58",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to ensure the repository 'acme-webapp' ends with "
        "no open code scanning alerts. By completion, all alerts for 'acme-webapp' must be in a non-open state by dismissing reason 'wontfix', and the final open-alerts listing must be empty."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "alice-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp"
        }),
        # Action(name="get_alert_details", kwargs={
        #     "owner": "alice-w",
        #     "repo_name": "acme-webapp",
        #     "alert_number": 9
        # }),
        Action(name="dismiss_alert", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "alert_number": 9,
            "dismiss_reason": "wontfix"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp"
        }),
    ],
    outputs=[
        {
            "success": "Alert #9 dismissed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "alert_number": 9,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "count": 0,
            "alerts": []
        }
    ]
),
Task(
    annotator="0",
    user_id="task_59",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your mission is for the repository 'ui-kit' to solve "
        "all open issues. Each record must receive a remark prior to resolution: issue '6' add "
        "'Icons added for email and phone.' by 'ui-team'; issue '10' add 'Added ThemeProvider guide.' by 'ui-dev'. "
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="get_all_issues_for_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit"}),
        Action(name="add_comment_to_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 6, "issue_comment": "Icons added for email and phone.", "issue_comment_user": "ui-team"}),
        Action(name="add_comment_to_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 10, "issue_comment": "Added ThemeProvider guide.", "issue_comment_user": "ui-dev"}),
        Action(name="close_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 6}),
        Action(name="close_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 10}),
        Action(name="get_all_issues_for_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit"}),
    ],
    outputs=[
        {
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "count": 2,
            "issues": [
            {
                "number": 6,
                "title": "Icon set is incomplete",
                "body": "We are missing several common icons (email, phone)",
                "state": "closed",
                "labels": [
                "design",
                "help-wanted"
                ],
                "assignees": [
                "design-lead"
                ],
                "comments": [
                "Queued for next sprint",
                "Icons added for email and phone."
                ],
                "comment_users": [
                "prod-mgr",
                "ui-team"
                ],
                "created_ts": "2023-12-03T08:45:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            },
            {
                "number": 10,
                "title": "Docs need a theming section",
                "body": "Add a guide on ThemeProvider usage",
                "state": "closed",
                "labels": [
                "documentation"
                ],
                "assignees": [
                "ui-dev"
                ],
                "comments": [
                "Will add examples",
                "Added ThemeProvider guide."
                ],
                "comment_users": [
                "ui-dev",
                "ui-dev"
                ],
                "created_ts": "2023-12-04T10:00:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            }
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_60",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your mission is for the repository 'acme-webapp' to end with "
        "a new branch 'feature-batch-add' that contains exactly four new files with these contents: "
        "'docs/CONTRIBUTING.md' -> 'Contribute via PRs.', "
        "'docs/CODE_OF_CONDUCT.md' -> 'Be kind.', "
        "'examples/usage.ts' -> 'export function run(){return 42}', and "
        "'scripts/setup.sh' -> '#!/usr/bin/env bash echo setup'. "
        "These changes are authored by 'alice-w' with the commit message 'Add 4 files'. "
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "docs/CONTRIBUTING.md", "file_content": "Contribute via PRs."}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "docs/CODE_OF_CONDUCT.md", "file_content": "Be kind."}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "examples/usage.ts", "file_content": "export function run(){return 42}"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "scripts/setup.sh", "file_content": "#!/usr/bin/env bash echo setup"}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "commit_message": "Add 4 files", "commit_author": "alice-w"}),
        Action(
            name="list_all_terminal_message",
            kwargs={}
        ),
    ],
    outputs=[
        {
            "success": "Initial commit added to alice-w/acme-webapp@feature-batch-add.",
            "commit": {
            "sha": "commit_sha_101",
            "message": "Add 4 files",
            "author": "alice-w",
            "timestamp": "2025-08-21T12:00:00Z"
            },
            "branch_commit_count": 1
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-batch-add' created in alice-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/CONTRIBUTING.md' to alice-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'docs/CODE_OF_CONDUCT.md' to alice-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'examples/usage.ts' to alice-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'scripts/setup.sh' to alice-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@feature-batch-add."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_61",
    instruction=(
        "You are 'data-scientist' with 'ds@nlplabs.ai' and auth key as "
        "'ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj'. Your mission is for the repository 'ml-pipeline' to "
        "end with a newly raised code scanning alert 'Unvalidated redirect detected in checkout flow' of severity 'medium' "
        "on ref 'refs/heads/main', and then for that alert to be marked dismissed once triaged as not-exploitable."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "data-scientist",
            "email": "ds@nlplabs.ai",
            "auth_key": "ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj"
        }),
        Action(name="create_code_scanning_alert", kwargs={
            "owner": "data-scientist",
            "repo_name": "ml-pipeline",
            "severity": "medium",
            "description": "Unvalidated redirect detected in checkout flow",
            "ref": "refs/heads/main"
        }),
        # Action(name="get_alert_details", kwargs={
        #     "owner": "data-scientist",
        #     "repo_name": "ml-pipeline",
        #     "alert_number": 101
        # }),
        Action(name="dismiss_alert", kwargs={
            "owner": "data-scientist",
            "repo_name": "ml-pipeline",
            "alert_number": 101,
            "dismiss_reason": "not-exploitable"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "data-scientist",
            "repo_name": "ml-pipeline"
        }),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for data-scientist/ml-pipeline.",
            "repo": "data-scientist/ml-pipeline",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "data-scientist",
            "repo_name": "ml-pipeline",
            "count": 1,
            "alerts": [
            {
                "number": 36,
                "severity": "medium",
                "state": "open",
                "description": "Pickle deserialization security risk",
                "ref": "refs/heads/main",
                "created_ts": "2023-11-20T10:45:00Z",
                "dismissed_ts": None
            }
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_62",
    instruction=(
        "You are 'bob-dev' with 'bob.martinez@devstudio.com' and auth key as "
        "'ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i'. Your mission is for the repository 'utils-js' to "
        "end with its default branch 'master' containing a new file 'docs/USAGE.md' whose contents are exactly "
        "'# Usage Guide Run npm start to launch the app.'. This change must originate from branch 'feature-docs', "
        "be authored by 'bob-dev' with the commit message  and Pr title as  'Add docs/USAGE.md', and be proposed in a pull request "
        " with body 'Provide instructions for running the chat app.'"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "bob-dev",
            "email": "bob.martinez@devstudio.com",
            "auth_key": "ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i"
        }),
        Action(name="create_new_branch", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "base_branch": "master"
        }),
        Action(name="add_new_file_in_repo", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "file_name": "docs/USAGE.md",
            "file_content": "# Usage Guide Run npm start to launch the app."
        }),
        Action(name="initial_commit", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "commit_message": "Add docs/USAGE.md",
            "commit_author": "bob-dev"
        }),
        Action(name="create_pull_request", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "pr_title": "Add docs/USAGE.md",
            "pr_body": "Provide instructions for running the chat app.",
            "head_branch_name": "feature-docs",
            "base_branch_name": "master",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/USAGE.md"]
        }),
        Action(name="approve_pr", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "pr_number": 101
        }),
        Action(name="merge_branch", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "source_branch_name": "feature-docs",
            "target_branch_name": "master"
        }),
        Action(name="mark_pr_as_merged", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "pr_number": 101
        }),
        Action(name="delete_branch", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs"
        }),
        Action(name="list_all_terminal_message", kwargs={})
    ],
    outputs=[
        {
            "success": "PR #101 merged for bob-dev/utils-js.",
            "repo": "bob-dev/utils-js",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-docs' created in bob-dev/utils-js from 'master'.",
            "2025-08-21T12:00:00Z : Added 'docs/USAGE.md' to bob-dev/utils-js@feature-docs.",
            "2025-08-21T12:00:00Z : Initial commit added to bob-dev/utils-js@feature-docs.",
            "2025-08-21T12:00:00Z : Pull request #101 created for bob-dev/utils-js.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for bob-dev/utils-js.",
            "2025-08-21T12:30:00Z : Merged 'feature-docs' into 'master' for bob-dev/utils-js with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for bob-dev/utils-js.",
            "2025-08-21T12:30:00Z : Branch 'feature-docs' deleted from bob-dev/utils-js."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_63",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to assign john to pull request"
        "#5 in 'acme-webapp' repo and he made a comment 'Nice Job' and approved the PR."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
                name="get_pr_details",
                kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "pr_number":5},
            ),
        Action(
            name="assign_pull_request_reviewers",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 5, "reviewers": ["john"]}
        ),
        Action(
            name="add_pull_request_comment",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 5, "comment": "Nice Job", "comment_user": "john", "review_state": "COMMENT"}
        ),
        Action(
            name="approve_pr",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 5}
        ),
        Action(
            name="get_pr_details",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 5}
        ),
        Action(
            name="list_all_terminal_message",
            kwargs={},
        ),
    ],
    outputs=[
        {
            "number": 5,
            "title": "Add authentication module",
            "body": "This PR adds basic authentication functionality",
            "state": "open",
            "base_branch": "main",
            "head_branch": "feature-auth",
            "head_sha": "d1e2f3a4b5c6",
            "mergeable": True,
            "merged": False,
            "files": [
            [
                "src/auth.py",
                "tests/test_auth.py"
            ]
            ],
            "comments": [
            [
                "Looks good overall",
                "Please add more tests",
                "Nice Job"
            ]
            ],
            "comment_users": [
            [
                "dev-sue",
                "qa-mike",
                "john"
            ]
            ],
            "reviewers": [
            [
                "dev-sue",
                "qa-mike",
                "john"
            ]
            ],
            "review_states": [
            [
                [
                "COMMENT",
                "APPROVE"
                ],
                [
                "REQUEST_CHANGES",
                "APPROVE"
                ],
                [
                "REQUESTED",
                "COMMENT",
                "APPROVE"
                ]
            ]
            ],
            "review_events": [
            [
                [
                "COMMENT",
                "APPROVE"
                ],
                [
                "REQUEST_CHANGES",
                "APPROVE"
                ],
                [
                "REQUESTED",
                "COMMENT",
                "APPROVE"
                ]
            ]
            ],
            "created_ts": "2023-12-02T09:00:00Z",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #5 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Comment added to PR #5 for alice-w/acme-webapp; review state/event appended.",
            "2025-08-21T12:30:00Z : PR #5 marked APPROVE for alice-w/acme-webapp."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_64",
    instruction=(
        "You are 'backend-core' with 'backend@coreservices.io' and auth key "
        "'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. "
        "For 'payments-service', add a diagnostic comment 'Added extra 3DS telemetry to reproduce; monitoring for failures.' to issue #13 and close issue #15, "
        "and then list all issues for the repo."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "backend-core",
            "email": "backend@coreservices.io",
            "auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 13,
            "issue_comment": "Added extra 3DS telemetry to reproduce; monitoring for failures.",
            "issue_comment_user": "backend-core"
        }),
        Action(name="close_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 15
        }),
        Action(name="get_all_issues_for_repo", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service"
        })
    ],
    outputs=[
        {
            "owner": "backend-core",
            "repo_name": "payments-service",
            "count": 2,
            "issues": [
            {
                "number": 13,
                "title": "3DS fallback not triggered",
                "body": "On some cards, 3DS fallback is not invoked",
                "state": "open",
                "labels": [
                "bug",
                "payments"
                ],
                "assignees": [
                "payments-lead",
                "qa-erin"
                ],
                "comments": [
                "Adding logs to reproduce",
                "Added extra 3DS telemetry to reproduce; monitoring for failures."
                ],
                "comment_users": [
                "backend-core",
                "backend-core"
                ],
                "created_ts": "2023-12-03T13:00:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            },
            {
                "number": 15,
                "title": "Timeout too aggressive",
                "body": "Timeout should be 60s for long-running transactions",
                "state": "closed",
                "labels": [
                "bug",
                "priority-medium"
                ],
                "assignees": [
                "backend-core"
                ],
                "comments": [
                "Proposed patch incoming"
                ],
                "comment_users": [
                "backend-core"
                ],
                "created_ts": "2023-12-03T13:30:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            }
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_65",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to ensure the repository 'acme-webapp' ends with "
        "no open code scanning alerts. By completion, all alerts for 'acme-webapp' must be in a non-open state by dismissing reason 'wontfix', and the final open-alerts listing must be empty."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "alice-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp"
        }),
        # Action(name="get_alert_details", kwargs={
        #     "owner": "alice-w",
        #     "repo_name": "acme-webapp",
        #     "alert_number": 9
        # }),
        Action(name="dismiss_alert", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "alert_number": 9,
            "dismiss_reason": "wontfix"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp"
        }),
    ],
    outputs=[
        {
            "success": "Alert #9 dismissed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "alert_number": 9,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "count": 0,
            "alerts": []
        }
    ]
),
Task(
    annotator="0",
    user_id="task_66",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your mission is for the repository 'ui-kit' to solve "
        "all open issues. Each record must receive a remark prior to resolution: issue '6' add "
        "'Icons added for email and phone.' by 'ui-team'; issue '10' add 'Added ThemeProvider guide.' by 'ui-dev'. "
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="get_all_issues_for_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit"}),
        Action(name="add_comment_to_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 6, "issue_comment": "Icons added for email and phone.", "issue_comment_user": "ui-team"}),
        Action(name="add_comment_to_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 10, "issue_comment": "Added ThemeProvider guide.", "issue_comment_user": "ui-dev"}),
        Action(name="close_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 6}),
        Action(name="close_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 10}),
        Action(name="get_all_issues_for_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit"}),
    ],
    outputs=[
        {
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "count": 2,
            "issues": [
            {
                "number": 6,
                "title": "Icon set is incomplete",
                "body": "We are missing several common icons (email, phone)",
                "state": "closed",
                "labels": [
                "design",
                "help-wanted"
                ],
                "assignees": [
                "design-lead"
                ],
                "comments": [
                "Queued for next sprint",
                "Icons added for email and phone."
                ],
                "comment_users": [
                "prod-mgr",
                "ui-team"
                ],
                "created_ts": "2023-12-03T08:45:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            },
            {
                "number": 10,
                "title": "Docs need a theming section",
                "body": "Add a guide on ThemeProvider usage",
                "state": "closed",
                "labels": [
                "documentation"
                ],
                "assignees": [
                "ui-dev"
                ],
                "comments": [
                "Will add examples",
                "Added ThemeProvider guide."
                ],
                "comment_users": [
                "ui-dev",
                "ui-dev"
                ],
                "created_ts": "2023-12-04T10:00:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            }
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_67",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your mission is for the repository 'acme-webapp' to end with "
        "a new branch 'feature-batch-add' that contains exactly four new files with these contents: "
        "'docs/CONTRIBUTING.md' -> 'Contribute via PRs.', "
        "'docs/CODE_OF_CONDUCT.md' -> 'Be kind.', "
        "'examples/usage.ts' -> 'export function run(){return 42}', and "
        "'scripts/setup.sh' -> '#!/usr/bin/env bash echo setup'. "
        "These changes are authored by 'alice-w' with the commit message 'Add 4 files'. "
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "docs/CONTRIBUTING.md", "file_content": "Contribute via PRs."}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "docs/CODE_OF_CONDUCT.md", "file_content": "Be kind."}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "examples/usage.ts", "file_content": "export function run(){return 42}"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "scripts/setup.sh", "file_content": "#!/usr/bin/env bash echo setup"}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "commit_message": "Add 4 files", "commit_author": "alice-w"}),
        Action(
            name="list_all_terminal_message",
            kwargs={}
        ),
    ],
    outputs=[
        {
            "success": "Initial commit added to alice-w/acme-webapp@feature-batch-add.",
            "commit": {
            "sha": "commit_sha_101",
            "message": "Add 4 files",
            "author": "alice-w",
            "timestamp": "2025-08-21T12:00:00Z"
            },
            "branch_commit_count": 1
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-batch-add' created in alice-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/CONTRIBUTING.md' to alice-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'docs/CODE_OF_CONDUCT.md' to alice-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'examples/usage.ts' to alice-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'scripts/setup.sh' to alice-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@feature-batch-add."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_68",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your mission is for the repository 'acme-webapp' to end with "
        "a branch 'feature-setup' where the file 'docs/SETUP.md' containing 'Install dependencies and run'. "
        "and update the fils's content to 'Install dependencies and run. Start server' authored by "
        "'alice-w' using the commit message 'Add docs/SETUP.md', and later was modified by 'alice-w' using the commit message 'Update docs/SETUP.md'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "alice-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="create_new_branch", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "base_branch": "main"
        }),
        Action(name="add_new_file_in_repo", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "file_name": "docs/SETUP.md",
            "file_content": "Install dependencies and run"
        }),
        Action(name="initial_commit", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "commit_message": "Add docs/SETUP.md",
            "commit_author": "alice-w"
        }),
        Action(name="update_file_in_repo", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "file_name": "docs/SETUP.md",
            "file_content": "Install dependencies and run. Start server"
        }),
        Action(name="make_commit", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "commit_message": "Update docs/SETUP.md",
            "commit_author": "alice-w"
        }),
    ],
    outputs=[
        {
            "success": "Updated 'docs/SETUP.md' in alice-w/acme-webapp@feature-setup.",
            "repo": "alice-w/acme-webapp",
            "branch": "feature-setup",
            "file": {
            "file_name": "docs/SETUP.md",
            "previous_content": "Install dependencies and run",
            "new_content": "Install dependencies and run. Start server"
            }
        }
    ]
),
Task(
    annotator="0",
    user_id="task_69",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' ends up with "
        "a new document at 'docs/RELEASE_NOTES_1.1.0.md' whose contents are exactly '## 1.1.0 - Minor fixes - Docs update'. "
        "This change must originate from the line named 'release-notes-1.1.0', be authored by 'alice-w', and be introduced via a pull request titled 'Docs: Release notes 1.1.0' with body "
        "'Add release notes for version 1.1.0.' The pull request must be reviewed by 'john'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "file_name": "docs/RELEASE_NOTES_1.1.0.md", "file_content": "## 1.1.0 - Minor fixes - Docs update"}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "commit_message": "Add docs/RELEASE_NOTES_1.1.0.md", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "pr_title": "Docs: Release notes 1.1.0",
            "pr_body": "Add release notes for version 1.1.0.",
            "head_branch_name": "release-notes-1.1.0",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/RELEASE_NOTES_1.1.0.md"]
        }),
        Action(name="assign_pull_request_reviewers", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101, "reviewers": ["john"]}),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "release-notes-1.1.0", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0"}),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'release-notes-1.1.0' created in alice-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/RELEASE_NOTES_1.1.0.md' to alice-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Pull request #101 created for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #101 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'release-notes-1.1.0' into 'main' for alice-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'release-notes-1.1.0' deleted from alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_70",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your mission is for the repository 'acme-webapp' to end with "
        "three issue records created and then resolved in state 'closed'. The records must be exactly: "
        "('Login button unresponsive', body 'Clicking “Login” does nothing on Safari 16', labels ['bug','ui'], assignees ['frontend team']); "
        "('Race condition in cache warmup', body 'Concurrent warmup tasks sometimes clobber entries', labels ['bug','backend'], assignees ['backend team']); "
        "and ('Add dark mode docs', body 'Document enabling dark mode in the README', labels ['docs','enhancement'], assignees ['docs team'])."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "alice-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="create_new_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "title": "Login button unresponsive",
            "body": "Clicking “Login” does nothing on Safari 16",
            "labels": ["bug", "ui"],
            "assignees": ["frontend team"]
        }),
        Action(name="create_new_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "title": "Race condition in cache warmup",
            "body": "Concurrent warmup tasks sometimes clobber entries",
            "labels": ["bug", "backend"],
            "assignees": ["backend team"]
        }),
        Action(name="create_new_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "title": "Add dark mode docs",
            "body": "Document enabling dark mode in the README",
            "labels": ["docs", "enhancement"],
            "assignees": ["docs team"]
        }),
        Action(name="close_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 101
        }),
        Action(name="close_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 102
        }),
        Action(name="close_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 103
        }),

    ],
    outputs=[
        {
            "success": "Issue #101 closed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #102 closed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "issue_number": 102,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #103 closed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "issue_number": 103,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_71",
    instruction=(

        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to introduce a CLI entry point to "
        "'acme-webapp' via an isolated branch named 'feature-add-cli' adding the file 'cli/main.py' with contents "
        "\"print('Hello from CLI')\" and a commit message 'Add CLI entrypoint' authored by 'alice-w', and ensure "
        "this change is integrated into 'main' with the branch cleaned up afterwards."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="create_new_branch",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "base_branch": "main"}
        ),
        Action(
            name="add_new_file_in_repo",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "file_name": "cli/main.py", "file_content": "print('Hello from CLI')"}
        ),
        Action(
            name="initial_commit",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "commit_message": "Add CLI entrypoint", "commit_author": "alice-w"}
        ),
        Action(
                name="merge_branch",
                kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "source_branch_name":"feature-add-cli", "target_branch_name":"main"},
            ),
        # Action(
        #     name="mark_pr_as_merged",
        #     kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 11}
        # ),
        Action(
            name="delete_branch",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli"}
        ),

        Action(
            name="get_repo_info_for_owner",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp"}
        ),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "description": "A sample demonstration repository",
            "private": False,
            "auto_init": True,
            "default_branch": "main",
            "file_paths": [
            "README.md",
            "LICENSE",
            ".gitignore",
            "requirements.txt",
            "src/main.py",
            "src/app.py",
            "src/utils.py",
            "src/config.py",
            "tests/test_app.py",
            "docs/ARCHITECTURE.md",
            "cli/main.py"
            ],
            "file_contents": [
            "# Acme Webapp\n\nFlask-based demo application.",
            "MIT License\n\nCopyright (c) 2023",
            "__pycache__/\n.env\n*.pyc\n",
            "flask==2.3.2\nrequests==2.31.0\n",
            "print('Hello, World!')\n",
            "from flask import Flask\napp = Flask(__name__)\n@app.get('/')\ndef index():\n  return 'OK'\n",
            "def helper(x: int) -> int:\n  return x * 2\n",
            "DEBUG=True\nPORT=5000\n",
            "from src.app import app\n\ndef test_index():\n  client = app.test_client()\n  assert client.get('/').status_code == 200\n",
            "# Architecture\n\n- App layer\n- Utils layer\n- Config\n",
            "print('Hello from CLI')"
            ],
            "branches": [
            "main",
            "feature-update"
            ],
            "branch_shas": [
            "merge_sha_101",
            "c3d4e5f6a7b8091a2b3c4d5e6f708192a3b4c5d6"
            ],
            "created_ts": "2023-12-01T10:00:00Z",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
                "2025-08-21T12:00:00Z : Branch 'feature-add-cli' created in alice-w/acme-webapp from 'main'.",
                "2025-08-21T12:00:00Z : Added 'cli/main.py' to alice-w/acme-webapp@feature-add-cli.",
                "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@feature-add-cli.",
                "2025-08-21T12:30:00Z : Merged 'feature-add-cli' into 'main' for alice-w/acme-webapp with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : Branch 'feature-add-cli' deleted from alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_72",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to add contribution guidance to "
        "'acme-webapp' with a new file 'CONTRIBUTING.md' whose contents are exactly 'Please follow Conventional Commits.' "
        "authored by 'alice-w' on branch 'feature-branch', proposed via a pull request titled 'Add contributing guide' "
        "with body 'Introduce CONTRIBUTING.md' and merge it back, "
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "file_name": "CONTRIBUTING.md", "file_content": "Please follow Conventional Commits."}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "commit_message": "Add CONTRIBUTING.md", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_title": "Add contributing guide", "pr_body": "Introduce CONTRIBUTING.md", "head_branch_name": "feature-branch", "base_branch_name": "main", "head_sha": "commit_sha_101", "pr_files": ["CONTRIBUTING.md"]}),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "feature-branch", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "feature-branch"}),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
                                                                      "messages": [
                                                                        "2025-08-21T12:00:00Z : Branch 'feature-branch' created in alice-w/acme-webapp from 'main'.",
                                                                        "2025-08-21T12:00:00Z : Added 'CONTRIBUTING.md' to alice-w/acme-webapp@feature-branch.",
                                                                        "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@feature-branch.",
                                                                        "2025-08-21T12:00:00Z : Pull request #101 created for alice-w/acme-webapp.",
                                                                        "2025-08-21T12:30:00Z : PR #101 marked APPROVE for alice-w/acme-webapp.",
                                                                        "2025-08-21T12:30:00Z : Merged 'feature-branch' into 'main' for alice-w/acme-webapp with SHA merge_sha_101.",
                                                                        "2025-08-21T12:30:00Z : PR #101 merged for alice-w/acme-webapp.",
                                                                        "2025-08-21T12:30:00Z : Branch 'feature-branch' deleted from alice-w/acme-webapp."
                                                                      ]
                                                                    }
    ]
),
Task(
    annotator="0",
    user_id="task_73",
    instruction=(
        "You are 'bob-dev' with 'bob.martinez@devstudio.com' and auth key "
        "'ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i'. "
        "you want to Create a feature branch 'feature-tel-input' for 'utils-js' (base: 'master') "
        "add 'src/utils/phone.js' with a simple code 'export const isPhone = 0;' and  with commit message 'Add phone validator'"
        "open a PR titled 'Add phone validation utility' and body 'Introduce simple phone number regex validator.' to merge it back"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "bob-dev",
            "email": "bob.martinez@devstudio.com",
            "auth_key": "ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i"
        }),
        Action(name="create_new_branch", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-tel-input",
            "base_branch": "master"
        }),
        Action(name="add_new_file_in_repo", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-tel-input",
            "file_name": "src/utils/phone.js",
            "file_content": "export const isPhone = 0;"
        }),
        Action(name="initial_commit", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-tel-input",
            "commit_message": "Add phone validator",
            "commit_author": "bob-dev"
        }),
        Action(name="create_pull_request", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "pr_title": "Add phone validation utility",
            "pr_body": "Introduce simple phone number regex validator.",
            "head_branch_name": "feature-tel-input",
            "base_branch_name": "master",
            "head_sha": "commit_sha_101",
            "pr_files": ["src/utils/phone.js"]
        }),
        Action(name="approve_pr", kwargs={
            "owner": "bob-dev", "repo_name": "utils-js", "pr_number": 101
        }),
        Action(name="merge_branch", kwargs={
            "owner": "bob-dev",
            "repo_name": "utils-js",
            "source_branch_name": "feature-tel-input",
            "target_branch_name": "master"
        }),
        Action(name="mark_pr_as_merged", kwargs={
            "owner": "bob-dev", "repo_name": "utils-js", "pr_number": 101
        }),
        Action(name="delete_branch", kwargs={
            "owner": "bob-dev", "repo_name": "utils-js", "branch_name": "feature-tel-input"
        }),
        Action(name="list_all_terminal_message", kwargs={})
    ],
    outputs=[
        {
            "success": "PR #101 merged for bob-dev/utils-js.",
            "repo": "bob-dev/utils-js",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
                "2025-08-21T12:00:00Z : Branch 'feature-tel-input' created in bob-dev/utils-js from 'master'.",
                "2025-08-21T12:00:00Z : Added 'src/utils/phone.js' to bob-dev/utils-js@feature-tel-input.",
                "2025-08-21T12:00:00Z : Initial commit added to bob-dev/utils-js@feature-tel-input.",
                "2025-08-21T12:00:00Z : Pull request #101 created for bob-dev/utils-js.",
                "2025-08-21T12:30:00Z : PR #101 marked APPROVE for bob-dev/utils-js.",
                "2025-08-21T12:30:00Z : Merged 'feature-tel-input' into 'master' for bob-dev/utils-js with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : PR #101 merged for bob-dev/utils-js.",
                "2025-08-21T12:30:00Z : Branch 'feature-tel-input' deleted from bob-dev/utils-js."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_74",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to register a high-severity "
        "code scanning alert on the repository 'acme-webapp' describing 'Outdated library in authentication flow' "
        "for 'refs/heads/main', review the alert details, list open high-severity alerts, dismiss the new alert."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="create_code_scanning_alert",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "severity": "high", "description": "Outdated library in authentication flow", "ref": "refs/heads/main"}
        ),
        Action(
            name="get_alert_details",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
            name="list_open_alerts_for_repo",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "severity": "high"}
        ),
        Action(
            name="dismiss_alert",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
    ]
),

Task(
    annotator="0",
    user_id="task_75",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' ends up with "
        "a new document at 'docs/RELEASE_NOTES_1.1.0.md' whose contents are exactly '## 1.1.0 - Minor fixes - Docs update'. "
        "This change must originate from the line named 'release-notes-1.1.0', be authored by 'alice-w', and be introduced via a pull request titled 'Docs: Release notes 1.1.0' with body "
        "'Add release notes for version 1.1.0.' The pull request must be reviewed by 'john'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "file_name": "docs/RELEASE_NOTES_1.1.0.md", "file_content": "## 1.1.0 - Minor fixes - Docs update"}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "commit_message": "Add docs/RELEASE_NOTES_1.1.0.md", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "pr_title": "Docs: Release notes 1.1.0",
            "pr_body": "Add release notes for version 1.1.0.",
            "head_branch_name": "release-notes-1.1.0",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/RELEASE_NOTES_1.1.0.md"]
        }),
        Action(name="assign_pull_request_reviewers", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101, "reviewers": ["john"]}),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "release-notes-1.1.0", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0"}),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'release-notes-1.1.0' created in alice-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/RELEASE_NOTES_1.1.0.md' to alice-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Pull request #101 created for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #101 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'release-notes-1.1.0' into 'main' for alice-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'release-notes-1.1.0' deleted from alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_76",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co and auth key as 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'."
        " Your mission is for the repository 'ui-kit' to end in a state where its default branch 'main' contains the component file 'packages/alert/index.tsx' with"
        " contents exactly 'export const Alert = () => <div role='alert' />'. The change must originate on the branch 'feature-alert',"
        " be authored by 'ui-team' with the commit message 'Add packages/alert/index.tsx', and be represented by a pull request titled 'Add Alert component' with body 'Introduce basic Alert component.'"
        " from 'feature-alert' to 'main' and approving the pr."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="create_new_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "file_name": "packages/alert/index.tsx", "file_content": "export const Alert = () => <div role='alert' />"}),
        Action(name="initial_commit", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "commit_message": "Add packages/alert/index.tsx", "commit_author": "ui-team"}),
        Action(name="create_pull_request", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "pr_title": "Add Alert component",
            "pr_body": "Introduce basic Alert component.",
            "head_branch_name": "feature-alert",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["packages/alert/index.tsx"]
        }),
        Action(name="approve_pr", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "source_branch_name": "feature-alert", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert"}),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "success": "Branch 'feature-alert' deleted from ui-team/ui-kit.",
            "repo": "ui-team/ui-kit",
            "deleted_branch": "feature-alert",
            "removed_file_count": 11,
            "remaining_branches": [
            "main",
            "release-1.0",
            "feature-theme"
            ]
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-alert' created in ui-team/ui-kit from 'main'.",
            "2025-08-21T12:00:00Z : Added 'packages/alert/index.tsx' to ui-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Initial commit added to ui-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Pull request #101 created for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : Merged 'feature-alert' into 'main' for ui-team/ui-kit with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : Branch 'feature-alert' deleted from ui-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_77",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' reflects a new bug "
        "record whose title is 'Login page fails on refresh' and body is 'Refreshing the login page causes a 500 error on first load after deployment.' "
        "labeled with ['bug', 'high-priority'] and assigned to ['frontend team', 'backend team']. The record must include two remarks: "
        "'Investigated client-side cache headers.' by 'frontend team' and 'Patched session middleware.' by 'backend team'. "
        "The record should end in state 'closed' when complete."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "title": "Login page fails on refresh",
            "body": "Refreshing the login page causes a 500 error on first load after deployment.",
            "labels": ["bug", "high-priority"],
            "assignees": ["frontend team", "backend team"]
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Investigated client-side cache headers.",
            "issue_comment_user": "frontend team"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Patched session middleware.",
            "issue_comment_user": "backend team"
        }),
        Action(name="close_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 101
        }),
        # Action(name="get_all_issues_for_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp"}),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Added issue #101 to existing bucket",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Issue #101 closed for alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_78",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your task is to ensure the repository 'ui-kit' reflects a new enhancement "
        "record whose title is 'Add accessible Tooltip component' and body is 'Create a Tooltip that meets WCAG 2.2 with keyboard focus management.' "
        "labeled with ['enhancement', 'accessibility'] and assigned to ['ui-team']. The record must include two remarks: "
        "'Spec approved.' by 'design' and 'Implemented basic prototype.' by 'ui-team'. "
        "The record should end in state 'closed' when complete."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="create_new_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "title": "Add accessible Tooltip component",
            "body": "Create a Tooltip that meets WCAG 2.2 with keyboard focus management.",
            "labels": ["enhancement", "accessibility"],
            "assignees": ["ui-team"]
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Spec approved.",
            "issue_comment_user": "design"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Implemented basic prototype.",
            "issue_comment_user": "ui-team"
        }),
        Action(name="close_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101
        }),
        # Action(name="get_all_issues_for_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit"}),
        # Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for ui-team/ui-kit.",
            "repo": "ui-team/ui-kit",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_79",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to log and resolve a bug report by closing it, in the "
        "repository 'acme-webapp' by creating an issue titled 'Fix login redirect', body "
        "'Users are redirected to /home instead of /dashboard', label 'bug', assignees 'frontend team' and "
        "'backend team', collect confirmation comments from both teams as 'Backend routing updated.' and 'Frontend redirect fixed.'."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="create_new_issue",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "title": "Fix login redirect", "body": "Users are redirected to /home instead of /dashboard", "labels": ["bug"], "assignees": ["frontend team", "backend team"]}
        ),
        Action(
            name="add_comment_to_issue",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "issue_number": 101, "issue_comment": "Backend routing updated.", "issue_comment_user": "backend team"}
        ),
        Action(
            name="add_comment_to_issue",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "issue_number": 101, "issue_comment": "Frontend redirect fixed.", "issue_comment_user": "frontend team"}
        ),
        Action(
            name="close_issue",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "issue_number": 101}
        ),
        Action(
            name="get_all_issues_for_repo",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp"}
        ),
    ],
    outputs=[
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "count": 3,
            "issues": [
            {
                "number": 3,
                "title": "Performance optimization needed",
                "body": "The current algorithm is too slow for large datasets",
                "state": "open",
                "labels": [
                "enhancement",
                "performance"
                ],
                "assignees": [
                "alice-w",
                "perf-joe"
                ],
                "comments": [
                "I'll look into this",
                "Agreed, we need better algorithms"
                ],
                "comment_users": [
                "alice-w",
                "tech-lead-tara"
                ],
                "created_ts": "2023-12-01T12:00:00Z",
                "updated_ts": "2023-12-02T10:15:00Z"
            },
            {
                "number": 8,
                "title": "Documentation outdated",
                "body": "README needs to be updated with new API changes",
                "state": "closed",
                "labels": [
                "documentation",
                "good-first-issue"
                ],
                "assignees": [
                "docs-amy"
                ],
                "comments": [
                "Working on this now",
                "Updated - please review"
                ],
                "comment_users": [
                "docs-amy",
                "docs-amy"
                ],
                "created_ts": "2023-11-30T08:30:00Z",
                "updated_ts": "2023-12-01T16:45:00Z"
            },
            {
                "number": 101,
                "title": "Fix login redirect",
                "body": "Users are redirected to /home instead of /dashboard",
                "state": "closed",
                "labels": [
                "bug"
                ],
                "assignees": [
                "frontend team",
                "backend team"
                ],
                "comments": [
                "Backend routing updated.",
                "Frontend redirect fixed."
                ],
                "comment_users": [
                "backend team",
                "frontend team"
                ],
                "created_ts": "2025-08-21T12:00:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            }
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_80",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to register a high-severity "
        "code scanning alert on the repository 'acme-webapp' describing 'Outdated library in authentication flow' "
        "for 'refs/heads/main', review the alert details, list open high-severity alerts, dismiss the new alert."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="create_code_scanning_alert",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "severity": "high", "description": "Outdated library in authentication flow", "ref": "refs/heads/main"}
        ),
        Action(
            name="get_alert_details",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
            name="list_open_alerts_for_repo",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "severity": "high"}
        ),
        Action(
            name="dismiss_alert",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
    ]
),
Task(
    annotator="0",
    user_id="task_81",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure that the repository 'acme-webapp' ends up with "
        "its default branch 'main' containing a README whose contents are exactly 'Corrected README content.'. "
        "This change must originate from the branch named 'hotfix-typo', be authored by 'alice-w' with the commit message "
        "'Fix README typo', and be introduced via a pull request titled 'Hotfix: README typo' with body "
        "'Correct minor README punctuation.' by approving PR"
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo", "base_branch": "main"}),
        Action(name="update_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo", "file_name": "README.md", "file_content": "Corrected README content."}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo", "commit_message": "Fix README typo", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_title": "Hotfix: README typo", "pr_body": "Correct minor README punctuation.", "head_branch_name": "hotfix-typo", "base_branch_name": "main", "head_sha": "commit_sha_101", "pr_files": ["README.md"]}),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "hotfix-typo", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo"}),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "success": "PR #101 merged for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'hotfix-typo' created in alice-w/acme-webapp from 'main'.",
            "2025-08-21T12:30:00Z : Updated 'README.md' in alice-w/acme-webapp@hotfix-typo.",
            "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@hotfix-typo.",
            "2025-08-21T12:00:00Z : Pull request #101 created for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'hotfix-typo' into 'main' for alice-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'hotfix-typo' deleted from alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_82",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' ends up with "
        "a new document at 'docs/RELEASE_NOTES_1.1.0.md' whose contents are exactly '## 1.1.0 - Minor fixes - Docs update'. "
        "This change must originate from the line named 'release-notes-1.1.0', be authored by 'alice-w', and be introduced via a pull request titled 'Docs: Release notes 1.1.0' with body "
        "'Add release notes for version 1.1.0.' The pull request must be reviewed by 'john'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "file_name": "docs/RELEASE_NOTES_1.1.0.md", "file_content": "## 1.1.0 - Minor fixes - Docs update"}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "commit_message": "Add docs/RELEASE_NOTES_1.1.0.md", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "pr_title": "Docs: Release notes 1.1.0",
            "pr_body": "Add release notes for version 1.1.0.",
            "head_branch_name": "release-notes-1.1.0",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/RELEASE_NOTES_1.1.0.md"]
        }),
        Action(name="assign_pull_request_reviewers", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101, "reviewers": ["john"]}),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "release-notes-1.1.0", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0"}),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'release-notes-1.1.0' created in alice-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/RELEASE_NOTES_1.1.0.md' to alice-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Pull request #101 created for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #101 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'release-notes-1.1.0' into 'main' for alice-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'release-notes-1.1.0' deleted from alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_83",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co and auth key as 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'."
        " Your mission is for the repository 'ui-kit' to end in a state where its default branch 'main' contains the component file 'packages/alert/index.tsx' with"
        " contents exactly 'export const Alert = () => <div role='alert' />'. The change must originate on the branch 'feature-alert',"
        " be authored by 'ui-team' with the commit message 'Add packages/alert/index.tsx', and be represented by a pull request titled 'Add Alert component' with body 'Introduce basic Alert component.'"
        " from 'feature-alert' to 'main' and approving the pr."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="create_new_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "file_name": "packages/alert/index.tsx", "file_content": "export const Alert = () => <div role='alert' />"}),
        Action(name="initial_commit", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "commit_message": "Add packages/alert/index.tsx", "commit_author": "ui-team"}),
        Action(name="create_pull_request", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "pr_title": "Add Alert component",
            "pr_body": "Introduce basic Alert component.",
            "head_branch_name": "feature-alert",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["packages/alert/index.tsx"]
        }),
        Action(name="approve_pr", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "source_branch_name": "feature-alert", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert"}),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "success": "Branch 'feature-alert' deleted from ui-team/ui-kit.",
            "repo": "ui-team/ui-kit",
            "deleted_branch": "feature-alert",
            "removed_file_count": 11,
            "remaining_branches": [
            "main",
            "release-1.0",
            "feature-theme"
            ]
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-alert' created in ui-team/ui-kit from 'main'.",
            "2025-08-21T12:00:00Z : Added 'packages/alert/index.tsx' to ui-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Initial commit added to ui-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Pull request #101 created for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : Merged 'feature-alert' into 'main' for ui-team/ui-kit with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : Branch 'feature-alert' deleted from ui-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_84",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' reflects a new bug "
        "record whose title is 'Login page fails on refresh' and body is 'Refreshing the login page causes a 500 error on first load after deployment.' "
        "labeled with ['bug', 'high-priority'] and assigned to ['frontend team', 'backend team']. The record must include two remarks: "
        "'Investigated client-side cache headers.' by 'frontend team' and 'Patched session middleware.' by 'backend team'. "
        "The record should end in state 'closed' when complete."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "title": "Login page fails on refresh",
            "body": "Refreshing the login page causes a 500 error on first load after deployment.",
            "labels": ["bug", "high-priority"],
            "assignees": ["frontend team", "backend team"]
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Investigated client-side cache headers.",
            "issue_comment_user": "frontend team"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Patched session middleware.",
            "issue_comment_user": "backend team"
        }),
        Action(name="close_issue", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "issue_number": 101
        }),
        # Action(name="get_all_issues_for_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp"}),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Added issue #101 to existing bucket",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Issue #101 closed for alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_85",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your task is to ensure the repository 'ui-kit' reflects a new enhancement "
        "record whose title is 'Add accessible Tooltip component' and body is 'Create a Tooltip that meets WCAG 2.2 with keyboard focus management.' "
        "labeled with ['enhancement', 'accessibility'] and assigned to ['ui-team']. The record must include two remarks: "
        "'Spec approved.' by 'design' and 'Implemented basic prototype.' by 'ui-team'. "
        "The record should end in state 'closed' when complete."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="create_new_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "title": "Add accessible Tooltip component",
            "body": "Create a Tooltip that meets WCAG 2.2 with keyboard focus management.",
            "labels": ["enhancement", "accessibility"],
            "assignees": ["ui-team"]
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Spec approved.",
            "issue_comment_user": "design"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Implemented basic prototype.",
            "issue_comment_user": "ui-team"
        }),
        Action(name="close_issue", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "issue_number": 101
        }),
        # Action(name="get_all_issues_for_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit"}),
        # Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for ui-team/ui-kit.",
            "repo": "ui-team/ui-kit",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        }
    ]
),
Task(
    annotator="0",
    user_id="task_86",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' ends up with "
        "an open code scanning alert recorded at ref 'refs/heads/main' having severity 'high' and description "
        "'SQL injection risk detected in src/db.py (user input concatenation).'. The alert must remain open and be "
        "retrievable by its details after creation."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "alice-w", "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="create_code_scanning_alert", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp",
            "severity": "high",
            "description": "SQL injection risk detected in src/db.py (user input concatenation).",
            "ref": "refs/heads/main"
        }),
        Action(name="get_alert_details", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp",
            "alert_number": 101
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp"
        }),
    ],
    outputs=[
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "count": 2,
            "alerts": [
            {
                "number": 9,
                "severity": "high",
                "state": "open",
                "description": "SQL injection vulnerability in user input handling",
                "ref": "refs/heads/main",
                "created_ts": "2023-12-02T14:30:00Z",
                "dismissed_ts": None
            },
            {
                "number": 101,
                "severity": "high",
                "state": "open",
                "description": "SQL injection risk detected in src/db.py (user input concatenation).",
                "ref": "refs/heads/main",
                "created_ts": "2025-08-21T12:00:00Z",
                "dismissed_ts": None
            }
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_87",
    instruction=(
        "You are 'data-scientist' with 'ds@nlplabs.ai' and auth key as "
        "'ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj'. Your mission is for the repository 'ml-pipeline' to "
        "end with a newly raised code scanning alert 'Unvalidated redirect detected in checkout flow' of severity 'medium' "
        "on ref 'refs/heads/main', and then for that alert to be marked dismissed once triaged as not-exploitable."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "data-scientist",
            "email": "ds@nlplabs.ai",
            "auth_key": "ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj"
        }),
        Action(name="create_code_scanning_alert", kwargs={
            "owner": "data-scientist",
            "repo_name": "ml-pipeline",
            "severity": "medium",
            "description": "Unvalidated redirect detected in checkout flow",
            "ref": "refs/heads/main"
        }),
        # Action(name="get_alert_details", kwargs={
        #     "owner": "data-scientist",
        #     "repo_name": "ml-pipeline",
        #     "alert_number": 101
        # }),
        Action(name="dismiss_alert", kwargs={
            "owner": "data-scientist",
            "repo_name": "ml-pipeline",
            "alert_number": 101,
            "dismiss_reason": "not-exploitable"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "data-scientist",
            "repo_name": "ml-pipeline"
        }),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for data-scientist/ml-pipeline.",
            "repo": "data-scientist/ml-pipeline",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "data-scientist",
            "repo_name": "ml-pipeline",
            "count": 1,
            "alerts": [
            {
                "number": 36,
                "severity": "medium",
                "state": "open",
                "description": "Pickle deserialization security risk",
                "ref": "refs/heads/main",
                "created_ts": "2023-11-20T10:45:00Z",
                "dismissed_ts": None
            }
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_88",
    instruction=(
        "You are 'backend-core' with 'backend@coreservices.io' and auth key "
        "'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. "
        "For 'payments-service', add a diagnostic comment 'Added extra 3DS telemetry to reproduce; monitoring for failures.' to issue #13 and close issue #15, "
        "and then list all issues for the repo."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "backend-core",
            "email": "backend@coreservices.io",
            "auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
        }),
        Action(name="add_comment_to_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 13,
            "issue_comment": "Added extra 3DS telemetry to reproduce; monitoring for failures.",
            "issue_comment_user": "backend-core"
        }),
        Action(name="close_issue", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service",
            "issue_number": 15
        }),
        Action(name="get_all_issues_for_repo", kwargs={
            "owner": "backend-core",
            "repo_name": "payments-service"
        })
    ],
    outputs=[
        {
            "owner": "backend-core",
            "repo_name": "payments-service",
            "count": 2,
            "issues": [
            {
                "number": 13,
                "title": "3DS fallback not triggered",
                "body": "On some cards, 3DS fallback is not invoked",
                "state": "open",
                "labels": [
                "bug",
                "payments"
                ],
                "assignees": [
                "payments-lead",
                "qa-erin"
                ],
                "comments": [
                "Adding logs to reproduce",
                "Added extra 3DS telemetry to reproduce; monitoring for failures."
                ],
                "comment_users": [
                "backend-core",
                "backend-core"
                ],
                "created_ts": "2023-12-03T13:00:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            },
            {
                "number": 15,
                "title": "Timeout too aggressive",
                "body": "Timeout should be 60s for long-running transactions",
                "state": "closed",
                "labels": [
                "bug",
                "priority-medium"
                ],
                "assignees": [
                "backend-core"
                ],
                "comments": [
                "Proposed patch incoming"
                ],
                "comment_users": [
                "backend-core"
                ],
                "created_ts": "2023-12-03T13:30:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            }
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_89",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your task is for the repository "
        "'ui-kit' to dismiss open medium-severity code scanning alerts on 'refs/heads/main'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "ui-team",
            "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "severity": "medium",
            "ref": "refs/heads/main"
        }),
        Action(name="get_alert_details", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="dismiss_alert", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="get_alert_details", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "number": 2,
            "severity": "medium",
            "state": "dismissed",
            "description": "Potential XSS in button label",
            "ref": "refs/heads/main",
            "created_ts": "2023-12-03T12:00:00Z",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:30:00Z : Alert #2 dismissed for ui-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_90",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. approve and merge pull request #12 for ui-kit repo."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "ui-team",
            "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="get_pr_details", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit", "pr_number": 12
        }),
        Action(name="approve_pr", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit", "pr_number": 12
        }),
        Action(name="merge_branch", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit",
            "source_branch_name": "release-1.0",
            "target_branch_name": "main"
        }),
        Action(name="mark_pr_as_merged", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit", "pr_number": 12
        }),
        Action(name="delete_branch", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit", "branch_name": "release-1.0"
        }),
        Action(name="get_repo_info_for_owner", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit"
        }),
        Action(name="list_all_terminal_message", kwargs={})
    ],
    outputs=[
        {
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "description": "Reusable UI components",
            "private": False,
            "auto_init": True,
            "default_branch": "main",
            "file_paths": [
            "README.md",
            "LICENSE",
            ".npmrc",
            "package.json",
            "packages/button/index.tsx",
            "packages/card/index.tsx",
            "docs/STYLEGUIDE.md",
            "CHANGELOG.md"
            ],
            "file_contents": [
            "# UI Kit\n\nComponent library.",
            "MIT License\n",
            "legacy-peer-deps=true\n",
            "{\n  \"name\": \"ui-kit\",\n  \"version\": \"1.0.0\"\n}",
            "export const Button = () => <button>Click</button>;\n",
            "export const Card = () => <div className='card' />;\n",
            "# Styleguide\n\nTypography, spacing, color.",
            "# Changelog\n- Init\n"
            ],
            "branches": [
            "main",
            "feature-theme"
            ],
            "branch_shas": [
            "merge_sha_101",
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            ],
            "created_ts": "2023-10-20T08:00:00Z",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
                "2025-08-21T12:30:00Z : PR #12 marked APPROVE for ui-team/ui-kit.",
                "2025-08-21T12:30:00Z : Merged 'release-1.0' into 'main' for ui-team/ui-kit with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : PR #12 merged for ui-team/ui-kit.",
                "2025-08-21T12:30:00Z : Branch 'release-1.0' deleted from ui-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_91",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your task is to register a high-severity "
        "code scanning alert on the repository 'acme-webapp' describing 'Outdated library in authentication flow' "
        "for 'refs/heads/main', review the alert details, list open high-severity alerts, dismiss the new alert."
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="create_code_scanning_alert",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "severity": "high", "description": "Outdated library in authentication flow", "ref": "refs/heads/main"}
        ),
        Action(
            name="get_alert_details",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
            name="list_open_alerts_for_repo",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "severity": "high"}
        ),
        Action(
            name="dismiss_alert",
            kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for alice-w/acme-webapp.",
            "repo": "alice-w/acme-webapp",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
    ]
),

Task(
    annotator="0",
    user_id="task_92",
    instruction=(
        "You are 'security-team' with 'security@enterprise.com' and auth key as "
        "'ghp_sec1q2w3e4r5t6y7u8i9o0pasdfghjklzxcvbn'. Your mission is for the repository 'security-scanner' "
        "to end with all open code scanning alerts dismissed"
    ),
    actions=[
        Action(
            name="authenticate_user",
            kwargs={"username": "security-team", "email": "security@enterprise.com", "auth_key": "ghp_sec1q2w3e4r5t6y7u8i9o0pasdfghjklzxcvbn"}
        ),
        Action(name="list_open_alerts_for_repo", kwargs={
        "owner": "security-team",
        "repo_name": "security-scanner"
        }),
        Action(name="dismiss_alert", kwargs={
        "owner": "security-team",
        "repo_name": "security-scanner",
        "alert_number": 18
        }),
        Action(name="dismiss_alert", kwargs={
        "owner": "security-team",
        "repo_name": "security-scanner",
        "alert_number": 21
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
        "owner": "security-team",
        "repo_name": "security-scanner"
        }),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
    {
        "success": "Alert #18 dismissed for security-team/security-scanner.",
        "repo": "security-team/security-scanner",
        "alert_number": 18,
        "state": "dismissed",
        "dismissed_ts": "2025-08-21T12:30:00Z"
    },
    {
        "success": "Alert #21 dismissed for security-team/security-scanner.",
        "repo": "security-team/security-scanner",
        "alert_number": 21,
        "state": "dismissed",
        "dismissed_ts": "2025-08-21T12:30:00Z"
    },
    {
    "messages": [
            "2025-08-21T12:30:00Z : Alert #18 dismissed for security-team/security-scanner.",
            "2025-08-21T12:30:00Z : Alert #21 dismissed for security-team/security-scanner."
    ]
    }
    ]
),
Task(
    annotator="0",
    user_id="task_93",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your mission is for the repository 'ui-kit' to solve "
        "all open issues. Each record must receive a remark prior to resolution: issue '6' add "
        "'Icons added for email and phone.' by 'ui-team'; issue '10' add 'Added ThemeProvider guide.' by 'ui-dev'. "
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="get_all_issues_for_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit"}),
        Action(name="add_comment_to_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 6, "issue_comment": "Icons added for email and phone.", "issue_comment_user": "ui-team"}),
        Action(name="add_comment_to_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 10, "issue_comment": "Added ThemeProvider guide.", "issue_comment_user": "ui-dev"}),
        Action(name="close_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 6}),
        Action(name="close_issue", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "issue_number": 10}),
        Action(name="get_all_issues_for_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit"}),
    ],
    outputs=[
        {
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "count": 2,
            "issues": [
            {
                "number": 6,
                "title": "Icon set is incomplete",
                "body": "We are missing several common icons (email, phone)",
                "state": "closed",
                "labels": [
                "design",
                "help-wanted"
                ],
                "assignees": [
                "design-lead"
                ],
                "comments": [
                "Queued for next sprint",
                "Icons added for email and phone."
                ],
                "comment_users": [
                "prod-mgr",
                "ui-team"
                ],
                "created_ts": "2023-12-03T08:45:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            },
            {
                "number": 10,
                "title": "Docs need a theming section",
                "body": "Add a guide on ThemeProvider usage",
                "state": "closed",
                "labels": [
                "documentation"
                ],
                "assignees": [
                "ui-dev"
                ],
                "comments": [
                "Will add examples",
                "Added ThemeProvider guide."
                ],
                "comment_users": [
                "ui-dev",
                "ui-dev"
                ],
                "created_ts": "2023-12-04T10:00:00Z",
                "updated_ts": "2025-08-21T12:30:00Z"
            }
            ]
        }
    ]
),





Task(
annotator="0",
user_id="task_94",
instruction=(
"You are 'backend-core' with 'backend@coreservices.io' and auth key as "
"'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. Add an end-to-end test scaffold to 'payments-service': "
"on a new branch 'feature-e2e-tests' from 'main', add file 'tests/e2e/payments_flow.test.ts' with contents "
"'E2E skeleton for payments flow.', with message 'Add E2E payments test skeleton' authored by 'backend-core', "
"open a PRwith titled 'Add E2E tests' (body 'Introduce payments flow E2E skeleton') from 'feature-e2e-tests' to 'main'  and merge it "
),
actions=[
Action(name="authenticate_user", kwargs={
"username": "backend-core",
"email": "backend@coreservices.io",
"auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
}),
Action(name="create_new_branch", kwargs={
"owner": "backend-core",
"repo_name": "payments-service",
"branch_name": "feature-e2e-tests",
"base_branch": "main"
}),
Action(name="add_new_file_in_repo", kwargs={
"owner": "backend-core",
"repo_name": "payments-service",
"branch_name": "feature-e2e-tests",
"file_name": "tests/e2e/payments_flow.test.ts",
"file_content": "E2E skeleton for payments flow."
}),
Action(name="initial_commit", kwargs={
"owner": "backend-core",
"repo_name": "payments-service",
"branch_name": "feature-e2e-tests",
"commit_message": "Add E2E payments test skeleton",
"commit_author": "backend-core"
}),
Action(name="create_pull_request", kwargs={
"owner": "backend-core",
"repo_name": "payments-service",
"pr_title": "Add E2E tests",
"pr_body": "Introduce payments flow E2E skeleton",
"head_branch_name": "feature-e2e-tests",
"base_branch_name": "main",
"head_sha": "commit_sha_101",
"pr_files": ["tests/e2e/payments_flow.test.ts"]
}),
Action(name="approve_pr", kwargs={
"owner": "backend-core",
"repo_name": "payments-service",
"pr_number": 101
}),
Action(name="merge_branch", kwargs={
"owner": "backend-core",
"repo_name": "payments-service",
"source_branch_name": "feature-e2e-tests",
"target_branch_name": "main"
}),
Action(name="mark_pr_as_merged", kwargs={
"owner": "backend-core",
"repo_name": "payments-service",
"pr_number": 101
}),
Action(name="delete_branch", kwargs={
"owner": "backend-core",
"repo_name": "payments-service",
"branch_name": "feature-e2e-tests"
}),
Action(name="list_all_terminal_message", kwargs={}),
],
outputs=[
{
    "success": "PR #101 merged for backend-core/payments-service.",
    "repo": "backend-core/payments-service",
    "pr_number": 101,
    "state": "merged",
    "merged": True,
    "mergeable": True,
    "updated_ts": "2025-08-21T12:30:00Z"
},
{
"messages": [
"2025-08-21T12:00:00Z : Branch 'feature-e2e-tests' created in backend-core/payments-service from 'main'.",
"2025-08-21T12:00:00Z : Added 'tests/e2e/payments_flow.test.ts' to backend-core/payments-service@feature-e2e-tests.",
"2025-08-21T12:00:00Z : Initial commit added to backend-core/payments-service@feature-e2e-tests.",
"2025-08-21T12:00:00Z : Pull request #101 created for backend-core/payments-service.",
"2025-08-21T12:30:00Z : PR #101 marked APPROVE for backend-core/payments-service.",
"2025-08-21T12:30:00Z : Merged 'feature-e2e-tests' into 'main' for backend-core/payments-service with SHA merge_sha_101.",
"2025-08-21T12:30:00Z : PR #101 merged for backend-core/payments-service.",
"2025-08-21T12:30:00Z : Branch 'feature-e2e-tests' deleted from backend-core/payments-service."
]
}
]
),

Task(
annotator="0",
user_id="task_95",
instruction=(
"You are 'backend-core' with 'backend@coreservices.io' and auth key as "
"'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. close the open issue #15 in 'payments-service' "
"titled 'Timeout too aggressive': add a QA confirmation comment 'Validated 60s timeout in staging.' by 'qa-erin',"
),
actions=[
Action(name="authenticate_user", kwargs={
"username": "backend-core",
"email": "backend@coreservices.io",
"auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
}),
Action(name="add_comment_to_issue", kwargs={
"owner": "backend-core",
"repo_name": "payments-service",
"issue_number": 15,
"issue_comment": "Validated 60s timeout in staging.",
"issue_comment_user": "qa-erin"
}),
Action(name="close_issue", kwargs={
"owner": "backend-core",
"repo_name": "payments-service",
"issue_number": 15
}),
],
outputs=[
{
    "success": "Issue #15 closed for backend-core/payments-service.",
    "repo": "backend-core/payments-service",
    "issue_number": 15,
    "state": "closed",
    "updated_ts": "2025-08-21T12:30:00Z"
}
]
),
Task(
    annotator="0",
    user_id="task_96",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' ends up with "
        "a new document at 'docs/RELEASE_NOTES_1.1.0.md' whose contents are exactly '## 1.1.0 - Minor fixes - Docs update'. "
        "This change must originate from the line named 'release-notes-1.1.0', be authored by 'alice-w', and be introduced via a pull request titled 'Docs: Release notes 1.1.0' with body "
        "'Add release notes for version 1.1.0.' The pull request must be reviewed by 'john'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "alice-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="create_new_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "file_name": "docs/RELEASE_NOTES_1.1.0.md", "file_content": "## 1.1.0 - Minor fixes - Docs update"}),
        Action(name="initial_commit", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "commit_message": "Add docs/RELEASE_NOTES_1.1.0.md", "commit_author": "alice-w"}),
        Action(name="create_pull_request", kwargs={
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "pr_title": "Docs: Release notes 1.1.0",
            "pr_body": "Add release notes for version 1.1.0.",
            "head_branch_name": "release-notes-1.1.0",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/RELEASE_NOTES_1.1.0.md"]
        }),
        Action(name="assign_pull_request_reviewers", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101, "reviewers": ["john"]}),
        Action(name="approve_pr", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "source_branch_name": "release-notes-1.1.0", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "alice-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0"}),
        Action(
                name="list_all_terminal_message",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'release-notes-1.1.0' created in alice-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/RELEASE_NOTES_1.1.0.md' to alice-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Initial commit added to alice-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Pull request #101 created for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #101 for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'release-notes-1.1.0' into 'main' for alice-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for alice-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'release-notes-1.1.0' deleted from alice-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_97",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co and auth key as 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'."
        " Your mission is for the repository 'ui-kit' to end in a state where its default branch 'main' contains the component file 'packages/alert/index.tsx' with"
        " contents exactly 'export const Alert = () => <div role='alert' />'. The change must originate on the branch 'feature-alert',"
        " be authored by 'ui-team' with the commit message 'Add packages/alert/index.tsx', and be represented by a pull request titled 'Add Alert component' with body 'Introduce basic Alert component.'"
        " from 'feature-alert' to 'main' and approving the pr."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={"username": "ui-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="create_new_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "base_branch": "main"}),
        Action(name="add_new_file_in_repo", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "file_name": "packages/alert/index.tsx", "file_content": "export const Alert = () => <div role='alert' />"}),
        Action(name="initial_commit", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "commit_message": "Add packages/alert/index.tsx", "commit_author": "ui-team"}),
        Action(name="create_pull_request", kwargs={
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "pr_title": "Add Alert component",
            "pr_body": "Introduce basic Alert component.",
            "head_branch_name": "feature-alert",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["packages/alert/index.tsx"]
        }),
        Action(name="approve_pr", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="merge_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "source_branch_name": "feature-alert", "target_branch_name": "main"}),
        Action(name="mark_pr_as_merged", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="delete_branch", kwargs={"owner": "ui-team", "repo_name": "ui-kit", "branch_name": "feature-alert"}),
        Action(name="list_all_terminal_message", kwargs={}),
    ],
    outputs=[
        {
            "success": "Branch 'feature-alert' deleted from ui-team/ui-kit.",
            "repo": "ui-team/ui-kit",
            "deleted_branch": "feature-alert",
            "removed_file_count": 11,
            "remaining_branches": [
            "main",
            "release-1.0",
            "feature-theme"
            ]
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-alert' created in ui-team/ui-kit from 'main'.",
            "2025-08-21T12:00:00Z : Added 'packages/alert/index.tsx' to ui-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Initial commit added to ui-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Pull request #101 created for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : Merged 'feature-alert' into 'main' for ui-team/ui-kit with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for ui-team/ui-kit.",
            "2025-08-21T12:30:00Z : Branch 'feature-alert' deleted from ui-team/ui-kit."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_99",
    instruction=(
        "You are 'alice-w' with 'alice.w@acme.dev' and auth key as "
        "'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' ends up with "
        "an open code scanning alert recorded at ref 'refs/heads/main' having severity 'high' and description "
        "'SQL injection risk detected in src/db.py (user input concatenation).'. The alert must remain open and be "
        "retrievable by its details after creation."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "alice-w", "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="create_code_scanning_alert", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp",
            "severity": "high",
            "description": "SQL injection risk detected in src/db.py (user input concatenation).",
            "ref": "refs/heads/main"
        }),
        Action(name="get_alert_details", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp",
            "alert_number": 101
        }),
        Action(name="list_open_alerts_for_repo", kwargs={
            "owner": "alice-w", "repo_name": "acme-webapp"
        }),
    ],
    outputs=[
        {
            "owner": "alice-w",
            "repo_name": "acme-webapp",
            "count": 2,
            "alerts": [
            {
                "number": 9,
                "severity": "high",
                "state": "open",
                "description": "SQL injection vulnerability in user input handling",
                "ref": "refs/heads/main",
                "created_ts": "2023-12-02T14:30:00Z",
                "dismissed_ts": None
            },
            {
                "number": 101,
                "severity": "high",
                "state": "open",
                "description": "SQL injection risk detected in src/db.py (user input concatenation).",
                "ref": "refs/heads/main",
                "created_ts": "2025-08-21T12:00:00Z",
                "dismissed_ts": None
            }
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_100",
    instruction=(
        "You are 'ui-team' with 'team@uidesign.co' and auth key as "
        "'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your task is to ensure the repository 'ui-kit' ends with a code "
        "scanning alert initially recorded at ref 'refs/heads/main' having severity 'medium' and description "
        "'Unsafe innerHTML assignment detected in packages/card/index.tsx.' which is then dismissed with reason "
        "'false_positive'."
    ),
    actions=[
        Action(name="authenticate_user", kwargs={
            "username": "ui-team", "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="create_code_scanning_alert", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit",
            "severity": "medium",
            "description": "Unsafe innerHTML assignment detected in packages/card/index.tsx.",
            "ref": "refs/heads/main"
        }),
        Action(name="get_alert_details", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit",
            "alert_number": 101
        }),
        Action(name="dismiss_alert", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit",
            "alert_number": 101,
            "dismiss_reason": "false_positive"
        }),
        # Action(name="list_open_alerts_for_repo", kwargs={
        #     "owner": "ui-team", "repo_name": "ui-kit"
        # }),
        Action(name="get_alert_details", kwargs={
            "owner": "ui-team", "repo_name": "ui-kit",
            "alert_number": 101
        }),
    ],
    outputs=[
        {
            "owner": "ui-team",
            "repo_name": "ui-kit",
            "number": 101,
            "severity": "medium",
            "state": "dismissed",
            "description": "Unsafe innerHTML assignment detected in packages/card/index.tsx.",
            "ref": "refs/heads/main",
            "created_ts": "2025-08-21T12:00:00Z",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        }
    ]
),








]


            # Action(
            #     name="authenticate_user",
            #     kwargs={"username":"alice-w", "email":"alice.w@acme.dev", "auth_key":"ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"},
            # ),
            # Action(
            #     name="get_repo_info_for_owner",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp"},
            # ),
            # Action(
            #     name="get_branch_content",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp","branch_name":"feature-update"},
            # ),
            # Action(
            #     name="delete_repository",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp"},
            # ),
            # Action(
            #     name="create_repository",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "private_flag":False, "auto_init_flag":True},
            # ),
            # Action(
            #     name="create_new_branch",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "branch_name":"feature-update2","base_branch":"feature-update"},
            # ),
            # Action(
            #     name="add_new_file_in_repo",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "branch_name":"feature-update2","file_name":"docs/CHANGEaszdfaLOG.md", "file_content":"asfasgagasdaaf"},
            # ),
            # Action(
            #     name="update_file_in_repo",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "branch_name":"feature-update2","file_name":"docs/CHANGEaszdfaLOG.md", "file_content":"asfasgagasdaaf9137912"},
            # ),
            # Action(
            #     name="delete_file_in_repo",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "branch_name":"feature-update2","file_name":"docs/CHANGEaszdfaLOG.md"},
            # ),
            # Action(
            #     name="create_new_branch",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "branch_name":"feature-update2","base_branch":"feature-update"},
            # ),
            # Action(
            #     name="initial_commit",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "branch_name":"feature-update2", "commit_message":"Initial commit", "commit_author":"alice-w"},
            # ),
            # Action(
            #     name="make_commit",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "branch_name":"feature-update2", "commit_message":"second  commit", "commit_author":"alice-w"},
            # ),
            # Action(
            #     name="create_pull_request",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "pr_title":"InitPR", "pr_body":"Initial PR", "head_branch_name":"feature-update2", "base_branch_name":"feature-update", "head_sha":"commit_sha_13", "pr_files":["docs/CHANGEaszdfaLOG.md"]},
            # ),
            # Action(
            #     name="assign_pull_request_reviewers",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "pr_number":101, "reviewers":["john"]},
            # ),
            # Action(
            #     name="add_pull_request_comment",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "pr_number":101, "comment":"Nice Job", "comment_user":"john", "review_state":"COMMENT"},
            # ),
            # Action(
            #     name="add_pull_request_comment",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "pr_number":101, "comment":"Maybe need some changes", "comment_user":"john", "review_state":"REQUEST_CHANGE"},
            # ),
            # Action(
            #     name="approve_pr",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "pr_number":101},
            # ),
            
            # Action(
            #     name="list_of_pr_for_repo",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp"},
            # ),
            
            # Action(
            #     name="merge_branch",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "source_branch_name":"feature-update2", "target_branch_name":"feature-update"},
            # ),
            
            # Action(
            #     name="merge_pull_request",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "pr_number":101},
            # ),
            # Action(
            #     name="mark_pr_as_merged",
            #     kwargs={"owner": "ui-team", "repo_name": "ui-kit", "pr_number": 11}
            # ),
            # Action(
            #     name="get_pr_details",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "pr_number":101},
            # ),
            # Action(
            #     name="delete_branch",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp", "branch_name":"feature-update2"},
            # ),
            # Action(
            #     name="create_new_issue",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp","title":"fix UI","body":"Webpage not working","labels":["bug-fix"],"assignees":["frontend team","backend team"]},
            # ),
            # Action(
            #     name="add_comment_to_issue",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp","issue_number":101, "issue_comment":"Fixed backend", "issue_comment_user":"backend team"},
            # ),
            
            # Action(
            #     name="add_comment_to_issue",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp","issue_number":101, "issue_comment":"Fixed UI", "issue_comment_user":"frontend team"},
            # ),
            # Action(
            #     name="close_issue",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp","issue_number":101},
            # ),
            # Action(
            #     name="get_all_issues_for_repo",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp"},
            # ),
            # Action(
            #     name="create_code_scanning_alert",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp","severity":"low", "description":"some bug", "ref":"refs/heads/main"},
            # ),
            # Action(
            #     name="get_alert_details",
            #     kwargs={"owner":"alice-w", "repo_name":"acme-webapp","alert_number":101},
            # ),
            # Action(
            #     name="list_open_alerts_for_repo",
            #     kwargs={"owner":"ui-team", "repo_name":"ui-kit"},
            # ),
            # Action(
            #     name="dismiss_alert",
            #     kwargs={"owner":"ui-team", "repo_name":"ui-kit","alert_number":2},
            # ),
            # Action(
            #     name="list_open_alerts_for_repo",
            #     kwargs={"owner":"ui-team", "repo_name":"ui-kit"},
            # ),
            # Action(
            #     name="list_all_terminal_message",
            #     kwargs={},
            # ),