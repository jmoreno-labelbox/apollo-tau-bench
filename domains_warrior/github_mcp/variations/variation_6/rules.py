RULES = [
    # Judge Evaluation Criteria for GitHub MCP Task Execution

    # Core Execution Standards
    "Tasks must execute successfully using only the provided GitHub MCP tools.",
    "All tool calls must use valid parameters that exist in the task instruction or previous tool outputs.",
    "Task execution must follow a logical workflow from authentication to completion.",
    "Tasks must produce the exact deliverables specified in the instruction.",

    # Authentication Validation
    "Authentication must be performed first using get_me with valid username and auth_key.",
    "Authentication tokens must follow the GitHub pattern and be valid for the specified user.",
    "Username must match the token owner for successful authentication.",

    # Repository Operations Validation
    "Repository operations must use valid repository names and owners.",
    "Repository creation must include appropriate parameters (name, description, private/public, autoInit).",
    "Repository deletion must be preceded by verification of repository existence.",
    "Repository naming conflicts must be handled by appending '_v2' suffix. When creating a new repository with an existing name, the output repository name will be 'original_name_v2'.",

    # File Operations Validation
    "File operations must use valid file paths relative to repository root.",
    "File content must be properly formatted and syntactically correct for the file type.",
    "File operations on branches must verify branch existence before execution.",
    "Commit messages must be descriptive and follow conventional commit format.",

    # Version Control Validation
    "Branch creation must use valid commit SHAs from list_commits outputs.",
    "Branch names must follow standard patterns (feature/, bugfix/, etc.).",
    "Pull request creation must include valid source and target branches.",
    "Pull request titles and descriptions must match instruction specifications.",

    # Issue Management Validation
    "Issue creation must include required fields (title, body, labels, assignees).",
    "Issue numbers must be captured from create_issue returns for subsequent operations.",
    "Issue updates must modify only the specified fields (title, body, labels, assignees).",
    "Issue comments must contain the exact text specified in the instruction.",

    # Pull Request Validation
    "Pull request operations must use valid PR numbers from create_pull_request returns.",
    "Pull request reviews must include appropriate body text and state.",
    "Pull request merging must use valid merge methods (squash, merge, rebase).",
    "Pull request status checks must verify the correct PR state.",

    # Code Analysis Validation
    "Code search queries must be specific and relevant to the task goal.",
    "Security scanning must check for actual vulnerabilities in the specified repository.",
    "Code scanning alerts must be properly categorized and documented.",

    # Workflow Logic Validation
    "Task execution must follow logical dependency chains between tool calls.",
    "Verification steps must only verify what was actually created or modified.",
    "Tasks must not include unnecessary tool calls unrelated to the deliverable.",
    "Multi-step workflows must derive later parameters from earlier tool outputs.",

    # Output Validation
    "Task outputs must match the exact values specified in the instruction.",
    "All required deliverables must be successfully created and verified.",
    "Task completion must be confirmed through appropriate verification steps.",
    "No extraneous data gathering beyond what's required for the task goal.",

    # Error Handling Validation
    "Tasks must handle potential errors gracefully (repository not found, file not found, etc.).",
    "Tasks must not use hardcoded values that don't exist in the system.",
    "Tasks must reject operations that cannot be completed with available tools.",
    "Tasks must provide meaningful error messages when operations fail.",

    # Instruction Compliance Validation
    "Task execution must follow the exact deliverable specified in the instruction.",
    "All action parameters must be traceable to the instruction text.",
    "Instructions must be goal-oriented, not procedural step-by-step guidance.",
    "Task complexity must match the specified difficulty level (Hard/Expert).",

    # Real-world Authenticity Validation
    "Tasks must represent realistic GitHub workflows that developers would actually perform.",
    "Tool usage must demonstrate understanding of GitHub's actual API patterns.",
    "Workflows must be efficient and avoid unnecessary data gathering.",
    "Task scenarios must be plausible and relevant to real development practices.",

    # Quality Standards Validation
    "Code implementations must follow standard programming conventions.",
    "Documentation updates must be meaningful and well-structured.",
    "Security practices must follow industry standards.",
    "UI/UX improvements must include accessibility considerations.",

    # Default Values and Common Parameters
    "The state 'open' is the default for list_issues and list_pull_requests operations unless otherwise specified.",
    "The branch 'main' is the default branch for repository operations unless otherwise specified.",
    "Common parameters like 'open' and 'main' are implicitly available for tool calls.",

    # Issue Discovery and Selection Guidelines
    "When instructions refer to 'most recent issue', 'latest issue', or 'existing issues', the agent must discover the actual issue numbers through repository exploration.",
    "Issue discovery should prioritize open issues unless the instruction specifies otherwise.",
    "When multiple issues exist, 'most recent' refers to the highest issue number in the repository.",
    "Issue selection criteria should be based on issue state, labels, or creation date as specified in the instruction.",
    "The agent should not assume specific issue numbers without first discovering what issues exist in the repository.",

    # Repository Discovery and Creation Guidelines
    "When creating new repositories, the agent should first explore existing repositories to understand naming patterns and available labels.",
    "Repository creation workflows should examine related existing repositories to inform the setup of new repositories.",
    "The agent should discover available labels from existing repositories before applying them to new repositories.",
    "Repository naming conflicts should be resolved by checking existing repositories before creation.",

    # Pull Request Workflow Guidelines
    "When pull request checks are pending or failing, the agent should output the message 'Pull request cannot be merged: required checks are still pending. All checks must pass before merging.' and stop the merge workflow.",
    "Pull request merge workflows should verify all required checks are passing before attempting to merge.",
    "Pull request review workflows should include status verification as a prerequisite for merging.",
]
