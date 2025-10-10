# rules.py
# NOTE: Rules must be a plain list of strings. No code, no objects, no conditionals.
# These rules are intentionally declarative so the LLM can infer workflows without being spoon-fed steps.

RULES = [
  # =========================
  # WORKFLOWS (plain English)
  # =========================
  "WORKFLOW: review_kickoff — start a review for a Figma artifact; export assets using the specified profile; email stakeholders with the asset attached; add the 'needs-review' tag at kickoff; record the run.",
  "WORKFLOW: changes_requested_escalation — mark changes requested on a review cycle;  escalate to the named recipients with the given labels; keep discussion in the same thread; record the run.",
  "WORKFLOW: approvals_append — append one or more approvals to a review cycle at explicit timestamps; if quorum is met for the day, mark the cycle accordingly and swap tags from 'needs-review' to 'approved/<YYYYMMDD>'; record the run.",
  "WORKFLOW: rereview_kickoff — request a re-review after fixes; notify the listed recipients using the re-review notice template; continue in the existing day's thread; record the run.",
  "WORKFLOW: release_handoff — get changes since the previous release tag; attach a fresh export; email handoff to stakeholders; add the tag 'released/<YYYYMMDD>' on the artifact; record the run.",
  "WORKFLOW: sync_email_to_figma — sync the latest Gmail thread message into the target Figma artifact as a comment; keep reference to the thread; record the run.",
  #"WORKFLOW: governance_update — update tags/metadata on a Figma artifact (add/remove) as directed; record the run.",
  "WORKFLOW: a11y_audit_report — read accessibility findings for the named audit across the specified categories only; produce a PDF report from those findings; record the run.",
  "WORKFLOW: ds_audit_report — read design-system findings for the named audit across the specified categories only; produce a PDF report from those findings; record the run.",
  "WORKFLOW: combined_audit_report — read both A11Y and DS findings for the named audit; produce a single combined PDF report; record the run.",
  "WORKFLOW: fixplan_create_and_deliver — create a minimal fix plan from available findings; if no relevant findings exist, deliver an empty plan (no synthesized items); deliver via one of {COMMENTS, TICKETS, PDF, EMAIL} as instructed; record the run. use the deliver method for the 'content' field in create_figma_comment",
  "WORKFLOW: fix_item_status_update — after a plan is delivered, update one or more fix item statuses (e.g., APPLIED/DEFERRED) using references produced during delivery (comment id or ticket id); record the run.",

  # =========================
  # THREAD & EMAIL POLICIES
  # =========================
  "THREAD_POLICY: Other than changes_requested_escalation, Maintain a single Gmail thread per artifact per <YYYYMMDD>; continue an existing on the same-day thread if present; otherwise start a new one.",
  "SUBJECT_OVERRIDE_RULE: When continuing an existing thread on the same day for the same artifact, do not generate a new subject; reply in-thread.",
  "EMAIL_LABEL_RULE: Apply only labels provided in the instruction or templates; do not invent labels.",
  "EMAIL_CHECKLIST_RULE: Before sending emails ensure to include attachments when the instruction requires the exported asset.",
  "ASSET_ATTACHMENT_RULE: If the instruction says the review email must include the exported asset, that asset must be attached; do not substitute or omit.",
  "EXPORT_PROFILE_RULE: Use exactly the export profile specified in the instruction; do not invent or change profiles.",
  "SYNC_POLICY: When syncing an email to Figma as a comment, reference the dataset-provided thread_id; do not synthesize any thread identifiers.",

  # =========================
  # APPROVALS, QUORUM & SLA
  # =========================
  "QUORUM_RULE: Quorum is met when at least 2 approvals are recorded for the same review cycle within the same <YYYYMMDD> as the instruction timestamp.",
  "CHANGES_REQUESTED_SLA_RULE: If the instruction references an SLA, treat it as elapsed only if the provided timestamps demonstrate the delay window has passed; escalate to the listed recipients with the given labels; do not invent recipients or labels.",

  # =========================
  # AUDIT CATEGORIES (allowed)
  # =========================
  "A11Y_CATEGORIES_ALLOWED: {COLOR_CONTRAST, ALT_TEXT, FOCUS_ORDER}",
  "DS_CATEGORIES_ALLOWED: {COMPONENT_MISMATCH, SPACING, TOKENS, UNMAPPED, AMBIGUOUS}",
  "AUDIT_SCOPE_RULE: When a category list is provided in the instruction, only include findings from those categories in the report; do not include other categories.",

  # =========================
  # RELEASE / DIFF POLICY
  # =========================
  "RELEASE_DIFF_RULE: When asked to summarize changes since the previous release, determine the latest prior tag with prefix 'release/' and base the summary on that diff; do not invent a prior tag.",
  "RELEASE_TAGGING_RULE: After a successful handoff, add the tag 'released/<YYYYMMDD>' to the artifact where <YYYYMMDD> comes from the instruction timestamp date.",

  # =========================
  # GOVERNANCE TAG RULES
  # =========================
  # "GOVERNANCE_AT_KICKOFF: On review kickoff, add the tag 'needs-review' to the artifact unless the instruction explicitly says otherwise.",
  # "GOVERNANCE_ON_QUORUM: When quorum is met, swap 'needs-review' for 'approved/<YYYYMMDD>' where date derives from the instruction timestamp.",
  # "GOVERNANCE_UPDATE_RULE: Only modify tags explicitly requested by instruction or workflow policy; do not invent tags.",

  # =========================
  # ID RULES (deterministic)
  # =========================
  "ID_RULE: request_id — prefixes by operation: en- (provisioning/creates); rv- (review); au- (audit); rl- (release); em- (email); up- (updates). Pattern: <prefix><seq>, where seq is zero-padded to 3 digits starting at 001 per task (e.g., rv-001). Do not mandate request_id to the tools that doesnt require that field.",
  "ID_RULE: review_cycle_id — rev-<artifact_id>-<YYYYMMDD>-<seq> (seq starts at 1 per artifact_id per <YYYYMMDD>).",
  "ID_RULE: audit_id — aud-<artifact_id>-<YYYYMMDD>-<seq>.",
  "ID_RULE: export_id — exp-<artifact_id>-<YYYYMMDD>-<format>-<seq> (format ∈ {png,pdf,zip}).",
  "ID_RULE: fixplan_id — fp-<artifact_id>-<YYYYMMDD>-<seq>.",
  "ID_RULE: fix_item_id — fpi-<fixplan_id>-<seq>.",
  "ID_RULE: release_id — rel-<artifact_id>-<YYYYMMDD>-<seq>.",
  "ID_RULE: email_draft_id — ed-<thread_or_artifact>-<YYYYMMDDThhmmssZ>.",
  "ID_RULE: gmail_thread_id — MUST use the dataset-provided thread_id; never fabricate.",
  "ID_RULE: timestamp_derivation — every ISO8601Z used by tools must appear in the instruction; the <YYYYMMDD> used in IDs comes from that timestamp.",
  "ID_RULE: sequencing — unless otherwise stated, seq increments with each new ID emitted in the SAME task and namespace.",
  "CYCLE_ALIAS_RULE: Use dataset aliases for legacy cycle ids — e.g., cycle_001 ⇒ art_001."
  "OVERRIDE: Always accept and use tool generated IDs as valid ID even if its not following above rules."
  
  

  # =========================
  # TEMPLATE FAMILIES & VERSIONS
  # =========================
  "TEMPLATE_FAMILY: email.review_request — ACTIVE=v2; SUBJECT=email.review_request.v2_subject; BODY=email.review_request.v2_body; FALLBACK_SUBJECT=email.generic_plain.v1_subject; FALLBACK_BODY=email.generic_plain.v1",
  "TEMPLATE_FAMILY: email.rereview_notice — ACTIVE=v1; SUBJECT=email.rereview_notice.v1_subject; BODY=email.rereview_notice.v1",
  "TEMPLATE_FAMILY: email.release_handoff — ACTIVE=v1; SUBJECT=email.release_handoff.v1_subject; BODY=email.release_handoff.v1",
  "TEMPLATE_FAMILY: email.fixplan_delivery — ACTIVE=v1; SUBJECT=email.fixplan_delivery.v1_subject; BODY=email.fixplan_delivery.v1",
  "TEMPLATE_FAMILY: email.generic_plain — ACTIVE=v1; SUBJECT=email.generic_plain.v1_subject; BODY=email.generic_plain.v1",

  "TEMPLATE_SELECTION_RULE: If the instruction provides an explicit subject/body, use it verbatim and ignore templates.",
  "TEMPLATE_SELECTION_RULE: Else, if the instruction names a specific template key, use that exact key.",
  "TEMPLATE_SELECTION_RULE: Else, route by intent phrase in the instruction: 'email-based design review' ⇒ email.review_request (use ACTIVE version); 're-review' ⇒ email.rereview_notice; 'release handoff' ⇒ email.release_handoff; 'email the plan' ⇒ email.fixplan_delivery; otherwise ⇒ email.generic_plain (ACTIVE).",
  "TEMPLATE_SELECTION_RULE: If multiple ACTIVE versions are declared for a family, choose the highest semantic version (v3 > v2 > v1).",
  "TEMPLATE_VERSIONING_RULE: Only one ACTIVE version per template family; older versions must be marked DEPRECATED.",
  "TEMPLATE_DEPRECATED: email.review_request.v1",
  "TEMPLATE_DEPRECATED: email.generic_plain.v0",
  "TEMPLATE_DEPRECATED: email.release_handoff.v0",

  # =========================
  # TEMPLATE TOKEN RULES
  # =========================
  "TEMPLATE_TOKENS_ALLOWED: TEMPLATE_TOKENS_ALLOWED: {artifact_id}, {date}, {export_profile}, {release_id}, {prev_tag}, {owner_email}, {recipients}, {audit_id}, {asset_id}, {thread_id}",
  "TEMPLATE_TOKEN_SOURCE_RULE: {date} is derived from the instruction timestamp (YYYY-MM-DD).",
  "DATE_FORMAT_RULE: {date} must use YYYY-MM-DD derived from the ISO8601Z instruction time.",
  "MISSING_TOKEN_RULE: If a required token is unavailable, leave it blank or omit the phrase; do not invent content.",

  # =========================
  # EMAIL TEMPLATES (subjects/bodies)
  # =========================
  "TEMPLATE: email.review_request.v2_subject = \"Review Request — {artifact_id} — {date}\"",
  "TEMPLATE: email.review_request.v2_body = \"Hi team,\\nPlease review the attached {export_profile} export for {artifact_id}.\\nThanks.\"",
  "TEMPLATE: email.rereview_notice.v1_subject = \"Re-review Needed — {artifact_id} — {date}\"",
  "TEMPLATE: email.rereview_notice.v1 = \"Fixes have been applied on {artifact_id}; please re-review the latest assets.\"",
  "TEMPLATE: email.release_handoff.v1_subject = \"Release Handoff — {release_id} — {date}\"",
  "TEMPLATE: email.release_handoff.v1 = \"Hello stakeholders,\\nPlease find the release notes for {release_id}, including changes.\\nRegards.\"",
  "TEMPLATE: email.fixplan_delivery.v1_subject = \"Fix Plan — {artifact_id} — {date}\"",
  "TEMPLATE: email.fixplan_delivery.v1 = \"Hello,\\nThe fix plan for {artifact_id} is attached/delivered as requested.\\nThanks.\"",
  "TEMPLATE: email.generic_plain.v1_subject = \"Update — {date}\"",
  "TEMPLATE: email.generic_plain.v1 = \"Hello,\\nPlease see details attached.\\nThanks.\"",





  "TEMPLATE_FAMILY: figma.comment.sync — ACTIVE=v1; BODY=figma.comment.sync.v1",
  "TEMPLATE: figma.comment.sync.v1 = \"Synced from Gmail thread {thread_id} on {date}.\"",

  # "SENDER_SELECTION_RULE: If the instruction does not specify a sender, map by role using SENDER_ROLE_MAP.",
  # "SENDER_ROLE_MAP: {'design review coordinator':'sarah.designer@company.com'}",
  # "SENDER_ROLE_MAP: {'design review coordinator':'sarah.designer@company.com'}",

  "TEMPLATE_FAMILY: figma.comment.sync — ACTIVE=v1; BODY=figma.comment.sync.v1",
  "TEMPLATE: figma.comment.sync.v1 = \"Synced from Gmail thread {thread_id} on {date}.\"",
  "COMMENT_AUTHOR_RULE: For sync_email_to_figma, set author_email to design-review@company.com unless explicitly provided.",

  "TEMPLATE_FAMILY: figma.comment.audit_report_sent — ACTIVE=v1; BODY=figma.comment.audit_report_sent.v1",
  "TEMPLATE_SELECTION_RULE: For logging audit report delivery to Figma comments, use figma.comment.audit_report_sent (ACTIVE).",
  "TEMPLATE: figma.comment.audit_report_sent.v1 = 'Audit report sent — {artifact_id} — {audit_id} — {date} — asset {asset_id}'",

  'TEMPLATE_FAMILY: email.sync_confirmation — ACTIVE=v1; SUBJECT=email.sync_confirmation.v1_subject; BODY=email.sync_confirmation.v1',
  'TEMPLATE: email.sync_confirmation.v1_subject = "Sync to Figma — {artifact_id} — {date}"',
  'TEMPLATE: email.sync_confirmation.v1 = "Thread {thread_id} synced to {artifact_id} on {date}."',
  'TEMPLATE_SELECTION_RULE: For a post-sync acknowledgement email, use email.sync_confirmation (ACTIVE).',


  "SENDER_SELECTION_RULE: If the instruction does not specify a sender, map by role using SENDER_ROLE_MAP.",
  "SENDER_ROLE_MAP: {'design review coordinator':'sarah.designer@company.com','review program manager':'design-review@company.com', 'design systems triage lead':'sarah.designer@company.com', 'governance steward' : 'sarah.designer@company.com' , 'accessibility audit lead': 'design-review@company.com'}",


  # Changes-requested escalation (so the body/subject aren’t invented)
  "TEMPLATE_SELECTION_RULE: If the instruction mentions 'changes-requested' or 'escalate' for a review cycle, use email.changes_requested (ACTIVE). user v1 if there is a 'artifact_id' present in the context. use v2 if there is no 'artifact_id' present in the context.",
  "TEMPLATE: email.changes_requested.v1_subject = \"Changes Requested — {date}\"",
  "TEMPLATE: email.changes_requested.v1 = \"Changes requested for {artifact_id}. Continuing in today’s thread.\"",
  "TEMPLATE: email.changes_requested.v2 = \"Changes requested. Continuing in today’s thread.\"",

  # Consolidated review subject/body for multi-artifact kickoffs
  "TEMPLATE_FAMILY: email.review_request_consolidated — ACTIVE=v1; SUBJECT=email.review_request_consolidated.v1_subject; BODY=email.review_request_consolidated.v1",
  "TEMPLATE: email.review_request_consolidated.v1_subject = \"Review Request — Consolidated — {date}\"",
  "TEMPLATE: email.review_request_consolidated.v1 = \"Hi team,\\nPlease review the attached {export_profile} exports.\\nThanks.\"",

  # Figma sync comment content
  "TEMPLATE_FAMILY: figma.comment.sync — ACTIVE=v1; BODY=figma.comment.sync.v1",
  "TEMPLATE: figma.comment.sync.v1 = \"Synced from Gmail thread {thread_id} on {date}.\"",

  # Optional: cycle→artifact alias so approvals can swap tags deterministically (edit as your dataset requires)
  "CYCLE_ALIAS: {'cycle_008':'art_001','cycle_005':'art_003'}",

  # =========================
  # DATA & ERROR SAFETY
  # =========================
  "DATA_RULE: Never invent artifacts, audits, releases, threads, or recipients; use only IDs present in instruction or returned by tools.",
  "DATA_RULE: For fix plans, do not synthesize items when no relevant findings are available; an empty plan is acceptable.",
  "ERROR_RULE: If required data is missing (e.g., export profile, recipients, audit categories), fail with a clear error message and do not substitute values.",
  "OUTPUT_RULE: Task outputs must be directly derived from tool results; do not duplicate keys; normalize status values to lowercase (e.g., 'completed'). This does not apply to tool and action outputs.",
]
