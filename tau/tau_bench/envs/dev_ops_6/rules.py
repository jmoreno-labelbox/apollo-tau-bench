RULES = [
    "Task instructions should consistently be written using SECOND PERSON ('You ...').",
    "Refrain from using step-by-step language; instead, express objectives, limitations, and criteria for successful completion.",
    "Ensure that actions can be performed using parameters that are deterministically obtained from the instruction, previous tool outputs, or these rules.",
    "The tools are responsible for generating IDs and timestamps. These should not be included in actions.",
    "For translation records, every entry MUST contain only: string_key, locale, and target_string. An 'id' must NOT be included.",
"Notification # 1 (job queued): notification_type='info', title='Job queued: {string_key} [{targets}]', message='TMS job initiated for {string_key}', channel='slack'."
"Notification # 2 (validations successful):   notification_type='update',   title='Validations successful: {string_key} [{targets}]',   message='Validations for {string_key} succeeded for {targets}',   channel='slack'."
    "Unless specified, the source locale defaults to 'en'.",
    "TMS jobs must include a source_locale and a minimum of one target_locale.",
    "For link_work_items, the 'link_type' parameter must be provided.",
    "For send_notification, the 'notification_type' parameter must be specified.",
    "Translation entries must exclude 'id'; any supplied 'id' will be disregarded by tools, which will instead generate deterministic IDs internally.",
]