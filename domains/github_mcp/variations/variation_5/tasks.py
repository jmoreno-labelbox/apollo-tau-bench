# Copyright Sierra

tasks = [
    {
        "annotator": 1,
        "user_id": "user_505",
        "instruction": "Your strategic goal is to handle the **New Service Onboarding and Governance Policy** for a project named 'notification-service'. This policy insists that new services are not only technically bootstrapped but also adhere to initial governance and security compliance standards before their first release. You are accountable for ensuring the repository fully aligns with the policy using the allocated **Onboarding Manifest**. Your ultimate deliverable is a summary of the repository\u2019s health to validate its compliant state. **Onboarding Manifest:** * **Repository:** {name: 'notification-service', description: 'Centralized service for handling user notifications.', private: True} * **Governance:** * **Commits:** [{message: 'docs: Add MIT License', author: 'docs-sophia'}, {message: 'docs: Add SECURITY.md policy', author: 'docs-sophia'}] * **Ops Issue:** {title: 'ops: Configure main branch protection rules', body: 'Tracking issue for branch protection setup as per governance policy.', labels: ['ops', 'governance'], assignee: 'infra-lead'} * **Security Remediation:** * **Alert:** {severity: 'medium', description: 'Default template includes outdated dependency: common-lib v1.2.3', file: 'package.json', branch: 'main'} * **Issue:** {title: 'fix: Update outdated dependency common-lib', body: 'Tracking issue to update the vulnerable common-lib dependency.', labels: ['security', 'dependency'], assignee: 'infra-lead'} * **Code:** {branch: 'fix/update-common-lib', commit_message: 'fix: Upgrade common-lib to v1.2.4', author: 'infra-lead'} * **PR:** {title: 'fix(deps): Upgrade common-lib to v1.2.4', body: 'PR to upgrade outdated common-lib dependency to v1.2.4.'} * **Release:** {version: 'v0.1.0', description: 'Initial compliant release.'}",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "notification-service",
                    "description": "Centralized service for handling user notifications.",
                    "private": true
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "notification-service",
                    "branch": "main",
                    "message": "docs: Add MIT License",
                    "author": "docs-sophia"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "notification-service",
                    "branch": "main",
                    "message": "docs: Add SECURITY.md policy",
                    "author": "docs-sophia"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "title": "ops: Configure main branch protection rules",
                    "body": "Tracking issue for branch protection setup as per governance policy.",
                    "labels": [
                        "ops",
                        "governance"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "issue_number": 12,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "notification-service",
                    "severity": "medium",
                    "description": "Default template includes outdated dependency: common-lib v1.2.3",
                    "file": "package.json",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "title": "fix: Update outdated dependency common-lib",
                    "body": "Tracking issue to update the vulnerable common-lib dependency.",
                    "labels": [
                        "security",
                        "dependency"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "issue_number": 13,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "notification-service",
                    "branch": "fix/update-common-lib",
                    "message": "fix: Upgrade common-lib to v1.2.4",
                    "author": "infra-lead"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "notification-service",
                    "title": "fix(deps): Upgrade common-lib to v1.2.4",
                    "body": "PR to upgrade outdated common-lib dependency to v1.2.4.",
                    "head_branch": "fix/update-common-lib",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "notification-service",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "issue_number": 13
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "notification-service",
                    "alert_number": 10
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "notification-service",
                    "version": "v0.1.0",
                    "description": "Initial compliant release."
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "notification-service"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "notification-service",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_1005",
        "instruction": "Your mission is to coordinate the **Infrastructure Hardening Policy** for the 'infra-terraform' repository. The policy necessitates addressing identified compliance gaps by tracking each item in a separate issue and resolving it with a dedicated pull request. You are tasked with coordinating this process for all items listed in the **Hardening Manifest**. The final deliverable is a report of commits by author to confirm that the 'platform-team' executed all required changes. **Hardening Manifest:** * **Work Items:** [ {title: 'Add restrictive security group rules'}, {title: 'Enable S3 bucket access logging'} ]",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "Add restrictive security group rules",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 12,
                    "assignees": [
                        "platform-team"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "feature/sg-rules",
                    "message": "feat: Implement restrictive ingress rules",
                    "author": "platform-team"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "feat: Add restrictive security groups",
                    "body": "",
                    "head_branch": "feature/sg-rules",
                    "base_branch": "main",
                    "author": "platform-team"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "Enable S3 bucket access logging",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 13,
                    "assignees": [
                        "platform-team"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "feature/s3-logging",
                    "message": "feat: Enable server access logging for all buckets",
                    "author": "platform-team"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "feat: Enable S3 access logging",
                    "body": "",
                    "head_branch": "feature/s3-logging",
                    "base_branch": "main",
                    "author": "platform-team"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 13
                },
            },
            {
                "name": "CountCommitsByAuthor",
                "arguments": {
                    "repo_name": "infra-terraform"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "infra-terraform",
                        "commits_by_author": {
                            "platform-team": 2
                        },
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_1003",
        "instruction": "Your task is to handle the **Full Security Audit and Remediation Policy** on the 'acme-webapp' repository. You are responsible for addressing the vulnerabilities outlined in the **Data Specification** and making sure the repository's final condition is entirely compliant with the official **Compliance Specification** provided below. Your final output should be a health summary that certifies all the detected vulnerabilities have been rectified. **Compliance Specification:** * **Vulnerability Remediation:** Both the 'high' and 'medium' severity alerts need to be in a 'fixed' state. * **Incident Tracking:** Two corresponding issues, one for each vulnerability, must be established to monitor the remediation and should be in a 'closed' state. * **Code Consolidation:** The code fixes for both vulnerabilities must be joined into a single 'merged' Pull Request. * **Release:** A new, secure version 'v1.1.0' must be published, described as 'Security hardening release.' **Data Specification:** * High-Severity Alert: {description: 'Cross-Site Scripting (XSS) in user profile page', file: 'src/app/profile.html'} * Medium-Severity Alert: {description: 'Insecure Direct Object Reference in API', file: 'src/app/api.py'} * Issue Titles: ['Fix XSS in profile page', 'Fix IDOR in API'] * Code Artifacts: {branch: 'security/hardening-sprint', commit_message: 'fix: Harden XSS and IDOR vulnerabilities', pr_title: 'fix: Security Hardening', author: 'maya-w'} * Release Details: {version: 'v1.1.0', description: 'Security hardening release.'}",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "severity": "high",
                    "description": "Cross-Site Scripting (XSS) in user profile page",
                    "file": "src/app/profile.html",
                    "branch": "main"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "severity": "medium",
                    "description": "Insecure Direct Object Reference in API",
                    "file": "src/app/api.py",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Fix XSS in profile page",
                    "body": ""
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Fix IDOR in API",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12,
                    "assignees": [
                        "maya-w"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 13,
                    "assignees": [
                        "maya-w"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "security/hardening-sprint",
                    "message": "fix: Harden XSS and IDOR vulnerabilities",
                    "author": "maya-w"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "fix: Security Hardening",
                    "body": "",
                    "head_branch": "security/hardening-sprint",
                    "base_branch": "main",
                    "author": "maya-w"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 13
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "alert_number": 10
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "alert_number": 11
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "version": "v1.1.0",
                    "description": "Security hardening release."
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "acme-webapp"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "acme-webapp",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_9003",
        "instruction": "Your assignment is to oversee the **Feature Development Lifecycle Policy** for the 'ui-kit' repository. The policy stipulates that a new feature is to be tracked, developed, and reviewed prior to being integrated. You must employ the supplied **Feature Manifest** to produce all essential artifacts. Your final deliverable is the repository's activity dashboard to confirm that the feature was integrated successfully. **Compliance Specification:** The end state must demonstrate that a new feature was monitored through an issue, which must be 'closed'. The work is to be carried out on a feature branch and submitted via a pull request. The pull request must be evaluated before it is merged. **Feature Manifest:** * **Issue:** {title: 'Feature: Add user avatar component', body: 'Tracking issue for the new user avatar component.', labels: ['feature', 'ui'], assignee: 'ui-dev'} * **Code Artifacts:** {branch: 'feature/avatar-component', commit_message: 'feat: Add new user avatar component', pr_title: 'feat: User Avatar Component', pr_body: 'This PR adds the new user avatar component.', author: 'ui-dev'} * **Reviewer:** 'design-lead'",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Feature: Add user avatar component",
                    "body": "Tracking issue for the new user avatar component.",
                    "labels": [
                        "feature",
                        "ui"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/avatar-component",
                    "message": "feat: Add new user avatar component",
                    "author": "ui-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "feat: User Avatar Component",
                    "body": "This PR adds the new user avatar component.",
                    "head_branch": "feature/avatar-component",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "reviewers": [
                        "design-lead"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "ui-kit"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "ui-kit",
                        "commits_count": 1,
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_4001",
        "instruction": "Your task is to handle the **Repository Re-branding Policy** for the 'portfolio-site' repository, as it is being transformed into a team blog. The policy entails establishing the repository and modifying its metadata, with all related changes logged through issues. You must deliver a detailed list of all commits made throughout the rebranding to serve as an audit trail. **Compliance Specification:** Ensure the final outcome reflects that the repository has been created privately and its description revised. An epic issue should be initiated and concluded to monitor the whole rebranding initiative. Develop and close two sub-task issues to oversee specific actions. All tasks must culminate in one merged pull request. **Data Specification:** * Repo Name: 'portfolio-site' * Initial Description: 'Personal portfolio website.' * New Description: 'A new blog for the engineering team.' * Epic Title: 'Rebrand portfolio-site to Team Blog' * Task Titles: ['Update index.html with blog layout', 'Add new blog-styles.css file'] * Assignee/Author: 'intern-emma' * Code Artifacts: {branch: 'feature/rebrand', commit_message: 'feat: Rebrand site to team blog', pr_title: 'feat: Team Blog Rebrand'}",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "description": "Personal portfolio website.",
                    "private": true
                },
            },
            {
                "name": "UpdateRepositoryDescription",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "description": "A new blog for the engineering team."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "title": "Rebrand portfolio-site to Team Blog",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "issue_number": 12,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "title": "Update index.html with blog layout",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "issue_number": 13,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "title": "Add new blog-styles.css file",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "issue_number": 14,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "branch": "feature/rebrand",
                    "message": "feat: Rebrand site to team blog",
                    "author": "intern-emma"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "title": "feat: Team Blog Rebrand",
                    "body": "",
                    "head_branch": "feature/rebrand",
                    "base_branch": "main",
                    "author": "intern-emma"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "pr_number": 10,
                    "issue_number": 14
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "issue_number": 13
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "issue_number": 14
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "issue_number": 12
                },
            },
            {
                "name": "ListCommitsByBranch",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "branch": "feature/rebrand"
                }
            }
        ],
        "outputs": [
                [
                    {
                        "commit_id": "e4d3bffc0cca",
                        "repo": "portfolio-site",
                        "branch": "feature/rebrand",
                        "message": "feat: Rebrand site to team blog",
                        "author": "intern-emma",
                        "timestamp": "2025-08-26"
                    }
                ]
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_60001",
        "instruction": "Please handle the **Hotfix Porting and Verification Policy** for the 'security-scanner' repository. A critical hotfix, v0.4.1, previously applied to a release branch, needs to be integrated back into the main development line. The policy mandates a complete and verifiable record of this process, culminating in a new QA verification task. Your deliverable is a set of reports\u2014the repository's activity dashboard and an issue aging report\u2014to verify the process completion and to aid in prioritizing the new verification task. **Compliance Specification:** The final outcome must indicate that the porting activity was tracked using a primary issue, which must be 'closed'. All code alterations should be unified in a single 'merged' pull request on the 'hotfix/parser-revert-port' branch. This PR should include commits from various authors regarding the reversion, conflict resolution, and updated tests. A new open verification issue must be initiated. **Data Manifest:** * **Porting Task:** {main_issue_title: 'Port hotfix v0.4.1 to main', main_issue_body: 'Main tracking issue for porting hotfix v0.4.1 to the main branch.', labels: ['hotfix', 'porting'], assignee: 'security-group'} * **Verification Task:** {qa_issue_title: 'Verify hotfix integration in next release', qa_issue_body: 'Create a formal verification plan for the ported hotfix in the upcoming release.', labels: ['verification', 'qa'], assignee: 'qa-erin'} * **Implementation:** * **PR:** {title: 'chore: Port hotfix v0.4.1 to main', body: 'PR to port the emergency hotfix back to the main development line.', reviewers: ['security-group', 'tech-lead-tara', 'qa-erin']} * **Commits:** [ {message: 'revert: Revert parser engine to stable version', author: 'security-group'}, {message: 'refactor: Resolve merge conflicts with main', author: 'security-group'}, {message: 'test: Update tests for main branch compatibility', author: 'qa-erin'} ]",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Port hotfix v0.4.1 to main",
                    "body": "Main tracking issue for porting hotfix v0.4.1 to the main branch.",
                    "labels": [
                        "hotfix",
                        "porting"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "hotfix/parser-revert-port",
                    "message": "revert: Revert parser engine to stable version",
                    "author": "security-group"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "hotfix/parser-revert-port",
                    "message": "refactor: Resolve merge conflicts with main",
                    "author": "security-group"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "hotfix/parser-revert-port",
                    "message": "test: Update tests for main branch compatibility",
                    "author": "qa-erin"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "chore: Port hotfix v0.4.1 to main",
                    "body": "PR to port the emergency hotfix back to the main development line.",
                    "head_branch": "hotfix/parser-revert-port",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "reviewers": [
                        "security-group",
                        "tech-lead-tara",
                        "qa-erin"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Verify hotfix integration in next release",
                    "body": "Create a formal verification plan for the ported hotfix in the upcoming release.",
                    "labels": [
                        "verification",
                        "qa"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "qa-erin"
                    ]
                },
            },
            {
                "name": "GetIssueAgingReport",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": [
                        {
                            "issue_id": "ISSUE_security-scanner_ad99393c",
                            "title": "Port hotfix v0.4.1 to main",
                            "state": "closed",
                            "created_at": "2025-08-26",
                            "days_open": 0,
                            "report_date": "2025-08-26"
                        },
                        {
                            "issue_id": "ISSUE_security-scanner_948af871",
                            "title": "Verify hotfix integration in next release",
                            "state": "open",
                            "created_at": "2025-08-26",
                            "days_open": 0,
                            "report_date": "2025-08-26"
                        }
                    ]
                },
                {
                    "status": "ok",
                    "data": {
                        "repo": "security-scanner",
                        "commits_count": 3,
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_304",
        "instruction": "Your responsibility is to handle the company's **Production Incident Response Policy** for the 'security-scanner' repository. A faulty deployment has triggered a critical production alert. You need to manage the entire incident lifecycle, which involves releasing a hotfix and starting a post-mortem, using the provided **Incident Manifest**. Your ultimate deliverable is the repository health summary, validating that the incident is resolved and a post-mortem is in progress. **Incident Manifest:** * **Faulty Release:** * **Details:** {version: '0.4.0', description: 'Release with new parser engine.'} * **Code:** {commit_message: 'feat: Rollout new parser engine', branch: 'release/v0.4.0', pr_title: 'Release v0.4.0', pr_body: 'PR for v0.4.0 release.'} * **Deployment:** {environment: 'production-v0.4.0'} * **Incident Alert:** * **Details:** {severity: 'critical', description: 'Production Outage: Invalid parser config deployed causes infinite loop.', file: 'src/parser.rs', branch: 'main'} * **Hotfix:** * **Issue:** {title: 'HOTFIX: Production outage in parser engine', body: 'Tracking issue for the emergency hotfix.', labels: ['bug', 'hotfix', 'production-issue'], assignee: 'security-group'} * **Code:** {branch: 'hotfix/parser-revert', commit_message: 'revert: Revert parser engine to stable version'} * **PR:** {title: 'Hotfix: Revert parser engine change', body: 'Hotfix PR to revert the parser engine.'} * **Release:** {version: '0.4.1', description: 'Hotfix release to revert faulty parser engine.'} * **Deployment:** {environment: 'production-v0.4.1'} * **Post-Mortem:** * **Issue:** {title: 'Post-Mortem: Parser Engine Outage v0.4.0', body: 'Post-mortem investigation tracking issue.', labels: ['post-mortem', 'audit'], assignee: 'tech-lead-tara'}",
        "actions": [
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "release/v0.4.0",
                    "message": "feat: Rollout new parser engine",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Release v0.4.0",
                    "body": "PR for v0.4.0 release.",
                    "head_branch": "release/v0.4.0",
                    "base_branch": "main"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "security-scanner",
                    "version": "0.4.0",
                    "description": "Release with new parser engine."
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "security-scanner",
                    "environment": "production-v0.4.0"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "severity": "critical",
                    "description": "Production Outage: Invalid parser config deployed causes infinite loop.",
                    "file": "src/parser.rs",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "HOTFIX: Production outage in parser engine",
                    "body": "Tracking issue for the emergency hotfix.",
                    "labels": [
                        "bug",
                        "hotfix",
                        "production-issue"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "hotfix/parser-revert",
                    "message": "revert: Revert parser engine to stable version",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Hotfix: Revert parser engine change",
                    "body": "Hotfix PR to revert the parser engine.",
                    "head_branch": "hotfix/parser-revert",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 11,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "security-scanner",
                    "version": "0.4.1",
                    "description": "Hotfix release to revert faulty parser engine."
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "security-scanner",
                    "environment": "production-v0.4.1"
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "alert_number": 10
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Post-Mortem: Parser Engine Outage v0.4.0",
                    "body": "Post-mortem investigation tracking issue.",
                    "labels": [
                        "post-mortem",
                        "audit"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "security-scanner",
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_5002",
        "instruction": "Your objective is to coordinate the **Core Refactor Policy** for the 'payments-service' repository. The policy mandates that major refactoring tasks are tracked via a main epic and designated sub-tasks, with all code modifications integrated into a single pull request. You are tasked with overseeing this process using the supplied **Refactor Manifest**. Your final output is a dual report: one that counts commits by author to authenticate the work, and another that assesses the repository's risk score to confirm no new security issues have been introduced. **Refactor Manifest: Q3 Performance** * **Tracking:** * **Epic:** {title: 'Q3 Performance Refactor', body: ''} * **Sub-Tasks:** [{title: 'Optimize database query patterns', body: ''}, {title: 'Implement caching layer for responses', body: ''}] * **Implementation:** * **Branch:** 'refactor/performance-q3' * **Commits:** [{message: 'refactor: Optimize DB queries'}, {message: 'feat: Add caching layer'}] * **PR:** {title: 'refactor: Q3 Performance Improvements', body: ''} * **Ownership:** {assignee: 'server-main', author: 'server-main'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Q3 Performance Refactor",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Optimize database query patterns",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 13,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Implement caching layer for responses",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 14,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "refactor/performance-q3",
                    "message": "refactor: Optimize DB queries",
                    "author": "server-main"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "refactor/performance-q3",
                    "message": "feat: Add caching layer",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "refactor: Q3 Performance Improvements",
                    "body": "",
                    "head_branch": "refactor/performance-q3",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10,
                    "issue_number": 14
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 13
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 14
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12
                },
            },
            {
                "name": "CountCommitsByAuthor",
                "arguments": {
                    "repo_name": "payments-service"
                },
            },
            {
                "name": "GetRepositoryRiskScore",
                "arguments": {
                    "repo_name": "payments-service"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "payments-service",
                        "commits_by_author": {
                            "server-main": 2
                        },
                        "report_date": "2025-08-26"
                    }
                },
                {
                    "status": "ok",
                    "data": {
                        "repo": "payments-service",
                        "open_alerts_count": 0,
                        "risk_score": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_6001",
        "instruction": "Your task is to manage the transformation of the 'portfolio-site' repository into a new team blog, ensuring complete adherence to the company's **Repository Re-branding Policy**. The policy dictates that the entire process, from the creation of the repository and the updating of metadata to the application of changes, is meticulously documented through a main epic and detailed sub-tasks. Every piece of work must be compiled into a single, reviewable pull request. You bear the responsibility for handling this process utilizing the supplied **Re-branding Manifest**. Your ultimate deliverable is a compilation of all commits executed during the rebranding to act as an audit trail. **Re-branding Manifest:** * **Repository:** {name: 'portfolio-site', initial_description: 'Personal portfolio website.', new_description: 'A new blog for the engineering team.', private: True} * **Tracking:** * **Epic:** {title: 'Rebrand portfolio-site to Team Blog', body: ''} * **Sub-Tasks:** [{title: 'Update index.html with blog layout', body: ''}, {title: 'Add new blog-styles.css file', body: ''}] * **Implementation:** * **Branch:** 'feature/rebrand' * **Commit:** {message: 'feat: Rebrand site to team blog'} * **PR:** {title: 'feat: Team Blog Rebrand', body: ''} * **Ownership:** {assignee: 'intern-emma', author: 'intern-emma'}",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "description": "Personal portfolio website.",
                    "private": true
                },
            },
            {
                "name": "UpdateRepositoryDescription",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "description": "A new blog for the engineering team."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "title": "Rebrand portfolio-site to Team Blog",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "issue_number": 12,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "title": "Update index.html with blog layout",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "issue_number": 13,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "title": "Add new blog-styles.css file",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "issue_number": 14,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "branch": "feature/rebrand",
                    "message": "feat: Rebrand site to team blog",
                    "author": "intern-emma"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "title": "feat: Team Blog Rebrand",
                    "body": "",
                    "head_branch": "feature/rebrand",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "pr_number": 10,
                    "issue_number": 14
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "issue_number": 13
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "issue_number": 14
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "issue_number": 12
                },
            },
            {
                "name": "ListCommitsByBranch",
                "arguments": {
                    "repo_name": "portfolio-site",
                    "branch": "feature/rebrand"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": [
                        {
                            "commit_id": "e4d3bffc0cca",
                            "repo": "portfolio-site",
                            "branch": "feature/rebrand",
                            "message": "feat: Rebrand site to team blog",
                            "author": "intern-emma",
                            "timestamp": "2025-08-26",
                            "report_date": "2025-08-26"
                        }
                    ]
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_105",
        "instruction": "Your main goal is to coordinate the company's **Standard Project Bootstrap Policy** for the new 'log-analyzer-service'. This policy guarantees that all new projects are initiated with a uniform set of primary artifacts for tracking, security, and deployment readiness. You must utilize the given **Bootstrap Manifest** to generate all necessary entities and ensure the final condition complies with the **Compliance Specification**. **Compliance Specification:** * The first new issue created for this task must be `number: 12`. * The first new security alert created for this task must be `number: 10`. **Bootstrap Manifest:** * **Repository:** {name: 'log-analyzer-service', description: 'Service for parsing and analyzing application logs.', private: True} * **Initial Commit:** {author: 'server-main', message: 'Initial commit: project structure and boilerplate'} * **Tracking Issue:** {title: 'Define initial logging schema', body: 'Establish the standard JSON schema for log entries.', labels: ['schema', 'design'], assignee: 'server-main'} * **Initial Security Alert:** {severity: 'high', description: 'Potential for arbitrary code execution via insecure YAML parsing.', file: 'src/parser.py', branch: 'main'} * **Initial Deployment:** {environment: 'development'}",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "description": "Service for parsing and analyzing application logs.",
                    "private": true
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "branch": "main",
                    "message": "Initial commit: project structure and boilerplate",
                    "author": "server-main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "title": "Define initial logging schema",
                    "body": "Establish the standard JSON schema for log entries.",
                    "labels": [
                        "schema",
                        "design"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "severity": "high",
                    "description": "Potential for arbitrary code execution via insecure YAML parsing.",
                    "file": "src/parser.py",
                    "branch": "main"
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "environment": "development"
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "log-analyzer-service"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "log-analyzer-service",
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts": 1,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_701",
        "instruction": "Your main strategic goal is to oversee the incorporation of a critical hotfix into the main development branch for the 'security-scanner' repository, ensuring complete compliance with the company's **Hotfix Porting and Verification Policy**. This policy requires a transparent and auditable record for backporting hotfixes from release branches to the main branch, which includes setting up a follow-up verification task. You are tasked with handling this procedure using the provided **Porting Manifest**. Your ultimate deliverable is a collection of reports \u2014 the repository's activity dashboard and an issue aging report \u2014 to validate the completion of the process and assist in prioritizing the forthcoming verification task. **Porting Manifest:** * **Hotfix Version to Port:** v0.4.1 * **Description:** The hotfix reverts the parser engine to a stable version and requires porting back to the 'main' branch. The work will include merging conflict resolution and test updates. * **Ownership:** The porting task is managed by 'security-group', with testing assistance from 'qa-erin'. 'qa-erin' should be assigned the follow-up verification task. * **Review:** The porting pull request needs approval from 'security-group', 'tech-lead-tara', and 'qa-erin'.",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Port hotfix v0.4.1 to main",
                    "body": "Main tracking issue for porting hotfix v0.4.1 to the main branch.",
                    "labels": [
                        "hotfix",
                        "porting"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "hotfix/parser-revert-port",
                    "message": "revert: Revert parser engine to stable version",
                    "author": "security-group"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "hotfix/parser-revert-port",
                    "message": "refactor: Resolve merge conflicts with main",
                    "author": "security-group"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "hotfix/parser-revert-port",
                    "message": "test: Update tests for main branch compatibility",
                    "author": "qa-erin"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "chore: Port hotfix v0.4.1 to main",
                    "body": "PR to port the emergency hotfix back to the main development line.",
                    "head_branch": "hotfix/parser-revert-port",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "reviewers": [
                        "security-group",
                        "tech-lead-tara",
                        "qa-erin"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Verify hotfix integration in next release",
                    "body": "Create a formal verification plan for the ported hotfix in the upcoming release.",
                    "labels": [
                        "verification",
                        "qa"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "qa-erin"
                    ]
                },
            },
            {
                "name": "GetIssueAgingReport",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": [
                        {
                            "issue_id": "ISSUE_security-scanner_ad99393c",
                            "title": "Port hotfix v0.4.1 to main",
                            "state": "closed",
                            "created_at": "2025-08-26",
                            "days_open": 0,
                            "report_date": "2025-08-26"
                        },
                        {
                            "issue_id": "ISSUE_security-scanner_948af871",
                            "title": "Verify hotfix integration in next release",
                            "state": "open",
                            "created_at": "2025-08-26",
                            "days_open": 0,
                            "report_date": "2025-08-26"
                        }
                    ]
                },
                {
                    "status": "ok",
                    "data": {
                        "repo": "security-scanner",
                        "commits_count": 3,
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_2003",
        "instruction": "Make certain that the 'ml-pipeline' repository adheres to the **Proactive Dependency Update Policy** by implementing the update for the scikit-learn library as detailed in the **Update Manifest**. The definitive deliverable has to be the repository's activity dashboard to verify the update's completion. **Update Manifest: scikit-learn** * **Tracking Issue:** {title: 'chore(deps): Update scikit-learn to latest version', body: 'Update the scikit-learn dependency to the latest stable version.', labels: ['chore', 'dependencies'], assignee: 'ml-engineer'} * **Implementation:** * **Branch:** 'chore/update-sklearn' * **Commit:** {message: 'chore: Update scikit-learn to v1.4.0', author: 'ml-engineer'} * **PR:** {title: 'chore(deps): Update scikit-learn', body: 'This PR updates scikit-learn.'} * **Reviewer:** 'ml-engineer'",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "title": "chore(deps): Update scikit-learn to latest version",
                    "body": "Update the scikit-learn dependency to the latest stable version.",
                    "labels": [
                        "chore",
                        "dependencies"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "issue_number": 12,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "branch": "chore/update-sklearn",
                    "message": "chore: Update scikit-learn to v1.4.0",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "title": "chore(deps): Update scikit-learn",
                    "body": "This PR updates scikit-learn.",
                    "head_branch": "chore/update-sklearn",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "pr_number": 10,
                    "reviewers": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "ml-pipeline"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "ml-pipeline",
                        "commits_count": 1,
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_604",
        "instruction": "Your primary strategic responsibility is to handle the **Quarterly Tech Debt Initiative Policy** for the 'security-scanner' repository. This policy necessitates that a central epic oversees all planned refactoring for the quarter, with each tech debt item being resolved in sequence. Every solution must be formally tracked and merged through its own pull request. You are tasked with coordinating this process using the provided **Tech Debt Manifest**. Your final output is the repository's activity dashboard, confirming that all tech debt items for the quarter have been resolved, while the main epic remains open to monitor the overall initiative. **Tech Debt Manifest (Q3):** * **Main Epic:** {title: 'Q3 Tech Debt Paydown', body: 'Main epic to track all Q3 tech debt sub-tasks.', labels: ['tech-debt', 'epic'], assignee: 'tech-lead-tara'} * **Sub-Task Issues:** [ {title: 'Refactor Parser Module', body: 'Sub-task to track the refactoring of the parser module.', labels: ['tech-debt', 'refactor'], assignee: 'security-group'}, {title: 'Update Deprecated Dependencies', body: 'Sub-task to track the update of deprecated dependencies.', labels: ['tech-debt', 'chore'], assignee: 'security-group'}, {title: 'Remove Deprecated Handlers', body: 'Sub-task to track the removal of deprecated v1 handlers.', labels: ['tech-debt', 'refactor'], assignee: 'security-group'} ] * **Code Implementations:** [ {branch: 'refactor/parser', commit_message: 'refactor: Simplify parser logic', author: 'security-group'}, {branch: 'chore/update-deps', commit_message: 'chore: Update all dependencies to latest stable', author: 'security-group'}, {branch: 'refactor/remove-handlers', commit_message: 'refactor: Remove unused v1 handlers', author: 'security-group'} ] * **Pull Requests:** [ {title: 'refactor: Parser Module', body: 'PR to implement the parser refactor.', reviewers: ['tech-lead-tara']}, {title: 'chore: Update Dependencies', body: 'PR to update all dependencies to their latest stable versions.', reviewers: ['tech-lead-tara']}, {title: 'refactor: Remove Deprecated Handlers', body: 'PR to remove the unused v1 handlers.', reviewers: ['tech-lead-tara']} ]",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Q3 Tech Debt Paydown",
                    "body": "Main epic to track all Q3 tech debt sub-tasks.",
                    "labels": [
                        "tech-debt",
                        "epic"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Refactor Parser Module",
                    "body": "Sub-task to track the refactoring of the parser module.",
                    "labels": [
                        "tech-debt",
                        "refactor"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "refactor/parser",
                    "message": "refactor: Simplify parser logic",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "refactor: Parser Module",
                    "body": "PR to implement the parser refactor.",
                    "head_branch": "refactor/parser",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Update Deprecated Dependencies",
                    "body": "Sub-task to track the update of deprecated dependencies.",
                    "labels": [
                        "tech-debt",
                        "chore"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 14,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "chore/update-deps",
                    "message": "chore: Update all dependencies to latest stable",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "chore: Update Dependencies",
                    "body": "PR to update all dependencies to their latest stable versions.",
                    "head_branch": "chore/update-deps",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 11,
                    "issue_number": 14
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 11,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 14
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Remove Deprecated Handlers",
                    "body": "Sub-task to track the removal of deprecated v1 handlers.",
                    "labels": [
                        "tech-debt",
                        "refactor"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 15,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "refactor/remove-handlers",
                    "message": "refactor: Remove unused v1 handlers",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "refactor: Remove Deprecated Handlers",
                    "body": "PR to remove the unused v1 handlers.",
                    "head_branch": "refactor/remove-handlers",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 12,
                    "issue_number": 15
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 12,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 12
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 15
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "security-scanner",
                        "commits_count": 3,
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_204",
        "instruction": "Your responsibility is to manage the company's **Standard Year-End Governance Audit Policy** for the 'ui-kit' repository. This policy requires a thorough analysis of project activity and health metrics from the final quarter of the year. The policy stipulates that all findings are compiled into a formal summary issue. You must utilize the provided **Audit Manifest** to scope your analysis and produce the necessary artifact. Your final deliverable is the comprehensive end-to-end report for the repository to ensure the audit is complete. **Audit Manifest (Year-End 2023):** * **Analysis Scope:** * Commit Date Range: Start='2023-10-01T00:00:00Z', End='2023-12-31T23:59:59Z' * Issue Label Filter: 'bug' * **Summary Issue Artifact:** * Title: 'Governance Audit Findings for Year-End 2023' * Body: 'This issue summarizes the Year-End 2023 audit, covering performance, security, and backlog status.' * Labels: ['audit', 'governance'] * Assignee: 'release-manager'",
        "actions": [
            {
                "name": "CountCommitsByAuthor",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "ListCommitsByDateRange",
                "arguments": {
                    "repo_name": "ui-kit",
                    "start_date": "2023-10-01T00:00:00Z",
                    "end_date": "2023-12-31T23:59:59Z"
                },
            },
            {
                "name": "GetIssueAgingReport",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "ListIssuesByLabel",
                "arguments": {
                    "repo_name": "ui-kit",
                    "label": "bug"
                },
            },
            {
                "name": "GetPullRequestMergeTimeReport",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "ListPullRequests",
                "arguments": {
                    "repo_name": "ui-kit",
                    "state": "open"
                },
            },
            {
                "name": "GetOpenSecurityAlerts",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "GetRepositoryRiskScore",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "GetReleasesByRepository",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "GetDeploymentFrequencyReport",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Governance Audit Findings for Year-End 2023",
                    "body": "This issue summarizes the Year-End 2023 audit, covering performance, security, and backlog status.",
                    "labels": [
                        "audit",
                        "governance"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12,
                    "assignees": [
                        "release-manager"
                    ]
                },
            },
            {
                "name": "GenerateEndToEndReport",
                "arguments": {
                    "repo_name": "ui-kit"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "ui-kit",
                    "commits_count": 0,
                    "open_issues": 1,
                    "merged_prs": 0,
                    "open_alerts": 0,
                    "releases_count": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_30002",
        "instruction": "Handle the implementation of the **Cross-Repo Incompatibility Policy**. An ongoing feature in 'react-dashboard' has caused a new high-severity alert due to a conflict with the 'ui-kit' dependency. The policy requires temporarily halting the feature development, addressing the root issue in the dependency, and subsequently resuming and concluding the feature rollout. You are in charge of carrying out this coordinated sequence using the supplied **Incompatibility Manifest**. The end task is to produce cross-entity reports for both repositories to validate the resolution. **Incompatibility Manifest:** * **`react-dashboard` (Downstream Consumer):** * **Alert:** {description: 'Component crashing due to ui-kit incompatibility', file: 'src/components/NewFeature.tsx', severity: 'high', branch: 'feature/analytics-chart'} * **Feature:** {issue_title: 'Feature: New analytics chart', issue_body: '', branch: 'feature/analytics-chart', pr_title: 'Feature: New analytics chart', pr_body: 'This PR completes the analytics chart feature after the upstream fix.'} * **Code:** {initial_commit: 'feat: Initial analytics chart structure', final_commit: 'fix: Update component to support new ui-kit version', author: 'ui-developer'} * **`ui-kit` (Upstream Dependency):** * **Bug:** {issue_title: 'Bug: Prop validation fails in Card component', issue_body: 'The Card component prop validation is too strict, causing crashes in downstream consumers.', assignee: 'ui-dev'} * **Code:** {branch: 'fix/prop-validation', commit_message: 'fix: Add backward compatibility for Card props', pr_title: 'fix: Prop validation', pr_body: 'This PR relaxes prop validation for backward compatibility.', author: 'ui-dev'}",
        "actions": [
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "feature/analytics-chart",
                    "message": "feat: Initial analytics chart structure",
                    "author": "ui-developer"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "severity": "high",
                    "description": "Component crashing due to ui-kit incompatibility",
                    "file": "src/components/NewFeature.tsx",
                    "branch": "feature/analytics-chart"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "title": "Feature: New analytics chart",
                    "body": ""
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Bug: Prop validation fails in Card component",
                    "body": "The Card component prop validation is too strict, causing crashes in downstream consumers."
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 13,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "fix/prop-validation",
                    "message": "fix: Add backward compatibility for Card props",
                    "author": "ui-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "fix: Prop validation",
                    "body": "This PR relaxes prop validation for backward compatibility.",
                    "head_branch": "fix/prop-validation",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 13
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 12,
                    "assignees": [
                        "ui-developer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "feature/analytics-chart",
                    "message": "fix: Update component to support new ui-kit version",
                    "author": "ui-developer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "title": "Feature: New analytics chart",
                    "body": "This PR completes the analytics chart feature after the upstream fix.",
                    "head_branch": "feature/analytics-chart",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 11,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 12
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "alert_number": 10
                },
            },
            {
                "name": "GetCrossEntityReport",
                "arguments": {
                    "repo_name": "react-dashboard"
                },
            },
            {
                "name": "GetCrossEntityReport",
                "arguments": {
                    "repo_name": "ui-kit"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "react-dashboard",
                        "open_issues": 0,
                        "merged_prs": 1,
                        "recent_commits": 2,
                        "open_alerts": 0,
                        "last_deployment": "none",
                        "report_date": "2025-08-26"
                    }
                },
                {
                    "status": "ok",
                    "data": {
                        "repo": "ui-kit",
                        "open_issues": 0,
                        "merged_prs": 1,
                        "recent_commits": 1,
                        "open_alerts": 0,
                        "last_deployment": "none",
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_602",
        "instruction": "Your main strategic role is to oversee the reaction to a key vulnerability in 'common-lib', ensuring that all impacted repositories adhere to the company's **Staggered Security Patching Protocol**. This protocol necessitates a transparent and verifiable record of patching procedures, with a central epic overseeing the entire project and specific tasks for each affected repository based on their tier. You are tasked with managing this process with the help of the following **Patching Manifest**. The ultimate output is a collection of health summaries for the patched repositories to act as the formal documentation of policy adherence. **Patching Manifest: common-lib Vulnerability** * **Main Epic (Tracked in 'security-scanner'):** {title: 'URGENT: Patch common-lib vulnerability', body: 'Main epic to track patching of common-lib across all services.', labels: ['security', 'vulnerability', 'epic'], assignee: 'tech-lead-tara'} * **Tier 1 Service (`security-scanner`):** * **Issue:** {title: '[Patch] Upgrade common-lib in security-scanner', body: 'Sub-task to track patching of common-lib in the security-scanner repository.', labels: ['security', 'patch'], assignee: 'security-group'} * **Code:** {branch: 'hotfix/sec-lib-patch', commit_message: 'fix: Upgrade common-lib to v1.5.1', author: 'security-group'} * **PR:** {title: 'fix(deps): Upgrade common-lib', body: 'This PR upgrades the vulnerable common-lib dependency to a patched version.'} * **Release:** {version: 'v0.5.1', description: 'Security patch release.'} * **Deployment:** {environment: 'production'} * **Tier 2 Service (`ui-kit`):** * **Issue:** {title: '[Patch] Upgrade common-lib in ui-kit', body: 'Sub-task to track patching of common-lib in the ui-kit repository.', labels: ['security', 'patch'], assignee: 'ui-dev'} * **Code:** {branch: 'hotfix/ui-lib-patch', commit_message: 'fix: Upgrade common-lib to v1.5.1', author: 'ui-dev'} * **PR:** {title: 'fix(deps): Upgrade common-lib', body: 'This PR upgrades the vulnerable common-lib dependency to a patched version.'} * **Release:** {version: 'v3.2.1', description: 'Security patch release.'} * **Deployment:** {environment: 'staging'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "URGENT: Patch common-lib vulnerability",
                    "body": "Main epic to track patching of common-lib across all services.",
                    "labels": [
                        "security",
                        "vulnerability",
                        "epic"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "[Patch] Upgrade common-lib in security-scanner",
                    "body": "Sub-task to track patching of common-lib in the security-scanner repository.",
                    "labels": [
                        "security",
                        "patch"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "hotfix/sec-lib-patch",
                    "message": "fix: Upgrade common-lib to v1.5.1",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "fix(deps): Upgrade common-lib",
                    "body": "This PR upgrades the vulnerable common-lib dependency to a patched version.",
                    "head_branch": "hotfix/sec-lib-patch",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "security-scanner",
                    "version": "v0.5.1",
                    "description": "Security patch release."
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "security-scanner",
                    "environment": "production"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "[Patch] Upgrade common-lib in ui-kit",
                    "body": "Sub-task to track patching of common-lib in the ui-kit repository.",
                    "labels": [
                        "security",
                        "patch"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 14,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "hotfix/ui-lib-patch",
                    "message": "fix: Upgrade common-lib to v1.5.1",
                    "author": "ui-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "fix(deps): Upgrade common-lib",
                    "body": "This PR upgrades the vulnerable common-lib dependency to a patched version.",
                    "head_branch": "hotfix/ui-lib-patch",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 11,
                    "issue_number": 14
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
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 14
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "ui-kit",
                    "version": "v3.2.1",
                    "description": "Security patch release."
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "ui-kit",
                    "environment": "staging"
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "ui-kit"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "security-scanner",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                },
                {
                    "status": "ok",
                    "data": {
                        "repo": "ui-kit",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_10002",
        "instruction": "Your assignment is to handle the **Documentation Update Policy** for the 'infra-terraform' repository. The policy stipulates that all documentation modifications are to be formally tracked through an issue and carried out via a merged pull request. It is essential to use the supplied **Doc Manifest** to generate the necessary artifacts. Your final task is to provide a list of commits for the relevant branch, serving as an audit log. **Doc Manifest:** * **Issue:** {title: 'Docs: Add guide for new RDS module', body: 'Tracking issue for creating the RDS module documentation.', labels: ['documentation'], assignee: 'platform-team'} * **Implementation:** {branch: 'docs/rds-guide', commit_message: 'docs: Add usage guide for the new RDS module', author: 'platform-team'} * **PR:** {title: 'Docs: RDS Module Guide', body: 'This PR adds the new RDS module guide.'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "Docs: Add guide for new RDS module",
                    "body": "Tracking issue for creating the RDS module documentation.",
                    "labels": [
                        "documentation"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 12,
                    "assignees": [
                        "platform-team"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "docs/rds-guide",
                    "message": "docs: Add usage guide for the new RDS module",
                    "author": "platform-team"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "Docs: RDS Module Guide",
                    "body": "This PR adds the new RDS module guide.",
                    "head_branch": "docs/rds-guide",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 12
                },
            },
            {
                "name": "ListCommitsByBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "docs/rds-guide"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": [
                        {
                            "commit_id": "1c2fef47d1cf",
                            "repo": "infra-terraform",
                            "branch": "docs/rds-guide",
                            "message": "docs: Add usage guide for the new RDS module",
                            "author": "platform-team",
                            "timestamp": "2025-08-26",
                            "report_date": "2025-08-26"
                        }
                    ]
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_20002",
        "instruction": "Your task is to coordinate the **Documentation Update Policy** for the 'react-dashboard' repository. In accordance with the policy, every change to documentation requires formal tracking via an issue and should be executed through a merged pull request. You need to utilize the provided **Doc Manifest** to construct the necessary deliverables. Your ultimate goal is to compile a list of commits for the branch as an audit record. **Doc Manifest:** * **Issue:** {title: 'Docs: Update README with new setup instructions', body: 'The README.md is outdated and needs to be updated with the new project setup instructions.', labels: ['documentation'], assignee: 'ui-developer'} * **Implementation:** {branch: 'docs/readme-update', commit_message: 'docs: Update README with new setup instructions', pr_title: 'Docs: Update README', pr_body: 'This PR updates the README file.', author: 'ui-developer'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "title": "Docs: Update README with new setup instructions",
                    "body": "The README.md is outdated and needs to be updated with the new project setup instructions.",
                    "labels": [
                        "documentation"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 12,
                    "assignees": [
                        "ui-developer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "docs/readme-update",
                    "message": "docs: Update README with new setup instructions",
                    "author": "ui-developer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "title": "Docs: Update README",
                    "body": "This PR updates the README file.",
                    "head_branch": "docs/readme-update",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 12
                },
            },
            {
                "name": "ListCommitsByBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "docs/readme-update"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": [
                        {
                            "commit_id": "80fc79c09e51",
                            "repo": "react-dashboard",
                            "branch": "docs/readme-update",
                            "message": "docs: Update README with new setup instructions",
                            "author": "ui-developer",
                            "timestamp": "2025-08-26",
                            "report_date": "2025-08-26"
                        }
                    ]
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_705",
        "instruction": "The principal strategic goal is to manage the establishment of the new 'notification-service' repository, ensuring it adheres completely to the company's **New Service Onboarding and Governance Policy**. This policy specifies that new services must be both technically bootstrapped and meet initial governance and security compliance criteria before their initial release. It is your duty to handle this procedure using the specified **Onboarding Manifest**. The final output required is a health summary of the repository to validate its compliant status. **Onboarding Manifest:** * **Repository:** {name: 'notification-service', description: 'Centralized service for handling user notifications.', private: True} * **Governance:** * **Commits:** [{message: 'docs: Add MIT License', author: 'docs-sophia'}, {message: 'docs: Add SECURITY.md policy', author: 'docs-sophia'}] * **Ops Issue:** {title: 'ops: Configure main branch protection rules', body: 'Tracking issue for branch protection setup as per governance policy.', labels: ['ops', 'governance'], assignee: 'infra-lead'} * **Security Remediation:** * **Alert:** {severity: 'medium', description: 'Default template includes outdated dependency: common-lib v1.2.3', file: 'package.json', branch: 'main'} * **Issue:** {title: 'fix: Update outdated dependency common-lib', body: 'Tracking issue to update the vulnerable common-lib dependency.', labels: ['security', 'dependency'], assignee: 'infra-lead'} * **Code:** {branch: 'fix/update-common-lib', commit_message: 'fix: Upgrade common-lib to v1.2.4', author: 'infra-lead'} * **PR:** {title: 'fix(deps): Upgrade common-lib to v1.2.4', body: 'PR to upgrade outdated common-lib dependency to v1.2.4.'} * **Release:** {version: 'v0.1.0', description: 'Initial compliant release.'}",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "notification-service",
                    "description": "Centralized service for handling user notifications.",
                    "private": true
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "notification-service",
                    "branch": "main",
                    "message": "docs: Add MIT License",
                    "author": "docs-sophia"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "notification-service",
                    "branch": "main",
                    "message": "docs: Add SECURITY.md policy",
                    "author": "docs-sophia"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "title": "ops: Configure main branch protection rules",
                    "body": "Tracking issue for branch protection setup as per governance policy.",
                    "labels": [
                        "ops",
                        "governance"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "issue_number": 12,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "notification-service",
                    "severity": "medium",
                    "description": "Default template includes outdated dependency: common-lib v1.2.3",
                    "file": "package.json",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "title": "fix: Update outdated dependency common-lib",
                    "body": "Tracking issue to update the vulnerable common-lib dependency.",
                    "labels": [
                        "security",
                        "dependency"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "issue_number": 13,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "notification-service",
                    "branch": "fix/update-common-lib",
                    "message": "fix: Upgrade common-lib to v1.2.4",
                    "author": "infra-lead"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "notification-service",
                    "title": "fix(deps): Upgrade common-lib to v1.2.4",
                    "body": "PR to upgrade outdated common-lib dependency to v1.2.4.",
                    "head_branch": "fix/update-common-lib",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "notification-service",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "issue_number": 13
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "notification-service",
                    "alert_number": 10
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "notification-service",
                    "version": "v0.1.0",
                    "description": "Initial compliant release."
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "notification-service"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "notification-service",
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_905",
        "instruction": "Your task is to implement the **Quarterly Performance Initiative Policy** for the 'nlp-models' repository. This policy dictates that known performance bottlenecks should be tracked through a main epic and a specific sub-task for addressing the issue. All code enhancements need to be integrated successfully via a pull request. You are accountable for orchestrating this process for the recognized 'High memory usage during training' bottleneck using the detailed **Initiative Manifest**. What you need to deliver is the repository's activity dashboard to verify the policy has been effectively implemented. **Initiative Manifest: Q3 Performance** * **Epic:** {title: 'Q3 Performance Initiative', body: '', assignee: 'tech-lead-tara'} * **Remediation Task:** * **Issue:** {title: 'Task: High memory usage during training', body: '', assignee: 'ml-engineer'} * **Implementation:** {branch: 'perf/memory-tuning', author: 'ml-engineer', commit_message: 'perf: Reduce memory footprint via gradient accumulation'} * **PR:** {title: 'perf: Optimize memory usage', body: ''}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "Q3 Performance Initiative",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "assignees": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "Task: High memory usage during training",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 13,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "nlp-models",
                    "branch": "perf/memory-tuning",
                    "message": "perf: Reduce memory footprint via gradient accumulation",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "perf: Optimize memory usage",
                    "body": "",
                    "head_branch": "perf/memory-tuning",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 13
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "nlp-models"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "nlp-models",
                        "commits_count": 1,
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_501",
        "instruction": "Your strategic responsibility is to manage the complete lifecycle of a feature deployment and its urgent rollback within the 'acme-webapp' repository, ensuring it fully complies with the company's **Multi-Stage Incident Resolution Policy**. This policy requires a documented, auditable process for both the initial feature launch and the remedial actions taken upon identifying a critical issue, including merging a revert PR. You are tasked with coordinating this two-step procedure using the provided **Incident Manifest**. Your ultimate deliverable is the health summary of the repository, confirming the incident's final status. **Incident Manifest: Profile Caching Feature** * **Stage 1: Feature Rollout** * **Issue:** {title: 'Implement User Profile Caching', body: 'Tracks the full lifecycle of the user profile caching feature.', labels: ['feature'], assignee: 'maya-w'} * **Code:** {branch: 'feature/profile-caching', commit_message: 'feat: Add user profile caching logic', author: 'dev-sue'} * **PR:** {title: 'Feature: User Profile Caching', body: 'PR to implement the user profile caching feature as per requirements.', reviewers: ['qa-mike']} * **Release:** {version: 'v1.1.0', description: 'Release with user profile caching.'} * **Deployment:** {environment: 'production'} * **Stage 2: Emergency Rollback** * **Alert:** {severity: 'critical', description: 'Post-release discovery: Caching logic exposes sensitive user data.', file: 'src/app.py', branch: 'main'} * **Issue:** {title: 'EMERGENCY: Rollback v1.1.0 due to critical vulnerability', body: 'Issue to track the emergency rollback of the profile caching feature.', labels: ['security', 'bug'], assignee: 'security-group'} * **Code:** {branch: 'revert/profile-caching', commit_message: 'revert: Revert user profile caching feature', author: 'security-group'} * **PR:** {title: 'Revert: User Profile Caching', body: 'Reverting the caching feature due to a critical vulnerability.'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Implement User Profile Caching",
                    "body": "Tracks the full lifecycle of the user profile caching feature.",
                    "labels": [
                        "feature"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12,
                    "assignees": [
                        "maya-w"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature/profile-caching",
                    "message": "feat: Add user profile caching logic",
                    "author": "dev-sue"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Feature: User Profile Caching",
                    "body": "PR to implement the user profile caching feature as per requirements.",
                    "head_branch": "feature/profile-caching",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10,
                    "reviewers": [
                        "qa-mike"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "version": "v1.1.0",
                    "description": "Release with user profile caching."
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "environment": "production"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "severity": "critical",
                    "description": "Post-release discovery: Caching logic exposes sensitive user data.",
                    "file": "src/app.py",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "EMERGENCY: Rollback v1.1.0 due to critical vulnerability",
                    "body": "Issue to track the emergency rollback of the profile caching feature.",
                    "labels": [
                        "security",
                        "bug"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 13,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "revert/profile-caching",
                    "message": "revert: Revert user profile caching feature",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Revert: User Profile Caching",
                    "body": "Reverting the caching feature due to a critical vulnerability.",
                    "head_branch": "revert/profile-caching",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 11,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 13
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "acme-webapp"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "acme-webapp",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 1,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_203",
        "instruction": "As part of the security team, your goal is to handle the company's **Vulnerability Triage and Full Remediation Cycle Policy** for the 'security-scanner' repository. The policy specifies that high-priority vulnerabilities must be comprehensively tracked as issues, and that the most severe vulnerabilities should be fully addressed through a reviewed and merged pull request. You are tasked with coordinating this process for the vulnerabilities outlined in the provided **Triage Manifest**. Your final goal is the repository's activity dashboard to verify the policy has been appropriately completed. **Triage Manifest:** * **Vulnerability 1 (Critical):** * **Action:** Remediate * **Details:** Unsafe Deserialization * **Issue:** {title: 'Remediate Critical: Unsafe Deserialization', body: 'Tracking issue for the unsafe deserialization vulnerability.', labels: ['security', 'critical-risk'], assignee: 'security-group'} * **Code:** {branch: 'hotfix/critical-deserialization', base_branch: 'main', commits: [{message: 'fix: Initial patch for unsafe deserialization', author: 'security-group'}, {message: 'test: Add unit tests for deserialization fix', author: 'qa-erin'}, {message: 'docs: Update security docs regarding deserialization', author: 'docs-sophia'}]} * **PR:** {title: 'Fix: Unsafe Deserialization', body: 'Complete fix for the critical deserialization vulnerability.', reviewers: ['tech-lead-tara']} * **Vulnerability 2 (High):** * **Action:** Track * **Details:** Buffer Overflow * **Issue:** {title: 'Remediate High: Buffer Overflow', body: 'Tracking issue for the potential buffer overflow vulnerability.', labels: ['security', 'high-risk'], assignee: 'perf-nathan'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Remediate Critical: Unsafe Deserialization",
                    "body": "Tracking issue for the unsafe deserialization vulnerability.",
                    "labels": [
                        "security",
                        "critical-risk"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Remediate High: Buffer Overflow",
                    "body": "Tracking issue for the potential buffer overflow vulnerability.",
                    "labels": [
                        "security",
                        "high-risk"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "perf-nathan"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "hotfix/critical-deserialization",
                    "message": "fix: Initial patch for unsafe deserialization",
                    "author": "security-group"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "hotfix/critical-deserialization",
                    "message": "test: Add unit tests for deserialization fix",
                    "author": "qa-erin"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "hotfix/critical-deserialization",
                    "message": "docs: Update security docs regarding deserialization",
                    "author": "docs-sophia"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Fix: Unsafe Deserialization",
                    "body": "Complete fix for the critical deserialization vulnerability.",
                    "head_branch": "hotfix/critical-deserialization",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "security-scanner",
                        "commits_count": 3,
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_1001",
        "instruction": "Your task is to handle the **Cross-Team Security Collaboration Policy** in response to a critical vulnerability. This policy necessitates a coordinated action: the vulnerability must be resolved in the affected repository ('k8s-monitoring'), and a preventative detection rule should be concurrently added to the 'security-scanner'. Ensure all work is formally documented and results in patched or upgraded states for both repositories. Use the provided **Collaboration Manifest** to manage this process. Your final deliverable consists of a set of activity dashboards for both repositories to confirm the successful execution of the policy. **Collaboration Manifest:** * **Vulnerability:** {description: 'Insecure Grafana dashboard permissions', file: 'kubernetes/grafana.yaml', severity: 'critical', branch: 'main'} * **Remediation Work (`k8s-monitoring`):** * **Issue:** {title: 'Remediate insecure Grafana dashboard permissions', body: '', assignee: 'infra-lead'} * **Code:** {branch: 'fix/grafana-perms', commit_message: 'fix: Restrict Grafana dashboard access', author: 'infra-lead'} * **PR:** {title: 'fix: Harden Grafana permissions', body: '', reviewers: ['security-group']} * **Prevention Work (`security-scanner`):** * **Issue:** {title: 'Add detection for insecure Grafana permissions', body: '', assignee: 'security-group'} * **Code:** {branch: 'feature/grafana-rule', commit_message: 'feat: Add Grafana permission scanner rule', author: 'security-group'} * **PR:** {title: 'feat: Add Grafana permission rule', body: ''} * **Release:** {version: 'v0.8.0', description: 'Adds new Grafana security rule.'}",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "severity": "critical",
                    "description": "Insecure Grafana dashboard permissions",
                    "file": "kubernetes/grafana.yaml",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Remediate insecure Grafana dashboard permissions",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 12,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Add detection for insecure Grafana permissions",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "feature/grafana-rule",
                    "message": "feat: Add Grafana permission scanner rule",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "feat: Add Grafana permission rule",
                    "body": "",
                    "head_branch": "feature/grafana-rule",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "security-scanner",
                    "version": "v0.8.0",
                    "description": "Adds new Grafana security rule."
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "fix/grafana-perms",
                    "message": "fix: Restrict Grafana dashboard access",
                    "author": "infra-lead"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "fix: Harden Grafana permissions",
                    "body": "",
                    "head_branch": "fix/grafana-perms",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 11,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 11,
                    "reviewers": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 12
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "alert_number": 10
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "k8s-monitoring",
                        "commits_count": 1,
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                },
                {
                    "status": "ok",
                    "data": {
                        "repo": "security-scanner",
                        "commits_count": 1,
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_7004",
        "instruction": "Your task is to manage the **Cross-Repository Dependency Patching Policy**. A regression in 'utils-js' is impacting 'acme-webapp'. The policy demands a coordinated correction, initiating with the upstream dependency and followed by an update in the downstream consumer. Utilize the provided **Patching Manifest** to bring both repositories into a compliant, resolved condition. Your final deliverable is a series of cross-entity reports for both repositories to verify the complete resolution. **Patching Manifest:** * **`utils-js` (Upstream Fix):** * **Issue:** {title: 'Regression: Negative currency formatting', body: 'The previous fix was insufficient and a regression has been reported.', labels: ['bug', 'regression'], assignee: 'ryan-dev'} * **Code:** {branch: 'fix/currency-regression-1.0.3', commit_message: 'fix: Add robust handling for negative currency values', author: 'ryan-dev'} * **PR:** {title: 'Fix: Regression on Negative Currency Formatting', body: 'This PR provides a more robust fix for the regression.'} * **Release:** {version: 'v1.0.3', description: 'Robust fix for currency formatting regression.'} * **`acme-webapp` (Downstream Update):** * **Issue:** {title: 'Upstream Bug: Data Corruption from utils-js', body: 'Tracking downstream impact of the regression in utils-js.', labels: ['bug', 'dependency'], assignee: 'maya-w'} * **Code:** {branch: 'chore/update-utils-js-1.0.3', commit_message: 'Chore: Update utils-js to v1.0.3', author: 'maya-w'} * **PR:** {title: 'Chore: Update utils-js to v1.0.3', body: 'Integrating upstream fix to resolve data corruption.'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Upstream Bug: Data Corruption from utils-js",
                    "body": "Tracking downstream impact of the regression in utils-js.",
                    "labels": [
                        "bug",
                        "dependency"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12,
                    "assignees": [
                        "maya-w"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "Regression: Negative currency formatting",
                    "body": "The previous fix was insufficient and a regression has been reported.",
                    "labels": [
                        "bug",
                        "regression"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 13,
                    "assignees": [
                        "ryan-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "utils-js",
                    "branch": "fix/currency-regression-1.0.3",
                    "message": "fix: Add robust handling for negative currency values",
                    "author": "ryan-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "Fix: Regression on Negative Currency Formatting",
                    "head_branch": "fix/currency-regression-1.0.3",
                    "base_branch": "master",
                    "body": "This PR provides a more robust fix for the regression."
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 13
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "utils-js",
                    "version": "v1.0.3",
                    "description": "Robust fix for currency formatting regression."
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "chore/update-utils-js-1.0.3",
                    "message": "Chore: Update utils-js to v1.0.3",
                    "author": "maya-w"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Chore: Update utils-js to v1.0.3",
                    "head_branch": "chore/update-utils-js-1.0.3",
                    "base_branch": "main",
                    "body": "Integrating upstream fix to resolve data corruption."
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 11,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12
                },
            },
            {
                "name": "GetCrossEntityReport",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "GetCrossEntityReport",
                "arguments": {
                    "repo_name": "utils-js"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "acme-webapp",
                        "open_issues": 0,
                        "merged_prs": 1,
                        "recent_commits": 1,
                        "open_alerts": 0,
                        "last_deployment": "none",
                        "report_date": "2025-08-26"
                    }
                },
                {
                    "status": "ok",
                    "data": {
                        "repo": "utils-js",
                        "open_issues": 0,
                        "merged_prs": 1,
                        "recent_commits": 1,
                        "open_alerts": 0,
                        "last_deployment": "none",
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_4004",
        "instruction": "Your task is to handle the **Post-Incident Analysis Policy** for the 'security-scanner' repository. This policy mandates a comprehensive and verifiable resolution process for security incidents, in which various related alerts are combined and monitored through a single issue, then resolved with one pull request. You are responsible for coordinating this process using the designated **Incident Manifest**. Your final output is a report detailing all security alerts resolved in the repository to certify adherence to the process. **Incident Manifest:** * **Alerts to Remediate:** [ {severity: 'high', description: 'Insecure dependency in Cargo.toml', file: 'Cargo.toml', branch: 'main'}, {severity: 'low', description: 'Unused variable in scanner.rs', file: 'src/scanner.rs', branch: 'main'} ] * **Consolidated Tracking Issue:** {title: 'Security: Remediate multiple alerts', body: '', assignee: 'security-group'} * **Consolidated Fix:** * **Branch:** 'fix/multi-alert-remediation' * **Commit:** {message: 'fix: Update dependency and remove unused variable', author: 'security-group'} * **PR:** {title: 'fix: Remediate multiple alerts', body: ''}",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "severity": "high",
                    "description": "Insecure dependency in Cargo.toml",
                    "file": "Cargo.toml",
                    "branch": "main"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "severity": "low",
                    "description": "Unused variable in scanner.rs",
                    "file": "src/scanner.rs",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Security: Remediate multiple alerts",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "fix/multi-alert-remediation",
                    "message": "fix: Update dependency and remove unused variable",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "fix: Remediate multiple alerts",
                    "body": "",
                    "head_branch": "fix/multi-alert-remediation",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "alert_number": 10
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "alert_number": 11
                },
            },
            {
                "name": "GetResolvedSecurityAlerts",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": [
                        {
                            "alert_id": "ALERT_security-scanner_56ed3e11",
                            "severity": "high",
                            "state": "fixed",
                            "resolved_at": "2025-08-26",
                            "description": "Insecure dependency in Cargo.toml"
                        },
                        {
                            "alert_id": "ALERT_security-scanner_a69022dd",
                            "severity": "low",
                            "state": "fixed",
                            "resolved_at": "2025-08-26",
                            "description": "Unused variable in scanner.rs"
                        }
                    ]
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_804",
        "instruction": "Your key strategic goal is to implement the **Quarterly Tech Debt Initiative Policy** for the 'security-scanner' repository. This policy requires that a primary epic oversees all planned refactoring activities for the quarter, with each tech debt task executed and incorporated sequentially via its own distinct issue and pull request. You are responsible for ensuring the repository is updated to showcase the completion of this process, utilizing the provided **Tech Debt Manifest**. Your final deliverable is the repository's activity dashboard to verify all tech debt tasks for the quarter have been completed. **Tech Debt Manifest (Q3):** * **Main Epic:** {title: 'Q3 Tech Debt Paydown', body: 'Main epic to track all Q3 tech debt sub-tasks.', labels: ['tech-debt', 'epic'], assignee: 'tech-lead-tara'} * **Work Items:** [ { name: 'Refactor Parser', issue: {title: 'Refactor Parser Module', body: 'Sub-task to track the refactoring of the parser module.', labels: ['tech-debt', 'refactor'], assignee: 'security-group'}, code: {branch: 'refactor/parser', commit_message: 'refactor: Simplify parser logic', author: 'security-group'}, pr: {title: 'refactor: Parser Module', body: 'PR to implement the parser refactor.', reviewers: ['tech-lead-tara']} }, { name: 'Update Dependencies', issue: {title: 'Update Deprecated Dependencies', body: 'Sub-task to track the update of deprecated dependencies.', labels: ['tech-debt', 'chore'], assignee: 'security-group'}, code: {branch: 'chore/update-deps', commit_message: 'chore: Update all dependencies to latest stable', author: 'security-group'}, pr: {title: 'chore: Update Dependencies', body: 'PR to update all dependencies to their latest stable versions.', reviewers: ['tech-lead-tara']} }, { name: 'Remove Handlers', issue: {title: 'Remove Deprecated Handlers', body: 'Sub-task to track the removal of deprecated v1 handlers.', labels: ['tech-debt', 'refactor'], assignee: 'security-group'}, code: {branch: 'refactor/remove-handlers', commit_message: 'refactor: Remove unused v1 handlers', author: 'security-group'}, pr: {title: 'refactor: Remove Deprecated Handlers', body: 'PR to remove the unused v1 handlers.', reviewers: ['tech-lead-tara']} } ]",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Q3 Tech Debt Paydown",
                    "body": "Main epic to track all Q3 tech debt sub-tasks.",
                    "labels": [
                        "tech-debt",
                        "epic"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Refactor Parser Module",
                    "body": "Sub-task to track the refactoring of the parser module.",
                    "labels": [
                        "tech-debt",
                        "refactor"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "refactor/parser",
                    "message": "refactor: Simplify parser logic",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "refactor: Parser Module",
                    "body": "PR to implement the parser refactor.",
                    "head_branch": "refactor/parser",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Update Deprecated Dependencies",
                    "body": "Sub-task to track the update of deprecated dependencies.",
                    "labels": [
                        "tech-debt",
                        "chore"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 14,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "chore/update-deps",
                    "message": "chore: Update all dependencies to latest stable",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "chore: Update Dependencies",
                    "body": "PR to update all dependencies to their latest stable versions.",
                    "head_branch": "chore/update-deps",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 11,
                    "issue_number": 14
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 11,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 14
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Remove Deprecated Handlers",
                    "body": "Sub-task to track the removal of deprecated v1 handlers.",
                    "labels": [
                        "tech-debt",
                        "refactor"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 15,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "refactor/remove-handlers",
                    "message": "refactor: Remove unused v1 handlers",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "refactor: Remove Deprecated Handlers",
                    "body": "PR to remove the unused v1 handlers.",
                    "head_branch": "refactor/remove-handlers",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 12,
                    "issue_number": 15
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 12,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 12
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 15
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "security-scanner",
                        "commits_count": 3,
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_704",
        "instruction": "Your primary strategic goal is to oversee the handling of a zero-day incident in the 'security-scanner' repository, making sure it is fully compliant with the company's **Zero-Day Vulnerability Response Protocol**. This urgent protocol requires a clear and traceable record for both the emergency patch and the necessary public announcement. You are accountable for coordinating this process using the provided **Zero-Day Manifest**. Your final output is the repository health summary, which will serve as the official documentation of policy adherence. **Zero-Day Manifest: YAML Parser RCE** * **Incident Alert:** {severity: 'critical', description: 'Zero-Day RCE Vulnerability in YAML Parser', file: 'src/parser.rs', branch: 'main'} * **Main Tracking Epic:** {title: 'INCIDENT: Zero-Day RCE in YAML Parser', body: 'Main epic to track the zero-day incident response and remediation.', labels: ['security', 'incident', 'epic'], assignee: 'security-group'} * **Workstreams:** [ { name: 'Patch Development', issue: {title: 'ACTION: Develop Patch for Zero-Day RCE', body: 'Sub-task to develop the emergency patch for the YAML RCE.', labels: ['security', 'bug'], assignee: 'security-group'}, code: {branch: 'hotfix/zero-day-rce', commit_message: 'fix: Add validation to YAML parser to prevent RCE', author: 'security-group'}, pr: {title: 'fix: Patch for Zero-Day RCE', body: 'Emergency patch for the YAML parser RCE vulnerability.'} }, { name: 'Public Communication', issue: {title: 'ACTION: Write Security Advisory for Zero-Day', body: 'Sub-task to write and publish the official security advisory for the YAML RCE.', labels: ['security', 'documentation'], assignee: 'docs-sophia'}, code: {branch: 'docs/zero-day-advisory', commit_message: 'docs: Add security advisory for YAML RCE', author: 'docs-sophia'}, pr: {title: 'docs: Publish Security Advisory for Zero-Day', body: 'PR containing the new security advisory document.'} } ]",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "severity": "critical",
                    "description": "Zero-Day RCE Vulnerability in YAML Parser",
                    "file": "src/parser.rs",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "INCIDENT: Zero-Day RCE in YAML Parser",
                    "body": "Main epic to track the zero-day incident response and remediation.",
                    "labels": [
                        "security",
                        "incident",
                        "epic"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "ACTION: Write Security Advisory for Zero-Day",
                    "body": "Sub-task to write and publish the official security advisory for the YAML RCE.",
                    "labels": [
                        "security",
                        "documentation"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "docs-sophia"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "ACTION: Develop Patch for Zero-Day RCE",
                    "body": "Sub-task to develop the emergency patch for the YAML RCE.",
                    "labels": [
                        "security",
                        "bug"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 14,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "hotfix/zero-day-rce",
                    "message": "fix: Add validation to YAML parser to prevent RCE",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "fix: Patch for Zero-Day RCE",
                    "body": "Emergency patch for the YAML parser RCE vulnerability.",
                    "head_branch": "hotfix/zero-day-rce",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 14
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 14
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "alert_number": 10
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "docs/zero-day-advisory",
                    "message": "docs: Add security advisory for YAML RCE",
                    "author": "docs-sophia"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "docs: Publish Security Advisory for Zero-Day",
                    "body": "PR containing the new security advisory document.",
                    "head_branch": "docs/zero-day-advisory",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 11,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "security-scanner",
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_20004",
        "instruction": "Your task is to implement the **New Project Bootstrap Policy** for the 'user-preferences-api'. This policy guarantees all new projects begin with a standardized set of fundamental artifacts for tracking, security, and deployment preparedness. You must use the provided **Bootstrap Manifest** to establish all required elements. Your final output is a compilation of open issues to verify that the initial setup tasks are accurately recorded. **Compliance Specification:** The end state must demonstrate that the repository was established as 'private'. It must include an initial commit and two 'open' issues for initial setup tasks. **Bootstrap Manifest:** * **Repository:** {name: 'user-preferences-api', description: 'Service for managing user preferences and settings.', private: True} * **Initial Commit:** {author: 'infra-lead', message: 'Initial commit from service template'} * **Issue 1:** {title: 'Setup CI/CD pipeline', body: 'Configure the standard CI/CD pipeline for the new service.', labels: ['setup', 'ci-cd'], assignee: 'infra-lead'} * **Issue 2:** {title: 'Add basic authentication endpoints', body: 'Implement initial authentication endpoints as per the security spec.', labels: ['feature', 'auth'], assignee: 'server-main'}",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "user-preferences-api",
                    "description": "Service for managing user preferences and settings.",
                    "private": true
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "user-preferences-api",
                    "branch": "main",
                    "message": "Initial commit from service template",
                    "author": "infra-lead"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "user-preferences-api",
                    "title": "Setup CI/CD pipeline",
                    "body": "Configure the standard CI/CD pipeline for the new service.",
                    "labels": [
                        "setup",
                        "ci-cd"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "user-preferences-api",
                    "issue_number": 12,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "user-preferences-api",
                    "title": "Add basic authentication endpoints",
                    "body": "Implement initial authentication endpoints as per the security spec.",
                    "labels": [
                        "feature",
                        "auth"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "user-preferences-api",
                    "issue_number": 13,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "GetOpenIssues",
                "arguments": {
                    "repo_name": "user-preferences-api"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": [
                        {
                            "issue_id": "ISSUE_user-preferences-api_3ded9583",
                            "title": "Setup CI/CD pipeline",
                            "state": "open",
                            "assignees": [
                                "infra-lead"
                            ],
                            "labels": [
                                "setup",
                                "ci-cd"
                            ],
                            "created_at": "2025-08-26",
                            "report_date": "2025-08-26"
                        },
                        {
                            "issue_id": "ISSUE_user-preferences-api_537cd6a9",
                            "title": "Add basic authentication endpoints",
                            "state": "open",
                            "assignees": [
                                "server-main"
                            ],
                            "labels": [
                                "feature",
                                "auth"
                            ],
                            "created_at": "2025-08-26",
                            "report_date": "2025-08-26"
                        }
                    ]
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_7005",
        "instruction": "Your task is to handle the **Ecosystem Health Audit Policy**. This involves analyzing key repositories and aggregating the findings within a newly created repository. Utilize the provided **Audit Manifest** to ensure compliance with the repository's final state. Your final output should be a comprehensive report validating the creation and contents of the new repository. **Compliance Specification:** The final configuration must demonstrate that a new private repository, 'Ecosystem-Audit-Logs', has been established and filled. This repository should contain an initial setup commit and three 'open' issues, one corresponding to each audited repository. Each issue needs to be properly assigned and include the synthesized results of a risk and issue-aging analysis. **Audit Manifest:** * **New Repository:** {name: 'Ecosystem-Audit-Logs', description: 'Centralized repository for tracking automated ecosystem health audits.'} * **Initial Commit:** {author: 'infra-lead', message: 'Initial setup for automated health reporting and audit tracking.'} * **Audit Findings:** [ {repo_to_audit: 'security-scanner', issue: {title: 'Audit: security-scanner', body: 'Analysis results: Risk Score=0, Aging Issues=0.', labels: ['audit', 'security'], assignee: 'security-group'}}, {repo_to_audit: 'k8s-monitoring', issue: {title: 'Audit: k8s-monitoring', body: 'Analysis results: Risk Score=0, Aging Issues=0.', labels: ['audit', 'infra'], assignee: 'infra-lead'}}, {repo_to_audit: 'nlp-models', issue: {title: 'Audit: nlp-models', body: 'Analysis results: Risk Score=0, Aging Issues=0.', labels: ['audit', 'mlops'], assignee: 'ml-engineer'}} ]",
        "actions": [
            {
                "name": "GetRepositoryRiskScore",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "GetIssueAgingReport",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "GetRepositoryRiskScore",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "GetIssueAgingReport",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                },
            },
            {
                "name": "GetRepositoryRiskScore",
                "arguments": {
                    "repo_name": "nlp-models"
                },
            },
            {
                "name": "GetIssueAgingReport",
                "arguments": {
                    "repo_name": "nlp-models"
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "Ecosystem-Audit-Logs",
                    "private": true,
                    "description": "Centralized repository for tracking automated ecosystem health audits."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "Ecosystem-Audit-Logs",
                    "title": "Audit: security-scanner",
                    "body": "Analysis results: Risk Score=0, Aging Issues=0.",
                    "labels": [
                        "audit",
                        "security"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "Ecosystem-Audit-Logs",
                    "issue_number": 12,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "Ecosystem-Audit-Logs",
                    "title": "Audit: k8s-monitoring",
                    "body": "Analysis results: Risk Score=0, Aging Issues=0.",
                    "labels": [
                        "audit",
                        "infra"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "Ecosystem-Audit-Logs",
                    "issue_number": 13,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "Ecosystem-Audit-Logs",
                    "title": "Audit: nlp-models",
                    "body": "Analysis results: Risk Score=0, Aging Issues=0.",
                    "labels": [
                        "audit",
                        "mlops"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "Ecosystem-Audit-Logs",
                    "issue_number": 14,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "Ecosystem-Audit-Logs",
                    "branch": "main",
                    "message": "Initial setup for automated health reporting and audit tracking.",
                    "author": "infra-lead"
                },
            },
            {
                "name": "GenerateEndToEndReport",
                "arguments": {
                    "repo_name": "Ecosystem-Audit-Logs"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "Ecosystem-Audit-Logs",
                        "commits_count": 1,
                        "open_issues": 3,
                        "merged_prs": 0,
                        "open_alerts": 0,
                        "releases_count": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_5003",
        "instruction": "Your goal is to coordinate the **Alert Triage Policy** for the 'acme-webapp' repository. A new alert of low severity may be a false positive. The policy mandates a structured investigation and dismissal process involving tracking the investigation, creating a code comment through a pull request to suppress the alert, and resolving the original alert. Utilize the provided **Data Specification** to develop all necessary artifacts. Your concluding deliverable is a report detailing all resolved security alerts in the repository to audit the triage decision. **Data Specification:** * **Alert Details:** {description: 'Hardcoded timeout value', file: 'src/config.py', severity: 'low'} * **Tracking Issue:** {title: 'Investigate hardcoded timeout alert - False Positive', body: '', assignee: 'maya-w'} * **Code Artifacts:** {branch: 'chore/suppress-linter-warning', commit_message: 'chore: Suppress linter warning for timeout value', pr_title: 'chore: Suppress timeout warning', pr_body: '', author: 'maya-w'}",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "severity": "low",
                    "description": "Hardcoded timeout value",
                    "file": "src/config.py",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Investigate hardcoded timeout alert - False Positive",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12,
                    "assignees": [
                        "maya-w"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "chore/suppress-linter-warning",
                    "message": "chore: Suppress linter warning for timeout value",
                    "author": "maya-w"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "chore: Suppress timeout warning",
                    "body": "",
                    "head_branch": "chore/suppress-linter-warning",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "alert_number": 10
                },
            },
            {
                "name": "GetResolvedSecurityAlerts",
                "arguments": {
                    "repo_name": "acme-webapp"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": [
                        {
                            "alert_id": "ALERT_acme-webapp_a4e691ce",
                            "severity": "low",
                            "state": "fixed",
                            "resolved_at": "2025-08-26",
                            "description": "Hardcoded timeout value"
                        }
                    ]
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_3004",
        "instruction": "Your task is to handle the **New Team Member Onboarding Policy** for the 'ui-kit' repository. This policy guarantees that new developers, such as 'intern-emma', undertake a standard introductory assignment by resolving a tracked issue via a reviewed pull request to get accustomed to the contribution process. Utilize the provided **Onboarding Manifest** to generate all necessary documents. Your final requirement is the repository's activity dashboard to confirm the successful accomplishment of the onboarding task. **Compliance Specification:** The final outcome must demonstrate that a 'good first issue' was created and given to the new team member, and this issue must be 'closed'. The task should be implemented on a feature branch and 'merged' through a pull request that has been aptly reviewed. **Onboarding Manifest:** * **Issue:** {title: 'Good First Issue: Add accessibility labels to Button component', body: ''} * **New Team Member (Assignee/Author):** 'intern-emma' * **Reviewer:** 'design-lead' * **Code Artifacts:** {branch: 'feature/aria-labels', commit_message: 'feat: Add ARIA labels to Button component', pr_title: 'feat: Add accessibility labels', pr_body: ''}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Good First Issue: Add accessibility labels to Button component",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/aria-labels",
                    "message": "feat: Add ARIA labels to Button component",
                    "author": "intern-emma"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "feat: Add accessibility labels",
                    "body": "",
                    "head_branch": "feature/aria-labels",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "reviewers": [
                        "design-lead"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "ui-kit"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "ui-kit",
                        "commits_count": 1,
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_603",
        "instruction": "Your main strategic directive is to coordinate the lifecycle of a new feature for the 'ui-kit' repository, ensuring full adherence to the company's **Experiment-Driven Development Policy**. This policy dictates that new user-facing functionalities are developed behind a feature flag and that a separate issue monitors the experiment's analysis. You are charged with transitioning the repository to a state that aligns with the policy, utilizing the given manifest for the 'New Checkout Button' feature. Your final requirement is the repository's activity dashboard, which verifies the feature's release and the experiment's readiness for analysis. **Compliance Specification:** The final result must indicate that the development issue is 'closed' and the code 'merged' via a pull request encompassing all necessary commits. The separate issue for A/B test analysis must remain 'open'. A new release has to be published and deployed to production. **Experiment Manifest: New Checkout Button** * **Development Task:** {issue_title: 'Develop New Checkout Button', issue_body: 'Main tracking issue for the development of the new checkout button.', labels: ['feature', 'ui', 'epic'], assignee: 'ui-dev'} * **Analysis Task:** {issue_title: 'Analyze A/B Test Results for New Checkout Button', issue_body: 'Issue to track the analysis of the A/B test results.', labels: ['analytics', 'research'], assignee: 'ml-engineer'} * **Implementation:** * **Branch:** 'feature/checkout-button' * **Commits:** [{message: 'feat: Implement new checkout button UI', author: 'ui-dev'}, {message: 'feat: Add feature flag for A/B testing checkout button', author: 'ui-dev'}, {message: 'test: Add unit tests for new button and feature flag', author: 'qa-erin'}] * **Pull Request:** {title: 'Feature: New Checkout Button with A/B Test Flag', body: 'PR to release the new checkout button behind a feature flag for A/B testing.', reviewers: ['tech-lead-tara']} * **Release:** {version: 'v3.4.0', description: 'New Checkout Button with A/B Test'} * **Deployment:** {environment: 'production'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Develop New Checkout Button",
                    "body": "Main tracking issue for the development of the new checkout button.",
                    "labels": [
                        "feature",
                        "ui",
                        "epic"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Analyze A/B Test Results for New Checkout Button",
                    "body": "Issue to track the analysis of the A/B test results.",
                    "labels": [
                        "analytics",
                        "research"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 13,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/checkout-button",
                    "message": "feat: Implement new checkout button UI",
                    "author": "ui-dev"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/checkout-button",
                    "message": "feat: Add feature flag for A/B testing checkout button",
                    "author": "ui-dev"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/checkout-button",
                    "message": "test: Add unit tests for new button and feature flag",
                    "author": "qa-erin"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Feature: New Checkout Button with A/B Test Flag",
                    "body": "PR to release the new checkout button behind a feature flag for A/B testing.",
                    "head_branch": "feature/checkout-button",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "ui-kit",
                    "version": "v3.4.0",
                    "description": "New Checkout Button with A/B Test"
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "ui-kit",
                    "environment": "production"
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "ui-kit"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "ui-kit",
                        "commits_count": 3,
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_605",
        "instruction": "Your strategic goal is to handle the **Disaster Recovery Protocol** for the 'ui-kit' repository that has been marked as corrupted. This protocol involves the creation of a new, clean repository and the migration of essential work, ensuring a clear audit trail on both repositories. You are tasked with restoring the ecosystem to match the official **Recovery Specification** by utilizing the provided manifest. Your final task is to compile a list detailing the health summaries for both the old and new repositories to record the recovery operation's status. **Recovery Manifest:** * **Incident Tracking (`ui-kit`):** * **Alert:** {description: 'FATAL: Repository index corrupted; read-only mode enabled.', file: '.git/index', severity: 'critical'} * **Issue:** {title: 'DR: Plan migration to new repository', body: 'Main tracking issue for the disaster recovery plan and migration to ui-kit-recovered.', labels: ['disaster-recovery', 'ops'], assignee: 'infra-lead'} * **New Repository (`ui-kit-recovered`):** * **Configuration:** {name: 'ui-kit-recovered', description: 'Recovered version of ui-kit.', private: True} * **Ported Features:** [ {name: 'Theming Engine', issue: {title: '[Port] Re-implement Theming Engine', body: 'Port of theming engine to recovered repo.', labels: ['recovery', 'port'], assignee: 'ui-dev'}, code: {branch: 'feat/port-theming', commit_message: 'feat: Re-implement theming engine', author: 'ui-dev'}, pr: {title: 'feat: Port theming engine', body: 'PR to port the theming engine from the old repository.'}}, {name: 'Button Component', issue: {title: '[Port] Re-implement Button Component', body: 'Port of button component to recovered repo.', labels: ['recovery', 'port'], assignee: 'ui-dev'}, code: {branch: 'feat/port-button', commit_message: 'feat: Re-implement button component', author: 'ui-dev'}, pr: {title: 'feat: Port button component', body: 'PR to port the button component from the old repository.'}} ] * **Release:** {version: 'v4.0.0-recovered', description: 'Initial recovered release.', environment: 'production'}",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "ui-kit",
                    "severity": "critical",
                    "description": "FATAL: Repository index corrupted; read-only mode enabled.",
                    "file": ".git/index",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "DR: Plan migration to new repository",
                    "body": "Main tracking issue for the disaster recovery plan and migration to ui-kit-recovered.",
                    "labels": [
                        "disaster-recovery",
                        "ops"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "description": "Recovered version of ui-kit.",
                    "private": true
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "title": "[Port] Re-implement Theming Engine",
                    "body": "Port of theming engine to recovered repo.",
                    "labels": [
                        "recovery",
                        "port"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "issue_number": 13,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "branch": "feat/port-theming",
                    "message": "feat: Re-implement theming engine",
                    "author": "ui-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "title": "feat: Port theming engine",
                    "body": "PR to port the theming engine from the old repository.",
                    "head_branch": "feat/port-theming",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "issue_number": 13
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "title": "[Port] Re-implement Button Component",
                    "body": "Port of button component to recovered repo.",
                    "labels": [
                        "recovery",
                        "port"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "issue_number": 14,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "branch": "feat/port-button",
                    "message": "feat: Re-implement button component",
                    "author": "ui-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "title": "feat: Port button component",
                    "body": "PR to port the button component from the old repository.",
                    "head_branch": "feat/port-button",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "pr_number": 11,
                    "issue_number": 14
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "issue_number": 14
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "version": "v4.0.0-recovered",
                    "description": "Initial recovered release."
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "ui-kit-recovered",
                    "environment": "production"
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "ui-kit-recovered"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "ui-kit",
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts": 1,
                        "report_date": "2025-08-26"
                    }
                },
                {
                    "status": "ok",
                    "data": {
                        "repo": "ui-kit-recovered",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_502",
        "instruction": "Your duty is to coordinate a cross-repository feature development in accordance with the **Cross-Team API Dependency Protocol**. This protocol is activated when a frontend application necessitates a new backend endpoint. It dictates that the backend API must be implemented, released, and subsequently utilized by the frontend application, with all tasks meticulously recorded. You are to use the provided **Feature Manifest** to manage this entire process across both the 'payments-api' (backend) and 'ui-kit' (frontend) repositories. Your final obligation is to assemble a list featuring the activity dashboards for both repositories to verify the protocol was successfully carried out. **Feature Manifest:** * **`payments-api` (Backend):** * **Repository:** {name: 'payments-api', description: 'Handles all payment processing and transaction history.', private: True} * **Issue:** {title: '[API] Create /v2/payment-history Endpoint', body: 'Issue to track the implementation of the new transaction history endpoint.', labels: ['api', 'feature'], assignee: 'server-main'} * **Code:** {branch: 'feature/history-endpoint', commit_message: 'feat: Implement transaction history endpoint', author: 'server-main'} * **PR:** {title: 'feat: Add /v2/payment-history endpoint', body: 'This PR adds the new endpoint for retrieving user payment history.'} * **Release:** {version: 'v2.1.0', description: 'Adds /v2/payment-history endpoint.'} * **`ui-kit` (Frontend):** * **Issue:** {title: '[UI] Build Payment History Component', body: 'Issue to track the development of the new Payment History component.', labels: ['feature', 'ui'], assignee: 'ui-dev'} * **Code:** {branch: 'feature/payment-history', commits: [{message: 'feat: Add new Payment History component', author: 'ui-dev'}, {message: 'refactor: Integrate payments-api v2.1.0', author: 'ui-dev'}]} * **PR:** {title: 'feat: Payment History Component', body: 'This PR adds the new Payment History component that consumes the payments-api.'}",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "payments-api",
                    "description": "Handles all payment processing and transaction history.",
                    "private": true
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "[UI] Build Payment History Component",
                    "body": "Issue to track the development of the new Payment History component.",
                    "labels": [
                        "feature",
                        "ui"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-api",
                    "title": "[API] Create /v2/payment-history Endpoint",
                    "body": "Issue to track the implementation of the new transaction history endpoint.",
                    "labels": [
                        "api",
                        "feature"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "payments-api",
                    "issue_number": 13,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-api",
                    "branch": "feature/history-endpoint",
                    "message": "feat: Implement transaction history endpoint",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "payments-api",
                    "title": "feat: Add /v2/payment-history endpoint",
                    "body": "This PR adds the new endpoint for retrieving user payment history.",
                    "head_branch": "feature/history-endpoint",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "payments-api",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-api",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "payments-api",
                    "issue_number": 13
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "payments-api",
                    "version": "v2.1.0",
                    "description": "Adds /v2/payment-history endpoint."
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/payment-history",
                    "message": "feat: Add new Payment History component",
                    "author": "ui-dev"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/payment-history",
                    "message": "refactor: Integrate payments-api v2.1.0",
                    "author": "ui-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "feat: Payment History Component",
                    "body": "This PR adds the new Payment History component that consumes the payments-api.",
                    "head_branch": "feature/payment-history",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 11,
                    "issue_number": 12
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
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "payments-api"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "ui-kit",
                        "commits_count": 2,
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                },
                {
                    "status": "ok",
                    "data": {
                        "repo": "payments-api",
                        "commits_count": 1,
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_405",
        "instruction": "Your main strategic goal is to handle the post-incident lifecycle for the 'security-scanner' repository, ensuring it perfectly conforms to the company's **Incident Post-Mortem Policy**. This policy requires a transparent and auditable process to track preventative actions identified after an incident, with a central epic monitoring the entire sequence and individual tasks for each action item. You are tasked with guaranteeing that the repository's condition reflects the successful completion of this process, utilizing the given **Post-Mortem Manifest**. Your ultimate deliverable is the repository's activity dashboard, which will function as the official documentation of policy compliance. **Post-Mortem Manifest: Q3 Parser Engine Outage** * **Main Epic:** {title: 'Post-Mortem: Q3 Parser Engine Outage', body: 'Main tracking issue for the post-mortem, to be populated with root cause analysis.', labels: ['post-mortem', 'audit'], assignee: 'tech-lead-tara'} * **Action Items:** [ { status: 'Completed', issue: {title: '[Action Item] Add more alerting for parser errors', body: 'Sub-task to add enhanced alerting to detect parser configuration errors pre-deployment.', labels: ['action-item', 'monitoring'], assignee: 'infra-lead'}, code: {branch: 'feature/parser-alerting', commit_message: 'feat: Add enhanced alerting for parser config errors', author: 'infra-lead'}, pr: {title: 'Feature: Enhanced Parser Alerting', body: 'PR to implement enhanced alerting as per post-mortem action item.', reviewers: ['tech-lead-tara']} }, { status: 'Open', issue: {title: '[Action Item] Improve unit test coverage for parser module', body: 'Sub-task to improve unit test coverage to prevent similar regressions.', labels: ['action-item', 'testing'], assignee: 'qa-erin'} }, { status: 'Open', issue: {title: '[Action Item] Refactor parser module for resilience', body: 'Sub-task to refactor the parser to handle malformed configs gracefully.', labels: ['action-item', 'tech-debt'], assignee: 'security-group'} } ]",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Post-Mortem: Q3 Parser Engine Outage",
                    "body": "Main tracking issue for the post-mortem, to be populated with root cause analysis.",
                    "labels": [
                        "post-mortem",
                        "audit"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "[Action Item] Add more alerting for parser errors",
                    "body": "Sub-task to add enhanced alerting to detect parser configuration errors pre-deployment.",
                    "labels": [
                        "action-item",
                        "monitoring"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "[Action Item] Improve unit test coverage for parser module",
                    "body": "Sub-task to improve unit test coverage to prevent similar regressions.",
                    "labels": [
                        "action-item",
                        "testing"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 14,
                    "assignees": [
                        "qa-erin"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "[Action Item] Refactor parser module for resilience",
                    "body": "Sub-task to refactor the parser to handle malformed configs gracefully.",
                    "labels": [
                        "action-item",
                        "tech-debt"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 15,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "feature/parser-alerting",
                    "message": "feat: Add enhanced alerting for parser config errors",
                    "author": "infra-lead"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Feature: Enhanced Parser Alerting",
                    "body": "PR to implement enhanced alerting as per post-mortem action item.",
                    "head_branch": "feature/parser-alerting",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "security-scanner",
                        "commits_count": 1,
                        "open_issues": 3,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_103",
        "instruction": "Your task is to coordinate the **Quarterly Health and Velocity Audit Policy** for the 'nlp-models' repository. This policy demands a thorough evaluation of the repository's development backlog, recent activities, and current security status. The results of the audit need to be compiled into a formal tracking issue to allocate ownership for examination. You should employ the stipulated **Audit Manifest** to define your analysis scope and create the necessary tracking documentation. Your final deliverable is a detailed repository activity dashboard that summarizes the repository's present condition after the audit. **Audit Manifest: Q3 nlp-models** * **Analysis Scope:** * **Backlog & Velocity:** Examine issue aging and pull request merge times. * **Recent Activity:** Review commit activity for November 2023 (2023-11-01T00:00:00Z to 2023-11-30T23:59:59Z). * **Security Posture:** Inspect open security alerts. * **Tracking Issue:** {title: 'Audit project velocity and backlog', body: 'Generated from audit: review aged issues and PR merge times to identify bottlenecks.', labels: ['audit', 'performance'], assignee: 'ml-engineer'}",
        "actions": [
            {
                "name": "GetIssueAgingReport",
                "arguments": {
                    "repo_name": "nlp-models"
                },
            },
            {
                "name": "GetPullRequestMergeTimeReport",
                "arguments": {
                    "repo_name": "nlp-models"
                },
            },
            {
                "name": "ListCommitsByDateRange",
                "arguments": {
                    "repo_name": "nlp-models",
                    "start_date": "2023-11-01T00:00:00Z",
                    "end_date": "2023-11-30T23:59:59Z"
                },
            },
            {
                "name": "GetOpenSecurityAlerts",
                "arguments": {
                    "repo_name": "nlp-models"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "Audit project velocity and backlog",
                    "body": "Generated from audit: review aged issues and PR merge times to identify bottlenecks.",
                    "labels": [
                        "audit",
                        "performance"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "nlp-models"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "nlp-models",
                        "commits_count": 0,
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_40001",
        "instruction": "Your task is to handle the **Staged Rollout Policy** for the 'k8s-monitoring' repository. This policy necessitates that new features undergo deployment and verification in a 'staging' environment prior to creating a final issue to monitor the production release. You are in charge of ensuring the repository reflects the successful completion of this entire process, as specified by the official **Rollout Specification** below. Your ultimate deliverable is the repository's activity dashboard to confirm the feature's full verification and readiness for production. **Rollout Specification: Alertmanager Integration** * **Feature Tracking:** The principal feature, monitored by an issue, must be 'closed'. * **Code Implementation:** Consolidate all work into a singular 'merged' pull request. * **Staging Verification:** Must register a deployment to the 'staging' environment and close a subsequent QA verification issue. * **Production Readiness:** An open issue must monitor the production release. **Data Manifest:** * **Feature Issue:** {title: 'Implement Alertmanager for notifications', body: 'Main tracking issue for the Alertmanager feature.', labels: ['feature', 'epic'], assignee: 'infra-lead'} * **Code Artifacts:** {branch: 'feature/alertmanager', commit_message: 'feat: Add Alertmanager manifests and config', pr_title: 'feat: Add Alertmanager', pr_body: 'PR to introduce Alertmanager for alert routing.'} * **QA Issue:** {title: 'Staging Verification for Alertmanager', body: 'Tracking issue for QA verification on the staging environment.', labels: ['qa', 'verification'], assignee: 'qa-erin'} * **Production Issue:** {title: 'Schedule Production Release for Alertmanager', body: 'All checks passed. Ready to schedule production deployment.', labels: ['release', 'ops'], assignee: 'release-manager'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Implement Alertmanager for notifications",
                    "body": "Main tracking issue for the Alertmanager feature.",
                    "labels": [
                        "feature",
                        "epic"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 12,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "feature/alertmanager",
                    "message": "feat: Add Alertmanager manifests and config",
                    "author": "infra-lead"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "feat: Add Alertmanager",
                    "body": "PR to introduce Alertmanager for alert routing.",
                    "head_branch": "feature/alertmanager",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 12
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "environment": "staging"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Staging Verification for Alertmanager",
                    "body": "Tracking issue for QA verification on the staging environment.",
                    "labels": [
                        "qa",
                        "verification"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 13,
                    "assignees": [
                        "qa-erin"
                    ]
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 13
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Schedule Production Release for Alertmanager",
                    "body": "All checks passed. Ready to schedule production deployment.",
                    "labels": [
                        "release",
                        "ops"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 14,
                    "assignees": [
                        "release-manager"
                    ]
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "k8s-monitoring",
                        "commits_count": 1,
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_40003",
        "instruction": "You are assigned to coordinate the **Documentation Update Policy** for the 'nlp-models' repository. The policy mandates that all documentation modifications are officially tracked and executed through a pull request. Utilize the provided **Doc Manifest** to craft and process the necessary artifacts. Your end deliverable is a compile of commits for the pertinent branch to act as an audit trail of the changes. **Compliance Specification:** The concluding state must illustrate that a tracking issue for the documentation update was created and has been 'closed', and that the work is 'merged' via a pull request. **Doc Manifest:** * **Issue:** {title: 'Docs: Clarify data preprocessing steps', body: 'The current documentation for data preprocessing is unclear and needs examples.', labels: ['documentation'], assignee: 'ml-engineer'} * **Code Artifacts:** {branch: 'docs/preprocessing-guide', commit_message: 'docs: Add detailed examples to preprocessing guide', pr_title: 'Docs: Clarify preprocessing guide', pr_body: 'This PR adds examples to the preprocessing documentation.', author: 'ml-engineer'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "Docs: Clarify data preprocessing steps",
                    "body": "The current documentation for data preprocessing is unclear and needs examples.",
                    "labels": [
                        "documentation"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "nlp-models",
                    "branch": "docs/preprocessing-guide",
                    "message": "docs: Add detailed examples to preprocessing guide",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "Docs: Clarify preprocessing guide",
                    "body": "This PR adds examples to the preprocessing documentation.",
                    "head_branch": "docs/preprocessing-guide",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12
                },
            },
            {
                "name": "ListCommitsByBranch",
                "arguments": {
                    "repo_name": "nlp-models",
                    "branch": "docs/preprocessing-guide"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": [
                        {
                            "commit_id": "8a7d6f5e4c3b",
                            "repo": "nlp-models",
                            "branch": "docs/preprocessing-guide",
                            "message": "docs: Add detailed examples to preprocessing guide",
                            "author": "ml-engineer",
                            "timestamp": "2025-08-26",
                            "report_date": "2025-08-26"
                        }
                    ]
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_50001",
        "instruction": "Handle the **Incident Post-Mortem Policy** for the 'security-scanner' repository. Due to a recent production outage, it's necessary to conduct a post-mortem to establish corrective measures. The policy involves creating a main epic to oversee the post-mortem and sub-tasks for each action item. You are required to utilize the provided **Post-Mortem Manifest** to generate the essential artifacts. The repository's activity dashboard, exhibiting the current state of the post-mortem process, is your final deliverable. **Compliance Specification:** The endpoint should display an 'open' main post-mortem epic issue. A sub-task for a completed action item has to be 'closed', with its fix properly 'merged' through a pull request. Two other sub-tasks for ongoing tasks must stay 'open'. **Post-Mortem Manifest:** * **Main Epic:** {title: 'Post-Mortem: Q3 Parser Engine Outage', body: 'Main epic to track all action items from the Q3 parser outage.', labels: ['post-mortem', 'epic'], assignee: 'tech-lead-tara'} * **Completed Action Item:** * **Issue:** {title: 'ACTION: Add more alerting for parser errors', body: 'Sub-task to add enhanced alerting to detect parser configuration errors pre-deployment.', labels: ['action-item', 'monitoring'], assignee: 'infra-lead'} * **Code:** {branch: 'feature/parser-alerting', commit_message: 'feat: Add enhanced alerting for parser config errors', pr_title: 'Feature: Enhanced Parser Alerting', pr_body: 'PR to implement enhanced alerting as per post-mortem action item.', author: 'infra-lead', reviewers: ['tech-lead-tara']} * **Open Action Items:** * {title: '[Action Item] Improve unit test coverage for parser module', body: 'Sub-task to improve unit test coverage to prevent similar regressions.', labels: ['action-item', 'testing'], assignee: 'qa-erin'} * {title: '[Action Item] Refactor parser module for resilience', body: 'Sub-task to refactor the parser to handle malformed configs gracefully.', labels: ['action-item', 'tech-debt'], assignee: 'security-group'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Post-Mortem: Q3 Parser Engine Outage",
                    "body": "Main epic to track all action items from the Q3 parser outage.",
                    "labels": [
                        "post-mortem",
                        "epic"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "ACTION: Add more alerting for parser errors",
                    "body": "Sub-task to add enhanced alerting to detect parser configuration errors pre-deployment.",
                    "labels": [
                        "action-item",
                        "monitoring"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "[Action Item] Improve unit test coverage for parser module",
                    "body": "Sub-task to improve unit test coverage to prevent similar regressions.",
                    "labels": [
                        "action-item",
                        "testing"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 14,
                    "assignees": [
                        "qa-erin"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "[Action Item] Refactor parser module for resilience",
                    "body": "Sub-task to refactor the parser to handle malformed configs gracefully.",
                    "labels": [
                        "action-item",
                        "tech-debt"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 15,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "feature/parser-alerting",
                    "message": "feat: Add enhanced alerting for parser config errors",
                    "author": "infra-lead"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Feature: Enhanced Parser Alerting",
                    "body": "PR to implement enhanced alerting as per post-mortem action item.",
                    "head_branch": "feature/parser-alerting",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "security-scanner",
                        "commits_count": 1,
                        "open_issues": 3,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_50003",
        "instruction": "Coordinate the **Multi-Commit Feature Policy** for the 'nlp-models' repository. This policy necessitates that features involving contributions from several authors are unified into one pull request for evaluation. You are to apply the given **Feature Manifest** to create all required artifacts. A summary of commits by author to confirm contributions forms your final deliverable. **Compliance Specification:** The completion state must demonstrate that a feature was recorded via a 'closed' issue. The work should be incorporated into a single 'merged' pull request featuring two commits from different authors, with successful review completion. **Feature Manifest:** * **Issue:** {title: 'Feature: Add model performance visualization', body: 'Tracking issue for the new performance visualization feature.', labels: ['feature', 'visualization'], assignee: 'ml-engineer'} * **Code Artifacts:** * **Branch:** 'feature/perf-viz' * **PR:** {title: 'feat: Model Performance Visualization', body: 'Adds new components for model performance visualization.', reviewers: ['tech-lead-tara']} * **Commits:** [ {message: 'feat: Add data hooks for visualization API', author: 'ml-engineer'}, {message: 'feat: Implement chart components for visualization', author: 'ml-engineer'} ]",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "Feature: Add model performance visualization",
                    "body": "Tracking issue for the new performance visualization feature.",
                    "labels": [
                        "feature",
                        "visualization"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "nlp-models",
                    "branch": "feature/perf-viz",
                    "message": "feat: Add data hooks for visualization API",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "nlp-models",
                    "branch": "feature/perf-viz",
                    "message": "feat: Implement chart components for visualization",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "feat: Model Performance Visualization",
                    "body": "Adds new components for model performance visualization.",
                    "head_branch": "feature/perf-viz",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12
                },
            },
            {
                "name": "CountCommitsByAuthor",
                "arguments": {
                    "repo_name": "nlp-models"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "nlp-models",
                        "commits_by_author": {
                            "ml-engineer": 1
                        },
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_50004",
        "instruction": "Your assignment involves handling the **New Service Onboarding and Governance Policy** for the newly developed 'notification-service'. This policy requires that new services are both technically initialized and compliant with initial governance and security standards before their inaugural release. You are tasked with ensuring the repository's condition fully matches the **Onboarding Compliance Specification**. Your final deliverable is a summary of the repository's health to verify its compliant status. **Onboarding Compliance Specification:** The endpoint condition must demonstrate the repository's creation and inclusion of governance documentation. An operational readiness task ('Configure main branch protection rules') must be 'completed'. A known vulnerability from the base template needs to be addressed, which involves a 'medium' severity alert being 'resolved' and the related tracking issue to be 'completed' after its fix is 'integrated' through a pull request. Lastly, an initial compliant release is required to be put out. **Data Manifest:** * **Repository:** {name: 'notification-service', description: 'Centralized service for handling user notifications.', private: True} * **Governance:** * **Commits:** [{message: 'docs: Add MIT License', author: 'docs-sophia'}, {message: 'docs: Add SECURITY.md policy', author: 'docs-sophia'}] * **Ops Issue:** {title: 'ops: Configure main branch protection rules', body: 'Tracking issue for branch protection setup as per governance policy.', labels: ['ops', 'governance'], assignee: 'infra-lead'} * **Security Remediation:** * **Alert:** {severity: 'medium', description: 'Default template includes outdated dependency: common-lib v1.2.3', file: 'package.json'} * **Issue:** {title: 'fix: Update outdated dependency common-lib', body: 'Tracking issue to update the vulnerable common-lib dependency.', labels: ['security', 'dependency'], assignee: 'infra-lead'} * **Code:** {branch: 'fix/update-common-lib', commit_message: 'fix: Upgrade common-lib to v1.2.4', pr_title: 'fix(deps): Upgrade common-lib to v1.2.4', pr_body: 'PR to upgrade outdated common-lib dependency to v1.2.4.', author: 'infra-lead'} * **Release:** {version: 'v0.1.0', description: 'Initial compliant release.'}",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "notification-service",
                    "description": "Centralized service for handling user notifications.",
                    "private": true
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "notification-service",
                    "branch": "main",
                    "message": "docs: Add MIT License",
                    "author": "docs-sophia"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "notification-service",
                    "branch": "main",
                    "message": "docs: Add SECURITY.md policy",
                    "author": "docs-sophia"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "title": "ops: Configure main branch protection rules",
                    "body": "Tracking issue for branch protection setup as per governance policy.",
                    "labels": [
                        "ops",
                        "governance"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "issue_number": 12,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "notification-service",
                    "severity": "medium",
                    "description": "Default template includes outdated dependency: common-lib v1.2.3",
                    "file": "package.json",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "title": "fix: Update outdated dependency common-lib",
                    "body": "Tracking issue to update the vulnerable common-lib dependency.",
                    "labels": [
                        "security",
                        "dependency"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "issue_number": 13,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "notification-service",
                    "branch": "fix/update-common-lib",
                    "message": "fix: Upgrade common-lib to v1.2.4",
                    "author": "infra-lead"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "notification-service",
                    "title": "fix(deps): Upgrade common-lib to v1.2.4",
                    "body": "PR to upgrade outdated common-lib dependency to v1.2.4.",
                    "head_branch": "fix/update-common-lib",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "notification-service",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "notification-service",
                    "issue_number": 13
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "notification-service",
                    "alert_number": 10
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "notification-service",
                    "version": "v0.1.0",
                    "description": "Initial compliant release."
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "notification-service"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "notification-service",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_50005",
        "instruction": "Your mission is to manage the **Standard Bug Fix Policy** for the 'payments-service' repository. The policy dictates that bugs must be officially tracked via issues and cleared via pull requests. You are to employ the given **Bug Manifest** to establish and handle all necessary items. Your final deliverable is a summary of the repository's health to confirm that the bug has been fixed and all items are completed. **Compliance Specification:** The final condition must demonstrate the bug is completely resolved. This necessitates a 'completed' tracking issue and a matching 'merged' pull request containing the fix from its specific branch, with the two items properly connected. **Bug Manifest:** * **Issue:** {title: 'Bug: Incorrect fee calculation for international transactions', body: 'The service is applying the wrong fee percentage for non-domestic transactions.', labels: ['bug', 'payments'], assignee: 'server-main'} * **Code Artifacts:** {branch: 'fix/international-fees', commit_message: 'fix: Apply correct fee tier for international payments', pr_title: 'Fix: International Fee Calculation', pr_body: 'This PR resolves the incorrect fee calculation bug.', author: 'server-main'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Bug: Incorrect fee calculation for international transactions",
                    "body": "The service is applying the wrong fee percentage for non-domestic transactions.",
                    "labels": [
                        "bug",
                        "payments"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "fix/international-fees",
                    "message": "fix: Apply correct fee tier for international payments",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Fix: International Fee Calculation",
                    "body": "This PR resolves the incorrect fee calculation bug.",
                    "head_branch": "fix/international-fees",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "payments-service"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "payments-service",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_60003",
        "instruction": "Your task is to handle the **Secure Project Bootstrap Policy** for the new 'inventory-management-api' repository. This policy requires that new projects created from a template must have any known vulnerabilities from that template resolved before the initial release. You are responsible for ensuring the repository's condition fully aligns with the **Bootstrap Compliance Specification**. Your final deliverable is the repository's health summary to verify a compliant initial state. **Bootstrap Compliance Specification:** The final state must show that the repository was created with an initial commit. A 'medium' severity alert for an outdated dependency from the template must be 'fixed'. The entire setup and remediation process must be tracked via a main epic issue and a specific sub-task for the fix, both of which must be 'closed'. The fix must be delivered via a 'merged' pull request. A secure initial release must be published. **Data Manifest:** * **Repository:** {name: 'inventory-management-api', description: 'API for managing warehouse inventory.', private: True, initial_commit_message: 'Initial commit from template', initial_commit_author: 'infra-lead'} * **Security Alert:** {severity: 'medium', description: 'Default template includes outdated dependency: GSON v2.8.5', file: 'pom.xml'} * **Tracking:** * **Epic Issue:** {title: 'Initial Project Setup', body: 'Main tracking issue for the complete and secure setup of the new repository.', labels: ['setup', 'epic'], assignee: 'server-main'} * **Fix Issue:** {title: 'fix: Update outdated GSON dependency', body: 'Sub-task to update the vulnerable GSON dependency from the initial template.', labels: ['security', 'dependency'], assignee: 'server-main'} * **Remediation:** * **Code:** {branch: 'hotfix/gson-upgrade', commit_message: 'fix: Upgrade GSON to v2.8.9', author: 'server-main'} * **PR:** {title: 'fix(deps): Upgrade GSON to v2.8.9', body: 'PR to upgrade outdated GSON dependency.', reviewers: ['tech-lead-tara']} * **Release:** {version: 'v0.1.0', description: 'Initial secure release.'}",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "description": "API for managing warehouse inventory.",
                    "private": true
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "branch": "main",
                    "message": "Initial commit from template",
                    "author": "infra-lead"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "severity": "medium",
                    "description": "Default template includes outdated dependency: GSON v2.8.5",
                    "file": "pom.xml",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "title": "Initial Project Setup",
                    "body": "Main tracking issue for the complete and secure setup of the new repository.",
                    "labels": [
                        "setup",
                        "epic"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "title": "fix: Update outdated GSON dependency",
                    "body": "Sub-task to update the vulnerable GSON dependency from the initial template.",
                    "labels": [
                        "security",
                        "dependency"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "issue_number": 13,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "branch": "hotfix/gson-upgrade",
                    "message": "fix: Upgrade GSON to v2.8.9",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "title": "fix(deps): Upgrade GSON to v2.8.9",
                    "body": "PR to upgrade outdated GSON dependency.",
                    "head_branch": "hotfix/gson-upgrade",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "issue_number": 13
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "alert_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "version": "v0.1.0",
                    "description": "Initial secure release."
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "inventory-management-api"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "inventory-management-api",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_30001",
        "instruction": "Your responsibility is to coordinate the **Standard Bug Fix Policy** for the 'payments-service' repository. The policy necessitates that bugs are formally tracked via issues and resolved through pull requests. You must utilize the provided **Bug Manifest** to create and process all necessary artifacts. Your final deliverable is the repository's health summary to confirm that the bug has been resolved and all artifacts are closed. **Compliance Specification:** The final state must demonstrate that the bug is fully resolved. This requires a 'closed' tracking issue and a corresponding 'merged' pull request containing the code fix from its dedicated branch, with the two artifacts correctly linked. **Bug Manifest:** * **Issue:** {number: 12, title: 'Bug: Timeout issue with new payment gateway', body: 'Transactions are timing out when using the new payment gateway.', labels: ['bug', 'networking'], assignee: 'server-main'} * **Code Artifacts:** {pr_number: 10, branch: 'fix/gateway-timeout', commit_message: 'fix: Increase timeout for new payment gateway', pr_title: 'Fix: Gateway Timeout', pr_body: 'This PR resolves the gateway timeout bug.', author: 'server-main'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Bug: Timeout issue with new payment gateway",
                    "body": "Transactions are timing out when using the new payment gateway.",
                    "labels": [
                        "bug",
                        "networking"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "fix/gateway-timeout",
                    "message": "fix: Increase timeout for new payment gateway",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Fix: Gateway Timeout",
                    "body": "This PR resolves the gateway timeout bug.",
                    "head_branch": "fix/gateway-timeout",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "payments-service"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "payments-service",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_30003",
        "instruction": "Your task is to handle the **Feature Development Lifecycle Policy** for the 'ui-kit' repository. This policy mandates that each new feature must be tracked, implemented, and reviewed before it is merged. Utilize the given **Feature Manifest** to produce all necessary artifacts. The ultimate goal is to provide the repository's activity dashboard to confirm the successful integration of the feature. **Compliance Specification:** The end result must demonstrate that a new feature was tracked via an issue, which must be 'closed'. The work has to be executed on a feature branch and sent through a pull request. The pull request needs to be reviewed prior to merging. **Feature Manifest:** * **Issue:** {number: 12, title: 'Feature: Add user avatar component', body: 'Tracking issue for the new user avatar component.', labels: ['feature', 'ui'], assignee: 'ui-dev'} * **Code Artifacts:** {pr_number: 10, branch: 'feature/avatar-component', commit_message: 'feat: Add new user avatar component', pr_title: 'feat: User Avatar Component', pr_body: 'This PR adds the new user avatar component.', author: 'ui-dev'} * **Reviewer:** 'design-lead'",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Feature: Add user avatar component",
                    "body": "Tracking issue for the new user avatar component.",
                    "labels": [
                        "feature",
                        "ui"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/avatar-component",
                    "message": "feat: Add new user avatar component",
                    "author": "ui-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "feat: User Avatar Component",
                    "body": "This PR adds the new user avatar component.",
                    "head_branch": "feature/avatar-component",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "reviewers": [
                        "design-lead"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "ui-kit"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "ui-kit",
                        "commits_count": 1,
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_30004",
        "instruction": "Your task is to coordinate the **New Project Bootstrap Policy** for the 'log-analyzer-service'. This policy guarantees that all new projects are initiated with a standardized set of initial artifacts for tracking, security, and deployment preparedness. Utilize the given **Bootstrap Manifest** to ensure all necessary entities are created. The ultimate objective is to present the initial health summary for the newly established repository. **Compliance Specification:** The concluding state must demonstrate that the repository was created with an initial commit, includes an 'open' tracking issue, one 'open' security alert, and has been deployed to the 'development' environment. **Bootstrap Manifest:** * **Repository:** {name: 'log-analyzer-service', description: 'Service for parsing and analyzing application logs.', private: True} * **Initial Commit:** {author: 'server-main', message: 'Initial commit: project structure and boilerplate'} * **Tracking Issue:** {number: 12, title: 'Define initial logging schema', body: 'Establish the standard JSON schema for log entries.', labels: ['schema', 'design'], assignee: 'server-main'} * **Initial Security Alert:** {severity: 'high', description: 'Potential for arbitrary code execution via insecure YAML parsing.', file: 'src/parser.py'} * **Initial Deployment:** {environment: 'development'}",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "description": "Service for parsing and analyzing application logs.",
                    "private": true
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "branch": "main",
                    "message": "Initial commit: project structure and boilerplate",
                    "author": "server-main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "title": "Define initial logging schema",
                    "body": "Establish the standard JSON schema for log entries.",
                    "labels": [
                        "schema",
                        "design"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "severity": "high",
                    "description": "Potential for arbitrary code execution via insecure YAML parsing.",
                    "file": "src/parser.py",
                    "branch": "main"
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "environment": "development"
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "log-analyzer-service"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "log-analyzer-service",
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts": 1,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_30005",
        "instruction": "Your task is to handle the **Multi-Commit Feature Policy** for the 'infra-terraform' repository. This policy stipulates that features with contributions from multiple authors must be consolidated into a single pull request for review. Utilize the supplied **Feature Manifest** to assemble all necessary artifacts. Your concluding deliverable should include a report detailing commits by author to confirm the contributions. **Compliance Specification:** The end state must confirm a feature was tracked using a 'closed' issue. The work needs to be encapsulated in a lone 'merged' pull request encompassing two commits from separate authors. **Feature Manifest:** * **Issue:** {number: 12, title: 'Feature: Add reusable VPC module', body: 'Tracking issue for the new reusable VPC Terraform module.', labels: ['feature', 'terraform'], assignee: 'platform-team'} * **Code Artifacts:** {pr_number: 10, branch: 'feature/vpc-module', pr_title: 'feat: Reusable VPC Module', pr_body: 'Adds a new reusable module for creating standardized VPCs.', reviewers: ['tech-lead-tara']} * **Commits:** * Commit 1: {message: 'feat: Add main module structure and variables', author: 'platform-team'} * Commit 2: {message: 'test: Add integration tests for VPC module', author: 'infra-lead'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "Feature: Add reusable VPC module",
                    "body": "Tracking issue for the new reusable VPC Terraform module.",
                    "labels": [
                        "feature",
                        "terraform"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 12,
                    "assignees": [
                        "platform-team"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "feature/vpc-module",
                    "message": "feat: Add main module structure and variables",
                    "author": "platform-team"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "feature/vpc-module",
                    "message": "test: Add integration tests for VPC module",
                    "author": "infra-lead"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "feat: Reusable VPC Module",
                    "body": "Adds a new reusable module for creating standardized VPCs.",
                    "head_branch": "feature/vpc-module",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 12
                },
            },
            {
                "name": "CountCommitsByAuthor",
                "arguments": {
                    "repo_name": "infra-terraform"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "infra-terraform",
                        "commits_by_author": {
                            "platform-team": 1,
                            "infra-lead": 1
                        },
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_20001",
        "instruction": "Your task is to coordinate the **Standard Bug Fix Policy** for the 'payments-service' repository. This policy mandates that bugs should be formally tracked through issues and addressed using pull requests. Employ the given **Bug Manifest** to create and manage all necessary artifacts. Your final deliverable is a health summary of the repository to verify that the bug is fixed and all artifacts are completed. **Compliance Specification:** The end state must confirm the bug is entirely resolved. This demands a 'closed' tracking issue and a corresponding 'merged' pull request encompassing the fix from its respective branch, with both artifacts correctly interconnected. **Bug Manifest:** * **Issue:** {number: 12, title: 'Bug: Timeout issue with new payment gateway', body: 'Transactions are timing out when using the new payment gateway.', labels: ['bug', 'networking'], assignee: 'server-main'} * **Code Artifacts:** {pr_number: 10, branch: 'fix/gateway-timeout', commit_message: 'fix: Increase timeout for new payment gateway', pr_title: 'Fix: Gateway Timeout', pr_body: 'This PR resolves the gateway timeout bug.', author: 'server-main'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Bug: Timeout issue with new payment gateway",
                    "body": "Transactions are timing out when using the new payment gateway.",
                    "labels": [
                        "bug",
                        "networking"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "fix/gateway-timeout",
                    "message": "fix: Increase timeout for new payment gateway",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Fix: Gateway Timeout",
                    "body": "This PR resolves the gateway timeout bug.",
                    "head_branch": "fix/gateway-timeout",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "payments-service"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "payments-service",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_20003",
        "instruction": "Your task is to manage the **Proactive Dependency Update Policy** concerning the 'ml-pipeline' repository. The policy mandates that outdated dependencies be timely updated. Utilize the provided **Update Manifest** for executing the update. Your end product should be the activity dashboard of the repository. **Compliance Specification:** The end condition must display a tracking issue for the dependency update that is now 'closed'. The effort must be encapsulated in a 'merged' pull request that has undergone review. **Update Manifest:** * **Issue:** {number: 12, title: 'chore(deps): Update scikit-learn to latest version', body: 'Update the scikit-learn dependency to the latest stable version.', labels: ['chore', 'dependencies'], assignee: 'ml-engineer'} * **Code Artifacts:** {pr_number: 10, branch: 'chore/update-sklearn', commit_message: 'chore: Update scikit-learn to v1.4.0', pr_title: 'chore(deps): Update scikit-learn', pr_body: 'This PR updates scikit-learn.', author: 'ml-engineer'} * **Reviewer:** 'ml-engineer'",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "title": "chore(deps): Update scikit-learn to latest version",
                    "body": "Update the scikit-learn dependency to the latest stable version.",
                    "labels": [
                        "chore",
                        "dependencies"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "issue_number": 12,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "branch": "chore/update-sklearn",
                    "message": "chore: Update scikit-learn to v1.4.0",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "title": "chore(deps): Update scikit-learn",
                    "body": "This PR updates scikit-learn.",
                    "head_branch": "chore/update-sklearn",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "pr_number": 10,
                    "reviewers": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "ml-pipeline"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "ml-pipeline",
                        "commits_count": 1,
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_20005",
        "instruction": "Your responsibility is to coordinate the **Multi-Commit Pull Request Policy** for the 'flutter-finance-app' repository. The policy necessitates that complex features involving input from various authors be unified into a single pull request. Employ the given **Feature Manifest** to compile all required artifacts. Your concluding deliverable will be a report detailing commits by each author to substantiate the contributions. **Compliance Specification:** The ultimate condition must illustrate that a feature was documented through a 'closed' issue. The endeavor must be contained in a single 'merged' pull request inclusive of two commits authored by different individuals. **Feature Manifest:** * **Issue:** {number: 12, title: 'Feature: Add budget tracking and alerts', body: 'Tracking issue for the new budget tracking feature.', labels: ['feature', 'budgeting'], assignee: 'app-developer'} * **Code Artifacts:** {pr_number: 10, branch: 'feature/budget-tracking', pr_title: 'feat: Budget tracking and alerts', pr_body: 'Adds new components for budget tracking.', reviewers: ['tech-lead-tara']} * **Commits:** * Commit 1: {message: 'feat: Add database schema for budgets', author: 'app-developer'} * Commit 2: {message: 'feat: Implement UI for budget creation', author: 'ui-developer'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "title": "Feature: Add budget tracking and alerts",
                    "body": "Tracking issue for the new budget tracking feature.",
                    "labels": [
                        "feature",
                        "budgeting"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "issue_number": 12,
                    "assignees": [
                        "app-developer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "branch": "feature/budget-tracking",
                    "message": "feat: Add database schema for budgets",
                    "author": "app-developer"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "branch": "feature/budget-tracking",
                    "message": "feat: Implement UI for budget creation",
                    "author": "ui-developer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "title": "feat: Budget tracking and alerts",
                    "body": "Adds new components for budget tracking.",
                    "head_branch": "feature/budget-tracking",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "issue_number": 12
                },
            },
            {
                "name": "CountCommitsByAuthor",
                "arguments": {
                    "repo_name": "flutter-finance-app"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "flutter-finance-app",
                        "commits_by_author": {
                            "app-developer": 1,
                            "ui-developer": 1
                        },
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_10001",
        "instruction": "Your task is to handle the **Blocked Feature Policy** for the 'acme-webapp' repository. There's a new feature in development, currently hindered by an outside dependency. This policy mandates that both the feature and its blocker must be officially documented. Your ultimate output is a health summary of the repository detailing the state of outstanding items. **Compliance Specification:** The final scenario should display an 'open' pull request for the feature, connected to its 'open' tracking issue. An additional 'open' issue must be present to monitor the external blocker. **Data Specification:** * **Feature Issue:** {title: 'Feature: Integrate new payment provider', body: 'Tracking issue for the new payment provider feature.', labels: ['feature', 'payments'], assignee: 'maya-w'} * **Blocker Issue:** {title: 'Blocker: Waiting for new API version from payments provider', body: 'This issue tracks the external dependency blocking the feature development.', labels: ['blocked', 'external-dependency'], assignee: 'tech-lead-tara'} * **Code Artifacts:** {branch: 'feature/new-provider', commit_message: 'feat: Add initial scaffolding for new payment provider', pr_title: 'WIP: Feature/New Payment Provider', pr_body: 'Work in progress PR for the new payment provider.', author: 'maya-w'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Feature: Integrate new payment provider",
                    "body": "Tracking issue for the new payment provider feature.",
                    "labels": [
                        "feature",
                        "payments"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12,
                    "assignees": [
                        "maya-w"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature/new-provider",
                    "message": "feat: Add initial scaffolding for new payment provider",
                    "author": "maya-w"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "WIP: Feature/New Payment Provider",
                    "body": "Work in progress PR for the new payment provider.",
                    "head_branch": "feature/new-provider",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Blocker: Waiting for new API version from payments provider",
                    "body": "This issue tracks the external dependency blocking the feature development.",
                    "labels": [
                        "blocked",
                        "external-dependency"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 13,
                    "assignees": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "acme-webapp"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "acme-webapp",
                        "open_issues": 2,
                        "open_prs": 1,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_10003",
        "instruction": "Your task is to implement the **Security Audit and Triage Policy** for the 'security-scanner' repository. The policy requires an audit to be conducted, with all findings recorded in a new, aggregated issue. Your final deliverable is a collection of closed issues to verify that the audit issue was documented and resolved. **Compliance Specification:** The final situation must show that a fresh issue was produced to encapsulate the audit findings, which is now in a 'closed' state indicating the completion of the audit report. **Audit Manifest:** * **Audit Scope:** Examine high-severity alerts, repository risk score, and team contribution stats. * **Summary Issue:** {title: 'Q3 Security Audit Summary', body: 'This issue summarizes the findings of the Q3 security audit, including risk score and alert review.', labels: ['audit', 'security'], assignee: 'tech-lead-tara'}",
        "actions": [
            {
                "name": "ListAlertsBySeverity",
                "arguments": {
                    "repo_name": "security-scanner",
                    "severity": "high"
                },
            },
            {
                "name": "GetRepositoryRiskScore",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "GetTeamContributionStats",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Q3 Security Audit Summary",
                    "body": "This issue summarizes the findings of the Q3 security audit, including risk score and alert review.",
                    "labels": [
                        "audit",
                        "security"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12
                },
            },
            {
                "name": "GetClosedIssues",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": [
                        {
                            "issue_id": "ISSUE_security-scanner_eb76c48f",
                            "title": "Q3 Security Audit Summary",
                            "labels": [
                                "audit",
                                "security"
                            ],
                            "state": "closed",
                            "closed_at": "2025-08-26",
                            "report_date": "2025-08-26"
                        }
                    ]
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_10004",
        "instruction": "Your task involves handling the **Hotfix Release Policy** for the 'payments-service' repository. A critical bug has surfaced that necessitates an urgent patch and release. You must employ the provided **Hotfix Manifest** to construct all artifacts. Your ultimate output is the repository's health summary, confirming the issue is resolved. **Compliance Specification:** The concluding state must demonstrate that a critical bug was monitored via an issue, which must now be 'closed'. The resolution must be carried out on a hotfix branch and 'merged' using a pull request. A fresh hotfix version must be released. **Hotfix Manifest:** * **Issue:** {title: 'Bug: Payment processor fails on CAD transactions', body: 'Critical bug causing failures for all CAD-denominated transactions.', labels: ['bug', 'hotfix'], assignee: 'server-main'} * **Code Artifacts:** {branch: 'hotfix/cad-transactions', commit_message: 'fix: Add CAD currency handling to processor', pr_title: 'Fix: CAD Transaction Bug', pr_body: 'Hotfix for the CAD transaction bug.', author: 'server-main'} * **Release:** {version: 'v1.0.1', description: 'Hotfix for CAD transaction failures.'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Bug: Payment processor fails on CAD transactions",
                    "body": "Critical bug causing failures for all CAD-denominated transactions.",
                    "labels": [
                        "bug",
                        "hotfix"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "hotfix/cad-transactions",
                    "message": "fix: Add CAD currency handling to processor",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Fix: CAD Transaction Bug",
                    "body": "Hotfix for the CAD transaction bug.",
                    "head_branch": "hotfix/cad-transactions",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "payments-service",
                    "version": "v1.0.1",
                    "description": "Hotfix for CAD transaction failures."
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "payments-service"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "payments-service",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_10005",
        "instruction": "Your assignment involves coordinating the **Multi-Commit Feature Policy** for the 'nlp-models' repository. The policy stipulates that features with inputs from multiple contributors are combined into a single pull request for review. You must use the supplied **Feature Manifest** to build all artifacts. Your final output is a report of commits by author to validate the contributions. **Compliance Specification:** The end state must illustrate that a feature was tracked via a 'closed' issue. The task must be contained in a single 'merged' pull request that encompasses two commits from different authors. **Feature Manifest:** * **Issue:** {number: 12, title: 'Feature: Add model performance visualization', body: 'Tracking issue for the new performance visualization feature.', labels: ['feature', 'visualization'], assignee: 'ml-engineer'} * **Code Artifacts:** {pr_number: 10, branch: 'feature/perf-viz', pr_title: 'feat: Model Performance Visualization', pr_body: 'Adds new components for model performance visualization.', reviewers: ['tech-lead-tara']} * **Commits:** * Commit 1: {message: 'feat: Add data hooks for visualization API', author: 'ml-engineer'} * Commit 2: {message: 'feat: Implement chart components for visualization', author: 'ml-engineer'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "Feature: Add model performance visualization",
                    "body": "Tracking issue for the new performance visualization feature.",
                    "labels": [
                        "feature",
                        "visualization"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "nlp-models",
                    "branch": "feature/perf-viz",
                    "message": "feat: Add data hooks for visualization API",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "nlp-models",
                    "branch": "feature/perf-viz",
                    "message": "feat: Implement chart components for visualization",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "feat: Model Performance Visualization",
                    "body": "Adds new components for model performance visualization.",
                    "head_branch": "feature/perf-viz",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12
                },
            },
            {
                "name": "CountCommitsByAuthor",
                "arguments": {
                    "repo_name": "nlp-models"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "nlp-models",
                        "commits_by_author": {
                            "ml-engineer": 1
                        },
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_9001",
        "instruction": "Your task is to handle the **Standard Bug Fix Policy** for the 'utils-js' repository. According to the policy, bugs need to be formally tracked through issues and resolved via pull requests. You are required to utilize the given **Bug Manifest** in order to generate and manage all necessary artifacts. Your ultimate deliverable is a health report for the repository that confirms the bug has been fixed and all associated artifacts have been closed. **Compliance Specification:** The concluded state must indicate that the bug is fully resolved. This includes a 'closed' tracking issue and an associated 'merged' pull request with the code correction from its specific branch, ensuring both artifacts are accurately linked. **Bug Manifest:** * **Issue:** {title: 'Bug: Incorrect parsing of UTC date strings', body: 'The date utility incorrectly handles UTC strings, causing off-by-one day errors.', labels: ['bug', 'datetime'], assignee: 'ryan-dev'} * **Code Artifacts:** {branch: 'fix/utc-parsing', commit_message: 'fix: Correct UTC date string parsing logic', pr_title: 'Fix: Date Parsing for UTC', pr_body: 'This PR resolves the UTC parsing bug.', author: 'ryan-dev'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "Bug: Incorrect parsing of UTC date strings",
                    "body": "The date utility incorrectly handles UTC strings, causing off-by-one day errors.",
                    "labels": [
                        "bug",
                        "datetime"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 12,
                    "assignees": [
                        "ryan-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "utils-js",
                    "branch": "fix/utc-parsing",
                    "message": "fix: Correct UTC date string parsing logic",
                    "author": "ryan-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "Fix: Date Parsing for UTC",
                    "body": "This PR resolves the UTC parsing bug.",
                    "head_branch": "fix/utc-parsing",
                    "base_branch": "master"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "utils-js"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "utils-js",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_9002",
        "instruction": "Your objective is to coordinate the **Alert Triage Policy** for a false positive identified in the 'acme-webapp' repository. The policy mandates a formal process of investigation, documentation, and dismissal. You must employ the provided **Triage Manifest** to establish all necessary artifacts. Your ultimate deliverable is a comprehensive report of all resolved security alerts for auditing the triage decision. **Compliance Specification:** The completed state should reflect the creation of a 'low' severity alert, which is subsequently marked as 'fixed,' signifying its dismissal. The investigation must be documented through an issue, which needs to be 'closed'. A pull request, solely comprising a code comment to suppress the linter warning, is required to be merged. **Triage Manifest:** * **Alert:** {severity: 'low', description: 'Hardcoded timeout value in configuration', file: 'src/config.py'} * **Issue:** {title: 'Investigate hardcoded timeout alert - False Positive', body: 'Investigation of the hardcoded timeout value, which is confirmed to be a false positive.', assignee: 'maya-w'} * **Code Artifacts:** {branch: 'chore/suppress-linter-warning', commit_message: 'chore: Suppress linter warning for intentional timeout value', pr_title: 'Chore: Suppress timeout warning', pr_body: 'Adding linter suppression comment for approved false positive.', author: 'maya-w'}",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "severity": "low",
                    "description": "Hardcoded timeout value in configuration",
                    "file": "src/config.py",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Investigate hardcoded timeout alert - False Positive",
                    "body": "Investigation of the hardcoded timeout value, which is confirmed to be a false positive."
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12,
                    "assignees": [
                        "maya-w"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "chore/suppress-linter-warning",
                    "message": "chore: Suppress linter warning for intentional timeout value",
                    "author": "maya-w"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Chore: Suppress timeout warning",
                    "body": "Adding linter suppression comment for approved false positive.",
                    "head_branch": "chore/suppress-linter-warning",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "alert_number": 10
                },
            },
            {
                "name": "GetResolvedSecurityAlerts",
                "arguments": {
                    "repo_name": "acme-webapp"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": [
                        {
                            "alert_id": "ALERT_acme-webapp_9707860a",
                            "severity": "low",
                            "state": "fixed",
                            "resolved_at": "2025-08-26",
                            "description": "Hardcoded timeout value in configuration"
                        }
                    ]
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_9004",
        "instruction": "Handle the **New Project Bootstrap Policy** for the 'log-analyzer-service'. This policy guarantees a consistent setup of initial artifacts for tracking, security, and deployment readiness across all new projects. Utilize the provided **Bootstrap Manifest** to establish all necessary entities. The final submission should be the initial health summary for the newly created repository. **Compliance Specification:** The completed state must demonstrate that the repository was initialized with a first commit, has one 'open' tracking issue, one 'open' security alert, and has been deployed to the 'development' environment. **Bootstrap Manifest:** * **Repository:** {name: 'log-analyzer-service', description: 'Service for parsing and analyzing application logs.', private: True} * **Initial Commit:** {author: 'server-main', message: 'Initial commit: project structure and boilerplate'} * **Tracking Issue:** {title: 'Define initial logging schema', body: 'Establish the standard JSON schema for log entries.', labels: ['schema', 'design'], assignee: 'server-main'} * **Initial Security Alert:** {severity: 'high', description: 'Potential for arbitrary code execution via insecure YAML parsing.', file: 'src/parser.py'} * **Initial Deployment:** {environment: 'development'}",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "description": "Service for parsing and analyzing application logs.",
                    "private": true
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "branch": "main",
                    "message": "Initial commit: project structure and boilerplate",
                    "author": "server-main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "title": "Define initial logging schema",
                    "body": "Establish the standard JSON schema for log entries.",
                    "labels": [
                        "schema",
                        "design"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "severity": "high",
                    "description": "Potential for arbitrary code execution via insecure YAML parsing.",
                    "file": "src/parser.py",
                    "branch": "main"
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "environment": "development"
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "log-analyzer-service"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "log-analyzer-service",
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts": 1,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_9005",
        "instruction": "Coordinate the **Multi-Commit Feature Policy** for the 'nlp-models' repository. This policy stipulates that features with inputs from multiple authors should be consolidated into one pull request for evaluation. Follow the provided **Feature Manifest** to produce all necessary artifacts. The final output should be a report of commits by author to confirm the contributions. **Compliance Specification:** The completed state must indicate that a feature was tracked via a 'closed' issue. The work needs to be contained within one 'merged' pull request that incorporates two commits from different authors. **Feature Manifest:** * **Issue:** {title: 'Feature: Add model performance visualization', body: 'Tracking issue for the new performance visualization feature.', labels: ['feature', 'visualization'], assignee: 'ml-engineer'} * **Code Artifacts:** {branch: 'feature/perf-viz', pr_title: 'feat: Model Performance Visualization', pr_body: 'Adds new components for model performance visualization.', reviewers: ['tech-lead-tara']} * **Commits:** * Commit 1: {message: 'feat: Add data hooks for visualization API', author: 'ml-engineer'} * Commit 2: {message: 'feat: Implement chart components for visualization', author: 'ml-engineer'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "Feature: Add model performance visualization",
                    "body": "Tracking issue for the new performance visualization feature.",
                    "labels": [
                        "feature",
                        "visualization"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "nlp-models",
                    "branch": "feature/perf-viz",
                    "message": "feat: Add data hooks for visualization API",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "nlp-models",
                    "branch": "feature/perf-viz",
                    "message": "feat: Implement chart components for visualization",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "feat: Model Performance Visualization",
                    "body": "Adds new components for model performance visualization.",
                    "head_branch": "feature/perf-viz",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "nlp-models",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12
                },
            },
            {
                "name": "CountCommitsByAuthor",
                "arguments": {
                    "repo_name": "nlp-models"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "nlp-models",
                        "commits_by_author": {
                            "ml-engineer": 1
                        },
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_8001",
        "instruction": "Your task is to handle the **Standard Bug Fix Policy** for the 'utils-js' repository. This policy demands that bugs are officially tracked with issues and sorted out through pull requests. Utilize the supplied **Bug Manifest** to generate and handle all necessary artifacts. Your concluding output is the repository's health summary to verify that the bug has been fixed and all artifacts are finalized. **Compliance Specification:** The end state must confirm that the bug is fully corrected. It requires having a 'closed' tracking issue and a 'merged' pull request containing the code fix drawn from its specific branch, with both artifacts appropriately linked. **Bug Manifest:** * **Issue:** {title: 'Bug: Incorrect parsing of UTC date strings', body: 'The date utility incorrectly handles UTC strings, causing off-by-one day errors.', labels: ['bug', 'datetime'], assignee: 'ryan-dev'} * **Code Artifacts:** {branch: 'fix/utc-parsing', commit_message: 'fix: Correct UTC date string parsing logic', pr_title: 'Fix: Date Parsing for UTC', pr_body: 'This PR resolves the UTC parsing bug.', author: 'ryan-dev'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "Bug: Incorrect parsing of UTC date strings",
                    "body": "The date utility incorrectly handles UTC strings, causing off-by-one day errors.",
                    "labels": [
                        "bug",
                        "datetime"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 12,
                    "assignees": [
                        "ryan-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "utils-js",
                    "branch": "fix/utc-parsing",
                    "message": "fix: Correct UTC date string parsing logic",
                    "author": "ryan-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "Fix: Date Parsing for UTC",
                    "body": "This PR resolves the UTC parsing bug.",
                    "head_branch": "fix/utc-parsing",
                    "base_branch": "master"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "utils-js"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "utils-js",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_8002",
        "instruction": "You are tasked with coordinating the **Alert Triage Policy** for a false positive in the 'acme-webapp' repository. The policy mandates a structured investigation, documentation, and dismissal process. Utilize the specified **Triage Manifest** to generate all necessary artifacts. Your final outcome is a report of all resolved security alerts to validate the triage result. **Compliance Specification:** The closing state must demonstrate that a 'low' severity alert was generated and subsequently flagged as 'fixed' to signify its dismissal. The inquiry must be monitored through an issue, which has to be 'closed'. A pull request that solely includes a code comment to mute the linter warning must get merged. **Triage Manifest:** * **Alert:** {severity: 'low', description: 'Hardcoded timeout value in configuration', file: 'src/config.py'} * **Issue:** {title: 'Investigate hardcoded timeout alert - False Positive', body: 'Investigation of the hardcoded timeout value, which is confirmed to be a false positive.', assignee: 'maya-w'} * **Code Artifacts:** {branch: 'chore/suppress-linter-warning', commit_message: 'chore: Suppress linter warning for intentional timeout value', pr_title: 'Chore: Suppress timeout warning', pr_body: 'Adding linter suppression comment for approved false positive.', author: 'maya-w'}",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "severity": "low",
                    "description": "Hardcoded timeout value in configuration",
                    "file": "src/config.py",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Investigate hardcoded timeout alert - False Positive",
                    "body": "Investigation of the hardcoded timeout value, which is confirmed to be a false positive."
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12,
                    "assignees": [
                        "maya-w"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "chore/suppress-linter-warning",
                    "message": "chore: Suppress linter warning for intentional timeout value",
                    "author": "maya-w"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Chore: Suppress timeout warning",
                    "body": "Adding linter suppression comment for approved false positive.",
                    "head_branch": "chore/suppress-linter-warning",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "alert_number": 10
                },
            },
            {
                "name": "GetResolvedSecurityAlerts",
                "arguments": {
                    "repo_name": "acme-webapp"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": [
                        {
                            "alert_id": "ALERT_acme-webapp_9707860a",
                            "severity": "low",
                            "state": "fixed",
                            "resolved_at": "2025-08-26",
                            "description": "Hardcoded timeout value in configuration"
                        }
                    ]
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_8003",
        "instruction": "Your task is to handle the **Feature Development Lifecycle Policy** for the 'ui-kit' repository. This policy necessitates that a new feature is monitored, implemented, and reviewed prior to merging. Utilize the provided **Feature Manifest** to produce all necessary artifacts. Your ultimate deliverable is the activity dashboard of the repository to confirm the successful integration of the feature. **Compliance Specification:** The ultimate state must indicate that a new feature was monitored through an issue, which must be 'closed'. The development must occur on a feature branch and be introduced via a pull request. The pull request needs to be reviewed before merging. **Feature Manifest:** * **Issue:** {title: 'Feature: Add user avatar component', body: 'Tracking issue for the new user avatar component.', labels: ['feature', 'ui'], assignee: 'ui-dev'} * **Code Artifacts:** {branch: 'feature/avatar-component', commit_message: 'feat: Add new user avatar component', pr_title: 'feat: User Avatar Component', pr_body: 'This PR adds the new user avatar component.', author: 'ui-dev'} * **Reviewer:** 'design-lead'",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Feature: Add user avatar component",
                    "body": "Tracking issue for the new user avatar component.",
                    "labels": [
                        "feature",
                        "ui"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/avatar-component",
                    "message": "feat: Add new user avatar component",
                    "author": "ui-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "feat: User Avatar Component",
                    "body": "This PR adds the new user avatar component.",
                    "head_branch": "feature/avatar-component",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "reviewers": [
                        "design-lead"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "ui-kit"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "ui-kit",
                        "commits_count": 1,
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_8004",
        "instruction": "Your responsibility is to coordinate the **New Project Bootstrap Policy** for the 'log-analyzer-service'. This policy ensures new projects are initiated with a consistent set of initial artifacts for tracking, security, and deployment preparedness. Utilize the provided **Bootstrap Manifest** to establish all required entities. Your concluding deliverable is the initial health summary for the newly set up repository. **Compliance Specification:** The concluding state must demonstrate that the repository was developed with an initial commit, possesses one 'open' tracking issue, one 'open' security alert, and has undergone deployment to the 'development' environment. **Bootstrap Manifest:** * **Repository:** {name: 'log-analyzer-service', description: 'Service for parsing and analyzing application logs.', private: True} * **Initial Commit:** {author: 'server-main', message: 'Initial commit: project structure and boilerplate'} * **Tracking Issue:** {title: 'Define initial logging schema', body: 'Establish the standard JSON schema for log entries.', labels: ['schema', 'design'], assignee: 'server-main'} * **Initial Security Alert:** {severity: 'high', description: 'Potential for arbitrary code execution via insecure YAML parsing.', file: 'src/parser.py'} * **Initial Deployment:** {environment: 'development'}",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "description": "Service for parsing and analyzing application logs.",
                    "private": true
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "branch": "main",
                    "message": "Initial commit: project structure and boilerplate",
                    "author": "server-main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "title": "Define initial logging schema",
                    "body": "Establish the standard JSON schema for log entries.",
                    "labels": [
                        "schema",
                        "design"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "severity": "high",
                    "description": "Potential for arbitrary code execution via insecure YAML parsing.",
                    "file": "src/parser.py",
                    "branch": "main"
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "log-analyzer-service",
                    "environment": "development"
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "log-analyzer-service"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "log-analyzer-service",
                        "open_issues": 1,
                        "open_prs": 0,
                        "open_alerts": 1,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_8005",
        "instruction": "Your task is to handle the **Release Hotfix Policy** for the 'payments-service' repository. A critical bug has been detected in a new release. The policy mandates tracking the bug and issuing a new hotfix version. Utilize the provided **Hotfix Manifest** for all operations. Your ultimate deliverable is a health summary of the repository, confirming the completion of the hotfix process and the absence of any unresolved items. **Compliance Specification:** The concluding state should display two releases: the original problematic one followed by the hotfix. A bug tracking issue must be 'closed', and the hotfix enacted through a 'merged' pull request. **Hotfix Manifest:** * **Initial Release:** {version: 'v1.0.0', description: 'Initial feature release.', commit_message: 'feat: Add new payment processor', pr_title: 'feat: New Payment Processor', pr_body: 'Initial PR for the new payment processor.'} * **Bug Issue:** {title: 'Bug: New processor fails on EUR transactions', body: 'Critical bug causing failures for all EUR-denominated transactions.', labels: ['bug', 'hotfix'], assignee: 'server-main'} * **Hotfix Artifacts:** {branch: 'hotfix/eur-transactions', commit_message: 'fix: Add EUR currency handling to new processor', pr_title: 'Fix: EUR Transaction Bug', pr_body: 'Hotfix for the EUR transaction bug.', author: 'server-main'} * **Hotfix Release:** {version: 'v1.0.1', description: 'Hotfix for EUR transaction failures.'}",
        "actions": [
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "main",
                    "message": "feat: Add new payment processor",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "feat: New Payment Processor",
                    "body": "Initial PR for the new payment processor.",
                    "head_branch": "main",
                    "base_branch": "main"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "payments-service",
                    "version": "v1.0.0",
                    "description": "Initial feature release."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Bug: New processor fails on EUR transactions",
                    "body": "Critical bug causing failures for all EUR-denominated transactions.",
                    "labels": [
                        "bug",
                        "hotfix"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "hotfix/eur-transactions",
                    "message": "fix: Add EUR currency handling to new processor",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Fix: EUR Transaction Bug",
                    "body": "Hotfix for the EUR transaction bug.",
                    "head_branch": "hotfix/eur-transactions",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 11,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "payments-service",
                    "version": "v1.0.1",
                    "description": "Hotfix for EUR transaction failures."
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "payments-service"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "payments-service",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_7001",
        "instruction": "Your task is to manage the company's **Full Security Remediation Policy** for the 'security-scanner' repository. The policy stipulates that any newly identified vulnerabilities must be logged, tracked, and completely resolved through a standard PR lifecycle. You are accountable for ensuring the repository's concluding state aligns with the official **Remediation Compliance Specification** provided below. Your final deliverable is a comprehensive report validating the repository's newly reinforced security stance. **Remediation Compliance Specification:** * **Vulnerability Logging:** Generate two new 'critical' alerts and subsequently transition them to a 'fixed' status. * **Incident Tracking:** Develop two corresponding issues to follow the alerts, which must be 'closed' by the conclusion of the procedure. * **Code Remediation:** All code updates must be combined into a single 'merged' Pull Request, originating from an existing branch and interconnected with both tracking issues. **Data Specification:** * Alert 1: {description: 'Unsafe deserialization in YAML parser', file: 'src/parser.rs'} * Alert 2: {description: 'Potential buffer overflow in string handler', file: 'src/scanner.rs'} * Issue 1: {title: 'Track: Unsafe Deserialization', body: 'Tracking issue for the critical alert regarding the YAML parser.', labels: ['bug', 'security'], assignee: 'security-group'} * Issue 2: {title: 'Track: Buffer Overflow', body: 'Tracking issue for the critical alert regarding the string handler.', labels: ['bug', 'security'], assignee: 'security-group'} * Code Artifacts: {branch: 'perf-optimizations', pr_title: 'Fix: Remediate Critical Parser and Scanner Vulnerabilities', pr_body: 'This PR addresses critical vulnerabilities discovered during a security audit.', commit_1: 'fix: Add validation to YAML parser', commit_2: 'fix: Implement bounds checking in string handler', author: 'security-group'}",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "severity": "critical",
                    "description": "Unsafe deserialization in YAML parser",
                    "file": "src/parser.rs",
                    "branch": "main"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "severity": "critical",
                    "description": "Potential buffer overflow in string handler",
                    "file": "src/scanner.rs",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Track: Unsafe Deserialization",
                    "body": "Tracking issue for the critical alert regarding the YAML parser.",
                    "labels": [
                        "bug",
                        "security"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Track: Buffer Overflow",
                    "body": "Tracking issue for the critical alert regarding the string handler.",
                    "labels": [
                        "bug",
                        "security"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "perf-optimizations",
                    "message": "fix: Add validation to YAML parser",
                    "author": "security-group"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "perf-optimizations",
                    "message": "fix: Implement bounds checking in string handler",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Fix: Remediate Critical Parser and Scanner Vulnerabilities",
                    "head_branch": "perf-optimizations",
                    "base_branch": "main",
                    "body": "This PR addresses critical vulnerabilities discovered during a security audit."
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "alert_number": 10
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "alert_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13
                },
            },
            {
                "name": "GenerateEndToEndReport",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "security-scanner",
                        "commits_count": 2,
                        "open_issues": 0,
                        "merged_prs": 1,
                        "open_alerts": 0,
                        "releases_count": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_7002",
        "instruction": "Handle the **Standard Release Protocol** for the 'k8s-monitoring' repository. Ensure that the repository's final state aligns with the official **Compliance Specification for v2.5.0** detailed below. Your task concludes with delivering the repository's health summary to verify the protocol was adhered to. **Compliance Specification for v2.5.0:** * **Code & PR:** A commit by `devops-lead` with the message 'Docs: Finalize guide for Prometheus v2.5.0' is required to be merged from the 'upgrade-prometheus' branch through a pull request titled 'Release v2.5.0: Prometheus Upgrade' accompanied by a body of 'This PR finalizes the Prometheus v2.5.0 upgrade for production release.'. * **Tracking:** Two new 'open' issues should be existent and assigned to `devops-lead`: one titled 'Task: Verify prometheus scraping post-upgrade' with a body of 'Post-release verification needed for prometheus scraping configurations.' and attached ['task', 'monitoring'] labels, alongside another titled 'Task: Audit Alertmanager notification channels' with a body of 'Post-release audit needed for Alertmanager notification routing and channels.' and ['task', 'alerting'] labels. * **Release & Deployment:** Publish a formal release 'v2.5.0' with the description 'Official release for the Prometheus v2.5.0 upgrade.', and note a deployment to the 'production' environment.",
        "actions": [
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "branch": "upgrade-prometheus",
                    "message": "Docs: Finalize guide for Prometheus v2.5.0",
                    "author": "infra-lead"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Release v2.5.0: Prometheus Upgrade",
                    "head_branch": "upgrade-prometheus",
                    "base_branch": "main",
                    "body": "This PR finalizes the Prometheus v2.5.0 upgrade for production release."
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "pr_number": 10
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Task: Verify prometheus scraping post-upgrade",
                    "body": "Post-release verification needed for prometheus scraping configurations.",
                    "labels": [
                        "task",
                        "monitoring"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 12,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Task: Audit Alertmanager notification channels",
                    "body": "Post-release audit needed for Alertmanager notification routing and channels.",
                    "labels": [
                        "task",
                        "alerting"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 13,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "version": "v2.5.0",
                    "description": "Official release for the Prometheus v2.5.0 upgrade."
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "environment": "production"
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "k8s-monitoring"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "k8s-monitoring",
                        "open_issues": 2,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_7003",
        "instruction": "Coordinate the **Backlog Grooming Policy** for the 'nlp-models' repository. Conduct a formal audit of the repository's health and formulate tracking issues for any identified areas in need of improvement using the provided **Audit Manifest** as a guide. Complete your task by producing an end-to-end report confirming the proper logging of new issues. **Compliance Specification:** The ultimate state of the repository must show two new 'open' issues, which have been accurately assigned in line with the audit's findings. **Audit Manifest:** * **Required Issue 1 (Technical Debt):** {title: 'Technical Debt: Audit Aging Items', body: 'Audit to identify and prioritize aging issues and slow PRs.', labels: ['tech-debt', 'audit'], assignee: 'ml-engineer'} * **Required Issue 2 (Enhancement):** {title: 'Enhancement: Improve Tokenizer Support', body: 'Formal tracking for feature request to improve custom tokenizer support.', labels: ['enhancement', 'tokenizer'], assignee: 'language-ai'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "Technical Debt: Audit Aging Items",
                    "body": "Audit to identify and prioritize aging issues and slow PRs.",
                    "labels": [
                        "tech-debt",
                        "audit"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 12,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "title": "Enhancement: Improve Tokenizer Support",
                    "body": "Formal tracking for feature request to improve custom tokenizer support.",
                    "labels": [
                        "enhancement",
                        "tokenizer"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "nlp-models",
                    "issue_number": 13,
                    "assignees": [
                        "language-ai"
                    ]
                },
            },
            {
                "name": "GenerateEndToEndReport",
                "arguments": {
                    "repo_name": "nlp-models"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "nlp-models",
                        "commits_count": 0,
                        "open_issues": 2,
                        "merged_prs": 0,
                        "open_alerts": 0,
                        "releases_count": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_6002",
        "instruction": "Your task is to handle the **Bug Resolution Audit Policy** for the 'utils-js' repository. A bug requires fixing and an appropriate audit trail must be established. The final deliverable you need to prepare is a repository health summary that verifies the bug tracking issue was resolved and closed as required. **Compliance Specification:** The outcome must indicate that a bug was tracked and is now 'closed'. The solution must be applied on a dedicated branch and integrated through a pull request. **Data Specification:** * Issue Title: 'Bug: Incorrect parsing of date strings' * Assignee/Author: 'ryan-dev' * Code Artifacts: {branch: 'fix/date-parsing', commit_message: 'fix: Correct date string parsing logic', pr_title: 'fix: Date parsing'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "Bug: Incorrect parsing of date strings",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 12,
                    "assignees": [
                        "ryan-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "utils-js",
                    "branch": "fix/date-parsing",
                    "message": "fix: Correct date string parsing logic",
                    "author": "ryan-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "fix: Date parsing",
                    "body": "",
                    "head_branch": "fix/date-parsing",
                    "base_branch": "master",
                    "author": "ryan-dev"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "utils-js"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "utils-js",
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_6003",
        "instruction": "You are assigned to coordinate the **Feature Development Lifecycle Policy** for the 'react-dashboard' repository. A new feature must be implemented and tracked. The policy stipulates that the pull request should be in a mergeable state prior to merging. Your final task is a repository health summary that confirms the successful feature integration. **Compliance Specification:** The final state must reflect that a new feature was managed through an issue, which must be 'closed'. The feature must be developed on a feature branch and a pull request must be submitted. The pull request's metadata needs verification for validity before merging. **Data Specification:** * Issue Title: 'Feature: Add user activity timeline' * Assignee/Author: 'ui-developer' * Code Artifacts: {branch: 'feature/activity-timeline', commit_message: 'feat: Add activity timeline component', pr_title: 'feat: User Activity Timeline'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "title": "Feature: Add user activity timeline",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 12,
                    "assignees": [
                        "ui-developer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "feature/activity-timeline",
                    "message": "feat: Add activity timeline component",
                    "author": "ui-developer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "title": "feat: User Activity Timeline",
                    "body": "",
                    "head_branch": "feature/activity-timeline",
                    "base_branch": "main",
                    "author": "ui-developer"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "GetPullRequestMetadata",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 10
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "react-dashboard"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "react-dashboard",
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_6004",
        "instruction": "Your task is to handle the **Iterative Fix Policy** for the 'ml-pipeline' repository. A high-severity alert has been activated. The policy demands documenting all fix attempts, including incorrect ones, to ensure a clear audit trail. Your final deliverable consists of a report of all resolved alerts to audit the successful fix. **Compliance Specification:** The final condition must illustrate that a new 'high' severity alert was established and subsequently marked as 'fixed'. The incident is to be tracked by a single issue and should be closed only when the final fix is merged. The audit trail must demonstrate one pull request that remains open without merging (indicating a failed attempt) and another pull request that was successfully merged with the right fix. **Data Specification:** * Alert Details: {description: 'Data leakage in preprocessing script', file: 'src/preprocessing.py'} * Issue Title: 'Security: Remediate data leakage in preprocessing' * Assignee/Author: 'ml-engineer' * Incorrect Fix: {branch: 'fix/leak-attempt-1', commit_message: 'fix: Sanitize output data', pr_title: 'fix: Sanitize data'} * Correct Fix: {branch: 'fix/leak-attempt-2', commit_message: 'fix: Isolate data processing contexts', pr_title: 'fix: Isolate processing contexts'}",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "severity": "high",
                    "description": "Data leakage in preprocessing script",
                    "file": "src/preprocessing.py",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "title": "Security: Remediate data leakage in preprocessing",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "issue_number": 12,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "branch": "fix/leak-attempt-1",
                    "message": "fix: Sanitize output data",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "title": "fix: Sanitize data",
                    "body": "",
                    "head_branch": "fix/leak-attempt-1",
                    "base_branch": "main",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "branch": "fix/leak-attempt-2",
                    "message": "fix: Isolate data processing contexts",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "title": "fix: Isolate processing contexts",
                    "body": "",
                    "head_branch": "fix/leak-attempt-2",
                    "base_branch": "main",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "pr_number": 11,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "issue_number": 12
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "alert_number": 10
                },
            },
            {
                "name": "GetResolvedSecurityAlerts",
                "arguments": {
                    "repo_name": "ml-pipeline"
                }
            }
        ],
        "outputs": [
                [
                    {
                        "alert_id": "ALERT_ml-pipeline_007eb4d6",
                        "severity": "high",
                        "state": "fixed",
                        "resolved_at": "2025-08-26",
                        "description": "Data leakage in preprocessing script"
                    }
                ]
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_6005",
        "instruction": "Your task is to coordinate the **Security Audit Policy** for the 'flutter-finance-app' repository. The policy mandates a comprehensive audit of open and resolved alerts. Your final deliverable involves a dual report cataloguing both open and resolved alerts, offering a thorough security posture overview. **Compliance Specification:** The end condition must indicate that a new 'medium' severity alert was created and is 'open', and a new 'low' severity alert was formed and subsequently marked as 'fixed'. The resolution of the low-severity alert must be tracked through a closed issue and a merged pull request. **Data Specification:** * Open Alert: {description: 'Use of deprecated encryption algorithm', file: 'lib/crypto.dart'} * Resolved Alert: {description: 'Verbose error message in UI', file: 'lib/ui.dart'} * Tracking Issue Title: 'Fix verbose error message' * Code Artifacts: {branch: 'fix/verbose-error', commit_message: 'fix: Use generic error messages', pr_title: 'fix: Verbose errors'}",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "severity": "medium",
                    "description": "Use of deprecated encryption algorithm",
                    "file": "lib/crypto.dart",
                    "branch": "main"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "severity": "low",
                    "description": "Verbose error message in UI",
                    "file": "lib/ui.dart",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "title": "Fix verbose error message",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "issue_number": 12,
                    "assignees": [
                        "app-developer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "branch": "fix/verbose-error",
                    "message": "fix: Use generic error messages",
                    "author": "app-developer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "title": "fix: Verbose errors",
                    "body": "",
                    "head_branch": "fix/verbose-error",
                    "base_branch": "main",
                    "author": "app-developer"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "issue_number": 12
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "alert_number": 11
                },
            },
            {
                "name": "GetOpenSecurityAlerts",
                "arguments": {
                    "repo_name": "flutter-finance-app"
                },
            },
            {
                "name": "GetResolvedSecurityAlerts",
                "arguments": {
                    "repo_name": "flutter-finance-app"
                }
            }
        ],
        "outputs": [
                [
                    {
                        "alert_id": "ALERT_flutter-finance-app_klm123no",
                        "severity": "medium",
                        "state": "open",
                        "created_at": "2025-08-26",
                        "description": "Use of deprecated encryption algorithm"
                    }
                ],
                [
                    {
                        "alert_id": "ALERT_flutter-finance-app_pqr456st",
                        "severity": "low",
                        "state": "fixed",
                        "resolved_at": "2025-08-26",
                        "description": "Verbose error message in UI"
                    }
                ]
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_5001",
        "instruction": "Your responsibility is to handle the **CI/CD Pipeline Hardening Policy** for the 'infra-terraform' repository. A security assessment has pinpointed vulnerabilities that need to be mitigated. This policy mandates tracking these efforts via a primary epic and detailed sub-tasks, ensuring all code modifications are integrated into a single, reviewed pull request. Once completed, all related tracking artifacts must be closed. Utilize the provided data specification to align the repository with compliance requirements. Your final deliverable should be the repository's activity dashboard demonstrating the policy's execution and the repository's clean state. **Data Specification:** * **Epic:** {title: 'Q3 CI/CD Hardening Sprint', body: ''} * **Sub-Tasks:** [{title: 'Integrate SAST scanning in pipeline', body: ''}, {title: 'Enforce branch protection rules on main', body: ''}] * **Implementation:** {branch: 'feature/pipeline-hardening', commit_message: 'feat: Add SAST scanning and branch protection', pr_title: 'feat: Harden CI/CD Pipeline', pr_body: ''} * **Ownership:** {assignee: 'platform-team', author: 'platform-team'} * **Review:** {reviewer: 'security-group'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "Q3 CI/CD Hardening Sprint",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 12,
                    "assignees": [
                        "platform-team"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "Integrate SAST scanning in pipeline",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 13,
                    "assignees": [
                        "platform-team"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "Enforce branch protection rules on main",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 14,
                    "assignees": [
                        "platform-team"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "feature/pipeline-hardening",
                    "message": "feat: Add SAST scanning and branch protection",
                    "author": "platform-team"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "feat: Harden CI/CD Pipeline",
                    "body": "",
                    "head_branch": "feature/pipeline-hardening",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10,
                    "issue_number": 14
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10,
                    "reviewers": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 13
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 14
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "infra-terraform"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "infra-terraform",
                        "commits_count": 1,
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_5004",
        "instruction": "Your responsibility is to handle the **New Service Onboarding Policy**. The new service, 'recommendation-engine', is under development. This policy requires the creation of the repository and its initial code, along with setting up basic monitoring within the central 'k8s-monitoring' repository. Deliver a filtered list of issues from the monitoring repo to verify the creation of the setup tasks. **Compliance Specification:** The final state must confirm that the new 'recommendation-engine' repository has been created, with an initial merged pull request. Simultaneously, two new issues must be created and left 'open' in the 'k8s-monitoring' repository to ensure the new service is included in the monitoring stack. These monitoring issues must be appropriately labeled. **Data Specification:** * `recommendation-engine` Artifacts: {description: 'Recommendation engine service', private: True, issue_title: 'Initial service setup', branch: 'feature/initial-setup', commit_message: 'feat: Initial service boilerplate', pr_title: 'feat: Initial Setup', assignee: 'ml-engineer'} * `k8s-monitoring` Issues: [{title: 'Add recommendation-engine to Prometheus scrape configs', labels: ['monitoring', 'config'], assignee: 'infra-lead'}, {title: 'Create Grafana dashboard for recommendation-engine', labels: ['monitoring', 'dashboard'], assignee: 'infra-lead'}]",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "description": "Recommendation engine service",
                    "private": true
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "title": "Initial service setup",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "issue_number": 12,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "branch": "feature/initial-setup",
                    "message": "feat: Initial service boilerplate",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "title": "feat: Initial Setup",
                    "body": "",
                    "head_branch": "feature/initial-setup",
                    "base_branch": "main",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Add recommendation-engine to Prometheus scrape configs",
                    "body": "",
                    "labels": [
                        "monitoring",
                        "config"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 13,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "title": "Create Grafana dashboard for recommendation-engine",
                    "body": "",
                    "labels": [
                        "monitoring",
                        "dashboard"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "issue_number": 14,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "ListIssuesByLabel",
                "arguments": {
                    "repo_name": "k8s-monitoring",
                    "label": "monitoring"
                }
            }
        ],
        "outputs": [
                [
                    {
                        "issue_id": "ISSUE_k8s-monitoring_c0e36431",
                        "title": "Add recommendation-engine to Prometheus scrape configs",
                        "labels": [
                            "monitoring",
                            "config"
                        ],
                        "state": "open",
                        "report_date": "2025-08-26"
                    },
                    {
                        "issue_id": "ISSUE_k8s-monitoring_22cc09d5",
                        "title": "Create Grafana dashboard for recommendation-engine",
                        "labels": [
                            "monitoring",
                            "dashboard"
                        ],
                        "state": "open",
                        "report_date": "2025-08-26"
                    }
                ]
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_4002",
        "instruction": "Your task is to handle the **Merge Velocity Audit Policy** for the 'payments-service' repository. Management is concerned about the duration it takes to merge pull requests. This policy requires creating and merging two distinct pull requests to emulate various types of changes and then producing a report on the average merge time. Your final deliverable is this report on the merge times. **Compliance Specification:** The final outcome must indicate that two distinct workflows were completed. Each workflow must entail a dedicated issue that is closed and a pull request that is merged. One workflow is assigned to a feature, and the other is for a bug fix. **Data Specification:** * Author/Assignee: 'server-main' * Feature Artifacts: {issue_title: 'Add support for a new payment gateway', branch: 'feature/new-gateway', commit_message: 'feat: Integrate new gateway API', pr_title: 'feat: New Gateway'} * Bugfix Artifacts: {issue_title: 'Fix currency formatting for negative values', branch: 'fix/currency-format', commit_message: 'fix: Handle negative currency values', pr_title: 'fix: Negative Currency'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Add support for a new payment gateway",
                    "body": ""
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "feature/new-gateway",
                    "message": "feat: Integrate new gateway API",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "feat: New Gateway",
                    "body": "",
                    "head_branch": "feature/new-gateway",
                    "base_branch": "main",
                    "author": "server-main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Fix currency formatting for negative values",
                    "body": ""
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "fix/currency-format",
                    "message": "fix: Handle negative currency values",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "fix: Negative Currency",
                    "body": "",
                    "head_branch": "fix/currency-format",
                    "base_branch": "main",
                    "author": "server-main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 11,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 13
                },
            },
            {
                "name": "GetPullRequestMergeTimeReport",
                "arguments": {
                    "repo_name": "payments-service"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "payments-service",
                    "merged_pr_count": 2,
                    "average_merge_time": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_4003",
        "instruction": "Your task is to handle the **Incident Triage Policy** for the 'infra-terraform' repository. A crucial security alert has been raised. This policy mandates creating a main incident issue and a sub-task for the resolution, implementing the fix, and ensuring all artifacts are correctly managed. You must utilize the provided **Incident Manifest** to generate all necessary artifacts. Your final deliverable is a health summary of the repository verifying that the incident was completely resolved. **Compliance Specification:** The final state must indicate that a new critical security alert was raised and subsequently marked as 'fixed'. Both a main incident issue and a sub-task issue for the fix must be 'closed'. The fix should be applied on a feature branch and merged via a pull request. This pull request must be associated with both the main incident issue and the sub-task issue. **Incident Manifest:** * **Alert Details:** {description: 'IAM role has excessive privileges', file: 'iam.tf'} * **Incident Issue:** {title: 'Incident: Overly permissive IAM role detected', body: ''} * **Fix-Task Issue:** {title: 'Task: Reduce IAM role permissions', body: ''} * **Ownership:** {assignee: 'platform-team', author: 'platform-team'} * **Code Artifacts:** {branch: 'fix/iam-permissions', commit_message: 'fix: Scope down IAM role to least privilege', pr_title: 'fix: Least Privilege for IAM Role', pr_body: ''}",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "severity": "critical",
                    "description": "IAM role has excessive privileges",
                    "file": "iam.tf",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "Incident: Overly permissive IAM role detected",
                    "body": ""
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "Task: Reduce IAM role permissions",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 12,
                    "assignees": [
                        "platform-team"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 13,
                    "assignees": [
                        "platform-team"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "fix/iam-permissions",
                    "message": "fix: Scope down IAM role to least privilege",
                    "author": "platform-team"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "fix: Least Privilege for IAM Role",
                    "body": "",
                    "head_branch": "fix/iam-permissions",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 12
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 13
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "alert_number": 10
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "infra-terraform"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "infra-terraform",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_4005",
        "instruction": "Your task involves handling the **Label-Based Issue Prioritization Policy** for the 'ui-kit' repository. A product manager is in the process of organizing the backlog for the next design sprint. The policy mandates the creation of several new issues with distinct labels followed by compiling a report focused solely on design-related tasks. Ultimately, your deliverable is the filtered list of these design issues. **Compliance Specification:** The end state must demonstrate that four new issues have been created and assigned. Two of these issues are to carry the 'design' label, one the 'bug' label, and another the 'enhancement' label. The issue tagged with 'bug' must be fully addressed, including merging a pull request and marking it as closed. The remaining three issues should still be open. **Data Specification:** * Design Issues: [{title: 'Redesign Card component shadows', assignee: 'design-lead', labels: ['design', 'ui']}, {title: 'Create new color palette for dark mode', assignee: 'design-lead', labels: ['design', 'theme']}] * Bug Issue: {title: 'Button click area is too small', assignee: 'ui-dev', labels: ['bug']} * Enhancement Issue: {title: 'Add new icon set for social media', assignee: 'ui-dev', labels: ['enhancement']} * Code Artifacts: {branch: 'fix/button-click-area', commit_message: 'fix: Increase padding on button component', pr_title: 'fix: Button click area'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Redesign Card component shadows",
                    "body": "",
                    "labels": [
                        "design",
                        "ui"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12,
                    "assignees": [
                        "design-lead"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Create new color palette for dark mode",
                    "body": "",
                    "labels": [
                        "design",
                        "theme"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 13,
                    "assignees": [
                        "design-lead"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Add new icon set for social media",
                    "body": "",
                    "labels": [
                        "enhancement"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 14,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Button click area is too small",
                    "body": "",
                    "labels": [
                        "bug"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 15,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "fix/button-click-area",
                    "message": "fix: Increase padding on button component",
                    "author": "ui-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "fix: Button click area",
                    "body": "",
                    "head_branch": "fix/button-click-area",
                    "base_branch": "main",
                    "author": "ui-dev"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 15
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 15
                },
            },
            {
                "name": "ListIssuesByLabel",
                "arguments": {
                    "repo_name": "ui-kit",
                    "label": "design"
                }
            }
        ],
        "outputs": [
                [
                    {
                        "issue_id": "ISSUE_ui-kit_2bb1b710",
                        "title": "Redesign Card component shadows",
                        "labels": [
                            "design",
                            "ui"
                        ],
                        "state": "open",
                        "report_date": "2025-08-26"
                    },
                    {
                        "issue_id": "ISSUE_ui-kit_e9e3e3d2",
                        "title": "Create new color palette for dark mode",
                        "labels": [
                            "design",
                            "theme"
                        ],
                        "state": "open",
                        "report_date": "2025-08-26"
                    }
                ]
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_3001",
        "instruction": "Your task is to carry out the **Automated Security Rollback Policy** for the 'payments-service' repository. A recently added commit has resulted in a critical vulnerability. The policy necessitates an immediate and total rollback of the change. The end deliverable is a comprehensive report certifying that the repository is secure. **Compliance Specification:** The final state needs to reflect that a new critical security alert was created and subsequently marked as 'fixed'. A tracking issue for the incident is to be 'closed'. The rollback must conclude with the merging of a pull request that effectively reverts the faulty commit. **Data Specification:** * Bad Commit Message: 'feat: Add new payment processor with RCE vulnerability' * Alert Details: {description: 'Remote Code Execution in new payment processor', file: 'src/payments.js'} * Incident Tracking: {issue_title: 'EMERGENCY: Revert critical RCE vulnerability', assignee: 'server-main'} * Revert Artifacts: {branch: 'hotfix/revert-rce', commit_message: 'revert: Revert payment processor with RCE vulnerability', pr_title: 'hotfix: Revert RCE Vulnerability', reviewer: 'tech-lead-tara'}",
        "actions": [
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "main",
                    "message": "feat: Add new payment processor with RCE vulnerability",
                    "author": "server-main"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "payments-service",
                    "severity": "critical",
                    "description": "Remote Code Execution in new payment processor",
                    "file": "src/payments.js",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "EMERGENCY: Revert critical RCE vulnerability",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "hotfix/revert-rce",
                    "message": "revert: Revert payment processor with RCE vulnerability",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "hotfix: Revert RCE Vulnerability",
                    "body": "",
                    "head_branch": "hotfix/revert-rce",
                    "base_branch": "main",
                    "author": "server-main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "payments-service",
                    "alert_number": 10
                },
            },
            {
                "name": "GenerateEndToEndReport",
                "arguments": {
                    "repo_name": "payments-service"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "payments-service",
                    "commits_count": 2,
                    "open_issues": 0,
                    "merged_prs": 1,
                    "open_alerts": 0,
                    "releases_count": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_3002",
        "instruction": "Your assignment involves handling the **Cross-Repo Incompatibility Policy**. In 'react-dashboard', a feature under development has led to a high-severity alert due to an incompatibility with 'ui-kit'. According to the policy, you must halt the feature work, resolve the root problem in the dependency ('ui-kit'), and then continue the feature development. Your final task is to provide cross-entity reports for both repositories. **Compliance Specification:** In the final stage, there should be evidence that a new 'high' severity alert was generated in 'react-dashboard' and subsequently marked as 'fixed'. A tracking issue in 'ui-kit' needs to be 'closed' with its resolution merged through a pull request. Afterwards, the initial feature work in 'react-dashboard', which should also be linked to an issue, must be finalized and merged via a separate pull request. All associated issues have to be closed. **Data Specification:** * `react-dashboard` Artifacts: {alert_description: 'Component crashing due to ui-kit incompatibility', alert_file: 'src/components/NewFeature.tsx', issue_title: 'Feature: New analytics chart', branch: 'feature/analytics-chart', initial_commit: 'feat: Initial analytics chart structure', final_commit: 'fix: Update component to support new ui-kit version'} * `ui-kit` Artifacts: {issue_title: 'Bug: Prop validation fails in Card component', branch: 'fix/prop-validation', commit_message: 'fix: Add backward compatibility for Card props', pr_title: 'fix: Prop validation'}",
        "actions": [
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "feature/analytics-chart",
                    "message": "feat: Initial analytics chart structure",
                    "author": "ui-developer"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "severity": "high",
                    "description": "Component crashing due to ui-kit incompatibility",
                    "file": "src/components/NewFeature.tsx",
                    "branch": "feature/analytics-chart"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "title": "Feature: New analytics chart",
                    "body": ""
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Bug: Prop validation fails in Card component",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 13,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "fix/prop-validation",
                    "message": "fix: Add backward compatibility for Card props",
                    "author": "ui-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "fix: Prop validation",
                    "body": "",
                    "head_branch": "fix/prop-validation",
                    "base_branch": "main",
                    "author": "ui-dev"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 13
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 12,
                    "assignees": [
                        "ui-developer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "feature/analytics-chart",
                    "message": "fix: Update component to support new ui-kit version",
                    "author": "ui-developer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "title": "Feature: New analytics chart",
                    "body": "",
                    "head_branch": "feature/analytics-chart",
                    "base_branch": "main",
                    "author": "ui-developer"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 12
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "alert_number": 10
                },
            },
            {
                "name": "GetCrossEntityReport",
                "arguments": {
                    "repo_name": "react-dashboard"
                },
            },
            {
                "name": "GetCrossEntityReport",
                "arguments": {
                    "repo_name": "ui-kit"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "react-dashboard",
                    "open_issues": 0,
                    "merged_prs": 1,
                    "recent_commits": 2,
                    "open_alerts": 0,
                    "last_deployment": "none",
                    "report_date": "2025-08-26"
                },
                {
                    "repo": "ui-kit",
                    "open_issues": 0,
                    "merged_prs": 1,
                    "recent_commits": 1,
                    "open_alerts": 0,
                    "last_deployment": "none",
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_3003",
        "instruction": "Your assignment is to coordinate the **Bug Triage and Audit Policy** for the 'acme-webapp' repository. A critical bug reported by a user must be divided into sub-tasks and fixed. The policy mandates a clear audit line from the bug report to the final code integration. Your task is to deliver an audit report that connects the fix commit to the pull request. **Compliance Specification:** In the end, documentation must show a main epic issue was created to follow the user report, and two sub-task issues (one for investigation, one for the fix) were generated and eventually closed. The bug fix must be carried out on a feature branch and merged using a pull request. This pull request should be linked to all three issues (the epic and the two sub-tasks). **Data Specification:** * Epic Title: 'User Report: Login page not working on Safari' * Assignee for Epic: 'tech-lead-tara' * Sub-Task Titles: ['Investigate Safari-specific CSS issue', 'Fix CSS rendering bug on Safari'] * Assignee for Sub-Tasks: 'maya-w' * Code Artifacts: {branch: 'bugfix/safari-css', commit_message: 'fix: Add vendor prefixes for Safari CSS compatibility', pr_title: 'fix: Safari CSS rendering', author: 'maya-w'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "User Report: Login page not working on Safari",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12,
                    "assignees": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Investigate Safari-specific CSS issue",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 13,
                    "assignees": [
                        "maya-w"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Fix CSS rendering bug on Safari",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 14,
                    "assignees": [
                        "maya-w"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "bugfix/safari-css",
                    "message": "fix: Add vendor prefixes for Safari CSS compatibility",
                    "author": "maya-w"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "fix: Safari CSS rendering",
                    "body": "",
                    "head_branch": "bugfix/safari-css",
                    "base_branch": "main",
                    "author": "maya-w"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10,
                    "issue_number": 14
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 13
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 14
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12
                },
            },
            {
                "name": "MapCommitsToPullRequests",
                "arguments": {
                    "repo_name": "acme-webapp"
                }
            }
        ],
        "outputs": [
                [
                    {
                        "pr_id": "PR_acme-webapp_e47660a5",
                        "commit_ids": [
                            "5a0cfd3926b4"
                        ],
                        "report_date": "2025-08-26"
                    }
                ]
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_3005",
        "instruction": "Handle the implementation of the **Post-Incident Analysis Policy**. An incident has been resolved within the 'infra-terraform' repository, requiring a report to audit the response timeline. Your final task is to prepare an issue aging report to ensure the incident issue was promptly resolved. **Compliance Specification:** The repository's final state must detail the entire lifecycle of an incident resolution. This encompasses creating a critical security alert, issuing a tracking issue for the incident, committing and pull requesting the fix, closing the issue, and resolving the alert. **Data Specification:** * Alert: {description: 'S3 Bucket exposed publicly', file: 's3.tf', severity: 'critical'} * Issue Title: 'Incident: Public S3 Bucket Exposure' * Code Artifacts: {branch: 'hotfix/s3-policy', commit_message: 'fix: Apply private ACL to S3 bucket', pr_title: 'fix: Correct S3 bucket policy'} * Assignee/Author: 'platform-team'",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "severity": "critical",
                    "description": "S3 Bucket exposed publicly",
                    "file": "s3.tf",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "Incident: Public S3 Bucket Exposure",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 12,
                    "assignees": [
                        "platform-team"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "branch": "hotfix/s3-policy",
                    "message": "fix: Apply private ACL to S3 bucket",
                    "author": "platform-team"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "title": "fix: Correct S3 bucket policy",
                    "body": "",
                    "head_branch": "hotfix/s3-policy",
                    "base_branch": "main",
                    "author": "platform-team"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "issue_number": 12
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "infra-terraform",
                    "alert_number": 10
                },
            },
            {
                "name": "GetIssueAgingReport",
                "arguments": {
                    "repo_name": "infra-terraform"
                }
            }
        ],
        "outputs": [
                [
                    {
                        "issue_id": "ISSUE_infra-terraform_b4e9b8f2",
                        "title": "Incident: Public S3 Bucket Exposure",
                        "state": "closed",
                        "created_at": "2025-08-26",
                        "days_open": 0,
                        "report_date": "2025-08-26"
                    }
                ]
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_2001",
        "instruction": "Coordinate the implementation of the **Multi-Stage Feature Rollout Policy**. A new feature within 'flutter-finance-app' requires an updated dependency from 'utils-js'. The policy necessitates that both the dependency is updated and the new feature is integrated, culminating in the application's deployment to a 'staging-android' environment with a formal release. Your final duty is to compile a commit list for the 'flutter-finance-app' repository to review the changes. **Compliance Specification:** The ecosystem's final state must demonstrate the completion of this task across both repositories. Ensure closure of all related tracking issues, merging of all pull requests, and release of new versions for both repositories. The final application must be deployed as specified to the staging environment. **Data Specification:** * `utils-js` Artifacts: {issue_title: 'Add new array utility function', branch: 'feature/array-util', commit_message: 'feat: Add advanced array sorting utility', pr_title: 'feat: Add array utility', release_version: 'v1.1.0', release_description: 'Adds new array utilities.'} * `flutter-finance-app` Artifacts: {issue_title: 'Integrate new array utility from utils-js', branch: 'feature/new-integration', commit_message: 'feat: Integrate utils-js v1.1.0 for improved performance', pr_title: 'feat: Integrate new utils', release_version: 'v1.3.0', release_description: 'Integrates new dependency for performance improvements.'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "Add new array utility function",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 12,
                    "assignees": [
                        "ryan-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "utils-js",
                    "branch": "feature/array-util",
                    "message": "feat: Add advanced array sorting utility",
                    "author": "ryan-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "feat: Add array utility",
                    "body": "",
                    "head_branch": "feature/array-util",
                    "base_branch": "master",
                    "author": "ryan-dev"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "utils-js",
                    "version": "v1.1.0",
                    "description": "Adds new array utilities."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "title": "Integrate new array utility from utils-js",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "issue_number": 13,
                    "assignees": [
                        "app-developer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "branch": "feature/new-integration",
                    "message": "feat: Integrate utils-js v1.1.0 for improved performance",
                    "author": "app-developer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "title": "feat: Integrate new utils",
                    "body": "",
                    "head_branch": "feature/new-integration",
                    "base_branch": "main",
                    "author": "app-developer"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "issue_number": 13
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "environment": "staging-android"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "version": "v1.3.0",
                    "description": "Integrates new dependency for performance improvements."
                },
            },
            {
                "name": "ListCommitsByDateRange",
                "arguments": {
                    "repo_name": "flutter-finance-app",
                    "start_date": "2025-08-26",
                    "end_date": "2025-08-26"
                }
            }
        ],
        "outputs": [
                [
                    {
                        "commit_id": "387ef3422d8f",
                        "repo": "flutter-finance-app",
                        "message": "feat: Integrate utils-js v1.1.0 for improved performance",
                        "author": "app-developer",
                        "timestamp": "2025-08-26",
                        "report_date": "2025-08-26"
                    }
                ]
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_2002",
        "instruction": "You are tasked with handling the **Cross-Team Bug Triage Policy**. A severe bug reported in 'payments-service' has been linked to a core issue in 'acme-webapp'. This policy mandates a coordinated resolution, commencing with the dependency. It is crucial that the concluding state of both repositories aligns with the **Triage Specification**. Your ultimate output should include a series of cross-entity reports for both repositories, providing a comprehensive overview of the resolution. **Triage Specification:** Ensure the final state reflects that the root issue in 'acme-webapp' was identified and fixed initially, this involves closing an issue and merging a pull request with the hotfix. Next, the 'payments-service' must be revised to incorporate this corrected version, which also needs to be tracked through a closed issue and a merged pull request. **Data Specification:** * `payments-service` Artifacts: {issue_title: 'Bug: Transaction processing fails for certain card types', pr_title: 'chore: Update dependency to acme-webapp', branch: 'fix/dependency-update', commit_message: 'chore: Update acme-webapp to latest version', author: 'server-main', assignee: 'server-main'} * `acme-webapp` Artifacts: {issue_title: 'Hotfix: Null pointer exception in input handler', pr_title: 'fix: Null pointer in handler', branch: 'hotfix/null-pointer', commit_message: 'fix: Add null check to input handler', author: 'maya-w', assignee: 'maya-w'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Bug: Transaction processing fails for certain card types",
                    "body": ""
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Hotfix: Null pointer exception in input handler",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 13,
                    "assignees": [
                        "maya-w"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "hotfix/null-pointer",
                    "message": "fix: Add null check to input handler",
                    "author": "maya-w"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "fix: Null pointer in handler",
                    "body": "",
                    "head_branch": "hotfix/null-pointer",
                    "base_branch": "main",
                    "author": "maya-w"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 13
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "fix/dependency-update",
                    "message": "chore: Update acme-webapp to latest version",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "chore: Update dependency to acme-webapp",
                    "body": "",
                    "head_branch": "fix/dependency-update",
                    "base_branch": "main",
                    "author": "server-main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 11,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 12
                },
            },
            {
                "name": "GetCrossEntityReport",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "GetCrossEntityReport",
                "arguments": {
                    "repo_name": "payments-service"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "acme-webapp",
                    "open_issues": 0,
                    "merged_prs": 1,
                    "recent_commits": 1,
                    "open_alerts": 0,
                    "last_deployment": "none",
                    "report_date": "2025-08-26"
                },
                {
                    "repo": "payments-service",
                    "open_issues": 0,
                    "merged_prs": 1,
                    "recent_commits": 1,
                    "open_alerts": 0,
                    "last_deployment": "none",
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_2005",
        "instruction": "You are responsible for coordinating the **Repository Health Remediation Policy**. It has been recognized that the 'security-scanner' repository requires a plan to mitigate known structural issues. This policy necessitates the formulation and documentation of a formal approach. Your final output should be a listing of open issues for the repository, verifying that the remediation plan has been accurately commenced. **Compliance Specification:** For the final state to be valid, an epic issue must be created to monitor the overall remediation strategy. Additionally, two sub-task issues should be opened for the most pressing two concerns. All three newly created issues must remain open and be assigned to the correct team lead. **Data Specification:** * Target Repository: 'security-scanner' * Team Lead: 'security-group' * Epic Title: 'Q3 Remediation Plan for security-scanner' * Sub-Task Titles: ['Address high false-positive rate for XSS detection', 'Improve performance for large codebases']",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Q3 Remediation Plan for security-scanner",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Address high false-positive rate for XSS detection",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Improve performance for large codebases",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 14,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "GetOpenIssues",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                [
                    {
                        "issue_id": "ISSUE_security-scanner_ed799e7d",
                        "title": "Q3 Remediation Plan for security-scanner",
                        "state": "open",
                        "assignees": [
                            "security-group"
                        ],
                        "labels": [],
                        "created_at": "2025-08-26",
                        "report_date": "2025-08-26"
                    },
                    {
                        "issue_id": "ISSUE_security-scanner_7636a0bb",
                        "title": "Address high false-positive rate for XSS detection",
                        "state": "open",
                        "assignees": [
                            "security-group"
                        ],
                        "labels": [],
                        "created_at": "2025-08-26",
                        "report_date": "2025-08-26"
                    },
                    {
                        "issue_id": "ISSUE_security-scanner_292c349e",
                        "title": "Improve performance for large codebases",
                        "state": "open",
                        "assignees": [
                            "security-group"
                        ],
                        "labels": [],
                        "created_at": "2025-08-26",
                        "report_date": "2025-08-26"
                    }
                ]
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_1002",
        "instruction": "Your task is to handle the **Code Cleanup and Deprecation Policy** for the 'utils-js' repository. The objective is to eliminate the deprecated 'formatCurrency' function from the codebase. The repository's final state must demonstrate that this deprecation was officially tracked and completed through the standard development lifecycle of issues and pull requests. Your ultimate deliverable is the repository's risk score to affirm that the cleanup was accomplished successfully.",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "Deprecate formatCurrency in src/utils/format.js",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 12,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "Remove formatCurrency test in test/format.test.js",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 13,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "utils-js",
                    "branch": "refactor/remove-currency-func",
                    "message": "refactor: Remove deprecated formatCurrency function",
                    "author": "intern-emma"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "title": "refactor: Remove formatCurrency",
                    "body": "",
                    "head_branch": "refactor/remove-currency-func",
                    "base_branch": "master",
                    "author": "intern-emma"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "utils-js",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 12
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "utils-js",
                    "issue_number": 13
                },
            },
            {
                "name": "GetRepositoryRiskScore",
                "arguments": {
                    "repo_name": "utils-js"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "utils-js",
                    "open_alerts_count": 0,
                    "risk_score": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_1004",
        "instruction": "Your responsibility is to manage the **Model Drift Retraining Policy** for the 'ml-pipeline' repository. The policy is activated when performance degradation is observed in a production model. You must ensure the repository's condition aligns with the **Retraining Specification**, which involves updating the model, releasing a new version, and deploying it. Your concluding deliverable is the issue aging report to verify swift tracking and resolution of the incident. **Retraining Specification:** The policy mandates that an incident be tracked via an issue, which must be closed upon resolution. A fixed code including the updated model parameters must be applied on a feature branch and merged through a pull request. A new hotfix version of the model must be released, and its deployment to the 'production-model-serving' environment must be logged. **Data Specification:** * Issue Title: 'Incident: Model performance degraded in production' * Assignee/Author: 'ml-engineer' * Code Artifacts: {branch: 'hotfix/retrain-model', commit_message: 'refactor: Update model with new training data', pr_title: 'fix: Retrain production model'} * Release Details: {version: 'v1.3.1', description: 'Hotfix release with retrained model.'}",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "title": "Incident: Model performance degraded in production",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "issue_number": 12,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "branch": "hotfix/retrain-model",
                    "message": "refactor: Update model with new training data",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "title": "fix: Retrain production model",
                    "body": "",
                    "head_branch": "hotfix/retrain-model",
                    "base_branch": "main",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "version": "v1.3.1",
                    "description": "Hotfix release with retrained model."
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "ml-pipeline",
                    "environment": "production-model-serving"
                },
            },
            {
                "name": "GetIssueAgingReport",
                "arguments": {
                    "repo_name": "ml-pipeline"
                }
            }
        ],
        "outputs": [
                [
                    {
                        "issue_id": "ISSUE_ml-pipeline_d02d357f",
                        "title": "Incident: Model performance degraded in production",
                        "state": "closed",
                        "created_at": "2025-08-26",
                        "days_open": 0,
                        "report_date": "2025-08-26"
                    }
                ]
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_901",
        "instruction": "Handle the **Security Incident Response and Hardening Policy** due to a newly discovered vulnerability. Your task is to ensure the incident is completely resolved and preventive measures are established, aligning both the 'payments-service' and 'security-scanner' repositories with the official **Incident Hardening Specification**. Your concluding delivery involves health summaries for both repositories confirming the policy's successful execution. **Incident Hardening Specification:** The policy mandates that the identified vulnerability in 'payments-service' is fully patched and a hotfix is issued. Simultaneously, the 'security-scanner' must be enhanced with new detection rules for this vulnerability class and receive an updated version release. All remediation and development work must be documented through issues and pull requests, which need to be closed and merged in that order. The initial security alert must be designated as resolved. **Data Specification:** * Vulnerability Details: {description: 'Remote Code Execution via deserialization', file: 'src/server.ts'} * `payments-service` Artifacts: {issue_title: 'Patch Critical RCE Vulnerability', pr_title: 'fix: Patch RCE vulnerability in deserialization module', branch: 'hotfix/rce-patch', release_version: 'v0.2.1', release_description: 'Security patch for critical RCE vulnerability.', assignee: 'server-main'} * `security-scanner` Artifacts: {issue_title: 'Enhance scanner with RCE detection rule', pr_title: 'feat: Add deserialization RCE detection rule', branch: 'feature/rce-detection', release_version: 'v0.7.0', release_description: 'Adds detection for deserialization-based RCE.', assignee: 'security-group'}",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "payments-service",
                    "severity": "critical",
                    "description": "Remote Code Execution via deserialization",
                    "file": "src/server.ts",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Enhance scanner with RCE detection rule",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "feature/rce-detection",
                    "message": "feat: Add deserialization RCE detection rule",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "feat: Add deserialization RCE detection rule",
                    "body": "",
                    "head_branch": "feature/rce-detection",
                    "base_branch": "main"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "security-scanner",
                    "version": "v0.7.0",
                    "description": "Adds detection for deserialization-based RCE."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "Patch Critical RCE Vulnerability",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 13,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "payments-service",
                    "branch": "hotfix/rce-patch",
                    "message": "fix: Patch RCE vulnerability in deserialization module",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "title": "fix: Patch RCE vulnerability in deserialization module",
                    "body": "",
                    "head_branch": "hotfix/rce-patch",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 11,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "payments-service",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "payments-service",
                    "issue_number": 13
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "payments-service",
                    "alert_number": 10
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "payments-service",
                    "version": "v0.2.1",
                    "description": "Security patch for critical RCE vulnerability."
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "payments-service"
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "payments-service",
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                },
                {
                    "repo": "security-scanner",
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_902",
        "instruction": "Oversee the **New Service Onboarding with Dependency Integration Policy**. The process is initiated when a new service, 'recommendation-engine', demands a modification in an existing shared service, 'security-scanner', for proper functionality. You must coordinate the entire lifecycle for both repositories, ensuring their final states align with the official **Cross-Repo Integration Specification**. Your ultimate report is a compilation of health summaries for both repositories to validate a successful and seamless integration. **Cross-Repo Integration Specification:** * **'security-scanner' Final State:** A tracking issue for implementing custom rules for the new service must be closed. The corresponding pull request from a feature branch must be merged. A new release 'v0.6.0' with the description 'Adds support for recommendation-engine.' must be published. * **'recommendation-engine' Final State:** The repository should be established as 'private' with the description 'Collaborative filtering recommendation engine.'. A tracking issue for the initial model implementation must be closed, and its associated pull request from a feature branch must be merged. The merged code must include commits for both the initial model structure and its integration with the updated 'security-scanner'.",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "description": "Collaborative filtering recommendation engine.",
                    "private": true
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Add custom rules for recommendation-engine",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "feature/reco-engine-rules",
                    "message": "feat: Add custom security rules for new recommendation engine",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "feat: Add recommendation-engine security rules",
                    "body": "",
                    "head_branch": "feature/reco-engine-rules",
                    "base_branch": "main"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "security-scanner",
                    "version": "v0.6.0",
                    "description": "Adds support for recommendation-engine."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "title": "Implement initial collaborative filtering model",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "issue_number": 13,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "branch": "feature/collab-filter",
                    "message": "feat: Add initial model structure",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "branch": "feature/collab-filter",
                    "message": "refactor: Integrate with security-scanner v0.6.0",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "title": "feat: Initial collaborative filtering model",
                    "body": "",
                    "head_branch": "feature/collab-filter",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "pr_number": 11,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "recommendation-engine",
                    "issue_number": 13
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "recommendation-engine"
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "recommendation-engine",
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                },
                {
                    "repo": "security-scanner",
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_903",
        "instruction": "Your primary strategic goal involves handling the **Quarterly Security Backlog Drive Policy** for the 'security-scanner' repository. This policy calls for a layered remediation process based on the severity of vulnerabilities. Your responsibility is to align the repository with this tiered approach as outlined in the official **Backlog Drive Compliance Specification**. The final output required from you is the repository's activity dashboard verifying the policy's successful implementation. **Backlog Drive Compliance Specification:** * **Tracking Artifacts:** Ensure the final state includes an 'open' epic issue titled 'Q3 Security Backlog Drive', assigned to 'tech-lead-tara'. * **Critical Vulnerability:** Confirm the repository displays that a new critical alert for 'Improper Input Validation' in 'src/api.rs' has been fully addressed. This necessitates its tracking issue ('Fix Critical: Improper Input Validation') being 'closed', alongside merging its related pull request ('fix: Add strict input validation') from branch 'fix/input-validation'. * **High Vulnerability:** A new high-severity alert for 'Hardcoded Secret' in 'src/config.rs' requires active remediation. This necessitates keeping an 'open' tracking issue ('Remediate High: Hardcoded Secret') and an 'open' pull request ('WIP: Remove hardcoded secret') from branch 'fix/hardcoded-secret'. * **Medium Vulnerability:** It is necessary to track a new medium-severity alert for 'Verbose Error Messages' in 'src/errors.rs'. This requires maintaining an 'open' tracking issue ('Track Medium: Verbose Error Messages') assigned to 'intern-emma'.",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Q3 Security Backlog Drive",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "severity": "critical",
                    "description": "Improper Input Validation",
                    "file": "src/api.rs",
                    "branch": "main"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "severity": "high",
                    "description": "Hardcoded Secret",
                    "file": "src/config.rs",
                    "branch": "main"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "severity": "medium",
                    "description": "Verbose Error Messages",
                    "file": "src/errors.rs",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Fix Critical: Improper Input Validation",
                    "body": ""
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "fix/input-validation",
                    "message": "fix: Add strict input validation",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "fix: Add strict input validation",
                    "body": "",
                    "head_branch": "fix/input-validation",
                    "base_branch": "main"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "alert_number": 10
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Remediate High: Hardcoded Secret",
                    "body": ""
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "fix/hardcoded-secret",
                    "message": "WIP: Remove hardcoded secret",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "WIP: Remove hardcoded secret",
                    "body": "",
                    "head_branch": "fix/hardcoded-secret",
                    "base_branch": "main"
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 11,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Track Medium: Verbose Error Messages",
                    "body": ""
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 15,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "security-scanner",
                    "commits_count": 2,
                    "open_issues": 3,
                    "open_prs": 1,
                    "open_alerts_by_severity": {
                        "critical": 0,
                        "high": 1,
                        "medium": 1,
                        "low": 0,
                        "unknown": 0
                    },
                    "open_alerts": 2,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_904",
        "instruction": "Your main task is to coordinate the **Service Sunset Policy** for a newly created repository named 'legacy-api'. This policy oversees the structured deactivation of a service, ensuring all tracking artifacts are properly administered and a wrap-up version is released. You must ensure the repository's state adheres to the official **Sunset Compliance Specification**. Your ultimate deliverable is the repository's health summary, confirming a smooth shutdown without any pending issues. **Sunset Compliance Specification:** * **Required Repository State:** * A 'private' repository should exist with the description: 'Legacy API for sunsetting.' * **Required State of Tracking Artifacts:** * The main epic issue titled 'Epic: Sunset Legacy API', assigned to 'tech-lead-tara', needs to be in a 'closed' state. * A tracking issue labeled 'Task: Add deprecation notice to API', assigned to 'server-main', must be 'closed'. * **Required State of Code and Releases:** * Ensure a pull request titled 'feat: Add deprecation notice' from the 'feature/deprecation-notice' branch is 'merged'. This PR should be linked to the 'Task: Add deprecation notice to API' issue. * A final, stable release 'v2.0.0' described as 'Final release with deprecation notice.' needs to be published.",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "legacy-api",
                    "description": "Legacy API for sunsetting.",
                    "private": true
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "legacy-api",
                    "title": "Epic: Sunset Legacy API",
                    "body": "",
                    "labels": [
                        "epic",
                        "deprecation"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "legacy-api",
                    "issue_number": 12,
                    "assignees": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "legacy-api",
                    "title": "Task: Add deprecation notice to API",
                    "body": "",
                    "labels": [
                        "task"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "legacy-api",
                    "issue_number": 13,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "legacy-api",
                    "branch": "feature/deprecation-notice",
                    "message": "feat: Add deprecation notice",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "legacy-api",
                    "title": "feat: Add deprecation notice",
                    "body": "",
                    "head_branch": "feature/deprecation-notice",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "legacy-api",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "legacy-api",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "legacy-api",
                    "issue_number": 13
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "legacy-api",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "legacy-api",
                    "version": "v2.0.0",
                    "description": "Final release with deprecation notice."
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "legacy-api"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "legacy-api",
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_801",
        "instruction": "Your main strategic aim is to oversee the establishment of a new hire's initial project in full accordance with the company's **New Hire Onboarding Policy**. This policy requires that a specific starter repository be created with a well-organized list of onboarding tasks. It is your duty to confirm that the final state of the new repository precisely matches the official **Onboarding Compliance Specification** detailed below. Your final submission should be the repository's activity dashboard, serving as the formal record of policy adherence. **Onboarding Compliance Specification for 'new-hire-starter-project':** * **Required Repository State:** * Must remain 'private' with description: 'Starter project for new engineering hires.' * **Required State of Onboarding Issues:** * A primary epic titled 'Onboarding Plan for new hire' (body: 'Main epic to track the new hire onboarding process.', labels: ['onboarding', 'epic'], assigned to 'intern-emma') is required to be 'open'. * A sub-task titled 'Task 1: Set up local development environment' (body: 'Sub-task to track local environment setup.', labels: ['onboarding', 'setup'], assigned to 'intern-emma') must remain 'open'. * A sub-task titled 'Task 2: Complete first coding task' (body: 'Sub-task for the first coding assignment.', labels: ['onboarding', 'coding-task'], assigned to 'intern-emma') must be set to 'closed'. * A sub-task titled 'Task 3: Schedule team introduction meetings' (body: 'Sub-task to schedule introductory meetings.', labels: ['onboarding', 'meetings'], assigned to 'intern-emma') must be 'open'. * **Required State of First Coding Task:** * A pull request titled 'feat: Add welcome message endpoint' (body: 'PR for the first coding task, implementing the /hello endpoint.', reviewed by ['tech-lead-tara']) should be 'merged' into 'main', associated with the coding task issue, and include a commit 'feat: Implement /hello endpoint' by 'intern-emma' from the 'feature/welcome-endpoint' branch.",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "description": "Starter project for new engineering hires.",
                    "private": true
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "title": "Onboarding Plan for new hire",
                    "body": "Main epic to track the new hire onboarding process.",
                    "labels": [
                        "onboarding",
                        "epic"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "issue_number": 12,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "title": "Task 1: Set up local development environment",
                    "body": "Sub-task to track local environment setup.",
                    "labels": [
                        "onboarding",
                        "setup"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "issue_number": 13,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "title": "Task 2: Complete first coding task",
                    "body": "Sub-task for the first coding assignment.",
                    "labels": [
                        "onboarding",
                        "coding-task"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "issue_number": 14,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "title": "Task 3: Schedule team introduction meetings",
                    "body": "Sub-task to schedule introductory meetings.",
                    "labels": [
                        "onboarding",
                        "meetings"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "issue_number": 15,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "branch": "feature/welcome-endpoint",
                    "message": "feat: Implement /hello endpoint",
                    "author": "intern-emma"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "title": "feat: Add welcome message endpoint",
                    "body": "PR for the first coding task, implementing the /hello endpoint.",
                    "head_branch": "feature/welcome-endpoint",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "pr_number": 10,
                    "issue_number": 14
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "issue_number": 14
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "new-hire-starter-project"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "new-hire-starter-project",
                    "commits_count": 1,
                    "open_issues": 3,
                    "open_prs": 0,
                    "open_alerts_by_severity": {
                        "critical": 0,
                        "high": 0,
                        "medium": 0,
                        "low": 0,
                        "unknown": 0
                    },
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_802",
        "instruction": "Your main strategic aim is to manage the **Secure Development Lifecycle (SDL) Policy** for the 'ui-kit' repository. This policy mandates that all development activities, particularly those that pose security concerns, adhere to a stringent, documentable remediation and approval process. A new feature has triggered a serious security alert, and you are entrusted with ensuring the repository\u2019s final state shows a compliant resolution, as outlined in the official **SDL Compliance Specification** below. Your final delivery is the repository activity dashboard, which will serve as the formal record of policy adherence. **SDL Compliance Specification for Data Export Feature:** * **Required State of Feature Development:** * A major feature issue titled 'Add new Data Export component' (body: 'Main tracking issue for the Data Export feature.', labels: ['feature'], assigned to 'ui-dev') must be 'closed'. * **Required State of Security Remediation:** * A 'critical' alert concerning 'Data Export component leaks PII' on file 'src/export.js' needs to be 'fixed'. * A security issue titled 'CRITICAL: Fix PII leak in Data Export PR' (body: 'Tracking issue for the PII leak discovered in the Data Export PR.', labels: ['security', 'bug'], assigned to 'security-group') must be 'closed'. * **Required State of Codebase:** * A pull request titled 'feat: Add new Data Export component' (body: 'PR for the new Data Export component with PII leak remediation.', reviewed by ['security-group']) must be 'merged' and connected to both the feature and security tracking issues. * The merged PR must encompass both the initial feature commit ('feat: Add initial data export component') and the following remediation commit ('fix: Sanitize user data in export component').",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Add new Data Export component",
                    "body": "Main tracking issue for the Data Export feature.",
                    "labels": [
                        "feature"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/data-export",
                    "message": "feat: Add initial data export component",
                    "author": "ui-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "feat: Add new Data Export component",
                    "body": "PR for the new Data Export component with PII leak remediation.",
                    "head_branch": "feature/data-export",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "ui-kit",
                    "severity": "critical",
                    "description": "Data Export component leaks PII",
                    "file": "src/export.js",
                    "branch": "feature/data-export"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "CRITICAL: Fix PII leak in Data Export PR",
                    "body": "Tracking issue for the PII leak discovered in the Data Export PR.",
                    "labels": [
                        "security",
                        "bug"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 13,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/data-export",
                    "message": "fix: Sanitize user data in export component",
                    "author": "security-group"
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "reviewers": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "ui-kit",
                    "alert_number": 10
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 13
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "ui-kit"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "ui-kit",
                    "commits_count": 2,
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts_by_severity": {
                        "critical": 0,
                        "high": 0,
                        "medium": 0,
                        "low": 0,
                        "unknown": 0
                    },
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_803",
        "instruction": "Your core strategic task is to apply the **Release Failure and Hotfix Protocol** for the newly implemented 'mission-critical-service'. This procedure must be followed when a production deployment causes a significant issue, necessitating an urgent rollback and subsequent hotfix. Your responsibility includes ensuring the repository's final status fully conforms to the official **Incident Response Compliance Specification**, outlined below. Your culminating task is providing a health summary of the repository to verify the service's stability on the updated hotfix version. **Incident Response Compliance Specification for mission-critical-service:** * **Required Repository State:** * Must be a 'private' repository with description: 'A new mission critical service for core business operations.' * **Required State of Releases & Deployments:** * A stable release 'v1.0.0' (desc: 'Stable release.') must be published, containing a commit with message 'feat: Initial implementation for v1.0.0', and its deployment to 'production-v1.0' registered. * A faulty release 'v1.1.0' (desc: 'Faulty release.') must be published, containing a commit with message 'feat: New feature with data corruption bug', and its deployment to 'production-v1.1' registered. * A rollback deployment to 'production-v1.0-rollback' must be registered to address the incident. * A concluding hotfix release 'v1.1.1' (desc: 'Hotfix release.') must be published and its ultimate deployment to 'production-v1.1.1' registered. * **Required State of Incident Tracking:** * A 'critical' alert for 'v1.1.0 deployment caused data corruption' in file 'src/db.js' must be 'fixed'. * An emergency issue titled 'EMERGENCY: Rollback v1.1.0' (body: 'Emergency issue to track the rollback of v1.1.0.', labels: ['incident']) must be 'closed'. * A hotfix issue titled 'Hotfix for v1.1.1' (body: 'Issue to track the development of the v1.1.1 hotfix.', labels: ['hotfix']) must be 'closed', monitoring a 'merged' PR titled 'fix: Hotfix for v1.1.1' (body: 'PR for the v1.1.1 hotfix.') from branch 'hotfix/v1.1.1' with the commit 'fix: Add data migration script and patch corruption bug'.",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "description": "A new mission critical service for core business operations.",
                    "private": true
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "branch": "main",
                    "message": "feat: Initial implementation for v1.0.0",
                    "author": "server-main"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "version": "v1.0.0",
                    "description": "Stable release."
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "environment": "production-v1.0"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "branch": "main",
                    "message": "feat: New feature with data corruption bug",
                    "author": "server-main"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "version": "v1.1.0",
                    "description": "Faulty release."
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "environment": "production-v1.1"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "severity": "critical",
                    "description": "v1.1.0 deployment caused data corruption",
                    "file": "src/db.js",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "title": "EMERGENCY: Rollback v1.1.0",
                    "body": "Emergency issue to track the rollback of v1.1.0.",
                    "labels": [
                        "incident"
                    ]
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "environment": "production-v1.0-rollback"
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "title": "Hotfix for v1.1.1",
                    "body": "Issue to track the development of the v1.1.1 hotfix.",
                    "labels": [
                        "hotfix"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "issue_number": 13,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "branch": "hotfix/v1.1.1",
                    "message": "fix: Add data migration script and patch corruption bug",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "title": "fix: Hotfix for v1.1.1",
                    "body": "PR for the v1.1.1 hotfix.",
                    "head_branch": "hotfix/v1.1.1",
                    "base_branch": "main"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "issue_number": 13
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "alert_number": 10
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "version": "v1.1.1",
                    "description": "Hotfix release."
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "mission-critical-service",
                    "environment": "production-v1.1.1"
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "mission-critical-service"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "mission-critical-service",
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_805",
        "instruction": "Your primary duty is to oversee the **External Contribution Management Policy** for the publicly accessible 'ui-kit' repository. This policy mandates that contributions from external sources are tracked using a corresponding internal issue, and that in-house developers incorporate any required modifications or tests before integration. You need to ensure the repository reaches a state that adheres to the **External Contribution Compliance Specification** outlined below. The deliverables include a series of reports\u2014the repository's activity dashboard and a team contribution stats report\u2014to confirm the contribution has been successfully incorporated and to assess the distribution of work between external and internal contributors. **External Contribution Compliance Specification:** * **Required State of Tracking Artifacts (all 'closed'):** * An external issue titled 'Feature request: Add CSV export button' (body: 'A public request for a new feature to export data grids as CSV.', labels: ['feature-request']). * An internal issue titled '[Tracker] Oversee contribution for CSV export' (body: 'Internal issue to track the external contribution for the CSV export feature.', labels: ['tracker', 'external-contribution'], assigned to 'ui-dev'). * **Required State of Codebase:** * A PR titled 'feat: Add CSV export functionality' (body: 'Adds a button to export data grid contents as a CSV file.', reviewed by ['tech-lead-tara']) must be 'merged' and linked to both issues. * The merged PR must include the following commits from the 'feature/csv-export' branch: 1. `feat: Add basic CSV export button` (Author: 'contractor-alex') 2. `style: Adjust export button to match design system` (Author: 'ui-dev') 3. `test: Add unit tests for CSV generation` (Author: 'qa-erin') * **Required State of Release:** A release 'v3.5.1' ('Adds CSV export functionality from external contributor.') must be published.",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Feature request: Add CSV export button",
                    "body": "A public request for a new feature to export data grids as CSV.",
                    "labels": [
                        "feature-request"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "[Tracker] Oversee contribution for CSV export",
                    "body": "Internal issue to track the external contribution for the CSV export feature.",
                    "labels": [
                        "tracker",
                        "external-contribution"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 13,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/csv-export",
                    "message": "feat: Add basic CSV export button",
                    "author": "contractor-alex"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "feat: Add CSV export functionality",
                    "body": "Adds a button to export data grid contents as a CSV file.",
                    "head_branch": "feature/csv-export",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/csv-export",
                    "message": "style: Adjust export button to match design system",
                    "author": "ui-dev"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/csv-export",
                    "message": "test: Add unit tests for CSV generation",
                    "author": "qa-erin"
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 13
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "ui-kit",
                    "version": "v3.5.1",
                    "description": "Adds CSV export functionality from external contributor."
                },
            },
            {
                "name": "GetTeamContributionStats",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "ui-kit"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "ui-kit",
                    "team_stats": {
                        "unknown": {
                            "commits": 0,
                            "prs": 1,
                            "issues": 0
                        },
                        "contractor-alex": {
                            "commits": 1,
                            "prs": 0,
                            "issues": 0
                        },
                        "ui-dev": {
                            "commits": 1,
                            "prs": 0,
                            "issues": 1
                        },
                        "qa-erin": {
                            "commits": 1,
                            "prs": 0,
                            "issues": 0
                        }
                    },
                    "report_date": "2025-08-26"
                },
                {
                    "repo": "ui-kit",
                    "commits_count": 3,
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts_by_severity": {
                        "critical": 0,
                        "high": 0,
                        "medium": 0,
                        "low": 0,
                        "unknown": 0
                    },
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_702",
        "instruction": "Your primary strategic objective is to handle the complete lifecycle of a feature as per the **Staged Deployment and Verification Policy** for the 'ui-kit' repository. This policy insists that new features be deployed and confirmed in a 'staging' environment before they gain approval for 'production'. You are accountable for ensuring the repository reaches a state that demonstrates the successful carrying out of this full procedure, as defined by the official **Staged Rollout Compliance Specification** below. Your ultimate deliverable is the repository's activity dashboard which will verify the feature is fully validated and set for production. **Staged Rollout Compliance Specification: Advanced Charting Feature** * **Required State of Feature Development:** * A primary issue titled 'Implement Advanced Charting Library' (body: 'Main tracking issue for the Advanced Charting feature.', labels: ['feature', 'epic'], assigned to 'ui-dev') must be 'closed'. * A PR titled 'feat: Advanced Charting Library' (body: 'PR to introduce the advanced charting library.', reviewed by ['tech-lead-tara']) must be 'merged', containing commits 'feat: Add charting components' and 'test: Add chart rendering tests' from the 'feature/adv-charts' branch. * **Required State of Staging Verification:** * A deployment to the 'staging' environment must be registered. * A verification issue titled 'Staging Verification for Advanced Charting' (body: 'Tracking issue for QA verification on the staging environment.', labels: ['qa', 'verification'], assigned to 'qa-erin') must be 'closed'. * **Required State of Production Readiness:** * A concluding issue titled 'Schedule Production Release for Advanced Charting v3.5.0' (body: 'All checks passed. Ready to schedule production deployment.', labels: ['release', 'ops'], assigned to 'release-manager') must be 'open'.",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Implement Advanced Charting Library",
                    "body": "Main tracking issue for the Advanced Charting feature.",
                    "labels": [
                        "feature",
                        "epic"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/adv-charts",
                    "message": "feat: Add charting components",
                    "author": "ui-dev"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feature/adv-charts",
                    "message": "test: Add chart rendering tests",
                    "author": "qa-erin"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "feat: Advanced Charting Library",
                    "body": "PR to introduce the advanced charting library.",
                    "head_branch": "feature/adv-charts",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "ui-kit",
                    "environment": "staging"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Staging Verification for Advanced Charting",
                    "body": "Tracking issue for QA verification on the staging environment.",
                    "labels": [
                        "qa",
                        "verification"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 13,
                    "assignees": [
                        "qa-erin"
                    ]
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 13
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Schedule Production Release for Advanced Charting v3.5.0",
                    "body": "All checks passed. Ready to schedule production deployment.",
                    "labels": [
                        "release",
                        "ops"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 14,
                    "assignees": [
                        "release-manager"
                    ]
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "ui-kit"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "ui-kit",
                    "commits_count": 2,
                    "open_issues": 1,
                    "open_prs": 0,
                    "open_alerts_by_severity": {
                        "critical": 0,
                        "high": 0,
                        "medium": 0,
                        "low": 0,
                        "unknown": 0
                    },
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_703",
        "instruction": "Your primary strategic objective is to coordinate the creation of the new 'inventory-management-api' repository, ensuring it completely adheres to the company's **Secure Project Bootstrap Policy**. This policy requires that all new projects resolve any known vulnerabilities from their base template before the first release. You are tasked with ensuring the repository's final state perfectly matches the official **Secure Bootstrap Compliance Specification**, as outlined below. Your final deliverable is the repository's health summary, which will act as the formal record of policy adherence. **Secure Bootstrap Compliance Specification:** * **Required Repository State:** * A 'private' repository must be established with description: 'API for managing warehouse inventory.' and contain an initial commit with the message 'Initial commit from template' by 'infra-lead'. * **Required State of Initial Security Posture:** * A 'medium' severity alert for 'Default template includes outdated dependency: GSON v2.8.5' in 'pom.xml' must be 'fixed'. * A main setup issue titled 'Initial Project Setup' (body: 'Main tracking issue for the complete and secure setup of the new repository.', labels: ['setup', 'epic'], assigned to 'server-main') must be 'closed'. * A sub-task issue titled 'fix: Update outdated GSON dependency' (body: 'Sub-task to update the vulnerable GSON dependency from the initial template.', labels: ['security', 'dependency'], assigned to 'server-main') must be 'closed'. * A PR titled 'fix(deps): Upgrade GSON to v2.8.9' (body: 'PR to upgrade outdated GSON dependency.', reviewed by ['tech-lead-tara']) must be 'merged', linked to the security sub-task, and contain a commit 'fix: Upgrade GSON to v2.8.9' (author: 'server-main') from the 'hotfix/gson-upgrade' branch. * **Required State of Release:** * A release 'v0.1.0' ('Initial secure release.') must be published.",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "description": "API for managing warehouse inventory.",
                    "private": true
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "branch": "main",
                    "message": "Initial commit from template",
                    "author": "infra-lead"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "severity": "medium",
                    "description": "Default template includes outdated dependency: GSON v2.8.5",
                    "file": "pom.xml",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "title": "Initial Project Setup",
                    "body": "Main tracking issue for the complete and secure setup of the new repository.",
                    "labels": [
                        "setup",
                        "epic"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "title": "fix: Update outdated GSON dependency",
                    "body": "Sub-task to update the vulnerable GSON dependency from the initial template.",
                    "labels": [
                        "security",
                        "dependency"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "issue_number": 13,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "branch": "hotfix/gson-upgrade",
                    "message": "fix: Upgrade GSON to v2.8.9",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "title": "fix(deps): Upgrade GSON to v2.8.9",
                    "body": "PR to upgrade outdated GSON dependency.",
                    "head_branch": "hotfix/gson-upgrade",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "issue_number": 13
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "alert_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "inventory-management-api",
                    "version": "v0.1.0",
                    "description": "Initial secure release."
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "inventory-management-api"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "inventory-management-api",
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_601",
        "instruction": "Your foremost strategic aim is to handle the establishment of a new hire's initial project, guaranteeing it thoroughly complies with the company's **New Hire Onboarding Policy**. This policy requires that a specific starter repository is set up with an organized series of onboarding tasks. You are accountable for verifying that the repository's final state fully aligns with the official **Onboarding Compliance Specification**, outlined below. Your concluding deliverable is the activity dashboard of the repository, which will serve as the official proof of policy adherence. **Onboarding Compliance Specification for 'new-hire-starter-project':** * **Required Repository State:** * Must be 'private' with description: 'Starter project for new engineering hires.' * **Required State of Onboarding Issues:** * A main epic titled 'Onboarding Plan for new hire' (body: 'Main epic to track the new hire onboarding process.', labels: ['onboarding', 'epic']) must be 'open' and assigned to 'intern-emma'. * A sub-task titled 'Task 1: Set up local development environment' (body: 'Sub-task to track local environment setup.', labels: ['onboarding', 'setup']) must be 'open' and assigned to 'intern-emma'. * A sub-task titled 'Task 2: Complete first coding task' (body: 'Sub-task for the first coding assignment.', labels: ['onboarding', 'coding-task']) must be 'closed'. * A sub-task titled 'Task 3: Schedule team introduction meetings' (body: 'Sub-task to schedule introductory meetings.', labels: ['onboarding', 'meetings']) must be 'open' and assigned to 'intern-emma'. * **Required State of First Coding Task:** * A pull request titled 'feat: Add welcome message endpoint' (body: 'PR for the first coding task.', reviewed by ['tech-lead-tara']) must be 'merged' into 'main', linked to the coding task issue, and contain a commit 'feat: Implement /hello endpoint' by 'intern-emma' from the 'feature/welcome-endpoint' branch.",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "description": "Starter project for new engineering hires.",
                    "private": true
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "title": "Onboarding Plan for new hire",
                    "body": "Main epic to track the new hire onboarding process.",
                    "labels": [
                        "onboarding",
                        "epic"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "issue_number": 12,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "title": "Task 1: Set up local development environment",
                    "body": "Sub-task to track local environment setup.",
                    "labels": [
                        "onboarding",
                        "setup"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "issue_number": 13,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "title": "Task 2: Complete first coding task",
                    "body": "Sub-task for the first coding assignment.",
                    "labels": [
                        "onboarding",
                        "coding-task"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "issue_number": 14,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "title": "Task 3: Schedule team introduction meetings",
                    "body": "Sub-task to schedule introductory meetings.",
                    "labels": [
                        "onboarding",
                        "meetings"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "issue_number": 15,
                    "assignees": [
                        "intern-emma"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "branch": "feature/welcome-endpoint",
                    "message": "feat: Implement /hello endpoint",
                    "author": "intern-emma"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "title": "feat: Add welcome message endpoint",
                    "body": "PR for the first coding task.",
                    "head_branch": "feature/welcome-endpoint",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "pr_number": 10,
                    "issue_number": 14
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "new-hire-starter-project",
                    "issue_number": 14
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "new-hire-starter-project"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "new-hire-starter-project",
                    "commits_count": 1,
                    "open_issues": 3,
                    "open_prs": 0,
                    "open_alerts_by_severity": {
                        "critical": 0,
                        "high": 0,
                        "medium": 0,
                        "low": 0,
                        "unknown": 0
                    },
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_503",
        "instruction": "Your principal strategic task is to coordinate the full compliance of the 'security-scanner' repository with the company's **Audit and Proactive Hardening Policy**. This policy stipulates that each audit finding is duly recorded and that a preventive measure is enacted to address the root cause. You are tasked with guaranteeing that the repository's condition perfectly conforms to the official **Audit Compliance Specification**, specified below. Your final output is the activity dashboard of the repository, which will serve as the official documentation of policy compliance. **Audit Compliance Specification for security-scanner:** * **Required State of Audit Findings (Issues):** * An issue titled 'Finding: Inconsistent Logging Levels' (body: 'Audit finding identifying multiple inconsistent logging levels across modules.', labels: ['bug', 'logging'], assigned to 'security-group') must be 'open'. * An issue titled 'Finding: High Memory Usage in Scanner' (body: 'Audit finding identifying high memory usage during large file scans.', labels: ['performance'], assigned to 'perf-nathan') must be 'open'. * A main issue titled 'Q3 Security Audit Findings' (body: 'Main tracking issue for all Q3 audit findings and the preventative action PR.', labels: ['audit'], assigned to 'tech-lead-tara') must be 'closed'. * **Required State of Preventative Control:** * A pull request titled 'build: Add static analysis pre-commit hook' (body: 'This PR adds a pre-commit hook for static analysis to prevent future issues.', reviewed by ['tech-lead-tara']) must be 'merged' into 'main', linked to the main audit issue, and contain a commit 'build: Add static analysis pre-commit hook' by 'infra-lead' from the 'feature/static-analysis-hook' branch.",
        "actions": [
            {
                "name": "GetIssueAgingReport",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "GetPullRequestMergeTimeReport",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "GetOpenSecurityAlerts",
                "arguments": {
                    "repo_name": "security-scanner"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Finding: Inconsistent Logging Levels",
                    "body": "Audit finding identifying multiple inconsistent logging levels across modules.",
                    "labels": [
                        "bug",
                        "logging"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Finding: High Memory Usage in Scanner",
                    "body": "Audit finding identifying high memory usage during large file scans.",
                    "labels": [
                        "performance"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "perf-nathan"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Q3 Security Audit Findings",
                    "body": "Main tracking issue for all Q3 audit findings and the preventative action PR.",
                    "labels": [
                        "audit"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 14,
                    "assignees": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "feature/static-analysis-hook",
                    "message": "build: Add static analysis pre-commit hook",
                    "author": "infra-lead"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "build: Add static analysis pre-commit hook",
                    "body": "This PR adds a pre-commit hook for static analysis to prevent future issues.",
                    "head_branch": "feature/static-analysis-hook",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 14
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 14
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "security-scanner",
                    "commits_count": 1,
                    "open_issues": 2,
                    "open_prs": 0,
                    "open_alerts_by_severity": {
                        "critical": 0,
                        "high": 0,
                        "medium": 0,
                        "low": 0,
                        "unknown": 0
                    },
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_402",
        "instruction": "Take charge of managing the security lifecycle for the 'security-scanner' repository, ensuring it is in complete adherence to the company's **Comprehensive Security Hardening Policy**. This policy requires a distinct and reviewable trail for the handling of tiered vulnerabilities. You are accountable for ensuring the repository's condition mirrors the effective execution of this policy, as outlined in the official **Hardening Compliance Specification** below. Your concluding deliverable is a health summary of the repository to formally record policy compliance. **Hardening Compliance Specification for security-scanner:** * **Necessary State for Critical Risks ('Unsafe deserialization' in 'src/parser.rs'):** * A tracking issue named 'Fix Critical: Unsafe Deserialization' (body: 'Full remediation tracking for the critical unsafe deserialization alert.', labels: ['security']) must be 'closed' and assigned to 'security-group'. * The associated alert must be 'fixed'. * A PR titled 'Fix: Unsafe Deserialization' (body: 'PR containing the complete fix for the unsafe deserialization vulnerability.') must be 'merged', containing a commit with the message 'fix: Patch unsafe deserialization vulnerability' from the 'fix/critical-deserialization' branch. * **Necessary State for High Risks ('Potential buffer overflow' in 'src/handlers.rs'):** * A tracking issue named 'Remediate High: Buffer Overflow' (body: 'Remediation tracking for the high-severity buffer overflow alert.', labels: ['security']) must be 'open' and assigned to 'security-group'. * A PR titled 'WIP: Remediate Buffer Overflow' (body: 'WIP PR to introduce memory-safe string handling.') must be 'open', containing a commit with the message 'refactor: Introduce memory-safe string handling' from the 'fix/high-buffer-overflow' branch. * **Necessary State for Medium Risks ('Use of deprecated crypto functions' in 'src/crypto.rs'):** * A tracking issue named 'Track Medium: Deprecated Crypto Usage' (body: 'Tracking issue for future refactoring of deprecated crypto functions.', labels: ['security'], assigned to 'security-group') must be 'open'. * **General Requirements:** * All PRs must be reviewed by 'tech-lead-tara'.",
        "actions": [
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "severity": "critical",
                    "description": "Unsafe deserialization",
                    "file": "src/parser.rs",
                    "branch": "main"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "severity": "high",
                    "description": "Potential buffer overflow",
                    "file": "src/handlers.rs",
                    "branch": "main"
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "severity": "medium",
                    "description": "Use of deprecated crypto functions",
                    "file": "src/crypto.rs",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Fix Critical: Unsafe Deserialization",
                    "body": "Full remediation tracking for the critical unsafe deserialization alert.",
                    "labels": [
                        "security"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "fix/critical-deserialization",
                    "message": "fix: Patch unsafe deserialization vulnerability",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Fix: Unsafe Deserialization",
                    "body": "PR containing the complete fix for the unsafe deserialization vulnerability.",
                    "head_branch": "fix/critical-deserialization",
                    "base_branch": "main"
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12
                },
            },
            {
                "name": "FixSecurityAlert",
                "arguments": {
                    "repo_name": "security-scanner",
                    "alert_number": 10
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Remediate High: Buffer Overflow",
                    "body": "Remediation tracking for the high-severity buffer overflow alert.",
                    "labels": [
                        "security"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "fix/high-buffer-overflow",
                    "message": "refactor: Introduce memory-safe string handling",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "WIP: Remediate Buffer Overflow",
                    "body": "WIP PR to introduce memory-safe string handling.",
                    "head_branch": "fix/high-buffer-overflow",
                    "base_branch": "main"
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 11,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Track Medium: Deprecated Crypto Usage",
                    "body": "Tracking issue for future refactoring of deprecated crypto functions.",
                    "labels": [
                        "security"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 14,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "security-scanner",
                    "open_issues": 2,
                    "open_prs": 1,
                    "open_alerts": 2,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_301",
        "instruction": "Your mission is to implement the company's **Tiered Vulnerability Response Protocol** on the 'security-scanner' repository. This protocol calls for a dual-focus: complete remediation for critical-risk items and preliminary containment for high-risk items. You need to carry out this protocol to address the vulnerabilities described in the specification below. Your ultimate deliverable is the repository's activity dashboard to confirm that the protocol was accurately executed and the repository state reflects the finished critical remediation and the ongoing high-risk containment. **Compliance Specification:** * **Critical Vulnerability (Unsafe Deserialization):** This must be fully remediated. The final state must show a 'closed' tracking issue and a 'merged' pull request with the hotfix. This work is owned by the 'security-group'. * **High Vulnerability (Buffer Overflow):** This requires initial containment. The final state must show an 'open' tracking issue and an 'open' work-in-progress pull request with initial mitigation steps. This work is owned by 'perf-nathan'. * **General Requirements:** All pull requests related to this protocol must be reviewed by 'tech-lead-tara'.",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Remediate Critical: Unsafe Deserialization",
                    "body": "Tracking issue for the unsafe deserialization vulnerability.",
                    "labels": [
                        "security",
                        "critical-risk"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Remediate High: Buffer Overflow",
                    "body": "Tracking issue for the potential buffer overflow vulnerability.",
                    "labels": [
                        "security",
                        "high-risk"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 13,
                    "assignees": [
                        "perf-nathan"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "hotfix/critical-deserialization",
                    "message": "fix: Initial patch for unsafe deserialization",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "Fix: Unsafe Deserialization",
                    "body": "Complete fix for the critical deserialization vulnerability.",
                    "head_branch": "hotfix/critical-deserialization",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "issue_number": 12
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "security-scanner",
                    "branch": "fix/buffer-overflow-config",
                    "message": "feat: Add memory safe string handling config",
                    "author": "perf-nathan"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "security-scanner",
                    "title": "WIP: Config for Buffer Overflow",
                    "body": "Configuration update to mitigate buffer overflow risks.",
                    "head_branch": "fix/buffer-overflow-config",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 11,
                    "issue_number": 13
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "security-scanner",
                    "pr_number": 11,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "security-scanner"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "security-scanner",
                        "commits_count": 2,
                        "open_issues": 1,
                        "open_prs": 1,
                        "open_alerts_by_severity": {
                            "critical": 0,
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                            "unknown": 0
                        },
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_302",
        "instruction": "Your main responsibility is to verify that the new 'api-gateway' project fully adheres to the company's **New Service Incubation Policy**. This policy mandates that each new service accomplishes two foundational feature cycles before initiating their first alpha release. Utilize the provided compliance specification and data manifest to transition the repository from its initial creation to a fully compliant v0.1.0-alpha state. Your ultimate deliverable is the repository's health summary, which shows that the repository's status matches the policy requirements. **Compliance Specification for v0.1.0-alpha:** The final objective is that the repository is established and two core features ('Authentication' and 'Rate Limiting') are completely executed. Complete implementation signifies that each feature is monitored through an issue which is now 'closed', with the related code integrated through a pull request. Lastly, an official alpha release must be published. **Data Manifest:** * **Repository Config:** {name: 'api-gateway', description: 'Central API Gateway for microservices.', private: True} * **Feature 1 (Authentication):** {issue_title: 'Implement Authentication Route', issue_body: 'Implementation of the primary authentication endpoint.', labels: ['feature', 'auth'], assignee: 'server-main', branch: 'feature/auth-route', commit_author: 'server-main', commit_message: 'feat: Add JWT authentication middleware and /auth route', pr_title: 'Feature: Authentication Route', pr_body: 'PR for the authentication route.'} * **Feature 2 (Rate Limiting):** {issue_title: 'Implement Rate Limiting', issue_body: 'Implementation of IP-based rate limiting.', labels: ['feature', 'performance'], assignee: 'infra-lead', branch: 'feature/rate-limit', commit_author: 'infra-lead', commit_message: 'feat: Add IP-based rate limiting', pr_title: 'Feature: Rate Limiting', pr_body: 'PR for rate limiting.'} * **Release Artifact:** {version: 'v0.1.0-alpha', description: 'First alpha release with auth and rate limiting.'}",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "api-gateway",
                    "description": "Central API Gateway for microservices.",
                    "private": true
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "api-gateway",
                    "title": "Implement Authentication Route",
                    "body": "Implementation of the primary authentication endpoint.",
                    "labels": [
                        "feature",
                        "auth"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "api-gateway",
                    "issue_number": 12,
                    "assignees": [
                        "server-main"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "api-gateway",
                    "branch": "feature/auth-route",
                    "message": "feat: Add JWT authentication middleware and /auth route",
                    "author": "server-main"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "api-gateway",
                    "title": "Feature: Authentication Route",
                    "body": "PR for the authentication route.",
                    "head_branch": "feature/auth-route",
                    "base_branch": "main"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "api-gateway",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "api-gateway",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "api-gateway",
                    "title": "Implement Rate Limiting",
                    "body": "Implementation of IP-based rate limiting.",
                    "labels": [
                        "feature",
                        "performance"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "api-gateway",
                    "issue_number": 13,
                    "assignees": [
                        "infra-lead"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "api-gateway",
                    "branch": "feature/rate-limit",
                    "message": "feat: Add IP-based rate limiting",
                    "author": "infra-lead"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "api-gateway",
                    "title": "Feature: Rate Limiting",
                    "body": "PR for rate limiting.",
                    "head_branch": "feature/rate-limit",
                    "base_branch": "main"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "api-gateway",
                    "pr_number": 11
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "api-gateway",
                    "issue_number": 13
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "api-gateway",
                    "version": "v0.1.0-alpha",
                    "description": "First alpha release with auth and rate limiting."
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "api-gateway"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "api-gateway",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 0,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_303",
        "instruction": "Your task is to handle the **Major Version Release Preparation Policy** for the imminent 'v4.0.0' release of the 'ui-kit' repository. The policy stipulates that every planned feature and deprecation must be formally monitored, executed, and merged into the main branch via a unified release pull request. You should use the **Release Work Manifest** provided to develop all essential artifacts for this preparation stage. Your ultimate deliverable is the activity dashboard of the repository, confirming that all modifications have been successfully merged and the repository is primed for the v4.0.0 tag. **Release Work Manifest for v4.0.0:** * **Feature A (Dark Mode):** * Title: 'Implement Dark Mode v2', Body: 'Tracking issue for Dark Mode v2 implementation.', Labels: ['feature', 'ui'], Assignee: 'ui-dev' * **Feature B (Accessibility):** * Title: 'Add Accessibility Tree Shaking', Body: 'Tracking issue for accessibility tree shaking.', Labels: ['feature', 'a11y'], Assignee: 'ui-developer' * **Deprecation C (Grid):** * Title: 'Deprecate Legacy Grid Component', Body: 'Tracking issue for legacy grid deprecation.', Labels: ['deprecation', 'tech-debt'], Assignee: 'ui-dev' * **Implementation:** * Branch: 'release/v4.0.0', Author: 'ui-dev', Commits: ['feat: Dark Mode v2', 'feat: Accessibility Tree Shaking', 'refactor: Deprecate Legacy Grid'] * **Consolidated PR:** * Title: 'Release: Version 4.0.0', Body: 'Consolidated PR for v4.0.0, including all new features and deprecations.', Reviewers: ['design-lead', 'tech-lead-tara']",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Implement Dark Mode v2",
                    "body": "Tracking issue for Dark Mode v2 implementation.",
                    "labels": [
                        "feature",
                        "ui"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Add Accessibility Tree Shaking",
                    "body": "Tracking issue for accessibility tree shaking.",
                    "labels": [
                        "feature",
                        "a11y"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 13,
                    "assignees": [
                        "ui-developer"
                    ]
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Deprecate Legacy Grid Component",
                    "body": "Tracking issue for legacy grid deprecation.",
                    "labels": [
                        "deprecation",
                        "tech-debt"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 14,
                    "assignees": [
                        "ui-dev"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "release/v4.0.0",
                    "message": "feat: Dark Mode v2",
                    "author": "ui-dev"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "release/v4.0.0",
                    "message": "feat: Accessibility Tree Shaking",
                    "author": "ui-dev"
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "release/v4.0.0",
                    "message": "refactor: Deprecate Legacy Grid",
                    "author": "ui-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Release: Version 4.0.0",
                    "body": "Consolidated PR for v4.0.0, including all new features and deprecations.",
                    "head_branch": "release/v4.0.0",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 13
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "issue_number": 14
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10,
                    "reviewers": [
                        "design-lead",
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 13
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 14
                },
            },
            {
                "name": "GetRepositoryActivityDashboard",
                "arguments": {
                    "repo_name": "ui-kit"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "ui-kit",
                    "commits_count": 3,
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts_by_severity": {
                        "critical": 0,
                        "high": 0,
                        "medium": 0,
                        "low": 0,
                        "unknown": 0
                    },
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_305",
        "instruction": "Your key responsibility is to verify that the new 'data-pipeline-orchestrator' project adheres entirely to the company's **New Project Go-Live Policy**. This policy dictates that new services be initiated with all essential artifacts, such as initial features and security scans, prior to their inaugural release. Your duty is to progress the repository from its newly created state to one that complies with the official **Compliance Specification for v0.1.0**. The final outcome expected from you is a health summary of the repository, confirming that its condition aligns with the policy. **Compliance Specification for v0.1.0:** The repository's final state must demonstrate a successfully implemented initial feature, documented through a 'closed' issue and a 'merged' pull request. The repository should also include an initial 'medium' severity security alert logged. Additionally, a formal release must be published and deployed to 'staging'. **Data Manifest:** * **Repository Config:** {name: 'data-pipeline-orchestrator', description: 'Service for orchestrating ETL data pipelines.', private: True} * **Initial Feature:** {issue_title: 'Setup initial DAG structure', issue_body: 'Tracks the implementation of the initial DAG structure for the orchestrator.', labels: ['feature', 'architecture'], assignee: 'ml-engineer', branch: 'feature/initial-dag', commit_author: 'ml-engineer', commit_message: 'feat: Add initial DAG scaffolding', pr_title: 'Feature: Initial DAG Structure', pr_body: 'PR for the initial DAG structure.', reviewers: ['ml-engineer']} * **Security Alert:** {severity: 'medium', description: 'Hardcoded credentials in connector module.', file: 'src/connectors/db.py'} * **Release Artifacts:** {version: '0.1.0', description: 'Initial release with basic DAG orchestration.', environment: 'staging'}",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "description": "Service for orchestrating ETL data pipelines.",
                    "private": true
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "title": "Setup initial DAG structure",
                    "body": "Tracks the implementation of the initial DAG structure for the orchestrator.",
                    "labels": [
                        "feature",
                        "architecture"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "issue_number": 12,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "branch": "feature/initial-dag",
                    "message": "feat: Add initial DAG scaffolding",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "title": "Feature: Initial DAG Structure",
                    "body": "PR for the initial DAG structure.",
                    "head_branch": "feature/initial-dag",
                    "base_branch": "main"
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "pr_number": 10,
                    "reviewers": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "severity": "medium",
                    "description": "Hardcoded credentials in connector module.",
                    "file": "src/connectors/db.py",
                    "branch": "main"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "version": "0.1.0",
                    "description": "Initial release with basic DAG orchestration."
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "environment": "staging"
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator"
                }
            }
        ],
        "outputs": [
                {
                    "status": "ok",
                    "data": {
                        "repo": "data-pipeline-orchestrator",
                        "open_issues": 0,
                        "open_prs": 0,
                        "open_alerts": 1,
                        "report_date": "2025-08-26"
                    }
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_201",
        "instruction": "Your task is to oversee the complete lifecycle of a feature implementation along with its emergency rollback for the 'acme-webapp' repository, in compliance with company policy. Start by supervising the merge of a new feature using the 'Feature Manifest'. An urgent vulnerability concerning this feature is identified immediately afterwards. You are required to implement the 'Emergency Reversal Policy' by employing the 'Reversal Manifest', formally documenting the issue and devising a fix. The endpoint of your responsibilities is a health summary of the repository, indicating the prevailing emergency condition. **Feature Manifest (v1.1.0):** * Tracking Issue: Title='Implement User Profile Caching', Body='Tracks caching implementation.', Labels=['feature'], Assignee='maya-w' * Implementation: Branch='feature/profile-caching', Commit Author='dev-sue', Commit Message='feat: Add user profile caching logic' * Pull Request: Title='Feature: User Profile Caching', Body='PR for user profile caching.', Reviewers=['qa-mike'] **Reversal Manifest:** * Security Alert: Severity='critical', Description='Post-merge discovery: Caching logic exposes sensitive user data.', File='src/app.py' * Reversal Issue: Title='EMERGENCY: Reversal of profile caching feature', Body='Reversal required due to critical vulnerability.', Labels=['security', 'bug'], Assignee='security-group' * Reversal PR: Title='Revert: User Profile Caching', Body='Reverting the caching feature due to a critical vulnerability.', Branch='revert/profile-caching', Commit Author='security-group', Commit Message='revert: Revert user profile caching feature'",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Implement User Profile Caching",
                    "body": "Tracks caching implementation.",
                    "labels": [
                        "feature"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12,
                    "assignees": [
                        "maya-w"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "feature/profile-caching",
                    "message": "feat: Add user profile caching logic",
                    "author": "dev-sue"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Feature: User Profile Caching",
                    "body": "PR for user profile caching.",
                    "head_branch": "feature/profile-caching",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10,
                    "reviewers": [
                        "qa-mike"
                    ]
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "severity": "critical",
                    "description": "Post-merge discovery: Caching logic exposes sensitive user data.",
                    "file": "src/app.py",
                    "branch": "main"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "EMERGENCY: Reversal of profile caching feature",
                    "body": "Reversal required due to critical vulnerability.",
                    "labels": [
                        "security",
                        "bug"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 13,
                    "assignees": [
                        "security-group"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "branch": "revert/profile-caching",
                    "message": "revert: Revert user profile caching feature",
                    "author": "security-group"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Revert: User Profile Caching",
                    "body": "Reverting the caching feature due to a critical vulnerability.",
                    "head_branch": "revert/profile-caching",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "pr_number": 11,
                    "issue_number": 13
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "acme-webapp"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "acme-webapp",
                    "open_issues": 1,
                    "open_prs": 1,
                    "open_alerts": 1,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_202",
        "instruction": "Handle a major update in the 'ui-kit' core library and ensure the necessary changes are reflected in the downstream 'react-dashboard' application, following the regular cross-repository upgrade protocol. Utilize the given manifests for updating the library and adapting the application. Ultimately, compile a list of health summaries for both repositories to verify the operation's completion. **Manifest for ui-kit (v3.0.0):** * **Tracking Issue:** * Title: '[v3.0] Breaking Change: Deprecate legacy Button API' * Body: 'Tracks the deprecation of the legacy Button API for the v3.0.0 release.' * Labels: ['breaking-change', 'v3.0'] * **Implementation:** * Branch: 'feat/v3-button-api' * Commit Author: 'ui-dev' * Commit Message: 'refactor: Replace legacy Button API with new spec' * **Pull Request:** * Title: 'Refactor: New Button API for v3.0.0' * Body: 'This PR introduces the new Button API and removes the deprecated legacy component.' * **Release:** * Version: '3.0.0' * Description: 'Version 3.0.0 with new Button API.' **Manifest for react-dashboard:** * **Tracking Issue:** * Title: 'Upgrade to ui-kit v3.0.0' * Body: 'Adapt application to the new Button API introduced in ui-kit v3.0.0.' * Labels: ['dependency-upgrade', 'tech-debt'] * Assignee: 'ui-developer' * **Implementation:** * Branch: 'feat/upgrade-uikit-v3' * Commit Author: 'ui-developer' * Commit Message: 'feat: Update app to use new ui-kit Button API' * **Pull Request:** * Title: 'Upgrade: Adapt to ui-kit v3.0.0' * Body: 'This PR adapts the app to the breaking changes in ui-kit v3.0.0.' * Reviewers: ['tech-lead-tara']",
        "actions": [
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "[v3.0] Breaking Change: Deprecate legacy Button API",
                    "body": "Tracks the deprecation of the legacy Button API for the v3.0.0 release.",
                    "labels": [
                        "breaking-change",
                        "v3.0"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "ui-kit",
                    "branch": "feat/v3-button-api",
                    "message": "refactor: Replace legacy Button API with new spec",
                    "author": "ui-dev"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "title": "Refactor: New Button API for v3.0.0",
                    "body": "This PR introduces the new Button API and removes the deprecated legacy component.",
                    "head_branch": "feat/v3-button-api",
                    "base_branch": "main"
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "ui-kit",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "ui-kit",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "ui-kit",
                    "version": "3.0.0",
                    "description": "Version 3.0.0 with new Button API."
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "title": "Upgrade to ui-kit v3.0.0",
                    "body": "Adapt application to the new Button API introduced in ui-kit v3.0.0.",
                    "labels": [
                        "dependency-upgrade",
                        "tech-debt"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "issue_number": 13,
                    "assignees": [
                        "ui-developer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "branch": "feat/upgrade-uikit-v3",
                    "message": "feat: Update app to use new ui-kit Button API",
                    "author": "ui-developer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "title": "Upgrade: Adapt to ui-kit v3.0.0",
                    "body": "This PR adapts the app to the breaking changes in ui-kit v3.0.0.",
                    "head_branch": "feat/upgrade-uikit-v3",
                    "base_branch": "main"
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 11,
                    "issue_number": 13
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "react-dashboard",
                    "pr_number": 11,
                    "reviewers": [
                        "tech-lead-tara"
                    ]
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "ui-kit"
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "react-dashboard"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "ui-kit",
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                },
                {
                    "repo": "react-dashboard",
                    "open_issues": 1,
                    "open_prs": 1,
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_205",
        "instruction": "Coordinate the application of the company's 'New Project Go-Live Policy' for the 'data-pipeline-orchestrator' service. This involves a comprehensive end-to-end setup, spanning from the creation of the repository to its inaugural release. According to company policy, the initial issue in a project is assigned ID 12, and the first PR is given ID 10; following entries are numbered consecutively. Utilize the specified Go-Live Manifest to generate all materials in line with this policy. Your output is the post-release repository health summary. **Go-Live Manifest for data-pipeline-orchestrator:** * **Repository:** * Description: 'Service for orchestrating ETL data pipelines.' * Privacy: 'private' * **Initial Feature Issue:** * Title: 'Setup initial DAG structure' * Body: 'Tracks the implementation of the initial DAG structure for the orchestrator.' * Labels: ['feature', 'architecture'] * Assignee: 'ml-engineer' * **Feature Implementation:** * Branch: 'feature/initial-dag' * Commit Author: 'ml-engineer' * Commit Message: 'feat: Add initial DAG scaffolding' * **Pull Request:** * Title: 'Feature: Initial DAG Structure' * Body: 'PR for the initial DAG structure.' * Base Branch: 'main' * Reviewers: ['ml-engineer'] * **Day-One Security Alert:** * Severity: 'medium' * Description: 'Hardcoded credentials in connector module.' * File: 'src/connectors/db.py' * **First Release:** * Version: '0.1.0' * Description: 'Initial release with basic DAG orchestration.' * **Deployment:** * Environment: 'staging'",
        "actions": [
            {
                "name": "CreateRepository",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "description": "Service for orchestrating ETL data pipelines.",
                    "private": true
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "title": "Setup initial DAG structure",
                    "body": "Tracks the implementation of the initial DAG structure for the orchestrator.",
                    "labels": [
                        "feature",
                        "architecture"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "issue_number": 12,
                    "assignees": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "AddCommitToBranch",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "branch": "feature/initial-dag",
                    "message": "feat: Add initial DAG scaffolding",
                    "author": "ml-engineer"
                },
            },
            {
                "name": "OpenPullRequest",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "title": "Feature: Initial DAG Structure",
                    "body": "PR for the initial DAG structure.",
                    "head_branch": "feature/initial-dag",
                    "base_branch": "main"
                },
            },
            {
                "name": "RequestPullRequestReview",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "pr_number": 10,
                    "reviewers": [
                        "ml-engineer"
                    ]
                },
            },
            {
                "name": "LinkPullRequestToIssue",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "pr_number": 10,
                    "issue_number": 12
                },
            },
            {
                "name": "MergePullRequest",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "pr_number": 10
                },
            },
            {
                "name": "CloseIssue",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "issue_number": 12
                },
            },
            {
                "name": "CreateSecurityAlert",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "severity": "medium",
                    "description": "Hardcoded credentials in connector module.",
                    "file": "src/connectors/db.py",
                    "branch": "main"
                },
            },
            {
                "name": "CreateRelease",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "version": "0.1.0",
                    "description": "Initial release with basic DAG orchestration."
                },
            },
            {
                "name": "RegisterDeployEvent",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator",
                    "environment": "staging"
                },
            },
            {
                "name": "GetRepositoryHealthSummary",
                "arguments": {
                    "repo_name": "data-pipeline-orchestrator"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "data-pipeline-orchestrator",
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts": 1,
                    "report_date": "2025-08-26"
                }
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "user_104",
        "instruction": "In your capacity for preserving repository health, manage a thorough audit of the 'acme-webapp' repository. According to standard policy, all such audits must conclude with a formal tracking issue that summarizes the findings and assigns responsibility for any needed improvements. Thus, your obligation involves examining the repository's backlogs, open changes, and security position, followed by the creation of a single, critical 'Post-Audit Action Plan' issue. This issue must include the body 'This issue tracks the necessary follow-up actions from the comprehensive repository health audit.', be labeled ['audit', 'priority-high'], and assigned to 'maya-w'. Your conclusive task is to provide the cross-entity report reflecting the repository's state once this audit-tracking issue is established.",
        "actions": [
            {
                "name": "GetIssueAgingReport",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "ListPullRequests",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "state": "open"
                },
            },
            {
                "name": "GetRepositoryRiskScore",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "GetOpenSecurityAlerts",
                "arguments": {
                    "repo_name": "acme-webapp"
                },
            },
            {
                "name": "CreateIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "title": "Post-Audit Action Plan",
                    "body": "This issue tracks the necessary follow-up actions from the comprehensive repository health audit.",
                    "labels": [
                        "audit",
                        "priority-high"
                    ]
                },
            },
            {
                "name": "AssignIssue",
                "arguments": {
                    "repo_name": "acme-webapp",
                    "issue_number": 12,
                    "assignees": [
                        "maya-w"
                    ]
                },
            },
            {
                "name": "GetCrossEntityReport",
                "arguments": {
                    "repo_name": "acme-webapp"
                }
            }
        ],
        "outputs": [
                {
                    "repo": "acme-webapp",
                    "open_issues": 1,
                    "merged_prs": 0,
                    "recent_commits": 0,
                    "open_alerts": 0,
                    "last_deployment": "none",
                    "report_date": "2025-08-26"
                }
        ]
    }
]
