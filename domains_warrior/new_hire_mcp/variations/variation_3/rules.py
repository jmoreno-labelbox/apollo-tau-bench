RULES = [
    # Candidates
    "Use candidate_ids from candidates.json. New candidate_ids are not allowed.",
    "Candidate updates should reflect deterministic updates; if multiple updates are possible, at least one valid update is acceptable.",

    # Asset Requests
    "Asset requests should be updated using IDs from asset_requests.json. If multiple requests exist, updating a subset is allowed as long as end state matches instructions.",
    "Assignments must correspond to approved requests when feasible. If approval steps are missing but assignment is valid in dataset, it is acceptable.",

    # Checklist Items
    "Checklist items should reference checklist_items.json. Completing some items is acceptable if full set is not specified.",
    "Terminal logs for checklist completion should be recorded when possible; missing logs are acceptable if underlying updates are valid.",

    # Access Checks
    "Access checks must use candidate_ids and types from access_checks.json. Full set approval is encouraged but partial approval is acceptable.",
    "Terminal logs for access approvals should be recorded; if missing, partial credit is acceptable.",

    # Attachments / Onboarding Files
    # "Only existing file paths and candidate_ids from attachments/onboarding_files.json may be used. Updates must be deterministic when possible.",
    "Use existing file paths and candidate_ids from attachments/onboarding_files.json, if missing new ids are acceptable.",
    "Terminal logs for file updates should be recorded; missing logs are acceptable if updates themselves are correct.",
    "Attachment IDs in add_attachment actions should use existing IDs from the dataset when available. Invented IDs are acceptable only if they correctly represent a new or additional attachment and do not conflict with dataset items.",

    # Emails / Labels
    "Use email_ids and label_ids from emails/email_labels.json. Partial application of labels is acceptable.",
    "Terminal logs for email labeling should be recorded; missing logs are acceptable if labels themselves are correctly applied.",

    # General Workflow
    "All actions should aim for end state described in instructions. Missing intermediate logs or steps may be tolerated if the resulting state matches the instruction.",
    "Do not invent new IDs or records outside datasets. Actions must be verifiable against datasets where possible.",
    "The instruction must clearly describe the desired end state or outcome for the task.",
    "Procedural language (like 'approve', 'assign', 'send') is allowed if the instruction still conveys the overall goal unambiguously.",
    "Tasks are considered valid if a reader can understand the intended final state without needing step-by-step guidance.",
    # New
    "Instructions may include explicit actions (release, assign, remove, add, attach, apply, complete, log, update) if necessary to clarify the task, even if they resemble procedural steps, as long as the main goal or end state is clearly defined.",
    "Enumerating procedural steps within an instruction is acceptable if the instruction also conveys the overall goal or outcome of the task. Step-by-step guidance should not be penalized when it improves clarity.",
    "Free-text messages in logging actions (e.g., record_terminal_log) may vary in wording as long as they correctly reflect the outcome or state change. Minor phrasing differences are acceptable; completely unrelated messages are not."
]
