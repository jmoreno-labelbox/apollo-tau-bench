from domains.dto import Action, Task

TASKS = [
    Task(
    annotator="0",
    user_id="task_44",
    instruction=(
        "As 'maya-w' with 'alice.w@acme.dev' and authorized under 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', your assignment is to introduce contribution guidance to 'acme-webapp' by creating a new file 'CONTRIBUTING.md' with exactly the content 'Please follow Conventional Commits.' crafted by 'maya-w' on the 'feature-branch'. This should be suggested through a pull request titled 'Add contributing guide' with the body 'Introduce CONTRIBUTING.md' and subsequently merged."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "file_name": "CONTRIBUTING.md", "file_content": "Please follow Conventional Commits."}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "commit_message": "Add CONTRIBUTING.md", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_title": "Add contributing guide", "pr_body": "Introduce CONTRIBUTING.md", "head_branch_name": "feature-branch", "base_branch_name": "main", "head_sha": "commit_sha_101", "pr_files": ["CONTRIBUTING.md"]}),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "feature-branch", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-branch"}),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-branch' created in maya-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'CONTRIBUTING.md' to maya-w/acme-webapp@feature-branch.",
            "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@feature-branch.",
            "2025-08-21T12:00:00Z : Pull request #101 created for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'feature-branch' into 'main' for maya-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'feature-branch' deleted from maya-w/acme-webapp."
            ]
        }
    ]
),

    Task(
    annotator="0",
    user_id="task_30",
    instruction=(
        "Assume the role of 'ryan-dev' with 'bob.martinez@devstudio.com' and the authentication key 'ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i'. Your task involves ensuring that the repository 'utils-js' concludes with its default 'master' branch incorporating a new file 'docs/USAGE.md', the content of which is '# Usage Guide Run npm start to launch the app.'. Initiate this process from the 'feature-docs' branch authored by 'ryan-dev' using the commit message and PR title 'Add docs/USAGE.md', and advocate for this in a pull request containing 'Provide instructions for running the chat app.' as its body."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "ryan-dev",
            "email": "bob.martinez@devstudio.com",
            "auth_key": "ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i"
        }),
        Action(name="CreateNewBranch", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "base_branch": "master"
        }),
        Action(name="AddNewFileInRepo", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "file_name": "docs/USAGE.md",
            "file_content": "# Usage Guide Run npm start to launch the app."
        }),
        Action(name="InitialCommit", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "commit_message": "Add docs/USAGE.md",
            "commit_author": "ryan-dev"
        }),
        Action(name="CreatePullRequest", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "pr_title": "Add docs/USAGE.md",
            "pr_body": "Provide instructions for running the chat app.",
            "head_branch_name": "feature-docs",
            "base_branch_name": "master",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/USAGE.md"]
        }),
        Action(name="ApprovePr", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "pr_number": 101
        }),
        Action(name="MergeBranch", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "source_branch_name": "feature-docs",
            "target_branch_name": "master"
        }),
        Action(name="MarkPrAsMerged", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "pr_number": 101
        }),
        Action(name="DeleteBranch", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs"
        }),
        Action(name="ListAllTerminalMessage", kwargs={})
    ],
    outputs=[
        {
            "success": "PR #101 merged for ryan-dev/utils-js.",
            "repo": "ryan-dev/utils-js",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-docs' created in ryan-dev/utils-js from 'master'.",
            "2025-08-21T12:00:00Z : Added 'docs/USAGE.md' to ryan-dev/utils-js@feature-docs.",
            "2025-08-21T12:00:00Z : Initial commit added to ryan-dev/utils-js@feature-docs.",
            "2025-08-21T12:00:00Z : Pull request #101 created for ryan-dev/utils-js.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for ryan-dev/utils-js.",
            "2025-08-21T12:30:00Z : Merged 'feature-docs' into 'master' for ryan-dev/utils-js with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for ryan-dev/utils-js.",
            "2025-08-21T12:30:00Z : Branch 'feature-docs' deleted from ryan-dev/utils-js."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_31",
    instruction=(
        "Act as 'ryan-dev' with 'bob.martinez@devstudio.com' and auth key 'ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i'. Create a new feature branch named 'feature-tel-input' for 'utils-js' (base: 'master'), include 'src/utils/phone.js' with a simple script 'export const isPhone = 0;' and commit it with the message 'Add phone validator'. Subsequently, combine it back via a PR titled 'Add phone validation utility' and body 'Introduce simple phone number regex validator.'"
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "ryan-dev",
            "email": "bob.martinez@devstudio.com",
            "auth_key": "ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i"
        }),
        Action(name="CreateNewBranch", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-tel-input",
            "base_branch": "master"
        }),
        Action(name="AddNewFileInRepo", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-tel-input",
            "file_name": "src/utils/phone.js",
            "file_content": "export const isPhone = 0;"
        }),
        Action(name="InitialCommit", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-tel-input",
            "commit_message": "Add phone validator",
            "commit_author": "ryan-dev"
        }),
        Action(name="CreatePullRequest", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "pr_title": "Add phone validation utility",
            "pr_body": "Introduce simple phone number regex validator.",
            "head_branch_name": "feature-tel-input",
            "base_branch_name": "master",
            "head_sha": "commit_sha_101",
            "pr_files": ["src/utils/phone.js"]
        }),
        Action(name="ApprovePr", kwargs={
            "owner": "ryan-dev", "repo_name": "utils-js", "pr_number": 101
        }),
        Action(name="MergeBranch", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "source_branch_name": "feature-tel-input",
            "target_branch_name": "master"
        }),
        Action(name="MarkPrAsMerged", kwargs={
            "owner": "ryan-dev", "repo_name": "utils-js", "pr_number": 101
        }),
        Action(name="DeleteBranch", kwargs={
            "owner": "ryan-dev", "repo_name": "utils-js", "branch_name": "feature-tel-input"
        }),
        Action(name="ListAllTerminalMessage", kwargs={})
    ],
    outputs=[
        {
            "success": "PR #101 merged for ryan-dev/utils-js.",
            "repo": "ryan-dev/utils-js",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
                "2025-08-21T12:00:00Z : Branch 'feature-tel-input' created in ryan-dev/utils-js from 'master'.",
                "2025-08-21T12:00:00Z : Added 'src/utils/phone.js' to ryan-dev/utils-js@feature-tel-input.",
                "2025-08-21T12:00:00Z : Initial commit added to ryan-dev/utils-js@feature-tel-input.",
                "2025-08-21T12:00:00Z : Pull request #101 created for ryan-dev/utils-js.",
                "2025-08-21T12:30:00Z : PR #101 marked APPROVE for ryan-dev/utils-js.",
                "2025-08-21T12:30:00Z : Merged 'feature-tel-input' into 'master' for ryan-dev/utils-js with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : PR #101 merged for ryan-dev/utils-js.",
                "2025-08-21T12:30:00Z : Branch 'feature-tel-input' deleted from ryan-dev/utils-js."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_32",
    instruction=(
        "Operate as 'server-main' with 'backend@coreservices.io' and auth key 'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. For 'payments-service', append a diagnostic comment 'Added extra 3DS telemetry to reproduce; monitoring for failures.' to issue #13, close issue #15, and subsequently, enumerate all issues for the repository."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "server-main",
            "email": "backend@coreservices.io",
            "auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 13,
            "issue_comment": "Added extra 3DS telemetry to reproduce; monitoring for failures.",
            "issue_comment_user": "server-main"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 15
        }),
        Action(name="GetAllIssuesForRepo", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service"
        })
    ],
    outputs=[
        {
            "owner": "server-main",
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
                "server-main",
                "server-main"
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
                "server-main"
                ],
                "comments": [
                "Proposed patch incoming"
                ],
                "comment_users": [
                "server-main"
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
        "As a member of 'design-team' with the email 'team@uidesign.co' and authorization key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s', your assignment involves the 'ui-kit' repository. Address any open medium-severity code scanning alerts on 'refs/heads/main' by taking action to dismiss them."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "design-team",
            "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "severity": "medium",
            "ref": "refs/heads/main"
        }),
        Action(name="DismissAlert", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="GetAlertDetails", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "owner": "design-team",
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
            "2025-08-21T12:30:00Z : Alert #2 dismissed for design-team/ui-kit."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_35",
    instruction=(
        "As 'maya-w' utilizing the email 'alice.w@acme.dev' and the authorization key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', proceed to remove 'docs/ARCHITECTURE.md' from 'acme-webapp' on 'main'. Afterward, display the branch contents and terminal log."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "maya-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="DeleteFileInRepo", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "branch_name": "main",
            "file_name": "docs/ARCHITECTURE.md"
        }),
        Action(name="GetBranchContent", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "main"
        }),
        Action(name="ListAllTerminalMessage", kwargs={})
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
            "2025-08-21T12:30:00Z : Deleted 'docs/ARCHITECTURE.md' from maya-w/acme-webapp@main."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_22",
    instruction=(
        "Handle the task as 'design-team' with 'team@uidesign.co' and the auth key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your goal is for the repository 'ui-kit' to reach a state where its default branch 'main' includes the component file 'packages/alert/index.tsx' with the contents precisely as 'export const Alert = () => <div role='alert' />'. Begin this change on the branch 'feature-alert', ensure it's authored by 'design-team', and submit with the commit message 'Add packages/alert/index.tsx'. Present the modification via a pull request titled 'Add Alert component' with the description 'Introduce basic Alert component.'"
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="CreateNewBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "file_name": "packages/alert/index.tsx", "file_content": "export const Alert = () => <div role='alert' />"}),
        Action(name="InitialCommit", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "commit_message": "Add packages/alert/index.tsx", "commit_author": "design-team"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "pr_title": "Add Alert component",
            "pr_body": "Introduce basic Alert component.",
            "head_branch_name": "feature-alert",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["packages/alert/index.tsx"]
        }),
        Action(name="ApprovePr", kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "source_branch_name": "feature-alert", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert"}),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "success": "Branch 'feature-alert' deleted from design-team/ui-kit.",
            "repo": "design-team/ui-kit",
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
            "2025-08-21T12:00:00Z : Branch 'feature-alert' created in design-team/ui-kit from 'main'.",
            "2025-08-21T12:00:00Z : Added 'packages/alert/index.tsx' to design-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Initial commit added to design-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Pull request #101 created for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : Merged 'feature-alert' into 'main' for design-team/ui-kit with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : Branch 'feature-alert' deleted from design-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_98",
    instruction=(
        "Coordinate as 'ryan-dev' with 'bob.martinez@devstudio.com' and the auth key 'ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i'. Ensure that the repository 'utils-js' concludes with its default branch 'master' holding a new file 'docs/USAGE.md' containing the exact text '# Usage Guide Run npm start to launch the app.'. This update should initiate from the branch 'feature-docs', be recorded by 'ryan-dev' with the commit message and PR title 'Add docs/USAGE.md', and be outlined in a pull request with the body 'Provide instructions for running the chat app.'"
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "ryan-dev",
            "email": "bob.martinez@devstudio.com",
            "auth_key": "ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i"
        }),
        Action(name="CreateNewBranch", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "base_branch": "master"
        }),
        Action(name="AddNewFileInRepo", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "file_name": "docs/USAGE.md",
            "file_content": "# Usage Guide Run npm start to launch the app."
        }),
        Action(name="InitialCommit", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "commit_message": "Add docs/USAGE.md",
            "commit_author": "ryan-dev"
        }),
        Action(name="CreatePullRequest", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "pr_title": "Add docs/USAGE.md",
            "pr_body": "Provide instructions for running the chat app.",
            "head_branch_name": "feature-docs",
            "base_branch_name": "master",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/USAGE.md"]
        }),
        Action(name="ApprovePr", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "pr_number": 101
        }),
        Action(name="MergeBranch", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "source_branch_name": "feature-docs",
            "target_branch_name": "master"
        }),
        Action(name="MarkPrAsMerged", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "pr_number": 101
        }),
        Action(name="DeleteBranch", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs"
        }),
        Action(name="ListAllTerminalMessage", kwargs={})
    ],
    outputs=[
        {
            "success": "PR #101 merged for ryan-dev/utils-js.",
            "repo": "ryan-dev/utils-js",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-docs' created in ryan-dev/utils-js from 'master'.",
            "2025-08-21T12:00:00Z : Added 'docs/USAGE.md' to ryan-dev/utils-js@feature-docs.",
            "2025-08-21T12:00:00Z : Initial commit added to ryan-dev/utils-js@feature-docs.",
            "2025-08-21T12:00:00Z : Pull request #101 created for ryan-dev/utils-js.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for ryan-dev/utils-js.",
            "2025-08-21T12:30:00Z : Merged 'feature-docs' into 'master' for ryan-dev/utils-js with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for ryan-dev/utils-js.",
            "2025-08-21T12:30:00Z : Branch 'feature-docs' deleted from ryan-dev/utils-js."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_34",
    instruction=(
        "Handle the authorization and merge pull request #12 for the 'ui-kit' repository as 'design-team' with the email 'team@uidesign.co' and authentication key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "design-team",
            "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="GetPrDetails", kwargs={
            "owner": "design-team", "repo_name": "ui-kit", "pr_number": 12
        }),
        Action(name="ApprovePr", kwargs={
            "owner": "design-team", "repo_name": "ui-kit", "pr_number": 12
        }),
        Action(name="MergeBranch", kwargs={
            "owner": "design-team", "repo_name": "ui-kit",
            "source_branch_name": "release-1.0",
            "target_branch_name": "main"
        }),
        Action(name="MarkPrAsMerged", kwargs={
            "owner": "design-team", "repo_name": "ui-kit", "pr_number": 12
        }),
        Action(name="DeleteBranch", kwargs={
            "owner": "design-team", "repo_name": "ui-kit", "branch_name": "release-1.0"
        }),
        Action(name="GetRepoInfoForOwner", kwargs={
            "owner": "design-team", "repo_name": "ui-kit"
        }),
        Action(name="ListAllTerminalMessage", kwargs={})
    ],
    outputs=[
        {
            "owner": "design-team",
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
                "2025-08-21T12:30:00Z : PR #12 marked APPROVE for design-team/ui-kit.",
                "2025-08-21T12:30:00Z : Merged 'release-1.0' into 'main' for design-team/ui-kit with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : PR #12 merged for design-team/ui-kit.",
                "2025-08-21T12:30:00Z : Branch 'release-1.0' deleted from design-team/ui-kit."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_40",
    instruction=(
        "Coordinate to ensure the 'ui-kit' repository displays a new enhancement record with the title 'Add accessible Tooltip component' and the body 'Create a Tooltip that meets WCAG 2.2 with keyboard focus management.', tagged with ['enhancement', 'accessibility'], and assigned to ['design-team']. The record needs to incorporate two comments: 'Spec approved.' by 'design' and 'Implemented basic prototype.' by 'design-team'. Ensure the record concludes in the 'closed' state when all tasks are completed."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="CreateNewIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "title": "Add accessible Tooltip component",
            "body": "Create a Tooltip that meets WCAG 2.2 with keyboard focus management.",
            "labels": ["enhancement", "accessibility"],
            "assignees": ["design-team"]
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Spec approved.",
            "issue_comment_user": "design"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Implemented basic prototype.",
            "issue_comment_user": "design-team"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101
        }),
        # Action(name="GetAllIssuesForRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit"}),
        # Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for design-team/ui-kit.",
            "repo": "design-team/ui-kit",
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
        "Act as 'maya-w' using 'alice.w@acme.dev' and the authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. The goal is for the repository 'acme-webapp' to ultimately have its default branch 'main' including the file 'examples/hello.txt' with the exact content 'hello'. Begin this change from the branch 'feature-example', ensuring it is authored by 'maya-w', and commit with the message 'Add examples/hello.txt'. Proceed to merge this change via a pull request titled 'Add example' with the body 'Introduce a simple example file.'"
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "base_branch": "main"}),
        Action(
                name="GetRepoInfoForOwner",
                kwargs={"owner":"maya-w", "repo_name":"acme-webapp"},
            ),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "file_name": "examples/hello.txt", "file_content": "hello"}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "commit_message": "Add examples/hello.txt", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "pr_title": "Add example",
            "pr_body": "Introduce a simple example file.",
            "head_branch_name": "feature-example",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["examples/hello.txt"]
        }),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "feature-example", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example"}),
        Action(
                name="GetRepoInfoForOwner",
                kwargs={"owner":"maya-w", "repo_name":"acme-webapp"},
            ),
    ],
    outputs=[
        {
            "owner": "maya-w",
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
        "Operate as 'maya-w' using 'alice.w@acme.dev' and the authorization key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task involves adding a new security policy to the repository 'acme-webapp' (description: 'A sample demonstration repository') by creating a feature branch 'feature-security-policy'. This branch should introduce a file named 'SECURITY.md' at the root of the repository containing '## Security Policy. Please report vulnerabilities to security@acme.dev within 24 hours.'. Then, initiate a pull request into 'main' with the title 'Add security policy' and the body 'Introduce SECURITY.md with coordinated disclosure instructions.' for these updates."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="CreateNewBranch",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-security-policy", "base_branch": "main"}
        ),
        Action(
            name="AddNewFileInRepo",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-security-policy", "file_name": "SECURITY.md", "file_content": "## Security Policy. Please report vulnerabilities to security@acme.dev within 24 hours."}
        ),
        Action(
            name="InitialCommit",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-security-policy", "commit_message": "Add SECURITY.md", "commit_author": "maya-w"}
        ),
        Action(
            name="CreatePullRequest",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_title": "Add security policy", "pr_body": "Introduce SECURITY.md with coordinated disclosure instructions.", "head_branch_name": "feature-security-policy", "base_branch_name": "main", "head_sha": "commit_sha_101", "pr_files": ["SECURITY.md"]}
        ),
        Action(
            name="ListAllTerminalMessage",
            kwargs={}
        ),
    ],
    outputs=[
        {
            "success": "Branch 'feature-security-policy' created in maya-w/acme-webapp from 'main'.",
            "repo": "maya-w/acme-webapp",
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
            "success": "Pull request #101 created for maya-w/acme-webapp.",
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
            "2025-08-21T12:00:00Z : Branch 'feature-security-policy' created in maya-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'SECURITY.md' to maya-w/acme-webapp@feature-security-policy.",
            "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@feature-security-policy.",
            "2025-08-21T12:00:00Z : Pull request #101 created for maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_02",
    instruction=(
        "Take on the role of 'maya-w' with the email 'alice.w@acme.dev' and the authorization key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', then proceed to designate nathan for pull request#5 in the repository 'acme-webapp'. He has added a comment 'Nice Job' and has given approval for the PR."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
                name="GetPrDetails",
                kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "pr_number":5},
            ),
        Action(
            name="AssignPullRequestReviewers",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 5, "reviewers": ["nathan"]}
        ),
        Action(
            name="AddPullRequestComment",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 5, "comment": "Nice Job", "comment_user": "nathan", "review_state": "COMMENT"}
        ),
        Action(
            name="ApprovePr",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 5}
        ),
        Action(
            name="GetPrDetails",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 5}
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
                "nathan"
            ]
            ],
            "reviewers": [
            [
                "dev-sue",
                "qa-mike",
                "nathan"
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
        "Act as 'design-team' with the contact 'team@uidesign.co' and the auth key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s', then manage the process to finalize the pull request #11, previously approved and ready for merging, for the 'ui-kit' repository. This ensures the main branch reflects the sanctioned changes and tidies up the feature branch."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}
        ),
        Action(
            name="GetPrDetails",
            kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 11}
        ),
        Action(
            name="MergeBranch",
            kwargs={"owner":"design-team", "repo_name":"ui-kit", "source_branch_name":"feature-theme", "target_branch_name":"main"}
        ),
        Action(
            name="MarkPrAsMerged",
            kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 11}
        ),
        Action(
            name="DeleteBranch",
            kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-theme"}
        ),
        Action(
            name="GetRepoInfoForOwner",
            kwargs={"owner": "design-team", "repo_name": "ui-kit"}
        ),
        Action(
            name="ListAllTerminalMessage",
            kwargs={}
        ),
    ],
    outputs=[
        {
            "owner": "design-team",
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
                "2025-08-21T12:30:00Z : Merged 'feature-theme' into 'main' for design-team/ui-kit with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : PR #11 merged for design-team/ui-kit.",
                "2025-08-21T12:30:00Z : Branch 'feature-theme' deleted from design-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_04",
    instruction=(
        "Handle the task as 'design-team' using 'team@uidesign.co' and auth key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your responsibility is to address open medium-severity code scanning alerts on 'refs/heads/main' in the 'ui-kit' repository."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "design-team",
            "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "severity": "medium",
            "ref": "refs/heads/main"
        }),
        Action(name="GetAlertDetails", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="DismissAlert", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="GetAlertDetails", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "owner": "design-team",
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
            "2025-08-21T12:30:00Z : Alert #2 dismissed for design-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_05",
    instruction=(
        "Act as 'maya-w' with 'alice.w@acme.dev' and auth key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to create a CLI entry point for 'acme-webapp' on a separate branch called 'feature-add-cli'. This involves adding the file 'cli/main.py' containing \"print('Hello from CLI')\" with a commit message 'Add CLI entrypoint', authored by 'maya-w'. Ensure this update is merged into 'main', and then remove the branch."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="CreateNewBranch",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "base_branch": "main"}
        ),
        Action(
            name="AddNewFileInRepo",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "file_name": "cli/main.py", "file_content": "print('Hello from CLI')"}
        ),
        Action(
            name="InitialCommit",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "commit_message": "Add CLI entrypoint", "commit_author": "maya-w"}
        ),
        Action(
                name="MergeBranch",
                kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "source_branch_name":"feature-add-cli", "target_branch_name":"main"},
            ),
        # Action(
        #     name="markPrAsMerged",
        #     kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 11}
        # ),
        Action(
            name="DeleteBranch",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli"}
        ),
        # Action(
        #     name="createPullRequest",
        #     kwargs={
        #         "owner": "maya-w",
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
        #     name="approvePr",
        #     kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}
        # ),
        # Action(
        #     name="mergePullRequest",
        #     kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}
        # ),
        Action(
            name="GetRepoInfoForOwner",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp"}
        ),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "owner": "maya-w",
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
                "2025-08-21T12:00:00Z : Branch 'feature-add-cli' created in maya-w/acme-webapp from 'main'.",
                "2025-08-21T12:00:00Z : Added 'cli/main.py' to maya-w/acme-webapp@feature-add-cli.",
                "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@feature-add-cli.",
                "2025-08-21T12:30:00Z : Merged 'feature-add-cli' into 'main' for maya-w/acme-webapp with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : Branch 'feature-add-cli' deleted from maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_06",
    instruction=(
        "Your role is 'maya-w' with 'alice.w@acme.dev' and authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your responsibility is to incorporate contribution guidance into 'acme-webapp' by creating a new file named 'CONTRIBUTING.md' with the text 'Please follow Conventional Commits.' crafted by 'maya-w' on branch 'feature-branch'. This should be suggested through a pull request titled 'Add contributing guide' with the description 'Introduce CONTRIBUTING.md' and ensure it is merged."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "file_name": "CONTRIBUTING.md", "file_content": "Please follow Conventional Commits."}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "commit_message": "Add CONTRIBUTING.md", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_title": "Add contributing guide", "pr_body": "Introduce CONTRIBUTING.md", "head_branch_name": "feature-branch", "base_branch_name": "main", "head_sha": "commit_sha_101", "pr_files": ["CONTRIBUTING.md"]}),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "feature-branch", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-branch"}),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
                                                                      "messages": [
                                                                        "2025-08-21T12:00:00Z : Branch 'feature-branch' created in maya-w/acme-webapp from 'main'.",
                                                                        "2025-08-21T12:00:00Z : Added 'CONTRIBUTING.md' to maya-w/acme-webapp@feature-branch.",
                                                                        "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@feature-branch.",
                                                                        "2025-08-21T12:00:00Z : Pull request #101 created for maya-w/acme-webapp.",
                                                                        "2025-08-21T12:30:00Z : PR #101 marked APPROVE for maya-w/acme-webapp.",
                                                                        "2025-08-21T12:30:00Z : Merged 'feature-branch' into 'main' for maya-w/acme-webapp with SHA merge_sha_101.",
                                                                        "2025-08-21T12:30:00Z : PR #101 merged for maya-w/acme-webapp.",
                                                                        "2025-08-21T12:30:00Z : Branch 'feature-branch' deleted from maya-w/acme-webapp."
                                                                      ]
                                                                    }
    ]
),
Task(
    annotator="0",
    user_id="task_07",
    instruction=(
        "As 'maya-w' with the email 'alice.w@acme.dev' and authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', your objective is to conclude with 'acme-webapp' having its main branch 'main' feature the file 'examples/hello.txt' precisely containing 'hello'. This modification should stem from 'feature-example', be credited to 'maya-w' with the commit message 'Add examples/hello.txt', and employ a pull request named 'Add example' with the body 'Introduce a simple example file.' to integrate 'feature-example' into 'main'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "base_branch": "main"}),
        Action(
                name="GetRepoInfoForOwner",
                kwargs={"owner":"maya-w", "repo_name":"acme-webapp"},
            ),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "file_name": "examples/hello.txt", "file_content": "hello"}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "commit_message": "Add examples/hello.txt", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "pr_title": "Add example",
            "pr_body": "Introduce a simple example file.",
            "head_branch_name": "feature-example",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["examples/hello.txt"]
        }),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "feature-example", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example"}),
        Action(
                name="GetRepoInfoForOwner",
                kwargs={"owner":"maya-w", "repo_name":"acme-webapp"},
            ),
    ],
    outputs=[
        {
            "owner": "maya-w",
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
        "As 'maya-w' using the email 'alice.w@acme.dev' and authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', your task is to log a high-severity code scanning alert on the 'acme-webapp' repository with the description 'Outdated library in authentication flow' for 'refs/heads/main'. Afterward, examine the alert details, enumerate open high-severity alerts, and dismiss the newly created alert."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="CreateCodeScanningAlert",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "severity": "high", "description": "Outdated library in authentication flow", "ref": "refs/heads/main"}
        ),
        Action(
            name="GetAlertDetails",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
            name="ListOpenAlertsForRepo",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "severity": "high"}
        ),
        Action(
            name="DismissAlert",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
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
        "As 'maya-w' using the email 'alice.w@acme.dev' and authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', your task is to log a high-severity code scanning alert on the 'acme-webapp' repository with the description 'Outdated library in authentication flow' for 'refs/heads/main'. Afterward, examine the alert details, enumerate open high-severity alerts, and dismiss the newly created alert."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="CreateCodeScanningAlert",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "severity": "high", "description": "Outdated library in authentication flow", "ref": "refs/heads/main"}
        ),
        Action(
            name="GetAlertDetails",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
            name="ListOpenAlertsForRepo",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "severity": "high"}
        ),
        Action(
            name="DismissAlert",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
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
        "You are 'maya-w' with 'alice.w@acme.dev' and auth key as 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your assignment is to make certain that the repository 'acme-webapp' results in its default branch 'main' including a README with contents precisely 'Corrected README content.'. This modification needs to start from the branch entitled 'hotfix-typo', be credited to 'maya-w' with the commit note 'Fix README typo', and be presented through a pull request labeled 'Hotfix: README typo' with the description 'Correct minor README punctuation.' by approving PR"
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo", "base_branch": "main"}),
        Action(name="UpdateFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo", "file_name": "README.md", "file_content": "Corrected README content."}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo", "commit_message": "Fix README typo", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_title": "Hotfix: README typo", "pr_body": "Correct minor README punctuation.", "head_branch_name": "hotfix-typo", "base_branch_name": "main", "head_sha": "commit_sha_101", "pr_files": ["README.md"]}),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "hotfix-typo", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo"}),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "success": "PR #101 merged for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'hotfix-typo' created in maya-w/acme-webapp from 'main'.",
            "2025-08-21T12:30:00Z : Updated 'README.md' in maya-w/acme-webapp@hotfix-typo.",
            "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@hotfix-typo.",
            "2025-08-21T12:00:00Z : Pull request #101 created for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'hotfix-typo' into 'main' for maya-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'hotfix-typo' deleted from maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_11",
    instruction=(
        "You are 'maya-w' with 'alice.w@acme.dev' and auth key as 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your responsibility is to make sure the repository 'acme-webapp' results in a new document at 'docs/RELEASE_NOTES_1.1.0.md' whose contents are precisely '## 1.1.0 - Minor fixes - Docs update'. This alteration must commence from the line named 'release-notes-1.1.0', be written by 'maya-w', and be presented through a pull request entitled 'Docs: Release notes 1.1.0' with the explanation 'Add release notes for version 1.1.0.' The pull request should be reviewed by 'nathan'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "file_name": "docs/RELEASE_NOTES_1.1.0.md", "file_content": "## 1.1.0 - Minor fixes - Docs update"}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "commit_message": "Add docs/RELEASE_NOTES_1.1.0.md", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "pr_title": "Docs: Release notes 1.1.0",
            "pr_body": "Add release notes for version 1.1.0.",
            "head_branch_name": "release-notes-1.1.0",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/RELEASE_NOTES_1.1.0.md"]
        }),
        Action(name="AssignPullRequestReviewers", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101, "reviewers": ["nathan"]}),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "release-notes-1.1.0", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0"}),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'release-notes-1.1.0' created in maya-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/RELEASE_NOTES_1.1.0.md' to maya-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Pull request #101 created for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #101 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'release-notes-1.1.0' into 'main' for maya-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'release-notes-1.1.0' deleted from maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_12",
    instruction=(
        "Handle the role of 'design-team' utilizing 'team@uidesign.co and auth key as 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your objective is to ensure the repository 'ui-kit' reaches a state where its default branch 'main' possesses the component file 'packages/alert/index.tsx' with the exact content 'export const Alert = () => <div role='alert' />'. The modification must be initiated on the branch 'feature-alert', authored by 'design-team' and accompanied by the commit message 'Add packages/alert/index.tsx'. It should be encapsulated within a pull request titled 'Add Alert component' with the description 'Introduce basic Alert component.' moving from 'feature-alert' to 'main' and approved appropriately."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="CreateNewBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "file_name": "packages/alert/index.tsx", "file_content": "export const Alert = () => <div role='alert' />"}),
        Action(name="InitialCommit", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "commit_message": "Add packages/alert/index.tsx", "commit_author": "design-team"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "pr_title": "Add Alert component",
            "pr_body": "Introduce basic Alert component.",
            "head_branch_name": "feature-alert",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["packages/alert/index.tsx"]
        }),
        Action(name="ApprovePr", kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "source_branch_name": "feature-alert", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert"}),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "success": "Branch 'feature-alert' deleted from design-team/ui-kit.",
            "repo": "design-team/ui-kit",
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
            "2025-08-21T12:00:00Z : Branch 'feature-alert' created in design-team/ui-kit from 'main'.",
            "2025-08-21T12:00:00Z : Added 'packages/alert/index.tsx' to design-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Initial commit added to design-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Pull request #101 created for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : Merged 'feature-alert' into 'main' for design-team/ui-kit with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : Branch 'feature-alert' deleted from design-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_13",
    instruction=(
        "Coordinate as 'maya-w' with 'alice.w@acme.dev' and auth key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your job is to make sure the repository 'acme-webapp' displays a new bug entry titled 'Login page fails on refresh' and containing the body 'Refreshing the login page causes a 500 error on first load after deployment.' tagged with ['bug', 'high-priority'] and assigned to ['frontend team', 'backend team']. The entry must feature two comments: 'Investigated client-side cache headers.' by 'frontend team' and 'Patched session middleware.' by 'backend team'. Conclude the process by ensuring the record is in 'closed' status when finalized."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "title": "Login page fails on refresh",
            "body": "Refreshing the login page causes a 500 error on first load after deployment.",
            "labels": ["bug", "high-priority"],
            "assignees": ["frontend team", "backend team"]
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Investigated client-side cache headers.",
            "issue_comment_user": "frontend team"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Patched session middleware.",
            "issue_comment_user": "backend team"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 101
        }),
        # Action(name="GetAllIssuesForRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp"}),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Added issue #101 to existing bucket",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Issue #101 closed for maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_14",
    instruction=(
        "You are 'design-team' with 'team@uidesign.co' and auth key as 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Manage the repository 'ui-kit' so that it displays a new enhancement record with the title 'Add accessible Tooltip component' and body 'Create a Tooltip that meets WCAG 2.2 with keyboard focus management.' This should be labeled ['enhancement', 'accessibility'] and allocated to ['design-team']. The record is required to have two comments: 'Spec approved.' by 'design' and 'Implemented basic prototype.' by 'design-team'. Conclude the record with a 'closed' status once it is finalized."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="CreateNewIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "title": "Add accessible Tooltip component",
            "body": "Create a Tooltip that meets WCAG 2.2 with keyboard focus management.",
            "labels": ["enhancement", "accessibility"],
            "assignees": ["design-team"]
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Spec approved.",
            "issue_comment_user": "design"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Implemented basic prototype.",
            "issue_comment_user": "design-team"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101
        }),
        # Action(name="GetAllIssuesForRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit"}),
        # Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for design-team/ui-kit.",
            "repo": "design-team/ui-kit",
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
        "You are 'maya-w' with 'alice.w@acme.dev' and auth key as 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Coordinate the repository 'acme-webapp' so it ultimately contains an open code scanning alert registered at ref 'refs/heads/main' with severity marked as 'high' and description 'SQL injection risk detected in src/db.py (user input concatenation).'. This alert must remain open and accessible by its specifics following creation."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "maya-w", "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="CreateCodeScanningAlert", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp",
            "severity": "high",
            "description": "SQL injection risk detected in src/db.py (user input concatenation).",
            "ref": "refs/heads/main"
        }),
        Action(name="GetAlertDetails", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp",
            "alert_number": 101
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp"
        }),
    ],
    outputs=[
        {
            "owner": "maya-w",
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
        "As 'design-team' with 'team@uidesign.co' and authentication key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s', your responsibility is to verify that the 'ui-kit' repository concludes with a code scanning alert that was initially documented at ref 'refs/heads/main'. The alert should have a 'medium' severity and the description 'Unsafe innerHTML assignment detected in packages/card/index.tsx.' which must subsequently be dismissed for the reason 'false_positive'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "design-team", "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="CreateCodeScanningAlert", kwargs={
            "owner": "design-team", "repo_name": "ui-kit",
            "severity": "medium",
            "description": "Unsafe innerHTML assignment detected in packages/card/index.tsx.",
            "ref": "refs/heads/main"
        }),
        Action(name="GetAlertDetails", kwargs={
            "owner": "design-team", "repo_name": "ui-kit",
            "alert_number": 101
        }),
        Action(name="DismissAlert", kwargs={
            "owner": "design-team", "repo_name": "ui-kit",
            "alert_number": 101,
            "dismiss_reason": "false_positive"
        }),
        # Action(name="ListOpenAlertsForRepo", kwargs={
        #     "owner": "design-team", "repo_name": "ui-kit"
        # }),
        Action(name="GetAlertDetails", kwargs={
            "owner": "design-team", "repo_name": "ui-kit",
            "alert_number": 101
        }),
    ],
    outputs=[
        {
            "owner": "design-team",
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
        "As 'maya-w' with 'alice.w@acme.dev' and authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', your duty is to ensure that the 'acme-webapp' repository concludes with no open code scanning alerts after management. Initiate recording of an alert at ref 'refs/heads/feature-hardening' with a 'medium' severity and the description 'Weak hashing algorithm (md5) used in src/utils.py.'. This alert must be dismissed with the reason 'wontfix'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "maya-w", "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="CreateCodeScanningAlert", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp",
            "severity": "medium",
            "description": "Weak hashing algorithm (md5) used in src/utils.py.",
            "ref": "refs/heads/feature-hardening"
        }),
        Action(name="DismissAlert", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp",
            "alert_number": 101,
            "dismiss_reason": "wontfix"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp"
        }),
        Action(name="DismissAlert", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp",
            "alert_number": 9,
            "dismiss_reason": "wontfix"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp"
        }),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Alert #9 dismissed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
            "alert_number": 9,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "maya-w",
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
        "Act as 'maya-w' with 'alice.w@acme.dev' utilizing the auth key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to confirm that the repository 'acme-webapp' concludes with no open code scanning alerts. Ensure all alerts for 'acme-webapp' are transitioned to a non-open state by employing the dismiss reason 'wontfix', resulting in an empty final open-alerts listing."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "maya-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp"
        }),
        # Action(name="GetAlertDetails", kwargs={
        #     "owner": "maya-w",
        #     "repo_name": "acme-webapp",
        #     "alert_number": 9
        # }),
        Action(name="DismissAlert", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "alert_number": 9,
            "dismiss_reason": "wontfix"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp"
        }),
    ],
    outputs=[
        {
            "success": "Alert #9 dismissed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
            "alert_number": 9,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "maya-w",
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
        "Operate as 'design-team' with 'team@uidesign.co' using the auth key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your objective is to address every open issue in the repository 'ui-kit'. Each entry should be annotated with a remark before resolving: issue '6' add 'Icons added for email and phone.' by 'design-team'; issue '10' add 'Added ThemeProvider guide.' by 'ui-dev'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="GetAllIssuesForRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit"}),
        Action(name="AddCommentToIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 6, "issue_comment": "Icons added for email and phone.", "issue_comment_user": "design-team"}),
        Action(name="AddCommentToIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 10, "issue_comment": "Added ThemeProvider guide.", "issue_comment_user": "ui-dev"}),
        Action(name="CloseIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 6}),
        Action(name="CloseIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 10}),
        Action(name="GetAllIssuesForRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit"}),
    ],
    outputs=[
        {
            "owner": "design-team",
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
                "design-team"
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
        "Assume the identity of 'maya-w' using 'alice.w@acme.dev' with the authorization key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your goal is to culminate the repository 'acme-webapp' with a newly created branch 'feature-batch-add' that incorporates precisely four new files having the specified contents: 'docs/CONTRIBUTING.md' with 'Contribute via PRs.', 'docs/CODE_OF_CONDUCT.md' with 'Be kind.', 'examples/usage.ts' with 'export function run(){return 42}', and 'scripts/setup.sh' with '#!/usr/bin/env bash echo setup'. These modifications should be credited to 'maya-w' accompanied by the commit message 'Add 4 files'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "docs/CONTRIBUTING.md", "file_content": "Contribute via PRs."}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "docs/CODE_OF_CONDUCT.md", "file_content": "Be kind."}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "examples/usage.ts", "file_content": "export function run(){return 42}"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "scripts/setup.sh", "file_content": "#!/usr/bin/env bash echo setup"}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "commit_message": "Add 4 files", "commit_author": "maya-w"}),
        Action(
            name="ListAllTerminalMessage",
            kwargs={}
        ),
    ],
    outputs=[
        {
            "success": "Initial commit added to maya-w/acme-webapp@feature-batch-add.",
            "commit": {
            "sha": "commit_sha_101",
            "message": "Add 4 files",
            "author": "maya-w",
            "timestamp": "2025-08-21T12:00:00Z"
            },
            "branch_commit_count": 1
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-batch-add' created in maya-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/CONTRIBUTING.md' to maya-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'docs/CODE_OF_CONDUCT.md' to maya-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'examples/usage.ts' to maya-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'scripts/setup.sh' to maya-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@feature-batch-add."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_21",
    instruction=(
        "Assume the identity of 'maya-w' using 'alice.w@acme.dev' with the authorization key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your objective is to finalize the repository 'acme-webapp' with a branch 'feature-setup', initially creating the file 'docs/SETUP.md' with the content 'Install dependencies and run'. Modify this file to reflect 'Install dependencies and run. Start server', actions attributed to 'maya-w' using the respective commit messages 'Add docs/SETUP.md' and 'Update docs/SETUP.md'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "maya-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="CreateNewBranch", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "base_branch": "main"
        }),
        Action(name="AddNewFileInRepo", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "file_name": "docs/SETUP.md",
            "file_content": "Install dependencies and run"
        }),
        Action(name="InitialCommit", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "commit_message": "Add docs/SETUP.md",
            "commit_author": "maya-w"
        }),
        Action(name="UpdateFileInRepo", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "file_name": "docs/SETUP.md",
            "file_content": "Install dependencies and run. Start server"
        }),
        Action(name="MakeCommit", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "commit_message": "Update docs/SETUP.md",
            "commit_author": "maya-w"
        }),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "success": "Updated 'docs/SETUP.md' in maya-w/acme-webapp@feature-setup.",
            "repo": "maya-w/acme-webapp",
            "branch": "feature-setup",
            "file": {
            "file_name": "docs/SETUP.md",
            "previous_content": "Install dependencies and run",
            "new_content": "Install dependencies and run. Start server"
            }
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-setup' created in maya-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/SETUP.md' to maya-w/acme-webapp@feature-setup.",
            "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@feature-setup.",
            "2025-08-21T12:30:00Z : Updated 'docs/SETUP.md' in maya-w/acme-webapp@feature-setup.",
            "2025-08-21T12:30:00Z : Commit added to maya-w/acme-webapp@feature-setup."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_23",
    instruction=(
        "You are operating as 'maya-w' with the email 'alice.w@acme.dev' and the authorization key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task involves ensuring that the repository 'acme-webapp' concludes with the creation and resolution of three issues, closing each one. The issues must be precisely: ('Login button unresponsive', with body 'Clicking “Login” does nothing on Safari 16', labeled ['bug','ui'], with assignees ['frontend team']); ('Race condition in cache warmup', described as 'Concurrent warmup tasks sometimes clobber entries', carrying labels ['bug','backend'], assigned to ['backend team']); and ('Add dark mode docs', detailed as 'Document enabling dark mode in the README', tagged with ['docs','enhancement'], allocated to ['docs team'])."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "maya-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="CreateNewIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "title": "Login button unresponsive",
            "body": "Clicking “Login” does nothing on Safari 16",
            "labels": ["bug", "ui"],
            "assignees": ["frontend team"]
        }),
        Action(name="CreateNewIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "title": "Race condition in cache warmup",
            "body": "Concurrent warmup tasks sometimes clobber entries",
            "labels": ["bug", "backend"],
            "assignees": ["backend team"]
        }),
        Action(name="CreateNewIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "title": "Add dark mode docs",
            "body": "Document enabling dark mode in the README",
            "labels": ["docs", "enhancement"],
            "assignees": ["docs team"]
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 101
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 102
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 103
        }),

    ],
    outputs=[
        {
            "success": "Issue #101 closed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #102 closed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
            "issue_number": 102,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #103 closed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
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
        "Your responsibility is as 'server-main' using the email 'backend@coreservices.io' with the auth key 'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. Your objective is to ensure that the repository 'payments-service' concludes with its main branch 'main' including the exact file 'src/server.ts' which states 'This file sets the request timeout to 60 seconds.'. This update should originate from the branch 'hotfix-timeout-60s', with 'server-main' as the author and accompanied by the commit message 'Increase request timeout to 60s'. It should also be finalized through a pull request titled 'Hotfix: increase timeout' with the description 'Set request timeout to 60 seconds in server.ts' before merging the PR."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "server-main",
            "email": "backend@coreservices.io",
            "auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
        }),
        Action(name="CreateNewBranch", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "branch_name": "hotfix-timeout-60s",
            "base_branch": "main"
        }),
        Action(name="UpdateFileInRepo", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "branch_name": "hotfix-timeout-60s",
            "file_name": "src/server.ts",
            "file_content": "This file sets the request timeout to 60 seconds."
        }),
        Action(name="InitialCommit", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "branch_name": "hotfix-timeout-60s",
            "commit_message": "Increase request timeout to 60s",
            "commit_author": "server-main"
        }),
        Action(name="CreatePullRequest", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "pr_title": "Hotfix: increase timeout",
            "pr_body": "Set request timeout to 60 seconds in server.ts",
            "head_branch_name": "hotfix-timeout-60s",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["src/server.ts"]
        }),
        Action(name="ApprovePr", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "pr_number": 101
        }),
        Action(name="MergeBranch", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "source_branch_name": "hotfix-timeout-60s",
            "target_branch_name": "main"
        }),
        Action(name="MarkPrAsMerged", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "pr_number": 101
        }),
        Action(name="DeleteBranch", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "branch_name": "hotfix-timeout-60s"
        }),
        Action(
            name="ListAllTerminalMessage",
            kwargs={},
        ),
    ],
    outputs=[
        {
            "success": "PR #101 merged for server-main/payments-service.",
            "repo": "server-main/payments-service",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'hotfix-timeout-60s' created in server-main/payments-service from 'main'.",
            "2025-08-21T12:30:00Z : Updated 'src/server.ts' in server-main/payments-service@hotfix-timeout-60s.",
            "2025-08-21T12:00:00Z : Initial commit added to server-main/payments-service@hotfix-timeout-60s.",
            "2025-08-21T12:00:00Z : Pull request #101 created for server-main/payments-service.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for server-main/payments-service.",
            "2025-08-21T12:30:00Z : Merged 'hotfix-timeout-60s' into 'main' for server-main/payments-service with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for server-main/payments-service.",
            "2025-08-21T12:30:00Z : Branch 'hotfix-timeout-60s' deleted from server-main/payments-service."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_25",
    instruction=(
        "Act as 'design-team' with 'team@uidesign.co' and use the authentication key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your task involves ensuring that the repository 'ui-kit' concludes with its default branch 'main' including the file 'docs/ACCESSIBILITY.md', the contents of which must be 'This document describes accessibility guidelines for UI components.' Create a new branch named 'feature-a11y-docs', make sure 'design-team' authors it with the commit message 'Add ACCESSIBILITY.md docs', and create a pull request titled 'Add accessibility guidelines' with body 'Provide accessibility standards for all components.' Then proceed to merge it back."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "design-team",
            "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="CreateNewBranch", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "branch_name": "feature-a11y-docs",
            "base_branch": "main"
        }),
        Action(name="AddNewFileInRepo", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "branch_name": "feature-a11y-docs",
            "file_name": "docs/ACCESSIBILITY.md",
            "file_content": "This document describes accessibility guidelines for UI components."
        }),
        Action(name="InitialCommit", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "branch_name": "feature-a11y-docs",
            "commit_message": "Add ACCESSIBILITY.md docs",
            "commit_author": "design-team"
        }),
        Action(name="CreatePullRequest", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "pr_title": "Add accessibility guidelines",
            "pr_body": "Provide accessibility standards for all components.",
            "head_branch_name": "feature-a11y-docs",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/ACCESSIBILITY.md"]
        }),
        Action(name="ApprovePr", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "pr_number": 101
        }),
        Action(name="MergeBranch", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "source_branch_name": "feature-a11y-docs",
            "target_branch_name": "main"
        }),
        Action(name="MarkPrAsMerged", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "pr_number": 101
        }),
        Action(name="DeleteBranch", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "branch_name": "feature-a11y-docs"
        }),
        Action(
            name="ListAllTerminalMessage",
            kwargs={},
        ),
    ],
    outputs=[
        {
            "success": "PR #101 merged for design-team/ui-kit.",
            "repo": "design-team/ui-kit",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-a11y-docs' created in design-team/ui-kit from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/ACCESSIBILITY.md' to design-team/ui-kit@feature-a11y-docs.",
            "2025-08-21T12:00:00Z : Initial commit added to design-team/ui-kit@feature-a11y-docs.",
            "2025-08-21T12:00:00Z : Pull request #101 created for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : Merged 'feature-a11y-docs' into 'main' for design-team/ui-kit with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : Branch 'feature-a11y-docs' deleted from design-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_26",
    instruction=(
        "Operate as 'server-main' using 'backend@coreservices.io' along with the auth key 'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. Your objective is to ensure the repository 'payments-service' results in a newly created issue titled 'Database connection leak' with body 'Investigate and fix connection pool not releasing connections properly.' and labeled as 'bug'. Comments were provided by 'app-developer' and assigned to 'db-team' with the message 'Monitoring shows spikes during peak load.', after which it should be marked as resolved by closing the issue."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "server-main",
            "email": "backend@coreservices.io",
            "auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
        }),
        Action(name="CreateNewIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "title": "Database connection leak",
            "body": "Investigate and fix connection pool not releasing connections properly.",
            "labels": ["bug"],
            "assignees": ["db-team"]
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 101,
            "issue_comment": "Monitoring shows spikes during peak load.",
            "issue_comment_user": "app-developer"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 101
        }),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for server-main/payments-service.",
            "repo": "server-main/payments-service",
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
        "As 'server-main' with 'backend@coreservices.io' and the authentication key 'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h', your task is to ensure that the repository 'payments-service' concludes with three newly created issues, each labeled 'bug'. These should be titled 'Color contrast issue', 'Missing ARIA labels', and 'Keyboard navigation bug', and must include the respective bodies: 'Ensure text meets WCAG contrast standards.', 'Add ARIA labels to form fields.', and 'Fix tab order in modal dialogs.'. Add the corresponding comments 'Verified issue during accessibility testing.', 'Confirmed missing ARIA labels on signup form.', and 'Reproduced bug when navigating modals with keyboard.' from the qa-team. Finally, ensure all the issues are closed."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "server-main",
            "email": "backend@coreservices.io",
            "auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
        }),
        Action(name="CreateNewIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "title": "Color contrast issue",
            "body": "Ensure text meets WCAG contrast standards.",
            "labels": ["bug"],
            "assignees": ["qa-team"]
        }),
        Action(name="CreateNewIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "title": "Missing ARIA labels",
            "body": "Add ARIA labels to form fields.",
            "labels": ["bug"],
            "assignees": ["qa-team"]
        }),
        Action(name="CreateNewIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "title": "Keyboard navigation bug",
            "body": "Fix tab order in modal dialogs.",
            "labels": ["bug"],
            "assignees": ["qa-team"]
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 101,
            "issue_comment": "Verified issue during accessibility testing.",
            "issue_comment_user": "qa-team"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 102,
            "issue_comment": "Confirmed missing ARIA labels on signup form.",
            "issue_comment_user": "qa-team"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 103,
            "issue_comment": "Reproduced bug when navigating modals with keyboard.",
            "issue_comment_user": "qa-team"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 101
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 102
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 103
        }),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for server-main/payments-service.",
            "repo": "server-main/payments-service",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #102 closed for server-main/payments-service.",
            "repo": "server-main/payments-service",
            "issue_number": 102,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #103 closed for server-main/payments-service.",
            "repo": "server-main/payments-service",
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
        "As 'app-developer' with 'mobile@appstudio.com' and the authentication key 'ghp_mob6y7u8i9o0p1qwertyuiopasdfghjklzxcvbnm', your task is to guarantee that all open code scanning alerts in the repository 'flutter-finance-app' are dismissed. These alerts vary in severity and must be marked as dismissed, with updated timestamps accurately recorded."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "app-developer",
            "email": "mobile@appstudio.com",
            "auth_key": "ghp_mob6y7u8i9o0p1qwertyuiopasdfghjklzxcvbnm"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "app-developer",
            "repo_name": "flutter-finance-app"
        }),
        Action(name="DismissAlert", kwargs={
            "owner": "app-developer",
            "repo_name": "flutter-finance-app",
            "alert_number": 57
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "app-developer",
            "repo_name": "flutter-finance-app"
        }),
    ],
    outputs=[
        {
            "success": "Alert #57 dismissed for app-developer/flutter-finance-app.",
            "repo": "app-developer/flutter-finance-app",
            "alert_number": 57,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "app-developer",
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
        "You are 'ml-engineer' with 'ds@nlplabs.ai' and the authentication key 'ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj'. Your task is for the repository 'ml-pipeline' to conclude with a newly generated code scanning alert 'Unvalidated redirect detected in checkout flow' of medium severity on ref 'refs/heads/main', and subsequently for that alert to be marked as dismissed once it is triaged as not-exploitable."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "ml-engineer",
            "email": "ds@nlplabs.ai",
            "auth_key": "ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj"
        }),
        Action(name="CreateCodeScanningAlert", kwargs={
            "owner": "ml-engineer",
            "repo_name": "ml-pipeline",
            "severity": "medium",
            "description": "Unvalidated redirect detected in checkout flow",
            "ref": "refs/heads/main"
        }),
        # Action(name="GetAlertDetails", kwargs={
        #     "owner": "ml-engineer",
        #     "repo_name": "ml-pipeline",
        #     "alert_number": 101
        # }),
        Action(name="DismissAlert", kwargs={
            "owner": "ml-engineer",
            "repo_name": "ml-pipeline",
            "alert_number": 101,
            "dismiss_reason": "not-exploitable"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "ml-engineer",
            "repo_name": "ml-pipeline"
        }),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for ml-engineer/ml-pipeline.",
            "repo": "ml-engineer/ml-pipeline",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "ml-engineer",
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
        "You are 'security-group' with 'security@enterprise.com' and the authentication key 'ghp_sec1q2w3e4r5t6y7u8i9o0pasdfghjklzxcvbn'. Your task is for the repository 'security-scanner' to conclude with all open code scanning alerts marked as dismissed."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "security-group", "email": "security@enterprise.com", "auth_key": "ghp_sec1q2w3e4r5t6y7u8i9o0pasdfghjklzxcvbn"}
        ),
        Action(name="ListOpenAlertsForRepo", kwargs={
        "owner": "security-group",
        "repo_name": "security-scanner"
        }),
        Action(name="DismissAlert", kwargs={
        "owner": "security-group",
        "repo_name": "security-scanner",
        "alert_number": 18
        }),
        Action(name="DismissAlert", kwargs={
        "owner": "security-group",
        "repo_name": "security-scanner",
        "alert_number": 21
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
        "owner": "security-group",
        "repo_name": "security-scanner"
        }),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
    {
        "success": "Alert #18 dismissed for security-group/security-scanner.",
        "repo": "security-group/security-scanner",
        "alert_number": 18,
        "state": "dismissed",
        "dismissed_ts": "2025-08-21T12:30:00Z"
    },
    {
        "success": "Alert #21 dismissed for security-group/security-scanner.",
        "repo": "security-group/security-scanner",
        "alert_number": 21,
        "state": "dismissed",
        "dismissed_ts": "2025-08-21T12:30:00Z"
    },
    {
    "messages": [
            "2025-08-21T12:30:00Z : Alert #18 dismissed for security-group/security-scanner.",
            "2025-08-21T12:30:00Z : Alert #21 dismissed for security-group/security-scanner."
    ]
    }
    ]
),
Task(
    annotator="0",
    user_id="task_37",
    instruction=(
        "Act as 'design-team' with 'team@uidesign.co' using the auth key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Proceed to merge the current pull request #11 in the 'ui-kit' repository."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}
        ),
        Action(name="GetPrDetails", kwargs={
        "owner": "design-team",
        "repo_name": "ui-kit",
        "pr_number": 11
        }),
        Action(name="ApprovePr", kwargs={
        "owner": "design-team",
        "repo_name": "ui-kit",
        "pr_number": 11
        }),
        Action(name="MergeBranch", kwargs={
        "owner": "design-team",
        "repo_name": "ui-kit",
        "source_branch_name": "feature-theme",
        "target_branch_name": "main"
        }),
        Action(name="MarkPrAsMerged", kwargs={
        "owner": "design-team",
        "repo_name": "ui-kit",
        "pr_number": 11
        }),
        Action(name="DeleteBranch", kwargs={
        "owner": "design-team",
        "repo_name": "ui-kit",
        "branch_name": "feature-theme"
        }),
        Action(name="GetRepoInfoForOwner", kwargs={
        "owner": "design-team",
        "repo_name": "ui-kit"
        }),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
    {
        "owner": "design-team",
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
        "2025-08-21T12:30:00Z : PR #11 marked APPROVE for design-team/ui-kit.",
        "2025-08-21T12:30:00Z : Merged 'feature-theme' into 'main' for design-team/ui-kit with SHA merge_sha_101.",
        "2025-08-21T12:30:00Z : PR #11 merged for design-team/ui-kit.",
        "2025-08-21T12:30:00Z : Branch 'feature-theme' deleted from design-team/ui-kit."
    ]
    }
    ]
),
Task(
    annotator="0",
    user_id="task_38",
    instruction=(
        "Operate as 'design-team' with 'team@uidesign.co' and the auth key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Coordinate the update of the 'ui-kit' repository to show a new enhancement entry, titled 'Add accessible Tooltip component', with the body 'Create a Tooltip that meets WCAG 2.2 with keyboard focus management.' This entry should be labeled with ['enhancement', 'accessibility'] and assigned to ['design-team']. Ensure two comments are included: 'Spec approved.' by 'design' and 'Implemented basic prototype.' by 'design-team'. Make sure the entry concludes in a 'closed' state upon completion."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="CreateNewIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "title": "Add accessible Tooltip component",
            "body": "Create a Tooltip that meets WCAG 2.2 with keyboard focus management.",
            "labels": ["enhancement", "accessibility"],
            "assignees": ["design-team"]
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Spec approved.",
            "issue_comment_user": "design"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Implemented basic prototype.",
            "issue_comment_user": "design-team"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101
        }),
        # Action(name="GetAllIssuesForRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit"}),
        # Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for design-team/ui-kit.",
            "repo": "design-team/ui-kit",
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
        "Assume the role of 'maya-w' using the email 'alice.w@acme.dev' and authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your objective is to ensure that the repository 'acme-webapp' culminates with its default branch 'main' having the file 'examples/hello.txt' with the content 'hello'. The modification should commence on the branch 'feature-example', be committed by 'maya-w' with the message 'Add examples/hello.txt', and be integrated through a pull request titled 'Add example' with the description 'Introduce a simple example file.' transferring from 'feature-example' to 'main'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "base_branch": "main"}),
        Action(
                name="GetRepoInfoForOwner",
                kwargs={"owner":"maya-w", "repo_name":"acme-webapp"},
            ),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "file_name": "examples/hello.txt", "file_content": "hello"}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "commit_message": "Add examples/hello.txt", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "pr_title": "Add example",
            "pr_body": "Introduce a simple example file.",
            "head_branch_name": "feature-example",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["examples/hello.txt"]
        }),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "feature-example", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example"}),
        Action(
                name="GetRepoInfoForOwner",
                kwargs={"owner":"maya-w", "repo_name":"acme-webapp"},
            ),
    ],
    outputs=[
        {
            "owner": "maya-w",
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
        "Act as 'design-team' with the email 'team@uidesign.co' and authentication key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your assignment is to incorporate a new security policy into the present repository 'ui-kit' (description: 'A sample demonstration repository'). Introduce this by creating a feature branch 'feature-security-policy' which adds a file titled 'SECURITY.md' at the root of the repository containing '## Security Policy. Please report vulnerabilities to security@acme.dev within 24 hours.'. Submit a pull request into 'main' with the title 'Add security policy' and description 'Introduce SECURITY.md with coordinated disclosure instructions.' to apply this update."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}
        ),
        Action(
            name="CreateNewBranch",
            kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-security-policy", "base_branch": "main"}
        ),
        Action(
            name="AddNewFileInRepo",
            kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-security-policy", "file_name": "SECURITY.md", "file_content": "## Security Policy. Please report vulnerabilities to security@acme.dev within 24 hours."}
        ),
        Action(
            name="InitialCommit",
            kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-security-policy", "commit_message": "Add SECURITY.md", "commit_author": "design-team"}
        ),
        Action(
            name="CreatePullRequest",
            kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_title": "Add security policy", "pr_body": "Introduce SECURITY.md with coordinated disclosure instructions.", "head_branch_name": "feature-security-policy", "base_branch_name": "main", "head_sha": "commit_sha_101", "pr_files": ["SECURITY.md"]}
        ),
        Action(
            name="ListAllTerminalMessage",
            kwargs={}
        ),
    ],
    outputs=[
        {
                                                                      "success": "Pull request #101 created for design-team/ui-kit.",
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
            "2025-08-21T12:00:00Z : Branch 'feature-security-policy' created in design-team/ui-kit from 'main'.",
                                                                        "2025-08-21T12:00:00Z : Added 'SECURITY.md' to design-team/ui-kit@feature-security-policy.",
                                                                        "2025-08-21T12:00:00Z : Initial commit added to design-team/ui-kit@feature-security-policy.",
                                                                        "2025-08-21T12:00:00Z : Pull request #101 created for design-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_42",
    instruction=(
        "Assume the identity of 'maya-w' using 'alice.w@acme.dev' and the authorization key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to delegate the assignment of nathan to pull request#5 within the 'acme-webapp' repository, where he left the comment 'Nice Job' and gave his approval for the PR."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
                name="GetPrDetails",
                kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "pr_number":5},
            ),
        Action(
            name="AssignPullRequestReviewers",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 5, "reviewers": ["nathan"]}
        ),
        Action(
            name="AddPullRequestComment",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 5, "comment": "Nice Job", "comment_user": "nathan", "review_state": "COMMENT"}
        ),
        Action(
            name="ApprovePr",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 5}
        ),
        Action(
            name="GetPrDetails",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 5}
        ),
        Action(
            name="ListAllTerminalMessage",
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
                "nathan"
            ]
            ],
            "reviewers": [
            [
                "dev-sue",
                "qa-mike",
                "nathan"
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
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #5 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Comment added to PR #5 for maya-w/acme-webapp; review state/event appended.",
            "2025-08-21T12:30:00Z : PR #5 marked APPROVE for maya-w/acme-webapp."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_43",
    instruction=(
        "Assume the identity of 'maya-w' using 'alice.w@acme.dev' and the authorization key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task involves creating a CLI entry point in 'acme-webapp' by establishing an isolated branch titled 'feature-add-cli'. Introduce the file 'cli/main.py' containing the line \"print('Hello from CLI')\" and commit this with the message 'Add CLI entrypoint', authored by 'maya-w'. Ensure these modifications are merged into 'main' and subsequently that the branch is deleted."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="CreateNewBranch",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "base_branch": "main"}
        ),
        Action(
            name="AddNewFileInRepo",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "file_name": "cli/main.py", "file_content": "print('Hello from CLI')"}
        ),
        Action(
            name="InitialCommit",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "commit_message": "Add CLI entrypoint", "commit_author": "maya-w"}
        ),
        Action(
                name="MergeBranch",
                kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "source_branch_name":"feature-add-cli", "target_branch_name":"main"},
            ),
        # Action(
        #     name="markPrAsMerged",
        #     kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 11}
        # ),
        Action(
            name="DeleteBranch",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli"}
        ),

        Action(
            name="GetRepoInfoForOwner",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp"}
        ),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "owner": "maya-w",
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
                "2025-08-21T12:00:00Z : Branch 'feature-add-cli' created in maya-w/acme-webapp from 'main'.",
                "2025-08-21T12:00:00Z : Added 'cli/main.py' to maya-w/acme-webapp@feature-add-cli.",
                "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@feature-add-cli.",
                "2025-08-21T12:30:00Z : Merged 'feature-add-cli' into 'main' for maya-w/acme-webapp with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : Branch 'feature-add-cli' deleted from maya-w/acme-webapp."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_46",
    instruction=(
        "As 'maya-w' with 'alice.w@acme.dev' and the authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', your assignment is to file a high-severity code scanning alert in the repository 'acme-webapp' by describing 'Outdated library in authentication flow' for 'refs/heads/main'. Then review the alert specifics, enumerate any open high-severity alerts, and then dismiss the newly created alert."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="CreateCodeScanningAlert",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "severity": "high", "description": "Outdated library in authentication flow", "ref": "refs/heads/main"}
        ),
        Action(
            name="GetAlertDetails",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
            name="ListOpenAlertsForRepo",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "severity": "high"}
        ),
        Action(
            name="DismissAlert",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
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
        "Operating as 'maya-w' with 'alice.w@acme.dev' and the authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', your responsibility is to ensure that the repository 'acme-webapp' receives a new document at 'docs/RELEASE_NOTES_1.1.0.md', containing exactly '## 1.1.0 - Minor fixes - Docs update'. This modification must start from the branch named 'release-notes-1.1.0', authored by 'maya-w', and be incorporated via a pull request called 'Docs: Release notes 1.1.0' with the body 'Add release notes for version 1.1.0.' The pull request needs a review from 'nathan'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "file_name": "docs/RELEASE_NOTES_1.1.0.md", "file_content": "## 1.1.0 - Minor fixes - Docs update"}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "commit_message": "Add docs/RELEASE_NOTES_1.1.0.md", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "pr_title": "Docs: Release notes 1.1.0",
            "pr_body": "Add release notes for version 1.1.0.",
            "head_branch_name": "release-notes-1.1.0",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/RELEASE_NOTES_1.1.0.md"]
        }),
        Action(name="AssignPullRequestReviewers", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101, "reviewers": ["nathan"]}),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "release-notes-1.1.0", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0"}),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'release-notes-1.1.0' created in maya-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/RELEASE_NOTES_1.1.0.md' to maya-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Pull request #101 created for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #101 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'release-notes-1.1.0' into 'main' for maya-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'release-notes-1.1.0' deleted from maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_48",
    instruction=(
        "Your role is 'design-team' with 'team@uidesign.co and use the auth key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. The objective is for the 'ui-kit' repository to conclude with its default branch 'main' including the component file 'packages/alert/index.tsx' precisely containing 'export const Alert = () => <div role='alert' />'. Changes must emerge from the 'feature-alert' branch, drafted by 'design-team' featuring the commit message 'Add packages/alert/index.tsx', and displayed by a pull request titled 'Add Alert component' with the description 'Introduce basic Alert component.' from 'feature-alert' to 'main', and subsequently approving the pr."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="CreateNewBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "file_name": "packages/alert/index.tsx", "file_content": "export const Alert = () => <div role='alert' />"}),
        Action(name="InitialCommit", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "commit_message": "Add packages/alert/index.tsx", "commit_author": "design-team"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "pr_title": "Add Alert component",
            "pr_body": "Introduce basic Alert component.",
            "head_branch_name": "feature-alert",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["packages/alert/index.tsx"]
        }),
        Action(name="ApprovePr", kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "source_branch_name": "feature-alert", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert"}),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "success": "Branch 'feature-alert' deleted from design-team/ui-kit.",
            "repo": "design-team/ui-kit",
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
            "2025-08-21T12:00:00Z : Branch 'feature-alert' created in design-team/ui-kit from 'main'.",
            "2025-08-21T12:00:00Z : Added 'packages/alert/index.tsx' to design-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Initial commit added to design-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Pull request #101 created for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : Merged 'feature-alert' into 'main' for design-team/ui-kit with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : Branch 'feature-alert' deleted from design-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_49",
    instruction=(
        "Assigned to you, 'maya-w' with 'alice.w@acme.dev', and holding the auth key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', is the task to confirm the 'acme-webapp' repository shows a new bug record with the title 'Login page fails on refresh' and details 'Refreshing the login page causes a 500 error on first load after deployment.' tagged with ['bug', 'high-priority'] and delegated to ['frontend team', 'backend team']. Ensure the record contains two comments: 'Investigated client-side cache headers.' by 'frontend team' and 'Patched session middleware.' by 'backend team'. Finalize the record in a 'closed' state upon completion."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "title": "Login page fails on refresh",
            "body": "Refreshing the login page causes a 500 error on first load after deployment.",
            "labels": ["bug", "high-priority"],
            "assignees": ["frontend team", "backend team"]
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Investigated client-side cache headers.",
            "issue_comment_user": "frontend team"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Patched session middleware.",
            "issue_comment_user": "backend team"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 101
        }),
        # Action(name="GetAllIssuesForRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp"}),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Added issue #101 to existing bucket",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Issue #101 closed for maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_50",
    instruction=(
        "As 'design-team' using 'team@uidesign.co' and authentication key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s', your responsibility is to make sure the 'ui-kit' repository receives a new enhancement entry titled 'Add accessible Tooltip component' with the content 'Create a Tooltip that meets WCAG 2.2 with keyboard focus management.' tagged as ['enhancement', 'accessibility'] and assigned to ['design-team']. Ensure the entry includes two notes: 'Spec approved.' from 'design' and 'Implemented basic prototype.' from 'design-team'. The entry should conclude with the status 'closed' upon completion."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="CreateNewIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "title": "Add accessible Tooltip component",
            "body": "Create a Tooltip that meets WCAG 2.2 with keyboard focus management.",
            "labels": ["enhancement", "accessibility"],
            "assignees": ["design-team"]
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Spec approved.",
            "issue_comment_user": "design"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Implemented basic prototype.",
            "issue_comment_user": "design-team"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101
        }),
        # Action(name="GetAllIssuesForRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit"}),
        # Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for design-team/ui-kit.",
            "repo": "design-team/ui-kit",
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
        "Act as 'server-main' with 'backend@coreservices.io' and the authorization key 'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. Your task is to introduce three new issues in the 'payments-service' repository, each marked with the label 'bug'. The issues should be titled 'Color contrast issue', 'Missing ARIA labels', and 'Keyboard navigation bug', accompanied by descriptions 'Ensure text meets WCAG contrast standards.', 'Add ARIA labels to form fields.', and 'Fix tab order in modal dialogs.' Add comments for verification: 'Verified issue during accessibility testing.', 'Confirmed missing ARIA labels on signup form.', and 'Reproduced bug when navigating modals with keyboard.' from the qa-team. Ultimately, ensure the issue is marked as closed."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "server-main",
            "email": "backend@coreservices.io",
            "auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
        }),
        Action(name="CreateNewIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "title": "Color contrast issue",
            "body": "Ensure text meets WCAG contrast standards.",
            "labels": ["bug"],
            "assignees": ["qa-team"]
        }),
        Action(name="CreateNewIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "title": "Missing ARIA labels",
            "body": "Add ARIA labels to form fields.",
            "labels": ["bug"],
            "assignees": ["qa-team"]
        }),
        Action(name="CreateNewIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "title": "Keyboard navigation bug",
            "body": "Fix tab order in modal dialogs.",
            "labels": ["bug"],
            "assignees": ["qa-team"]
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 101,
            "issue_comment": "Verified issue during accessibility testing.",
            "issue_comment_user": "qa-team"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 102,
            "issue_comment": "Confirmed missing ARIA labels on signup form.",
            "issue_comment_user": "qa-team"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 103,
            "issue_comment": "Reproduced bug when navigating modals with keyboard.",
            "issue_comment_user": "qa-team"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 101
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 102
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 103
        }),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for server-main/payments-service.",
            "repo": "server-main/payments-service",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #102 closed for server-main/payments-service.",
            "repo": "server-main/payments-service",
            "issue_number": 102,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #103 closed for server-main/payments-service.",
            "repo": "server-main/payments-service",
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
        "As 'app-developer' with email 'mobile@appstudio.com' and authorization key 'ghp_mob6y7u8i9o0p1qwertyuiopasdfghjklzxcvbnm', your goal is for the 'flutter-finance-app' repository to finish with all its open code scanning alerts dismissed. The repository presently contains alerts of different severities, and each must be dismissed with updated timestamps noted."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "app-developer",
            "email": "mobile@appstudio.com",
            "auth_key": "ghp_mob6y7u8i9o0p1qwertyuiopasdfghjklzxcvbnm"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "app-developer",
            "repo_name": "flutter-finance-app"
        }),
        Action(name="DismissAlert", kwargs={
            "owner": "app-developer",
            "repo_name": "flutter-finance-app",
            "alert_number": 57
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "app-developer",
            "repo_name": "flutter-finance-app"
        }),
    ],
    outputs=[
        {
            "success": "Alert #57 dismissed for app-developer/flutter-finance-app.",
            "repo": "app-developer/flutter-finance-app",
            "alert_number": 57,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "app-developer",
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
        "As 'ml-engineer' having 'ds@nlplabs.ai' and the auth key 'ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj', your objective is for the 'ml-pipeline' repository to conclude with a newly issued code scanning alert 'Unvalidated redirect detected in checkout flow' of severity 'medium' on the reference 'refs/heads/main', and subsequently for that alert to be marked as dismissed after being assessed as not-exploitable."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "ml-engineer",
            "email": "ds@nlplabs.ai",
            "auth_key": "ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj"
        }),
        Action(name="CreateCodeScanningAlert", kwargs={
            "owner": "ml-engineer",
            "repo_name": "ml-pipeline",
            "severity": "medium",
            "description": "Unvalidated redirect detected in checkout flow",
            "ref": "refs/heads/main"
        }),
        # Action(name="GetAlertDetails", kwargs={
        #     "owner": "ml-engineer",
        #     "repo_name": "ml-pipeline",
        #     "alert_number": 101
        # }),
        Action(name="DismissAlert", kwargs={
            "owner": "ml-engineer",
            "repo_name": "ml-pipeline",
            "alert_number": 101,
            "dismiss_reason": "not-exploitable"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "ml-engineer",
            "repo_name": "ml-pipeline"
        }),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for ml-engineer/ml-pipeline.",
            "repo": "ml-engineer/ml-pipeline",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "ml-engineer",
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
        "Acting as 'security-group' with 'security@enterprise.com' and the authorization key 'ghp_sec1q2w3e4r5t6y7u8i9o0pasdfghjklzxcvbn', your task is to ensure the repository 'security-scanner' has all open code scanning alerts dismissed."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "security-group", "email": "security@enterprise.com", "auth_key": "ghp_sec1q2w3e4r5t6y7u8i9o0pasdfghjklzxcvbn"}
        ),
        Action(name="ListOpenAlertsForRepo", kwargs={
        "owner": "security-group",
        "repo_name": "security-scanner"
        }),
        Action(name="DismissAlert", kwargs={
        "owner": "security-group",
        "repo_name": "security-scanner",
        "alert_number": 18
        }),
        Action(name="DismissAlert", kwargs={
        "owner": "security-group",
        "repo_name": "security-scanner",
        "alert_number": 21
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
        "owner": "security-group",
        "repo_name": "security-scanner"
        }),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
    {
        "success": "Alert #18 dismissed for security-group/security-scanner.",
        "repo": "security-group/security-scanner",
        "alert_number": 18,
        "state": "dismissed",
        "dismissed_ts": "2025-08-21T12:30:00Z"
    },
    {
        "success": "Alert #21 dismissed for security-group/security-scanner.",
        "repo": "security-group/security-scanner",
        "alert_number": 21,
        "state": "dismissed",
        "dismissed_ts": "2025-08-21T12:30:00Z"
    },
    {
    "messages": [
            "2025-08-21T12:30:00Z : Alert #18 dismissed for security-group/security-scanner.",
            "2025-08-21T12:30:00Z : Alert #21 dismissed for security-group/security-scanner."
    ]
    }
    ]
),

