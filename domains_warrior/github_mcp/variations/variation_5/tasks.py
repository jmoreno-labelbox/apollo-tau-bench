from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="1",
        user_id="user_505",
        instruction=(
            "Your strategic objective is to execute the **New Service Onboarding and Governance Policy** for a project named 'notification-service'. "
            "This policy mandates that new services are not only technically bootstrapped but also meet initial governance and security compliance "
            "standards before their first release. You are responsible for bringing the repository to a state that fully conforms to the policy "
            "by using the provided **Onboarding Manifest**. Your final deliverable is the repository's health summary to confirm its compliant state.\n\n"
            "**Onboarding Manifest:**\n"
            "* **Repository:** {name: 'notification-service', description: 'Centralized service for handling user notifications.', private: True}\n"
            "* **Governance:**\n"
            "    * **Commits:** [{message: 'docs: Add MIT License', author: 'docs-amy'}, {message: 'docs: Add SECURITY.md policy', author: 'docs-amy'}]\n"
            "    * **Ops Issue:** {title: 'ops: Configure main branch protection rules', body: 'Tracking issue for branch protection setup as per governance policy.', labels: ['ops', 'governance'], assignee: 'devops-lead'}\n"
            "* **Security Remediation:**\n"
            "    * **Alert:** {severity: 'medium', description: 'Default template includes outdated dependency: common-lib v1.2.3', file: 'package.json', branch: 'main'}\n"
            "    * **Issue:** {title: 'fix: Update outdated dependency common-lib', body: 'Tracking issue to update the vulnerable common-lib dependency.', labels: ['security', 'dependency'], assignee: 'devops-lead'}\n"
            "    * **Code:** {branch: 'fix/update-common-lib', commit_message: 'fix: Upgrade common-lib to v1.2.4', author: 'devops-lead'}\n"
            "    * **PR:** {title: 'fix(deps): Upgrade common-lib to v1.2.4', body: 'PR to upgrade outdated common-lib dependency to v1.2.4.'}\n"
            "* **Release:** {version: 'v0.1.0', description: 'Initial compliant release.'}"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "notification-service", "description": "Centralized service for handling user notifications.", "private": True}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "notification-service", "branch": "main", "message": "docs: Add MIT License", "author": "docs-amy"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "notification-service", "branch": "main", "message": "docs: Add SECURITY.md policy", "author": "docs-amy"}),
            Action(name="create_issue", kwargs={"repo_name": "notification-service", "title": "ops: Configure main branch protection rules", "body": "Tracking issue for branch protection setup as per governance policy.", "labels": ["ops", "governance"]}),
            Action(name="assign_issue", kwargs={"repo_name": "notification-service", "issue_number": 12, "assignees": ["devops-lead"]}),
            Action(name="close_issue", kwargs={"repo_name": "notification-service", "issue_number": 12}),
            Action(name="create_security_alert", kwargs={"repo_name": "notification-service", "severity": "medium", "description": "Default template includes outdated dependency: common-lib v1.2.3", "file": "package.json", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "notification-service", "title": "fix: Update outdated dependency common-lib", "body": "Tracking issue to update the vulnerable common-lib dependency.", "labels": ["security", "dependency"]}),
            Action(name="assign_issue", kwargs={"repo_name": "notification-service", "issue_number": 13, "assignees": ["devops-lead"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "notification-service", "branch": "fix/update-common-lib", "message": "fix: Upgrade common-lib to v1.2.4", "author": "devops-lead"}),
            Action(name="open_pull_request", kwargs={"repo_name": "notification-service", "title": "fix(deps): Upgrade common-lib to v1.2.4", "body": "PR to upgrade outdated common-lib dependency to v1.2.4.", "head_branch": "fix/update-common-lib", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "notification-service", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "notification-service", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "notification-service", "issue_number": 13}),
            Action(name="fix_security_alert", kwargs={"repo_name": "notification-service", "alert_number": 10}),
            Action(name="create_release", kwargs={"repo_name": "notification-service", "version": "v0.1.0", "description": "Initial compliant release."}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "notification-service"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_1005",
        instruction=(
            "Your mission is to execute the **Infrastructure Hardening Policy** for the 'infra-terraform' repository. The policy requires addressing identified compliance gaps by tracking each item as a separate issue and resolving it via a dedicated pull request. "
            "You are responsible for executing this process for all items listed in the **Hardening Manifest**. "
            "Your final deliverable is a report of commits by author to verify that the 'ops-team' completed all required changes.\n\n"
            "**Hardening Manifest:**\n"
            "* **Work Items:** [\n"
            "    {title: 'Add restrictive security group rules'},\n"
            "    {title: 'Enable S3 bucket access logging'}\n"
            "]"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "infra-terraform", "title": "Add restrictive security group rules", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 12, "assignees": ["ops-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "infra-terraform", "branch": "feature/sg-rules", "message": "feat: Implement restrictive ingress rules", "author": "ops-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "infra-terraform", "title": "feat: Add restrictive security groups", "body": "", "head_branch": "feature/sg-rules", "base_branch": "main", "author": "ops-team"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "infra-terraform", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 12}),
            Action(name="create_issue", kwargs={"repo_name": "infra-terraform", "title": "Enable S3 bucket access logging", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 13, "assignees": ["ops-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "infra-terraform", "branch": "feature/s3-logging", "message": "feat: Enable server access logging for all buckets", "author": "ops-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "infra-terraform", "title": "feat: Enable S3 access logging", "body": "", "head_branch": "feature/s3-logging", "base_branch": "main", "author": "ops-team"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "infra-terraform", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 13}),
            Action(name="count_commits_by_author", kwargs={"repo_name": "infra-terraform"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "infra-terraform",
                    "commits_by_author": {
                        "ops-team": 2
                    },
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_1003",
        instruction=(
            "Your mission is to execute the **Full Security Audit and Remediation Policy** on the 'acme-webapp' repository. You must remediate the vulnerabilities detailed in the **Data Specification** and ensure the repository's final state fully aligns with the official **Compliance Specification** below. "
            "Your final deliverable is a health summary certifying that all identified vulnerabilities have been resolved.\n\n"
            "**Compliance Specification:**\n"
            "* **Vulnerability Remediation:** Both the 'high' and 'medium' severity alerts must be in a 'fixed' state.\n"
            "* **Incident Tracking:** Two corresponding issues, one for each vulnerability, must be created to track the remediation and must be in a 'closed' state.\n"
            "* **Code Consolidation:** The code fixes for both vulnerabilities must be consolidated into a single 'merged' Pull Request.\n"
            "* **Release:** A new, secure version 'v1.1.0' must be released, described as 'Security hardening release.'\n\n"
            "**Data Specification:**\n"
            "* High-Severity Alert: {description: 'Cross-Site Scripting (XSS) in user profile page', file: 'src/app/profile.html'}\n"
            "* Medium-Severity Alert: {description: 'Insecure Direct Object Reference in API', file: 'src/app/api.py'}\n"
            "* Issue Titles: ['Fix XSS in profile page', 'Fix IDOR in API']\n"
            "* Code Artifacts: {branch: 'security/hardening-sprint', commit_message: 'fix: Harden XSS and IDOR vulnerabilities', pr_title: 'fix: Security Hardening', author: 'alice-w'}\n"
            "* Release Details: {version: 'v1.1.0', description: 'Security hardening release.'}"
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "acme-webapp", "severity": "high", "description": "Cross-Site Scripting (XSS) in user profile page", "file": "src/app/profile.html", "branch": "main"}),
            Action(name="create_security_alert", kwargs={"repo_name": "acme-webapp", "severity": "medium", "description": "Insecure Direct Object Reference in API", "file": "src/app/api.py", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "Fix XSS in profile page", "body": ""}),
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "Fix IDOR in API", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12, "assignees": ["alice-w"]}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 13, "assignees": ["alice-w"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "acme-webapp", "branch": "security/hardening-sprint", "message": "fix: Harden XSS and IDOR vulnerabilities", "author": "alice-w"}),
            Action(name="open_pull_request", kwargs={"repo_name": "acme-webapp", "title": "fix: Security Hardening", "body": "", "head_branch": "security/hardening-sprint", "base_branch": "main", "author": "alice-w"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 10, "issue_number": 12}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12}),
            Action(name="close_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 13}),
            Action(name="fix_security_alert", kwargs={"repo_name": "acme-webapp", "alert_number": 10}),
            Action(name="fix_security_alert", kwargs={"repo_name": "acme-webapp", "alert_number": 11}),
            Action(name="create_release", kwargs={"repo_name": "acme-webapp", "version": "v1.1.0", "description": "Security hardening release."}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "acme-webapp"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_9003",
        instruction=(
            "Your mission is to execute the **Feature Development Lifecycle Policy** for the 'ui-kit' repository. The policy requires that a new feature is tracked, implemented, and reviewed before being merged. You must use the provided **Feature Manifest** to create all required artifacts. Your final deliverable is the repository's activity dashboard to certify that the feature was successfully integrated.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a new feature was tracked via an issue, which must be 'closed'. The work must be implemented on a feature branch and submitted via a pull request. The pull request must be reviewed before it is merged.\n\n"
            "**Feature Manifest:**\n"
            "* **Issue:** {title: 'Feature: Add user avatar component', body: 'Tracking issue for the new user avatar component.', labels: ['feature', 'ui'], assignee: 'ui-dev'}\n"
            "* **Code Artifacts:** {branch: 'feature/avatar-component', commit_message: 'feat: Add new user avatar component', pr_title: 'feat: User Avatar Component', pr_body: 'This PR adds the new user avatar component.', author: 'ui-dev'}\n"
            "* **Reviewer:** 'design-lead'"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Feature: Add user avatar component", "body": "Tracking issue for the new user avatar component.", "labels": ["feature", "ui"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12, "assignees": ["ui-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/avatar-component", "message": "feat: Add new user avatar component", "author": "ui-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "feat: User Avatar Component", "body": "This PR adds the new user avatar component.", "head_branch": "feature/avatar-component", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "ui-kit", "pr_number": 10, "reviewers": ["design-lead"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "ui-kit"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "ui-kit",
                    "commits_count": 1,
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_4001",
        instruction=(
            "Your mission is to execute the **Repository Re-branding Policy** for the 'portfolio-site' repository, which is being repurposed as a new team blog. "
            "The policy requires creating the repository and updating its metadata, tracking all related changes through issues. Your final deliverable is a list of all commits made during the rebranding process to serve as an audit trail.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that the repository was created as private and its description updated. An epic issue must be created and closed to track the entire rebranding initiative. "
            "Two sub-task issues must also be created and closed to track specific actions. All work must be consolidated into a single merged pull request.\n\n"
            "**Data Specification:**\n"
            "* Repo Name: 'portfolio-site'\n"
            "* Initial Description: 'Personal portfolio website.'\n"
            "* New Description: 'A new blog for the engineering team.'\n"
            "* Epic Title: 'Rebrand portfolio-site to Team Blog'\n"
            "* Task Titles: ['Update index.html with blog layout', 'Add new blog-styles.css file']\n"
            "* Assignee/Author: 'intern-sarah'\n"
            "* Code Artifacts: {branch: 'feature/rebrand', commit_message: 'feat: Rebrand site to team blog', pr_title: 'feat: Team Blog Rebrand'}"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "portfolio-site", "description": "Personal portfolio website.", "private": True}),
            Action(name="update_repository_description", kwargs={"repo_name": "portfolio-site", "description": "A new blog for the engineering team."}),
            Action(name="create_issue", kwargs={"repo_name": "portfolio-site", "title": "Rebrand portfolio-site to Team Blog", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "portfolio-site", "issue_number": 12, "assignees": ["intern-sarah"]}),
            Action(name="create_issue", kwargs={"repo_name": "portfolio-site", "title": "Update index.html with blog layout", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "portfolio-site", "issue_number": 13, "assignees": ["intern-sarah"]}),
            Action(name="create_issue", kwargs={"repo_name": "portfolio-site", "title": "Add new blog-styles.css file", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "portfolio-site", "issue_number": 14, "assignees": ["intern-sarah"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "portfolio-site", "branch": "feature/rebrand", "message": "feat: Rebrand site to team blog", "author": "intern-sarah"}),
            Action(name="open_pull_request", kwargs={"repo_name": "portfolio-site", "title": "feat: Team Blog Rebrand", "body": "", "head_branch": "feature/rebrand", "base_branch": "main", "author": "intern-sarah"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "portfolio-site", "pr_number": 10, "issue_number": 12}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "portfolio-site", "pr_number": 10, "issue_number": 13}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "portfolio-site", "pr_number": 10, "issue_number": 14}),
            Action(name="merge_pull_request", kwargs={"repo_name": "portfolio-site", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "portfolio-site", "issue_number": 13}),
            Action(name="close_issue", kwargs={"repo_name": "portfolio-site", "issue_number": 14}),
            Action(name="close_issue", kwargs={"repo_name": "portfolio-site", "issue_number": 12}),
            Action(name="list_commits_by_branch", kwargs={"repo_name": "portfolio-site", "branch": "feature/rebrand"}),
        ],
        outputs=[
            [
                {
                    "commit_id": "e4d3bffc0cca",
                    "repo": "portfolio-site",
                    "branch": "feature/rebrand",
                    "message": "feat: Rebrand site to team blog",
                    "author": "intern-sarah",
                    "timestamp": "2025-08-26"
                }
            ]
        ],
    ),
    Task(
        annotator="1",
        user_id="user_60001",
        instruction=(
            "Your mission is to execute the **Hotfix Porting and Verification Policy** for the 'security-scanner' repository. A critical hotfix, v0.4.1, which was previously applied to a release branch, must now be ported back to the main development line. The policy requires a full and auditable trail for this process, culminating in a new verification task for QA. Your final deliverable is a set of reports—the repository's activity dashboard and an issue aging report—to confirm the process is complete and to help prioritize the new verification task.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that the porting effort was tracked via a main issue, which must now be 'closed'. All code changes must be consolidated into a single 'merged' pull request on the 'hotfix/parser-revert-port' branch. This PR must contain commits from multiple authors covering the revert, conflict resolution, and updated tests. A new follow-up issue for verification must be created and left 'open'.\n\n"
            "**Data Manifest:**\n"
            "* **Porting Task:** {main_issue_title: 'Port hotfix v0.4.1 to main', main_issue_body: 'Main tracking issue for porting hotfix v0.4.1 to the main branch.', labels: ['hotfix', 'porting'], assignee: 'security-team'}\n"
            "* **Verification Task:** {qa_issue_title: 'Verify hotfix integration in next release', qa_issue_body: 'Create a formal verification plan for the ported hotfix in the upcoming release.', labels: ['verification', 'qa'], assignee: 'qa-erin'}\n"
            "* **Implementation:**\n"
            "    * **PR:** {title: 'chore: Port hotfix v0.4.1 to main', body: 'PR to port the emergency hotfix back to the main development line.', reviewers: ['security-team', 'tech-lead-tara', 'qa-erin']}\n"
            "    * **Commits:** [\n"
            "        {message: 'revert: Revert parser engine to stable version', author: 'security-team'},\n"
            "        {message: 'refactor: Resolve merge conflicts with main', author: 'security-team'},\n"
            "        {message: 'test: Update tests for main branch compatibility', author: 'qa-erin'}\n"
            "    ]"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Port hotfix v0.4.1 to main", "body": "Main tracking issue for porting hotfix v0.4.1 to the main branch.", "labels": ["hotfix", "porting"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "hotfix/parser-revert-port", "message": "revert: Revert parser engine to stable version", "author": "security-team"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "hotfix/parser-revert-port", "message": "refactor: Resolve merge conflicts with main", "author": "security-team"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "hotfix/parser-revert-port", "message": "test: Update tests for main branch compatibility", "author": "qa-erin"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "chore: Port hotfix v0.4.1 to main", "body": "PR to port the emergency hotfix back to the main development line.", "head_branch": "hotfix/parser-revert-port", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 10, "reviewers": ["security-team", "tech-lead-tara", "qa-erin"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Verify hotfix integration in next release", "body": "Create a formal verification plan for the ported hotfix in the upcoming release.", "labels": ["verification", "qa"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["qa-erin"]}),
            Action(name="get_issue_aging_report", kwargs={"repo_name": "security-scanner"}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
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
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_304",
        instruction=(
            "Your role is to execute the company's **Production Incident Response Policy** for the 'security-scanner' repository. A faulty deployment has caused a critical production alert. "
            "You must manage the full incident lifecycle, which includes releasing a hotfix and initiating a post-mortem, using the provided **Incident Manifest**. "
            "Your final deliverable is the repository health summary, confirming the incident is resolved and a post-mortem is underway.\n\n"
            "**Incident Manifest:**\n"
            "* **Faulty Release:**\n"
            "    * **Details:** {version: '0.4.0', description: 'Release with new parser engine.'}\n"
            "    * **Code:** {commit_message: 'feat: Rollout new parser engine', branch: 'release/v0.4.0', pr_title: 'Release v0.4.0', pr_body: 'PR for v0.4.0 release.'}\n"
            "    * **Deployment:** {environment: 'production-v0.4.0'}\n"
            "* **Incident Alert:**\n"
            "    * **Details:** {severity: 'critical', description: 'Production Outage: Invalid parser config deployed causes infinite loop.', file: 'src/parser.rs', branch: 'main'}\n"
            "* **Hotfix:**\n"
            "    * **Issue:** {title: 'HOTFIX: Production outage in parser engine', body: 'Tracking issue for the emergency hotfix.', labels: ['bug', 'hotfix', 'production-issue'], assignee: 'security-team'}\n"
            "    * **Code:** {branch: 'hotfix/parser-revert', commit_message: 'revert: Revert parser engine to stable version'}\n"
            "    * **PR:** {title: 'Hotfix: Revert parser engine change', body: 'Hotfix PR to revert the parser engine.'}\n"
            "    * **Release:** {version: '0.4.1', description: 'Hotfix release to revert faulty parser engine.'}\n"
            "    * **Deployment:** {environment: 'production-v0.4.1'}\n"
            "* **Post-Mortem:**\n"
            "    * **Issue:** {title: 'Post-Mortem: Parser Engine Outage v0.4.0', body: 'Post-mortem investigation tracking issue.', labels: ['post-mortem', 'audit'], assignee: 'tech-lead-tara'}"
        ),
        actions=[
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "release/v0.4.0", "message": "feat: Rollout new parser engine", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "Release v0.4.0", "body": "PR for v0.4.0 release.", "head_branch": "release/v0.4.0", "base_branch": "main"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="create_release", kwargs={"repo_name": "security-scanner", "version": "0.4.0", "description": "Release with new parser engine."}),
            Action(name="register_deploy_event", kwargs={"repo_name": "security-scanner", "environment": "production-v0.4.0"}),
            Action(name="create_security_alert", kwargs={"repo_name": "security-scanner", "severity": "critical", "description": "Production Outage: Invalid parser config deployed causes infinite loop.", "file": "src/parser.rs", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "HOTFIX: Production outage in parser engine", "body": "Tracking issue for the emergency hotfix.", "labels": ["bug", "hotfix", "production-issue"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "hotfix/parser-revert", "message": "revert: Revert parser engine to stable version", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "Hotfix: Revert parser engine change", "body": "Hotfix PR to revert the parser engine.", "head_branch": "hotfix/parser-revert", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 11, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12}),
            Action(name="create_release", kwargs={"repo_name": "security-scanner", "version": "0.4.1", "description": "Hotfix release to revert faulty parser engine."}),
            Action(name="register_deploy_event", kwargs={"repo_name": "security-scanner", "environment": "production-v0.4.1"}),
            Action(name="fix_security_alert", kwargs={"repo_name": "security-scanner", "alert_number": 10}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Post-Mortem: Parser Engine Outage v0.4.0", "body": "Post-mortem investigation tracking issue.", "labels": ["post-mortem", "audit"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["tech-lead-tara"]}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_5002",
        instruction=(
            "Your mission is to execute the **Core Refactor Policy** for the 'payments-service' repository. The policy requires that major refactoring work is tracked via a main epic and specific sub-tasks, with all code changes consolidated into a single pull request. "
            "You are responsible for executing this process using the provided **Refactor Manifest**. "
            "Your final deliverable is a dual report: one counting commits by author to verify the work, and another checking the repository's risk score to ensure no new security issues were introduced.\n\n"
            "**Refactor Manifest: Q3 Performance**\n"
            "* **Tracking:**\n"
            "    * **Epic:** {title: 'Q3 Performance Refactor', body: ''}\n"
            "    * **Sub-Tasks:** [{title: 'Optimize database query patterns', body: ''}, {title: 'Implement caching layer for responses', body: ''}]\n"
            "* **Implementation:**\n"
            "    * **Branch:** 'refactor/performance-q3'\n"
            "    * **Commits:** [{message: 'refactor: Optimize DB queries'}, {message: 'feat: Add caching layer'}]\n"
            "    * **PR:** {title: 'refactor: Q3 Performance Improvements', body: ''}\n"
            "* **Ownership:** {assignee: 'backend-core', author: 'backend-core'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "payments-service", "title": "Q3 Performance Refactor", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "payments-service", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="create_issue", kwargs={"repo_name": "payments-service", "title": "Optimize database query patterns", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "payments-service", "issue_number": 13, "assignees": ["backend-core"]}),
            Action(name="create_issue", kwargs={"repo_name": "payments-service", "title": "Implement caching layer for responses", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "payments-service", "issue_number": 14, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-service", "branch": "refactor/performance-q3", "message": "refactor: Optimize DB queries", "author": "backend-core"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-service", "branch": "refactor/performance-q3", "message": "feat: Add caching layer", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "payments-service", "title": "refactor: Q3 Performance Improvements", "body": "", "head_branch": "refactor/performance-q3", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "payments-service", "pr_number": 10, "issue_number": 12}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "payments-service", "pr_number": 10, "issue_number": 13}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "payments-service", "pr_number": 10, "issue_number": 14}),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "payments-service", "issue_number": 13}),
            Action(name="close_issue", kwargs={"repo_name": "payments-service", "issue_number": 14}),
            Action(name="close_issue", kwargs={"repo_name": "payments-service", "issue_number": 12}),
            Action(name="count_commits_by_author", kwargs={"repo_name": "payments-service"}),
            Action(name="get_repository_risk_score", kwargs={"repo_name": "payments-service"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "payments-service",
                    "commits_by_author": {
                        "backend-core": 2
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_6001",
        instruction=(
            "Your mission is to govern the repurposing of the 'portfolio-site' repository into a new team blog, ensuring full compliance with the company's **Repository Re-branding Policy**. "
            "This policy requires that the entire initiative, from repository creation and metadata updates to the implementation of changes, is formally tracked via a main epic and specific sub-tasks. "
            "All work must be consolidated into a single, auditable pull request. You are responsible for executing this process using the provided **Re-branding Manifest**. "
            "Your final deliverable is a list of all commits made during the rebranding process to serve as an audit trail.\n\n"
            "**Re-branding Manifest:**\n"
            "* **Repository:** {name: 'portfolio-site', initial_description: 'Personal portfolio website.', new_description: 'A new blog for the engineering team.', private: True}\n"
            "* **Tracking:**\n"
            "    * **Epic:** {title: 'Rebrand portfolio-site to Team Blog', body: ''}\n"
            "    * **Sub-Tasks:** [{title: 'Update index.html with blog layout', body: ''}, {title: 'Add new blog-styles.css file', body: ''}]\n"
            "* **Implementation:**\n"
            "    * **Branch:** 'feature/rebrand'\n"
            "    * **Commit:** {message: 'feat: Rebrand site to team blog'}\n"
            "    * **PR:** {title: 'feat: Team Blog Rebrand', body: ''}\n"
            "* **Ownership:** {assignee: 'intern-sarah', author: 'intern-sarah'}"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "portfolio-site", "description": "Personal portfolio website.", "private": True}),
            Action(name="update_repository_description", kwargs={"repo_name": "portfolio-site", "description": "A new blog for the engineering team."}),
            Action(name="create_issue", kwargs={"repo_name": "portfolio-site", "title": "Rebrand portfolio-site to Team Blog", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "portfolio-site", "issue_number": 12, "assignees": ["intern-sarah"]}),
            Action(name="create_issue", kwargs={"repo_name": "portfolio-site", "title": "Update index.html with blog layout", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "portfolio-site", "issue_number": 13, "assignees": ["intern-sarah"]}),
            Action(name="create_issue", kwargs={"repo_name": "portfolio-site", "title": "Add new blog-styles.css file", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "portfolio-site", "issue_number": 14, "assignees": ["intern-sarah"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "portfolio-site", "branch": "feature/rebrand", "message": "feat: Rebrand site to team blog", "author": "intern-sarah"}),
            Action(name="open_pull_request", kwargs={"repo_name": "portfolio-site", "title": "feat: Team Blog Rebrand", "body": "", "head_branch": "feature/rebrand", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "portfolio-site", "pr_number": 10, "issue_number": 12}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "portfolio-site", "pr_number": 10, "issue_number": 13}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "portfolio-site", "pr_number": 10, "issue_number": 14}),
            Action(name="merge_pull_request", kwargs={"repo_name": "portfolio-site", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "portfolio-site", "issue_number": 13}),
            Action(name="close_issue", kwargs={"repo_name": "portfolio-site", "issue_number": 14}),
            Action(name="close_issue", kwargs={"repo_name": "portfolio-site", "issue_number": 12}),
            Action(name="list_commits_by_branch", kwargs={"repo_name": "portfolio-site", "branch": "feature/rebrand"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": [
                    {
                        "commit_id": "e4d3bffc0cca",
                        "repo": "portfolio-site",
                        "branch": "feature/rebrand",
                        "message": "feat: Rebrand site to team blog",
                        "author": "intern-sarah",
                        "timestamp": "2025-08-26",
                        "report_date": "2025-08-26"
                    }
                ]
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_105",
        instruction=(
            "Your primary objective is to execute the company's **Standard Project Bootstrap Policy** for the new 'log-analyzer-service'. "
            "This policy ensures all new projects are created with a consistent set of initial artifacts for tracking, security, and "
            "deployment readiness. You must use the provided **Bootstrap Manifest** to create all required entities and ensure the final state "
            "adheres to the **Compliance Specification**.\n\n"
            "**Compliance Specification:**\n"
            "* The first new issue created for this task must be `number: 12`.\n"
            "* The first new security alert created for this task must be `number: 10`.\n\n"
            "**Bootstrap Manifest:**\n"
            "* **Repository:** {name: 'log-analyzer-service', description: 'Service for parsing and analyzing application logs.', private: True}\n"
            "* **Initial Commit:** {author: 'backend-core', message: 'Initial commit: project structure and boilerplate'}\n"
            "* **Tracking Issue:** {title: 'Define initial logging schema', body: 'Establish the standard JSON schema for log entries.', labels: ['schema', 'design'], assignee: 'backend-core'}\n"
            "* **Initial Security Alert:** {severity: 'high', description: 'Potential for arbitrary code execution via insecure YAML parsing.', file: 'src/parser.py', branch: 'main'}\n"
            "* **Initial Deployment:** {environment: 'development'}"
        ),
        actions=[
            Action(name="create_repository", kwargs={
                "repo_name": "log-analyzer-service",
                "description": "Service for parsing and analyzing application logs.",
                "private": True
            }),
            Action(name="add_commit_to_branch", kwargs={
                "repo_name": "log-analyzer-service",
                "branch": "main",
                "message": "Initial commit: project structure and boilerplate",
                "author": "backend-core"
            }),
            Action(name="create_issue", kwargs={
                "repo_name": "log-analyzer-service",
                "title": "Define initial logging schema",
                "body": "Establish the standard JSON schema for log entries.",
                "labels": ["schema", "design"]
            }),
            Action(name="assign_issue", kwargs={"repo_name": "log-analyzer-service", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="create_security_alert", kwargs={
                "repo_name": "log-analyzer-service",
                "severity": "high",
                "description": "Potential for arbitrary code execution via insecure YAML parsing.",
                "file": "src/parser.py",
                "branch": "main"
            }),
            Action(name="register_deploy_event", kwargs={"repo_name": "log-analyzer-service", "environment": "development"}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "log-analyzer-service"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_701",
        instruction=(
            "Your primary strategic objective is to govern the integration of a critical hotfix into the main development line for the 'security-scanner' "
            "repository, ensuring it fully aligns with the company's **Hotfix Porting and Verification Policy**. This policy mandates a clear and "
            "auditable trail for porting release-branch hotfixes back to main, including the creation of a follow-up verification task.\n\n"
            "You are responsible for executing this process using the provided **Porting Manifest**. Your final deliverable is a set of reports—the "
            "repository's activity dashboard and an issue aging report—to confirm the process is complete and to help prioritize the new verification task.\n\n"
            "**Porting Manifest:**\n"
            "* **Hotfix Version to Port:** v0.4.1\n"
            "* **Description:** The hotfix reverts the parser engine to a stable version and requires porting back to the 'main' branch. The work will involve resolving merge conflicts and updating tests.\n"
            "* **Ownership:** The porting task is owned by 'security-team', with testing support from 'qa-erin'. The follow-up verification task should be assigned to 'qa-erin'.\n"
            "* **Review:** The porting pull request requires review from 'security-team', 'tech-lead-tara', and 'qa-erin'."
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Port hotfix v0.4.1 to main", "body": "Main tracking issue for porting hotfix v0.4.1 to the main branch.", "labels": ["hotfix", "porting"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "hotfix/parser-revert-port", "message": "revert: Revert parser engine to stable version", "author": "security-team"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "hotfix/parser-revert-port", "message": "refactor: Resolve merge conflicts with main", "author": "security-team"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "hotfix/parser-revert-port", "message": "test: Update tests for main branch compatibility", "author": "qa-erin"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "chore: Port hotfix v0.4.1 to main", "body": "PR to port the emergency hotfix back to the main development line.", "head_branch": "hotfix/parser-revert-port", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 10, "reviewers": ["security-team", "tech-lead-tara", "qa-erin"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Verify hotfix integration in next release", "body": "Create a formal verification plan for the ported hotfix in the upcoming release.", "labels": ["verification", "qa"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["qa-erin"]}),
            Action(name="get_issue_aging_report", kwargs={"repo_name": "security-scanner"}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
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
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ]
    ),
    Task(
        annotator="1",
        user_id="user_2003",
        instruction=(
            "Ensure the 'ml-pipeline' repository is compliant with the **Proactive Dependency Update Policy** by applying the update for the scikit-learn library as specified in the **Update Manifest**. "
            "The final deliverable must be the repository's activity dashboard to certify the update is complete.\n\n"
            "**Update Manifest: scikit-learn**\n"
            "* **Tracking Issue:** {title: 'chore(deps): Update scikit-learn to latest version', body: 'Update the scikit-learn dependency to the latest stable version.', labels: ['chore', 'dependencies'], assignee: 'ml-engineer'}\n"
            "* **Implementation:**\n"
            "    * **Branch:** 'chore/update-sklearn'\n"
            "    * **Commit:** {message: 'chore: Update scikit-learn to v1.4.0', author: 'ml-engineer'}\n"
            "    * **PR:** {title: 'chore(deps): Update scikit-learn', body: 'This PR updates scikit-learn.'}\n"
            "* **Reviewer:** 'data-scientist'"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "ml-pipeline", "title": "chore(deps): Update scikit-learn to latest version", "body": "Update the scikit-learn dependency to the latest stable version.", "labels": ["chore", "dependencies"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ml-pipeline", "issue_number": 12, "assignees": ["ml-engineer"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ml-pipeline", "branch": "chore/update-sklearn", "message": "chore: Update scikit-learn to v1.4.0", "author": "ml-engineer"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ml-pipeline", "title": "chore(deps): Update scikit-learn", "body": "This PR updates scikit-learn.", "head_branch": "chore/update-sklearn", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ml-pipeline", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "ml-pipeline", "pr_number": 10, "reviewers": ["data-scientist"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ml-pipeline", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ml-pipeline", "issue_number": 12}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "ml-pipeline"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "ml-pipeline",
                    "commits_count": 1,
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_604",
        instruction=(
            "Your primary strategic objective is to execute the **Quarterly Tech Debt Initiative Policy** for the 'security-scanner' repository. "
            "This policy mandates that a central epic tracks all planned refactoring work for the quarter and that each individual tech debt item is resolved sequentially, with each resolution being formally tracked and merged via its own pull request. "
            "You are responsible for executing this process using the provided **Tech Debt Manifest**. "
            "Your final deliverable is the repository's activity dashboard to confirm all tech debt items for the quarter have been resolved, with the main epic remaining open to track the overall initiative.\n\n"
            "**Tech Debt Manifest (Q3):**\n"
            "* **Main Epic:** {title: 'Q3 Tech Debt Paydown', body: 'Main epic to track all Q3 tech debt sub-tasks.', labels: ['tech-debt', 'epic'], assignee: 'tech-lead-tara'}\n"
            "* **Sub-Task Issues:** [\n"
            "    {title: 'Refactor Parser Module', body: 'Sub-task to track the refactoring of the parser module.', labels: ['tech-debt', 'refactor'], assignee: 'security-team'},\n"
            "    {title: 'Update Deprecated Dependencies', body: 'Sub-task to track the update of deprecated dependencies.', labels: ['tech-debt', 'chore'], assignee: 'security-team'},\n"
            "    {title: 'Remove Deprecated Handlers', body: 'Sub-task to track the removal of deprecated v1 handlers.', labels: ['tech-debt', 'refactor'], assignee: 'security-team'}\n"
            "]\n"
            "* **Code Implementations:** [\n"
            "    {branch: 'refactor/parser', commit_message: 'refactor: Simplify parser logic', author: 'security-team'},\n"
            "    {branch: 'chore/update-deps', commit_message: 'chore: Update all dependencies to latest stable', author: 'security-team'},\n"
            "    {branch: 'refactor/remove-handlers', commit_message: 'refactor: Remove unused v1 handlers', author: 'security-team'}\n"
            "]\n"
            "* **Pull Requests:** [\n"
            "    {title: 'refactor: Parser Module', body: 'PR to implement the parser refactor.', reviewers: ['tech-lead-tara']},\n"
            "    {title: 'chore: Update Dependencies', body: 'PR to update all dependencies to their latest stable versions.', reviewers: ['tech-lead-tara']},\n"
            "    {title: 'refactor: Remove Deprecated Handlers', body: 'PR to remove the unused v1 handlers.', reviewers: ['tech-lead-tara']}\n"
            "]"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Q3 Tech Debt Paydown", "body": "Main epic to track all Q3 tech debt sub-tasks.", "labels": ["tech-debt", "epic"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["tech-lead-tara"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Refactor Parser Module", "body": "Sub-task to track the refactoring of the parser module.", "labels": ["tech-debt", "refactor"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "refactor/parser", "message": "refactor: Simplify parser logic", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "refactor: Parser Module", "body": "PR to implement the parser refactor.", "head_branch": "refactor/parser", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 13}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Update Deprecated Dependencies", "body": "Sub-task to track the update of deprecated dependencies.", "labels": ["tech-debt", "chore"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 14, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "chore/update-deps", "message": "chore: Update all dependencies to latest stable", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "chore: Update Dependencies", "body": "PR to update all dependencies to their latest stable versions.", "head_branch": "chore/update-deps", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 11, "issue_number": 14}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 11, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 14}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Remove Deprecated Handlers", "body": "Sub-task to track the removal of deprecated v1 handlers.", "labels": ["tech-debt", "refactor"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 15, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "refactor/remove-handlers", "message": "refactor: Remove unused v1 handlers", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "refactor: Remove Deprecated Handlers", "body": "PR to remove the unused v1 handlers.", "head_branch": "refactor/remove-handlers", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 12, "issue_number": 15}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 12, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 12}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 15}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "security-scanner",
                    "commits_count": 3,
                    "open_issues": 1,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_204",
        instruction=(
            "Your role is to execute the company's **Standard Year-End Governance Audit Policy** for the 'ui-kit' repository. This policy "
            "requires a comprehensive analysis of project activity and health metrics from the final quarter of the year. The policy mandates "
            "that all findings are consolidated into a formal summary issue. You must use the provided **Audit Manifest** to scope your "
            "analysis and create the required artifact. Your final deliverable is the complete end-to-end report for the repository to "
            "confirm the audit is complete.\n\n"
            "**Audit Manifest (Year-End 2023):**\n"
            "* **Analysis Scope:**\n"
            "    * Commit Date Range: Start='2023-10-01T00:00:00Z', End='2023-12-31T23:59:59Z'\n"
            "    * Issue Label Filter: 'bug'\n"
            "* **Summary Issue Artifact:**\n"
            "    * Title: 'Governance Audit Findings for Year-End 2023'\n"
            "    * Body: 'This issue summarizes the Year-End 2023 audit, covering performance, security, and backlog status.'\n"
            "    * Labels: ['audit', 'governance']\n"
            "    * Assignee: 'release-manager'"
        ),
        actions=[
            Action(name="count_commits_by_author", kwargs={"repo_name": "ui-kit"}),
            Action(name="list_commits_by_date_range", kwargs={"repo_name": "ui-kit", "start_date": "2023-10-01T00:00:00Z", "end_date": "2023-12-31T23:59:59Z"}),
            Action(name="get_issue_aging_report", kwargs={"repo_name": "ui-kit"}),
            Action(name="list_issues_by_label", kwargs={"repo_name": "ui-kit", "label": "bug"}),
            Action(name="get_pull_request_merge_time_report", kwargs={"repo_name": "ui-kit"}),
            Action(name="list_pull_requests", kwargs={"repo_name": "ui-kit", "state": "open"}),
            Action(name="get_open_security_alerts", kwargs={"repo_name": "ui-kit"}),
            Action(name="get_repository_risk_score", kwargs={"repo_name": "ui-kit"}),
            Action(name="get_releases_by_repository", kwargs={"repo_name": "ui-kit"}),
            Action(name="get_deployment_frequency_report", kwargs={"repo_name": "ui-kit"}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Governance Audit Findings for Year-End 2023", "body": "This issue summarizes the Year-End 2023 audit, covering performance, security, and backlog status.", "labels": ["audit", "governance"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12, "assignees": ["release-manager"]}),
            Action(name="generate_end_to_end_report", kwargs={"repo_name": "ui-kit"}),
        ],
        outputs=[
            {
                "repo": "ui-kit",
                "commits_count": 0,
                "open_issues": 1,
                "merged_prs": 0,
                "open_alerts": 0,
                "releases_count": 0,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_30002",
        instruction=(
            "Your mission is to execute the **Cross-Repo Incompatibility Policy**. A feature-in-progress in 'react-dashboard' has triggered a new high-severity alert due to an incompatibility with the 'ui-kit' dependency. "
            "The policy requires pausing the feature work, fixing the root cause in the dependency, and then resuming and completing the feature work. You are responsible for executing this coordinated process using the provided **Incompatibility Manifest**. "
            "Your final deliverable is a set of cross-entity reports for both repositories to certify the resolution.\n\n"
            "**Incompatibility Manifest:**\n"
            "* **`react-dashboard` (Downstream Consumer):**\n"
            "    * **Alert:** {description: 'Component crashing due to ui-kit incompatibility', file: 'src/components/NewFeature.tsx', severity: 'high', branch: 'feature/analytics-chart'}\n"
            "    * **Feature:** {issue_title: 'Feature: New analytics chart', issue_body: '', branch: 'feature/analytics-chart', pr_title: 'Feature: New analytics chart', pr_body: 'This PR completes the analytics chart feature after the upstream fix.'}\n"
            "    * **Code:** {initial_commit: 'feat: Initial analytics chart structure', final_commit: 'fix: Update component to support new ui-kit version', author: 'frontend-dev'}\n"
            "* **`ui-kit` (Upstream Dependency):**\n"
            "    * **Bug:** {issue_title: 'Bug: Prop validation fails in Card component', issue_body: 'The Card component prop validation is too strict, causing crashes in downstream consumers.', assignee: 'ui-dev'}\n"
            "    * **Code:** {branch: 'fix/prop-validation', commit_message: 'fix: Add backward compatibility for Card props', pr_title: 'fix: Prop validation', pr_body: 'This PR relaxes prop validation for backward compatibility.', author: 'ui-dev'}"
        ),
        actions=[
            Action(name="add_commit_to_branch", kwargs={"repo_name": "react-dashboard", "branch": "feature/analytics-chart", "message": "feat: Initial analytics chart structure", "author": "frontend-dev"}),
            Action(name="create_security_alert", kwargs={"repo_name": "react-dashboard", "severity": "high", "description": "Component crashing due to ui-kit incompatibility", "file": "src/components/NewFeature.tsx", "branch": "feature/analytics-chart"}),
            Action(name="create_issue", kwargs={"repo_name": "react-dashboard", "title": "Feature: New analytics chart", "body": ""}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Bug: Prop validation fails in Card component", "body": "The Card component prop validation is too strict, causing crashes in downstream consumers."}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 13, "assignees": ["ui-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "fix/prop-validation", "message": "fix: Add backward compatibility for Card props", "author": "ui-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "fix: Prop validation", "body": "This PR relaxes prop validation for backward compatibility.", "head_branch": "fix/prop-validation", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 13}),
            Action(name="assign_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 12, "assignees": ["frontend-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "react-dashboard", "branch": "feature/analytics-chart", "message": "fix: Update component to support new ui-kit version", "author": "frontend-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "react-dashboard", "title": "Feature: New analytics chart", "body": "This PR completes the analytics chart feature after the upstream fix.", "head_branch": "feature/analytics-chart", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "react-dashboard", "pr_number": 11, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "react-dashboard", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 12}),
            Action(name="fix_security_alert", kwargs={"repo_name": "react-dashboard", "alert_number": 10}),
            Action(name="get_cross_entity_report", kwargs={"repo_name": "react-dashboard"}),
            Action(name="get_cross_entity_report", kwargs={"repo_name": "ui-kit"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "react-dashboard", "open_issues": 0, "merged_prs": 1, "recent_commits": 2, "open_alerts": 0, "last_deployment": "none", "report_date": "2025-08-26"
                }
            },
            {
                "status": "ok",
                "data": {
                    "repo": "ui-kit", "open_issues": 0, "merged_prs": 1, "recent_commits": 1, "open_alerts": 0, "last_deployment": "none", "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_602",
        instruction=(
            "Your primary strategic objective is to govern the response to a critical vulnerability in 'common-lib', ensuring all affected "
            "repositories align with the company's **Staggered Security Patching Protocol**. This protocol mandates a clear and auditable "
            "trail of patching activities, with a main epic tracking the entire initiative and sub-tasks for each affected repository according to their tier. "
            "You are responsible for executing this process using the provided **Patching Manifest**. Your final deliverable is a list of health summaries for the patched repositories to serve as the official record of policy compliance.\n\n"
            "**Patching Manifest: common-lib Vulnerability**\n"
            "* **Main Epic (Tracked in 'security-scanner'):** {title: 'URGENT: Patch common-lib vulnerability', body: 'Main epic to track patching of common-lib across all services.', labels: ['security', 'vulnerability', 'epic'], assignee: 'tech-lead-tara'}\n"
            "* **Tier 1 Service (`security-scanner`):**\n"
            "    * **Issue:** {title: '[Patch] Upgrade common-lib in security-scanner', body: 'Sub-task to track patching of common-lib in the security-scanner repository.', labels: ['security', 'patch'], assignee: 'security-team'}\n"
            "    * **Code:** {branch: 'hotfix/sec-lib-patch', commit_message: 'fix: Upgrade common-lib to v1.5.1', author: 'security-team'}\n"
            "    * **PR:** {title: 'fix(deps): Upgrade common-lib', body: 'This PR upgrades the vulnerable common-lib dependency to a patched version.'}\n"
            "    * **Release:** {version: 'v0.5.1', description: 'Security patch release.'}\n"
            "    * **Deployment:** {environment: 'production'}\n"
            "* **Tier 2 Service (`ui-kit`):**\n"
            "    * **Issue:** {title: '[Patch] Upgrade common-lib in ui-kit', body: 'Sub-task to track patching of common-lib in the ui-kit repository.', labels: ['security', 'patch'], assignee: 'ui-dev'}\n"
            "    * **Code:** {branch: 'hotfix/ui-lib-patch', commit_message: 'fix: Upgrade common-lib to v1.5.1', author: 'ui-dev'}\n"
            "    * **PR:** {title: 'fix(deps): Upgrade common-lib', body: 'This PR upgrades the vulnerable common-lib dependency to a patched version.'}\n"
            "    * **Release:** {version: 'v3.2.1', description: 'Security patch release.'}\n"
            "    * **Deployment:** {environment: 'staging'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "URGENT: Patch common-lib vulnerability", "body": "Main epic to track patching of common-lib across all services.", "labels": ["security", "vulnerability", "epic"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["tech-lead-tara"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "[Patch] Upgrade common-lib in security-scanner", "body": "Sub-task to track patching of common-lib in the security-scanner repository.", "labels": ["security", "patch"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "hotfix/sec-lib-patch", "message": "fix: Upgrade common-lib to v1.5.1", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "fix(deps): Upgrade common-lib", "body": "This PR upgrades the vulnerable common-lib dependency to a patched version.", "head_branch": "hotfix/sec-lib-patch", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13}),
            Action(name="create_release", kwargs={"repo_name": "security-scanner", "version": "v0.5.1", "description": "Security patch release."}),
            Action(name="register_deploy_event", kwargs={"repo_name": "security-scanner", "environment": "production"}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "[Patch] Upgrade common-lib in ui-kit", "body": "Sub-task to track patching of common-lib in the ui-kit repository.", "labels": ["security", "patch"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 14, "assignees": ["ui-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "hotfix/ui-lib-patch", "message": "fix: Upgrade common-lib to v1.5.1", "author": "ui-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "fix(deps): Upgrade common-lib", "body": "This PR upgrades the vulnerable common-lib dependency to a patched version.", "head_branch": "hotfix/ui-lib-patch", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 11, "issue_number": 14}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 14}),
            Action(name="create_release", kwargs={"repo_name": "ui-kit", "version": "v3.2.1", "description": "Security patch release."}),
            Action(name="register_deploy_event", kwargs={"repo_name": "ui-kit", "environment": "staging"}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "security-scanner"}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "ui-kit"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_10002",
        instruction=(
            "Your mission is to execute the **Documentation Update Policy** for the 'infra-terraform' repository. The policy requires that all documentation changes are formally tracked via an issue and implemented via a merged pull request. "
            "You must use the provided **Doc Manifest** to create the required artifacts. "
            "Your final deliverable is a list of commits for the relevant branch to serve as an audit trail.\n\n"
            "**Doc Manifest:**\n"
            "* **Issue:** {title: 'Docs: Add guide for new RDS module', body: 'Tracking issue for creating the RDS module documentation.', labels: ['documentation'], assignee: 'ops-team'}\n"
            "* **Implementation:** {branch: 'docs/rds-guide', commit_message: 'docs: Add usage guide for the new RDS module', author: 'ops-team'}\n"
            "* **PR:** {title: 'Docs: RDS Module Guide', body: 'This PR adds the new RDS module guide.'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "infra-terraform", "title": "Docs: Add guide for new RDS module", "body": "Tracking issue for creating the RDS module documentation.", "labels": ["documentation"]}),
            Action(name="assign_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 12, "assignees": ["ops-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "infra-terraform", "branch": "docs/rds-guide", "message": "docs: Add usage guide for the new RDS module", "author": "ops-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "infra-terraform", "title": "Docs: RDS Module Guide", "body": "This PR adds the new RDS module guide.", "head_branch": "docs/rds-guide", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "infra-terraform", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "infra-terraform", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 12}),
            Action(name="list_commits_by_branch", kwargs={"repo_name": "infra-terraform", "branch": "docs/rds-guide"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": [
                    {
                        "commit_id": "1c2fef47d1cf",
                        "repo": "infra-terraform",
                        "branch": "docs/rds-guide",
                        "message": "docs: Add usage guide for the new RDS module",
                        "author": "ops-team",
                        "timestamp": "2025-08-26",
                        "report_date": "2025-08-26"
                    }
                ]
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_20002",
        instruction=(
            "Your mission is to execute the **Documentation Update Policy** for the 'react-dashboard' repository. The policy requires that all documentation changes are formally tracked via an issue and implemented via a merged pull request. "
            "You must use the provided **Doc Manifest** to create the required artifacts. "
            "Your final deliverable is a list of commits for the branch to serve as an audit trail.\n\n"
            "**Doc Manifest:**\n"
            "* **Issue:** {title: 'Docs: Update README with new setup instructions', body: 'The README.md is outdated and needs to be updated with the new project setup instructions.', labels: ['documentation'], assignee: 'frontend-dev'}\n"
            "* **Implementation:** {branch: 'docs/readme-update', commit_message: 'docs: Update README with new setup instructions', pr_title: 'Docs: Update README', pr_body: 'This PR updates the README file.', author: 'frontend-dev'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "react-dashboard", "title": "Docs: Update README with new setup instructions", "body": "The README.md is outdated and needs to be updated with the new project setup instructions.", "labels": ["documentation"]}),
            Action(name="assign_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 12, "assignees": ["frontend-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "react-dashboard", "branch": "docs/readme-update", "message": "docs: Update README with new setup instructions", "author": "frontend-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "react-dashboard", "title": "Docs: Update README", "body": "This PR updates the README file.", "head_branch": "docs/readme-update", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "react-dashboard", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "react-dashboard", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 12}),
            Action(name="list_commits_by_branch", kwargs={"repo_name": "react-dashboard", "branch": "docs/readme-update"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": [
                    {
                        "commit_id": "80fc79c09e51",
                        "repo": "react-dashboard",
                        "branch": "docs/readme-update",
                        "message": "docs: Update README with new setup instructions",
                        "author": "frontend-dev",
                        "timestamp": "2025-08-26",
                        "report_date": "2025-08-26"
                    }
                ]
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_705",
        instruction=(
            "Your primary strategic objective is to govern the creation of the new 'notification-service' repository, ensuring it fully aligns "
            "with the company's **New Service Onboarding and Governance Policy**. This policy mandates that new services are not only technically "
            "bootstrapped but also meet initial governance and security compliance standards before their first release. You are responsible for "
            "executing this process using the provided **Onboarding Manifest**. Your final deliverable "
            "is the repository's health summary to confirm its compliant state.\n\n"
            "**Onboarding Manifest:**\n"
            "* **Repository:** {name: 'notification-service', description: 'Centralized service for handling user notifications.', private: True}\n"
            "* **Governance:**\n"
            "    * **Commits:** [{message: 'docs: Add MIT License', author: 'docs-amy'}, {message: 'docs: Add SECURITY.md policy', author: 'docs-amy'}]\n"
            "    * **Ops Issue:** {title: 'ops: Configure main branch protection rules', body: 'Tracking issue for branch protection setup as per governance policy.', labels: ['ops', 'governance'], assignee: 'devops-lead'}\n"
            "* **Security Remediation:**\n"
            "    * **Alert:** {severity: 'medium', description: 'Default template includes outdated dependency: common-lib v1.2.3', file: 'package.json', branch: 'main'}\n"
            "    * **Issue:** {title: 'fix: Update outdated dependency common-lib', body: 'Tracking issue to update the vulnerable common-lib dependency.', labels: ['security', 'dependency'], assignee: 'devops-lead'}\n"
            "    * **Code:** {branch: 'fix/update-common-lib', commit_message: 'fix: Upgrade common-lib to v1.2.4', author: 'devops-lead'}\n"
            "    * **PR:** {title: 'fix(deps): Upgrade common-lib to v1.2.4', body: 'PR to upgrade outdated common-lib dependency to v1.2.4.'}\n"
            "* **Release:** {version: 'v0.1.0', description: 'Initial compliant release.'}"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "notification-service", "description": "Centralized service for handling user notifications.", "private": True}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "notification-service", "branch": "main", "message": "docs: Add MIT License", "author": "docs-amy"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "notification-service", "branch": "main", "message": "docs: Add SECURITY.md policy", "author": "docs-amy"}),
            Action(name="create_issue", kwargs={"repo_name": "notification-service", "title": "ops: Configure main branch protection rules", "body": "Tracking issue for branch protection setup as per governance policy.", "labels": ["ops", "governance"]}),
            Action(name="assign_issue", kwargs={"repo_name": "notification-service", "issue_number": 12, "assignees": ["devops-lead"]}),
            Action(name="create_security_alert", kwargs={"repo_name": "notification-service", "severity": "medium", "description": "Default template includes outdated dependency: common-lib v1.2.3", "file": "package.json", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "notification-service", "title": "fix: Update outdated dependency common-lib", "body": "Tracking issue to update the vulnerable common-lib dependency.", "labels": ["security", "dependency"]}),
            Action(name="assign_issue", kwargs={"repo_name": "notification-service", "issue_number": 13, "assignees": ["devops-lead"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "notification-service", "branch": "fix/update-common-lib", "message": "fix: Upgrade common-lib to v1.2.4", "author": "devops-lead"}),
            Action(name="open_pull_request", kwargs={"repo_name": "notification-service", "title": "fix(deps): Upgrade common-lib to v1.2.4", "body": "PR to upgrade outdated common-lib dependency to v1.2.4.", "head_branch": "fix/update-common-lib", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "notification-service", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "notification-service", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "notification-service", "issue_number": 13}),
            Action(name="fix_security_alert", kwargs={"repo_name": "notification-service", "alert_number": 10}),
            Action(name="create_release", kwargs={"repo_name": "notification-service", "version": "v0.1.0", "description": "Initial compliant release."}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "notification-service"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_905",
        instruction=(
            "Your mission is to enforce the **Quarterly Performance Initiative Policy** for the 'nlp-models' repository. This policy requires that known performance bottlenecks are formally tracked via a main epic and a specific sub-task for the remediation work. "
            "All code optimizations must be successfully merged via a pull request. You are responsible for executing this process for the known 'High memory usage during training' bottleneck using the provided **Initiative Manifest**. "
            "Your deliverable is the repository's activity dashboard to confirm the policy was successfully executed.\n\n"
            "**Initiative Manifest: Q3 Performance**\n"
            "* **Epic:** {title: 'Q3 Performance Initiative', body: '', assignee: 'tech-lead-tara'}\n"
            "* **Remediation Task:**\n"
            "    * **Issue:** {title: 'Task: High memory usage during training', body: '', assignee: 'ml-engineer'}\n"
            "    * **Implementation:** {branch: 'perf/memory-tuning', author: 'ml-engineer', commit_message: 'perf: Reduce memory footprint via gradient accumulation'}\n"
            "    * **PR:** {title: 'perf: Optimize memory usage', body: ''}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "nlp-models", "title": "Q3 Performance Initiative", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "assignees": ["tech-lead-tara"]}),
            Action(name="create_issue", kwargs={"repo_name": "nlp-models", "title": "Task: High memory usage during training", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "nlp-models", "issue_number": 13, "assignees": ["ml-engineer"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "nlp-models", "branch": "perf/memory-tuning", "message": "perf: Reduce memory footprint via gradient accumulation", "author": "ml-engineer"}),
            Action(name="open_pull_request", kwargs={"repo_name": "nlp-models", "title": "perf: Optimize memory usage", "body": "", "head_branch": "perf/memory-tuning", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "nlp-models", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "nlp-models", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "nlp-models", "issue_number": 13}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "nlp-models"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "nlp-models",
                    "commits_count": 1,
                    "open_issues": 1,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_501",
        instruction=(
            "Your strategic objective is to govern the full lifecycle of a feature deployment and its subsequent emergency rollback on the 'acme-webapp' "
            "repository, ensuring it fully aligns with the company's **Multi-Stage Incident Resolution Policy**. This policy mandates a clear, "
            "auditable trail for both the initial feature release and the corrective actions taken upon discovery of a critical flaw, including the merge of a revert PR. You are "
            "responsible for executing this two-stage process using the provided **Incident Manifest**. Your final deliverable is the repository's "
            "health summary, confirming the final state of the incident.\n\n"
            "**Incident Manifest: Profile Caching Feature**\n"
            "* **Stage 1: Feature Rollout**\n"
            "    * **Issue:** {title: 'Implement User Profile Caching', body: 'Tracks the full lifecycle of the user profile caching feature.', labels: ['feature'], assignee: 'alice-w'}\n"
            "    * **Code:** {branch: 'feature/profile-caching', commit_message: 'feat: Add user profile caching logic', author: 'dev-sue'}\n"
            "    * **PR:** {title: 'Feature: User Profile Caching', body: 'PR to implement the user profile caching feature as per requirements.', reviewers: ['qa-mike']}\n"
            "    * **Release:** {version: 'v1.1.0', description: 'Release with user profile caching.'}\n"
            "    * **Deployment:** {environment: 'production'}\n"
            "* **Stage 2: Emergency Rollback**\n"
            "    * **Alert:** {severity: 'critical', description: 'Post-release discovery: Caching logic exposes sensitive user data.', file: 'src/app.py', branch: 'main'}\n"
            "    * **Issue:** {title: 'EMERGENCY: Rollback v1.1.0 due to critical vulnerability', body: 'Issue to track the emergency rollback of the profile caching feature.', labels: ['security', 'bug'], assignee: 'security-team'}\n"
            "    * **Code:** {branch: 'revert/profile-caching', commit_message: 'revert: Revert user profile caching feature', author: 'security-team'}\n"
            "    * **PR:** {title: 'Revert: User Profile Caching', body: 'Reverting the caching feature due to a critical vulnerability.'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "Implement User Profile Caching", "body": "Tracks the full lifecycle of the user profile caching feature.", "labels": ["feature"]}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12, "assignees": ["alice-w"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "acme-webapp", "branch": "feature/profile-caching", "message": "feat: Add user profile caching logic", "author": "dev-sue"}),
            Action(name="open_pull_request", kwargs={"repo_name": "acme-webapp", "title": "Feature: User Profile Caching", "body": "PR to implement the user profile caching feature as per requirements.", "head_branch": "feature/profile-caching", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "acme-webapp", "pr_number": 10, "reviewers": ["qa-mike"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12}),
            Action(name="create_release", kwargs={"repo_name": "acme-webapp", "version": "v1.1.0", "description": "Release with user profile caching."}),
            Action(name="register_deploy_event", kwargs={"repo_name": "acme-webapp", "environment": "production"}),
            Action(name="create_security_alert", kwargs={"repo_name": "acme-webapp", "severity": "critical", "description": "Post-release discovery: Caching logic exposes sensitive user data.", "file": "src/app.py", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "EMERGENCY: Rollback v1.1.0 due to critical vulnerability", "body": "Issue to track the emergency rollback of the profile caching feature.", "labels": ["security", "bug"]}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 13, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "acme-webapp", "branch": "revert/profile-caching", "message": "revert: Revert user profile caching feature", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "acme-webapp", "title": "Revert: User Profile Caching", "body": "Reverting the caching feature due to a critical vulnerability.", "head_branch": "revert/profile-caching", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 11, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 13}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "acme-webapp"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_203",
        instruction=(
            "As a member of the security team, your objective is to execute the company's **Vulnerability Triage and Full Remediation Cycle Policy** "
            "for the 'security-scanner' repository. The policy requires that high-priority vulnerabilities are formally tracked as issues, and that the most "
            "critical vulnerabilities are fully remediated via a reviewed and merged pull request. You are responsible for executing this process for the "
            "vulnerabilities detailed in the provided **Triage Manifest**. Your final deliverable is the repository's "
            "activity dashboard to confirm the policy has been successfully executed.\n\n"
            "**Triage Manifest:**\n"
            "* **Vulnerability 1 (Critical):**\n"
            "    * **Action:** Remediate\n"
            "    * **Details:** Unsafe Deserialization\n"
            "    * **Issue:** {title: 'Remediate Critical: Unsafe Deserialization', body: 'Tracking issue for the unsafe deserialization vulnerability.', labels: ['security', 'critical-risk'], assignee: 'security-team'}\n"
            "    * **Code:** {branch: 'hotfix/critical-deserialization', base_branch: 'main', commits: [{message: 'fix: Initial patch for unsafe deserialization', author: 'security-team'}, {message: 'test: Add unit tests for deserialization fix', author: 'qa-erin'}, {message: 'docs: Update security docs regarding deserialization', author: 'docs-amy'}]}\n"
            "    * **PR:** {title: 'Fix: Unsafe Deserialization', body: 'Complete fix for the critical deserialization vulnerability.', reviewers: ['tech-lead-tara']}\n"
            "* **Vulnerability 2 (High):**\n"
            "    * **Action:** Track\n"
            "    * **Details:** Buffer Overflow\n"
            "    * **Issue:** {title: 'Remediate High: Buffer Overflow', body: 'Tracking issue for the potential buffer overflow vulnerability.', labels: ['security', 'high-risk'], assignee: 'perf-joe'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Remediate Critical: Unsafe Deserialization", "body": "Tracking issue for the unsafe deserialization vulnerability.", "labels": ["security", "critical-risk"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["security-team"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Remediate High: Buffer Overflow", "body": "Tracking issue for the potential buffer overflow vulnerability.", "labels": ["security", "high-risk"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["perf-joe"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "hotfix/critical-deserialization", "message": "fix: Initial patch for unsafe deserialization", "author": "security-team"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "hotfix/critical-deserialization", "message": "test: Add unit tests for deserialization fix", "author": "qa-erin"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "hotfix/critical-deserialization", "message": "docs: Update security docs regarding deserialization", "author": "docs-amy"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "Fix: Unsafe Deserialization", "body": "Complete fix for the critical deserialization vulnerability.", "head_branch": "hotfix/critical-deserialization", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "security-scanner",
                    "commits_count": 3,
                    "open_issues": 1,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_1001",
        instruction=(
            "Your mission is to execute the **Cross-Team Security Collaboration Policy** in response to a critical vulnerability. This policy requires a coordinated response: the vulnerability must be remediated in the affected repository ('k8s-monitoring'), and a preventative detection rule must be simultaneously added to the 'security-scanner'. "
            "All work must be formally tracked and result in patched or upgraded states for both repositories. You must use the provided **Collaboration Manifest** to orchestrate this process. "
            "Your final deliverable is a set of activity dashboards for both repositories to certify that the policy was successfully executed.\n\n"
            "**Collaboration Manifest:**\n"
            "* **Vulnerability:** {description: 'Insecure Grafana dashboard permissions', file: 'kubernetes/grafana.yaml', severity: 'critical', branch: 'main'}\n"
            "* **Remediation Work (`k8s-monitoring`):**\n"
            "    * **Issue:** {title: 'Remediate insecure Grafana dashboard permissions', body: '', assignee: 'devops-lead'}\n"
            "    * **Code:** {branch: 'fix/grafana-perms', commit_message: 'fix: Restrict Grafana dashboard access', author: 'devops-lead'}\n"
            "    * **PR:** {title: 'fix: Harden Grafana permissions', body: '', reviewers: ['security-team']}\n"
            "* **Prevention Work (`security-scanner`):**\n"
            "    * **Issue:** {title: 'Add detection for insecure Grafana permissions', body: '', assignee: 'security-team'}\n"
            "    * **Code:** {branch: 'feature/grafana-rule', commit_message: 'feat: Add Grafana permission scanner rule', author: 'security-team'}\n"
            "    * **PR:** {title: 'feat: Add Grafana permission rule', body: ''}\n"
            "    * **Release:** {version: 'v0.8.0', description: 'Adds new Grafana security rule.'}"
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "k8s-monitoring", "severity": "critical", "description": "Insecure Grafana dashboard permissions", "file": "kubernetes/grafana.yaml", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "k8s-monitoring", "title": "Remediate insecure Grafana dashboard permissions", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 12, "assignees": ["devops-lead"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Add detection for insecure Grafana permissions", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "feature/grafana-rule", "message": "feat: Add Grafana permission scanner rule", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "feat: Add Grafana permission rule", "body": "", "head_branch": "feature/grafana-rule", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13}),
            Action(name="create_release", kwargs={"repo_name": "security-scanner", "version": "v0.8.0", "description": "Adds new Grafana security rule."}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "k8s-monitoring", "branch": "fix/grafana-perms", "message": "fix: Restrict Grafana dashboard access", "author": "devops-lead"}),
            Action(name="open_pull_request", kwargs={"repo_name": "k8s-monitoring", "title": "fix: Harden Grafana permissions", "body": "", "head_branch": "fix/grafana-perms", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "k8s-monitoring", "pr_number": 11, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "k8s-monitoring", "pr_number": 11, "reviewers": ["security-team"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "k8s-monitoring", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 12}),
            Action(name="fix_security_alert", kwargs={"repo_name": "k8s-monitoring", "alert_number": 10}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "k8s-monitoring",
                    "commits_count": 1,
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
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
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_7004",
        instruction=(
            "Your mission is to execute the **Cross-Repository Dependency Patching Policy**. A regression in 'utils-js' is affecting 'acme-webapp'. "
            "The policy requires a coordinated fix, starting with the upstream dependency, followed by an update in the downstream consumer. "
            "You must use the provided **Patching Manifest** to bring both repositories into a compliant, resolved state. "
            "Your final deliverable is a set of cross-entity reports for both repositories to validate the complete resolution.\n\n"
            "**Patching Manifest:**\n"
            "* **`utils-js` (Upstream Fix):**\n"
            "    * **Issue:** {title: 'Regression: Negative currency formatting', body: 'The previous fix was insufficient and a regression has been reported.', labels: ['bug', 'regression'], assignee: 'bob-dev'}\n"
            "    * **Code:** {branch: 'fix/currency-regression-1.0.3', commit_message: 'fix: Add robust handling for negative currency values', author: 'bob-dev'}\n"
            "    * **PR:** {title: 'Fix: Regression on Negative Currency Formatting', body: 'This PR provides a more robust fix for the regression.'}\n"
            "    * **Release:** {version: 'v1.0.3', description: 'Robust fix for currency formatting regression.'}\n"
            "* **`acme-webapp` (Downstream Update):**\n"
            "    * **Issue:** {title: 'Upstream Bug: Data Corruption from utils-js', body: 'Tracking downstream impact of the regression in utils-js.', labels: ['bug', 'dependency'], assignee: 'alice-w'}\n"
            "    * **Code:** {branch: 'chore/update-utils-js-1.0.3', commit_message: 'Chore: Update utils-js to v1.0.3', author: 'alice-w'}\n"
            "    * **PR:** {title: 'Chore: Update utils-js to v1.0.3', body: 'Integrating upstream fix to resolve data corruption.'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "Upstream Bug: Data Corruption from utils-js", "body": "Tracking downstream impact of the regression in utils-js.", "labels": ["bug", "dependency"]}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12, "assignees": ["alice-w"]}),
            Action(name="create_issue", kwargs={"repo_name": "utils-js", "title": "Regression: Negative currency formatting", "body": "The previous fix was insufficient and a regression has been reported.", "labels": ["bug", "regression"]}),
            Action(name="assign_issue", kwargs={"repo_name": "utils-js", "issue_number": 13, "assignees": ["bob-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "utils-js", "branch": "fix/currency-regression-1.0.3", "message": "fix: Add robust handling for negative currency values", "author": "bob-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "utils-js", "title": "Fix: Regression on Negative Currency Formatting", "head_branch": "fix/currency-regression-1.0.3", "base_branch": "master", "body": "This PR provides a more robust fix for the regression."}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "utils-js", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "utils-js", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "utils-js", "issue_number": 13}),
            Action(name="create_release", kwargs={"repo_name": "utils-js", "version": "v1.0.3", "description": "Robust fix for currency formatting regression."}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "acme-webapp", "branch": "chore/update-utils-js-1.0.3", "message": "Chore: Update utils-js to v1.0.3", "author": "alice-w"}),
            Action(name="open_pull_request", kwargs={"repo_name": "acme-webapp", "title": "Chore: Update utils-js to v1.0.3", "head_branch": "chore/update-utils-js-1.0.3", "base_branch": "main", "body": "Integrating upstream fix to resolve data corruption."}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 11, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12}),
            Action(name="get_cross_entity_report", kwargs={"repo_name": "acme-webapp"}),
            Action(name="get_cross_entity_report", kwargs={"repo_name": "utils-js"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "acme-webapp", "open_issues": 0, "merged_prs": 1, "recent_commits": 1, "open_alerts": 0, "last_deployment": "none", "report_date": "2025-08-26"
                }
            },
            {
                "status": "ok",
                "data": {
                    "repo": "utils-js", "open_issues": 0, "merged_prs": 1, "recent_commits": 1, "open_alerts": 0, "last_deployment": "none", "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_4004",
        instruction=(
            "Your mission is to execute the **Post-Incident Analysis Policy** for the 'security-scanner' repository. "
            "The policy requires a full and auditable resolution for security incidents, where multiple related alerts are consolidated and tracked via a single issue and resolved with a single pull request. "
            "You are responsible for executing this process using the provided **Incident Manifest**. "
            "Your final deliverable is a report of all resolved security alerts in the repository to certify that the process was followed.\n\n"
            "**Incident Manifest:**\n"
            "* **Alerts to Remediate:** [\n"
            "    {severity: 'high', description: 'Insecure dependency in Cargo.toml', file: 'Cargo.toml', branch: 'main'},\n"
            "    {severity: 'low', description: 'Unused variable in scanner.rs', file: 'src/scanner.rs', branch: 'main'}\n"
            "]\n"
            "* **Consolidated Tracking Issue:** {title: 'Security: Remediate multiple alerts', body: '', assignee: 'security-team'}\n"
            "* **Consolidated Fix:**\n"
            "    * **Branch:** 'fix/multi-alert-remediation'\n"
            "    * **Commit:** {message: 'fix: Update dependency and remove unused variable', author: 'security-team'}\n"
            "    * **PR:** {title: 'fix: Remediate multiple alerts', body: ''}"
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "security-scanner", "severity": "high", "description": "Insecure dependency in Cargo.toml", "file": "Cargo.toml", "branch": "main"}),
            Action(name="create_security_alert", kwargs={"repo_name": "security-scanner", "severity": "low", "description": "Unused variable in scanner.rs", "file": "src/scanner.rs", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Security: Remediate multiple alerts", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "fix/multi-alert-remediation", "message": "fix: Update dependency and remove unused variable", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "fix: Remediate multiple alerts", "body": "", "head_branch": "fix/multi-alert-remediation", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12}),
            Action(name="fix_security_alert", kwargs={"repo_name": "security-scanner", "alert_number": 10}),
            Action(name="fix_security_alert", kwargs={"repo_name": "security-scanner", "alert_number": 11}),
            Action(name="get_resolved_security_alerts", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_804",
        instruction=(
            "Your primary strategic objective is to execute the **Quarterly Tech Debt Initiative Policy** for the 'security-scanner' repository. "
            "This policy mandates that a central epic tracks all planned refactoring work for the quarter, and each tech debt item is implemented and merged sequentially through its own tracked issue and pull request. "
            "You are responsible for ensuring the repository's state reflects the completion of this process, using the provided **Tech Debt Manifest**. "
            "Your final deliverable is the repository's activity dashboard to confirm all tech debt items for the quarter have been resolved.\n\n"
            "**Tech Debt Manifest (Q3):**\n"
            "* **Main Epic:** {title: 'Q3 Tech Debt Paydown', body: 'Main epic to track all Q3 tech debt sub-tasks.', labels: ['tech-debt', 'epic'], assignee: 'tech-lead-tara'}\n"
            "* **Work Items:** [\n"
            "    {\n"
            "        name: 'Refactor Parser',\n"
            "        issue: {title: 'Refactor Parser Module', body: 'Sub-task to track the refactoring of the parser module.', labels: ['tech-debt', 'refactor'], assignee: 'security-team'},\n"
            "        code: {branch: 'refactor/parser', commit_message: 'refactor: Simplify parser logic', author: 'security-team'},\n"
            "        pr: {title: 'refactor: Parser Module', body: 'PR to implement the parser refactor.', reviewers: ['tech-lead-tara']}\n"
            "    },\n"
            "    {\n"
            "        name: 'Update Dependencies',\n"
            "        issue: {title: 'Update Deprecated Dependencies', body: 'Sub-task to track the update of deprecated dependencies.', labels: ['tech-debt', 'chore'], assignee: 'security-team'},\n"
            "        code: {branch: 'chore/update-deps', commit_message: 'chore: Update all dependencies to latest stable', author: 'security-team'},\n"
            "        pr: {title: 'chore: Update Dependencies', body: 'PR to update all dependencies to their latest stable versions.', reviewers: ['tech-lead-tara']}\n"
            "    },\n"
            "    {\n"
            "        name: 'Remove Handlers',\n"
            "        issue: {title: 'Remove Deprecated Handlers', body: 'Sub-task to track the removal of deprecated v1 handlers.', labels: ['tech-debt', 'refactor'], assignee: 'security-team'},\n"
            "        code: {branch: 'refactor/remove-handlers', commit_message: 'refactor: Remove unused v1 handlers', author: 'security-team'},\n"
            "        pr: {title: 'refactor: Remove Deprecated Handlers', body: 'PR to remove the unused v1 handlers.', reviewers: ['tech-lead-tara']}\n"
            "    }\n"
            "]"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Q3 Tech Debt Paydown", "body": "Main epic to track all Q3 tech debt sub-tasks.", "labels": ["tech-debt", "epic"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["tech-lead-tara"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Refactor Parser Module", "body": "Sub-task to track the refactoring of the parser module.", "labels": ["tech-debt", "refactor"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "refactor/parser", "message": "refactor: Simplify parser logic", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "refactor: Parser Module", "body": "PR to implement the parser refactor.", "head_branch": "refactor/parser", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 13}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Update Deprecated Dependencies", "body": "Sub-task to track the update of deprecated dependencies.", "labels": ["tech-debt", "chore"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 14, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "chore/update-deps", "message": "chore: Update all dependencies to latest stable", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "chore: Update Dependencies", "body": "PR to update all dependencies to their latest stable versions.", "head_branch": "chore/update-deps", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 11, "issue_number": 14}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 11, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 14}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Remove Deprecated Handlers", "body": "Sub-task to track the removal of deprecated v1 handlers.", "labels": ["tech-debt", "refactor"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 15, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "refactor/remove-handlers", "message": "refactor: Remove unused v1 handlers", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "refactor: Remove Deprecated Handlers", "body": "PR to remove the unused v1 handlers.", "head_branch": "refactor/remove-handlers", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 12, "issue_number": 15}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 12, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 12}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 15}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "security-scanner",
                    "commits_count": 3,
                    "open_issues": 1,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_704",
        instruction=(
            "Your primary strategic objective is to govern the response to a zero-day incident in the 'security-scanner' repository, ensuring it "
            "fully aligns with the company's **Zero-Day Vulnerability Response Protocol**. This high-urgency protocol mandates a clear and auditable "
            "trail for both the emergency patch and the required public communication. You are responsible for executing this process using the provided **Zero-Day Manifest**. "
            "Your final deliverable is the repository health summary, which will serve as the official record of policy compliance.\n\n"
            "**Zero-Day Manifest: YAML Parser RCE**\n"
            "* **Incident Alert:** {severity: 'critical', description: 'Zero-Day RCE Vulnerability in YAML Parser', file: 'src/parser.rs', branch: 'main'}\n"
            "* **Main Tracking Epic:** {title: 'INCIDENT: Zero-Day RCE in YAML Parser', body: 'Main epic to track the zero-day incident response and remediation.', labels: ['security', 'incident', 'epic'], assignee: 'security-team'}\n"
            "* **Workstreams:** [\n"
            "    {\n"
            "        name: 'Patch Development',\n"
            "        issue: {title: 'ACTION: Develop Patch for Zero-Day RCE', body: 'Sub-task to develop the emergency patch for the YAML RCE.', labels: ['security', 'bug'], assignee: 'security-team'},\n"
            "        code: {branch: 'hotfix/zero-day-rce', commit_message: 'fix: Add validation to YAML parser to prevent RCE', author: 'security-team'},\n"
            "        pr: {title: 'fix: Patch for Zero-Day RCE', body: 'Emergency patch for the YAML parser RCE vulnerability.'}\n"
            "    },\n"
            "    {\n"
            "        name: 'Public Communication',\n"
            "        issue: {title: 'ACTION: Write Security Advisory for Zero-Day', body: 'Sub-task to write and publish the official security advisory for the YAML RCE.', labels: ['security', 'documentation'], assignee: 'docs-amy'},\n"
            "        code: {branch: 'docs/zero-day-advisory', commit_message: 'docs: Add security advisory for YAML RCE', author: 'docs-amy'},\n"
            "        pr: {title: 'docs: Publish Security Advisory for Zero-Day', body: 'PR containing the new security advisory document.'}\n"
            "    }\n"
            "]"
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "security-scanner", "severity": "critical", "description": "Zero-Day RCE Vulnerability in YAML Parser", "file": "src/parser.rs", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "INCIDENT: Zero-Day RCE in YAML Parser", "body": "Main epic to track the zero-day incident response and remediation.", "labels": ["security", "incident", "epic"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["security-team"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "ACTION: Write Security Advisory for Zero-Day", "body": "Sub-task to write and publish the official security advisory for the YAML RCE.", "labels": ["security", "documentation"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["docs-amy"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "ACTION: Develop Patch for Zero-Day RCE", "body": "Sub-task to develop the emergency patch for the YAML RCE.", "labels": ["security", "bug"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 14, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "hotfix/zero-day-rce", "message": "fix: Add validation to YAML parser to prevent RCE", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "fix: Patch for Zero-Day RCE", "body": "Emergency patch for the YAML parser RCE vulnerability.", "head_branch": "hotfix/zero-day-rce", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 14}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 14}),
            Action(name="fix_security_alert", kwargs={"repo_name": "security-scanner", "alert_number": 10}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "docs/zero-day-advisory", "message": "docs: Add security advisory for YAML RCE", "author": "docs-amy"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "docs: Publish Security Advisory for Zero-Day", "body": "PR containing the new security advisory document.", "head_branch": "docs/zero-day-advisory", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 11, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_20004",
        instruction=(
            "Your mission is to execute the **New Project Bootstrap Policy** for the 'user-preferences-api'. This policy ensures all new projects are created with a consistent set of initial artifacts for tracking, security, and deployment readiness. You must use the provided **Bootstrap Manifest** to create all required entities. Your final deliverable is a list of open issues to confirm that the initial setup tasks are correctly logged.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that the repository was created as 'private'. It must contain an initial commit and two 'open' issues for initial setup tasks.\n\n"
            "**Bootstrap Manifest:**\n"
            "* **Repository:** {name: 'user-preferences-api', description: 'Service for managing user preferences and settings.', private: True}\n"
            "* **Initial Commit:** {author: 'devops-lead', message: 'Initial commit from service template'}\n"
            "* **Issue 1:** {title: 'Setup CI/CD pipeline', body: 'Configure the standard CI/CD pipeline for the new service.', labels: ['setup', 'ci-cd'], assignee: 'devops-lead'}\n"
            "* **Issue 2:** {title: 'Add basic authentication endpoints', body: 'Implement initial authentication endpoints as per the security spec.', labels: ['feature', 'auth'], assignee: 'backend-core'}"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "user-preferences-api", "description": "Service for managing user preferences and settings.", "private": True}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "user-preferences-api", "branch": "main", "message": "Initial commit from service template", "author": "devops-lead"}),
            Action(name="create_issue", kwargs={"repo_name": "user-preferences-api", "title": "Setup CI/CD pipeline", "body": "Configure the standard CI/CD pipeline for the new service.", "labels": ["setup", "ci-cd"]}),
            Action(name="assign_issue", kwargs={"repo_name": "user-preferences-api", "issue_number": 12, "assignees": ["devops-lead"]}),
            Action(name="create_issue", kwargs={"repo_name": "user-preferences-api", "title": "Add basic authentication endpoints", "body": "Implement initial authentication endpoints as per the security spec.", "labels": ["feature", "auth"]}),
            Action(name="assign_issue", kwargs={"repo_name": "user-preferences-api", "issue_number": 13, "assignees": ["backend-core"]}),
            Action(name="get_open_issues", kwargs={"repo_name": "user-preferences-api"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": [
                    {
                        "issue_id": "ISSUE_user-preferences-api_3ded9583",
                        "title": "Setup CI/CD pipeline",
                        "state": "open",
                        "assignees": ["devops-lead"],
                        "labels": ["setup", "ci-cd"],
                        "created_at": "2025-08-26",
                        "report_date": "2025-08-26"
                    },
                    {
                        "issue_id": "ISSUE_user-preferences-api_537cd6a9",
                        "title": "Add basic authentication endpoints",
                        "state": "open",
                        "assignees": ["backend-core"],
                        "labels": ["feature", "auth"],
                        "created_at": "2025-08-26",
                        "report_date": "2025-08-26"
                    }
                ]
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_7005",
        instruction=(
            "Your objective is to execute the **Ecosystem Health Audit Policy**. This policy requires analyzing key repositories and centralizing the findings in a new, dedicated repository. "
            "You must use the provided **Audit Manifest** to ensure the repository's final state is compliant. "
            "Your final deliverable is an end-to-end report for the new repository to validate its creation and content.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a new private repository, 'Ecosystem-Audit-Logs', has been created and populated. "
            "This repository must contain an initial setup commit and three 'open' issues, one for each audited repository. "
            "Each issue must be correctly assigned and contain the synthesized results of a risk and issue-aging analysis.\n\n"
            "**Audit Manifest:**\n"
            "* **New Repository:** {name: 'Ecosystem-Audit-Logs', description: 'Centralized repository for tracking automated ecosystem health audits.'}\n"
            "* **Initial Commit:** {author: 'devops-lead', message: 'Initial setup for automated health reporting and audit tracking.'}\n"
            "* **Audit Findings:** [\n"
            "    {repo_to_audit: 'security-scanner', issue: {title: 'Audit: security-scanner', body: 'Analysis results: Risk Score=0, Aging Issues=0.', labels: ['audit', 'security'], assignee: 'security-team'}},\n"
            "    {repo_to_audit: 'k8s-monitoring', issue: {title: 'Audit: k8s-monitoring', body: 'Analysis results: Risk Score=0, Aging Issues=0.', labels: ['audit', 'infra'], assignee: 'devops-lead'}},\n"
            "    {repo_to_audit: 'nlp-models', issue: {title: 'Audit: nlp-models', body: 'Analysis results: Risk Score=0, Aging Issues=0.', labels: ['audit', 'mlops'], assignee: 'data-scientist'}}\n"
            "]"
        ),
        actions=[
            Action(name="get_repository_risk_score", kwargs={"repo_name": "security-scanner"}),
            Action(name="get_issue_aging_report", kwargs={"repo_name": "security-scanner"}),
            Action(name="get_repository_risk_score", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="get_issue_aging_report", kwargs={"repo_name": "k8s-monitoring"}),
            Action(name="get_repository_risk_score", kwargs={"repo_name": "nlp-models"}),
            Action(name="get_issue_aging_report", kwargs={"repo_name": "nlp-models"}),
            Action(name="create_repository", kwargs={"repo_name": "Ecosystem-Audit-Logs", "private": True, "description": "Centralized repository for tracking automated ecosystem health audits."}),
            Action(name="create_issue", kwargs={"repo_name": "Ecosystem-Audit-Logs", "title": "Audit: security-scanner", "body": "Analysis results: Risk Score=0, Aging Issues=0.", "labels": ["audit", "security"]}),
            Action(name="assign_issue", kwargs={"repo_name": "Ecosystem-Audit-Logs", "issue_number": 12, "assignees": ["security-team"]}),
            Action(name="create_issue", kwargs={"repo_name": "Ecosystem-Audit-Logs", "title": "Audit: k8s-monitoring", "body": "Analysis results: Risk Score=0, Aging Issues=0.", "labels": ["audit", "infra"]}),
            Action(name="assign_issue", kwargs={"repo_name": "Ecosystem-Audit-Logs", "issue_number": 13, "assignees": ["devops-lead"]}),
            Action(name="create_issue", kwargs={"repo_name": "Ecosystem-Audit-Logs", "title": "Audit: nlp-models", "body": "Analysis results: Risk Score=0, Aging Issues=0.", "labels": ["audit", "mlops"]}),
            Action(name="assign_issue", kwargs={"repo_name": "Ecosystem-Audit-Logs", "issue_number": 14, "assignees": ["data-scientist"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "Ecosystem-Audit-Logs", "branch": "main", "message": "Initial setup for automated health reporting and audit tracking.", "author": "devops-lead"}),
            Action(name="generate_end_to_end_report", kwargs={"repo_name": "Ecosystem-Audit-Logs"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_5003",
        instruction=(
            "Your mission is to execute the **Alert Triage Policy** for the 'acme-webapp' repository. A new low-severity alert is suspected to be a false positive. "
            "The policy for handling such cases requires a formal investigation and dismissal process, where the investigation is tracked, a code comment is added via pull request to suppress the warning, and the original alert is resolved. "
            "You must use the provided **Data Specification** to create all required artifacts. Your final deliverable is a report of all resolved security alerts in the repository to audit the triage decision.\n\n"
            "**Data Specification:**\n"
            "* **Alert Details:** {description: 'Hardcoded timeout value', file: 'src/config.py', severity: 'low'}\n"
            "* **Tracking Issue:** {title: 'Investigate hardcoded timeout alert - False Positive', body: '', assignee: 'alice-w'}\n"
            "* **Code Artifacts:** {branch: 'chore/suppress-linter-warning', commit_message: 'chore: Suppress linter warning for timeout value', pr_title: 'chore: Suppress timeout warning', pr_body: '', author: 'alice-w'}"
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "acme-webapp", "severity": "low", "description": "Hardcoded timeout value", "file": "src/config.py", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "Investigate hardcoded timeout alert - False Positive", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12, "assignees": ["alice-w"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "acme-webapp", "branch": "chore/suppress-linter-warning", "message": "chore: Suppress linter warning for timeout value", "author": "alice-w"}),
            Action(name="open_pull_request", kwargs={"repo_name": "acme-webapp", "title": "chore: Suppress timeout warning", "body": "", "head_branch": "chore/suppress-linter-warning", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12}),
            Action(name="fix_security_alert", kwargs={"repo_name": "acme-webapp", "alert_number": 10}),
            Action(name="get_resolved_security_alerts", kwargs={"repo_name": "acme-webapp"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_3004",
        instruction=(
            "Your mission is to execute the **New Team Member Onboarding Policy** for the 'ui-kit' repository. This policy ensures new developers, like 'intern-sarah', complete a standard introductory task by resolving a tracked issue via a reviewed pull request to familiarize themselves with the contribution workflow. "
            "You must use the provided **Onboarding Manifest** to create all required artifacts. "
            "Your final deliverable is the repository's activity dashboard to certify the successful completion of the onboarding task.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a 'good first issue' was created and assigned to the new team member, and this issue must be 'closed'. "
            "The work must be implemented on a feature branch and 'merged' via a pull request that has been successfully reviewed.\n\n"
            "**Onboarding Manifest:**\n"
            "* **Issue:** {title: 'Good First Issue: Add accessibility labels to Button component', body: ''}\n"
            "* **New Team Member (Assignee/Author):** 'intern-sarah'\n"
            "* **Reviewer:** 'design-lead'\n"
            "* **Code Artifacts:** {branch: 'feature/aria-labels', commit_message: 'feat: Add ARIA labels to Button component', pr_title: 'feat: Add accessibility labels', pr_body: ''}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Good First Issue: Add accessibility labels to Button component", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12, "assignees": ["intern-sarah"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/aria-labels", "message": "feat: Add ARIA labels to Button component", "author": "intern-sarah"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "feat: Add accessibility labels", "body": "", "head_branch": "feature/aria-labels", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "ui-kit", "pr_number": 10, "reviewers": ["design-lead"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "ui-kit"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "ui-kit",
                    "commits_count": 1,
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_603",
        instruction=(
            "Your primary strategic objective is to govern the lifecycle of a new feature for the 'ui-kit' repository, ensuring it fully complies "
            "with the company's **Experiment-Driven Development Policy**. This policy requires that new user-facing features are developed behind "
            "a feature flag and that a separate issue tracks the experiment's analysis. You are responsible for bringing the repository to a state "
            "that conforms to the policy, using the provided manifest for the 'New Checkout Button' feature. Your final deliverable is the repository's activity dashboard, "
            "confirming the feature is released and the experiment is ready for analysis.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that the development issue is 'closed' and the code is 'merged' via a pull request containing all necessary commits. The separate issue for analyzing the A/B test must be 'open'. A new release must be published and deployed to production.\n\n"
            "**Experiment Manifest: New Checkout Button**\n"
            "* **Development Task:** {issue_title: 'Develop New Checkout Button', issue_body: 'Main tracking issue for the development of the new checkout button.', labels: ['feature', 'ui', 'epic'], assignee: 'ui-dev'}\n"
            "* **Analysis Task:** {issue_title: 'Analyze A/B Test Results for New Checkout Button', issue_body: 'Issue to track the analysis of the A/B test results.', labels: ['analytics', 'research'], assignee: 'data-scientist'}\n"
            "* **Implementation:**\n"
            "    * **Branch:** 'feature/checkout-button'\n"
            "    * **Commits:** [{message: 'feat: Implement new checkout button UI', author: 'ui-dev'}, {message: 'feat: Add feature flag for A/B testing checkout button', author: 'ui-dev'}, {message: 'test: Add unit tests for new button and feature flag', author: 'qa-erin'}]\n"
            "* **Pull Request:** {title: 'Feature: New Checkout Button with A/B Test Flag', body: 'PR to release the new checkout button behind a feature flag for A/B testing.', reviewers: ['tech-lead-tara']}\n"
            "* **Release:** {version: 'v3.4.0', description: 'New Checkout Button with A/B Test'}\n"
            "* **Deployment:** {environment: 'production'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Develop New Checkout Button", "body": "Main tracking issue for the development of the new checkout button.", "labels": ["feature", "ui", "epic"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12, "assignees": ["ui-dev"]}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Analyze A/B Test Results for New Checkout Button", "body": "Issue to track the analysis of the A/B test results.", "labels": ["analytics", "research"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 13, "assignees": ["data-scientist"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/checkout-button", "message": "feat: Implement new checkout button UI", "author": "ui-dev"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/checkout-button", "message": "feat: Add feature flag for A/B testing checkout button", "author": "ui-dev"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/checkout-button", "message": "test: Add unit tests for new button and feature flag", "author": "qa-erin"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "Feature: New Checkout Button with A/B Test Flag", "body": "PR to release the new checkout button behind a feature flag for A/B testing.", "head_branch": "feature/checkout-button", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 12}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 13}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "ui-kit", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12}),
            Action(name="create_release", kwargs={"repo_name": "ui-kit", "version": "v3.4.0", "description": "New Checkout Button with A/B Test"}),
            Action(name="register_deploy_event", kwargs={"repo_name": "ui-kit", "environment": "production"}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "ui-kit"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "ui-kit",
                    "commits_count": 3,
                    "open_issues": 1,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_605",
        instruction=(
            "Your strategic objective is to execute the **Disaster Recovery Protocol** for the 'ui-kit' repository, which has been declared corrupted. "
            "This policy requires creating a new, clean repository and migrating critical work, leaving a clear audit trail on both repositories. "
            "You are responsible for bringing the ecosystem to a state that matches the official **Recovery Specification** by using the provided manifest. "
            "Your final deliverable is a list containing the health summaries for both the old and new repositories to document the state of the recovery operation.\n\n"
            "**Recovery Manifest:**\n"
            "* **Incident Tracking (`ui-kit`):**\n"
            "    * **Alert:** {description: 'FATAL: Repository index corrupted; read-only mode enabled.', file: '.git/index', severity: 'critical'}\n"
            "    * **Issue:** {title: 'DR: Plan migration to new repository', body: 'Main tracking issue for the disaster recovery plan and migration to ui-kit-recovered.', labels: ['disaster-recovery', 'ops'], assignee: 'devops-lead'}\n"
            "* **New Repository (`ui-kit-recovered`):**\n"
            "    * **Configuration:** {name: 'ui-kit-recovered', description: 'Recovered version of ui-kit.', private: True}\n"
            "    * **Ported Features:** [\n"
            "        {name: 'Theming Engine', issue: {title: '[Port] Re-implement Theming Engine', body: 'Port of theming engine to recovered repo.', labels: ['recovery', 'port'], assignee: 'ui-dev'}, code: {branch: 'feat/port-theming', commit_message: 'feat: Re-implement theming engine', author: 'ui-dev'}, pr: {title: 'feat: Port theming engine', body: 'PR to port the theming engine from the old repository.'}},\n"
            "        {name: 'Button Component', issue: {title: '[Port] Re-implement Button Component', body: 'Port of button component to recovered repo.', labels: ['recovery', 'port'], assignee: 'ui-dev'}, code: {branch: 'feat/port-button', commit_message: 'feat: Re-implement button component', author: 'ui-dev'}, pr: {title: 'feat: Port button component', body: 'PR to port the button component from the old repository.'}}\n"
            "    ]\n"
            "    * **Release:** {version: 'v4.0.0-recovered', description: 'Initial recovered release.', environment: 'production'}"
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "ui-kit", "severity": "critical", "description": "FATAL: Repository index corrupted; read-only mode enabled.", "file": ".git/index", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "DR: Plan migration to new repository", "body": "Main tracking issue for the disaster recovery plan and migration to ui-kit-recovered.", "labels": ["disaster-recovery", "ops"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12, "assignees": ["devops-lead"]}),
            Action(name="create_repository", kwargs={"repo_name": "ui-kit-recovered", "description": "Recovered version of ui-kit.", "private": True}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit-recovered", "title": "[Port] Re-implement Theming Engine", "body": "Port of theming engine to recovered repo.", "labels": ["recovery", "port"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit-recovered", "issue_number": 13, "assignees": ["ui-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit-recovered", "branch": "feat/port-theming", "message": "feat: Re-implement theming engine", "author": "ui-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit-recovered", "title": "feat: Port theming engine", "body": "PR to port the theming engine from the old repository.", "head_branch": "feat/port-theming", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit-recovered", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit-recovered", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit-recovered", "issue_number": 13}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit-recovered", "title": "[Port] Re-implement Button Component", "body": "Port of button component to recovered repo.", "labels": ["recovery", "port"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit-recovered", "issue_number": 14, "assignees": ["ui-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit-recovered", "branch": "feat/port-button", "message": "feat: Re-implement button component", "author": "ui-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit-recovered", "title": "feat: Port button component", "body": "PR to port the button component from the old repository.", "head_branch": "feat/port-button", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit-recovered", "pr_number": 11, "issue_number": 14}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit-recovered", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit-recovered", "issue_number": 14}),
            Action(name="create_release", kwargs={"repo_name": "ui-kit-recovered", "version": "v4.0.0-recovered", "description": "Initial recovered release."}),
            Action(name="register_deploy_event", kwargs={"repo_name": "ui-kit-recovered", "environment": "production"}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "ui-kit"}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "ui-kit-recovered"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_502",
        instruction=(
            "Your role is to govern a cross-repository feature development according to the **Cross-Team API Dependency Protocol**. This protocol "
            "is invoked when a frontend application requires a new backend endpoint. It mandates that the backend API is implemented, released, and then consumed by the frontend application, with all work formally tracked. "
            "You must use the provided **Feature Manifest** to orchestrate this entire lifecycle across both the 'payments-api' (backend) and 'ui-kit' (frontend) repositories. "
            "Your final deliverable is a list containing the activity dashboards for both repositories to confirm the protocol was successfully executed.\n\n"
            "**Feature Manifest:**\n"
            "* **`payments-api` (Backend):**\n"
            "    * **Repository:** {name: 'payments-api', description: 'Handles all payment processing and transaction history.', private: True}\n"
            "    * **Issue:** {title: '[API] Create /v2/payment-history Endpoint', body: 'Issue to track the implementation of the new transaction history endpoint.', labels: ['api', 'feature'], assignee: 'backend-core'}\n"
            "    * **Code:** {branch: 'feature/history-endpoint', commit_message: 'feat: Implement transaction history endpoint', author: 'backend-core'}\n"
            "    * **PR:** {title: 'feat: Add /v2/payment-history endpoint', body: 'This PR adds the new endpoint for retrieving user payment history.'}\n"
            "    * **Release:** {version: 'v2.1.0', description: 'Adds /v2/payment-history endpoint.'}\n"
            "* **`ui-kit` (Frontend):**\n"
            "    * **Issue:** {title: '[UI] Build Payment History Component', body: 'Issue to track the development of the new Payment History component.', labels: ['feature', 'ui'], assignee: 'ui-dev'}\n"
            "    * **Code:** {branch: 'feature/payment-history', commits: [{message: 'feat: Add new Payment History component', author: 'ui-dev'}, {message: 'refactor: Integrate payments-api v2.1.0', author: 'ui-dev'}]}\n"
            "    * **PR:** {title: 'feat: Payment History Component', body: 'This PR adds the new Payment History component that consumes the payments-api.'}"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "payments-api", "description": "Handles all payment processing and transaction history.", "private": True}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "[UI] Build Payment History Component", "body": "Issue to track the development of the new Payment History component.", "labels": ["feature", "ui"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12, "assignees": ["ui-dev"]}),
            Action(name="create_issue", kwargs={"repo_name": "payments-api", "title": "[API] Create /v2/payment-history Endpoint", "body": "Issue to track the implementation of the new transaction history endpoint.", "labels": ["api", "feature"]}),
            Action(name="assign_issue", kwargs={"repo_name": "payments-api", "issue_number": 13, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-api", "branch": "feature/history-endpoint", "message": "feat: Implement transaction history endpoint", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "payments-api", "title": "feat: Add /v2/payment-history endpoint", "body": "This PR adds the new endpoint for retrieving user payment history.", "head_branch": "feature/history-endpoint", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "payments-api", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-api", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "payments-api", "issue_number": 13}),
            Action(name="create_release", kwargs={"repo_name": "payments-api", "version": "v2.1.0", "description": "Adds /v2/payment-history endpoint."}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/payment-history", "message": "feat: Add new Payment History component", "author": "ui-dev"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/payment-history", "message": "refactor: Integrate payments-api v2.1.0", "author": "ui-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "feat: Payment History Component", "body": "This PR adds the new Payment History component that consumes the payments-api.", "head_branch": "feature/payment-history", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 11, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "ui-kit"}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "payments-api"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "ui-kit",
                    "commits_count": 2,
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
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
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_405",
        instruction=(
            "Your primary strategic objective is to govern the post-incident lifecycle for the 'security-scanner' repository, ensuring it fully "
            "aligns with the company's **Incident Post-Mortem Policy**. This policy mandates a clear and auditable process for tracking preventative "
            "actions identified after an incident, with a main epic tracking the entire process and sub-tasks for each action item. "
            "You are responsible for ensuring the repository's state reflects the successful execution of this process, using the provided **Post-Mortem Manifest**. "
            "Your final deliverable is the repository's activity dashboard, which will serve as the official record of policy compliance.\n\n"
            "**Post-Mortem Manifest: Q3 Parser Engine Outage**\n"
            "* **Main Epic:** {title: 'Post-Mortem: Q3 Parser Engine Outage', body: 'Main tracking issue for the post-mortem, to be populated with root cause analysis.', labels: ['post-mortem', 'audit'], assignee: 'tech-lead-tara'}\n"
            "* **Action Items:** [\n"
            "    {\n"
            "        status: 'Completed',\n"
            "        issue: {title: '[Action Item] Add more alerting for parser errors', body: 'Sub-task to add enhanced alerting to detect parser configuration errors pre-deployment.', labels: ['action-item', 'monitoring'], assignee: 'devops-lead'},\n"
            "        code: {branch: 'feature/parser-alerting', commit_message: 'feat: Add enhanced alerting for parser config errors', author: 'devops-lead'},\n"
            "        pr: {title: 'Feature: Enhanced Parser Alerting', body: 'PR to implement enhanced alerting as per post-mortem action item.', reviewers: ['tech-lead-tara']}\n"
            "    },\n"
            "    {\n"
            "        status: 'Open',\n"
            "        issue: {title: '[Action Item] Improve unit test coverage for parser module', body: 'Sub-task to improve unit test coverage to prevent similar regressions.', labels: ['action-item', 'testing'], assignee: 'qa-erin'}\n"
            "    },\n"
            "    {\n"
            "        status: 'Open',\n"
            "        issue: {title: '[Action Item] Refactor parser module for resilience', body: 'Sub-task to refactor the parser to handle malformed configs gracefully.', labels: ['action-item', 'tech-debt'], assignee: 'security-team'}\n"
            "    }\n"
            "]"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Post-Mortem: Q3 Parser Engine Outage", "body": "Main tracking issue for the post-mortem, to be populated with root cause analysis.", "labels": ["post-mortem", "audit"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["tech-lead-tara"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "[Action Item] Add more alerting for parser errors", "body": "Sub-task to add enhanced alerting to detect parser configuration errors pre-deployment.", "labels": ["action-item", "monitoring"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["devops-lead"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "[Action Item] Improve unit test coverage for parser module", "body": "Sub-task to improve unit test coverage to prevent similar regressions.", "labels": ["action-item", "testing"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 14, "assignees": ["qa-erin"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "[Action Item] Refactor parser module for resilience", "body": "Sub-task to refactor the parser to handle malformed configs gracefully.", "labels": ["action-item", "tech-debt"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 15, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "feature/parser-alerting", "message": "feat: Add enhanced alerting for parser config errors", "author": "devops-lead"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "Feature: Enhanced Parser Alerting", "body": "PR to implement enhanced alerting as per post-mortem action item.", "head_branch": "feature/parser-alerting", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 13}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "security-scanner",
                    "commits_count": 1,
                    "open_issues": 3,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_103",
        instruction=(
            "Your mission is to execute the **Quarterly Health and Velocity Audit Policy** for the 'nlp-models' repository. "
            "This policy requires a comprehensive analysis of the repository's development backlog, recent activity, and current security posture. "
            "The findings of the audit must be consolidated into a formal tracking issue to assign ownership for review. "
            "You must use the provided **Audit Manifest** to scope your analysis and create the required tracking artifact. "
            "Your final deliverable is a full repository activity dashboard summarizing the repository's current state post-audit.\n\n"
            "**Audit Manifest: Q3 nlp-models**\n"
            "* **Analysis Scope:**\n"
            "    * **Backlog & Velocity:** Analyze issue aging and pull request merge times.\n"
            "    * **Recent Activity:** Analyze commit activity for November 2023 (2023-11-01T00:00:00Z to 2023-11-30T23:59:59Z).\n"
            "    * **Security Posture:** Analyze open security alerts.\n"
            "* **Tracking Issue:** {title: 'Audit project velocity and backlog', body: 'Generated from audit: review aged issues and PR merge times to identify bottlenecks.', labels: ['audit', 'performance'], assignee: 'data-scientist'}"
        ),
        actions=[
            Action(name="get_issue_aging_report", kwargs={"repo_name": "nlp-models"}),
            Action(name="get_pull_request_merge_time_report", kwargs={"repo_name": "nlp-models"}),
            Action(name="list_commits_by_date_range", kwargs={"repo_name": "nlp-models", "start_date": "2023-11-01T00:00:00Z", "end_date": "2023-11-30T23:59:59Z"}),
            Action(name="get_open_security_alerts", kwargs={"repo_name": "nlp-models"}),
            Action(name="create_issue", kwargs={
                "repo_name": "nlp-models",
                "title": "Audit project velocity and backlog",
                "body": "Generated from audit: review aged issues and PR merge times to identify bottlenecks.",
                "labels": ["audit", "performance"]
            }),
            Action(name="assign_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "assignees": ["data-scientist"]}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "nlp-models"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_40001",
        instruction=(
            "Your mission is to execute the **Staged Rollout Policy** for the 'k8s-monitoring' repository. This policy requires that new features are deployed and verified in a 'staging' environment before a final issue is created to track the production release. You are responsible for bringing the repository to a state that reflects the successful execution of this entire process, as defined by the official **Rollout Specification** below. Your final deliverable is the repository's activity dashboard to confirm the feature is fully verified and ready for production.\n\n"
            "**Rollout Specification: Alertmanager Integration**\n"
            "* **Feature Tracking:** The main feature, tracked by an issue, must be 'closed'.\n"
            "* **Code Implementation:** All work must be consolidated into a single 'merged' pull request.\n"
            "* **Staging Verification:** A deployment to the 'staging' environment must be registered, and a subsequent QA verification issue must be 'closed'.\n"
            "* **Production Readiness:** A final issue to track the production release must be 'open'.\n\n"
            "**Data Manifest:**\n"
            "* **Feature Issue:** {title: 'Implement Alertmanager for notifications', body: 'Main tracking issue for the Alertmanager feature.', labels: ['feature', 'epic'], assignee: 'devops-lead'}\n"
            "* **Code Artifacts:** {branch: 'feature/alertmanager', commit_message: 'feat: Add Alertmanager manifests and config', pr_title: 'feat: Add Alertmanager', pr_body: 'PR to introduce Alertmanager for alert routing.'}\n"
            "* **QA Issue:** {title: 'Staging Verification for Alertmanager', body: 'Tracking issue for QA verification on the staging environment.', labels: ['qa', 'verification'], assignee: 'qa-erin'}\n"
            "* **Production Issue:** {title: 'Schedule Production Release for Alertmanager', body: 'All checks passed. Ready to schedule production deployment.', labels: ['release', 'ops'], assignee: 'release-manager'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "k8s-monitoring", "title": "Implement Alertmanager for notifications", "body": "Main tracking issue for the Alertmanager feature.", "labels": ["feature", "epic"]}),
            Action(name="assign_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 12, "assignees": ["devops-lead"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "k8s-monitoring", "branch": "feature/alertmanager", "message": "feat: Add Alertmanager manifests and config", "author": "devops-lead"}),
            Action(name="open_pull_request", kwargs={"repo_name": "k8s-monitoring", "title": "feat: Add Alertmanager", "body": "PR to introduce Alertmanager for alert routing.", "head_branch": "feature/alertmanager", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "k8s-monitoring", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "k8s-monitoring", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 12}),
            Action(name="register_deploy_event", kwargs={"repo_name": "k8s-monitoring", "environment": "staging"}),
            Action(name="create_issue", kwargs={"repo_name": "k8s-monitoring", "title": "Staging Verification for Alertmanager", "body": "Tracking issue for QA verification on the staging environment.", "labels": ["qa", "verification"]}),
            Action(name="assign_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 13, "assignees": ["qa-erin"]}),
            Action(name="close_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 13}),
            Action(name="create_issue", kwargs={"repo_name": "k8s-monitoring", "title": "Schedule Production Release for Alertmanager", "body": "All checks passed. Ready to schedule production deployment.", "labels": ["release", "ops"]}),
            Action(name="assign_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 14, "assignees": ["release-manager"]}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "k8s-monitoring"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "k8s-monitoring",
                    "commits_count": 1,
                    "open_issues": 1,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_40003",
        instruction=(
            "Your mission is to execute the **Documentation Update Policy** for the 'nlp-models' repository. The policy requires that all documentation changes are formally tracked and implemented via a pull request. "
            "You must use the provided **Doc Manifest** to create and process the required artifacts. "
            "Your final deliverable is a list of commits for the relevant branch to serve as an audit trail of the changes.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a tracking issue for the documentation update was created and is now 'closed', and that the work has been 'merged' via a pull request.\n\n"
            "**Doc Manifest:**\n"
            "* **Issue:** {title: 'Docs: Clarify data preprocessing steps', body: 'The current documentation for data preprocessing is unclear and needs examples.', labels: ['documentation'], assignee: 'data-scientist'}\n"
            "* **Code Artifacts:** {branch: 'docs/preprocessing-guide', commit_message: 'docs: Add detailed examples to preprocessing guide', pr_title: 'Docs: Clarify preprocessing guide', pr_body: 'This PR adds examples to the preprocessing documentation.', author: 'data-scientist'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "nlp-models", "title": "Docs: Clarify data preprocessing steps", "body": "The current documentation for data preprocessing is unclear and needs examples.", "labels": ["documentation"]}),
            Action(name="assign_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "assignees": ["data-scientist"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "nlp-models", "branch": "docs/preprocessing-guide", "message": "docs: Add detailed examples to preprocessing guide", "author": "data-scientist"}),
            Action(name="open_pull_request", kwargs={"repo_name": "nlp-models", "title": "Docs: Clarify preprocessing guide", "body": "This PR adds examples to the preprocessing documentation.", "head_branch": "docs/preprocessing-guide", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "nlp-models", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "nlp-models", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12}),
            Action(name="list_commits_by_branch", kwargs={"repo_name": "nlp-models", "branch": "docs/preprocessing-guide"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": [
                    {
                        "commit_id": "8a7d6f5e4c3b",
                        "repo": "nlp-models",
                        "branch": "docs/preprocessing-guide",
                        "message": "docs: Add detailed examples to preprocessing guide",
                        "author": "data-scientist",
                        "timestamp": "2025-08-26",
                        "report_date": "2025-08-26"
                    }
                ]
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_50001",
        instruction=(
            "Your mission is to execute the **Incident Post-Mortem Policy** for the 'security-scanner' repository. Following a recent production outage, a post-mortem is required to track preventative actions. "
            "The policy requires creating a main epic to track the post-mortem and sub-tasks for each action item. You must use the provided **Post-Mortem Manifest** to create the necessary artifacts. "
            "Your final deliverable is the repository's activity dashboard to show the current state of the post-mortem process.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show a main post-mortem epic issue that remains 'open'. One sub-task for a completed action item must be 'closed', with its corresponding fix 'merged' via a pull request. "
            "Two other sub-tasks for ongoing actions must remain 'open'.\n\n"
            "**Post-Mortem Manifest:**\n"
            "* **Main Epic:** {title: 'Post-Mortem: Q3 Parser Engine Outage', body: 'Main epic to track all action items from the Q3 parser outage.', labels: ['post-mortem', 'epic'], assignee: 'tech-lead-tara'}\n"
            "* **Completed Action Item:**\n"
            "    * **Issue:** {title: 'ACTION: Add more alerting for parser errors', body: 'Sub-task to add enhanced alerting to detect parser configuration errors pre-deployment.', labels: ['action-item', 'monitoring'], assignee: 'devops-lead'}\n"
            "    * **Code:** {branch: 'feature/parser-alerting', commit_message: 'feat: Add enhanced alerting for parser config errors', pr_title: 'Feature: Enhanced Parser Alerting', pr_body: 'PR to implement enhanced alerting as per post-mortem action item.', author: 'devops-lead', reviewers: ['tech-lead-tara']}\n"
            "* **Open Action Items:**\n"
            "    * {title: '[Action Item] Improve unit test coverage for parser module', body: 'Sub-task to improve unit test coverage to prevent similar regressions.', labels: ['action-item', 'testing'], assignee: 'qa-erin'}\n"
            "    * {title: '[Action Item] Refactor parser module for resilience', body: 'Sub-task to refactor the parser to handle malformed configs gracefully.', labels: ['action-item', 'tech-debt'], assignee: 'security-team'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Post-Mortem: Q3 Parser Engine Outage", "body": "Main epic to track all action items from the Q3 parser outage.", "labels": ["post-mortem", "epic"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["tech-lead-tara"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "ACTION: Add more alerting for parser errors", "body": "Sub-task to add enhanced alerting to detect parser configuration errors pre-deployment.", "labels": ["action-item", "monitoring"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["devops-lead"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "[Action Item] Improve unit test coverage for parser module", "body": "Sub-task to improve unit test coverage to prevent similar regressions.", "labels": ["action-item", "testing"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 14, "assignees": ["qa-erin"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "[Action Item] Refactor parser module for resilience", "body": "Sub-task to refactor the parser to handle malformed configs gracefully.", "labels": ["action-item", "tech-debt"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 15, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "feature/parser-alerting", "message": "feat: Add enhanced alerting for parser config errors", "author": "devops-lead"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "Feature: Enhanced Parser Alerting", "body": "PR to implement enhanced alerting as per post-mortem action item.", "head_branch": "feature/parser-alerting", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 13}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "security-scanner",
                    "commits_count": 1,
                    "open_issues": 3,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_50003",
        instruction=(
            "Your mission is to execute the **Multi-Commit Feature Policy** for the 'nlp-models' repository. This policy requires that features with contributions from multiple authors are consolidated into a single pull request for review. "
            "You must use the provided **Feature Manifest** to create all artifacts. "
            "Your final deliverable is a report of commits by author to verify the contributions.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a feature was tracked via a 'closed' issue. The work must be contained in a single 'merged' pull request that includes two commits from different authors and was successfully reviewed.\n\n"
            "**Feature Manifest:**\n"
            "* **Issue:** {title: 'Feature: Add model performance visualization', body: 'Tracking issue for the new performance visualization feature.', labels: ['feature', 'visualization'], assignee: 'data-scientist'}\n"
            "* **Code Artifacts:**\n"
            "    * **Branch:** 'feature/perf-viz'\n"
            "    * **PR:** {title: 'feat: Model Performance Visualization', body: 'Adds new components for model performance visualization.', reviewers: ['tech-lead-tara']}\n"
            "    * **Commits:** [\n"
            "        {message: 'feat: Add data hooks for visualization API', author: 'data-scientist'},\n"
            "        {message: 'feat: Implement chart components for visualization', author: 'ml-engineer'}\n"
            "    ]\n"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "nlp-models", "title": "Feature: Add model performance visualization", "body": "Tracking issue for the new performance visualization feature.", "labels": ["feature", "visualization"]}),
            Action(name="assign_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "assignees": ["data-scientist"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "nlp-models", "branch": "feature/perf-viz", "message": "feat: Add data hooks for visualization API", "author": "data-scientist"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "nlp-models", "branch": "feature/perf-viz", "message": "feat: Implement chart components for visualization", "author": "ml-engineer"}),
            Action(name="open_pull_request", kwargs={"repo_name": "nlp-models", "title": "feat: Model Performance Visualization", "body": "Adds new components for model performance visualization.", "head_branch": "feature/perf-viz", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "nlp-models", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "nlp-models", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "nlp-models", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12}),
            Action(name="count_commits_by_author", kwargs={"repo_name": "nlp-models"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "nlp-models",
                    "commits_by_author": {
                        "data-scientist": 1,
                        "ml-engineer": 1
                    },
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_50004",
        instruction=(
            "Your mission is to execute the **New Service Onboarding and Governance Policy** for the new 'notification-service'. This policy mandates that new services are not only technically bootstrapped but also meet initial governance and security compliance standards before their first release. "
            "You are responsible for ensuring the repository's state fully aligns with the **Onboarding Compliance Specification**. "
            "Your final deliverable is the repository's health summary to confirm its compliant state.\n\n"
            "**Onboarding Compliance Specification:**\n"
            "The final state must show that the repository was created and contains governance documentation. An operational readiness issue ('Configure main branch protection rules') must be 'closed'. "
            "A known vulnerability from the base template must be remediated, which requires a 'medium' severity alert to be 'fixed' and its corresponding tracking issue to be 'closed' after its fix is 'merged' via a pull request. "
            "Finally, an initial compliant release must be published.\n\n"
            "**Data Manifest:**\n"
            "* **Repository:** {name: 'notification-service', description: 'Centralized service for handling user notifications.', private: True}\n"
            "* **Governance:**\n"
            "    * **Commits:** [{message: 'docs: Add MIT License', author: 'docs-amy'}, {message: 'docs: Add SECURITY.md policy', author: 'docs-amy'}]\n"
            "    * **Ops Issue:** {title: 'ops: Configure main branch protection rules', body: 'Tracking issue for branch protection setup as per governance policy.', labels: ['ops', 'governance'], assignee: 'devops-lead'}\n"
            "* **Security Remediation:**\n"
            "    * **Alert:** {severity: 'medium', description: 'Default template includes outdated dependency: common-lib v1.2.3', file: 'package.json'}\n"
            "    * **Issue:** {title: 'fix: Update outdated dependency common-lib', body: 'Tracking issue to update the vulnerable common-lib dependency.', labels: ['security', 'dependency'], assignee: 'devops-lead'}\n"
            "    * **Code:** {branch: 'fix/update-common-lib', commit_message: 'fix: Upgrade common-lib to v1.2.4', pr_title: 'fix(deps): Upgrade common-lib to v1.2.4', pr_body: 'PR to upgrade outdated common-lib dependency to v1.2.4.', author: 'devops-lead'}\n"
            "* **Release:** {version: 'v0.1.0', description: 'Initial compliant release.'}"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "notification-service", "description": "Centralized service for handling user notifications.", "private": True}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "notification-service", "branch": "main", "message": "docs: Add MIT License", "author": "docs-amy"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "notification-service", "branch": "main", "message": "docs: Add SECURITY.md policy", "author": "docs-amy"}),
            Action(name="create_issue", kwargs={"repo_name": "notification-service", "title": "ops: Configure main branch protection rules", "body": "Tracking issue for branch protection setup as per governance policy.", "labels": ["ops", "governance"]}),
            Action(name="assign_issue", kwargs={"repo_name": "notification-service", "issue_number": 12, "assignees": ["devops-lead"]}),
            Action(name="close_issue", kwargs={"repo_name": "notification-service", "issue_number": 12}),
            Action(name="create_security_alert", kwargs={"repo_name": "notification-service", "severity": "medium", "description": "Default template includes outdated dependency: common-lib v1.2.3", "file": "package.json", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "notification-service", "title": "fix: Update outdated dependency common-lib", "body": "Tracking issue to update the vulnerable common-lib dependency.", "labels": ["security", "dependency"]}),
            Action(name="assign_issue", kwargs={"repo_name": "notification-service", "issue_number": 13, "assignees": ["devops-lead"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "notification-service", "branch": "fix/update-common-lib", "message": "fix: Upgrade common-lib to v1.2.4", "author": "devops-lead"}),
            Action(name="open_pull_request", kwargs={"repo_name": "notification-service", "title": "fix(deps): Upgrade common-lib to v1.2.4", "body": "PR to upgrade outdated common-lib dependency to v1.2.4.", "head_branch": "fix/update-common-lib", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "notification-service", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "notification-service", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "notification-service", "issue_number": 13}),
            Action(name="fix_security_alert", kwargs={"repo_name": "notification-service", "alert_number": 10}),
            Action(name="create_release", kwargs={"repo_name": "notification-service", "version": "v0.1.0", "description": "Initial compliant release."}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "notification-service"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_50005",
        instruction=(
            "Your mission is to execute the **Standard Bug Fix Policy** for the 'payments-service' repository. The policy requires that bugs are formally tracked via issues and resolved via pull requests. "
            "You must use the provided **Bug Manifest** to create and process all required artifacts. "
            "Your final deliverable is the repository's health summary to certify that the bug has been resolved and all artifacts are closed.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that the bug is fully resolved. This requires a 'closed' tracking issue and a corresponding 'merged' pull request containing the code fix from its dedicated branch, with the two artifacts correctly linked.\n\n"
            "**Bug Manifest:**\n"
            "* **Issue:** {title: 'Bug: Incorrect fee calculation for international transactions', body: 'The service is applying the wrong fee percentage for non-domestic transactions.', labels: ['bug', 'payments'], assignee: 'backend-core'}\n"
            "* **Code Artifacts:** {branch: 'fix/international-fees', commit_message: 'fix: Apply correct fee tier for international payments', pr_title: 'Fix: International Fee Calculation', pr_body: 'This PR resolves the incorrect fee calculation bug.', author: 'backend-core'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "payments-service", "title": "Bug: Incorrect fee calculation for international transactions", "body": "The service is applying the wrong fee percentage for non-domestic transactions.", "labels": ["bug", "payments"]}),
            Action(name="assign_issue", kwargs={"repo_name": "payments-service", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-service", "branch": "fix/international-fees", "message": "fix: Apply correct fee tier for international payments", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "payments-service", "title": "Fix: International Fee Calculation", "body": "This PR resolves the incorrect fee calculation bug.", "head_branch": "fix/international-fees", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "payments-service", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "payments-service", "issue_number": 12}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "payments-service"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_60003",
        instruction=(
            "Your mission is to execute the **Secure Project Bootstrap Policy** for the new 'inventory-management-api' repository. "
            "This policy mandates that new projects created from a template must have any known vulnerabilities from that template remediated before the first release. "
            "You are responsible for ensuring the repository's state fully aligns with the **Bootstrap Compliance Specification**. "
            "Your final deliverable is the repository's health summary to confirm a compliant initial state.\n\n"
            "**Bootstrap Compliance Specification:**\n"
            "The final state must show that the repository was created with an initial commit. A 'medium' severity alert for an outdated dependency from the template must be 'fixed'. "
            "The entire setup and remediation process must be tracked via a main epic issue and a specific sub-task for the fix, both of which must be 'closed'. "
            "The fix must be delivered via a 'merged' pull request. A secure initial release must be published.\n\n"
            "**Data Manifest:**\n"
            "* **Repository:** {name: 'inventory-management-api', description: 'API for managing warehouse inventory.', private: True, initial_commit_message: 'Initial commit from template', initial_commit_author: 'devops-lead'}\n"
            "* **Security Alert:** {severity: 'medium', description: 'Default template includes outdated dependency: GSON v2.8.5', file: 'pom.xml'}\n"
            "* **Tracking:**\n"
            "    * **Epic Issue:** {title: 'Initial Project Setup', body: 'Main tracking issue for the complete and secure setup of the new repository.', labels: ['setup', 'epic'], assignee: 'backend-core'}\n"
            "    * **Fix Issue:** {title: 'fix: Update outdated GSON dependency', body: 'Sub-task to update the vulnerable GSON dependency from the initial template.', labels: ['security', 'dependency'], assignee: 'backend-core'}\n"
            "* **Remediation:**\n"
            "    * **Code:** {branch: 'hotfix/gson-upgrade', commit_message: 'fix: Upgrade GSON to v2.8.9', author: 'backend-core'}\n"
            "    * **PR:** {title: 'fix(deps): Upgrade GSON to v2.8.9', body: 'PR to upgrade outdated GSON dependency.', reviewers: ['tech-lead-tara']}\n"
            "* **Release:** {version: 'v0.1.0', description: 'Initial secure release.'}"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "inventory-management-api", "description": "API for managing warehouse inventory.", "private": True}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "inventory-management-api", "branch": "main", "message": "Initial commit from template", "author": "devops-lead"}),
            Action(name="create_security_alert", kwargs={"repo_name": "inventory-management-api", "severity": "medium", "description": "Default template includes outdated dependency: GSON v2.8.5", "file": "pom.xml", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "inventory-management-api", "title": "Initial Project Setup", "body": "Main tracking issue for the complete and secure setup of the new repository.", "labels": ["setup", "epic"]}),
            Action(name="assign_issue", kwargs={"repo_name": "inventory-management-api", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="create_issue", kwargs={"repo_name": "inventory-management-api", "title": "fix: Update outdated GSON dependency", "body": "Sub-task to update the vulnerable GSON dependency from the initial template.", "labels": ["security", "dependency"]}),
            Action(name="assign_issue", kwargs={"repo_name": "inventory-management-api", "issue_number": 13, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "inventory-management-api", "branch": "hotfix/gson-upgrade", "message": "fix: Upgrade GSON to v2.8.9", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "inventory-management-api", "title": "fix(deps): Upgrade GSON to v2.8.9", "body": "PR to upgrade outdated GSON dependency.", "head_branch": "hotfix/gson-upgrade", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "inventory-management-api", "pr_number": 10, "issue_number": 13}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "inventory-management-api", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "inventory-management-api", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "inventory-management-api", "issue_number": 13}),
            Action(name="fix_security_alert", kwargs={"repo_name": "inventory-management-api", "alert_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "inventory-management-api", "issue_number": 12}),
            Action(name="create_release", kwargs={"repo_name": "inventory-management-api", "version": "v0.1.0", "description": "Initial secure release."}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "inventory-management-api"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_30001",
        instruction=(
            "Your mission is to execute the **Standard Bug Fix Policy** for the 'payments-service' repository. The policy requires that bugs are formally tracked via issues and resolved via pull requests. You must use the provided **Bug Manifest** to create and process all required artifacts. Your final deliverable is the repository's health summary to certify that the bug has been resolved and all artifacts are closed.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that the bug is fully resolved. This requires a 'closed' tracking issue and a corresponding 'merged' pull request containing the code fix from its dedicated branch, with the two artifacts correctly linked.\n\n"
            "**Bug Manifest:**\n"
            "* **Issue:** {number: 12, title: 'Bug: Timeout issue with new payment gateway', body: 'Transactions are timing out when using the new payment gateway.', labels: ['bug', 'networking'], assignee: 'backend-core'}\n"
            "* **Code Artifacts:** {pr_number: 10, branch: 'fix/gateway-timeout', commit_message: 'fix: Increase timeout for new payment gateway', pr_title: 'Fix: Gateway Timeout', pr_body: 'This PR resolves the gateway timeout bug.', author: 'backend-core'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "payments-service", "title": "Bug: Timeout issue with new payment gateway", "body": "Transactions are timing out when using the new payment gateway.", "labels": ["bug", "networking"]}),
            Action(name="assign_issue", kwargs={"repo_name": "payments-service", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-service", "branch": "fix/gateway-timeout", "message": "fix: Increase timeout for new payment gateway", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "payments-service", "title": "Fix: Gateway Timeout", "body": "This PR resolves the gateway timeout bug.", "head_branch": "fix/gateway-timeout", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "payments-service", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "payments-service", "issue_number": 12}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "payments-service"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_30003",
        instruction=(
            "Your mission is to execute the **Feature Development Lifecycle Policy** for the 'ui-kit' repository. The policy requires that a new feature is tracked, implemented, and reviewed before being merged. You must use the provided **Feature Manifest** to create all required artifacts. Your final deliverable is the repository's activity dashboard to certify that the feature was successfully integrated.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a new feature was tracked via an issue, which must be 'closed'. The work must be implemented on a feature branch and submitted via a pull request. The pull request must be reviewed before it is merged.\n\n"
            "**Feature Manifest:**\n"
            "* **Issue:** {number: 12, title: 'Feature: Add user avatar component', body: 'Tracking issue for the new user avatar component.', labels: ['feature', 'ui'], assignee: 'ui-dev'}\n"
            "* **Code Artifacts:** {pr_number: 10, branch: 'feature/avatar-component', commit_message: 'feat: Add new user avatar component', pr_title: 'feat: User Avatar Component', pr_body: 'This PR adds the new user avatar component.', author: 'ui-dev'}\n"
            "* **Reviewer:** 'design-lead'"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Feature: Add user avatar component", "body": "Tracking issue for the new user avatar component.", "labels": ["feature", "ui"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12, "assignees": ["ui-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/avatar-component", "message": "feat: Add new user avatar component", "author": "ui-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "feat: User Avatar Component", "body": "This PR adds the new user avatar component.", "head_branch": "feature/avatar-component", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "ui-kit", "pr_number": 10, "reviewers": ["design-lead"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "ui-kit"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "ui-kit",
                    "commits_count": 1,
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_30004",
        instruction=(
            "Your mission is to execute the **New Project Bootstrap Policy** for the 'log-analyzer-service'. This policy ensures all new projects are created with a consistent set of initial artifacts for tracking, security, and deployment readiness. You must use the provided **Bootstrap Manifest** to create all required entities. Your final deliverable is the initial health summary for the newly created repository.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that the repository was created with an initial commit, has one 'open' tracking issue, one 'open' security alert, and has been deployed to the 'development' environment.\n\n"
            "**Bootstrap Manifest:**\n"
            "* **Repository:** {name: 'log-analyzer-service', description: 'Service for parsing and analyzing application logs.', private: True}\n"
            "* **Initial Commit:** {author: 'backend-core', message: 'Initial commit: project structure and boilerplate'}\n"
            "* **Tracking Issue:** {number: 12, title: 'Define initial logging schema', body: 'Establish the standard JSON schema for log entries.', labels: ['schema', 'design'], assignee: 'backend-core'}\n"
            "* **Initial Security Alert:** {severity: 'high', description: 'Potential for arbitrary code execution via insecure YAML parsing.', file: 'src/parser.py'}\n"
            "* **Initial Deployment:** {environment: 'development'}"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "log-analyzer-service", "description": "Service for parsing and analyzing application logs.", "private": True}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "log-analyzer-service", "branch": "main", "message": "Initial commit: project structure and boilerplate", "author": "backend-core"}),
            Action(name="create_issue", kwargs={"repo_name": "log-analyzer-service", "title": "Define initial logging schema", "body": "Establish the standard JSON schema for log entries.", "labels": ["schema", "design"]}),
            Action(name="assign_issue", kwargs={"repo_name": "log-analyzer-service", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="create_security_alert", kwargs={"repo_name": "log-analyzer-service", "severity": "high", "description": "Potential for arbitrary code execution via insecure YAML parsing.", "file": "src/parser.py", "branch": "main"}),
            Action(name="register_deploy_event", kwargs={"repo_name": "log-analyzer-service", "environment": "development"}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "log-analyzer-service"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_30005",
        instruction=(
            "Your mission is to execute the **Multi-Commit Feature Policy** for the 'infra-terraform' repository. The policy requires that features with contributions from multiple authors are consolidated into a single pull request for review. You must use the provided **Feature Manifest** to create all artifacts. Your final deliverable is a report of commits by author to verify the contributions.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a feature was tracked via a 'closed' issue. The work must be contained in a single 'merged' pull request that includes two commits from different authors.\n\n"
            "**Feature Manifest:**\n"
            "* **Issue:** {number: 12, title: 'Feature: Add reusable VPC module', body: 'Tracking issue for the new reusable VPC Terraform module.', labels: ['feature', 'terraform'], assignee: 'ops-team'}\n"
            "* **Code Artifacts:** {pr_number: 10, branch: 'feature/vpc-module', pr_title: 'feat: Reusable VPC Module', pr_body: 'Adds a new reusable module for creating standardized VPCs.', reviewers: ['tech-lead-tara']}\n"
            "* **Commits:**\n"
            "    * Commit 1: {message: 'feat: Add main module structure and variables', author: 'ops-team'}\n"
            "    * Commit 2: {message: 'test: Add integration tests for VPC module', author: 'devops-lead'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "infra-terraform", "title": "Feature: Add reusable VPC module", "body": "Tracking issue for the new reusable VPC Terraform module.", "labels": ["feature", "terraform"]}),
            Action(name="assign_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 12, "assignees": ["ops-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "infra-terraform", "branch": "feature/vpc-module", "message": "feat: Add main module structure and variables", "author": "ops-team"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "infra-terraform", "branch": "feature/vpc-module", "message": "test: Add integration tests for VPC module", "author": "devops-lead"}),
            Action(name="open_pull_request", kwargs={"repo_name": "infra-terraform", "title": "feat: Reusable VPC Module", "body": "Adds a new reusable module for creating standardized VPCs.", "head_branch": "feature/vpc-module", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "infra-terraform", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "infra-terraform", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "infra-terraform", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 12}),
            Action(name="count_commits_by_author", kwargs={"repo_name": "infra-terraform"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "infra-terraform",
                    "commits_by_author": {
                        "ops-team": 1,
                        "devops-lead": 1
                    },
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_20001",
        instruction=(
            "Your mission is to execute the **Standard Bug Fix Policy** for the 'payments-service' repository. The policy requires that bugs are formally tracked via issues and resolved via pull requests. You must use the provided **Bug Manifest** to create and process all required artifacts. Your final deliverable is the repository's health summary to certify that the bug has been resolved and all artifacts are closed.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that the bug is fully resolved. This requires a 'closed' tracking issue and a corresponding 'merged' pull request containing the code fix from its dedicated branch, with the two artifacts correctly linked.\n\n"
            "**Bug Manifest:**\n"
            "* **Issue:** {number: 12, title: 'Bug: Timeout issue with new payment gateway', body: 'Transactions are timing out when using the new payment gateway.', labels: ['bug', 'networking'], assignee: 'backend-core'}\n"
            "* **Code Artifacts:** {pr_number: 10, branch: 'fix/gateway-timeout', commit_message: 'fix: Increase timeout for new payment gateway', pr_title: 'Fix: Gateway Timeout', pr_body: 'This PR resolves the gateway timeout bug.', author: 'backend-core'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "payments-service", "title": "Bug: Timeout issue with new payment gateway", "body": "Transactions are timing out when using the new payment gateway.", "labels": ["bug", "networking"]}),
            Action(name="assign_issue", kwargs={"repo_name": "payments-service", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-service", "branch": "fix/gateway-timeout", "message": "fix: Increase timeout for new payment gateway", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "payments-service", "title": "Fix: Gateway Timeout", "body": "This PR resolves the gateway timeout bug.", "head_branch": "fix/gateway-timeout", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "payments-service", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "payments-service", "issue_number": 12}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "payments-service"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_20003",
        instruction=(
            "Your mission is to execute the **Proactive Dependency Update Policy** for the 'ml-pipeline' repository. The policy requires that outdated dependencies are updated in a timely manner. You must use the provided **Update Manifest** to perform the update. Your final deliverable is the repository's activity dashboard.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a tracking issue for the dependency update was created and is now 'closed'. The work must be contained in a 'merged' pull request that has been reviewed.\n\n"
            "**Update Manifest:**\n"
            "* **Issue:** {number: 12, title: 'chore(deps): Update scikit-learn to latest version', body: 'Update the scikit-learn dependency to the latest stable version.', labels: ['chore', 'dependencies'], assignee: 'ml-engineer'}\n"
            "* **Code Artifacts:** {pr_number: 10, branch: 'chore/update-sklearn', commit_message: 'chore: Update scikit-learn to v1.4.0', pr_title: 'chore(deps): Update scikit-learn', pr_body: 'This PR updates scikit-learn.', author: 'ml-engineer'}\n"
            "* **Reviewer:** 'data-scientist'"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "ml-pipeline", "title": "chore(deps): Update scikit-learn to latest version", "body": "Update the scikit-learn dependency to the latest stable version.", "labels": ["chore", "dependencies"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ml-pipeline", "issue_number": 12, "assignees": ["ml-engineer"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ml-pipeline", "branch": "chore/update-sklearn", "message": "chore: Update scikit-learn to v1.4.0", "author": "ml-engineer"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ml-pipeline", "title": "chore(deps): Update scikit-learn", "body": "This PR updates scikit-learn.", "head_branch": "chore/update-sklearn", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ml-pipeline", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "ml-pipeline", "pr_number": 10, "reviewers": ["data-scientist"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ml-pipeline", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ml-pipeline", "issue_number": 12}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "ml-pipeline"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "ml-pipeline",
                    "commits_count": 1,
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_20005",
        instruction=(
            "Your mission is to execute the **Multi-Commit Pull Request Policy** for the 'flutter-finance-app' repository. The policy requires that complex features with contributions from multiple authors are consolidated into a single pull request. You must use the provided **Feature Manifest** to create all artifacts. Your final deliverable is a report of commits by author to verify the contributions.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a feature was tracked via a 'closed' issue. The work must be contained in a single 'merged' pull request that includes two commits from different authors.\n\n"
            "**Feature Manifest:**\n"
            "* **Issue:** {number: 12, title: 'Feature: Add budget tracking and alerts', body: 'Tracking issue for the new budget tracking feature.', labels: ['feature', 'budgeting'], assignee: 'mobile-dev'}\n"
            "* **Code Artifacts:** {pr_number: 10, branch: 'feature/budget-tracking', pr_title: 'feat: Budget tracking and alerts', pr_body: 'Adds new components for budget tracking.', reviewers: ['tech-lead-tara']}\n"
            "* **Commits:**\n"
            "    * Commit 1: {message: 'feat: Add database schema for budgets', author: 'mobile-dev'}\n"
            "    * Commit 2: {message: 'feat: Implement UI for budget creation', author: 'frontend-dev'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "flutter-finance-app", "title": "Feature: Add budget tracking and alerts", "body": "Tracking issue for the new budget tracking feature.", "labels": ["feature", "budgeting"]}),
            Action(name="assign_issue", kwargs={"repo_name": "flutter-finance-app", "issue_number": 12, "assignees": ["mobile-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "flutter-finance-app", "branch": "feature/budget-tracking", "message": "feat: Add database schema for budgets", "author": "mobile-dev"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "flutter-finance-app", "branch": "feature/budget-tracking", "message": "feat: Implement UI for budget creation", "author": "frontend-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "flutter-finance-app", "title": "feat: Budget tracking and alerts", "body": "Adds new components for budget tracking.", "head_branch": "feature/budget-tracking", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "flutter-finance-app", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "flutter-finance-app", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "flutter-finance-app", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "flutter-finance-app", "issue_number": 12}),
            Action(name="count_commits_by_author", kwargs={"repo_name": "flutter-finance-app"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "flutter-finance-app",
                    "commits_by_author": {
                        "mobile-dev": 1,
                        "frontend-dev": 1
                    },
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_10001",
        instruction=(
            "Your mission is to execute the **Blocked Feature Policy** for the 'acme-webapp' repository. A new feature is in progress but is blocked by an external dependency. The policy requires that both the feature and the blocker are formally tracked. Your final deliverable is the repository's health summary to show the current state of open items.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show an 'open' pull request for the feature, linked to its 'open' tracking issue. A separate 'open' issue must exist to track the external blocker.\n\n"
            "**Data Specification:**\n"
            "* **Feature Issue:** {title: 'Feature: Integrate new payment provider', body: 'Tracking issue for the new payment provider feature.', labels: ['feature', 'payments'], assignee: 'alice-w'}\n"
            "* **Blocker Issue:** {title: 'Blocker: Waiting for new API version from payments provider', body: 'This issue tracks the external dependency blocking the feature development.', labels: ['blocked', 'external-dependency'], assignee: 'tech-lead-tara'}\n"
            "* **Code Artifacts:** {branch: 'feature/new-provider', commit_message: 'feat: Add initial scaffolding for new payment provider', pr_title: 'WIP: Feature/New Payment Provider', pr_body: 'Work in progress PR for the new payment provider.', author: 'alice-w'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "Feature: Integrate new payment provider", "body": "Tracking issue for the new payment provider feature.", "labels": ["feature", "payments"]}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12, "assignees": ["alice-w"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "acme-webapp", "branch": "feature/new-provider", "message": "feat: Add initial scaffolding for new payment provider", "author": "alice-w"}),
            Action(name="open_pull_request", kwargs={"repo_name": "acme-webapp", "title": "WIP: Feature/New Payment Provider", "body": "Work in progress PR for the new payment provider.", "head_branch": "feature/new-provider", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 10, "issue_number": 12}),
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "Blocker: Waiting for new API version from payments provider", "body": "This issue tracks the external dependency blocking the feature development.", "labels": ["blocked", "external-dependency"]}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 13, "assignees": ["tech-lead-tara"]}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "acme-webapp"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_10003",
        instruction=(
            "Your mission is to execute the **Security Audit and Triage Policy** for the 'security-scanner' repository. The policy requires that an audit is performed and that all findings are logged in a new, consolidated issue. Your final deliverable is a list of closed issues to confirm the audit issue was logged and resolved.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a new issue was created to summarize the audit findings and that this issue is now in a 'closed' state to signify the completion of the audit report.\n\n"
            "**Audit Manifest:**\n"
            "* **Audit Scope:** Analyze high-severity alerts, repository risk score, and team contribution stats.\n"
            "* **Summary Issue:** {title: 'Q3 Security Audit Summary', body: 'This issue summarizes the findings of the Q3 security audit, including risk score and alert review.', labels: ['audit', 'security'], assignee: 'tech-lead-tara'}"
        ),
        actions=[
            Action(name="list_alerts_by_severity", kwargs={"repo_name": "security-scanner", "severity": "high"}),
            Action(name="get_repository_risk_score", kwargs={"repo_name": "security-scanner"}),
            Action(name="get_team_contribution_stats", kwargs={"repo_name": "security-scanner"}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Q3 Security Audit Summary", "body": "This issue summarizes the findings of the Q3 security audit, including risk score and alert review.", "labels": ["audit", "security"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["tech-lead-tara"]}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12}),
            Action(name="get_closed_issues", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": [
                    {
                        "issue_id": "ISSUE_security-scanner_eb76c48f",
                        "title": "Q3 Security Audit Summary",
                        "labels": ["audit", "security"],
                        "state": "closed",
                        "closed_at": "2025-08-26",
                        "report_date": "2025-08-26"
                    }
                ]
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_10004",
        instruction=(
            "Your mission is to execute the **Hotfix Release Policy** for the 'payments-service' repository. A critical bug has been discovered that requires an immediate patch and release. You must use the provided **Hotfix Manifest** to create all artifacts. Your final deliverable is the repository's health summary, confirming the incident is resolved.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a critical bug was tracked via an issue, which must now be 'closed'. The fix must be implemented on a hotfix branch and 'merged' via a pull request. A new hotfix version must be released.\n\n"
            "**Hotfix Manifest:**\n"
            "* **Issue:** {title: 'Bug: Payment processor fails on CAD transactions', body: 'Critical bug causing failures for all CAD-denominated transactions.', labels: ['bug', 'hotfix'], assignee: 'backend-core'}\n"
            "* **Code Artifacts:** {branch: 'hotfix/cad-transactions', commit_message: 'fix: Add CAD currency handling to processor', pr_title: 'Fix: CAD Transaction Bug', pr_body: 'Hotfix for the CAD transaction bug.', author: 'backend-core'}\n"
            "* **Release:** {version: 'v1.0.1', description: 'Hotfix for CAD transaction failures.'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "payments-service", "title": "Bug: Payment processor fails on CAD transactions", "body": "Critical bug causing failures for all CAD-denominated transactions.", "labels": ["bug", "hotfix"]}),
            Action(name="assign_issue", kwargs={"repo_name": "payments-service", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-service", "branch": "hotfix/cad-transactions", "message": "fix: Add CAD currency handling to processor", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "payments-service", "title": "Fix: CAD Transaction Bug", "body": "Hotfix for the CAD transaction bug.", "head_branch": "hotfix/cad-transactions", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "payments-service", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "payments-service", "issue_number": 12}),
            Action(name="create_release", kwargs={"repo_name": "payments-service", "version": "v1.0.1", "description": "Hotfix for CAD transaction failures."}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "payments-service"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_10005",
        instruction=(
            "Your mission is to execute the **Multi-Commit Feature Policy** for the 'nlp-models' repository. The policy requires that features with contributions from multiple authors are consolidated into a single pull request for review. You must use the provided **Feature Manifest** to create all artifacts. Your final deliverable is a report of commits by author to verify the contributions.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a feature was tracked via a 'closed' issue. The work must be contained in a single 'merged' pull request that includes two commits from different authors.\n\n"
            "**Feature Manifest:**\n"
            "* **Issue:** {number: 12, title: 'Feature: Add model performance visualization', body: 'Tracking issue for the new performance visualization feature.', labels: ['feature', 'visualization'], assignee: 'data-scientist'}\n"
            "* **Code Artifacts:** {pr_number: 10, branch: 'feature/perf-viz', pr_title: 'feat: Model Performance Visualization', pr_body: 'Adds new components for model performance visualization.', reviewers: ['tech-lead-tara']}\n"
            "* **Commits:**\n"
            "    * Commit 1: {message: 'feat: Add data hooks for visualization API', author: 'data-scientist'}\n"
            "    * Commit 2: {message: 'feat: Implement chart components for visualization', author: 'ml-engineer'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "nlp-models", "title": "Feature: Add model performance visualization", "body": "Tracking issue for the new performance visualization feature.", "labels": ["feature", "visualization"]}),
            Action(name="assign_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "assignees": ["data-scientist"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "nlp-models", "branch": "feature/perf-viz", "message": "feat: Add data hooks for visualization API", "author": "data-scientist"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "nlp-models", "branch": "feature/perf-viz", "message": "feat: Implement chart components for visualization", "author": "ml-engineer"}),
            Action(name="open_pull_request", kwargs={"repo_name": "nlp-models", "title": "feat: Model Performance Visualization", "body": "Adds new components for model performance visualization.", "head_branch": "feature/perf-viz", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "nlp-models", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "nlp-models", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "nlp-models", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12}),
            Action(name="count_commits_by_author", kwargs={"repo_name": "nlp-models"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "nlp-models",
                    "commits_by_author": {
                        "data-scientist": 1,
                        "ml-engineer": 1
                    },
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_9001",
        instruction=(
            "Your mission is to execute the **Standard Bug Fix Policy** for the 'utils-js' repository. The policy requires that bugs are formally tracked via issues and resolved via pull requests. You must use the provided **Bug Manifest** to create and process all required artifacts. Your final deliverable is the repository's health summary to certify that the bug has been resolved and all artifacts are closed.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that the bug is fully resolved. This requires a 'closed' tracking issue and a corresponding 'merged' pull request containing the code fix from its dedicated branch, with the two artifacts correctly linked.\n\n"
            "**Bug Manifest:**\n"
            "* **Issue:** {title: 'Bug: Incorrect parsing of UTC date strings', body: 'The date utility incorrectly handles UTC strings, causing off-by-one day errors.', labels: ['bug', 'datetime'], assignee: 'bob-dev'}\n"
            "* **Code Artifacts:** {branch: 'fix/utc-parsing', commit_message: 'fix: Correct UTC date string parsing logic', pr_title: 'Fix: Date Parsing for UTC', pr_body: 'This PR resolves the UTC parsing bug.', author: 'bob-dev'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "utils-js", "title": "Bug: Incorrect parsing of UTC date strings", "body": "The date utility incorrectly handles UTC strings, causing off-by-one day errors.", "labels": ["bug", "datetime"]}),
            Action(name="assign_issue", kwargs={"repo_name": "utils-js", "issue_number": 12, "assignees": ["bob-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "utils-js", "branch": "fix/utc-parsing", "message": "fix: Correct UTC date string parsing logic", "author": "bob-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "utils-js", "title": "Fix: Date Parsing for UTC", "body": "This PR resolves the UTC parsing bug.", "head_branch": "fix/utc-parsing", "base_branch": "master"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "utils-js", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "utils-js", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "utils-js", "issue_number": 12}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "utils-js"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_9002",
        instruction=(
            "Your mission is to execute the **Alert Triage Policy** for a false positive in the 'acme-webapp' repository. The policy requires a formal investigation, documentation, and dismissal process. You must use the provided **Triage Manifest** to create all required artifacts. Your final deliverable is a report of all resolved security alerts to audit the triage decision.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a 'low' severity alert was created and then marked as 'fixed' to represent its dismissal. The investigation must be tracked via an issue, which must be 'closed'. A pull request containing only a code comment to suppress the linter warning must be merged.\n\n"
            "**Triage Manifest:**\n"
            "* **Alert:** {severity: 'low', description: 'Hardcoded timeout value in configuration', file: 'src/config.py'}\n"
            "* **Issue:** {title: 'Investigate hardcoded timeout alert - False Positive', body: 'Investigation of the hardcoded timeout value, which is confirmed to be a false positive.', assignee: 'alice-w'}\n"
            "* **Code Artifacts:** {branch: 'chore/suppress-linter-warning', commit_message: 'chore: Suppress linter warning for intentional timeout value', pr_title: 'Chore: Suppress timeout warning', pr_body: 'Adding linter suppression comment for approved false positive.', author: 'alice-w'}"
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "acme-webapp", "severity": "low", "description": "Hardcoded timeout value in configuration", "file": "src/config.py", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "Investigate hardcoded timeout alert - False Positive", "body": "Investigation of the hardcoded timeout value, which is confirmed to be a false positive."}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12, "assignees": ["alice-w"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "acme-webapp", "branch": "chore/suppress-linter-warning", "message": "chore: Suppress linter warning for intentional timeout value", "author": "alice-w"}),
            Action(name="open_pull_request", kwargs={"repo_name": "acme-webapp", "title": "Chore: Suppress timeout warning", "body": "Adding linter suppression comment for approved false positive.", "head_branch": "chore/suppress-linter-warning", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12}),
            Action(name="fix_security_alert", kwargs={"repo_name": "acme-webapp", "alert_number": 10}),
            Action(name="get_resolved_security_alerts", kwargs={"repo_name": "acme-webapp"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_9004",
        instruction=(
            "Your mission is to execute the **New Project Bootstrap Policy** for the 'log-analyzer-service'. This policy ensures all new projects are created with a consistent set of initial artifacts for tracking, security, and deployment readiness. You must use the provided **Bootstrap Manifest** to create all required entities. Your final deliverable is the initial health summary for the newly created repository.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that the repository was created with an initial commit, has one 'open' tracking issue, one 'open' security alert, and has been deployed to the 'development' environment.\n\n"
            "**Bootstrap Manifest:**\n"
            "* **Repository:** {name: 'log-analyzer-service', description: 'Service for parsing and analyzing application logs.', private: True}\n"
            "* **Initial Commit:** {author: 'backend-core', message: 'Initial commit: project structure and boilerplate'}\n"
            "* **Tracking Issue:** {title: 'Define initial logging schema', body: 'Establish the standard JSON schema for log entries.', labels: ['schema', 'design'], assignee: 'backend-core'}\n"
            "* **Initial Security Alert:** {severity: 'high', description: 'Potential for arbitrary code execution via insecure YAML parsing.', file: 'src/parser.py'}\n"
            "* **Initial Deployment:** {environment: 'development'}"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "log-analyzer-service", "description": "Service for parsing and analyzing application logs.", "private": True}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "log-analyzer-service", "branch": "main", "message": "Initial commit: project structure and boilerplate", "author": "backend-core"}),
            Action(name="create_issue", kwargs={"repo_name": "log-analyzer-service", "title": "Define initial logging schema", "body": "Establish the standard JSON schema for log entries.", "labels": ["schema", "design"]}),
            Action(name="assign_issue", kwargs={"repo_name": "log-analyzer-service", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="create_security_alert", kwargs={"repo_name": "log-analyzer-service", "severity": "high", "description": "Potential for arbitrary code execution via insecure YAML parsing.", "file": "src/parser.py", "branch": "main"}),
            Action(name="register_deploy_event", kwargs={"repo_name": "log-analyzer-service", "environment": "development"}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "log-analyzer-service"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_9005",
        instruction=(
            "Your mission is to execute the **Multi-Commit Feature Policy** for the 'nlp-models' repository. The policy requires that features with contributions from multiple authors are consolidated into a single pull request for review. You must use the provided **Feature Manifest** to create all artifacts. Your final deliverable is a report of commits by author to verify the contributions.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a feature was tracked via a 'closed' issue. The work must be contained in a single 'merged' pull request that includes two commits from different authors.\n\n"
            "**Feature Manifest:**\n"
            "* **Issue:** {title: 'Feature: Add model performance visualization', body: 'Tracking issue for the new performance visualization feature.', labels: ['feature', 'visualization'], assignee: 'data-scientist'}\n"
            "* **Code Artifacts:** {branch: 'feature/perf-viz', pr_title: 'feat: Model Performance Visualization', pr_body: 'Adds new components for model performance visualization.', reviewers: ['tech-lead-tara']}\n"
            "* **Commits:**\n"
            "    * Commit 1: {message: 'feat: Add data hooks for visualization API', author: 'data-scientist'}\n"
            "    * Commit 2: {message: 'feat: Implement chart components for visualization', author: 'ml-engineer'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "nlp-models", "title": "Feature: Add model performance visualization", "body": "Tracking issue for the new performance visualization feature.", "labels": ["feature", "visualization"]}),
            Action(name="assign_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "assignees": ["data-scientist"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "nlp-models", "branch": "feature/perf-viz", "message": "feat: Add data hooks for visualization API", "author": "data-scientist"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "nlp-models", "branch": "feature/perf-viz", "message": "feat: Implement chart components for visualization", "author": "ml-engineer"}),
            Action(name="open_pull_request", kwargs={"repo_name": "nlp-models", "title": "feat: Model Performance Visualization", "body": "Adds new components for model performance visualization.", "head_branch": "feature/perf-viz", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "nlp-models", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "nlp-models", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "nlp-models", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12}),
            Action(name="count_commits_by_author", kwargs={"repo_name": "nlp-models"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "nlp-models",
                    "commits_by_author": {
                        "data-scientist": 1,
                        "ml-engineer": 1
                    },
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_8001",
        instruction=(
            "Your mission is to execute the **Standard Bug Fix Policy** for the 'utils-js' repository. The policy requires that bugs are formally tracked via issues and resolved via pull requests. You must use the provided **Bug Manifest** to create and process all required artifacts. Your final deliverable is the repository's health summary to certify that the bug has been resolved and all artifacts are closed.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that the bug is fully resolved. This requires a 'closed' tracking issue and a corresponding 'merged' pull request containing the code fix from its dedicated branch, with the two artifacts correctly linked.\n\n"
            "**Bug Manifest:**\n"
            "* **Issue:** {title: 'Bug: Incorrect parsing of UTC date strings', body: 'The date utility incorrectly handles UTC strings, causing off-by-one day errors.', labels: ['bug', 'datetime'], assignee: 'bob-dev'}\n"
            "* **Code Artifacts:** {branch: 'fix/utc-parsing', commit_message: 'fix: Correct UTC date string parsing logic', pr_title: 'Fix: Date Parsing for UTC', pr_body: 'This PR resolves the UTC parsing bug.', author: 'bob-dev'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "utils-js", "title": "Bug: Incorrect parsing of UTC date strings", "body": "The date utility incorrectly handles UTC strings, causing off-by-one day errors.", "labels": ["bug", "datetime"]}),
            Action(name="assign_issue", kwargs={"repo_name": "utils-js", "issue_number": 12, "assignees": ["bob-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "utils-js", "branch": "fix/utc-parsing", "message": "fix: Correct UTC date string parsing logic", "author": "bob-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "utils-js", "title": "Fix: Date Parsing for UTC", "body": "This PR resolves the UTC parsing bug.", "head_branch": "fix/utc-parsing", "base_branch": "master"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "utils-js", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "utils-js", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "utils-js", "issue_number": 12}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "utils-js"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_8002",
        instruction=(
            "Your mission is to execute the **Alert Triage Policy** for a false positive in the 'acme-webapp' repository. The policy requires a formal investigation, documentation, and dismissal process. You must use the provided **Triage Manifest** to create all required artifacts. Your final deliverable is a report of all resolved security alerts to audit the triage decision.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a 'low' severity alert was created and then marked as 'fixed' to represent its dismissal. The investigation must be tracked via an issue, which must be 'closed'. A pull request containing only a code comment to suppress the linter warning must be merged.\n\n"
            "**Triage Manifest:**\n"
            "* **Alert:** {severity: 'low', description: 'Hardcoded timeout value in configuration', file: 'src/config.py'}\n"
            "* **Issue:** {title: 'Investigate hardcoded timeout alert - False Positive', body: 'Investigation of the hardcoded timeout value, which is confirmed to be a false positive.', assignee: 'alice-w'}\n"
            "* **Code Artifacts:** {branch: 'chore/suppress-linter-warning', commit_message: 'chore: Suppress linter warning for intentional timeout value', pr_title: 'Chore: Suppress timeout warning', pr_body: 'Adding linter suppression comment for approved false positive.', author: 'alice-w'}"
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "acme-webapp", "severity": "low", "description": "Hardcoded timeout value in configuration", "file": "src/config.py", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "Investigate hardcoded timeout alert - False Positive", "body": "Investigation of the hardcoded timeout value, which is confirmed to be a false positive."}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12, "assignees": ["alice-w"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "acme-webapp", "branch": "chore/suppress-linter-warning", "message": "chore: Suppress linter warning for intentional timeout value", "author": "alice-w"}),
            Action(name="open_pull_request", kwargs={"repo_name": "acme-webapp", "title": "Chore: Suppress timeout warning", "body": "Adding linter suppression comment for approved false positive.", "head_branch": "chore/suppress-linter-warning", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12}),
            Action(name="fix_security_alert", kwargs={"repo_name": "acme-webapp", "alert_number": 10}),
            Action(name="get_resolved_security_alerts", kwargs={"repo_name": "acme-webapp"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_8003",
        instruction=(
            "Your mission is to execute the **Feature Development Lifecycle Policy** for the 'ui-kit' repository. The policy requires that a new feature is tracked, implemented, and reviewed before being merged. You must use the provided **Feature Manifest** to create all required artifacts. Your final deliverable is the repository's activity dashboard to certify that the feature was successfully integrated.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a new feature was tracked via an issue, which must be 'closed'. The work must be implemented on a feature branch and submitted via a pull request. The pull request must be reviewed before it is merged.\n\n"
            "**Feature Manifest:**\n"
            "* **Issue:** {title: 'Feature: Add user avatar component', body: 'Tracking issue for the new user avatar component.', labels: ['feature', 'ui'], assignee: 'ui-dev'}\n"
            "* **Code Artifacts:** {branch: 'feature/avatar-component', commit_message: 'feat: Add new user avatar component', pr_title: 'feat: User Avatar Component', pr_body: 'This PR adds the new user avatar component.', author: 'ui-dev'}\n"
            "* **Reviewer:** 'design-lead'"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Feature: Add user avatar component", "body": "Tracking issue for the new user avatar component.", "labels": ["feature", "ui"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12, "assignees": ["ui-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/avatar-component", "message": "feat: Add new user avatar component", "author": "ui-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "feat: User Avatar Component", "body": "This PR adds the new user avatar component.", "head_branch": "feature/avatar-component", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "ui-kit", "pr_number": 10, "reviewers": ["design-lead"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "ui-kit"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "ui-kit",
                    "commits_count": 1,
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_8004",
        instruction=(
            "Your mission is to execute the **New Project Bootstrap Policy** for the 'log-analyzer-service'. This policy ensures all new projects are created with a consistent set of initial artifacts for tracking, security, and deployment readiness. You must use the provided **Bootstrap Manifest** to create all required entities. Your final deliverable is the initial health summary for the newly created repository.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that the repository was created with an initial commit, has one 'open' tracking issue, one 'open' security alert, and has been deployed to the 'development' environment.\n\n"
            "**Bootstrap Manifest:**\n"
            "* **Repository:** {name: 'log-analyzer-service', description: 'Service for parsing and analyzing application logs.', private: True}\n"
            "* **Initial Commit:** {author: 'backend-core', message: 'Initial commit: project structure and boilerplate'}\n"
            "* **Tracking Issue:** {title: 'Define initial logging schema', body: 'Establish the standard JSON schema for log entries.', labels: ['schema', 'design'], assignee: 'backend-core'}\n"
            "* **Initial Security Alert:** {severity: 'high', description: 'Potential for arbitrary code execution via insecure YAML parsing.', file: 'src/parser.py'}\n"
            "* **Initial Deployment:** {environment: 'development'}"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "log-analyzer-service", "description": "Service for parsing and analyzing application logs.", "private": True}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "log-analyzer-service", "branch": "main", "message": "Initial commit: project structure and boilerplate", "author": "backend-core"}),
            Action(name="create_issue", kwargs={"repo_name": "log-analyzer-service", "title": "Define initial logging schema", "body": "Establish the standard JSON schema for log entries.", "labels": ["schema", "design"]}),
            Action(name="assign_issue", kwargs={"repo_name": "log-analyzer-service", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="create_security_alert", kwargs={"repo_name": "log-analyzer-service", "severity": "high", "description": "Potential for arbitrary code execution via insecure YAML parsing.", "file": "src/parser.py", "branch": "main"}),
            Action(name="register_deploy_event", kwargs={"repo_name": "log-analyzer-service", "environment": "development"}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "log-analyzer-service"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_8005",
        instruction=(
            "Your mission is to execute the **Release Hotfix Policy** for the 'payments-service' repository. A new release has been found to contain a critical bug. The policy requires the bug to be tracked and a new hotfix version to be released. You must use the provided **Hotfix Manifest** to perform all actions. Your final deliverable is the repository's health summary to certify that the hotfix process was completed and the repository has no open items.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that two releases exist: the initial faulty one and the subsequent hotfix. A tracking issue for the bug must be 'closed', and the hotfix must be implemented via a 'merged' pull request.\n\n"
            "**Hotfix Manifest:**\n"
            "* **Initial Release:** {version: 'v1.0.0', description: 'Initial feature release.', commit_message: 'feat: Add new payment processor', pr_title: 'feat: New Payment Processor', pr_body: 'Initial PR for the new payment processor.'}\n"
            "* **Bug Issue:** {title: 'Bug: New processor fails on EUR transactions', body: 'Critical bug causing failures for all EUR-denominated transactions.', labels: ['bug', 'hotfix'], assignee: 'backend-core'}\n"
            "* **Hotfix Artifacts:** {branch: 'hotfix/eur-transactions', commit_message: 'fix: Add EUR currency handling to new processor', pr_title: 'Fix: EUR Transaction Bug', pr_body: 'Hotfix for the EUR transaction bug.', author: 'backend-core'}\n"
            "* **Hotfix Release:** {version: 'v1.0.1', description: 'Hotfix for EUR transaction failures.'}"
        ),
        actions=[
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-service", "branch": "main", "message": "feat: Add new payment processor", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "payments-service", "title": "feat: New Payment Processor", "body": "Initial PR for the new payment processor.", "head_branch": "main", "base_branch": "main"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 10}),
            Action(name="create_release", kwargs={"repo_name": "payments-service", "version": "v1.0.0", "description": "Initial feature release."}),
            Action(name="create_issue", kwargs={"repo_name": "payments-service", "title": "Bug: New processor fails on EUR transactions", "body": "Critical bug causing failures for all EUR-denominated transactions.", "labels": ["bug", "hotfix"]}),
            Action(name="assign_issue", kwargs={"repo_name": "payments-service", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-service", "branch": "hotfix/eur-transactions", "message": "fix: Add EUR currency handling to new processor", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "payments-service", "title": "Fix: EUR Transaction Bug", "body": "Hotfix for the EUR transaction bug.", "head_branch": "hotfix/eur-transactions", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "payments-service", "pr_number": 11, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "payments-service", "issue_number": 12}),
            Action(name="create_release", kwargs={"repo_name": "payments-service", "version": "v1.0.1", "description": "Hotfix for EUR transaction failures."}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "payments-service"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_7001",
        instruction=(
            "Your objective is to execute the company's **Full Security Remediation Policy** for the 'security-scanner' repository. The policy requires that newly discovered vulnerabilities are logged, tracked, and fully resolved through a standard PR lifecycle. You are responsible for ensuring the repository's final state matches the official **Remediation Compliance Specification** below. Your final deliverable is an end-to-end report to validate the repository's newly hardened security posture.\n\n"
            "**Remediation Compliance Specification:**\n"
            "* **Vulnerability Logging:** Two new 'critical' alerts must be created and subsequently moved to a 'fixed' state.\n"
            "* **Incident Tracking:** Two corresponding issues must be created to track the alerts and must be 'closed' by the end of the process.\n"
            "* **Code Remediation:** All code changes must be consolidated into a single 'merged' Pull Request, originating from an existing branch and linked to both tracking issues.\n\n"
            "**Data Specification:**\n"
            "* Alert 1: {description: 'Unsafe deserialization in YAML parser', file: 'src/parser.rs'}\n"
            "* Alert 2: {description: 'Potential buffer overflow in string handler', file: 'src/scanner.rs'}\n"
            "* Issue 1: {title: 'Track: Unsafe Deserialization', body: 'Tracking issue for the critical alert regarding the YAML parser.', labels: ['bug', 'security'], assignee: 'security-team'}\n"
            "* Issue 2: {title: 'Track: Buffer Overflow', body: 'Tracking issue for the critical alert regarding the string handler.', labels: ['bug', 'security'], assignee: 'security-team'}\n"
            "* Code Artifacts: {branch: 'perf-optimizations', pr_title: 'Fix: Remediate Critical Parser and Scanner Vulnerabilities', pr_body: 'This PR addresses critical vulnerabilities discovered during a security audit.', commit_1: 'fix: Add validation to YAML parser', commit_2: 'fix: Implement bounds checking in string handler', author: 'security-team'}"
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "security-scanner", "severity": "critical", "description": "Unsafe deserialization in YAML parser", "file": "src/parser.rs", "branch": "main"}),
            Action(name="create_security_alert", kwargs={"repo_name": "security-scanner", "severity": "critical", "description": "Potential buffer overflow in string handler", "file": "src/scanner.rs", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Track: Unsafe Deserialization", "body": "Tracking issue for the critical alert regarding the YAML parser.", "labels": ["bug", "security"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["security-team"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Track: Buffer Overflow", "body": "Tracking issue for the critical alert regarding the string handler.", "labels": ["bug", "security"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "perf-optimizations", "message": "fix: Add validation to YAML parser", "author": "security-team"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "perf-optimizations", "message": "fix: Implement bounds checking in string handler", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "Fix: Remediate Critical Parser and Scanner Vulnerabilities", "head_branch": "perf-optimizations", "base_branch": "main", "body": "This PR addresses critical vulnerabilities discovered during a security audit."}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 12}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="fix_security_alert", kwargs={"repo_name": "security-scanner", "alert_number": 10}),
            Action(name="fix_security_alert", kwargs={"repo_name": "security-scanner", "alert_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13}),
            Action(name="generate_end_to_end_report", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_7002",
        instruction=(
            "Your objective is to execute the **Standard Release Protocol** for the 'k8s-monitoring' repository. You are responsible for ensuring the repository's final state is compliant with the official **Compliance Specification for v2.5.0** below. Your final deliverable is the repository's health summary to confirm the protocol was followed.\n\n"
            "**Compliance Specification for v2.5.0:**\n"
            "* **Code & PR:** A commit by `devops-lead` with the message 'Docs: Finalize guide for Prometheus v2.5.0' must be merged from the 'upgrade-prometheus' branch via a pull request titled 'Release v2.5.0: Prometheus Upgrade' with a body of 'This PR finalizes the Prometheus v2.5.0 upgrade for production release.'.\n"
            "* **Tracking:** Two new 'open' issues must exist and be assigned to `devops-lead`: one titled 'Task: Verify prometheus scraping post-upgrade' with a body of 'Post-release verification needed for prometheus scraping configurations.' and ['task', 'monitoring'] labels, and another titled 'Task: Audit Alertmanager notification channels' with a body of 'Post-release audit needed for Alertmanager notification routing and channels.' and ['task', 'alerting'] labels.\n"
            "* **Release & Deployment:** A formal release 'v2.5.0' with the description 'Official release for the Prometheus v2.5.0 upgrade.' must be published, and a deployment to the 'production' environment must be registered."
        ),
        actions=[
            Action(name="add_commit_to_branch", kwargs={"repo_name": "k8s-monitoring", "branch": "upgrade-prometheus", "message": "Docs: Finalize guide for Prometheus v2.5.0", "author": "devops-lead"}),
            Action(name="open_pull_request", kwargs={"repo_name": "k8s-monitoring", "title": "Release v2.5.0: Prometheus Upgrade", "head_branch": "upgrade-prometheus", "base_branch": "main", "body": "This PR finalizes the Prometheus v2.5.0 upgrade for production release."}),
            Action(name="merge_pull_request", kwargs={"repo_name": "k8s-monitoring", "pr_number": 10}),
            Action(name="create_issue", kwargs={"repo_name": "k8s-monitoring", "title": "Task: Verify prometheus scraping post-upgrade", "body": "Post-release verification needed for prometheus scraping configurations.", "labels": ["task", "monitoring"]}),
            Action(name="assign_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 12, "assignees": ["devops-lead"]}),
            Action(name="create_issue", kwargs={"repo_name": "k8s-monitoring", "title": "Task: Audit Alertmanager notification channels", "body": "Post-release audit needed for Alertmanager notification routing and channels.", "labels": ["task", "alerting"]}),
            Action(name="assign_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 13, "assignees": ["devops-lead"]}),
            Action(name="create_release", kwargs={"repo_name": "k8s-monitoring", "version": "v2.5.0", "description": "Official release for the Prometheus v2.5.0 upgrade."}),
            Action(name="register_deploy_event", kwargs={"repo_name": "k8s-monitoring", "environment": "production"}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "k8s-monitoring"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_7003",
        instruction=(
            "Your objective is to execute the **Backlog Grooming Policy** for the 'nlp-models' repository. The policy requires a formal audit of repository health and the creation of tracking issues for identified areas of improvement. You must use the provided **Audit Manifest** to ensure the repository's final state is compliant. Your final deliverable is an end-to-end report confirming the new issues are correctly logged.\n\n"
            "**Compliance Specification:**\n"
            "The final state of the repository must include two new 'open' issues that have been correctly assigned based on the audit findings.\n\n"
            "**Audit Manifest:**\n"
            "* **Required Issue 1 (Technical Debt):** {title: 'Technical Debt: Audit Aging Items', body: 'Audit to identify and prioritize aging issues and slow PRs.', labels: ['tech-debt', 'audit'], assignee: 'ml-engineer'}\n"
            "* **Required Issue 2 (Enhancement):** {title: 'Enhancement: Improve Tokenizer Support', body: 'Formal tracking for feature request to improve custom tokenizer support.', labels: ['enhancement', 'tokenizer'], assignee: 'nlp-labs'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "nlp-models", "title": "Technical Debt: Audit Aging Items", "body": "Audit to identify and prioritize aging issues and slow PRs.", "labels": ["tech-debt", "audit"]}),
            Action(name="assign_issue", kwargs={"repo_name": "nlp-models", "issue_number": 12, "assignees": ["ml-engineer"]}),
            Action(name="create_issue", kwargs={"repo_name": "nlp-models", "title": "Enhancement: Improve Tokenizer Support", "body": "Formal tracking for feature request to improve custom tokenizer support.", "labels": ["enhancement", "tokenizer"]}),
            Action(name="assign_issue", kwargs={"repo_name": "nlp-models", "issue_number": 13, "assignees": ["nlp-labs"]}),
            Action(name="generate_end_to_end_report", kwargs={"repo_name": "nlp-models"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_6002",
        instruction=(
            "Your mission is to execute the **Bug Resolution Audit Policy** for the 'utils-js' repository. A bug needs to be fixed and a proper audit trail must be established. "
            "Your final deliverable is a repository health summary to certify that the bug tracking issue was correctly resolved and closed.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a bug was tracked via an issue, which must be 'closed'. The fix must be implemented on a dedicated branch and merged via a pull request.\n\n"
            "**Data Specification:**\n"
            "* Issue Title: 'Bug: Incorrect parsing of date strings'\n"
            "* Assignee/Author: 'bob-dev'\n"
            "* Code Artifacts: {branch: 'fix/date-parsing', commit_message: 'fix: Correct date string parsing logic', pr_title: 'fix: Date parsing'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "utils-js", "title": "Bug: Incorrect parsing of date strings", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "utils-js", "issue_number": 12, "assignees": ["bob-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "utils-js", "branch": "fix/date-parsing", "message": "fix: Correct date string parsing logic", "author": "bob-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "utils-js", "title": "fix: Date parsing", "body": "", "head_branch": "fix/date-parsing", "base_branch": "master", "author": "bob-dev"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "utils-js", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "utils-js", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "utils-js", "issue_number": 12}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "utils-js"}),
        ],
        outputs=[
            {
                "repo": "utils-js",
                "open_issues": 0,
                "open_prs": 0,
                "open_alerts": 0,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_6003",
        instruction=(
            "Your mission is to execute the **Feature Development Lifecycle Policy** for the 'react-dashboard' repository. A new feature needs to be implemented and tracked. "
            "The policy requires that the pull request is in a mergeable state before being merged. Your final deliverable is the repository's health summary to certify that the feature was successfully integrated.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a new feature was tracked via an issue, which must be 'closed'. The work must be implemented on a feature branch and submitted via a pull request. "
            "The metadata of this pull request must be checked to ensure it is valid before it is merged.\n\n"
            "**Data Specification:**\n"
            "* Issue Title: 'Feature: Add user activity timeline'\n"
            "* Assignee/Author: 'frontend-dev'\n"
            "* Code Artifacts: {branch: 'feature/activity-timeline', commit_message: 'feat: Add activity timeline component', pr_title: 'feat: User Activity Timeline'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "react-dashboard", "title": "Feature: Add user activity timeline", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 12, "assignees": ["frontend-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "react-dashboard", "branch": "feature/activity-timeline", "message": "feat: Add activity timeline component", "author": "frontend-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "react-dashboard", "title": "feat: User Activity Timeline", "body": "", "head_branch": "feature/activity-timeline", "base_branch": "main", "author": "frontend-dev"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "react-dashboard", "pr_number": 10, "issue_number": 12}),
            Action(name="get_pull_request_metadata", kwargs={"repo_name": "react-dashboard", "pr_number": 10}),
            Action(name="merge_pull_request", kwargs={"repo_name": "react-dashboard", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 12}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "react-dashboard"}),
        ],
        outputs=[
            {
                "repo": "react-dashboard",
                "open_issues": 0,
                "open_prs": 0,
                "open_alerts": 0,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_6004",
        instruction=(
            "Your mission is to execute the **Iterative Fix Policy** for the 'ml-pipeline' repository. A high-severity alert has been triggered. The policy requires documenting all attempted fixes, even incorrect ones, to maintain a clear audit trail. "
            "Your final deliverable is a report of all resolved alerts to audit the final, successful fix.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a new 'high' severity alert was created and later marked as 'fixed'. The incident must be tracked by a single issue, which should be closed only after the final fix is merged. "
            "The audit trail must show one pull request that remains open without merging (representing a failed attempt) and a second pull request that was successfully merged with the correct fix.\n\n"
            "**Data Specification:**\n"
            "* Alert Details: {description: 'Data leakage in preprocessing script', file: 'src/preprocessing.py'}\n"
            "* Issue Title: 'Security: Remediate data leakage in preprocessing'\n"
            "* Assignee/Author: 'ml-engineer'\n"
            "* Incorrect Fix: {branch: 'fix/leak-attempt-1', commit_message: 'fix: Sanitize output data', pr_title: 'fix: Sanitize data'}\n"
            "* Correct Fix: {branch: 'fix/leak-attempt-2', commit_message: 'fix: Isolate data processing contexts', pr_title: 'fix: Isolate processing contexts'}"
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "ml-pipeline", "severity": "high", "description": "Data leakage in preprocessing script", "file": "src/preprocessing.py", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "ml-pipeline", "title": "Security: Remediate data leakage in preprocessing", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "ml-pipeline", "issue_number": 12, "assignees": ["ml-engineer"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ml-pipeline", "branch": "fix/leak-attempt-1", "message": "fix: Sanitize output data", "author": "ml-engineer"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ml-pipeline", "title": "fix: Sanitize data", "body": "", "head_branch": "fix/leak-attempt-1", "base_branch": "main", "author": "ml-engineer"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ml-pipeline", "pr_number": 10, "issue_number": 12}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ml-pipeline", "branch": "fix/leak-attempt-2", "message": "fix: Isolate data processing contexts", "author": "ml-engineer"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ml-pipeline", "title": "fix: Isolate processing contexts", "body": "", "head_branch": "fix/leak-attempt-2", "base_branch": "main", "author": "ml-engineer"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ml-pipeline", "pr_number": 11, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ml-pipeline", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "ml-pipeline", "issue_number": 12}),
            Action(name="fix_security_alert", kwargs={"repo_name": "ml-pipeline", "alert_number": 10}),
            Action(name="get_resolved_security_alerts", kwargs={"repo_name": "ml-pipeline"}),
        ],
        outputs=[
            [
                {
                    "alert_id": "ALERT_ml-pipeline_007eb4d6",
                    "severity": "high",
                    "state": "fixed",
                    "resolved_at": "2025-08-26",
                    "description": "Data leakage in preprocessing script"
                }
            ]
        ],
    ),
    Task(
        annotator="1",
        user_id="user_6005",
        instruction=(
            "Your mission is to execute the **Security Audit Policy** for the 'flutter-finance-app' repository. The policy requires a full audit of open and resolved alerts. "
            "Your final deliverable is a dual report listing both open and resolved alerts to provide a complete security posture overview.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a new 'medium' severity alert was created and remains 'open', and a new 'low' severity alert was created and then marked as 'fixed'. "
            "The resolution of the low-severity alert must be tracked via a closed issue and a merged pull request.\n\n"
            "**Data Specification:**\n"
            "* Open Alert: {description: 'Use of deprecated encryption algorithm', file: 'lib/crypto.dart'}\n"
            "* Resolved Alert: {description: 'Verbose error message in UI', file: 'lib/ui.dart'}\n"
            "* Tracking Issue Title: 'Fix verbose error message'\n"
            "* Code Artifacts: {branch: 'fix/verbose-error', commit_message: 'fix: Use generic error messages', pr_title: 'fix: Verbose errors'}"
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "flutter-finance-app", "severity": "medium", "description": "Use of deprecated encryption algorithm", "file": "lib/crypto.dart", "branch": "main"}),
            Action(name="create_security_alert", kwargs={"repo_name": "flutter-finance-app", "severity": "low", "description": "Verbose error message in UI", "file": "lib/ui.dart", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "flutter-finance-app", "title": "Fix verbose error message", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "flutter-finance-app", "issue_number": 12, "assignees": ["mobile-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "flutter-finance-app", "branch": "fix/verbose-error", "message": "fix: Use generic error messages", "author": "mobile-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "flutter-finance-app", "title": "fix: Verbose errors", "body": "", "head_branch": "fix/verbose-error", "base_branch": "main", "author": "mobile-dev"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "flutter-finance-app", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "flutter-finance-app", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "flutter-finance-app", "issue_number": 12}),
            Action(name="fix_security_alert", kwargs={"repo_name": "flutter-finance-app", "alert_number": 11}),
            Action(name="get_open_security_alerts", kwargs={"repo_name": "flutter-finance-app"}),
            Action(name="get_resolved_security_alerts", kwargs={"repo_name": "flutter-finance-app"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_5001",
        instruction=(
            "Your mission is to execute the **CI/CD Pipeline Hardening Policy** for the 'infra-terraform' repository. A security review has identified weaknesses that must be addressed. "
            "The policy requires that such initiatives are tracked through a main epic and specific sub-tasks, with all code changes consolidated into a single, reviewed pull request. Upon completion, all related tracking artifacts must be closed. "
            "You must use the provided data specification to bring the repository into a compliant state. "
            "Your final deliverable is the repository's activity dashboard to certify that the policy was executed and the repository is in a clean state.\n\n"
            "**Data Specification:**\n"
            "* **Epic:** {title: 'Q3 CI/CD Hardening Sprint', body: ''}\n"
            "* **Sub-Tasks:** [{title: 'Integrate SAST scanning in pipeline', body: ''}, {title: 'Enforce branch protection rules on main', body: ''}]\n"
            "* **Implementation:** {branch: 'feature/pipeline-hardening', commit_message: 'feat: Add SAST scanning and branch protection', pr_title: 'feat: Harden CI/CD Pipeline', pr_body: ''}\n"
            "* **Ownership:** {assignee: 'ops-team', author: 'ops-team'}\n"
            "* **Review:** {reviewer: 'security-team'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "infra-terraform", "title": "Q3 CI/CD Hardening Sprint", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 12, "assignees": ["ops-team"]}),
            Action(name="create_issue", kwargs={"repo_name": "infra-terraform", "title": "Integrate SAST scanning in pipeline", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 13, "assignees": ["ops-team"]}),
            Action(name="create_issue", kwargs={"repo_name": "infra-terraform", "title": "Enforce branch protection rules on main", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 14, "assignees": ["ops-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "infra-terraform", "branch": "feature/pipeline-hardening", "message": "feat: Add SAST scanning and branch protection", "author": "ops-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "infra-terraform", "title": "feat: Harden CI/CD Pipeline", "body": "", "head_branch": "feature/pipeline-hardening", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "infra-terraform", "pr_number": 10, "issue_number": 12}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "infra-terraform", "pr_number": 10, "issue_number": 13}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "infra-terraform", "pr_number": 10, "issue_number": 14}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "infra-terraform", "pr_number": 10, "reviewers": ["security-team"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "infra-terraform", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 13}),
            Action(name="close_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 14}),
            Action(name="close_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 12}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "infra-terraform"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "infra-terraform",
                    "commits_count": 1,
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_5004",
        instruction=(
            "Your mission is to execute the **New Service Onboarding Policy**. A new service, 'recommendation-engine', is being created. The policy requires not only creating the repository and its initial code, "
            "but also setting up basic monitoring for it in the central 'k8s-monitoring' repository. Your final deliverable is a filtered list of issues from the monitoring repo to confirm that the setup tasks were created.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that the new 'recommendation-engine' repository was created and contains an initial merged pull request. Concurrently, two new issues must be created and left 'open' in the 'k8s-monitoring' repository to track the addition of the new service to the monitoring stack. These monitoring issues must be correctly labeled.\n\n"
            "**Data Specification:**\n"
            "* `recommendation-engine` Artifacts: {description: 'Recommendation engine service', private: True, issue_title: 'Initial service setup', branch: 'feature/initial-setup', commit_message: 'feat: Initial service boilerplate', pr_title: 'feat: Initial Setup', assignee: 'data-scientist'}\n"
            "* `k8s-monitoring` Issues: [{title: 'Add recommendation-engine to Prometheus scrape configs', labels: ['monitoring', 'config'], assignee: 'devops-lead'}, {title: 'Create Grafana dashboard for recommendation-engine', labels: ['monitoring', 'dashboard'], assignee: 'devops-lead'}]"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "recommendation-engine", "description": "Recommendation engine service", "private": True}),
            Action(name="create_issue", kwargs={"repo_name": "recommendation-engine", "title": "Initial service setup", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "recommendation-engine", "issue_number": 12, "assignees": ["data-scientist"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "recommendation-engine", "branch": "feature/initial-setup", "message": "feat: Initial service boilerplate", "author": "data-scientist"}),
            Action(name="open_pull_request", kwargs={"repo_name": "recommendation-engine", "title": "feat: Initial Setup", "body": "", "head_branch": "feature/initial-setup", "base_branch": "main", "author": "data-scientist"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "recommendation-engine", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "recommendation-engine", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "recommendation-engine", "issue_number": 12}),
            Action(name="create_issue", kwargs={"repo_name": "k8s-monitoring", "title": "Add recommendation-engine to Prometheus scrape configs", "body": "", "labels": ["monitoring", "config"]}),
            Action(name="assign_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 13, "assignees": ["devops-lead"]}),
            Action(name="create_issue", kwargs={"repo_name": "k8s-monitoring", "title": "Create Grafana dashboard for recommendation-engine", "body": "", "labels": ["monitoring", "dashboard"]}),
            Action(name="assign_issue", kwargs={"repo_name": "k8s-monitoring", "issue_number": 14, "assignees": ["devops-lead"]}),
            Action(name="list_issues_by_label", kwargs={"repo_name": "k8s-monitoring", "label": "monitoring"}),
        ],
        outputs=[
            [
                {
                    "issue_id": "ISSUE_k8s-monitoring_c0e36431",
                    "title": "Add recommendation-engine to Prometheus scrape configs",
                    "labels": ["monitoring", "config"],
                    "state": "open",
                    "report_date": "2025-08-26"
                },
                {
                    "issue_id": "ISSUE_k8s-monitoring_22cc09d5",
                    "title": "Create Grafana dashboard for recommendation-engine",
                    "labels": ["monitoring", "dashboard"],
                    "state": "open",
                    "report_date": "2025-08-26"
                }
            ]
        ],
    ),
    Task(
        annotator="1",
        user_id="user_4002",
        instruction=(
            "Your mission is to execute the **Merge Velocity Audit Policy** for the 'payments-service' repository. Management is concerned about the time it takes to merge pull requests. "
            "The policy requires creating and merging two separate pull requests to simulate different types of changes and then generating a report on the average merge time. "
            "Your final deliverable is this merge time report.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that two separate workflows were completed. Each workflow must include a dedicated issue that is closed and a pull request that is merged. "
            "One workflow is for a feature, and the other is for a bug fix.\n\n"
            "**Data Specification:**\n"
            "* Author/Assignee: 'backend-core'\n"
            "* Feature Artifacts: {issue_title: 'Add support for a new payment gateway', branch: 'feature/new-gateway', commit_message: 'feat: Integrate new gateway API', pr_title: 'feat: New Gateway'}\n"
            "* Bugfix Artifacts: {issue_title: 'Fix currency formatting for negative values', branch: 'fix/currency-format', commit_message: 'fix: Handle negative currency values', pr_title: 'fix: Negative Currency'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "payments-service", "title": "Add support for a new payment gateway", "body": ""}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-service", "branch": "feature/new-gateway", "message": "feat: Integrate new gateway API", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "payments-service", "title": "feat: New Gateway", "body": "", "head_branch": "feature/new-gateway", "base_branch": "main", "author": "backend-core"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "payments-service", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "payments-service", "issue_number": 12}),
            Action(name="create_issue", kwargs={"repo_name": "payments-service", "title": "Fix currency formatting for negative values", "body": ""}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-service", "branch": "fix/currency-format", "message": "fix: Handle negative currency values", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "payments-service", "title": "fix: Negative Currency", "body": "", "head_branch": "fix/currency-format", "base_branch": "main", "author": "backend-core"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "payments-service", "pr_number": 11, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "payments-service", "issue_number": 13}),
            Action(name="get_pull_request_merge_time_report", kwargs={"repo_name": "payments-service"}),
        ],
        outputs=[
            {
                "repo": "payments-service",
                "merged_pr_count": 2,
                "average_merge_time": 0,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_4003",
        instruction=(
            "Your mission is to execute the **Incident Triage Policy** for the 'infra-terraform' repository. A critical security alert has been triggered. "
            "The policy requires creating a main incident issue and a sub-task for the fix, implementing the fix, and ensuring all artifacts are correctly managed. "
            "You must use the provided **Incident Manifest** to create all required artifacts. "
            "Your final deliverable is a repository health summary to certify that the incident was fully resolved.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a new critical security alert was created and then marked as 'fixed'. A main incident issue and a sub-task issue for the fix must both be 'closed'. "
            "The fix must be implemented on a feature branch and merged via a pull request. This pull request must be linked to both the main incident issue and the sub-task issue.\n\n"
            "**Incident Manifest:**\n"
            "* **Alert Details:** {description: 'IAM role has excessive privileges', file: 'iam.tf'}\n"
            "* **Incident Issue:** {title: 'Incident: Overly permissive IAM role detected', body: ''}\n"
            "* **Fix-Task Issue:** {title: 'Task: Reduce IAM role permissions', body: ''}\n"
            "* **Ownership:** {assignee: 'ops-team', author: 'ops-team'}\n"
            "* **Code Artifacts:** {branch: 'fix/iam-permissions', commit_message: 'fix: Scope down IAM role to least privilege', pr_title: 'fix: Least Privilege for IAM Role', pr_body: ''}"
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "infra-terraform", "severity": "critical", "description": "IAM role has excessive privileges", "file": "iam.tf", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "infra-terraform", "title": "Incident: Overly permissive IAM role detected", "body": ""}),
            Action(name="create_issue", kwargs={"repo_name": "infra-terraform", "title": "Task: Reduce IAM role permissions", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 12, "assignees": ["ops-team"]}),
            Action(name="assign_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 13, "assignees": ["ops-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "infra-terraform", "branch": "fix/iam-permissions", "message": "fix: Scope down IAM role to least privilege", "author": "ops-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "infra-terraform", "title": "fix: Least Privilege for IAM Role", "body": "", "head_branch": "fix/iam-permissions", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "infra-terraform", "pr_number": 10, "issue_number": 12}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "infra-terraform", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "infra-terraform", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 12}),
            Action(name="close_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 13}),
            Action(name="fix_security_alert", kwargs={"repo_name": "infra-terraform", "alert_number": 10}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "infra-terraform"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_4005",
        instruction=(
            "Your mission is to execute the **Label-Based Issue Prioritization Policy** for the 'ui-kit' repository. A product manager needs to prepare the backlog for the next design sprint. "
            "The policy requires creating several new issues with different labels and then generating a report of only the design-related tasks. "
            "Your final deliverable is this filtered list of design issues.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that four new issues have been created and assigned. Two of these issues must have the 'design' label, one must have the 'bug' label, and one must have the 'enhancement' label. "
            "The issue labeled 'bug' must be fully resolved, including a merged pull request and its closure. The other three issues must remain open.\n\n"
            "**Data Specification:**\n"
            "* Design Issues: [{title: 'Redesign Card component shadows', assignee: 'design-lead', labels: ['design', 'ui']}, {title: 'Create new color palette for dark mode', assignee: 'design-lead', labels: ['design', 'theme']}]\n"
            "* Bug Issue: {title: 'Button click area is too small', assignee: 'ui-dev', labels: ['bug']}\n"
            "* Enhancement Issue: {title: 'Add new icon set for social media', assignee: 'ui-dev', labels: ['enhancement']}\n"
            "* Code Artifacts: {branch: 'fix/button-click-area', commit_message: 'fix: Increase padding on button component', pr_title: 'fix: Button click area'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Redesign Card component shadows", "body": "", "labels": ["design", "ui"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12, "assignees": ["design-lead"]}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Create new color palette for dark mode", "body": "", "labels": ["design", "theme"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 13, "assignees": ["design-lead"]}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Add new icon set for social media", "body": "", "labels": ["enhancement"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 14, "assignees": ["ui-dev"]}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Button click area is too small", "body": "", "labels": ["bug"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 15, "assignees": ["ui-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "fix/button-click-area", "message": "fix: Increase padding on button component", "author": "ui-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "fix: Button click area", "body": "", "head_branch": "fix/button-click-area", "base_branch": "main", "author": "ui-dev"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 15}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 15}),
            Action(name="list_issues_by_label", kwargs={"repo_name": "ui-kit", "label": "design"}),
        ],
        outputs=[
            [
                {
                    "issue_id": "ISSUE_ui-kit_2bb1b710",
                    "title": "Redesign Card component shadows",
                    "labels": ["design", "ui"],
                    "state": "open",
                    "report_date": "2025-08-26"
                },
                {
                    "issue_id": "ISSUE_ui-kit_e9e3e3d2",
                    "title": "Create new color palette for dark mode",
                    "labels": ["design", "theme"],
                    "state": "open",
                    "report_date": "2025-08-26"
                }
            ]
        ],
    ),
    Task(
        annotator="1",
        user_id="user_3001",
        instruction=(
            "Your mission is to execute the **Automated Security Rollback Policy** for the 'payments-service' repository. A new commit has introduced a critical vulnerability. "
            "The policy requires an immediate and full rollback of the change. Your final deliverable is an end-to-end report to certify that the repository is secure.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a new critical security alert was created and then marked as 'fixed'. A tracking issue for the incident must be 'closed'. "
            "The remediation must be completed by merging a pull request that effectively reverts the problematic commit.\n\n"
            "**Data Specification:**\n"
            "* Bad Commit Message: 'feat: Add new payment processor with RCE vulnerability'\n"
            "* Alert Details: {description: 'Remote Code Execution in new payment processor', file: 'src/payments.js'}\n"
            "* Incident Tracking: {issue_title: 'EMERGENCY: Revert critical RCE vulnerability', assignee: 'backend-core'}\n"
            "* Revert Artifacts: {branch: 'hotfix/revert-rce', commit_message: 'revert: Revert payment processor with RCE vulnerability', pr_title: 'hotfix: Revert RCE Vulnerability', reviewer: 'tech-lead-tara'}"
        ),
        actions=[
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-service", "branch": "main", "message": "feat: Add new payment processor with RCE vulnerability", "author": "backend-core"}),
            Action(name="create_security_alert", kwargs={"repo_name": "payments-service", "severity": "critical", "description": "Remote Code Execution in new payment processor", "file": "src/payments.js", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "payments-service", "title": "EMERGENCY: Revert critical RCE vulnerability", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "payments-service", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-service", "branch": "hotfix/revert-rce", "message": "revert: Revert payment processor with RCE vulnerability", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "payments-service", "title": "hotfix: Revert RCE Vulnerability", "body": "", "head_branch": "hotfix/revert-rce", "base_branch": "main", "author": "backend-core"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "payments-service", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "payments-service", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "payments-service", "issue_number": 12}),
            Action(name="fix_security_alert", kwargs={"repo_name": "payments-service", "alert_number": 10}),
            Action(name="generate_end_to_end_report", kwargs={"repo_name": "payments-service"}),
        ],
        outputs=[
            {
                "repo": "payments-service",
                "commits_count": 2,
                "open_issues": 0,
                "merged_prs": 1,
                "open_alerts": 0,
                "releases_count": 0,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_3002",
        instruction=(
            "Your mission is to execute the **Cross-Repo Incompatibility Policy**. A feature-in-progress in 'react-dashboard' has triggered a new high-severity alert due to an incompatibility with the current version of 'ui-kit'. "
            "The policy requires pausing the feature work, fixing the root cause in the dependency ('ui-kit'), and then resuming the feature work. Your final deliverable is a set of cross-entity reports for both repositories.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a new 'high' severity alert was created in 'react-dashboard' and later marked as 'fixed'. A tracking issue in 'ui-kit' must be 'closed' and its fix merged via a pull request. "
            "Subsequently, the original feature work in 'react-dashboard', also tracked by an issue, must be completed and merged via a separate pull request. All related issues must be closed.\n\n"
            "**Data Specification:**\n"
            "* `react-dashboard` Artifacts: {alert_description: 'Component crashing due to ui-kit incompatibility', alert_file: 'src/components/NewFeature.tsx', issue_title: 'Feature: New analytics chart', branch: 'feature/analytics-chart', initial_commit: 'feat: Initial analytics chart structure', final_commit: 'fix: Update component to support new ui-kit version'}\n"
            "* `ui-kit` Artifacts: {issue_title: 'Bug: Prop validation fails in Card component', branch: 'fix/prop-validation', commit_message: 'fix: Add backward compatibility for Card props', pr_title: 'fix: Prop validation'}"
        ),
        actions=[
            Action(name="add_commit_to_branch", kwargs={"repo_name": "react-dashboard", "branch": "feature/analytics-chart", "message": "feat: Initial analytics chart structure", "author": "frontend-dev"}),
            Action(name="create_security_alert", kwargs={"repo_name": "react-dashboard", "severity": "high", "description": "Component crashing due to ui-kit incompatibility", "file": "src/components/NewFeature.tsx", "branch": "feature/analytics-chart"}),
            Action(name="create_issue", kwargs={"repo_name": "react-dashboard", "title": "Feature: New analytics chart", "body": ""}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Bug: Prop validation fails in Card component", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 13, "assignees": ["ui-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "fix/prop-validation", "message": "fix: Add backward compatibility for Card props", "author": "ui-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "fix: Prop validation", "body": "", "head_branch": "fix/prop-validation", "base_branch": "main", "author": "ui-dev"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 13}),
            Action(name="assign_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 12, "assignees": ["frontend-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "react-dashboard", "branch": "feature/analytics-chart", "message": "fix: Update component to support new ui-kit version", "author": "frontend-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "react-dashboard", "title": "Feature: New analytics chart", "body": "", "head_branch": "feature/analytics-chart", "base_branch": "main", "author": "frontend-dev"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "react-dashboard", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 12}),
            Action(name="fix_security_alert", kwargs={"repo_name": "react-dashboard", "alert_number": 10}),
            Action(name="get_cross_entity_report", kwargs={"repo_name": "react-dashboard"}),
            Action(name="get_cross_entity_report", kwargs={"repo_name": "ui-kit"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_3003",
        instruction=(
            "Your mission is to execute the **Bug Triage and Audit Policy** for the 'acme-webapp' repository. A user has reported a critical bug that needs to be triaged into sub-tasks and resolved. "
            "The policy requires a clear audit trail from the initial report to the final merged code. Your final deliverable is an audit report mapping the fix commit to the pull request that delivered it.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a main epic issue was created to track the user report, and two sub-task issues (one for investigation, one for the fix) were also created and ultimately closed. "
            "The code fix must be implemented on a feature branch and merged via a pull request. This single pull request must be linked to all three issues (the epic and the two sub-tasks).\n\n"
            "**Data Specification:**\n"
            "* Epic Title: 'User Report: Login page not working on Safari'\n"
            "* Assignee for Epic: 'tech-lead-tara'\n"
            "* Sub-Task Titles: ['Investigate Safari-specific CSS issue', 'Fix CSS rendering bug on Safari']\n"
            "* Assignee for Sub-Tasks: 'alice-w'\n"
            "* Code Artifacts: {branch: 'bugfix/safari-css', commit_message: 'fix: Add vendor prefixes for Safari CSS compatibility', pr_title: 'fix: Safari CSS rendering', author: 'alice-w'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "User Report: Login page not working on Safari", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12, "assignees": ["tech-lead-tara"]}),
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "Investigate Safari-specific CSS issue", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 13, "assignees": ["alice-w"]}),
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "Fix CSS rendering bug on Safari", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 14, "assignees": ["alice-w"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "acme-webapp", "branch": "bugfix/safari-css", "message": "fix: Add vendor prefixes for Safari CSS compatibility", "author": "alice-w"}),
            Action(name="open_pull_request", kwargs={"repo_name": "acme-webapp", "title": "fix: Safari CSS rendering", "body": "", "head_branch": "bugfix/safari-css", "base_branch": "main", "author": "alice-w"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 10, "issue_number": 12}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 10, "issue_number": 13}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 10, "issue_number": 14}),
            Action(name="merge_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 13}),
            Action(name="close_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 14}),
            Action(name="close_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12}),
            Action(name="map_commits_to_pull_requests", kwargs={"repo_name": "acme-webapp"}),
        ],
        outputs=[
            [
                {
                    "pr_id": "PR_acme-webapp_e47660a5",
                    "commit_ids": [
                        "5a0cfd3926b4"
                    ],
                    "report_date": "2025-08-26"
                }
            ]
        ],
    ),
    Task(
        annotator="1",
        user_id="user_3005",
        instruction=(
            "Your mission is to execute the **Post-Incident Analysis Policy**. An incident in the 'infra-terraform' repository was recently resolved, and a report is required to audit the response timeline. "
            "Your final deliverable is an issue aging report to verify that the incident issue was resolved quickly.\n\n"
            "**Compliance Specification:**\n"
            "The final state of the repository must reflect the full lifecycle of an incident resolution. This includes the creation of a critical security alert, an issue to track the incident, a commit and pull request with the fix, the closure of the issue, and the fixing of the alert.\n\n"
            "**Data Specification:**\n"
            "* Alert: {description: 'S3 Bucket exposed publicly', file: 's3.tf', severity: 'critical'}\n"
            "* Issue Title: 'Incident: Public S3 Bucket Exposure'\n"
            "* Code Artifacts: {branch: 'hotfix/s3-policy', commit_message: 'fix: Apply private ACL to S3 bucket', pr_title: 'fix: Correct S3 bucket policy'}\n"
            "* Assignee/Author: 'ops-team'"
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "infra-terraform", "severity": "critical", "description": "S3 Bucket exposed publicly", "file": "s3.tf", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "infra-terraform", "title": "Incident: Public S3 Bucket Exposure", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 12, "assignees": ["ops-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "infra-terraform", "branch": "hotfix/s3-policy", "message": "fix: Apply private ACL to S3 bucket", "author": "ops-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "infra-terraform", "title": "fix: Correct S3 bucket policy", "body": "", "head_branch": "hotfix/s3-policy", "base_branch": "main", "author": "ops-team"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "infra-terraform", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "infra-terraform", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "infra-terraform", "issue_number": 12}),
            Action(name="fix_security_alert", kwargs={"repo_name": "infra-terraform", "alert_number": 10}),
            Action(name="get_issue_aging_report", kwargs={"repo_name": "infra-terraform"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_2001",
        instruction=(
            "Your mission is to execute the **Multi-Stage Feature Rollout Policy**. A new feature in 'flutter-finance-app' requires an updated dependency from 'utils-js'. "
            "The policy requires that both the dependency is updated and the new feature is integrated, with the final application deployed to a 'staging-android' environment and formally released. "
            "Your final deliverable is a list of commits for the 'flutter-finance-app' repository to audit the changes.\n\n"
            "**Compliance Specification:**\n"
            "The final state of the ecosystem must reflect the completion of this work across both repositories. All related tracking issues must be closed, all pull requests merged, and new versions for both repositories must be released. The final application must be deployed to the specified staging environment.\n\n"
            "**Data Specification:**\n"
            "* `utils-js` Artifacts: {issue_title: 'Add new array utility function', branch: 'feature/array-util', commit_message: 'feat: Add advanced array sorting utility', pr_title: 'feat: Add array utility', release_version: 'v1.1.0', release_description: 'Adds new array utilities.'}\n"
            "* `flutter-finance-app` Artifacts: {issue_title: 'Integrate new array utility from utils-js', branch: 'feature/new-integration', commit_message: 'feat: Integrate utils-js v1.1.0 for improved performance', pr_title: 'feat: Integrate new utils', release_version: 'v1.3.0', release_description: 'Integrates new dependency for performance improvements.'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "utils-js", "title": "Add new array utility function", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "utils-js", "issue_number": 12, "assignees": ["bob-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "utils-js", "branch": "feature/array-util", "message": "feat: Add advanced array sorting utility", "author": "bob-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "utils-js", "title": "feat: Add array utility", "body": "", "head_branch": "feature/array-util", "base_branch": "master", "author": "bob-dev"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "utils-js", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "utils-js", "issue_number": 12}),
            Action(name="create_release", kwargs={"repo_name": "utils-js", "version": "v1.1.0", "description": "Adds new array utilities."}),
            Action(name="create_issue", kwargs={"repo_name": "flutter-finance-app", "title": "Integrate new array utility from utils-js", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "flutter-finance-app", "issue_number": 13, "assignees": ["mobile-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "flutter-finance-app", "branch": "feature/new-integration", "message": "feat: Integrate utils-js v1.1.0 for improved performance", "author": "mobile-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "flutter-finance-app", "title": "feat: Integrate new utils", "body": "", "head_branch": "feature/new-integration", "base_branch": "main", "author": "mobile-dev"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "flutter-finance-app", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "flutter-finance-app", "issue_number": 13}),
            Action(name="register_deploy_event", kwargs={"repo_name": "flutter-finance-app", "environment": "staging-android"}),
            Action(name="create_release", kwargs={"repo_name": "flutter-finance-app", "version": "v1.3.0", "description": "Integrates new dependency for performance improvements."}),
            Action(name="list_commits_by_date_range", kwargs={"repo_name": "flutter-finance-app", "start_date": "2025-08-26", "end_date": "2025-08-26"}),
        ],
        outputs=[
            [
                {
                    "commit_id": "387ef3422d8f",
                    "repo": "flutter-finance-app",
                    "message": "feat: Integrate utils-js v1.1.0 for improved performance",
                    "author": "mobile-dev",
                    "timestamp": "2025-08-26",
                    "report_date": "2025-08-26"
                }
            ]
        ],
    ),
    Task(
        annotator="1",
        user_id="user_2002",
        instruction=(
            "Your mission is to execute the **Cross-Team Bug Triage Policy**. A critical bug reported in 'payments-service' has been traced back to an underlying issue in a dependency, 'acme-webapp'. "
            "The policy requires a coordinated fix, starting with the dependency. You must ensure the final state of both repositories complies with the **Triage Specification**. "
            "Your final deliverable is a set of cross-entity reports for both repositories to provide a full summary of the resolution.\n\n"
            "**Triage Specification:**\n"
            "The final state must show that the root cause in 'acme-webapp' was tracked and resolved first, which includes closing an issue and merging a pull request with the hotfix. "
            "Subsequently, the 'payments-service' must be updated to use this fixed version, a process which must also be tracked via a closed issue and a merged pull request.\n\n"
            "**Data Specification:**\n"
            "* `payments-service` Artifacts: {issue_title: 'Bug: Transaction processing fails for certain card types', pr_title: 'chore: Update dependency to acme-webapp', branch: 'fix/dependency-update', commit_message: 'chore: Update acme-webapp to latest version', author: 'backend-core', assignee: 'backend-core'}\n"
            "* `acme-webapp` Artifacts: {issue_title: 'Hotfix: Null pointer exception in input handler', pr_title: 'fix: Null pointer in handler', branch: 'hotfix/null-pointer', commit_message: 'fix: Add null check to input handler', author: 'alice-w', assignee: 'alice-w'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "payments-service", "title": "Bug: Transaction processing fails for certain card types", "body": ""}),
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "Hotfix: Null pointer exception in input handler", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 13, "assignees": ["alice-w"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "acme-webapp", "branch": "hotfix/null-pointer", "message": "fix: Add null check to input handler", "author": "alice-w"}),
            Action(name="open_pull_request", kwargs={"repo_name": "acme-webapp", "title": "fix: Null pointer in handler", "body": "", "head_branch": "hotfix/null-pointer", "base_branch": "main", "author": "alice-w"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 13}),
            Action(name="assign_issue", kwargs={"repo_name": "payments-service", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-service", "branch": "fix/dependency-update", "message": "chore: Update acme-webapp to latest version", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "payments-service", "title": "chore: Update dependency to acme-webapp", "body": "", "head_branch": "fix/dependency-update", "base_branch": "main", "author": "backend-core"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "payments-service", "pr_number": 11, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "payments-service", "issue_number": 12}),
            Action(name="get_cross_entity_report", kwargs={"repo_name": "acme-webapp"}),
            Action(name="get_cross_entity_report", kwargs={"repo_name": "payments-service"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_2005",
        instruction=(
            "Your mission is to execute the **Repository Health Remediation Policy**. The 'security-scanner' repository has been identified as "
            "requiring a remediation plan to address known architectural issues. The policy requires that a formal plan is created and tracked. "
            "Your final deliverable is a list of open issues for the repository to confirm that the remediation plan has been correctly initiated.\n\n"
            "**Compliance Specification:**\n"
            "The final state must show that a new epic issue was created to track the overall remediation plan. Two new sub-task issues must also be created "
            "to address the top two existing problems. All three new issues must be left open and assigned to the appropriate team lead.\n\n"
            "**Data Specification:**\n"
            "* Target Repository: 'security-scanner'\n"
            "* Team Lead: 'security-team'\n"
            "* Epic Title: 'Q3 Remediation Plan for security-scanner'\n"
            "* Sub-Task Titles: ['Address high false-positive rate for XSS detection', 'Improve performance for large codebases']"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Q3 Remediation Plan for security-scanner", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["security-team"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Address high false-positive rate for XSS detection", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["security-team"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Improve performance for large codebases", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 14, "assignees": ["security-team"]}),
            Action(name="get_open_issues", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
            [
                {
                    "issue_id": "ISSUE_security-scanner_ed799e7d",
                    "title": "Q3 Remediation Plan for security-scanner",
                    "state": "open",
                    "assignees": ["security-team"],
                    "labels": [],
                    "created_at": "2025-08-26",
                    "report_date": "2025-08-26"
                },
                {
                    "issue_id": "ISSUE_security-scanner_7636a0bb",
                    "title": "Address high false-positive rate for XSS detection",
                    "state": "open",
                    "assignees": ["security-team"],
                    "labels": [],
                    "created_at": "2025-08-26",
                    "report_date": "2025-08-26"
                },
                {
                    "issue_id": "ISSUE_security-scanner_292c349e",
                    "title": "Improve performance for large codebases",
                    "state": "open",
                    "assignees": ["security-team"],
                    "labels": [],
                    "created_at": "2025-08-26",
                    "report_date": "2025-08-26"
                }
            ]
        ],
    ),
    Task(
        annotator="1",
        user_id="user_1002",
        instruction=(
            "Your mission is to execute the **Code Cleanup and Deprecation Policy** for the 'utils-js' repository. The goal is to remove the "
            "deprecated 'formatCurrency' function from the codebase. The final state of the repository must reflect that this deprecation work "
            "was formally tracked and completed through the standard development lifecycle of issues and pull requests. Your final deliverable is "
            "the repository's risk score to certify that the cleanup was successful."
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "utils-js", "title": "Deprecate formatCurrency in src/utils/format.js", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "utils-js", "issue_number": 12, "assignees": ["intern-sarah"]}),
            Action(name="create_issue", kwargs={"repo_name": "utils-js", "title": "Remove formatCurrency test in test/format.test.js", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "utils-js", "issue_number": 13, "assignees": ["intern-sarah"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "utils-js", "branch": "refactor/remove-currency-func", "message": "refactor: Remove deprecated formatCurrency function", "author": "intern-sarah"}),
            Action(name="open_pull_request", kwargs={"repo_name": "utils-js", "title": "refactor: Remove formatCurrency", "body": "", "head_branch": "refactor/remove-currency-func", "base_branch": "master", "author": "intern-sarah"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "utils-js", "pr_number": 10, "issue_number": 12}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "utils-js", "pr_number": 10, "issue_number": 13}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "utils-js", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "utils-js", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "utils-js", "issue_number": 12}),
            Action(name="close_issue", kwargs={"repo_name": "utils-js", "issue_number": 13}),
            Action(name="get_repository_risk_score", kwargs={"repo_name": "utils-js"}),
        ],
        outputs=[
            {
                "repo": "utils-js",
                "open_alerts_count": 0,
                "risk_score": 0,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_1004",
        instruction=(
            "Your mission is to execute the **Model Drift Retraining Policy** for the 'ml-pipeline' repository. This policy is invoked when a "
            "production model shows performance degradation. You must ensure the repository's state complies with the **Retraining Specification**, "
            "which includes updating the model, releasing a new version, and deploying it. Your final deliverable is the issue aging report to "
            "confirm that the incident was tracked and resolved swiftly.\n\n"
            "**Retraining Specification:**\n"
            "The policy requires that an incident be tracked via an issue, which must be closed upon resolution. A code fix containing the updated model parameters must be implemented on a feature branch and merged via a pull request. A new hotfix version of the model must be released and its deployment to the 'production-model-serving' environment must be registered.\n\n"
            "**Data Specification:**\n"
            "* Issue Title: 'Incident: Model performance degraded in production'\n"
            "* Assignee/Author: 'data-scientist'\n"
            "* Code Artifacts: {branch: 'hotfix/retrain-model', commit_message: 'refactor: Update model with new training data', pr_title: 'fix: Retrain production model'}\n"
            "* Release Details: {version: 'v1.3.1', description: 'Hotfix release with retrained model.'}"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "ml-pipeline", "title": "Incident: Model performance degraded in production", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "ml-pipeline", "issue_number": 12, "assignees": ["data-scientist"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ml-pipeline", "branch": "hotfix/retrain-model", "message": "refactor: Update model with new training data", "author": "data-scientist"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ml-pipeline", "title": "fix: Retrain production model", "body": "", "head_branch": "hotfix/retrain-model", "base_branch": "main", "author": "data-scientist"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ml-pipeline", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ml-pipeline", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ml-pipeline", "issue_number": 12}),
            Action(name="create_release", kwargs={"repo_name": "ml-pipeline", "version": "v1.3.1", "description": "Hotfix release with retrained model."}),
            Action(name="register_deploy_event", kwargs={"repo_name": "ml-pipeline", "environment": "production-model-serving"}),
            Action(name="get_issue_aging_report", kwargs={"repo_name": "ml-pipeline"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_901",
        instruction=(
            "Your primary mission is to execute the **Security Incident Response and Hardening Policy**, triggered by a newly discovered vulnerability. "
            "Your objective is to ensure the incident is fully remediated and preventative measures are implemented, bringing both the 'payments-service' "
            "and 'security-scanner' repositories into compliance with the official **Incident Hardening Specification**. Your final deliverable is a "
            "set of health summaries for both repositories to certify that the policy was successfully executed.\n\n"
            "**Incident Hardening Specification:**\n"
            "The policy requires that the identified vulnerability in 'payments-service' is fully patched and a corresponding hotfix is released. Concurrently, the 'security-scanner' must be upgraded with new detection rules for this vulnerability class and receive a new version release. All remediation and enhancement work must be tracked through issues and pull requests, which must be closed and merged respectively. The initial security alert must be marked as fixed.\n\n"
            "**Data Specification:**\n"
            "* Vulnerability Details: {description: 'Remote Code Execution via deserialization', file: 'src/server.ts'}\n"
            "* `payments-service` Artifacts: {issue_title: 'Patch Critical RCE Vulnerability', pr_title: 'fix: Patch RCE vulnerability in deserialization module', branch: 'hotfix/rce-patch', release_version: 'v0.2.1', release_description: 'Security patch for critical RCE vulnerability.', assignee: 'backend-core'}\n"
            "* `security-scanner` Artifacts: {issue_title: 'Enhance scanner with RCE detection rule', pr_title: 'feat: Add deserialization RCE detection rule', branch: 'feature/rce-detection', release_version: 'v0.7.0', release_description: 'Adds detection for deserialization-based RCE.', assignee: 'security-team'}"
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "payments-service", "severity": "critical", "description": "Remote Code Execution via deserialization", "file": "src/server.ts", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Enhance scanner with RCE detection rule", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "feature/rce-detection", "message": "feat: Add deserialization RCE detection rule", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "feat: Add deserialization RCE detection rule", "body": "", "head_branch": "feature/rce-detection", "base_branch": "main"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12}),
            Action(name="create_release", kwargs={"repo_name": "security-scanner", "version": "v0.7.0", "description": "Adds detection for deserialization-based RCE."}),
            Action(name="create_issue", kwargs={"repo_name": "payments-service", "title": "Patch Critical RCE Vulnerability", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "payments-service", "issue_number": 13, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "payments-service", "branch": "hotfix/rce-patch", "message": "fix: Patch RCE vulnerability in deserialization module", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "payments-service", "title": "fix: Patch RCE vulnerability in deserialization module", "body": "", "head_branch": "hotfix/rce-patch", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "payments-service", "pr_number": 11, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "payments-service", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "payments-service", "issue_number": 13}),
            Action(name="fix_security_alert", kwargs={"repo_name": "payments-service", "alert_number": 10}),
            Action(name="create_release", kwargs={"repo_name": "payments-service", "version": "v0.2.1", "description": "Security patch for critical RCE vulnerability."}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "payments-service"}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_902",
        instruction=(
            "Your primary role is to execute the **New Service Onboarding with Dependency Integration Policy**. This policy is invoked when a new "
            "service, 'recommendation-engine', requires a change in an existing shared service, 'security-scanner', to function correctly. You must govern the "
            "entire lifecycle for both repositories, ensuring their final states comply with the official **Cross-Repo Integration Specification**. "
            "Your final deliverable is a list containing the health summaries for both repositories to confirm a successful and clean integration.\n\n"
            "**Cross-Repo Integration Specification:**\n"
            "* **'security-scanner' Final State:** A tracking issue for adding custom rules for the new service must be closed. The corresponding pull request from a feature branch must be merged. A new release 'v0.6.0' with the description 'Adds support for recommendation-engine.' must be published.\n"
            "* **'recommendation-engine' Final State:** The repository must be created as 'private' with the description 'Collaborative filtering recommendation engine.'. A tracking issue for the initial model implementation must be closed, and its corresponding pull request from a feature branch must be merged. The merged code must contain commits for both the initial model structure and the integration with the updated 'security-scanner'."
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "recommendation-engine", "description": "Collaborative filtering recommendation engine.", "private": True}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Add custom rules for recommendation-engine", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "feature/reco-engine-rules", "message": "feat: Add custom security rules for new recommendation engine", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "feat: Add recommendation-engine security rules", "body": "", "head_branch": "feature/reco-engine-rules", "base_branch": "main"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12}),
            Action(name="create_release", kwargs={"repo_name": "security-scanner", "version": "v0.6.0", "description": "Adds support for recommendation-engine."}),
            Action(name="create_issue", kwargs={"repo_name": "recommendation-engine", "title": "Implement initial collaborative filtering model", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "recommendation-engine", "issue_number": 13, "assignees": ["data-scientist"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "recommendation-engine", "branch": "feature/collab-filter", "message": "feat: Add initial model structure", "author": "data-scientist"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "recommendation-engine", "branch": "feature/collab-filter", "message": "refactor: Integrate with security-scanner v0.6.0", "author": "data-scientist"}),
            Action(name="open_pull_request", kwargs={"repo_name": "recommendation-engine", "title": "feat: Initial collaborative filtering model", "body": "", "head_branch": "feature/collab-filter", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "recommendation-engine", "pr_number": 11, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "recommendation-engine", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "recommendation-engine", "issue_number": 13}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "recommendation-engine"}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_903",
        instruction=(
            "Your primary strategic objective is to execute the **Quarterly Security Backlog Drive Policy** for the 'security-scanner' repository. "
            "This policy mandates a tiered remediation approach based on vulnerability severity. You are responsible for bringing the repository "
            "to a state that reflects this tiered response, as defined by the official **Backlog Drive Compliance Specification**. Your "
            "final deliverable is the repository's activity dashboard to confirm the policy was successfully executed.\n\n"
            "**Backlog Drive Compliance Specification:**\n"
            "* **Tracking Artifacts:** The final state must include an 'open' epic issue titled 'Q3 Security Backlog Drive', assigned to 'tech-lead-tara'.\n"
            "* **Critical Vulnerability:** The repository must show that a new critical alert for 'Improper Input Validation' in 'src/api.rs' has been fully remediated. This requires its tracking issue ('Fix Critical: Improper Input Validation') to be 'closed' and its associated pull request ('fix: Add strict input validation') from branch 'fix/input-validation' to be 'merged'.\n"
            "* **High Vulnerability:** A new high-severity alert for 'Hardcoded Secret' in 'src/config.rs' must have remediation in progress. This requires an 'open' tracking issue ('Remediate High: Hardcoded Secret') and an 'open' pull request ('WIP: Remove hardcoded secret') from branch 'fix/hardcoded-secret'.\n"
            "* **Medium Vulnerability:** A new medium-severity alert for 'Verbose Error Messages' in 'src/errors.rs' must be tracked. This requires an 'open' tracking issue ('Track Medium: Verbose Error Messages') assigned to 'intern-sarah'."
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Q3 Security Backlog Drive", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["tech-lead-tara"]}),
            Action(name="create_security_alert", kwargs={"repo_name": "security-scanner", "severity": "critical", "description": "Improper Input Validation", "file": "src/api.rs", "branch": "main"}),
            Action(name="create_security_alert", kwargs={"repo_name": "security-scanner", "severity": "high", "description": "Hardcoded Secret", "file": "src/config.rs", "branch": "main"}),
            Action(name="create_security_alert", kwargs={"repo_name": "security-scanner", "severity": "medium", "description": "Verbose Error Messages", "file": "src/errors.rs", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Fix Critical: Improper Input Validation", "body": ""}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "fix/input-validation", "message": "fix: Add strict input validation", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "fix: Add strict input validation", "body": "", "head_branch": "fix/input-validation", "base_branch": "main"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13}),
            Action(name="fix_security_alert", kwargs={"repo_name": "security-scanner", "alert_number": 10}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Remediate High: Hardcoded Secret", "body": ""}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "fix/hardcoded-secret", "message": "WIP: Remove hardcoded secret", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "WIP: Remove hardcoded secret", "body": "", "head_branch": "fix/hardcoded-secret", "base_branch": "main"}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 11, "reviewers": ["tech-lead-tara"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Track Medium: Verbose Error Messages", "body": ""}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 15, "assignees": ["intern-sarah"]}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
            {
                "repo": "security-scanner",
                "commits_count": 2,
                "open_issues": 3,
                "open_prs": 1,
                "open_alerts_by_severity": {"critical": 0, "high": 1, "medium": 1, "low": 0, "unknown": 0},
                "open_alerts": 2,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_904",
        instruction=(
            "Your primary objective is to execute the **Service Sunset Policy** for a new repository named 'legacy-api'. This policy governs the orderly "
            "decommissioning of a service, ensuring all tracking artifacts are correctly managed and a final version is released. You are responsible for "
            "bringing the repository's state into compliance with the official **Sunset Compliance Specification**. Your final deliverable is the "
            "repository's health summary to confirm a clean shutdown with no open items.\n\n"
            "**Sunset Compliance Specification:**\n"
            "* **Required Repository State:**\n"
            "    * A 'private' repository must exist with the description: 'Legacy API for sunsetting.'\n"
            "* **Required State of Tracking Artifacts:**\n"
            "    * A main epic issue titled 'Epic: Sunset Legacy API', assigned to 'tech-lead-tara', must be in a 'closed' state.\n"
            "    * A tracking issue titled 'Task: Add deprecation notice to API', assigned to 'backend-core', must be in a 'closed' state.\n"
            "* **Required State of Code and Releases:**\n"
            "    * A pull request titled 'feat: Add deprecation notice' from the 'feature/deprecation-notice' branch must be 'merged'. This PR must be linked to the 'Task: Add deprecation notice to API' issue.\n"
            "    * A final, stable release 'v2.0.0' with the description 'Final release with deprecation notice.' must be published."
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "legacy-api", "description": "Legacy API for sunsetting.", "private": True}),
            Action(name="create_issue", kwargs={"repo_name": "legacy-api", "title": "Epic: Sunset Legacy API", "body": "", "labels": ["epic", "deprecation"]}),
            Action(name="assign_issue", kwargs={"repo_name": "legacy-api", "issue_number": 12, "assignees": ["tech-lead-tara"]}),
            Action(name="create_issue", kwargs={"repo_name": "legacy-api", "title": "Task: Add deprecation notice to API", "body": "", "labels": ["task"]}),
            Action(name="assign_issue", kwargs={"repo_name": "legacy-api", "issue_number": 13, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "legacy-api", "branch": "feature/deprecation-notice", "message": "feat: Add deprecation notice", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "legacy-api", "title": "feat: Add deprecation notice", "body": "", "head_branch": "feature/deprecation-notice", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "legacy-api", "pr_number": 10, "issue_number": 13}),
            Action(name="merge_pull_request", kwargs={"repo_name": "legacy-api", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "legacy-api", "issue_number": 13}),
            Action(name="close_issue", kwargs={"repo_name": "legacy-api", "issue_number": 12}),
            Action(name="create_release", kwargs={"repo_name": "legacy-api", "version": "v2.0.0", "description": "Final release with deprecation notice."}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "legacy-api"}),
        ],
        outputs=[
            {
                "repo": "legacy-api",
                "open_issues": 0,
                "open_prs": 0,
                "open_alerts": 0,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_801",
        instruction=(
            "Your primary strategic objective is to govern the setup of a new hire's first project, ensuring it fully aligns with the company's "
            "**New Hire Onboarding Policy**. This policy mandates that a dedicated starter repository is created with a structured set of "
            "onboarding tasks. You are responsible for ensuring the new repository's final state perfectly matches the official "
            "**Onboarding Compliance Specification** detailed below. Your final deliverable is the repository's activity dashboard, which "
            "will serve as the official record of policy compliance.\n\n"
            "**Onboarding Compliance Specification for 'new-hire-starter-project':**\n"
            "* **Required Repository State:**\n"
            "    * Must be 'private' with description: 'Starter project for new engineering hires.'\n"
            "* **Required State of Onboarding Issues:**\n"
            "    * A main epic titled 'Onboarding Plan for new hire' (body: 'Main epic to track the new hire onboarding process.', "
            "labels: ['onboarding', 'epic'], assigned to 'intern-sarah') must be 'open'.\n"
            "    * A sub-task titled 'Task 1: Set up local development environment' (body: 'Sub-task to track local environment setup.', "
            "labels: ['onboarding', 'setup'], assigned to 'intern-sarah') must be 'open'.\n"
            "    * A sub-task titled 'Task 2: Complete first coding task' (body: 'Sub-task for the first coding assignment.', "
            "labels: ['onboarding', 'coding-task'], assigned to 'intern-sarah') must be 'closed'.\n"
            "    * A sub-task titled 'Task 3: Schedule team introduction meetings' (body: 'Sub-task to schedule introductory meetings.', "
            "labels: ['onboarding', 'meetings'], assigned to 'intern-sarah') must be 'open'.\n"
            "* **Required State of First Coding Task:**\n"
            "    * A pull request titled 'feat: Add welcome message endpoint' (body: 'PR for the first coding task, implementing the /hello endpoint.', "
            "reviewed by ['tech-lead-tara']) must be 'merged' into 'main', linked to the coding task issue, and contain a commit "
            "'feat: Implement /hello endpoint' by 'intern-sarah' from the 'feature/welcome-endpoint' branch."
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "new-hire-starter-project", "description": "Starter project for new engineering hires.", "private": True}),
            Action(name="create_issue", kwargs={"repo_name": "new-hire-starter-project", "title": "Onboarding Plan for new hire", "body": "Main epic to track the new hire onboarding process.", "labels": ["onboarding", "epic"]}),
            Action(name="assign_issue", kwargs={"repo_name": "new-hire-starter-project", "issue_number": 12, "assignees": ["intern-sarah"]}),
            Action(name="create_issue", kwargs={"repo_name": "new-hire-starter-project", "title": "Task 1: Set up local development environment", "body": "Sub-task to track local environment setup.", "labels": ["onboarding", "setup"]}),
            Action(name="assign_issue", kwargs={"repo_name": "new-hire-starter-project", "issue_number": 13, "assignees": ["intern-sarah"]}),
            Action(name="create_issue", kwargs={"repo_name": "new-hire-starter-project", "title": "Task 2: Complete first coding task", "body": "Sub-task for the first coding assignment.", "labels": ["onboarding", "coding-task"]}),
            Action(name="assign_issue", kwargs={"repo_name": "new-hire-starter-project", "issue_number": 14, "assignees": ["intern-sarah"]}),
            Action(name="create_issue", kwargs={"repo_name": "new-hire-starter-project", "title": "Task 3: Schedule team introduction meetings", "body": "Sub-task to schedule introductory meetings.", "labels": ["onboarding", "meetings"]}),
            Action(name="assign_issue", kwargs={"repo_name": "new-hire-starter-project", "issue_number": 15, "assignees": ["intern-sarah"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "new-hire-starter-project", "branch": "feature/welcome-endpoint", "message": "feat: Implement /hello endpoint", "author": "intern-sarah"}),
            Action(name="open_pull_request", kwargs={"repo_name": "new-hire-starter-project", "title": "feat: Add welcome message endpoint", "body": "PR for the first coding task, implementing the /hello endpoint.", "head_branch": "feature/welcome-endpoint", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "new-hire-starter-project", "pr_number": 10, "issue_number": 14}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "new-hire-starter-project", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "new-hire-starter-project", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "new-hire-starter-project", "issue_number": 14}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "new-hire-starter-project"}),
        ],
        outputs=[
            {
                "repo": "new-hire-starter-project",
                "commits_count": 1,
                "open_issues": 3,
                "open_prs": 0,
                "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                "open_alerts": 0,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_802",
        instruction=(
            "Your primary strategic objective is to govern the **Secure Development Lifecycle (SDL) Policy** for the 'ui-kit' repository. This "
            "policy mandates that all development work, especially that which triggers security concerns, follows a strict, auditable remediation "
            "and approval process. A new feature has triggered a critical security alert, and you are responsible for ensuring the repository's "
            "final state reflects a compliant resolution, as defined by the official **SDL Compliance Specification** below. Your final deliverable "
            "is the repository activity dashboard, which will serve as the official record of policy compliance.\n\n"
            "**SDL Compliance Specification for Data Export Feature:**\n"
            "* **Required State of Feature Development:**\n"
            "    * A main feature issue titled 'Add new Data Export component' (body: 'Main tracking issue for the Data Export feature.', "
            "labels: ['feature'], assigned to 'ui-dev') must be 'closed'.\n"
            "* **Required State of Security Remediation:**\n"
            "    * A 'critical' alert for 'Data Export component leaks PII' on file 'src/export.js' must be 'fixed'.\n"
            "    * A security issue titled 'CRITICAL: Fix PII leak in Data Export PR' (body: 'Tracking issue for the PII leak discovered in "
            "the Data Export PR.', labels: ['security', 'bug'], assigned to 'security-team') must be 'closed'.\n"
            "* **Required State of Codebase:**\n"
            "    * A pull request titled 'feat: Add new Data Export component' (body: 'PR for the new Data Export component with PII leak "
            "remediation.', reviewed by ['security-team']) must be 'merged' and linked to both the feature and security tracking issues.\n"
            "    * The merged PR must contain both the initial feature commit ('feat: Add initial data export component') and the subsequent "
            "remediation commit ('fix: Sanitize user data in export component')."
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Add new Data Export component", "body": "Main tracking issue for the Data Export feature.", "labels": ["feature"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12, "assignees": ["ui-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/data-export", "message": "feat: Add initial data export component", "author": "ui-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "feat: Add new Data Export component", "body": "PR for the new Data Export component with PII leak remediation.", "head_branch": "feature/data-export", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 12}),
            Action(name="create_security_alert", kwargs={"repo_name": "ui-kit", "severity": "critical", "description": "Data Export component leaks PII", "file": "src/export.js", "branch": "feature/data-export"}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "CRITICAL: Fix PII leak in Data Export PR", "body": "Tracking issue for the PII leak discovered in the Data Export PR.", "labels": ["security", "bug"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 13, "assignees": ["security-team"]}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 13}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/data-export", "message": "fix: Sanitize user data in export component", "author": "security-team"}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "ui-kit", "pr_number": 10, "reviewers": ["security-team"]}),
            Action(name="fix_security_alert", kwargs={"repo_name": "ui-kit", "alert_number": 10}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 13}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "ui-kit"}),
        ],
        outputs=[
            {
                "repo": "ui-kit",
                "commits_count": 2,
                "open_issues": 0,
                "open_prs": 0,
                "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                "open_alerts": 0,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_803",
        instruction=(
            "Your primary strategic objective is to execute the **Release Failure and Hotfix Protocol** for the new 'mission-critical-service'. This protocol "
            "is invoked when a production release introduces a critical regression, requiring an immediate rollback and a subsequent hotfix. You are "
            "responsible for ensuring the repository's final state perfectly matches the official **Incident Response Compliance Specification**, "
            "detailed below. Your final deliverable is the repository's health summary to confirm the service is stable on the new hotfix version.\n\n"
            "**Incident Response Compliance Specification for mission-critical-service:**\n"
            "* **Required Repository State:**\n"
            "    * Must be a 'private' repository with description: 'A new mission critical service for core business operations.'\n"
            "* **Required State of Releases & Deployments:**\n"
            "    * A stable release 'v1.0.0' (desc: 'Stable release.') must be published, containing a commit with message 'feat: Initial implementation for v1.0.0', and its deployment to 'production-v1.0' registered.\n"
            "    * A faulty release 'v1.1.0' (desc: 'Faulty release.') must be published, containing a commit with message 'feat: New feature with data corruption bug', and its deployment to 'production-v1.1' registered.\n"
            "    * A rollback deployment to 'production-v1.0-rollback' must be registered to mitigate the incident.\n"
            "    * A final hotfix release 'v1.1.1' (desc: 'Hotfix release.') must be published and its final deployment to 'production-v1.1.1' registered.\n"
            "* **Required State of Incident Tracking:**\n"
            "    * A 'critical' alert for 'v1.1.0 deployment caused data corruption' in file 'src/db.js' must be 'fixed'.\n"
            "    * An emergency issue titled 'EMERGENCY: Rollback v1.1.0' (body: 'Emergency issue to track the rollback of v1.1.0.', labels: ['incident']) must be 'closed'.\n"
            "    * A hotfix issue titled 'Hotfix for v1.1.1' (body: 'Issue to track the development of the v1.1.1 hotfix.', labels: ['hotfix']) must be 'closed', "
            "tracking a 'merged' PR titled 'fix: Hotfix for v1.1.1' (body: 'PR for the v1.1.1 hotfix.') from branch 'hotfix/v1.1.1' with the commit "
            "'fix: Add data migration script and patch corruption bug'."
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "mission-critical-service", "description": "A new mission critical service for core business operations.", "private": True}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "mission-critical-service", "branch": "main", "message": "feat: Initial implementation for v1.0.0", "author": "backend-core"}),
            Action(name="create_release", kwargs={"repo_name": "mission-critical-service", "version": "v1.0.0", "description": "Stable release."}),
            Action(name="register_deploy_event", kwargs={"repo_name": "mission-critical-service", "environment": "production-v1.0"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "mission-critical-service", "branch": "main", "message": "feat: New feature with data corruption bug", "author": "backend-core"}),
            Action(name="create_release", kwargs={"repo_name": "mission-critical-service", "version": "v1.1.0", "description": "Faulty release."}),
            Action(name="register_deploy_event", kwargs={"repo_name": "mission-critical-service", "environment": "production-v1.1"}),
            Action(name="create_security_alert", kwargs={"repo_name": "mission-critical-service", "severity": "critical", "description": "v1.1.0 deployment caused data corruption", "file": "src/db.js", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "mission-critical-service", "title": "EMERGENCY: Rollback v1.1.0", "body": "Emergency issue to track the rollback of v1.1.0.", "labels": ["incident"]}),
            Action(name="register_deploy_event", kwargs={"repo_name": "mission-critical-service", "environment": "production-v1.0-rollback"}),
            Action(name="close_issue", kwargs={"repo_name": "mission-critical-service", "issue_number": 12}),
            Action(name="create_issue", kwargs={"repo_name": "mission-critical-service", "title": "Hotfix for v1.1.1", "body": "Issue to track the development of the v1.1.1 hotfix.", "labels": ["hotfix"]}),
            Action(name="assign_issue", kwargs={"repo_name": "mission-critical-service", "issue_number": 13, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "mission-critical-service", "branch": "hotfix/v1.1.1", "message": "fix: Add data migration script and patch corruption bug", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "mission-critical-service", "title": "fix: Hotfix for v1.1.1", "body": "PR for the v1.1.1 hotfix.", "head_branch": "hotfix/v1.1.1", "base_branch": "main"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "mission-critical-service", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "mission-critical-service", "issue_number": 13}),
            Action(name="fix_security_alert", kwargs={"repo_name": "mission-critical-service", "alert_number": 10}),
            Action(name="create_release", kwargs={"repo_name": "mission-critical-service", "version": "v1.1.1", "description": "Hotfix release."}),
            Action(name="register_deploy_event", kwargs={"repo_name": "mission-critical-service", "environment": "production-v1.1.1"}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "mission-critical-service"}),
        ],
        outputs=[
            {
                "repo": "mission-critical-service",
                "open_issues": 0,
                "open_prs": 0,
                "open_alerts": 0,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_805",
        instruction=(
            "Your primary role is to govern the **External Contribution Management Policy** for the public 'ui-kit' repository. This policy "
            "requires that contributions from external users are tracked by a parallel internal issue and that internal developers add any "
            "necessary adjustments or tests before merging. You must bring the repository to a state that conforms to the **External "
            "Contribution Compliance Specification** below. Your final deliverable is a set of reports—the repository's activity dashboard "
            "and a team contribution stats report—to confirm that the contribution has been successfully integrated and to verify the work "
            "distribution between external and internal authors.\n\n"
            "**External Contribution Compliance Specification:**\n"
            "* **Required State of Tracking Artifacts (all 'closed'):**\n"
            "    * An external issue titled 'Feature request: Add CSV export button' (body: 'A public request for a new feature to export "
            "data grids as CSV.', labels: ['feature-request']).\n"
            "    * An internal issue titled '[Tracker] Oversee contribution for CSV export' (body: 'Internal issue to track the external "
            "contribution for the CSV export feature.', labels: ['tracker', 'external-contribution'], assigned to 'ui-dev').\n"
            "* **Required State of Codebase:**\n"
            "    * A PR titled 'feat: Add CSV export functionality' (body: 'Adds a button to export data grid contents as a CSV file.', "
            "reviewed by ['tech-lead-tara']) must be 'merged' and linked to both issues.\n"
            "    * The merged PR must contain the following commits from the 'feature/csv-export' branch:\n"
            "        1. `feat: Add basic CSV export button` (Author: 'contractor-alex')\n"
            "        2. `style: Adjust export button to match design system` (Author: 'ui-dev')\n"
            "        3. `test: Add unit tests for CSV generation` (Author: 'qa-erin')\n"
            "* **Required State of Release:** A release 'v3.5.1' ('Adds CSV export functionality from external contributor.') must be published."
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Feature request: Add CSV export button", "body": "A public request for a new feature to export data grids as CSV.", "labels": ["feature-request"]}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "[Tracker] Oversee contribution for CSV export", "body": "Internal issue to track the external contribution for the CSV export feature.", "labels": ["tracker", "external-contribution"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 13, "assignees": ["ui-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/csv-export", "message": "feat: Add basic CSV export button", "author": "contractor-alex"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "feat: Add CSV export functionality", "body": "Adds a button to export data grid contents as a CSV file.", "head_branch": "feature/csv-export", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 12}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 13}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/csv-export", "message": "style: Adjust export button to match design system", "author": "ui-dev"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/csv-export", "message": "test: Add unit tests for CSV generation", "author": "qa-erin"}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "ui-kit", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 13}),
            Action(name="create_release", kwargs={"repo_name": "ui-kit", "version": "v3.5.1", "description": "Adds CSV export functionality from external contributor."}),
            Action(name="get_team_contribution_stats", kwargs={"repo_name": "ui-kit"}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "ui-kit"}),
        ],
        outputs=[
            {
                "repo": "ui-kit",
                "team_stats": {
                    "unknown": {"commits": 0, "prs": 1, "issues": 0},
                    "contractor-alex": {"commits": 1, "prs": 0, "issues": 0},
                    "ui-dev": {"commits": 1, "prs": 0, "issues": 1},
                    "qa-erin": {"commits": 1, "prs": 0, "issues": 0}
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_702",
        instruction=(
            "Your primary strategic objective is to govern a full feature lifecycle according to the **Staged Deployment and Verification Policy** for the "
            "'ui-kit' repository. This policy requires new features to be deployed and verified in a 'staging' environment before being approved for "
            "'production'. You are responsible for bringing the repository to a state that reflects the successful execution of this entire process, "
            "as defined by the official **Staged Rollout Compliance Specification** below. Your final deliverable is the repository's activity dashboard "
            "to confirm the feature is fully verified and ready for production.\n\n"
            "**Staged Rollout Compliance Specification: Advanced Charting Feature**\n"
            "* **Required State of Feature Development:**\n"
            "    * A main issue titled 'Implement Advanced Charting Library' (body: 'Main tracking issue for the Advanced Charting feature.', "
            "labels: ['feature', 'epic'], assigned to 'ui-dev') must be 'closed'.\n"
            "    * A PR titled 'feat: Advanced Charting Library' (body: 'PR to introduce the advanced charting library.', reviewed by ['tech-lead-tara']) "
            "must be 'merged', containing commits 'feat: Add charting components' and 'test: Add chart rendering tests' from the 'feature/adv-charts' branch.\n"
            "* **Required State of Staging Verification:**\n"
            "    * A deployment to the 'staging' environment must be registered.\n"
            "    * A verification issue titled 'Staging Verification for Advanced Charting' (body: 'Tracking issue for QA verification on the staging environment.', "
            "labels: ['qa', 'verification'], assigned to 'qa-erin') must be 'closed'.\n"
            "* **Required State of Production Readiness:**\n"
            "    * A final issue titled 'Schedule Production Release for Advanced Charting v3.5.0' (body: 'All checks passed. Ready to schedule production "
            "deployment.', labels: ['release', 'ops'], assigned to 'release-manager') must be 'open'."
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Implement Advanced Charting Library", "body": "Main tracking issue for the Advanced Charting feature.", "labels": ["feature", "epic"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12, "assignees": ["ui-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/adv-charts", "message": "feat: Add charting components", "author": "ui-dev"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feature/adv-charts", "message": "test: Add chart rendering tests", "author": "qa-erin"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "feat: Advanced Charting Library", "body": "PR to introduce the advanced charting library.", "head_branch": "feature/adv-charts", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "ui-kit", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12}),
            Action(name="register_deploy_event", kwargs={"repo_name": "ui-kit", "environment": "staging"}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Staging Verification for Advanced Charting", "body": "Tracking issue for QA verification on the staging environment.", "labels": ["qa", "verification"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 13, "assignees": ["qa-erin"]}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 13}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Schedule Production Release for Advanced Charting v3.5.0", "body": "All checks passed. Ready to schedule production deployment.", "labels": ["release", "ops"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 14, "assignees": ["release-manager"]}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "ui-kit"}),
        ],
        outputs=[
            {
                "repo": "ui-kit",
                "commits_count": 2,
                "open_issues": 1,
                "open_prs": 0,
                "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                "open_alerts": 0,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_703",
        instruction=(
            "Your primary strategic objective is to govern the creation of the new 'inventory-management-api' repository, ensuring it fully "
            "aligns with the company's **Secure Project Bootstrap Policy**. This policy mandates that all new projects resolve any known "
            "vulnerabilities from their base template before the first release. You are responsible for ensuring the repository's final state "
            "perfectly matches the official **Secure Bootstrap Compliance Specification**, detailed below. Your final deliverable is the "
            "repository's health summary, which will serve as the official record of policy compliance.\n\n"
            "**Secure Bootstrap Compliance Specification:**\n"
            "* **Required Repository State:**\n"
            "    * A 'private' repository must be created with description: 'API for managing warehouse inventory.' and contain an initial "
            "commit with the message 'Initial commit from template' by 'devops-lead'.\n"
            "* **Required State of Initial Security Posture:**\n"
            "    * A 'medium' severity alert for 'Default template includes outdated dependency: GSON v2.8.5' in 'pom.xml' must be 'fixed'.\n"
            "    * A main setup issue titled 'Initial Project Setup' (body: 'Main tracking issue for the complete and secure setup of the new repository.', "
            "labels: ['setup', 'epic'], assigned to 'backend-core') must be 'closed'.\n"
            "    * A sub-task issue titled 'fix: Update outdated GSON dependency' (body: 'Sub-task to update the vulnerable GSON dependency "
            "from the initial template.', labels: ['security', 'dependency'], assigned to 'backend-core') must be 'closed'.\n"
            "    * A PR titled 'fix(deps): Upgrade GSON to v2.8.9' (body: 'PR to upgrade outdated GSON dependency.', reviewed by "
            "['tech-lead-tara']) must be 'merged', linked to the security sub-task, and contain a commit 'fix: Upgrade GSON to v2.8.9' "
            "(author: 'backend-core') from the 'hotfix/gson-upgrade' branch.\n"
            "* **Required State of Release:**\n"
            "    * A release 'v0.1.0' ('Initial secure release.') must be published."
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "inventory-management-api", "description": "API for managing warehouse inventory.", "private": True}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "inventory-management-api", "branch": "main", "message": "Initial commit from template", "author": "devops-lead"}),
            Action(name="create_security_alert", kwargs={"repo_name": "inventory-management-api", "severity": "medium", "description": "Default template includes outdated dependency: GSON v2.8.5", "file": "pom.xml", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "inventory-management-api", "title": "Initial Project Setup", "body": "Main tracking issue for the complete and secure setup of the new repository.", "labels": ["setup", "epic"]}),
            Action(name="assign_issue", kwargs={"repo_name": "inventory-management-api", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="create_issue", kwargs={"repo_name": "inventory-management-api", "title": "fix: Update outdated GSON dependency", "body": "Sub-task to update the vulnerable GSON dependency from the initial template.", "labels": ["security", "dependency"]}),
            Action(name="assign_issue", kwargs={"repo_name": "inventory-management-api", "issue_number": 13, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "inventory-management-api", "branch": "hotfix/gson-upgrade", "message": "fix: Upgrade GSON to v2.8.9", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "inventory-management-api", "title": "fix(deps): Upgrade GSON to v2.8.9", "body": "PR to upgrade outdated GSON dependency.", "head_branch": "hotfix/gson-upgrade", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "inventory-management-api", "pr_number": 10, "issue_number": 13}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "inventory-management-api", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "inventory-management-api", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "inventory-management-api", "issue_number": 13}),
            Action(name="fix_security_alert", kwargs={"repo_name": "inventory-management-api", "alert_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "inventory-management-api", "issue_number": 12}),
            Action(name="create_release", kwargs={"repo_name": "inventory-management-api", "version": "v0.1.0", "description": "Initial secure release."}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "inventory-management-api"}),
        ],
        outputs=[
            {
                "repo": "inventory-management-api",
                "open_issues": 0,
                "open_prs": 0,
                "open_alerts": 0,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_601",
        instruction=(
            "Your primary strategic objective is to govern the setup of a new hire's first project, ensuring it fully aligns with the company's "
            "**New Hire Onboarding Policy**. This policy mandates that a dedicated starter repository is created with a structured set of "
            "onboarding tasks. You are responsible for ensuring the repository's final state perfectly matches the official **Onboarding "
            "Compliance Specification**, detailed below. Your final deliverable is the repository's activity dashboard, which will serve "
            "as the official record of policy compliance.\n\n"
            "**Onboarding Compliance Specification for 'new-hire-starter-project':**\n"
            "* **Required Repository State:**\n"
            "    * Must be 'private' with description: 'Starter project for new engineering hires.'\n"
            "* **Required State of Onboarding Issues:**\n"
            "    * A main epic titled 'Onboarding Plan for new hire' (body: 'Main epic to track the new hire onboarding process.', labels: "
            "['onboarding', 'epic']) must be 'open' and assigned to 'intern-sarah'.\n"
            "    * A sub-task titled 'Task 1: Set up local development environment' (body: 'Sub-task to track local environment setup.', labels: "
            "['onboarding', 'setup']) must be 'open' and assigned to 'intern-sarah'.\n"
            "    * A sub-task titled 'Task 2: Complete first coding task' (body: 'Sub-task for the first coding assignment.', labels: "
            "['onboarding', 'coding-task']) must be 'closed'.\n"
            "    * A sub-task titled 'Task 3: Schedule team introduction meetings' (body: 'Sub-task to schedule introductory meetings.', "
            "labels: ['onboarding', 'meetings']) must be 'open' and assigned to 'intern-sarah'.\n"
            "* **Required State of First Coding Task:**\n"
            "    * A pull request titled 'feat: Add welcome message endpoint' (body: 'PR for the first coding task.', reviewed by "
            "['tech-lead-tara']) must be 'merged' into 'main', linked to the coding task issue, and contain a commit 'feat: Implement /hello "
            "endpoint' by 'intern-sarah' from the 'feature/welcome-endpoint' branch."
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "new-hire-starter-project", "description": "Starter project for new engineering hires.", "private": True}),
            Action(name="create_issue", kwargs={"repo_name": "new-hire-starter-project", "title": "Onboarding Plan for new hire", "body": "Main epic to track the new hire onboarding process.", "labels": ["onboarding", "epic"]}),
            Action(name="assign_issue", kwargs={"repo_name": "new-hire-starter-project", "issue_number": 12, "assignees": ["intern-sarah"]}),
            Action(name="create_issue", kwargs={"repo_name": "new-hire-starter-project", "title": "Task 1: Set up local development environment", "body": "Sub-task to track local environment setup.", "labels": ["onboarding", "setup"]}),
            Action(name="assign_issue", kwargs={"repo_name": "new-hire-starter-project", "issue_number": 13, "assignees": ["intern-sarah"]}),
            Action(name="create_issue", kwargs={"repo_name": "new-hire-starter-project", "title": "Task 2: Complete first coding task", "body": "Sub-task for the first coding assignment.", "labels": ["onboarding", "coding-task"]}),
            Action(name="assign_issue", kwargs={"repo_name": "new-hire-starter-project", "issue_number": 14, "assignees": ["intern-sarah"]}),
            Action(name="create_issue", kwargs={"repo_name": "new-hire-starter-project", "title": "Task 3: Schedule team introduction meetings", "body": "Sub-task to schedule introductory meetings.", "labels": ["onboarding", "meetings"]}),
            Action(name="assign_issue", kwargs={"repo_name": "new-hire-starter-project", "issue_number": 15, "assignees": ["intern-sarah"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "new-hire-starter-project", "branch": "feature/welcome-endpoint", "message": "feat: Implement /hello endpoint", "author": "intern-sarah"}),
            Action(name="open_pull_request", kwargs={"repo_name": "new-hire-starter-project", "title": "feat: Add welcome message endpoint", "body": "PR for the first coding task.", "head_branch": "feature/welcome-endpoint", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "new-hire-starter-project", "pr_number": 10, "issue_number": 14}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "new-hire-starter-project", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "new-hire-starter-project", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "new-hire-starter-project", "issue_number": 14}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "new-hire-starter-project"}),
        ],
        outputs=[
            {
                "repo": "new-hire-starter-project",
                "commits_count": 1,
                "open_issues": 3,
                "open_prs": 0,
                "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                "open_alerts": 0,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_503",
        instruction=(
            "Your primary strategic objective is to ensure the 'security-scanner' repository is brought into full compliance with the company's "
            "**Audit and Proactive Hardening Policy**. This policy mandates that all audit findings are formally tracked and that a preventative "
            "control is implemented to address the root cause. You are responsible for ensuring the repository's state perfectly matches the "
            "official **Audit Compliance Specification**, detailed below. Your final deliverable is the repository activity dashboard, which will "
            "serve as the official record of policy compliance.\n\n"
            "**Audit Compliance Specification for security-scanner:**\n"
            "* **Required State of Audit Findings (Issues):**\n"
            "    * An issue titled 'Finding: Inconsistent Logging Levels' (body: 'Audit finding identifying multiple inconsistent logging levels across modules.', "
            "labels: ['bug', 'logging'], assigned to 'security-team') must be 'open'.\n"
            "    * An issue titled 'Finding: High Memory Usage in Scanner' (body: 'Audit finding identifying high memory usage during large file scans.', "
            "labels: ['performance'], assigned to 'perf-joe') must be 'open'.\n"
            "    * A main issue titled 'Q3 Security Audit Findings' (body: 'Main tracking issue for all Q3 audit findings and the preventative action PR.', "
            "labels: ['audit'], assigned to 'tech-lead-tara') must be 'closed'.\n"
            "* **Required State of Preventative Control:**\n"
            "    * A pull request titled 'build: Add static analysis pre-commit hook' (body: 'This PR adds a pre-commit hook for static analysis to prevent future issues.', "
            "reviewed by ['tech-lead-tara']) must be 'merged' into 'main', linked to the main audit issue, and contain a commit "
            "'build: Add static analysis pre-commit hook' by 'devops-lead' from the 'feature/static-analysis-hook' branch."
        ),
        actions=[
            Action(name="get_issue_aging_report", kwargs={"repo_name": "security-scanner"}),
            Action(name="get_pull_request_merge_time_report", kwargs={"repo_name": "security-scanner"}),
            Action(name="get_open_security_alerts", kwargs={"repo_name": "security-scanner"}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Finding: Inconsistent Logging Levels", "body": "Audit finding identifying multiple inconsistent logging levels across modules.", "labels": ["bug", "logging"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["security-team"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Finding: High Memory Usage in Scanner", "body": "Audit finding identifying high memory usage during large file scans.", "labels": ["performance"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["perf-joe"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Q3 Security Audit Findings", "body": "Main tracking issue for all Q3 audit findings and the preventative action PR.", "labels": ["audit"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 14, "assignees": ["tech-lead-tara"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "feature/static-analysis-hook", "message": "build: Add static analysis pre-commit hook", "author": "devops-lead"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "build: Add static analysis pre-commit hook", "body": "This PR adds a pre-commit hook for static analysis to prevent future issues.", "head_branch": "feature/static-analysis-hook", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 14}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 14}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
            {
                "repo": "security-scanner",
                "commits_count": 1,
                "open_issues": 2,
                "open_prs": 0,
                "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                "open_alerts": 0,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_402",
        instruction=(
            "Your primary strategic objective is to govern the security lifecycle of the 'security-scanner' repository, ensuring it fully aligns "
            "with the company's **Comprehensive Security Hardening Policy**. This policy mandates a clear and auditable trail for the remediation "
            "of tiered vulnerabilities. You are responsible for ensuring the repository's state reflects the successful execution of this policy, "
            "as defined by the official **Hardening Compliance Specification** below. Your final deliverable is the repository's health summary, "
            "which will serve as the official record of policy compliance.\n\n"
            "**Hardening Compliance Specification for security-scanner:**\n"
            "* **Required State for Critical Risks ('Unsafe deserialization' in 'src/parser.rs'):**\n"
            "    * A tracking issue titled 'Fix Critical: Unsafe Deserialization' (body: 'Full remediation tracking for the critical unsafe deserialization alert.', "
            "labels: ['security']) must be 'closed' and assigned to 'security-team'.\n"
            "    * The corresponding alert must be 'fixed'.\n"
            "    * A PR titled 'Fix: Unsafe Deserialization' (body: 'PR containing the complete fix for the unsafe deserialization vulnerability.') must be 'merged', "
            "containing a commit with the message 'fix: Patch unsafe deserialization vulnerability' from the 'fix/critical-deserialization' branch.\n"
            "* **Required State for High Risks ('Potential buffer overflow' in 'src/handlers.rs'):**\n"
            "    * A tracking issue titled 'Remediate High: Buffer Overflow' (body: 'Remediation tracking for the high-severity buffer overflow alert.', "
            "labels: ['security']) must be 'open' and assigned to 'security-team'.\n"
            "    * A PR titled 'WIP: Remediate Buffer Overflow' (body: 'WIP PR to introduce memory-safe string handling.') must be 'open', containing "
            "a commit with the message 'refactor: Introduce memory-safe string handling' from the 'fix/high-buffer-overflow' branch.\n"
            "* **Required State for Medium Risks ('Use of deprecated crypto functions' in 'src/crypto.rs'):**\n"
            "    * A tracking issue titled 'Track Medium: Deprecated Crypto Usage' (body: 'Tracking issue for future refactoring of deprecated crypto functions.', "
            "labels: ['security'], assigned to 'security-team') must be 'open'.\n"
            "* **General Requirements:**\n"
            "    * All PRs must be reviewed by 'tech-lead-tara'."
        ),
        actions=[
            Action(name="create_security_alert", kwargs={"repo_name": "security-scanner", "severity": "critical", "description": "Unsafe deserialization", "file": "src/parser.rs", "branch": "main"}),
            Action(name="create_security_alert", kwargs={"repo_name": "security-scanner", "severity": "high", "description": "Potential buffer overflow", "file": "src/handlers.rs", "branch": "main"}),
            Action(name="create_security_alert", kwargs={"repo_name": "security-scanner", "severity": "medium", "description": "Use of deprecated crypto functions", "file": "src/crypto.rs", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Fix Critical: Unsafe Deserialization", "body": "Full remediation tracking for the critical unsafe deserialization alert.", "labels": ["security"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "fix/critical-deserialization", "message": "fix: Patch unsafe deserialization vulnerability", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "Fix: Unsafe Deserialization", "body": "PR containing the complete fix for the unsafe deserialization vulnerability.", "head_branch": "fix/critical-deserialization", "base_branch": "main"}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12}),
            Action(name="fix_security_alert", kwargs={"repo_name": "security-scanner", "alert_number": 10}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Remediate High: Buffer Overflow", "body": "Remediation tracking for the high-severity buffer overflow alert.", "labels": ["security"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "fix/high-buffer-overflow", "message": "refactor: Introduce memory-safe string handling", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "WIP: Remediate Buffer Overflow", "body": "WIP PR to introduce memory-safe string handling.", "head_branch": "fix/high-buffer-overflow", "base_branch": "main"}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 11, "reviewers": ["tech-lead-tara"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Track Medium: Deprecated Crypto Usage", "body": "Tracking issue for future refactoring of deprecated crypto functions.", "labels": ["security"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 14, "assignees": ["security-team"]}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
            {
                "repo": "security-scanner",
                "open_issues": 2,
                "open_prs": 1,
                "open_alerts": 2,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_301",
        instruction=(
            "Your strategic objective is to execute the company's **Tiered Vulnerability Response Protocol** on the 'security-scanner' repository. "
            "This protocol mandates a two-pronged approach: full remediation for critical-risk items and initial containment for high-risk items. "
            "You are required to implement this protocol to address the vulnerabilities described in the specification below. "
            "Your final deliverable is the repository's activity dashboard to verify that the protocol was correctly executed and the repository "
            "state reflects the completed critical remediation and the in-progress high-risk containment.\n\n"
            "**Compliance Specification:**\n"
            "* **Critical Vulnerability (Unsafe Deserialization):** This must be fully remediated. The final state must show a 'closed' tracking issue and a 'merged' pull request with the hotfix. This work is owned by the 'security-team'.\n"
            "* **High Vulnerability (Buffer Overflow):** This requires initial containment. The final state must show an 'open' tracking issue and an 'open' work-in-progress pull request with initial mitigation steps. This work is owned by 'perf-joe'.\n"
            "* **General Requirements:** All pull requests related to this protocol must be reviewed by 'tech-lead-tara'."
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Remediate Critical: Unsafe Deserialization", "body": "Tracking issue for the unsafe deserialization vulnerability.", "labels": ["security", "critical-risk"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12, "assignees": ["security-team"]}),
            Action(name="create_issue", kwargs={"repo_name": "security-scanner", "title": "Remediate High: Buffer Overflow", "body": "Tracking issue for the potential buffer overflow vulnerability.", "labels": ["security", "high-risk"]}),
            Action(name="assign_issue", kwargs={"repo_name": "security-scanner", "issue_number": 13, "assignees": ["perf-joe"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "hotfix/critical-deserialization", "message": "fix: Initial patch for unsafe deserialization", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "Fix: Unsafe Deserialization", "body": "Complete fix for the critical deserialization vulnerability.", "head_branch": "hotfix/critical-deserialization", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 10, "reviewers": ["tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "security-scanner", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "security-scanner", "issue_number": 12}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "security-scanner", "branch": "fix/buffer-overflow-config", "message": "feat: Add memory safe string handling config", "author": "perf-joe"}),
            Action(name="open_pull_request", kwargs={"repo_name": "security-scanner", "title": "WIP: Config for Buffer Overflow", "body": "Configuration update to mitigate buffer overflow risks.", "head_branch": "fix/buffer-overflow-config", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "security-scanner", "pr_number": 11, "issue_number": 13}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "security-scanner", "pr_number": 11, "reviewers": ["tech-lead-tara"]}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "security-scanner"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data": {
                    "repo": "security-scanner",
                    "commits_count": 2,
                    "open_issues": 1,
                    "open_prs": 1,
                    "open_alerts_by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "unknown": 0},
                    "open_alerts": 0,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_302",
        instruction=(
            "Your primary role is to ensure the new 'api-gateway' project fully complies with the company's **New Service Incubation Policy**. "
            "This policy requires that all new services complete two foundational feature cycles before their first alpha release. "
            "You must use the provided compliance specification and data manifest to bring the repository from a newly created state to its fully compliant v0.1.0-alpha state. "
            "Your final deliverable is the repository's health summary to confirm that the state of the repository aligns with the policy.\n\n"
            "**Compliance Specification for v0.1.0-alpha:**\n"
            "The final state must show that the repository has been created and that two foundational features ('Authentication' and 'Rate Limiting') have been fully implemented. "
            "A full implementation requires that each feature is tracked via an issue that is now 'closed', with the corresponding code merged via a pull request. "
            "Finally, a formal alpha release must be published.\n\n"
            "**Data Manifest:**\n"
            "* **Repository Config:** {name: 'api-gateway', description: 'Central API Gateway for microservices.', private: True}\n"
            "* **Feature 1 (Authentication):** {issue_title: 'Implement Authentication Route', issue_body: 'Implementation of the primary authentication endpoint.', labels: ['feature', 'auth'], assignee: 'backend-core', branch: 'feature/auth-route', commit_author: 'backend-core', commit_message: 'feat: Add JWT authentication middleware and /auth route', pr_title: 'Feature: Authentication Route', pr_body: 'PR for the authentication route.'}\n"
            "* **Feature 2 (Rate Limiting):** {issue_title: 'Implement Rate Limiting', issue_body: 'Implementation of IP-based rate limiting.', labels: ['feature', 'performance'], assignee: 'devops-lead', branch: 'feature/rate-limit', commit_author: 'devops-lead', commit_message: 'feat: Add IP-based rate limiting', pr_title: 'Feature: Rate Limiting', pr_body: 'PR for rate limiting.'}\n"
            "* **Release Artifact:** {version: 'v0.1.0-alpha', description: 'First alpha release with auth and rate limiting.'}"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "api-gateway", "description": "Central API Gateway for microservices.", "private": True}),
            Action(name="create_issue", kwargs={"repo_name": "api-gateway", "title": "Implement Authentication Route", "body": "Implementation of the primary authentication endpoint.", "labels": ["feature", "auth"]}),
            Action(name="assign_issue", kwargs={"repo_name": "api-gateway", "issue_number": 12, "assignees": ["backend-core"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "api-gateway", "branch": "feature/auth-route", "message": "feat: Add JWT authentication middleware and /auth route", "author": "backend-core"}),
            Action(name="open_pull_request", kwargs={"repo_name": "api-gateway", "title": "Feature: Authentication Route", "body": "PR for the authentication route.", "head_branch": "feature/auth-route", "base_branch": "main"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "api-gateway", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "api-gateway", "issue_number": 12}),
            Action(name="create_issue", kwargs={"repo_name": "api-gateway", "title": "Implement Rate Limiting", "body": "Implementation of IP-based rate limiting.", "labels": ["feature", "performance"]}),
            Action(name="assign_issue", kwargs={"repo_name": "api-gateway", "issue_number": 13, "assignees": ["devops-lead"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "api-gateway", "branch": "feature/rate-limit", "message": "feat: Add IP-based rate limiting", "author": "devops-lead"}),
            Action(name="open_pull_request", kwargs={"repo_name": "api-gateway", "title": "Feature: Rate Limiting", "body": "PR for rate limiting.", "head_branch": "feature/rate-limit", "base_branch": "main"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "api-gateway", "pr_number": 11}),
            Action(name="close_issue", kwargs={"repo_name": "api-gateway", "issue_number": 13}),
            Action(name="create_release", kwargs={"repo_name": "api-gateway", "version": "v0.1.0-alpha", "description": "First alpha release with auth and rate limiting."}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "api-gateway"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_303",
        instruction=(
            "Your objective is to execute the **Major Version Release Preparation Policy** for the upcoming 'v4.0.0' of the 'ui-kit' repository. "
            "The policy requires that all planned features and deprecations are formally tracked, implemented, and merged into the main branch "
            "via a consolidated release pull request. You must use the provided **Release Work Manifest** to create all required artifacts for "
            "this preparation process. Your final deliverable is the repository's activity dashboard to confirm that all changes have been "
            "successfully merged and the repository is ready for the v4.0.0 tag.\n\n"
            "**Release Work Manifest for v4.0.0:**\n"
            "* **Feature A (Dark Mode):**\n"
            "    * Title: 'Implement Dark Mode v2', Body: 'Tracking issue for Dark Mode v2 implementation.', Labels: ['feature', 'ui'], Assignee: 'ui-dev'\n"
            "* **Feature B (Accessibility):**\n"
            "    * Title: 'Add Accessibility Tree Shaking', Body: 'Tracking issue for accessibility tree shaking.', Labels: ['feature', 'a11y'], Assignee: 'frontend-dev'\n"
            "* **Deprecation C (Grid):**\n"
            "    * Title: 'Deprecate Legacy Grid Component', Body: 'Tracking issue for legacy grid deprecation.', Labels: ['deprecation', 'tech-debt'], Assignee: 'ui-dev'\n"
            "* **Implementation:**\n"
            "    * Branch: 'release/v4.0.0', Author: 'ui-dev', Commits: ['feat: Dark Mode v2', 'feat: Accessibility Tree Shaking', 'refactor: Deprecate Legacy Grid']\n"
            "* **Consolidated PR:**\n"
            "    * Title: 'Release: Version 4.0.0', Body: 'Consolidated PR for v4.0.0, including all new features and deprecations.', Reviewers: ['design-lead', 'tech-lead-tara']"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Implement Dark Mode v2", "body": "Tracking issue for Dark Mode v2 implementation.", "labels": ["feature", "ui"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12, "assignees": ["ui-dev"]}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Add Accessibility Tree Shaking", "body": "Tracking issue for accessibility tree shaking.", "labels": ["feature", "a11y"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 13, "assignees": ["frontend-dev"]}),
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "Deprecate Legacy Grid Component", "body": "Tracking issue for legacy grid deprecation.", "labels": ["deprecation", "tech-debt"]}),
            Action(name="assign_issue", kwargs={"repo_name": "ui-kit", "issue_number": 14, "assignees": ["ui-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "release/v4.0.0", "message": "feat: Dark Mode v2", "author": "ui-dev"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "release/v4.0.0", "message": "feat: Accessibility Tree Shaking", "author": "ui-dev"}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "release/v4.0.0", "message": "refactor: Deprecate Legacy Grid", "author": "ui-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "Release: Version 4.0.0", "body": "Consolidated PR for v4.0.0, including all new features and deprecations.", "head_branch": "release/v4.0.0", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 12}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 13}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "ui-kit", "pr_number": 10, "issue_number": 14}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "ui-kit", "pr_number": 10, "reviewers": ["design-lead", "tech-lead-tara"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 13}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 14}),
            Action(name="get_repository_activity_dashboard", kwargs={"repo_name": "ui-kit"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_305",
        instruction=(
            "Your primary role is to ensure the new 'data-pipeline-orchestrator' project fully complies with the company's **New Project Go-Live Policy**. "
            "This policy requires that new services are bootstrapped with all foundational artifacts, including initial features and security scans, before their first release. "
            "Your task is to bring the repository from a newly created state to one that matches the official **Compliance Specification for v0.1.0**. "
            "Your final deliverable is the repository's health summary to confirm that its state aligns with the policy.\n\n"
            "**Compliance Specification for v0.1.0:**\n"
            "The final state of the repository must show the successful implementation of an initial feature, which must be tracked via a 'closed' issue and a 'merged' pull request. "
            "The repository must also have an initial 'medium' severity security alert logged. Finally, a formal release must be published and deployed to 'staging'.\n\n"
            "**Data Manifest:**\n"
            "* **Repository Config:** {name: 'data-pipeline-orchestrator', description: 'Service for orchestrating ETL data pipelines.', private: True}\n"
            "* **Initial Feature:** {issue_title: 'Setup initial DAG structure', issue_body: 'Tracks the implementation of the initial DAG structure for the orchestrator.', labels: ['feature', 'architecture'], assignee: 'data-scientist', branch: 'feature/initial-dag', commit_author: 'ml-engineer', commit_message: 'feat: Add initial DAG scaffolding', pr_title: 'Feature: Initial DAG Structure', pr_body: 'PR for the initial DAG structure.', reviewers: ['data-scientist']}\n"
            "* **Security Alert:** {severity: 'medium', description: 'Hardcoded credentials in connector module.', file: 'src/connectors/db.py'}\n"
            "* **Release Artifacts:** {version: '0.1.0', description: 'Initial release with basic DAG orchestration.', environment: 'staging'}"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "data-pipeline-orchestrator", "description": "Service for orchestrating ETL data pipelines.", "private": True}),
            Action(name="create_issue", kwargs={"repo_name": "data-pipeline-orchestrator", "title": "Setup initial DAG structure", "body": "Tracks the implementation of the initial DAG structure for the orchestrator.", "labels": ["feature", "architecture"]}),
            Action(name="assign_issue", kwargs={"repo_name": "data-pipeline-orchestrator", "issue_number": 12, "assignees": ["data-scientist"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "data-pipeline-orchestrator", "branch": "feature/initial-dag", "message": "feat: Add initial DAG scaffolding", "author": "ml-engineer"}),
            Action(name="open_pull_request", kwargs={"repo_name": "data-pipeline-orchestrator", "title": "Feature: Initial DAG Structure", "body": "PR for the initial DAG structure.", "head_branch": "feature/initial-dag", "base_branch": "main"}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "data-pipeline-orchestrator", "pr_number": 10, "reviewers": ["data-scientist"]}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "data-pipeline-orchestrator", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "data-pipeline-orchestrator", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "data-pipeline-orchestrator", "issue_number": 12}),
            Action(name="create_security_alert", kwargs={"repo_name": "data-pipeline-orchestrator", "severity": "medium", "description": "Hardcoded credentials in connector module.", "file": "src/connectors/db.py", "branch": "main"}),
            Action(name="create_release", kwargs={"repo_name": "data-pipeline-orchestrator", "version": "0.1.0", "description": "Initial release with basic DAG orchestration."}),
            Action(name="register_deploy_event", kwargs={"repo_name": "data-pipeline-orchestrator", "environment": "staging"}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "data-pipeline-orchestrator"}),
        ],
        outputs=[
            {
                "status": "ok",
                "data":{
                    "repo": "data-pipeline-orchestrator",
                    "open_issues": 0,
                    "open_prs": 0,
                    "open_alerts": 1,
                    "report_date": "2025-08-26"
                }
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_201",
        instruction=(
            "Your objective is to manage the full lifecycle of a feature implementation and its subsequent emergency reversal for the 'acme-webapp' "
            "repository, following company policy. You will first oversee the merge of a new feature using the 'Feature Manifest'. Immediately "
            "after, a critical vulnerability is discovered related to this feature. You must then apply the 'Emergency Reversal Policy' using "
            "the 'Reversal Manifest' to formally track the problem and prepare a fix. Your final deliverable is the repository's health summary "
            "reflecting the active emergency state.\n\n"
            "**Feature Manifest (v1.1.0):**\n"
            "* Tracking Issue: Title='Implement User Profile Caching', Body='Tracks caching implementation.', Labels=['feature'], Assignee='alice-w'\n"
            "* Implementation: Branch='feature/profile-caching', Commit Author='dev-sue', Commit Message='feat: Add user profile caching logic'\n"
            "* Pull Request: Title='Feature: User Profile Caching', Body='PR for user profile caching.', Reviewers=['qa-mike']\n\n"
            "**Reversal Manifest:**\n"
            "* Security Alert: Severity='critical', Description='Post-merge discovery: Caching logic exposes sensitive user data.', File='src/app.py'\n"
            "* Reversal Issue: Title='EMERGENCY: Reversal of profile caching feature', Body='Reversal required due to critical vulnerability.', Labels=['security', 'bug'], Assignee='security-team'\n"
            "* Reversal PR: Title='Revert: User Profile Caching', Body='Reverting the caching feature due to a critical vulnerability.', Branch='revert/profile-caching', Commit Author='security-team', Commit Message='revert: Revert user profile caching feature'"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "Implement User Profile Caching", "body": "Tracks caching implementation.", "labels": ["feature"]}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12, "assignees": ["alice-w"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "acme-webapp", "branch": "feature/profile-caching", "message": "feat: Add user profile caching logic", "author": "dev-sue"}),
            Action(name="open_pull_request", kwargs={"repo_name": "acme-webapp", "title": "Feature: User Profile Caching", "body": "PR for user profile caching.", "head_branch": "feature/profile-caching", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 10, "issue_number": 12}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "acme-webapp", "pr_number": 10, "reviewers": ["qa-mike"]}),
            Action(name="merge_pull_request", kwargs={"repo_name": "acme-webapp", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12}),
            Action(name="create_security_alert", kwargs={"repo_name": "acme-webapp", "severity": "critical", "description": "Post-merge discovery: Caching logic exposes sensitive user data.", "file": "src/app.py", "branch": "main"}),
            Action(name="create_issue", kwargs={"repo_name": "acme-webapp", "title": "EMERGENCY: Reversal of profile caching feature", "body": "Reversal required due to critical vulnerability.", "labels": ["security", "bug"]}),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 13, "assignees": ["security-team"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "acme-webapp", "branch": "revert/profile-caching", "message": "revert: Revert user profile caching feature", "author": "security-team"}),
            Action(name="open_pull_request", kwargs={"repo_name": "acme-webapp", "title": "Revert: User Profile Caching", "body": "Reverting the caching feature due to a critical vulnerability.", "head_branch": "revert/profile-caching", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "acme-webapp", "pr_number": 11, "issue_number": 13}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "acme-webapp"}),
        ],
        outputs=[
            {
                "repo": "acme-webapp",
                "open_issues": 1,
                "open_prs": 1,
                "open_alerts": 1,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_202",
        instruction=(
            "Your task is to manage a breaking change in the 'ui-kit' core library and propagate the necessary updates to the downstream "
            "'react-dashboard' application, following the standard cross-repository upgrade policy. You will use the provided manifests "
            "for both the library update and the application adaptation. Your final deliverable is a list containing the health summaries "
            "for both repositories to confirm the status of the entire operation.\n\n"
            "**Manifest for ui-kit (v3.0.0):**\n"
            "* **Tracking Issue:**\n"
            "    * Title: '[v3.0] Breaking Change: Deprecate legacy Button API'\n"
            "    * Body: 'Tracks the deprecation of the legacy Button API for the v3.0.0 release.'\n"
            "    * Labels: ['breaking-change', 'v3.0']\n"
            "* **Implementation:**\n"
            "    * Branch: 'feat/v3-button-api'\n"
            "    * Commit Author: 'ui-dev'\n"
            "    * Commit Message: 'refactor: Replace legacy Button API with new spec'\n"
            "* **Pull Request:**\n"
            "    * Title: 'Refactor: New Button API for v3.0.0'\n"
            "    * Body: 'This PR introduces the new Button API and removes the deprecated legacy component.'\n"
            "* **Release:**\n"
            "    * Version: '3.0.0'\n"
            "    * Description: 'Version 3.0.0 with new Button API.'\n\n"
            "**Manifest for react-dashboard:**\n"
            "* **Tracking Issue:**\n"
            "    * Title: 'Upgrade to ui-kit v3.0.0'\n"
            "    * Body: 'Adapt application to the new Button API introduced in ui-kit v3.0.0.'\n"
            "    * Labels: ['dependency-upgrade', 'tech-debt']\n"
            "    * Assignee: 'frontend-dev'\n"
            "* **Implementation:**\n"
            "    * Branch: 'feat/upgrade-uikit-v3'\n"
            "    * Commit Author: 'frontend-dev'\n"
            "    * Commit Message: 'feat: Update app to use new ui-kit Button API'\n"
            "* **Pull Request:**\n"
            "    * Title: 'Upgrade: Adapt to ui-kit v3.0.0'\n"
            "    * Body: 'This PR adapts the app to the breaking changes in ui-kit v3.0.0.'\n"
            "    * Reviewers: ['tech-lead-tara']"
        ),
        actions=[
            Action(name="create_issue", kwargs={"repo_name": "ui-kit", "title": "[v3.0] Breaking Change: Deprecate legacy Button API", "body": "Tracks the deprecation of the legacy Button API for the v3.0.0 release.", "labels": ["breaking-change", "v3.0"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "ui-kit", "branch": "feat/v3-button-api", "message": "refactor: Replace legacy Button API with new spec", "author": "ui-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "ui-kit", "title": "Refactor: New Button API for v3.0.0", "body": "This PR introduces the new Button API and removes the deprecated legacy component.", "head_branch": "feat/v3-button-api", "base_branch": "main"}),
            Action(name="merge_pull_request", kwargs={"repo_name": "ui-kit", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "ui-kit", "issue_number": 12}),
            Action(name="create_release", kwargs={"repo_name": "ui-kit", "version": "3.0.0", "description": "Version 3.0.0 with new Button API."}),
            Action(name="create_issue", kwargs={"repo_name": "react-dashboard", "title": "Upgrade to ui-kit v3.0.0", "body": "Adapt application to the new Button API introduced in ui-kit v3.0.0.", "labels": ["dependency-upgrade", "tech-debt"]}),
            Action(name="assign_issue", kwargs={"repo_name": "react-dashboard", "issue_number": 13, "assignees": ["frontend-dev"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "react-dashboard", "branch": "feat/upgrade-uikit-v3", "message": "feat: Update app to use new ui-kit Button API", "author": "frontend-dev"}),
            Action(name="open_pull_request", kwargs={"repo_name": "react-dashboard", "title": "Upgrade: Adapt to ui-kit v3.0.0", "body": "This PR adapts the app to the breaking changes in ui-kit v3.0.0.", "head_branch": "feat/upgrade-uikit-v3", "base_branch": "main"}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "react-dashboard", "pr_number": 11, "issue_number": 13}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "react-dashboard", "pr_number": 11, "reviewers": ["tech-lead-tara"]}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "ui-kit"}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "react-dashboard"}),
        ],
        outputs=[
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
        ],
    ),
    Task(
        annotator="1",
        user_id="user_205",
        instruction=(
            "Your objective is to execute the company's 'New Project Go-Live Policy' for the 'data-pipeline-orchestrator' service. This policy requires "
            "a full end-to-end setup, from repository creation to a first release. Per system policy, the first new issue in a task receives ID 12 "
            "and the first new PR receives ID 10; subsequent new entities are numbered sequentially from there. You must use the provided "
            "Go-Live Manifest to create all artifacts according to this policy. Your deliverable is the repository's health summary post-release.\n\n"
            "**Go-Live Manifest for data-pipeline-orchestrator:**\n"
            "* **Repository:**\n"
            "    * Description: 'Service for orchestrating ETL data pipelines.'\n"
            "    * Privacy: 'private'\n"
            "* **Initial Feature Issue:**\n"
            "    * Title: 'Setup initial DAG structure'\n"
            "    * Body: 'Tracks the implementation of the initial DAG structure for the orchestrator.'\n"
            "    * Labels: ['feature', 'architecture']\n"
            "    * Assignee: 'data-scientist'\n"
            "* **Feature Implementation:**\n"
            "    * Branch: 'feature/initial-dag'\n"
            "    * Commit Author: 'ml-engineer'\n"
            "    * Commit Message: 'feat: Add initial DAG scaffolding'\n"
            "* **Pull Request:**\n"
            "    * Title: 'Feature: Initial DAG Structure'\n"
            "    * Body: 'PR for the initial DAG structure.'\n"
            "    * Base Branch: 'main'\n"
            "    * Reviewers: ['data-scientist']\n"
            "* **Day-One Security Alert:**\n"
            "    * Severity: 'medium'\n"
            "    * Description: 'Hardcoded credentials in connector module.'\n"
            "    * File: 'src/connectors/db.py'\n"
            "* **First Release:**\n"
            "    * Version: '0.1.0'\n"
            "    * Description: 'Initial release with basic DAG orchestration.'\n"
            "* **Deployment:**\n"
            "    * Environment: 'staging'"
        ),
        actions=[
            Action(name="create_repository", kwargs={"repo_name": "data-pipeline-orchestrator", "description": "Service for orchestrating ETL data pipelines.", "private": True}),
            Action(name="create_issue", kwargs={"repo_name": "data-pipeline-orchestrator", "title": "Setup initial DAG structure", "body": "Tracks the implementation of the initial DAG structure for the orchestrator.", "labels": ["feature", "architecture"]}),
            Action(name="assign_issue", kwargs={"repo_name": "data-pipeline-orchestrator", "issue_number": 12, "assignees": ["data-scientist"]}),
            Action(name="add_commit_to_branch", kwargs={"repo_name": "data-pipeline-orchestrator", "branch": "feature/initial-dag", "message": "feat: Add initial DAG scaffolding", "author": "ml-engineer"}),
            Action(name="open_pull_request", kwargs={"repo_name": "data-pipeline-orchestrator", "title": "Feature: Initial DAG Structure", "body": "PR for the initial DAG structure.", "head_branch": "feature/initial-dag", "base_branch": "main"}),
            Action(name="request_pull_request_review", kwargs={"repo_name": "data-pipeline-orchestrator", "pr_number": 10, "reviewers": ["data-scientist"]}),
            Action(name="link_pull_request_to_issue", kwargs={"repo_name": "data-pipeline-orchestrator", "pr_number": 10, "issue_number": 12}),
            Action(name="merge_pull_request", kwargs={"repo_name": "data-pipeline-orchestrator", "pr_number": 10}),
            Action(name="close_issue", kwargs={"repo_name": "data-pipeline-orchestrator", "issue_number": 12}),
            Action(name="create_security_alert", kwargs={"repo_name": "data-pipeline-orchestrator", "severity": "medium", "description": "Hardcoded credentials in connector module.", "file": "src/connectors/db.py", "branch": "main"}),
            Action(name="create_release", kwargs={"repo_name": "data-pipeline-orchestrator", "version": "0.1.0", "description": "Initial release with basic DAG orchestration."}),
            Action(name="register_deploy_event", kwargs={"repo_name": "data-pipeline-orchestrator", "environment": "staging"}),
            Action(name="get_repository_health_summary", kwargs={"repo_name": "data-pipeline-orchestrator"}),
        ],
        outputs=[
            {
                "repo": "data-pipeline-orchestrator",
                "open_issues": 0,
                "open_prs": 0,
                "open_alerts": 1,
                "report_date": "2025-08-26"
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_104",
        instruction=(
            "As part of your role in maintaining repository health, you are to conduct a comprehensive audit of the 'acme-webapp' repository. "
            "Standard policy requires that all such audits conclude with the creation of a formal tracking issue summarizing the findings and "
            "assigning ownership for remediation. Therefore, your task is to analyze the repository's backlogs, open changes, and security "
            "posture, and then create a single, high-priority 'Post-Audit Action Plan' issue. This issue should contain the body 'This issue "
            "tracks the necessary follow-up actions from the comprehensive repository health audit.', be labeled ['audit', 'priority-high'], "
            "and be assigned to 'alice-w'. Your final deliverable is the cross-entity report reflecting the repository's state once this "
            "audit-tracking issue is in place."
        ),
        actions=[
            Action(name="get_issue_aging_report", kwargs={"repo_name": "acme-webapp"}),
            Action(name="list_pull_requests", kwargs={"repo_name": "acme-webapp", "state": "open"}),
            Action(name="get_repository_risk_score", kwargs={"repo_name": "acme-webapp"}),
            Action(name="get_open_security_alerts", kwargs={"repo_name": "acme-webapp"}),
            Action(name="create_issue", kwargs={
                "repo_name": "acme-webapp",
                "title": "Post-Audit Action Plan",
                "body": "This issue tracks the necessary follow-up actions from the comprehensive repository health audit.",
                "labels": ["audit", "priority-high"]
            }),
            Action(name="assign_issue", kwargs={"repo_name": "acme-webapp", "issue_number": 12, "assignees": ["alice-w"]}),
            Action(name="get_cross_entity_report", kwargs={"repo_name": "acme-webapp"}),
        ],
        outputs=[
            {
                "repo": "acme-webapp",
                "open_issues": 1,
                "merged_prs": 0,
                "recent_commits": 0,
                "open_alerts": 0,
                "last_deployment": "none",
                "report_date": "2025-08-26"
            }
        ],
    ),
]
