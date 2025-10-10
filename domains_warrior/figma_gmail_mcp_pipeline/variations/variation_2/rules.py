RULES = [
    # Determinism & time
    "All create-style events use a fixed created timestamp; all update-style events use a fixed updated timestamp.",
    "Approvals use a fixed approval timestamp, and if the review was escalated, they use a fixed escalated-approval timestamp instead.",
    "SLA deadlines and escalation moments are recorded with fixed, deterministic timestamps.",

    # Identifier policy
    "Every new row across entities (artifacts, assets, cycles, threads, messages, comments, approvals, releases, diffs) receives a monotonic, human-readable identifier derived from current database size.",
    "Identifier generation must be reproducible across runs; never use randomness or wall-clock time.",

    # Sorting & presentation
    "Whenever returning multiple rows, sort results by the entity’s identifier in ascending order for stable output.",
    "Thread message histories are ordered by sent time and then identifier to ensure consistent playback.",

    # Artifacts
    "Artifacts capture type, naming, ownership, location, and link metadata; frame-specific fields are populated only when applicable.",
    "Artifact tags default to an empty list and should remain stable unless explicitly updated.",

    # Assets
    "Assets link to artifacts, record export profile and size, and default to a clean data-loss-prevention status with no details.",
    "When listing or grouping assets, preserve deterministic order and include only rows that match the intended artifact linkage.",

    # Review cycles
    "New review cycles begin in-flight, track SLA deadlines, and record escalation state without ambiguity.",
    "Cycle updates may adjust status, thread linkage, and escalation details; setting an escalation implies an SLA breach flag.",
    "Fetching a cycle is exact-match: either return the single cycle or a deterministic not-found response.",

    # Approvals
    "Approvals always update the parent cycle to the approved state.",
    "If a cycle is marked as breached, its approval timestamp reflects the escalated timeline.",
    "Approvals append to the ledger in deterministic order and never retroactively reorder history.",

    # Email threads & messages
    "New threads establish sender identity, recipients, labels, and initial message content; text is derived deterministically from HTML.",
    "Subsequent messages require sender authorization tied to the thread’s participants; unauthorized attempts yield a consistent error.",
    "Posting within a thread bumps the thread’s updated time using the fixed update policy and preserves ordered history.",
    "Notifications posted to a thread inherit the thread’s sender identity and follow the same HTML-to-text normalization.",

    # Comments
    "Comments anchor to artifacts, capture author and content, allow optional linkage to a source message, and store a resolved flag.",
    "Comment entries are immutable records apart from explicitly toggling resolution state in later updates.",

    # Releases & diffs
    "Releases are versioned milestones that log creation time and optional communication linkage.",
    "Release diffs capture added, updated, and removed items plus highlights and version bumps in deterministic lists.",
    "Looking up a diff by release yields exactly one row or a deterministic not-found result.",

    # Visual comparison (before/after)
    "Before/after comparisons carry forward all prior items unless explicitly removed, and include any new or updated items.",
    "Comparison outputs are returned as sorted lists to ensure repeatable results.",

    # Logging & auditability
    "Every user-visible state change appends a terminal log line with the fixed timestamp and a concise, human-readable message.",
    "Log storage keeps printed timestamps and messages aligned one-to-one for auditability, using a consistent rendering format.",

    # Defaults & constraints
    "Create events (artifacts, assets, cycles, threads, releases, diffs) use the fixed created time; updates (messages, cycle changes, approvals) use the fixed updated or approval time as applicable.",
    "All behaviors prioritize reproducibility, idempotency for repeated actions, and clear failure modes for invalid lookups or permissions."
    "Every now date uses this date '2024-08-23T12:00:00Z' as default"

    "To get any feedback for the artifact the default tag should include 'needs-review'",
    "'frame' is used as 'FRAME' in the input parameters",
    "For submitting a aproval request an artifact should be converted into asset by creating a new asset.",
    "default storage_ref location is in format of 'gs://company-assets/figma-exports/<filename>",
    "default size of newly created PNG 2x is 2000, PNG 3x is 3000, PNG 1x is 1000, SVG is 500, PDF is 200, unless specified.",
    "For submitting a approval request for asset, create a new cycle, and maintain a gmail thread throughout the process.",
    "default value of sla_deadline_ts is 2024-08-28T12:30:00Z",
    "default structure of subject for email thread related to review is 'Design Review: <filename>'",
    "default structure of html body for email thread related to review is '<p>Review for the <filename>. See attachment.</p>'",
    "default structure of html body for email thread related to request changes is '<p>Requesting changes: <message>.</p>'",
    "default structure of html body for email thread related to changes implmentation is '<p>Changes implemented: <message>.</p>'",
    "default structure of html body for email thread related to approval is '<p>Approved: <message>.</p>'",
    "default structure of html body for email thread related to new release is '<h2>Release Notes - <release_name></h2>'"
    "List of current_labels for email thread related to review should include 'Design/Needs-Review', 'figma', 'review' lables",
    "List of current_labels for email thread related to release should include 'Design/Release'",
    "Initial value status for creating a new review cycle is IN_FLIGHT, and status is updated to NEEDS_REVIEW for review tasks ",
    "Approval can be approved by changing status of review cycle to APPROVED, and a change can be requested back by changing the status of review cycle to CHANGES_REQUESTED",
    "for review cycle approval or request a change, a comment and a message should be created under the email thread",
    "gmail and figma comments should be synced, so if a review is submitted by user then user should also add a comment with content 'Submitted for review'. and if a change is requested then content of comment is 'Requested changes'."
    " and if a change is implemented then content of comment is 'Changes implemented', and if reuest is approved then content of comment is 'Approved'",
    "default value of resolved_flag while cerating a  comment is False, unless its content is 'Changes implemented' or 'Approved'"
    "For creating new artifacts, default values of artifact_type is FRAME, artifact_name is Hero Section, page_id is 1:2, current_tags is ['user', 'settings']",
    "for creating a new aritfact the filename format is <figma_file_id>_<frame_id_nullable>.png"
    "Default pattern for deeplink for creating a new artifact is 'https://www.figma.com/file/<filename>.png'"
    "For finding a thread for release note the format for the subject is '<release_name> - Release Notes' "
    "default pattern html body for release note is '<h2><release_name></h2><p>Highlights:</p><ul><li>Added frame <frame_id_nullable></li><li>Updated frame <frame_id_nullable></li><li>Removed frame <frame_id_nullable></li></ul>', based on number of added/updated/removed frames"
    "Notify the stakeholders after publishing release notes"
    "For creating new release the default value of figma_file_id is figd_abcd1234, and format of version_tag is 'release/<tag>, and for component_version_bumps is ['App update']"
    "For creating new release the version id should be taken from the release_name and it is in form of v<verison>"
    "For creating new release the the pattern for changelog_highlights is based on number of added frames, updated frames, removed frames if they are non zero number, in the format of ['Added <number of added frames> frames', 'Updated <number of updated frames> frames', 'Removed <number of removed frames> frames']"
    "For creating new release, create new artifact and asset for the added frames only."
    "Before vs after visuals are only of the output, there is no use of it as an input"

]
