WIKI = """
"Task instructions should consistently be written using SECOND PERSON ('You ...').",
    "Refrain from using step-by-step language; instead, express objectives, limitations, and criteria for successful completion.",
    "Ensure that actions can be performed using parameters that are deterministically obtained from the instruction, previous tool outputs, or these rules.",
    "The tools are responsible for generating IDs and timestamps. These should not be included in actions.",
    "For translation records, every entry MUST contain only: string_key, locale, and target_string. An 'id' must NOT be included.",
    "Notification #1 (job queued):   notification_type='info',   title='Job queued: {string_key} [{targets}
"""
