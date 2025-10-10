RULES = [
    # Identity & RBAC
    "Before write operations, validate target existence using stable identifiers (employee_id, account_id, mailbox_id, asset_id). If a required record is missing, do not hallucinate—record a validation issue and stop.",
    "RBAC baselines must be derived from rbac_group_map by (department, job_title); do not assign ad‑hoc groups unless the task explicitly provides them.",
    "All group membership changes must be appended to group_membership_audit with actor and timestamp.",

    # Accounts & Mailboxes
    "Directory accounts: set status strictly to one of {'enabled','disabled'}. Disabling should precede group removals in offboarding sequences.",
    "Mailboxes must respect departmental retention. Finance uses 'finance_7y'; others default to 'std_2y'.",

    # Licensing
    "License assignments must honor inventory limits: used_seats + reserved_seats <= total_seats. If capacity is insufficient, create a Jira ticket 'License Shortage', do not over‑allocate, and mark the lifecycle/ticket as blocked or on hold per context.",
    "License assign/revoke must atomically update license_assignments and license_inventory used_seats (no negative seats).",

    # Assets & MDM
    "Asset provisioning chooses from it_assets where status='in_stock'. Tie‑break by earliest purchase_date, then lexicographic asset_id.",
    "MDM enrollment and device handoff must be captured in device_workflow with a deterministic pickup_code provided by the caller.",
    "Returns must create device_workflow actions with due_ts per memo or instruction; do not change asset ownership until the return is completed.",

    # Tickets & Reporting
    "Ticket status transitions must be valid: New→(In Progress|On Hold)→(Resolved)→Closed, or New→Closed for cancellations.",
    "Daily metrics and backlog snapshots must be computed deterministically from tickets filtered by explicitly provided windows.",

    # Jira & Escalations
    "Shortages or system blockers require Jira tickets (issue_type among 'License Shortage','Hardware Shortage','Incident','Bug') and should set the related lifecycle to 'blocked' or ticket to 'On Hold'.",

    # HR Lifecycle
    "Onboarding: enqueue lifecycle, then (in order) baseline RBAC, license assignment, asset provisioning + MDM, app accounts, mailbox checks, finalize lifecycle to 'completed' only if no shortages exist.",
    "Offboarding: disable sign‑in, remove groups, revoke licenses (and decrement seats), archive mailbox (retention per policy), schedule device returns, notify manager (simulated), then mark lifecycle 'completed'.",

    # Determinism & Inputs
    "No tool may generate random IDs or dynamic timestamps. All IDs and timestamps are provided explicitly or derived deterministically from current table length (stable under identical initial state and action order).",
    "When multiple valid choices exist (assets, licenses), apply the tie‑breaker and return the chosen IDs in outputs when the task asks.",

    # Rejection & Validation
    "When required inputs are missing or inconsistent, write a validation_issues entry with details and stop rather than guessing.",
]