Task(
    annotator="0",
    user_id="task_55",
    instruction=(
        "Operating as 'design-team' with 'team@uidesign.co' and using the authorization key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s', coordinate the merge of the existing pull request #11 in the 'ui-kit' repository."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}
        ),
        Action(name="GetPrDetails", kwargs={
        "owner": "design-team",
        "repo_name": "ui-kit",
        "pr_number": 11
        }),
        Action(name="ApprovePr", kwargs={
        "owner": "design-team",
        "repo_name": "ui-kit",
        "pr_number": 11
        }),
        Action(name="MergeBranch", kwargs={
        "owner": "design-team",
        "repo_name": "ui-kit",
        "source_branch_name": "feature-theme",
        "target_branch_name": "main"
        }),
        Action(name="MarkPrAsMerged", kwargs={
        "owner": "design-team",
        "repo_name": "ui-kit",
        "pr_number": 11
        }),
        Action(name="DeleteBranch", kwargs={
        "owner": "design-team",
        "repo_name": "ui-kit",
        "branch_name": "feature-theme"
        }),
        Action(name="GetRepoInfoForOwner", kwargs={
        "owner": "design-team",
        "repo_name": "ui-kit"
        }),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
    {
        "owner": "design-team",
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
        "2025-08-21T12:30:00Z : PR #11 marked APPROVE for design-team/ui-kit.",
        "2025-08-21T12:30:00Z : Merged 'feature-theme' into 'main' for design-team/ui-kit with SHA merge_sha_101.",
        "2025-08-21T12:30:00Z : PR #11 merged for design-team/ui-kit.",
        "2025-08-21T12:30:00Z : Branch 'feature-theme' deleted from design-team/ui-kit."
    ]
    }
    ]
),
Task(
    annotator="0",
    user_id="task_56",
    instruction=(
        "Acting as 'design-team' with the address 'team@uidesign.co' and using the authentication key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s', your assignment involves confirming that the repository 'ui-kit' ultimately has a code scanning alert initially noted at reference 'refs/heads/main' with severity 'medium' and description 'Unsafe innerHTML assignment detected in packages/card/index.tsx.' This alert should then be marked as resolved with the reason 'false_positive'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "design-team", "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="CreateCodeScanningAlert", kwargs={
            "owner": "design-team", "repo_name": "ui-kit",
            "severity": "medium",
            "description": "Unsafe innerHTML assignment detected in packages/card/index.tsx.",
            "ref": "refs/heads/main"
        }),
        Action(name="GetAlertDetails", kwargs={
            "owner": "design-team", "repo_name": "ui-kit",
            "alert_number": 101
        }),
        Action(name="DismissAlert", kwargs={
            "owner": "design-team", "repo_name": "ui-kit",
            "alert_number": 101,
            "dismiss_reason": "false_positive"
        }),
        # Action(name="ListOpenAlertsForRepo", kwargs={
        #     "owner": "design-team", "repo_name": "ui-kit"
        # }),
        Action(name="GetAlertDetails", kwargs={
            "owner": "design-team", "repo_name": "ui-kit",
            "alert_number": 101
        }),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "owner": "design-team",
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
            "2025-08-21T12:30:00Z : Alert #101 dismissed for design-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_57",
    instruction=(
        "Taking on the role of 'maya-w' with the email 'alice.w@acme.dev' and the auth key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', your task is to ensure the repository 'acme-webapp' concludes with its default branch 'main' incorporating the file 'examples/hello.txt' with the precise content 'hello'. This modification should stem from the branch 'feature-example', be created by 'maya-w', carry the commit message 'Add examples/hello.txt', and be merged using a pull request named 'Add example' with the body 'Introduce a simple example file.' from 'feature-example' to 'main'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "base_branch": "main"}),
        Action(
                name="GetRepoInfoForOwner",
                kwargs={"owner":"maya-w", "repo_name":"acme-webapp"},
            ),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "file_name": "examples/hello.txt", "file_content": "hello"}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example", "commit_message": "Add examples/hello.txt", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "pr_title": "Add example",
            "pr_body": "Introduce a simple example file.",
            "head_branch_name": "feature-example",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["examples/hello.txt"]
        }),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "feature-example", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-example"}),
        Action(
                name="GetRepoInfoForOwner",
                kwargs={"owner":"maya-w", "repo_name":"acme-webapp"},
            ),
    ],
    outputs=[
        {
            "owner": "maya-w",
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
        "Identify yourself as 'maya-w' with 'alice.w@acme.dev' and use the auth key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your responsibility is to confirm that the repository 'acme-webapp' does not have any open code scanning alerts remaining. By the end of the task, ensure all alerts for 'acme-webapp' are not in an open state by dismissing them for reason 'wontfix', and verify that the final open-alerts listing is empty."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "maya-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp"
        }),
        # Action(name="GetAlertDetails", kwargs={
        #     "owner": "maya-w",
        #     "repo_name": "acme-webapp",
        #     "alert_number": 9
        # }),
        Action(name="DismissAlert", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "alert_number": 9,
            "dismiss_reason": "wontfix"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp"
        }),
    ],
    outputs=[
        {
            "success": "Alert #9 dismissed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
            "alert_number": 9,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "maya-w",
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
        "Assume the role of 'design-team' with 'team@uidesign.co' and make use of the auth key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your objective is to resolve all open issues in the repository 'ui-kit'. Every issue must receive a comment before being closed: for issue '6', include 'Icons added for email and phone.' signed by 'design-team'; for issue '10', append 'Added ThemeProvider guide.' noted by 'ui-dev'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="GetAllIssuesForRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit"}),
        Action(name="AddCommentToIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 6, "issue_comment": "Icons added for email and phone.", "issue_comment_user": "design-team"}),
        Action(name="AddCommentToIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 10, "issue_comment": "Added ThemeProvider guide.", "issue_comment_user": "ui-dev"}),
        Action(name="CloseIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 6}),
        Action(name="CloseIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 10}),
        Action(name="GetAllIssuesForRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit"}),
    ],
    outputs=[
        {
            "owner": "design-team",
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
                "design-team"
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
        "Operating as 'maya-w' with the email 'alice.w@acme.dev' and authorization key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', coordinate the creation of a new branch 'feature-batch-add' in the 'acme-webapp' repository. Ensure that this branch includes precisely four new files, with the following contents: 'docs/CONTRIBUTING.md' -> 'Contribute via PRs.', 'docs/CODE_OF_CONDUCT.md' -> 'Be kind.', 'examples/usage.ts' -> 'export function run(){return 42}', and 'scripts/setup.sh' -> '#!/usr/bin/env bash echo setup'. These modifications should be committed under the author 'maya-w' with the message 'Add 4 files'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "docs/CONTRIBUTING.md", "file_content": "Contribute via PRs."}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "docs/CODE_OF_CONDUCT.md", "file_content": "Be kind."}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "examples/usage.ts", "file_content": "export function run(){return 42}"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "scripts/setup.sh", "file_content": "#!/usr/bin/env bash echo setup"}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "commit_message": "Add 4 files", "commit_author": "maya-w"}),
        Action(
            name="ListAllTerminalMessage",
            kwargs={}
        ),
    ],
    outputs=[
        {
            "success": "Initial commit added to maya-w/acme-webapp@feature-batch-add.",
            "commit": {
            "sha": "commit_sha_101",
            "message": "Add 4 files",
            "author": "maya-w",
            "timestamp": "2025-08-21T12:00:00Z"
            },
            "branch_commit_count": 1
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-batch-add' created in maya-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/CONTRIBUTING.md' to maya-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'docs/CODE_OF_CONDUCT.md' to maya-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'examples/usage.ts' to maya-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'scripts/setup.sh' to maya-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@feature-batch-add."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_61",
    instruction=(
        "Acting as 'ml-engineer' with the email 'ds@nlplabs.ai' and using the authorization key 'ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj', handle the task of creating a new code scanning alert for the repository 'ml-pipeline'. The alert should indicate 'Unvalidated redirect detected in checkout flow' with a 'medium' severity level on the reference 'refs/heads/main'. Once the alert has been reviewed and determined to be not-exploitable, ensure it is dismissed."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "ml-engineer",
            "email": "ds@nlplabs.ai",
            "auth_key": "ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj"
        }),
        Action(name="CreateCodeScanningAlert", kwargs={
            "owner": "ml-engineer",
            "repo_name": "ml-pipeline",
            "severity": "medium",
            "description": "Unvalidated redirect detected in checkout flow",
            "ref": "refs/heads/main"
        }),
        # Action(name="GetAlertDetails", kwargs={
        #     "owner": "ml-engineer",
        #     "repo_name": "ml-pipeline",
        #     "alert_number": 101
        # }),
        Action(name="DismissAlert", kwargs={
            "owner": "ml-engineer",
            "repo_name": "ml-pipeline",
            "alert_number": 101,
            "dismiss_reason": "not-exploitable"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "ml-engineer",
            "repo_name": "ml-pipeline"
        }),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for ml-engineer/ml-pipeline.",
            "repo": "ml-engineer/ml-pipeline",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "ml-engineer",
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
        "Act as 'ryan-dev' using 'bob.martinez@devstudio.com' and the authentication key 'ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i'. The objective is to ensure that the repository 'utils-js' concludes with its default branch 'master' having a new file 'docs/USAGE.md' with contents precisely '# Usage Guide Run npm start to launch the app.'. Initiate this update from the branch 'feature-docs', with 'ryan-dev' as the author, using the commit message and Pr title 'Add docs/USAGE.md', and submit a pull request with the body 'Provide instructions for running the chat app.'"
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "ryan-dev",
            "email": "bob.martinez@devstudio.com",
            "auth_key": "ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i"
        }),
        Action(name="CreateNewBranch", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "base_branch": "master"
        }),
        Action(name="AddNewFileInRepo", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "file_name": "docs/USAGE.md",
            "file_content": "# Usage Guide Run npm start to launch the app."
        }),
        Action(name="InitialCommit", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs",
            "commit_message": "Add docs/USAGE.md",
            "commit_author": "ryan-dev"
        }),
        Action(name="CreatePullRequest", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "pr_title": "Add docs/USAGE.md",
            "pr_body": "Provide instructions for running the chat app.",
            "head_branch_name": "feature-docs",
            "base_branch_name": "master",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/USAGE.md"]
        }),
        Action(name="ApprovePr", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "pr_number": 101
        }),
        Action(name="MergeBranch", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "source_branch_name": "feature-docs",
            "target_branch_name": "master"
        }),
        Action(name="MarkPrAsMerged", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "pr_number": 101
        }),
        Action(name="DeleteBranch", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-docs"
        }),
        Action(name="ListAllTerminalMessage", kwargs={})
    ],
    outputs=[
        {
            "success": "PR #101 merged for ryan-dev/utils-js.",
            "repo": "ryan-dev/utils-js",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-docs' created in ryan-dev/utils-js from 'master'.",
            "2025-08-21T12:00:00Z : Added 'docs/USAGE.md' to ryan-dev/utils-js@feature-docs.",
            "2025-08-21T12:00:00Z : Initial commit added to ryan-dev/utils-js@feature-docs.",
            "2025-08-21T12:00:00Z : Pull request #101 created for ryan-dev/utils-js.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for ryan-dev/utils-js.",
            "2025-08-21T12:30:00Z : Merged 'feature-docs' into 'master' for ryan-dev/utils-js with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for ryan-dev/utils-js.",
            "2025-08-21T12:30:00Z : Branch 'feature-docs' deleted from ryan-dev/utils-js."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_63",
    instruction=(
        "Function as 'maya-w' with 'alice.w@acme.dev' and authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your role is to appoint nathan to pull request#5 in the 'acme-webapp' repository, where he added the comment 'Nice Job' and granted his approval for the PR."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
                name="GetPrDetails",
                kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "pr_number":5},
            ),
        Action(
            name="AssignPullRequestReviewers",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 5, "reviewers": ["nathan"]}
        ),
        Action(
            name="AddPullRequestComment",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 5, "comment": "Nice Job", "comment_user": "nathan", "review_state": "COMMENT"}
        ),
        Action(
            name="ApprovePr",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 5}
        ),
        Action(
            name="GetPrDetails",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 5}
        ),
        Action(
            name="ListAllTerminalMessage",
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
                "nathan"
            ]
            ],
            "reviewers": [
            [
                "dev-sue",
                "qa-mike",
                "nathan"
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
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #5 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Comment added to PR #5 for maya-w/acme-webapp; review state/event appended.",
            "2025-08-21T12:30:00Z : PR #5 marked APPROVE for maya-w/acme-webapp."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_64",
    instruction=(
        "As 'server-main' with 'backend@coreservices.io' and using the auth key 'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h', for 'payments-service', insert a diagnostic comment 'Added extra 3DS telemetry to reproduce; monitoring for failures.' to issue #13, close issue #15, and then compile a list of all issues in the repository."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "server-main",
            "email": "backend@coreservices.io",
            "auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 13,
            "issue_comment": "Added extra 3DS telemetry to reproduce; monitoring for failures.",
            "issue_comment_user": "server-main"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 15
        }),
        Action(name="GetAllIssuesForRepo", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service"
        })
    ],
    outputs=[
        {
            "owner": "server-main",
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
                "server-main",
                "server-main"
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
                "server-main"
                ],
                "comments": [
                "Proposed patch incoming"
                ],
                "comment_users": [
                "server-main"
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
        "As 'maya-w' with 'alice.w@acme.dev' and the auth key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', coordinate to ensure the 'acme-webapp' repository has no open code scanning alerts remaining. Upon completion, all alerts in 'acme-webapp' should be closed or in a non-open status by dismissing them with the reason 'wontfix', resulting in an empty final open-alerts list."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "maya-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp"
        }),
        # Action(name="GetAlertDetails", kwargs={
        #     "owner": "maya-w",
        #     "repo_name": "acme-webapp",
        #     "alert_number": 9
        # }),
        Action(name="DismissAlert", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "alert_number": 9,
            "dismiss_reason": "wontfix"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp"
        }),
    ],
    outputs=[
        {
            "success": "Alert #9 dismissed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
            "alert_number": 9,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "maya-w",
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
        "Your role is as 'design-team' with 'team@uidesign.co' and the authentication key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your responsibility involves the repository 'ui-kit' to address all unresolved issues. Ensure each entry receives a note before completion: for issue '6' append 'Icons added for email and phone.' credited to 'design-team'; for issue '10' append 'Added ThemeProvider guide.' credited to 'ui-dev'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="GetAllIssuesForRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit"}),
        Action(name="AddCommentToIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 6, "issue_comment": "Icons added for email and phone.", "issue_comment_user": "design-team"}),
        Action(name="AddCommentToIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 10, "issue_comment": "Added ThemeProvider guide.", "issue_comment_user": "ui-dev"}),
        Action(name="CloseIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 6}),
        Action(name="CloseIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 10}),
        Action(name="GetAllIssuesForRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit"}),
    ],
    outputs=[
        {
            "owner": "design-team",
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
                "design-team"
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
        "Your assignment involves being 'maya-w' with 'alice.w@acme.dev' and using the authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task for the repository 'acme-webapp' concludes with creating a new branch 'feature-batch-add' which must incorporate precisely four new files with specified contents: 'docs/CONTRIBUTING.md' -> 'Contribute via PRs.', 'docs/CODE_OF_CONDUCT.md' -> 'Be kind.', 'examples/usage.ts' -> 'export function run(){return 42}', and 'scripts/setup.sh' -> '#!/usr/bin/env bash echo setup'. These alterations are to be attributed to 'maya-w' with the commit message 'Add 4 files'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "docs/CONTRIBUTING.md", "file_content": "Contribute via PRs."}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "docs/CODE_OF_CONDUCT.md", "file_content": "Be kind."}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "examples/usage.ts", "file_content": "export function run(){return 42}"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "file_name": "scripts/setup.sh", "file_content": "#!/usr/bin/env bash echo setup"}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-batch-add", "commit_message": "Add 4 files", "commit_author": "maya-w"}),
        Action(
            name="ListAllTerminalMessage",
            kwargs={}
        ),
    ],
    outputs=[
        {
            "success": "Initial commit added to maya-w/acme-webapp@feature-batch-add.",
            "commit": {
            "sha": "commit_sha_101",
            "message": "Add 4 files",
            "author": "maya-w",
            "timestamp": "2025-08-21T12:00:00Z"
            },
            "branch_commit_count": 1
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'feature-batch-add' created in maya-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/CONTRIBUTING.md' to maya-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'docs/CODE_OF_CONDUCT.md' to maya-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'examples/usage.ts' to maya-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Added 'scripts/setup.sh' to maya-w/acme-webapp@feature-batch-add.",
            "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@feature-batch-add."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_68",
    instruction=(
        "Assume the role of 'maya-w' using 'alice.w@acme.dev' and the authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your objective is for the repository 'acme-webapp' to conclude with a branch 'feature-setup', where the file 'docs/SETUP.md' contains 'Install dependencies and run', and update the file's content to 'Install dependencies and run. Start server' with authorship by 'maya-w', using the commit message 'Add docs/SETUP.md', and subsequently modified by 'maya-w' with the commit message 'Update docs/SETUP.md'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "maya-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="CreateNewBranch", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "base_branch": "main"
        }),
        Action(name="AddNewFileInRepo", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "file_name": "docs/SETUP.md",
            "file_content": "Install dependencies and run"
        }),
        Action(name="InitialCommit", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "commit_message": "Add docs/SETUP.md",
            "commit_author": "maya-w"
        }),
        Action(name="UpdateFileInRepo", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "file_name": "docs/SETUP.md",
            "file_content": "Install dependencies and run. Start server"
        }),
        Action(name="MakeCommit", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "branch_name": "feature-setup",
            "commit_message": "Update docs/SETUP.md",
            "commit_author": "maya-w"
        }),
    ],
    outputs=[
        {
            "success": "Updated 'docs/SETUP.md' in maya-w/acme-webapp@feature-setup.",
            "repo": "maya-w/acme-webapp",
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
        "Act as 'maya-w' with 'alice.w@acme.dev' and the authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your responsibility is to confirm that the repository 'acme-webapp' culminates in a new document at 'docs/RELEASE_NOTES_1.1.0.md' with contents precisely '## 1.1.0 - Minor fixes - Docs update'. This alteration must commence from the branch named 'release-notes-1.1.0', be authored by 'maya-w', and be introduced through a pull request titled 'Docs: Release notes 1.1.0' with the description 'Add release notes for version 1.1.0.' The pull request requires a review by 'nathan'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "file_name": "docs/RELEASE_NOTES_1.1.0.md", "file_content": "## 1.1.0 - Minor fixes - Docs update"}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "commit_message": "Add docs/RELEASE_NOTES_1.1.0.md", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "pr_title": "Docs: Release notes 1.1.0",
            "pr_body": "Add release notes for version 1.1.0.",
            "head_branch_name": "release-notes-1.1.0",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/RELEASE_NOTES_1.1.0.md"]
        }),
        Action(name="AssignPullRequestReviewers", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101, "reviewers": ["nathan"]}),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "release-notes-1.1.0", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0"}),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'release-notes-1.1.0' created in maya-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/RELEASE_NOTES_1.1.0.md' to maya-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Pull request #101 created for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #101 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'release-notes-1.1.0' into 'main' for maya-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'release-notes-1.1.0' deleted from maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_70",
    instruction=(
        "Act as 'maya-w' using 'alice.w@acme.dev' and the authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your objective is to make sure that for the 'acme-webapp' repository, there are exactly three issue records both created and transitioned to 'closed' status. The issues should be the following: ('Login button unresponsive', body 'Clicking “Login” does nothing on Safari 16', labels ['bug','ui'], assignees ['frontend team']); ('Race condition in cache warmup', body 'Concurrent warmup tasks sometimes clobber entries', labels ['bug','backend'], assignees ['backend team']); and ('Add dark mode docs', body 'Document enabling dark mode in the README', labels ['docs','enhancement'], assignees ['docs team'])."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "maya-w",
            "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="CreateNewIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "title": "Login button unresponsive",
            "body": "Clicking “Login” does nothing on Safari 16",
            "labels": ["bug", "ui"],
            "assignees": ["frontend team"]
        }),
        Action(name="CreateNewIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "title": "Race condition in cache warmup",
            "body": "Concurrent warmup tasks sometimes clobber entries",
            "labels": ["bug", "backend"],
            "assignees": ["backend team"]
        }),
        Action(name="CreateNewIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "title": "Add dark mode docs",
            "body": "Document enabling dark mode in the README",
            "labels": ["docs", "enhancement"],
            "assignees": ["docs team"]
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 101
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 102
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 103
        }),

    ],
    outputs=[
        {
            "success": "Issue #101 closed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
            "issue_number": 101,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #102 closed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
            "issue_number": 102,
            "state": "closed",
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "success": "Issue #103 closed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
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
        "Operate as 'maya-w' with 'alice.w@acme.dev' and the authorization key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to establish a CLI entry point for 'acme-webapp' via a separate branch named 'feature-add-cli', incorporating the file 'cli/main.py' that contains \"print('Hello from CLI')\". Use the commit message 'Add CLI entrypoint' authored by 'maya-w', and guarantee that this update is merged into 'main' while the working branch is cleaned up post-merge."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="CreateNewBranch",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "base_branch": "main"}
        ),
        Action(
            name="AddNewFileInRepo",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "file_name": "cli/main.py", "file_content": "print('Hello from CLI')"}
        ),
        Action(
            name="InitialCommit",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli", "commit_message": "Add CLI entrypoint", "commit_author": "maya-w"}
        ),
        Action(
                name="MergeBranch",
                kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "source_branch_name":"feature-add-cli", "target_branch_name":"main"},
            ),
        # Action(
        #     name="markPrAsMerged",
        #     kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 11}
        # ),
        Action(
            name="DeleteBranch",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-add-cli"}
        ),

        Action(
            name="GetRepoInfoForOwner",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp"}
        ),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "owner": "maya-w",
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
                "2025-08-21T12:00:00Z : Branch 'feature-add-cli' created in maya-w/acme-webapp from 'main'.",
                "2025-08-21T12:00:00Z : Added 'cli/main.py' to maya-w/acme-webapp@feature-add-cli.",
                "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@feature-add-cli.",
                "2025-08-21T12:30:00Z : Merged 'feature-add-cli' into 'main' for maya-w/acme-webapp with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : Branch 'feature-add-cli' deleted from maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_72",
    instruction=(
        "Assume the identity of 'maya-w' using 'alice.w@acme.dev' with the authorization key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task involves providing contribution guidance to 'acme-webapp' by creating a new file named 'CONTRIBUTING.md' containing the exact text 'Please follow Conventional Commits.' This should be authored by 'maya-w' on the 'feature-branch', and proposed through a pull request titled 'Add contributing guide' with the body 'Introduce CONTRIBUTING.md', which should then be merged back."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "file_name": "CONTRIBUTING.md", "file_content": "Please follow Conventional Commits."}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-branch", "commit_message": "Add CONTRIBUTING.md", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_title": "Add contributing guide", "pr_body": "Introduce CONTRIBUTING.md", "head_branch_name": "feature-branch", "base_branch_name": "main", "head_sha": "commit_sha_101", "pr_files": ["CONTRIBUTING.md"]}),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "feature-branch", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "feature-branch"}),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
                                                                      "messages": [
                                                                        "2025-08-21T12:00:00Z : Branch 'feature-branch' created in maya-w/acme-webapp from 'main'.",
                                                                        "2025-08-21T12:00:00Z : Added 'CONTRIBUTING.md' to maya-w/acme-webapp@feature-branch.",
                                                                        "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@feature-branch.",
                                                                        "2025-08-21T12:00:00Z : Pull request #101 created for maya-w/acme-webapp.",
                                                                        "2025-08-21T12:30:00Z : PR #101 marked APPROVE for maya-w/acme-webapp.",
                                                                        "2025-08-21T12:30:00Z : Merged 'feature-branch' into 'main' for maya-w/acme-webapp with SHA merge_sha_101.",
                                                                        "2025-08-21T12:30:00Z : PR #101 merged for maya-w/acme-webapp.",
                                                                        "2025-08-21T12:30:00Z : Branch 'feature-branch' deleted from maya-w/acme-webapp."
                                                                      ]
                                                                    }
    ]
),
Task(
    annotator="0",
    user_id="task_73",
    instruction=(
        "Act as 'ryan-dev' with the email 'bob.martinez@devstudio.com' and authorization key 'ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i'. Your objective is to develop a feature branch named 'feature-tel-input' for 'utils-js' with 'master' as the base. Add the file 'src/utils/phone.js' containing the code 'export const isPhone = 0;'. Commit this with the message 'Add phone validator', and initiate a PR titled 'Add phone validation utility' with the body 'Introduce simple phone number regex validator.', aiming for a successful merge back."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "ryan-dev",
            "email": "bob.martinez@devstudio.com",
            "auth_key": "ghp_9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i"
        }),
        Action(name="CreateNewBranch", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-tel-input",
            "base_branch": "master"
        }),
        Action(name="AddNewFileInRepo", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-tel-input",
            "file_name": "src/utils/phone.js",
            "file_content": "export const isPhone = 0;"
        }),
        Action(name="InitialCommit", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "branch_name": "feature-tel-input",
            "commit_message": "Add phone validator",
            "commit_author": "ryan-dev"
        }),
        Action(name="CreatePullRequest", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "pr_title": "Add phone validation utility",
            "pr_body": "Introduce simple phone number regex validator.",
            "head_branch_name": "feature-tel-input",
            "base_branch_name": "master",
            "head_sha": "commit_sha_101",
            "pr_files": ["src/utils/phone.js"]
        }),
        Action(name="ApprovePr", kwargs={
            "owner": "ryan-dev", "repo_name": "utils-js", "pr_number": 101
        }),
        Action(name="MergeBranch", kwargs={
            "owner": "ryan-dev",
            "repo_name": "utils-js",
            "source_branch_name": "feature-tel-input",
            "target_branch_name": "master"
        }),
        Action(name="MarkPrAsMerged", kwargs={
            "owner": "ryan-dev", "repo_name": "utils-js", "pr_number": 101
        }),
        Action(name="DeleteBranch", kwargs={
            "owner": "ryan-dev", "repo_name": "utils-js", "branch_name": "feature-tel-input"
        }),
        Action(name="ListAllTerminalMessage", kwargs={})
    ],
    outputs=[
        {
            "success": "PR #101 merged for ryan-dev/utils-js.",
            "repo": "ryan-dev/utils-js",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
                "2025-08-21T12:00:00Z : Branch 'feature-tel-input' created in ryan-dev/utils-js from 'master'.",
                "2025-08-21T12:00:00Z : Added 'src/utils/phone.js' to ryan-dev/utils-js@feature-tel-input.",
                "2025-08-21T12:00:00Z : Initial commit added to ryan-dev/utils-js@feature-tel-input.",
                "2025-08-21T12:00:00Z : Pull request #101 created for ryan-dev/utils-js.",
                "2025-08-21T12:30:00Z : PR #101 marked APPROVE for ryan-dev/utils-js.",
                "2025-08-21T12:30:00Z : Merged 'feature-tel-input' into 'master' for ryan-dev/utils-js with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : PR #101 merged for ryan-dev/utils-js.",
                "2025-08-21T12:30:00Z : Branch 'feature-tel-input' deleted from ryan-dev/utils-js."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_74",
    instruction=(
        "Act as 'maya-w' with 'alice.w@acme.dev' and authenticate using the key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your responsibility is to log a critical code scanning alert on the repository 'acme-webapp' with the description 'Outdated library in authentication flow' for 'refs/heads/main'. Examine the alert specifics, compile a list of unresolved high-severity alerts, and then dismiss the newly logged alert."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="CreateCodeScanningAlert",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "severity": "high", "description": "Outdated library in authentication flow", "ref": "refs/heads/main"}
        ),
        Action(
            name="GetAlertDetails",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
            name="ListOpenAlertsForRepo",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "severity": "high"}
        ),
        Action(
            name="DismissAlert",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
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
        "Assume the identity of 'maya-w' with 'alice.w@acme.dev' and utilize the authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your duty is to guarantee that the repository 'acme-webapp' is updated to include a new document at 'docs/RELEASE_NOTES_1.1.0.md', containing exactly '## 1.1.0 - Minor fixes - Docs update'. This modification should stem from the branch 'release-notes-1.1.0', be authored by 'maya-w', and be implemented through a pull request with the title 'Docs: Release notes 1.1.0' and the body text 'Add release notes for version 1.1.0.' Reviews must be completed by 'nathan'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "file_name": "docs/RELEASE_NOTES_1.1.0.md", "file_content": "## 1.1.0 - Minor fixes - Docs update"}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "commit_message": "Add docs/RELEASE_NOTES_1.1.0.md", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "pr_title": "Docs: Release notes 1.1.0",
            "pr_body": "Add release notes for version 1.1.0.",
            "head_branch_name": "release-notes-1.1.0",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/RELEASE_NOTES_1.1.0.md"]
        }),
        Action(name="AssignPullRequestReviewers", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101, "reviewers": ["nathan"]}),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "release-notes-1.1.0", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0"}),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'release-notes-1.1.0' created in maya-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/RELEASE_NOTES_1.1.0.md' to maya-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Pull request #101 created for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #101 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'release-notes-1.1.0' into 'main' for maya-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'release-notes-1.1.0' deleted from maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_76",
    instruction=(
        "Handle the assignment as 'design-team' with 'team@uidesign.co and auth key as 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your objective is for the repository 'ui-kit' to ultimately have its default branch 'main' containing the component file 'packages/alert/index.tsx' with the precise content 'export const Alert = () => <div role='alert' />'. The modification must be initiated on the branch 'feature-alert', committed by 'design-team' with the commit message 'Add packages/alert/index.tsx', and be encapsulated in a pull request titled 'Add Alert component' with the description 'Introduce basic Alert component.' moving from 'feature-alert' to 'main' and receiving pr approval."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="CreateNewBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "file_name": "packages/alert/index.tsx", "file_content": "export const Alert = () => <div role='alert' />"}),
        Action(name="InitialCommit", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "commit_message": "Add packages/alert/index.tsx", "commit_author": "design-team"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "pr_title": "Add Alert component",
            "pr_body": "Introduce basic Alert component.",
            "head_branch_name": "feature-alert",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["packages/alert/index.tsx"]
        }),
        Action(name="ApprovePr", kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "source_branch_name": "feature-alert", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert"}),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "success": "Branch 'feature-alert' deleted from design-team/ui-kit.",
            "repo": "design-team/ui-kit",
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
            "2025-08-21T12:00:00Z : Branch 'feature-alert' created in design-team/ui-kit from 'main'.",
            "2025-08-21T12:00:00Z : Added 'packages/alert/index.tsx' to design-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Initial commit added to design-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Pull request #101 created for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : Merged 'feature-alert' into 'main' for design-team/ui-kit with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : Branch 'feature-alert' deleted from design-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_77",
    instruction=(
        "Coordinate as 'maya-w' with 'alice.w@acme.dev' and auth key as 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your responsibility is to verify that the repository 'acme-webapp' reflects a newly added bug record with the title 'Login page fails on refresh' and the text 'Refreshing the login page causes a 500 error on first load after deployment.' marked with ['bug', 'high-priority'] and assigned to ['frontend team', 'backend team']. The record needs to have two notes: 'Investigated client-side cache headers.' by 'frontend team' and 'Patched session middleware.' by 'backend team'. The record should conclude in state 'closed' upon completion."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "title": "Login page fails on refresh",
            "body": "Refreshing the login page causes a 500 error on first load after deployment.",
            "labels": ["bug", "high-priority"],
            "assignees": ["frontend team", "backend team"]
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Investigated client-side cache headers.",
            "issue_comment_user": "frontend team"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Patched session middleware.",
            "issue_comment_user": "backend team"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 101
        }),
        # Action(name="GetAllIssuesForRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp"}),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Added issue #101 to existing bucket",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Issue #101 closed for maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_78",
    instruction=(
        "Your role is 'design-team' with 'team@uidesign.co' and the authentication key as 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. It is your duty to guarantee that the 'ui-kit' repository includes a new enhancement record titled 'Add accessible Tooltip component' and a body description of 'Create a Tooltip that meets WCAG 2.2 with keyboard focus management.' This should be labeled with ['enhancement', 'accessibility'] and assigned to ['design-team']. There must be two remarks recorded: 'Spec approved.' by 'design' and 'Implemented basic prototype.' by 'design-team'. The record should be finalized in the 'closed' state upon completion."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="CreateNewIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "title": "Add accessible Tooltip component",
            "body": "Create a Tooltip that meets WCAG 2.2 with keyboard focus management.",
            "labels": ["enhancement", "accessibility"],
            "assignees": ["design-team"]
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Spec approved.",
            "issue_comment_user": "design"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Implemented basic prototype.",
            "issue_comment_user": "design-team"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101
        }),
        # Action(name="GetAllIssuesForRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit"}),
        # Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for design-team/ui-kit.",
            "repo": "design-team/ui-kit",
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
        "As 'maya-w' with 'alice.w@acme.dev' and the authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', your task is to document and resolve a bug report by closing it within the 'acme-webapp' repository. Initiate by creating an issue titled 'Fix login redirect', with the body 'Users are redirected to /home instead of /dashboard', assigned a 'bug' label, and designated to 'frontend team' and 'backend team'. Acquire confirmation comments stating 'Backend routing updated.' and 'Frontend redirect fixed.' from both teams."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="CreateNewIssue",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "title": "Fix login redirect", "body": "Users are redirected to /home instead of /dashboard", "labels": ["bug"], "assignees": ["frontend team", "backend team"]}
        ),
        Action(
            name="AddCommentToIssue",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "issue_number": 101, "issue_comment": "Backend routing updated.", "issue_comment_user": "backend team"}
        ),
        Action(
            name="AddCommentToIssue",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "issue_number": 101, "issue_comment": "Frontend redirect fixed.", "issue_comment_user": "frontend team"}
        ),
        Action(
            name="CloseIssue",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "issue_number": 101}
        ),
        Action(
            name="GetAllIssuesForRepo",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp"}
        ),
    ],
    outputs=[
        {
            "owner": "maya-w",
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
                "maya-w",
                "perf-nathan"
                ],
                "comments": [
                "I'll look into this",
                "Agreed, we need better algorithms"
                ],
                "comment_users": [
                "maya-w",
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
                "docs-sophia"
                ],
                "comments": [
                "Working on this now",
                "Updated - please review"
                ],
                "comment_users": [
                "docs-sophia",
                "docs-sophia"
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
        "You are 'maya-w' with 'alice.w@acme.dev' and auth key as 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', and your responsibility is to register a high-severity code scanning alert on the repository 'acme-webapp' with the description 'Outdated library in authentication flow' for 'refs/heads/main', examine the alert details, enumerate open high-severity alerts, and dismiss the new alert."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="CreateCodeScanningAlert",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "severity": "high", "description": "Outdated library in authentication flow", "ref": "refs/heads/main"}
        ),
        Action(
            name="GetAlertDetails",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
            name="ListOpenAlertsForRepo",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "severity": "high"}
        ),
        Action(
            name="DismissAlert",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
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
        "You are 'maya-w' with 'alice.w@acme.dev' and auth key as 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to make sure that the repository 'acme-webapp' results in its default branch 'main' having a README with contents exactly as 'Corrected README content.'. This change must come from the branch named 'hotfix-typo', be authored by 'maya-w' with the commit message 'Fix README typo,' and be introduced via a pull request titled 'Hotfix: README typo' with the body 'Correct minor README punctuation.' by approving the PR."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo", "base_branch": "main"}),
        Action(name="UpdateFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo", "file_name": "README.md", "file_content": "Corrected README content."}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo", "commit_message": "Fix README typo", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_title": "Hotfix: README typo", "pr_body": "Correct minor README punctuation.", "head_branch_name": "hotfix-typo", "base_branch_name": "main", "head_sha": "commit_sha_101", "pr_files": ["README.md"]}),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "hotfix-typo", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "hotfix-typo"}),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "success": "PR #101 merged for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
            "pr_number": 101,
            "state": "merged",
            "merged": True,
            "mergeable": True,
            "updated_ts": "2025-08-21T12:30:00Z"
        },
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'hotfix-typo' created in maya-w/acme-webapp from 'main'.",
            "2025-08-21T12:30:00Z : Updated 'README.md' in maya-w/acme-webapp@hotfix-typo.",
            "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@hotfix-typo.",
            "2025-08-21T12:00:00Z : Pull request #101 created for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'hotfix-typo' into 'main' for maya-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'hotfix-typo' deleted from maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_82",
    instruction=(
        "Act as 'maya-w' with 'alice.w@acme.dev' and your auth key is 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your responsibility is to have the repository 'acme-webapp' achieve the state where a new document at 'docs/RELEASE_NOTES_1.1.0.md' is in place, with the exact contents '## 1.1.0 - Minor fixes - Docs update'. This alteration should derive from the line named 'release-notes-1.1.0', be created by 'maya-w', and be enacted through a pull request titled 'Docs: Release notes 1.1.0' carrying the body 'Add release notes for version 1.1.0.' It is essential for the pull request to be reviewed by 'nathan'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "file_name": "docs/RELEASE_NOTES_1.1.0.md", "file_content": "## 1.1.0 - Minor fixes - Docs update"}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "commit_message": "Add docs/RELEASE_NOTES_1.1.0.md", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "pr_title": "Docs: Release notes 1.1.0",
            "pr_body": "Add release notes for version 1.1.0.",
            "head_branch_name": "release-notes-1.1.0",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/RELEASE_NOTES_1.1.0.md"]
        }),
        Action(name="AssignPullRequestReviewers", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101, "reviewers": ["nathan"]}),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "release-notes-1.1.0", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0"}),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'release-notes-1.1.0' created in maya-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/RELEASE_NOTES_1.1.0.md' to maya-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Pull request #101 created for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #101 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'release-notes-1.1.0' into 'main' for maya-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'release-notes-1.1.0' deleted from maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_83",
    instruction=(
        "Act as 'design-team' with 'team@uidesign.co and your auth key is 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your assignment is to ensure the repository 'ui-kit' culminates in a state where its default branch 'main' features the component file 'packages/alert/index.tsx' with the exact content 'export const Alert = () => <div role='alert' />'. The modification should start from the branch 'feature-alert', be executed by 'design-team' with the commit message 'Add packages/alert/index.tsx', and be featured as a pull request titled 'Add Alert component' with the body 'Introduce basic Alert component.' transitioning from 'feature-alert' to 'main' and ensuring the pr is approved."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="CreateNewBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "file_name": "packages/alert/index.tsx", "file_content": "export const Alert = () => <div role='alert' />"}),
        Action(name="InitialCommit", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "commit_message": "Add packages/alert/index.tsx", "commit_author": "design-team"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "pr_title": "Add Alert component",
            "pr_body": "Introduce basic Alert component.",
            "head_branch_name": "feature-alert",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["packages/alert/index.tsx"]
        }),
        Action(name="ApprovePr", kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "source_branch_name": "feature-alert", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert"}),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "success": "Branch 'feature-alert' deleted from design-team/ui-kit.",
            "repo": "design-team/ui-kit",
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
            "2025-08-21T12:00:00Z : Branch 'feature-alert' created in design-team/ui-kit from 'main'.",
            "2025-08-21T12:00:00Z : Added 'packages/alert/index.tsx' to design-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Initial commit added to design-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Pull request #101 created for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : Merged 'feature-alert' into 'main' for design-team/ui-kit with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : Branch 'feature-alert' deleted from design-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_84",
    instruction=(
        "Assume the identity of 'maya-w' using 'alice.w@acme.dev' and the authorization key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your assignment entails verifying that the repository 'acme-webapp' reflects a newly added bug entry titled 'Login page fails on refresh' with the description 'Refreshing the login page causes a 500 error on first load after deployment.' The entry should be tagged with ['bug', 'high-priority'] and tasked to ['frontend team', 'backend team']. Ensure inclusion of two comments: 'Investigated client-side cache headers.' by 'frontend team' and 'Patched session middleware.' by 'backend team'. Conclude the record in a 'closed' state upon task completion."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "title": "Login page fails on refresh",
            "body": "Refreshing the login page causes a 500 error on first load after deployment.",
            "labels": ["bug", "high-priority"],
            "assignees": ["frontend team", "backend team"]
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Investigated client-side cache headers.",
            "issue_comment_user": "frontend team"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 101,
            "issue_comment": "Patched session middleware.",
            "issue_comment_user": "backend team"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "issue_number": 101
        }),
        # Action(name="GetAllIssuesForRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp"}),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Added issue #101 to existing bucket",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Comment added to issue #101 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Issue #101 closed for maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_85",
    instruction=(
        "Operate as 'design-team' using the email 'team@uidesign.co' and authorization key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your mission is to confirm the repository 'ui-kit' includes a new enhancement entry titled 'Add accessible Tooltip component' and described as 'Create a Tooltip that meets WCAG 2.2 with keyboard focus management.' It must be labeled with ['enhancement', 'accessibility'] and allocated to ['design-team']. Include two notes: 'Spec approved.' by 'design' and 'Implemented basic prototype.' by 'design-team'. Finalize the record in a 'closed' state when finished."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="CreateNewIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "title": "Add accessible Tooltip component",
            "body": "Create a Tooltip that meets WCAG 2.2 with keyboard focus management.",
            "labels": ["enhancement", "accessibility"],
            "assignees": ["design-team"]
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Spec approved.",
            "issue_comment_user": "design"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101,
            "issue_comment": "Implemented basic prototype.",
            "issue_comment_user": "design-team"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "issue_number": 101
        }),
        # Action(name="GetAllIssuesForRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit"}),
        # Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "success": "Issue #101 closed for design-team/ui-kit.",
            "repo": "design-team/ui-kit",
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
        "You are 'maya-w' with 'alice.w@acme.dev' and auth key as 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your task is to ensure the repository 'acme-webapp' ultimately has an open code scanning alert documented at ref 'refs/heads/main' with severity 'high' and the description 'SQL injection risk detected in src/db.py (user input concatenation).'. The alert must stay open and be accessible by its details after being created."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "maya-w", "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="CreateCodeScanningAlert", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp",
            "severity": "high",
            "description": "SQL injection risk detected in src/db.py (user input concatenation).",
            "ref": "refs/heads/main"
        }),
        Action(name="GetAlertDetails", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp",
            "alert_number": 101
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp"
        }),
    ],
    outputs=[
        {
            "owner": "maya-w",
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
        "You are 'ml-engineer' with 'ds@nlplabs.ai' and auth key as 'ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj'. Your mission involves the repository 'ml-pipeline' concluding with a newly issued code scanning alert 'Unvalidated redirect detected in checkout flow' with severity 'medium' on ref 'refs/heads/main', and subsequently having that alert marked as dismissed once it is determined to be not-exploitable."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "ml-engineer",
            "email": "ds@nlplabs.ai",
            "auth_key": "ghp_ds2w3e4r5t6y7u8i9o0p1qwertyuiopasdfghj"
        }),
        Action(name="CreateCodeScanningAlert", kwargs={
            "owner": "ml-engineer",
            "repo_name": "ml-pipeline",
            "severity": "medium",
            "description": "Unvalidated redirect detected in checkout flow",
            "ref": "refs/heads/main"
        }),
        # Action(name="GetAlertDetails", kwargs={
        #     "owner": "ml-engineer",
        #     "repo_name": "ml-pipeline",
        #     "alert_number": 101
        # }),
        Action(name="DismissAlert", kwargs={
            "owner": "ml-engineer",
            "repo_name": "ml-pipeline",
            "alert_number": 101,
            "dismiss_reason": "not-exploitable"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "ml-engineer",
            "repo_name": "ml-pipeline"
        }),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for ml-engineer/ml-pipeline.",
            "repo": "ml-engineer/ml-pipeline",
            "alert_number": 101,
            "state": "dismissed",
            "dismissed_ts": "2025-08-21T12:30:00Z"
        },
        {
            "owner": "ml-engineer",
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
        "As 'server-main' using 'backend@coreservices.io' with the authorization key 'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h', proceed with adding a diagnostic comment 'Added extra 3DS telemetry to reproduce; monitoring for failures.' to issue #13 within 'payments-service', and ensure closing issue #15, followed by listing all the issues for the repo."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "server-main",
            "email": "backend@coreservices.io",
            "auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
        }),
        Action(name="AddCommentToIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 13,
            "issue_comment": "Added extra 3DS telemetry to reproduce; monitoring for failures.",
            "issue_comment_user": "server-main"
        }),
        Action(name="CloseIssue", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service",
            "issue_number": 15
        }),
        Action(name="GetAllIssuesForRepo", kwargs={
            "owner": "server-main",
            "repo_name": "payments-service"
        })
    ],
    outputs=[
        {
            "owner": "server-main",
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
                "server-main",
                "server-main"
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
                "server-main"
                ],
                "comments": [
                "Proposed patch incoming"
                ],
                "comment_users": [
                "server-main"
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
        "Act as 'design-team' with the email 'team@uidesign.co' and authorization key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. The task requires you to go to the 'ui-kit' repository and dismiss all open medium-severity code scanning alerts on 'refs/heads/main'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "design-team",
            "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "severity": "medium",
            "ref": "refs/heads/main"
        }),
        Action(name="GetAlertDetails", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="DismissAlert", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="GetAlertDetails", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "alert_number": 2
        }),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "owner": "design-team",
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
            "2025-08-21T12:30:00Z : Alert #2 dismissed for design-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_90",
    instruction=(
        "As 'design-team' using 'team@uidesign.co' and the authentication key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s', handle the approval and merging of pull request #12 for the ui-kit repository."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "design-team",
            "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="GetPrDetails", kwargs={
            "owner": "design-team", "repo_name": "ui-kit", "pr_number": 12
        }),
        Action(name="ApprovePr", kwargs={
            "owner": "design-team", "repo_name": "ui-kit", "pr_number": 12
        }),
        Action(name="MergeBranch", kwargs={
            "owner": "design-team", "repo_name": "ui-kit",
            "source_branch_name": "release-1.0",
            "target_branch_name": "main"
        }),
        Action(name="MarkPrAsMerged", kwargs={
            "owner": "design-team", "repo_name": "ui-kit", "pr_number": 12
        }),
        Action(name="DeleteBranch", kwargs={
            "owner": "design-team", "repo_name": "ui-kit", "branch_name": "release-1.0"
        }),
        Action(name="GetRepoInfoForOwner", kwargs={
            "owner": "design-team", "repo_name": "ui-kit"
        }),
        Action(name="ListAllTerminalMessage", kwargs={})
    ],
    outputs=[
        {
            "owner": "design-team",
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
                "2025-08-21T12:30:00Z : PR #12 marked APPROVE for design-team/ui-kit.",
                "2025-08-21T12:30:00Z : Merged 'release-1.0' into 'main' for design-team/ui-kit with SHA merge_sha_101.",
                "2025-08-21T12:30:00Z : PR #12 merged for design-team/ui-kit.",
                "2025-08-21T12:30:00Z : Branch 'release-1.0' deleted from design-team/ui-kit."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_91",
    instruction=(
        "Operating as 'maya-w' with 'alice.w@acme.dev' and the authentication key 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r', your duty is to coordinate the registration of a high-severity code scanning alert on the 'acme-webapp' repository, detailing 'Outdated library in authentication flow' for 'refs/heads/main', examine the alert details, compile a list of open high-severity alerts, and dismiss the new alert."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}
        ),
        Action(
            name="CreateCodeScanningAlert",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "severity": "high", "description": "Outdated library in authentication flow", "ref": "refs/heads/main"}
        ),
        Action(
            name="GetAlertDetails",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
        Action(
            name="ListOpenAlertsForRepo",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "severity": "high"}
        ),
        Action(
            name="DismissAlert",
            kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "alert_number": 101}
        ),
    ],
    outputs=[
        {
            "success": "Alert #101 dismissed for maya-w/acme-webapp.",
            "repo": "maya-w/acme-webapp",
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
        "You represent 'security-group' using 'security@enterprise.com' with the authorization key 'ghp_sec1q2w3e4r5t6y7u8i9o0pasdfghjklzxcvbn'. Your objective is to ensure that the repository 'security-scanner' concludes with all open code scanning alerts being dismissed."
    ),
    actions=[
        Action(
            name="AuthenticateUser",
            kwargs={"username": "security-group", "email": "security@enterprise.com", "auth_key": "ghp_sec1q2w3e4r5t6y7u8i9o0pasdfghjklzxcvbn"}
        ),
        Action(name="ListOpenAlertsForRepo", kwargs={
        "owner": "security-group",
        "repo_name": "security-scanner"
        }),
        Action(name="DismissAlert", kwargs={
        "owner": "security-group",
        "repo_name": "security-scanner",
        "alert_number": 18
        }),
        Action(name="DismissAlert", kwargs={
        "owner": "security-group",
        "repo_name": "security-scanner",
        "alert_number": 21
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
        "owner": "security-group",
        "repo_name": "security-scanner"
        }),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
    {
        "success": "Alert #18 dismissed for security-group/security-scanner.",
        "repo": "security-group/security-scanner",
        "alert_number": 18,
        "state": "dismissed",
        "dismissed_ts": "2025-08-21T12:30:00Z"
    },
    {
        "success": "Alert #21 dismissed for security-group/security-scanner.",
        "repo": "security-group/security-scanner",
        "alert_number": 21,
        "state": "dismissed",
        "dismissed_ts": "2025-08-21T12:30:00Z"
    },
    {
    "messages": [
            "2025-08-21T12:30:00Z : Alert #18 dismissed for security-group/security-scanner.",
            "2025-08-21T12:30:00Z : Alert #21 dismissed for security-group/security-scanner."
    ]
    }
    ]
),
Task(
    annotator="0",
    user_id="task_93",
    instruction=(
        "You represent 'design-team' using 'team@uidesign.co' with the authorization key 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your objective is to address all open issues in the repository 'ui-kit'. Prior to resolving each record, a remark is necessary: issue '6' add 'Icons added for email and phone.' by 'design-team'; issue '10' add 'Added ThemeProvider guide.' by 'ui-dev'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="GetAllIssuesForRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit"}),
        Action(name="AddCommentToIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 6, "issue_comment": "Icons added for email and phone.", "issue_comment_user": "design-team"}),
        Action(name="AddCommentToIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 10, "issue_comment": "Added ThemeProvider guide.", "issue_comment_user": "ui-dev"}),
        Action(name="CloseIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 6}),
        Action(name="CloseIssue", kwargs={"owner": "design-team", "repo_name": "ui-kit", "issue_number": 10}),
        Action(name="GetAllIssuesForRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit"}),
    ],
    outputs=[
        {
            "owner": "design-team",
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
                "design-team"
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
        "You are 'server-main' with 'backend@coreservices.io' and auth key as 'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. Construct an end-to-end test scaffold in 'payments-service': create a new branch 'feature-e2e-tests' from 'main', introduce a file 'tests/e2e/payments_flow.test.ts' containing 'E2E skeleton for payments flow.', with the commit message 'Add E2E payments test skeleton' authored by 'server-main', initiate a PR titled 'Add E2E tests' (body 'Introduce payments flow E2E skeleton') from 'feature-e2e-tests' to 'main' and integrate it."
    ),
actions=[
Action(name="AuthenticateUser", kwargs={
"username": "server-main",
"email": "backend@coreservices.io",
"auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
}),
Action(name="CreateNewBranch", kwargs={
"owner": "server-main",
"repo_name": "payments-service",
"branch_name": "feature-e2e-tests",
"base_branch": "main"
}),
Action(name="AddNewFileInRepo", kwargs={
"owner": "server-main",
"repo_name": "payments-service",
"branch_name": "feature-e2e-tests",
"file_name": "tests/e2e/payments_flow.test.ts",
"file_content": "E2E skeleton for payments flow."
}),
Action(name="InitialCommit", kwargs={
"owner": "server-main",
"repo_name": "payments-service",
"branch_name": "feature-e2e-tests",
"commit_message": "Add E2E payments test skeleton",
"commit_author": "server-main"
}),
Action(name="CreatePullRequest", kwargs={
"owner": "server-main",
"repo_name": "payments-service",
"pr_title": "Add E2E tests",
"pr_body": "Introduce payments flow E2E skeleton",
"head_branch_name": "feature-e2e-tests",
"base_branch_name": "main",
"head_sha": "commit_sha_101",
"pr_files": ["tests/e2e/payments_flow.test.ts"]
}),
Action(name="ApprovePr", kwargs={
"owner": "server-main",
"repo_name": "payments-service",
"pr_number": 101
}),
Action(name="MergeBranch", kwargs={
"owner": "server-main",
"repo_name": "payments-service",
"source_branch_name": "feature-e2e-tests",
"target_branch_name": "main"
}),
Action(name="MarkPrAsMerged", kwargs={
"owner": "server-main",
"repo_name": "payments-service",
"pr_number": 101
}),
Action(name="DeleteBranch", kwargs={
"owner": "server-main",
"repo_name": "payments-service",
"branch_name": "feature-e2e-tests"
}),
Action(name="ListAllTerminalMessage", kwargs={}),
],
outputs=[
{
    "success": "PR #101 merged for server-main/payments-service.",
    "repo": "server-main/payments-service",
    "pr_number": 101,
    "state": "merged",
    "merged": True,
    "mergeable": True,
    "updated_ts": "2025-08-21T12:30:00Z"
},
{
"messages": [
"2025-08-21T12:00:00Z : Branch 'feature-e2e-tests' created in server-main/payments-service from 'main'.",
"2025-08-21T12:00:00Z : Added 'tests/e2e/payments_flow.test.ts' to server-main/payments-service@feature-e2e-tests.",
"2025-08-21T12:00:00Z : Initial commit added to server-main/payments-service@feature-e2e-tests.",
"2025-08-21T12:00:00Z : Pull request #101 created for server-main/payments-service.",
"2025-08-21T12:30:00Z : PR #101 marked APPROVE for server-main/payments-service.",
"2025-08-21T12:30:00Z : Merged 'feature-e2e-tests' into 'main' for server-main/payments-service with SHA merge_sha_101.",
"2025-08-21T12:30:00Z : PR #101 merged for server-main/payments-service.",
"2025-08-21T12:30:00Z : Branch 'feature-e2e-tests' deleted from server-main/payments-service."
]
}
]
),

Task(
annotator="0",
user_id="task_95",
    instruction=(
        "You are 'server-main' with 'backend@coreservices.io' and auth key as 'ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h'. Resolve the open issue #15 in 'payments-service' titled 'Timeout too aggressive': append a QA confirmation comment 'Validated 60s timeout in staging.' by 'qa-erin'."
    ),
actions=[
Action(name="AuthenticateUser", kwargs={
"username": "server-main",
"email": "backend@coreservices.io",
"auth_key": "ghp_z5y4x3w2v1u0t9s8r7q6p5o4n3m2l1k0j9i8h"
}),
Action(name="AddCommentToIssue", kwargs={
"owner": "server-main",
"repo_name": "payments-service",
"issue_number": 15,
"issue_comment": "Validated 60s timeout in staging.",
"issue_comment_user": "qa-erin"
}),
Action(name="CloseIssue", kwargs={
"owner": "server-main",
"repo_name": "payments-service",
"issue_number": 15
}),
],
outputs=[
{
    "success": "Issue #15 closed for server-main/payments-service.",
    "repo": "server-main/payments-service",
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
        "You are 'maya-w' with 'alice.w@acme.dev' and auth key as 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your responsibility is to make sure the repository 'acme-webapp' achieves a state where a new document at 'docs/RELEASE_NOTES_1.1.0.md' exists with the contents exactly '## 1.1.0 - Minor fixes - Docs update'. This alteration needs to start from the line named 'release-notes-1.1.0', be executed by 'maya-w', and be presented through a pull request titled 'Docs: Release notes 1.1.0' with body 'Add release notes for version 1.1.0.' The pull request requires a review from 'nathan'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "maya-w", "email": "alice.w@acme.dev", "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"}),
        Action(name="CreateNewBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "file_name": "docs/RELEASE_NOTES_1.1.0.md", "file_content": "## 1.1.0 - Minor fixes - Docs update"}),
        Action(name="InitialCommit", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0", "commit_message": "Add docs/RELEASE_NOTES_1.1.0.md", "commit_author": "maya-w"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "maya-w",
            "repo_name": "acme-webapp",
            "pr_title": "Docs: Release notes 1.1.0",
            "pr_body": "Add release notes for version 1.1.0.",
            "head_branch_name": "release-notes-1.1.0",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["docs/RELEASE_NOTES_1.1.0.md"]
        }),
        Action(name="AssignPullRequestReviewers", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101, "reviewers": ["nathan"]}),
        Action(name="ApprovePr", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "source_branch_name": "release-notes-1.1.0", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "maya-w", "repo_name": "acme-webapp", "branch_name": "release-notes-1.1.0"}),
        Action(
                name="ListAllTerminalMessage",
                kwargs={},
            ),
    ],
    outputs=[
        {
            "messages": [
            "2025-08-21T12:00:00Z : Branch 'release-notes-1.1.0' created in maya-w/acme-webapp from 'main'.",
            "2025-08-21T12:00:00Z : Added 'docs/RELEASE_NOTES_1.1.0.md' to maya-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Initial commit added to maya-w/acme-webapp@release-notes-1.1.0.",
            "2025-08-21T12:00:00Z : Pull request #101 created for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Assigned reviewers to PR #101 for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Merged 'release-notes-1.1.0' into 'main' for maya-w/acme-webapp with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for maya-w/acme-webapp.",
            "2025-08-21T12:30:00Z : Branch 'release-notes-1.1.0' deleted from maya-w/acme-webapp."
            ]
        }
    ]
),
Task(
    annotator="0",
    user_id="task_97",
    instruction=(
        "You are 'design-team' with 'team@uidesign.co and auth key as 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your task is to ensure that the repository 'ui-kit' reaches a state where its default branch 'main' includes the component file 'packages/alert/index.tsx' with contents exactly 'export const Alert = () => <div role='alert' />'. The update must commence on the branch 'feature-alert', be executed by 'design-team' with the commit message 'Add packages/alert/index.tsx', and be communicated through a pull request titled 'Add Alert component' with body 'Introduce basic Alert component.' moving from 'feature-alert' to 'main', including approval of the pr."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={"username": "design-team", "email": "team@uidesign.co", "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"}),
        Action(name="CreateNewBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "base_branch": "main"}),
        Action(name="AddNewFileInRepo", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "file_name": "packages/alert/index.tsx", "file_content": "export const Alert = () => <div role='alert' />"}),
        Action(name="InitialCommit", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert", "commit_message": "Add packages/alert/index.tsx", "commit_author": "design-team"}),
        Action(name="CreatePullRequest", kwargs={
            "owner": "design-team",
            "repo_name": "ui-kit",
            "pr_title": "Add Alert component",
            "pr_body": "Introduce basic Alert component.",
            "head_branch_name": "feature-alert",
            "base_branch_name": "main",
            "head_sha": "commit_sha_101",
            "pr_files": ["packages/alert/index.tsx"]
        }),
        Action(name="ApprovePr", kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="MergeBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "source_branch_name": "feature-alert", "target_branch_name": "main"}),
        Action(name="MarkPrAsMerged", kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 101}),
        Action(name="DeleteBranch", kwargs={"owner": "design-team", "repo_name": "ui-kit", "branch_name": "feature-alert"}),
        Action(name="ListAllTerminalMessage", kwargs={}),
    ],
    outputs=[
        {
            "success": "Branch 'feature-alert' deleted from design-team/ui-kit.",
            "repo": "design-team/ui-kit",
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
            "2025-08-21T12:00:00Z : Branch 'feature-alert' created in design-team/ui-kit from 'main'.",
            "2025-08-21T12:00:00Z : Added 'packages/alert/index.tsx' to design-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Initial commit added to design-team/ui-kit@feature-alert.",
            "2025-08-21T12:00:00Z : Pull request #101 created for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : PR #101 marked APPROVE for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : Merged 'feature-alert' into 'main' for design-team/ui-kit with SHA merge_sha_101.",
            "2025-08-21T12:30:00Z : PR #101 merged for design-team/ui-kit.",
            "2025-08-21T12:30:00Z : Branch 'feature-alert' deleted from design-team/ui-kit."
            ]
        }
    ]
),

Task(
    annotator="0",
    user_id="task_99",
    instruction=(
        "You are 'maya-w' with 'alice.w@acme.dev' and auth key as 'ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r'. Your responsibility is to confirm that the repository 'acme-webapp' contains an open code scanning alert logged at ref 'refs/heads/main', characterized by a severity of 'high' and including the description 'SQL injection risk detected in src/db.py (user input concatenation).'. It is essential that the alert remains open and can be accessed by its details after creation."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "maya-w", "email": "alice.w@acme.dev",
            "auth_key": "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"
        }),
        Action(name="CreateCodeScanningAlert", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp",
            "severity": "high",
            "description": "SQL injection risk detected in src/db.py (user input concatenation).",
            "ref": "refs/heads/main"
        }),
        Action(name="GetAlertDetails", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp",
            "alert_number": 101
        }),
        Action(name="ListOpenAlertsForRepo", kwargs={
            "owner": "maya-w", "repo_name": "acme-webapp"
        }),
    ],
    outputs=[
        {
            "owner": "maya-w",
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
        "You are 'design-team' with 'team@uidesign.co' and auth key as 'ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s'. Your duty is to verify that the repository 'ui-kit' finalizes with a code scanning alert initially documented at ref 'refs/heads/main', having a severity level of 'medium' and described as 'Unsafe innerHTML assignment detected in packages/card/index.tsx.' which should then be dismissed with the reason 'false_positive'."
    ),
    actions=[
        Action(name="AuthenticateUser", kwargs={
            "username": "design-team", "email": "team@uidesign.co",
            "auth_key": "ghp_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s"
        }),
        Action(name="CreateCodeScanningAlert", kwargs={
            "owner": "design-team", "repo_name": "ui-kit",
            "severity": "medium",
            "description": "Unsafe innerHTML assignment detected in packages/card/index.tsx.",
            "ref": "refs/heads/main"
        }),
        Action(name="GetAlertDetails", kwargs={
            "owner": "design-team", "repo_name": "ui-kit",
            "alert_number": 101
        }),
        Action(name="DismissAlert", kwargs={
            "owner": "design-team", "repo_name": "ui-kit",
            "alert_number": 101,
            "dismiss_reason": "false_positive"
        }),
        # Action(name="ListOpenAlertsForRepo", kwargs={
        #     "owner": "design-team", "repo_name": "ui-kit"
        # }),
        Action(name="GetAlertDetails", kwargs={
            "owner": "design-team", "repo_name": "ui-kit",
            "alert_number": 101
        }),
    ],
    outputs=[
        {
            "owner": "design-team",
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
            #     name="authenticateUser",
            #     kwargs={"username":"maya-w", "email":"alice.w@acme.dev", "auth_key":"ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r"},
            # ),
            # Action(
            #     name="getRepoInfoForOwner",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp"},
            # ),
            # Action(
            #     name="getBranchContent",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp","branch_name":"feature-update"},
            # ),
            # Action(
            #     name="deleteRepository",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp"},
            # ),
            # Action(
            #     name="createRepository",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "private_flag":False, "auto_init_flag":True},
            # ),
            # Action(
            #     name="createNewBranch",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "branch_name":"feature-update2","base_branch":"feature-update"},
            # ),
            # Action(
            #     name="addNewFileInRepo",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "branch_name":"feature-update2","file_name":"docs/CHANGEaszdfaLOG.md", "file_content":"asfasgagasdaaf"},
            # ),
            # Action(
            #     name="updateFileInRepo",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "branch_name":"feature-update2","file_name":"docs/CHANGEaszdfaLOG.md", "file_content":"asfasgagasdaaf9137912"},
            # ),
            # Action(
            #     name="deleteFileInRepo",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "branch_name":"feature-update2","file_name":"docs/CHANGEaszdfaLOG.md"},
            # ),
            # Action(
            #     name="createNewBranch",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "branch_name":"feature-update2","base_branch":"feature-update"},
            # ),
            # Action(
            #     name="initialCommit",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "branch_name":"feature-update2", "commit_message":"Initial commit", "commit_author":"maya-w"},
            # ),
            # Action(
            #     name="makeCommit",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "branch_name":"feature-update2", "commit_message":"second  commit", "commit_author":"maya-w"},
            # ),
            # Action(
            #     name="createPullRequest",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "pr_title":"InitPR", "pr_body":"Initial PR", "head_branch_name":"feature-update2", "base_branch_name":"feature-update", "head_sha":"commit_sha_13", "pr_files":["docs/CHANGEaszdfaLOG.md"]},
            # ),
            # Action(
            #     name="assignPullRequestReviewers",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "pr_number":101, "reviewers":["nathan"]},
            # ),
            # Action(
            #     name="addPullRequestComment",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "pr_number":101, "comment":"Nice Job", "comment_user":"nathan", "review_state":"COMMENT"},
            # ),
            # Action(
            #     name="addPullRequestComment",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "pr_number":101, "comment":"Maybe need some changes", "comment_user":"nathan", "review_state":"REQUEST_CHANGE"},
            # ),
            # Action(
            #     name="approvePr",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "pr_number":101},
            # ),
            
            # Action(
            #     name="listOfPrForRepo",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp"},
            # ),
            
            # Action(
            #     name="mergeBranch",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "source_branch_name":"feature-update2", "target_branch_name":"feature-update"},
            # ),
            
            # Action(
            #     name="mergePullRequest",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "pr_number":101},
            # ),
            # Action(
            #     name="markPrAsMerged",
            #     kwargs={"owner": "design-team", "repo_name": "ui-kit", "pr_number": 11}
            # ),
            # Action(
            #     name="getPrDetails",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "pr_number":101},
            # ),
            # Action(
            #     name="deleteBranch",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp", "branch_name":"feature-update2"},
            # ),
            # Action(
            #     name="createNewIssue",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp","title":"fix UI","body":"Webpage not working","labels":["bug-fix"],"assignees":["frontend team","backend team"]},
            # ),
            # Action(
            #     name="addCommentToIssue",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp","issue_number":101, "issue_comment":"Fixed backend", "issue_comment_user":"backend team"},
            # ),
            
            # Action(
            #     name="addCommentToIssue",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp","issue_number":101, "issue_comment":"Fixed UI", "issue_comment_user":"frontend team"},
            # ),
            # Action(
            #     name="closeIssue",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp","issue_number":101},
            # ),
            # Action(
            #     name="getAllIssuesForRepo",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp"},
            # ),
            # Action(
            #     name="createCodeScanningAlert",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp","severity":"low", "description":"some bug", "ref":"refs/heads/main"},
            # ),
            # Action(
            #     name="getAlertDetails",
            #     kwargs={"owner":"maya-w", "repo_name":"acme-webapp","alert_number":101},
            # ),
            # Action(
            #     name="listOpenAlertsForRepo",
            #     kwargs={"owner":"design-team", "repo_name":"ui-kit"},
            # ),
            # Action(
            #     name="dismissAlert",
            #     kwargs={"owner":"design-team", "repo_name":"ui-kit","alert_number":2},
            # ),
            # Action(
            #     name="listOpenAlertsForRepo",
            #     kwargs={"owner":"design-team", "repo_name":"ui-kit"},
            # ),
            # Action(
            #     name="listAllTerminalMessage",
            #     kwargs={},
            # ),