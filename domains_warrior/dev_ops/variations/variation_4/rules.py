RULES = [
    # Writing style & intent
    "Always write task instructions in SECOND PERSON ('You ...').",
    "Tasks MUST require at least one database-modifying action (not read-only only).",
    "Avoid step-by-step, procedural phrasing. State goals, constraints, and success criteria.",
    "All parameters passed to actions MUST be deterministically derivable from the instruction text, prior tool outputs, or these rules.",
    "Do NOT invent random IDs. Use canonical deterministic IDs when an ID is not provided by a tool.",

    # Canonical, deterministic identifiers
    "Deterministic automation run key: 'AUTO::automation::{automation_type}::{input_ref}::canonical'.",
    "Deterministic test run key: 'AUTO::test_run::{pipeline_id}::canonical'.",

    # Build triage & automation
    "Allowed triage statuses: in_progress, manual_review.",
    "Allowed automation completion states: completed, failed, cancelled.",
    "Automation timing is deterministic: started_at='2025-01-27T12:30:00Z', ended_at='2025-01-27T12:35:00Z', duration_ms=300000.",

    # QA / reporting
    "If a test run summary includes a report_uri, the exact URI MUST be specified in the instruction.",
    "If an instruction references ownership mapping, the file path to map MUST be explicitly provided in the instruction.",

    # Assets
    "Asset performance ratings must be one of: low, medium, high.",
]
