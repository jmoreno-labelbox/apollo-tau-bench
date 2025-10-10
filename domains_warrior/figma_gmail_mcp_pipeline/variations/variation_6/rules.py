RULES = [
    # §0. Format & Purpose
    "§0.1 This document is a declarative policy list. Each item is a plain string; no code or conditionals.",
    "§0.2 The rules enumerate canonical IDs, templates, and policies so tools and tasks can reference values without inventing them.",
    "§0.3 Any action parameter must be sourced from: (a) these rules, or (b) the instruction text, or (c) a prior tool output in the same task.",

    # §1. Scope & Roles
    "§1.1 The agent acts as the Design Review Coordinator for the Figma↔Gmail workflow.",
    "§1.2 The workflow covers: review cycle creation/reuse, asset export, email thread creation/reuse, message posting, reply mirroring to Figma comments, approvals, and final status readout.",
    "§1.3 The agent may also act as the Release Publisher for email-based release handoffs.",
    "§1.4 The agent may also act as the Accessibility Audit Lead for email-based accessibility reviews.",
    "§1.5 The agent may also act as the Design Systems Triage Lead for design-system issue coordination.",
    "§1.6 The agent may also act as the Review Program Manager for in-flight review coordination and reminders.",
    "§1.7 The agent may also act as the Change Request Lead for communicating requested design changes.",
    "§1.8 The agent may also act as the Fix Plan Delivery Owner.",
    "§1.9 The agent may alsoact as the Fix Item Status Updater.",
    "§1.10 The agent may also act as the Audit Report Generator.",

    # §2. Determinism & Idempotency
    "§2.1 All writes are deterministic and idempotent; re-running the same task with the same inputs yields the same records.",
    "§2.2 Request namespaces produce stable IDs: thr_<request_id>, msg_<request_id>, asset_<request_id>, run_<request_id>.",
    "§2.3 If an entity for the same logical key already exists (cycle, thread, export, message), reuse it rather than creating a duplicate.",
    "§2.4 Do not write dynamic timestamps; when a time is required it must come from the instruction verbatim.",

    # §3. Time & Day Policy
    "§3.1 The 'day' used for deterministic grouping is the YYYY-MM-DD derived from the instruction timestamp.",
    "§3.2 All same-day operations related to one artifact should reference the same deterministic thread and consistent IDs.",

    # §4. Canonical Literals (Surfaces exact strings to avoid validation warnings)
    "§4.1 Canonical export profile for review and for release handoff: 'PNG 2x'.",
    "§4.2 Canonical review label for Gmail threads: 'Design/Needs-Review'.",
    "§4.3 Canonical review recipients allowed (array): ['design-review@company.com','ux-team@company.com', 'growth-team@company.com'] (order-insensitive).",
    "§4.4 Canonical review subject (single-message review): 'Design Review Request: 1 frames ready for review'.",
    "§4.5 Canonical review request body (exact text): 'Hi team, please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z'.",
    "§4.6 Canonical artifact name for art_001: 'Homepage Hero Section'.",
    "§4.7 Canonical asset id in this project when exported deterministically with request namespace en-002: 'asset_en-002' (example used in tasks).",
    "§4.8 Canonical cycle id allowed (array): ['rev-art_001-20240823-001', 'rev-art_002-20240824-001'] (order-insensitive).",
    "§4.9 Allowed request namespaces for this dataset: 'en-001', 'en-002', 'em-001', 'em-002', 'up-001', 'rv-001', 'rl-001', 'ax-001', 'ax-002', 'ax-003', 'ax-004', 'ds-001', 'ds-002', 'ds-003', 'ds-004', 'em-003', 'cr-001', 'cr-002', 'cr-003', 'cr-004', 'up-002', 'up-003', 'au-001', 'au-002', 'fp-001', 'fp-002'.",
    "§4.10 Canonical sender: 'sarah.designer@company.com'.",
    "§4.11 Canonical governance tag for review: 'needs-review'.",
    "§4.12 Canonical automation task name for review: 'review_kickoff'.",
    "§4.13 Canonical automation status: 'completed'.",
    "§4.14 Canonical release source id: 'release_001'.",
    "§4.15 Canonical generated release id for this dataset: 'rel-art_001-20240823-001'.",
    "§4.16 Canonical release recipients allowed (array): ['stakeholders@company.com','product-managers@company.com'] (order-insensitive).",
    "§4.17 Canonical release subject: 'Release Handoff — rel-art_001-20240823-001 — 2024-08-23'.",
    "§4.18 Canonical release body: 'Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes. Regards.'",
    "§4.19 Canonical governance tag for released builds: 'released/2024-08-23'.",
    "§4.20 Canonical automation task name for release: 'release_handoff'.",
    "§4.21 Canonical accessibility recipients allowed (array): ['accessibility@company.com','design-review@company.com'] (order-insensitive).",
    "§4.22 Canonical accessibility label: 'Design/Accessibility'.",
    "§4.23 Canonical accessibility subject: 'Accessibility Audit: Homepage Hero Section'.",
    "§4.24 Canonical accessibility body: 'Hi team, please perform an accessibility audit on Homepage Hero Section against WCAG 2.2 AA. Deadline: 2024-08-24T18:00:00Z'.",
    "§4.25 Canonical governance tag for accessibility: 'a11y/needs-audit'.",
    "§4.26 Canonical automation task name for accessibility: 'accessibility_audit_kickoff'.",
    "§4.27 Canonical design-systems recipients allowed (array): ['design-systems@company.com','frontend-guild@company.com'] (order-insensitive)."
    "§4.28 Canonical design-systems label: 'Design/Design-System'.",
    "§4.29 Canonical design-systems subject: 'Design System Triage: Homepage Hero Section'.",
    "§4.30 Canonical design-systems body: 'Hi team, please triage component and token issues found in Homepage Hero Section. Deadline: 2024-08-26T17:00:00Z'.",
    "§4.31 Canonical governance tag for design system triage: 'ds/triage-open'.",
    "§4.32 Canonical automation task name for design-systems: 'design_systems_triage'.",
    "§4.33 Canonical reminder body: 'Reminder: please review the attached design: Homepage Hero Section. Deadline: 2024-08-23T15:00:00Z'.",
    "§4.34 Canonical changes-request label: 'Design/Changes-Requested'.",
    "§4.35 Canonical changes-request subject: 'Changes Requested: Homepage Hero Section'.",
    "§4.36 Canonical changes-request body: 'Hi team, changes are requested for Homepage Hero Section. Please address the comments and re-submit. Deadline: 2024-08-26T17:00:00Z'.",
    "§4.37 Canonical governance tag for change requests: 'needs-changes'.",
    "§4.38 Canonical automation task name for change_request: 'change_request'.",
    "§4.39 Allowed fix plan delivery methods: 'COMMENTS', 'TICKETS', 'PDF', 'EMAIL'.",
    "§4.40 Allowed fix item statuses: 'PENDING', 'APPLIED'.",
    "§4.41 Allowed report formats: 'PDF'.",
    "§4.42 Canonical automation task name for fix item status update: 'fix_item_status_update'.",
    "§4.43 Canonical automation task name for fix plan delivery: 'fixplan_create_and_deliver'.",
    "§4.44 Canonical automation task name for combined audit report: 'combined_audit_report'.",
    "§4.45 Deterministic request namespaces for the 2024-08-23 release handoff on art_001: export=en-002, cycle=rv-001, thread=em-001, message=em-002, tags=up-001, run=rl-001.",
    "§4.46 Canonical release body (diff variant): 'Hello stakeholders, please find the release notes for rel-art_001-20240823-001, including changes since release_001. Regards.'",
    "§4.47 Deterministic namespaces for 2024-08-23 fix-item updates on plan_012 (audit_012): item_017=up-001, item_018=up-002, run=up-003.",
    "§4.48 Deterministic namespaces for 2024-08-24 fix-item updates on plan_012 (audit_012): item_017=up-001, item_019=up-002, run=up-003.",
    "§4.49 Deterministic namespaces for 2024-08-25 fix-item updates on plan_012 (audit_012): item_017=up-001, item_020=up-002, run=up-003.",
    "§4.50 Deterministic namespaces for 2024-08-26 fix-item updates on plan_012 (audit_012): item_018=up-001, item_019=up-002, run=up-003.",
    "§4.51 Deterministic namespaces for 2024-08-27 fix-item updates on plan_012 (audit_012): item_018=up-001, item_020=up-002, run=up-003.",
    "§4.52 Deterministic namespaces for 2024-08-28 fix-item updates on plan_012 (audit_012): item_019=up-001, item_020=up-002, run=up-003.",
    "§4.53 Canonical report asset id for this run: 'asset_au-001'.",
    "§4.54 Deterministic namespaces for 2024-08-23 combined audit report (audit_012, art_001): report=au-001, run=au-002.",
    "§4.55 Canonical artifact name for art_002: 'Pricing Page – Plans Grid'.",
    "§4.56 Canonical review subject (two-frame): 'Design Review Request: 2 frames ready for review'.",
    "§4.57 Canonical review body for art_002: 'Hi team, please review the attached design: Pricing Page – Plans Grid. Deadline: 2024-08-26T17:00:00Z'.",
    "§4.58 Canonical review recipients (variant): ['design-review@company.com','growth-team@company.com'] (order-insensitive).",
    "§4.59 Deterministic namespaces for 2024-08-24 review on art_002: cycle=rv-002, export=en-004, thread=em-004, message=em-005, tags=up-004, run=rv-004.",
    "§4.60 Canonical fixplan digest recipients: ['fix-owners@company.com','design-review@company.com'] (order-insensitive).",
    "§4.61 Canonical fixplan label: 'FixPlan/Owners'.",
    "§4.62 Canonical fixplan subject: 'Fix Plan Delivery: plan_011 — pending items'.",
    "§4.63 Canonical fixplan body: 'Please review the pending items for plan_011. Deadline: 2024-08-26T17:00:00Z'.",
    "§4.64 Deterministic namespaces for 2024-08-23 fixplan delivery (plan_011): summary=fp-001, comments=fp-002, tickets=fp-003, thread=fp-004, message=fp-005, tag=fp-006, run=fp-007.",
    "§4.65 Canonical governance tag for delivered fix plans: 'fixplan/delivered'.",
    "§4.66 Canonical team tag: 'WEBUX'",

    # §5. Templates & Content Sourcing
    "§5.1 Subjects, bodies, labels, and recipients must match the exact strings from §4 unless the instruction explicitly overrides them.",
    "§5.2 When a template family is used, its resolved subject/body must appear in either the rules (this section) or the instruction.",
    "§5.3 The agent must not invent new labels, subjects, or recipients; use only values surfaced in §4 or instruction.",

    # §6. Review Cycle Policy
    "§6.1 There is at most one open review cycle per artifact; if an open cycle exists, reuse it.",
    "§6.2 New cycles, when created deterministically for a given day, should use a stable ID of the form rev-<artifact_id>-<YYYYMMDD>-NNN.",
    "§6.3 The default open-cycle status is 'NEEDS_REVIEW' and transitions to 'APPROVED' when quorum is met.",
    "§6.4 The cycle stores recipients and an optional linked thread_id; this linkage must be stable within a task run.",

    # §7. Gmail Thread Policy
    "§7.1 Maintain a single Gmail thread per artifact per instruction day.",
    "§7.2 Prefer the cycle's existing linked thread_id if present and found.",
    "§7.3 Otherwise reuse a thread by natural key (subject, recipients, labels) using the strings from §4.",
    "§7.4 Only when no thread matches §7.2–§7.3, create a new deterministic thread (thr_<request_id>) and link it to the open cycle.",
    "§7.5 All subsequent email posts and sync operations must use the cycle-linked thread_id (no hard-coded placeholders).",

    # §8. Asset Export Policy
    "§8.1 Export the artifact's review frame using the exact profile from §4.1.",
    "§8.2 Reuse an existing export for the same (artifact_id, export_profile) pair on repeat runs; do not create duplicates.",
    "§8.3 The deterministic asset id may be provided by tools via request namespace (e.g., 'asset_en-002'); tasks should reuse it once surfaced.",

    # §9. Approvals & Quorum
    "§9.1 Count unique 'APPROVE' intents per cycle by approver email.",
    "§9.2 An approver cannot be double-counted for the same cycle.",
    "§9.3 The cycle transitions to 'APPROVED' when approvals ≥ the configured quorum; otherwise it remains in its prior state.",

    # §10. Data Normalization & Safety
    "§10.1 Tools must normalize tables and ignore non-dict rows; never call dict methods on lists.",
    "§10.2 Validate foreign keys before writes: artifact must exist to export; thread must exist to post; asset ids must exist to attach.",
    "§10.3 If a required entity is missing, return a deterministic error; do not fabricate rows to satisfy dependencies.",

    # §11. Sourcing & Echo Rules (prevents 'value not found' warnings)
    "§11.1 Any literal used in an action (subject, body_html, labels, recipients, export profile, artifact/asset ids) must be present in these rules (§4/§5), the instruction, or a prior tool output.",
    "§11.2 When using values from §4 (canonical literals), reuse the strings verbatim; do not paraphrase or alter punctuation.",
    "§11.3 If an action depends on a value produced by a previous action (e.g., asset id or thread id), pass that exact returned value forward without modification.",
    "§11.4 If the instruction supplies an explicit literal that conflicts with a canonical value in §4, prefer the instruction's literal for this task run and propagate it consistently.",
    "§11.5 Accessibility literals (recipients/label/subject/body/tag) must be reused verbatim from §4 unless the instruction overrides them.",
    "§11.6 Design-systems literals (recipients/label/subject/body/tag) must be reused verbatim from §4 unless the instruction overrides them.",
    "§11.7 Change-request literals (label/subject/body/tag) must be reused verbatim from §4 unless the instruction overrides them.",

    # §12. Output Discipline
    "§12.1 The final output must be sourced from authoritative tool getters (e.g., read the cycle) and return only the values requested by the task (cycle_id, final_status, etc.).",

    # §13. Fix Plans & Audits Policy
    "§13.1 A fix plan delivery is idempotent per run namespace; COMMENTS mirrors non-applied items as Figma comments.",
    "§13.2 Fix item status updates must normalize status to uppercase and record an audit trail.",
    "§13.3 Combined audit reports must validate audit_id and artifact_id, and produce a deterministic report_id and asset_id.",
    "§13.4 All outputs (plan delivery row, item updates, report row) must be sourced to deterministic IDs derived from request_id or next-increment.",

    # §14 Release Policy
    "§14.1 Release IDs use compact dates: rel-<artifact_id>-<YYYYMMDD>-001.",
    "§14.2 Export IDs use compact dates: exp-<artifact_id>-<YYYYMMDD>-<fmt>-001 where fmt∈{png,pdf}.",
]
