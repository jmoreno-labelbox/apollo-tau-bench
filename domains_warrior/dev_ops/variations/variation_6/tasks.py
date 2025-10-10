from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="dev_ops",
        user_id="V6_001",
        instruction=(
        "You will complete localization of the pause-menu 'Start Game' string using only CI metadata already provided "
        "(commit 'def789ghi012345', build run 'run_002', test 'test_result_045'). "
        "Your objective is to deliver a high-priority localization update for exactly 'ui.main_menu.start_game' in locales ['es','it'], "
        "with translations recorded ('Comenzar' for es, 'Avvia' for it), locale validations in a passed state, an updated localization workflow for PR 1601, "
        "appropriate relationship/labeling on the relevant work items (work_055 → work_140, relates_to; label_002 on work_140), and clear notifications "
        "that the job was queued and validations succeeded. "
        "You will rely on tool-generated IDs/timestamps and the domain rules for deterministic parameters; do not provide custom IDs or names, and do not include an 'id' "
        "field in translation entries (each entry must include only: string_key, locale, target_string). "
        "Use tool outputs to decide the order of operations as needed to meet these success criteria."
        ),
actions=[
  Action(name="create_tms_job", kwargs={
    "job_type":"translation",
    "source_locale":"en",
    "target_locales":["es","it"],
    "priority":"high",
    "metadata":{
      "component":"ui",
      "subcomponent":"pause_menu",
      "commit_sha":"def789ghi012345",
      "build_run_id":"run_002",
      "test_result_id":"test_result_045"
    }
  }),
  Action(name="record_translations", kwargs={
    "entries":[
      {"string_key":"ui.main_menu.start_game","locale":"es","target_string":"Comenzar"},
      {"string_key":"ui.main_menu.start_game","locale":"it","target_string":"Avvia"}
    ]
  }),
  Action(name="update_locale_validation", kwargs={
    "string_key":"ui.main_menu.start_game",
    "locale":"es",
    "validation_status":"passed"
  }),
  Action(name="update_locale_validation", kwargs={
    "string_key":"ui.main_menu.start_game",
    "locale":"it",
    "validation_status":"passed"
  }),
  Action(name="link_work_items", kwargs={
    "parent_id":"work_055",
    "child_id":"work_140",
    "link_type":"relates_to"
  }),
  Action(name="tag_work_item_with_label", kwargs={
    "work_item_id":"work_140",
    "label_id":"label_002"
  }),
  Action(name="create_localization_workflow", kwargs={
    "pr_number":1601,
    "changed_keys":["ui.main_menu.start_game"],
    "locales_processed":["es","it"],
    "overflow_issues":0,
    "status":"completed",
    "metadata":{
      "component":"ui",
      "subcomponent":"pause_menu",
      "commit_sha":"def789ghi012345",
      "build_run_id":"run_002",
      "test_result_id":"test_result_045"
    }
  }),
  Action(name="send_notification", kwargs={
    "notification_type":"info",
    "title":"Job queued: ui.main_menu.start_game [es,it]",
    "message":"TMS job created for ui.main_menu.start_game",
    "channel":"slack"
  }),
  Action(name="send_notification", kwargs={
    "notification_type":"update",
    "title":"Validations passed: ui.main_menu.start_game [es,it]",
    "message":"Validations passed for es,it for ui.main_menu.start_game",
    "channel":"slack"
  }),
],

        outputs=[
        "tms_job created",
        "es/it translations recorded",
        "es passed",
        "it passed",
        "work_055→work_140 linked",
        "label_002 applied",
        "localization workflow completed",
        "notifications sent"
        ]

    ),

Task(
  annotator="dev_ops",
  user_id="V6_002",
  instruction=(
    "You will complete a deterministic German localization update for 'ui.settings.audio' while using only read-only context checks "
    "as needed. Your success criteria are: a high-priority localization job for the update, the 'de' translation recorded as 'Audio', "
    "validation for 'de' in passed state, a completed localization workflow for PR 1602 including this key and locale, a deterministic "
    "notification that the job was queued and validations succeeded, and no custom IDs/timestamps provided by you. "
    "Translation entries must only include: string_key, locale, target_string. Rely on tool defaults and domain rules for all IDs, "
    "timestamps, and naming."
  ),

  actions=[
    Action(name="get_loc_string", kwargs={
      "string_key": "ui.settings.audio",
      "locale": "de"
    }),

    Action(name="create_tms_job", kwargs={
      "job_type": "translation",
      "source_locale": "en",
      "target_locales": ["de"],
      "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),

    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.settings.audio", "locale": "de", "target_string": "Audio"}
      ]
    }),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio",
      "locale": "de",
      "validation_status": "passed"
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1602,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["de"],
      "overflow_issues": 0,
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.settings.audio [de]",
      "message": "TMS job created for ui.settings.audio",
      "channel": "slack"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [de]",
      "message": "Validations passed for de for ui.settings.audio",
      "channel": "slack"
    }),
  ],

  outputs=[
    "context captured (de)",
    "tms_job created",
    "de translation recorded",
    "de passed",
    "localization workflow completed",
    "notifications sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_003",
  instruction=(
    "You will document and respond to a German overflow on 'ui.main_menu.start_game' using existing records as context. "
    "Your success criteria are: locale 'de' marked failed with validation_error 'Text exceeds 200px width'; a high-priority localization job "
    "for this issue; a completed localization workflow for PR 1010 reflecting this key and locale with overflow_issues=1; and a deterministic "
    "notification indicating the validation failure. Do not provide any custom IDs or timestamps. Translation entries are not required for this task."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={
      "string_key": "ui.main_menu.start_game",
      "locale": "de"
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game",
      "locale": "de",
      "validation_status": "failed",
      "validation_error": "Text exceeds 200px width"
    }),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["de"],
      "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations failed: ui.main_menu.start_game [de]",
      "message": "Text exceeds 200px width",
      "channel": "slack"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1010,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["de"],
      "overflow_issues": 1,
      "status": "completed"
    }),
  ],
  outputs=[
    "de validation failed with overflow",
    "tms_job created",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_004",
  instruction=(
    "You will remediate the Spanish main menu localization issue discovered in CI (build run 'run_003', commit 'abc123def456789') "
    "for string_key 'ui.main_menu.start_game'. Your success criteria are: a high-priority localization job captured with that CI context; "
    "the Spanish translation recorded as 'Iniciar'; validations in a passed state for 'es'; a completed localization workflow for PR 1006; "
    "and clear notifications indicating the job was queued and validations succeeded. "
    "Rely on tool-generated IDs/timestamps and domain rules for deterministic parameters. Do not provide custom IDs or timestamps. "
    "When recording translations, each entry must include only: string_key, locale, target_string."
  ),

  actions=[
    Action(name="get_build_run", kwargs={"id": "run_003"}), 
    Action(name="create_tms_job", kwargs={
      "job_type": "translation",
      "source_locale": "en",
      "target_locales": ["es"],
      "priority": "high",
      "metadata": {
        "component": "ui",
        "subcomponent": "main_menu",
        "build_run_id": "run_003",
        "commit_sha": "abc123def456789"
      }
    }),

    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.main_menu.start_game", "locale": "es", "target_string": "Iniciar"}
      ]
    }),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game",
      "locale": "es",
      "validation_status": "passed"
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1006,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["es"],
      "status": "completed",
      "metadata": {
        "component": "ui",
        "subcomponent": "main_menu",
        "build_run_id": "run_003",
        "commit_sha": "abc123def456789"
      }
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.main_menu.start_game [es]",
      "message": "TMS job created for ui.main_menu.start_game",
      "channel": "slack"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.main_menu.start_game [es]",
      "message": "Validations passed for es for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],

  outputs=[
    "CI context captured",
    "tms_job created",
    "es translation recorded",
    "es passed",
    "localization workflow completed",
    "notifications sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_005",
  instruction=(
    "You will ensure the Japanese audio update for 'ui.settings.audio' is applied with CI traceability using build run 'run_001' "
    "and commit 'abc123def456789'. Your success criteria are: a medium-priority localization job captured with that CI context; "
    "the Japanese translation recorded as 'オーディオ'; validation for 'ja' in a passed state; work linked work_045 → work_120 (relates_to) "
    "and labeled 'localization' on work_120; a completed localization workflow for PR 5005; and clear notifications that the job was queued "
    "and validations succeeded. Rely on tool-generated IDs/timestamps and domain rules; do not provide custom IDs or timestamps. "
    "Translation entries must only include: string_key, locale, target_string."
  ),

  actions=[
    Action(name="get_build_run", kwargs={"id": "run_001"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["ja"],
      "priority": "medium",
      "metadata": {
        "component": "ui",
        "subcomponent": "settings",
        "build_run_id": "run_001",
        "commit_sha": "abc123def456789"
      }
    }),

    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.settings.audio", "locale": "ja", "target_string": "オーディオ"}
      ]
    }),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio",
      "locale": "ja",
      "validation_status": "passed"
    }),

    Action(name="link_work_items", kwargs={
      "parent_id": "work_045",
      "child_id": "work_120",
      "link_type": "relates_to"
    }),

    Action(name="tag_work_item_with_label", kwargs={
      "work_item_id": "work_120",
      "label_name": "localization"
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 5005,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["ja"],
      "status": "completed",
      "metadata": {
        "component": "ui",
        "subcomponent": "settings",
        "build_run_id": "run_001",
        "commit_sha": "abc123def456789"
      }
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.settings.audio [ja]",
      "message": "TMS job created for ui.settings.audio",
      "channel": "slack"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [ja]",
      "message": "Validations passed for ja for ui.settings.audio",
      "channel": "slack"
    }),
  ],

  outputs=[
    "context consulted (run_001)",
    "tms_job created",
    "ja translation recorded",
    "ja passed",
    "work_045→work_120 linked",
    "work_120 tagged",
    "localization workflow completed",
    "notifications sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_006",
  instruction=(
    "You will complete a deterministic German rollout for 'ui.settings.audio' with full traceability. "
    "Your success criteria are: a medium-priority localization job for this key; the 'de' translation recorded as 'Audio'; "
    "validation in a passed state for 'de'; a completed localization workflow for PR 1008; a relates_to link work_045 → work_130; "
    "and clear notifications indicating the job was queued and validations succeeded. "
    "Rely on tool-generated IDs/timestamps and domain rules for deterministic parameters; do not provide custom IDs or timestamps. "
    "When recording translations, each entry must include only: string_key, locale, target_string."
  ),

  actions=[
    Action(name="create_tms_job", kwargs={
      "job_type": "translation",
      "source_locale": "en",
      "target_locales": ["de"],
      "priority": "medium",
      "metadata": {"component": "ui"}
    }),

    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.settings.audio", "locale": "de", "target_string": "Audio"}
      ]
    }),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio",
      "locale": "de",
      "validation_status": "passed"
    }),

    Action(name="link_work_items", kwargs={
      "parent_id": "work_045",
      "child_id": "work_130",
      "link_type": "relates_to"
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1008,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["de"],
      "overflow_issues": 0,
      "status": "completed",
      "metadata": {"component": "ui"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.settings.audio [de]",
      "message": "TMS job created for ui.settings.audio",
      "channel": "slack"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [de]",
      "message": "Validations passed for de for ui.settings.audio",
      "channel": "slack"
    }),
  ],

  outputs=[
    "tms_job created",
    "de translation recorded",
    "de passed",
    "work_045→work_130 linked",
    "localization workflow completed",
    "notifications sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_007",
  instruction=(
    "You will finalize the German validation state for 'ui.main_menu.start_game' with CI context using build run 'run_003' "
    "and commit 'abc123def456789'. Your success criteria are: validation for locale 'de' in a passed state; "
    "a medium-priority localization job captured with this CI context; a completed localization workflow for PR 1009; "
    "a 'localization' label applied to work_130; and clear notifications indicating the job was queued and validations succeeded. "
    "Rely on tool-generated IDs/timestamps and domain rules; do not provide custom IDs or timestamps. "
    "Translation entries are not required for this task."
  ),

  actions=[
    Action(name="get_build_run", kwargs={"id": "run_003"}),
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "de"}),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game",
      "locale": "de",
      "validation_status": "passed"
    }),

    Action(name="create_tms_job", kwargs={
      "job_type": "translation",
      "source_locale": "en",
      "target_locales": ["de"],
      "priority": "medium",
      "metadata": {
        "build_run_id": "run_003",
        "commit_sha": "abc123def456789"
      }
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1009,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["de"],
      "overflow_issues": 0,
      "status": "completed",
      "metadata": {
        "build_run_id": "run_003",
        "commit_sha": "abc123def456789"
      }
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.main_menu.start_game [de]",
      "message": "TMS job created for ui.main_menu.start_game",
      "channel": "slack"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.main_menu.start_game [de]",
      "message": "Validations passed for de for ui.main_menu.start_game",
      "channel": "slack"
    }),

    Action(name="tag_work_item_with_label", kwargs={
      "work_item_id": "work_130",
      "label_name": "localization"
    }),
  ],

  outputs=[
    "context consulted (run_003, de string read)",
    "de passed",
    "tms_job created",
    "localization workflow completed",
    "notification sent",
    "label applied"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_008",
  instruction=(
    "You will document a German overflow for 'ui.main_menu.start_game' and capture a remediation plan. "
    "Your success criteria are: locale 'de' marked failed with validation_error 'Text exceeds 200px width'; "
    "a high-priority localization job recorded (with reviewer context for user_006 if supported); "
    "the candidate German translation 'Starten' recorded; a completed localization workflow for PR 1010 with overflow_issues=1; "
    "and an update notification describing the failure. Rely on tool-generated IDs/timestamps and domain rules; "
    "do not provide custom IDs or timestamps. Each translation entry must include only: string_key, locale, target_string."
  ),

  actions=[
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game",
      "locale": "de",
      "validation_status": "failed",
      "validation_error": "Text exceeds 200px width"
    }),

    Action(name="create_tms_job", kwargs={
      "job_type": "translation",
      "source_locale": "en",
      "target_locales": ["de"],
      "priority": "high",
      "assigned_reviewers": ["user_006"]
    }),

    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.main_menu.start_game", "locale": "de", "target_string": "Starten"}
      ]
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1010,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["de"],
      "overflow_issues": 1,
      "status": "completed"
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validation failed: ui.main_menu.start_game [de]",
      "message": "Text exceeds 200px width for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],

  outputs=[
    "de validation failed (overflow)",
    "tms_job created",
    "de translation recorded",
    "localization workflow completed",
    "notification sent"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_009",
  instruction=(
    "You will complete an ES audio rollout for 'ui.settings.audio' with explicit templates and audit context. "
    "Your success criteria are: the current ES value for 'ui.settings.audio' is consulted (read-only); "
    "a medium-priority ES TMS job is created with metadata {'component':'ui','subcomponent':'settings'}; "
    "exactly one Spanish translation is recorded as 'Audio' (each entry includes only string_key, locale, target_string); "
    "validation for 'es' is set to 'passed'; a completed localization workflow for PR 1011 exists referencing "
    "changed_keys=['ui.settings.audio'], locales_processed=['es'], and the same UI/Settings metadata; and two Slack notifications are sent "
    "using the deterministic templates: (info) title='Job queued: ui.settings.audio [es]' / message='TMS job created for ui.settings.audio' "
    "and (update) title='Validations passed: ui.settings.audio [es]' / message='Validations passed for es for ui.settings.audio'. "
    "Use tool-generated IDs/timestamps only."
  ),

  actions=[
    Action(name="get_loc_string", kwargs={"string_key":"ui.settings.audio","locale":"es"}),

    Action(name="create_tms_job", kwargs={
      "source_locale":"en",
      "target_locales":["es"],
      "priority":"medium",
      "metadata":{"component":"ui","subcomponent":"settings"}
    }),

    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"ui.settings.audio","locale":"es","target_string":"Audio"}]
    }),

    Action(name="update_locale_validation", kwargs={
      "string_key":"ui.settings.audio","locale":"es","validation_status":"passed"
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number":1011,
      "changed_keys":["ui.settings.audio"],
      "locales_processed":["es"],
      "status":"completed",
      "metadata":{"component":"ui","subcomponent":"settings"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Job queued: ui.settings.audio [es]",
      "message":"TMS job created for ui.settings.audio",
      "channel":"slack"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"update",
      "title":"Validations passed: ui.settings.audio [es]",
      "message":"Validations passed for es for ui.settings.audio",
      "channel":"slack"
    }),
  ],

  outputs=[
    "context consulted (es)",
    "tms_job created",
    "es translation recorded",
    "es validation passed",
    "localization workflow completed",
    "notifications sent"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_010",
  instruction=(
    "You will complete a deterministic German update for 'ui.settings.audio' with traceability and lightweight coordination. "
    "Your success criteria are: a medium-priority localization job; one German translation recorded as 'Audio'; "
    "validation in a passed state for 'de'; a completed localization workflow for PR 1012; two notifications (job queued and validations passed); "
    "a relates_to link work_045 → work_130; and the 'localization' label applied to work_130. "
    "Rely on tool-generated IDs/timestamps and domain rules; do not provide custom IDs or timestamps. "
    "Each translation entry must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["de"], "priority": "medium"
    }),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.settings.audio", "locale": "de", "target_string": "Audio"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "de", "validation_status": "passed"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1012, "changed_keys": ["ui.settings.audio"], "locales_processed": ["de"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.settings.audio [de]",
      "message": "TMS job created for ui.settings.audio",
      "channel": "slack"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [de]",
      "message": "Validations passed for de for ui.settings.audio",
      "channel": "slack"
    }),
    Action(name="link_work_items", kwargs={"parent_id": "work_045", "child_id": "work_130", "link_type": "relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_130", "label_name": "localization"}),
  ],
  outputs=[
    "tms_job created", "de translation recorded", "de passed",
    "localization workflow completed", "notifications sent",
    "work_045→work_130 linked", "work_130 tagged"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_011",
  instruction=(
    "You will finalize the Japanese main-menu start label under localization policy. Your success criteria are: "
    "work_130 tagged with the existing 'localization' label; a high-priority localization job for 'ja' on the main menu; "
    "the Japanese translation 'ゲーム開始' recorded for 'ui.main_menu.start_game'; validation in a passed state for 'ja'; "
    "a completed localization workflow for PR 1015; and an info notification summarizing the update. "
    "Rely on tool-generated IDs/timestamps and domain rules; do not provide any custom IDs or timestamps. "
    "Each translation entry must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_130", "label_name": "localization"}),
    Action(name="create_tms_job", kwargs={"source_locale": "en", "target_locales": ["ja"], "priority": "high"}),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.main_menu.start_game", "locale": "ja", "target_string": "ゲーム開始"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "ja", "validation_status": "passed"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1015, "changed_keys": ["ui.main_menu.start_game"], "locales_processed": ["ja"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Validations passed: ui.main_menu.start_game [ja]",
      "message": "Validations passed for ja for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=[
    "label applied", "tms_job created", "ja translation recorded",
    "ja validation passed", "localization workflow completed", "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_012",
  instruction=(
    "You will capture a deterministic ES audio update. Your success criteria are: work_130 tagged with the existing "
    "'localization' label; a high-priority localization job for 'es' on settings; the Spanish translation 'Audio' recorded "
    "for 'ui.settings.audio'; validation in a passed state for 'es'; a completed localization workflow for PR 1014; "
    "and an update notification summarizing the change. Rely on tool-generated IDs/timestamps; do not provide custom IDs "
    "or timestamps. Each translation entry must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_130", "label_name": "localization"}),
    Action(name="create_tms_job", kwargs={"source_locale": "en", "target_locales": ["es"], "priority": "high"}),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.settings.audio", "locale": "es", "target_string": "Audio"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "es", "validation_status": "passed"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1014, "changed_keys": ["ui.settings.audio"], "locales_processed": ["es"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [es]",
      "message": "Validations passed for es for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "label applied", "tms_job created", "es translation recorded",
    "es validation passed", "localization workflow completed", "notification sent"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_013",
  instruction=(
    "You will complete a Japanese main-menu remediation. Your success criteria are: current entry checked (read-only) for "
    "'ui.main_menu.start_game' in 'ja'; a high-priority localization job for 'ja' on main menu; the Japanese translation "
    "'ゲーム開始' recorded; validation set to passed; a completed localization workflow for PR 1015; and an info notification "
    "describing readiness. Use tool-generated IDs/timestamps only. Each translation entry must include only: string_key, "
    "locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "ja"}),
    Action(name="create_tms_job", kwargs={"source_locale": "en", "target_locales": ["ja"], "priority": "high"}),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.main_menu.start_game", "locale": "ja", "target_string": "ゲーム開始"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "ja", "validation_status": "passed"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1015, "changed_keys": ["ui.main_menu.start_game"], "locales_processed": ["ja"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.main_menu.start_game [ja]",
      "message": "Validations passed for ja for ui.main_menu.start_game",
      "channel": "slack"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Ready for release: ui.main_menu.start_game [ja]",
      "message": "Localization for ja for ui.main_menu.start_game is ready.",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (ja)",
    "tms_job created",
    "ja translation recorded",
    "ja validation passed",
    "localization workflow completed",
    "validation update notification sent",
    "readiness info notification sent"
  ]
),



Task(
  annotator="dev_ops",
  user_id="V6_014",
  instruction=(
    "You will record an ES settings batch deterministically with context and validation. Your success criteria are: "
    "current ES text for 'ui.settings.audio' consulted (read-only); a high-priority localization job for 'es' on settings; "
    "the Spanish translation 'Audio' recorded for 'ui.settings.audio'; validation set to passed (no error field); "
    "a completed localization workflow for PR 1016; and an update notification summarizing the recording. "
    "Use tool-generated IDs/timestamps only. Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "es"}),
    Action(name="create_tms_job", kwargs={"source_locale": "en", "target_locales": ["es"], "priority": "high"}),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.settings.audio", "locale": "es", "target_string": "Audio"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "es", "validation_status": "passed"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1016, "changed_keys": ["ui.settings.audio"], "locales_processed": ["es"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [es]",
      "message": "Validations passed for es for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context captured", "tms_job created", "es translation recorded",
    "es validation passed", "localization workflow completed", "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_015",
  instruction=(
    "You will complete a JA VO timing remediation with CI traceability. Your success criteria are: CI context captured by "
    "consulting build run 'run_003' and commit 'abc123def456789'; the current JA settings-audio entry consulted (read-only); "
    "a high-priority localization job for 'ja' on settings recorded with CI metadata (build run and commit); a completed "
    "localization workflow for PR 1017 carrying the same CI metadata and overflow_issues=0; a relates_to link from work_045 "
    "to work_140; and an info notification stating the timing update using "
    "title='Timing updated: ui.settings.audio [ja]' and message='Timing updated for ja for ui.settings.audio'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_build_run", kwargs={"id": "run_003"}),
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "ja"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["ja"],
      "priority": "high",
      "metadata": {"build_run_id": "run_003", "commit_sha": "abc123def456789", "subcomponent": "settings"}
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1017,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["ja"],
      "overflow_issues": 0,
      "status": "completed",
      "metadata": {"build_run_id": "run_003", "commit_sha": "abc123def456789", "subcomponent": "settings"}
    }),

    Action(name="link_work_items", kwargs={
      "parent_id": "work_045",
      "child_id": "work_140",
      "link_type": "relates_to"
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Timing updated: ui.settings.audio [ja]",
      "message": "Timing updated for ja for ui.settings.audio",
      "channel": "slack"
    }),
  ],

  outputs=[
    "CI context consulted (run_003, abc123def456789)",
    "baseline ja value consulted",
    "tms_job created",
    "localization workflow completed",
    "work_045→work_140 linked",
    "notification sent"
  ]
),




Task(
  annotator="loc_integration",
  user_id="V6_016",
  instruction=(
    "You will base a DE review on repository context and persist deterministic records. Your success criteria are: "
    "CI context consulted (build run 'run_001', commit 'abc123def456789', test_result 'test_result_001', ownership for "
    "'src/game/engine/renderer.cpp') and the existing DE localization for 'ui.main_menu.start_game' read; a high-priority DE job "
    "for the main menu recorded with CI/ownership metadata; validation set to passed for 'de'; the translation 'Starten' recorded "
    "for 'ui.main_menu.start_game'; a completed localization workflow for PR 1016 carrying the same CI metadata; and an info "
    "notification announcing the build-triggered review. Use tool-generated IDs/timestamps only. Each translation entry must "
    "include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_build_run", kwargs={"id": "run_001"}),
    Action(name="get_source_change", kwargs={"commit_sha": "abc123def456789"}),
    Action(name="get_test_result", kwargs={"id": "test_result_001"}),
    Action(name="get_ownership_for_path", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "de"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["de"], "priority": "high",
      "metadata": {
        "component": "ui", "subcomponent": "main_menu",
        "commit_sha": "abc123def456789", "build_run_id": "run_001",
        "test_result_id": "test_result_001", "owner_id": "user_001",
        "file_path": "src/game/engine/renderer.cpp"
      }
    }),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "de", "validation_status": "passed"
    }),

    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.main_menu.start_game", "locale": "de", "target_string": "Starten"}]
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.main_menu.start_game [de]",
      "message": "TMS job created for ui.main_menu.start_game",
      "channel": "slack"
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1016, "changed_keys": ["ui.main_menu.start_game"], "locales_processed": ["de"],
      "status": "completed",
      "metadata": {
        "component": "ui", "commit_sha": "abc123def456789",
        "build_run_id": "run_001", "test_result_id": "test_result_001",
        "owner_id": "user_001", "file_path": "src/game/engine/renderer.cpp"
      }
    }),
  ],
  outputs=[
    "context consulted (build, commit, test, ownership, de string)",
    "tms_job created", "de validation passed", "de translation recorded",
    "notification sent", "localization workflow completed"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_017",
  instruction=(
    "You will roll out a Japanese refresh for settings audio with context and traceability. Your success criteria are: "
    "the current JA value for 'ui.settings.audio' consulted (read-only); the translation 'オーディオ' recorded; validation set to passed; "
    "a high-priority JA job for settings recorded; a relates_to link from work_045 to work_150 and the 'localization' label applied to work_150; "
    "a completed localization workflow for PR 1018; and an info notification that the job was queued. Use tool-generated IDs/timestamps only. "
    "Each translation entry must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "ja"}),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.settings.audio", "locale": "ja", "target_string": "オーディオ"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "ja", "validation_status": "passed"
    }),
    Action(name="create_tms_job", kwargs={"source_locale": "en", "target_locales": ["ja"], "priority": "high"}),
    Action(name="link_work_items", kwargs={"parent_id": "work_045", "child_id": "work_150", "link_type": "relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_150", "label_name": "localization"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1018, "changed_keys": ["ui.settings.audio"], "locales_processed": ["ja"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.settings.audio [ja]",
      "message": "TMS job created for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context captured (ja)", "ja translation recorded", "ja validation passed",
    "tms_job created", "work_045→work_150 linked", "label applied",
    "localization workflow completed", "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_018",
  instruction=(
    "You will record a deterministic ES audio application with context and validation. Your success criteria are: "
    "the current ES text for 'ui.settings.audio' consulted; a medium-priority ES job for settings recorded; work_140 tagged with "
    "the existing 'localization' label; validation set to passed (no error field); the translation 'Audio' recorded; a completed "
    "localization workflow for PR 1019; and an update notification. Use tool-generated IDs/timestamps only. "
    "Each translation entry must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "es"}),
    Action(name="create_tms_job", kwargs={"source_locale": "en", "target_locales": ["es"], "priority": "medium"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_140", "label_name": "localization"}),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "es", "validation_status": "passed"
    }),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.settings.audio", "locale": "es", "target_string": "Audio"}]
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1019, "changed_keys": ["ui.settings.audio"], "locales_processed": ["es"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [es]",
      "message": "Validations passed for es for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted", "tms_job created", "label applied",
    "es validation passed", "es translation recorded",
    "localization workflow completed", "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_019",
  instruction=(
    "You will execute a deterministic ES audio rollout with CI context and epic linkage. Your success criteria are: "
    "CI consulted (build run 'run_001' and commit 'abc123def456789') and the current ES text read; a medium-priority ES job for settings "
    "recorded with CI metadata (build run and commit); one translation recorded for 'ui.settings.audio' ('Audio'); validation set to passed; "
    "a relates_to link from work_045 to work_150 and 'localization' label applied to work_150; a completed localization workflow for PR 1020 "
    "with the same CI metadata; and two notifications indicating job queued and job completed. Use tool-generated IDs/timestamps only. "
    "Each translation entry must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_build_run", kwargs={"id": "run_001"}),
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "es"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["es"],
      "priority": "medium",
      "metadata": {"commit_sha": "abc123def456789", "build_run_id": "run_001"}
    }),

    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.settings.audio", "locale": "es", "target_string": "Audio"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "es", "validation_status": "passed"
    }),

    Action(name="link_work_items", kwargs={"parent_id": "work_045", "child_id": "work_150", "link_type": "relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_150", "label_name": "localization"}),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1020,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["es"],
      "status": "completed",
      "metadata": {"commit_sha": "abc123def456789", "build_run_id": "run_001"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.settings.audio [es]",
      "message": "TMS job created for ui.settings.audio",
      "channel": "slack"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Job completed: ui.settings.audio [es]",
      "message": "Job completed for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (run_001, abc123def456789, es read)",
    "tms_job created",
    "es translation recorded",
    "es validation passed",
    "work_045→work_150 linked",
    "work_150 tagged",
    "localization workflow completed",
    "notifications sent"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_020",
  instruction=(
    "You will finalize a deterministic ES validation and workflow. Your success criteria are: validation for "
    "'ui.settings.audio' in 'es' set to passed; a medium-priority ES job for settings recorded; a completed "
    "localization workflow for PR 1021; and an info notification confirming ES validation. Use tool-generated "
    "IDs/timestamps only."
  ),
  actions=[
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "es", "validation_status": "passed"
    }),
    Action(name="create_tms_job", kwargs={"source_locale": "en", "target_locales": ["es"], "priority": "medium"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1021, "changed_keys": ["ui.settings.audio"], "locales_processed": ["es"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Validations passed: ui.settings.audio [es]",
      "message": "Validations passed for es for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "es validation passed", "tms_job created",
    "localization workflow completed", "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_021",
  instruction=(
    "You will finalize the Italian main-menu start label deterministically. Your success criteria are: "
    "the current IT text for 'ui.main_menu.start_game' consulted; the translation 'Avvia' recorded; "
    "validation for 'it' set to passed; a medium-priority IT job for the main menu recorded; "
    "a completed localization workflow for PR 1022; and an info notification confirming the update. "
    "Use tool-generated IDs/timestamps only. Each translation entry must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "it"}),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.main_menu.start_game", "locale": "it", "target_string": "Avvia"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "it", "validation_status": "passed"
    }),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["it"], "priority": "medium"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1022, "changed_keys": ["ui.main_menu.start_game"], "locales_processed": ["it"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Validations passed: ui.main_menu.start_game [it]",
      "message": "Validations passed for it for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=[
    "it string consulted", "it translation recorded", "it validation passed",
    "tms_job created", "localization workflow completed", "notification sent"
  ]
),



Task(
  annotator="dev_ops",
  user_id="V6_022",
  instruction=(
    "You will ship a deterministic DE settings-audio update. Your success criteria are: "
    "the translation 'Audio' recorded for 'ui.settings.audio'; validation for 'de' set to passed; "
    "a medium-priority DE job for settings recorded; a completed localization workflow for PR 1023; "
    "and an update notification confirming the change. Use tool-generated IDs/timestamps only. "
    "Each translation entry must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.settings.audio", "locale": "de", "target_string": "Audio"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "de", "validation_status": "passed"
    }),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["de"], "priority": "medium"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1023, "changed_keys": ["ui.settings.audio"], "locales_processed": ["de"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [de]",
      "message": "Validations passed for de for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "de translation recorded", "de validation passed",
    "tms_job created", "localization workflow completed", "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_023",
  instruction=(
    "You will document a Spanish overflow for the main-menu start label and capture remediation. Your success criteria are: "
    "validation for 'ui.main_menu.start_game' in 'es' marked failed with error 'Text exceeds 200px width'; "
    "a high-priority ES job for main menu recorded; the candidate translation 'Iniciar' recorded; "
    "a completed localization workflow for PR 1024 with one overflow issue; "
    "and an update Slack notification sent using the exact strings "
    "title='Validations failed: ui.main_menu.start_game [es]' and "
    "message='Text exceeds 200px width for ui.main_menu.start_game'. "
    "Use tool-generated IDs/timestamps only. Each translation entry must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "es",
      "validation_status": "failed", "validation_error": "Text exceeds 200px width"
    }),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["es"], "priority": "high"
    }),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.main_menu.start_game", "locale": "es", "target_string": "Iniciar"}]
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1024, "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["es"], "status": "completed", "overflow_issues": 1
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations failed: ui.main_menu.start_game [es]",
      "message": "Text exceeds 200px width for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=[
    "es validation failed (overflow)", "tms_job created",
    "es translation recorded", "localization workflow completed", "notification sent"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_024",
  instruction=(
    "You will finalize a deterministic JA validation for settings audio with workflow and notice. "
    "Your success criteria are: validation for 'ui.settings.audio' in 'ja' set to passed; "
    "a medium-priority JA job for settings recorded; a completed localization workflow for PR 1025; "
    "and an info notification confirming JA validation. Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "ja", "validation_status": "passed"
    }),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["ja"], "priority": "medium"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1025, "changed_keys": ["ui.settings.audio"], "locales_processed": ["ja"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Validations passed: ui.settings.audio [ja]",
      "message": "Validations passed for ja for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "ja validation passed", "tms_job created",
    "localization workflow completed", "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_025",
  instruction=(
    "You will apply a deterministic ES/IT settings-audio rollout. Your success criteria are: "
    "the translations recorded ('Audio' for 'es' and 'it') for 'ui.settings.audio'; validations for 'es' and 'it' set to passed; "
    "a high-priority job targeting both locales recorded; a completed localization workflow for PR 1026; "
    "a relates_to link from work_045 to work_160 and the 'localization' label applied to work_160; "
    "and notifications acknowledging the rollout. Use tool-generated IDs/timestamps only. "
    "Each translation entry must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.settings.audio", "locale": "es", "target_string": "Audio"},
        {"string_key": "ui.settings.audio", "locale": "it", "target_string": "Audio"}
      ]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "es", "validation_status": "passed"
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "it", "validation_status": "passed"
    }),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["es", "it"], "priority": "high"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1026, "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["es", "it"], "status": "completed"
    }),
    Action(name="link_work_items", kwargs={
      "parent_id": "work_045", "child_id": "work_160", "link_type": "relates_to"
    }),
    Action(name="tag_work_item_with_label", kwargs={
      "work_item_id": "work_160", "label_name": "localization"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.settings.audio [es,it]",
      "message": "TMS job created for ui.settings.audio",
      "channel": "slack"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [es,it]",
      "message": "Validations passed for es,it for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "es/it translations recorded", "es passed", "it passed",
    "tms_job created", "localization workflow completed",
    "work_045→work_160 linked", "work_160 tagged", "notifications sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_026",
  instruction=(
    "You will persist an ES settings workflow with epic linkage and basic TMS context. "
    "Success criteria: the current ES value for 'ui.settings.audio' consulted; a relates_to link from work_045 to work_150; "
    "a medium-priority ES job for settings recorded with UI metadata; a completed workflow for PR 1027; "
    "and an update notification confirming the linkage. Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "es"}),

    Action(name="link_work_items", kwargs={
      "parent_id": "work_045",
      "child_id": "work_150",
      "link_type": "relates_to"
    }),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["es"],
      "priority": "medium",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio",
      "locale": "es",
      "validation_status": "passed"
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1027,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["es"],
      "status": "completed"
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Linkage confirmed: work_045→work_150",
      "message": "Relates_to linkage established between work_045 and work_150.",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (es)",
    "work_045→work_150 linked",
    "tms_job created",
    "es validation passed",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_027",
  instruction=(
    "You will run a CI-aware FR main-menu rollout with labeling. "
    "Success criteria: build run 'run_001' and commit 'abc123def456789' consulted; "
    "the translation 'Commencer' recorded for 'ui.main_menu.start_game' in 'fr'; validation set to passed; "
    'work_120 and work_140 tagged with "localization"; a medium-priority FR job recorded with CI metadata; '
    "a completed workflow for PR 1028; and an info notification. Use tool-generated IDs/timestamps only. "
    "Each translation entry must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_build_run", kwargs={"id": "run_001"}),

    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.main_menu.start_game", "locale": "fr", "target_string": "Commencer"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "fr", "validation_status": "passed"
    }),

    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_120", "label_name": "localization"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_140", "label_name": "localization"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["fr"],
      "priority": "medium",
      "metadata": {"commit_sha": "abc123def456789", "build_run_id": "run_001"}
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1028,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["fr"],
      "status": "completed"
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.main_menu.start_game [fr]",
      "message": "TMS job created for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (run_001, abc123def456789)",
    "fr translation recorded",
    "fr validation passed",
    "work_120 tagged",
    "work_140 tagged",
    "tms_job created",
    "localization workflow completed",
    "notification sent"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_028",
  instruction=(
    "You will persist a ZH validation result and audit records with TMS context. "
    "Success criteria: the current ZH main-menu text consulted; validation set to passed; "
    "a medium-priority ZH job recorded with UI metadata; a completed workflow for PR 1029; "
    "and an info notification confirming ZH validation. Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "zh"}),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "zh", "validation_status": "passed"
    }),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["zh"], "priority": "medium",
      "metadata": {"component": "ui"}
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1029,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["zh"],
      "status": "completed",
      "metadata": {"component": "ui"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Validations passed: ui.main_menu.start_game [zh]",
      "message": "Validations passed for zh for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (zh)",
    "zh validation passed",
    "tms_job created",
    "localization workflow completed",
    "notification sent"
  ]
),




Task(
  annotator="dev_ops",
  user_id="V6_029",
  instruction=(
    "You will apply a deterministic ZH settings-audio update across systems. "
    "Success criteria: a high-priority ZH job for settings recorded; the translation '音频' recorded for 'ui.settings.audio'; "
    "validation set to passed; a completed workflow for PR 1030; and an update notification. "
    "Use tool-generated IDs/timestamps only. Each translation entry must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={"source_locale": "en", "target_locales": ["zh"], "priority": "high"}),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.settings.audio", "locale": "zh", "target_string": "音频"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "zh", "validation_status": "passed"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1030, "changed_keys": ["ui.settings.audio"], "locales_processed": ["zh"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [zh]",
      "message": "Validations passed for zh for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "tms_job created", "zh translation recorded",
    "zh validation passed", "localization workflow completed", "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_030",
  instruction=(
    "You will record a deterministic DE overflow resolution for the main-menu start label. "
    "Success criteria: validation for 'ui.main_menu.start_game' in 'de' set to passed; "
    "a completed workflow for PR 1031; and an update notification confirming resolution. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "de", "validation_status": "passed"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1031, "changed_keys": ["ui.main_menu.start_game"], "locales_processed": ["de"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.main_menu.start_game [de]",
      "message": "Validations passed for de for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=[
    "de validation passed", "localization workflow completed", "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_031",
  instruction=(
    "You will ensure the system reflects an ES audio validation with traceable linkage and job context. "
    "Success criteria: the current ES entry for 'ui.settings.audio' consulted; a medium-priority ES job for settings recorded; "
    "the translation 'Audio' recorded; a relates_to link from work_045 to work_140; validation set to passed; "
    "a completed workflow for PR 1032; and an info notification confirming validation. "
    "Use tool-generated IDs/timestamps only. Each translation entry must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "es"}),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["es"], "priority": "medium", "metadata": {"component": "ui"}
    }),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.settings.audio", "locale": "es", "target_string": "Audio"}]
    }),
    Action(name="link_work_items", kwargs={"parent_id": "work_045", "child_id": "work_140", "link_type": "relates_to"}),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "es", "validation_status": "passed"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1032, "changed_keys": ["ui.settings.audio"], "locales_processed": ["es"],
      "overflow_issues": 0, "status": "completed", "metadata": {"component": "ui"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Validations passed: ui.settings.audio [es]",
      "message": "Validations passed for es for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (es)", "tms_job created", "es translation recorded",
    "work_045→work_140 linked", "es validation passed", "localization workflow completed", "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_032",
  instruction=(
    "You will document a DE overflow discovery and remediation with full traceability. "
    "Success criteria: current DE value for 'ui.main_menu.start_game' consulted; "
    "validation recorded as failed with error 'Text exceeds 200px width'; "
    "a high-priority DE job for the main menu captured with UI/Main Menu metadata; "
    "an update notification referencing the overflow; the translation 'Starten' recorded; "
    "follow-up validation set to passed; and a completed workflow for PR 1022. "
    "Use tool-generated IDs/timestamps only. Each translation entry must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "de"}),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "de",
      "validation_status": "failed", "validation_error": "Text exceeds 200px width"
    }),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["de"],
      "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations failed: ui.main_menu.start_game [de]",
      "message": "Text exceeds 200px width",
      "channel": "slack"
    }),

    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.main_menu.start_game", "locale": "de", "target_string": "Starten"}]
    }),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "de",
      "validation_status": "passed"
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1022,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["de"],
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),
  ],
  outputs=[
    "context consulted (de)",
    "de failed",
    "tms_job created",
    "notification sent",
    "de translation recorded",
    "de passed",
    "localization workflow completed"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_033",
  instruction=(
    "You will capture a deterministic FR settings-audio tone update. "
    "Success criteria: FR entry for 'ui.settings.audio' consulted; a high-priority FR job for settings with UI metadata; "
    "translation 'Audio' recorded for FR; validation set to passed; a completed workflow for PR 1023; and an info notification. "
    "Use tool-generated IDs/timestamps only. Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "fr"}),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["fr"], "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.settings.audio", "locale": "fr", "target_string": "Audio"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "fr", "validation_status": "passed"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1023, "changed_keys": ["ui.settings.audio"], "locales_processed": ["fr"],
      "overflow_issues": 0, "status": "completed", "metadata": {"component": "ui"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.settings.audio [fr]",
      "message": "TMS job created for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (fr)", "tms_job created", "fr translation recorded",
    "fr validation passed", "localization workflow completed", "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_034",
  instruction=(
    "You will persist a linkage, label, and JA settings update. Your success criteria are: a relates_to link work_045 → work_150; "
    "work_150 tagged with 'localization'; a high-priority JA job for UI/Settings recorded; the translation 'オーディオ' "
    "recorded for 'ui.settings.audio'; a completed workflow for PR 1024 reflecting 'ui.settings.audio' for locale 'ja'; "
    "and an info notification that the job was queued. Use tool-generated IDs/timestamps only. Translation entries must "
    "include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="link_work_items", kwargs={
      "parent_id": "work_045",
      "child_id": "work_150",
      "link_type": "relates_to"
    }),
    Action(name="tag_work_item_with_label", kwargs={
      "work_item_id": "work_150",
      "label_name": "localization"
    }),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["ja"],
      "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),
    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.settings.audio", "locale": "ja", "target_string": "オーディオ"}
      ]
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1024,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["ja"],
      "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.settings.audio [ja]",
      "message": "TMS job created for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "work_045→work_150 linked",
    "work_150 tagged",
    "tms_job created",
    "ja translation recorded",
    "localization workflow completed",
    "notification sent"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_035",
  instruction=(
    "You will ensure VO subtitle retiming with CI/TMS traceability. Your success criteria are: build run 'run_001' consulted; "
    "subtitle_001 retimed to start 0.10s and end 2.40s; a medium-priority EN job recorded with VO metadata and CI context; "
    "relates_to link work_045 → work_160 and work_160 tagged 'localization'; a completed workflow for PR 4025; and an update "
    "notification about the retime. Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_build_run", kwargs={"id": "run_001"}),
    Action(name="update_subtitle_timing", kwargs={
      "id": "subtitle_001", "updates": {"subtitle_start": 0.10, "subtitle_end": 2.40}
    }),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["en"], "priority": "medium",
      "metadata": {"component": "vo", "build_run_id": "run_001", "commit_sha": "abc123def456789"}
    }),
    Action(name="link_work_items", kwargs={"parent_id": "work_045", "child_id": "work_160", "link_type": "relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_160", "label_name": "localization"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 4025, "changed_keys": ["subtitle_001"], "locales_processed": ["en"],
      "overflow_issues": 0, "status": "completed",
      "metadata": {"component": "vo", "build_run_id": "run_001", "commit_sha": "abc123def456789"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Subtitle retimed: subtitle_001",
      "message": "subtitle_001 retimed to 0.10–2.40",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (run_001)", "subtitle_001 retimed", "tms_job created",
    "work_045→work_160 linked", "work_160 tagged", "localization workflow completed", "notification sent"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_036",
  instruction=(
    "You ensure a CI-aware ES audio apply for key 'ui.settings.audio'. "
    "Outcomes: build run 'run_003' and commit 'abc123def456789' consulted read-only; "
    "a medium-priority ES job captured with metadata {'build_run_id':'run_003','commit_sha':'abc123def456789'}; "
    "one ES translation recorded as 'Audio'; validation set to 'passed'; "
    "work_045→work_170 linked with link_type='relates_to' and work_170 tagged 'localization'; "
    "a completed workflow for PR 4026 includes the same CI metadata; and an info notification is sent using "
    "title='Job queued: ui.settings.audio [es]' and message='TMS job created for ui.settings.audio'. "
    "Use tool-generated IDs/timestamps only. Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_build_run", kwargs={"id": "run_003"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["es"],
      "priority": "medium",
      "metadata": {"build_run_id": "run_003", "commit_sha": "abc123def456789"}
    }),

    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.settings.audio", "locale": "es", "target_string": "Audio"}
      ]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio",
      "locale": "es",
      "validation_status": "passed"
    }),

    Action(name="link_work_items", kwargs={
      "parent_id": "work_045",
      "child_id": "work_170",
      "link_type": "relates_to"
    }),
    Action(name="tag_work_item_with_label", kwargs={
      "work_item_id": "work_170",
      "label_name": "localization"
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 4026,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["es"],
      "status": "completed",
      "metadata": {"build_run_id": "run_003", "commit_sha": "abc123def456789"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.settings.audio [es]",
      "message": "TMS job created for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (run_003, abc123def456789)",
    "tms_job created",
    "es translation recorded",
    "es validation passed",
    "work_045→work_170 linked",
    "work_170 tagged",
    "localization workflow completed",
    "notification sent"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_037",
  instruction=(
    "You will document a FR truncation detection and fix with traceability. "
    "Success criteria: the current FR value for 'ui.main_menu.start_game' is consulted; "
    "validation is recorded as failed with error 'Truncation risk at 20 char'; "
    "a high-priority FR job for the main menu is captured with UI/Main Menu metadata; an update notification referencing the issue is sent; "
    "the translation 'Jouer' is recorded; follow-up validation is set to passed; and a completed workflow for PR 1027 exists. "
    "Use tool-generated IDs/timestamps only. Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "fr"}),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "fr",
      "validation_status": "failed", "validation_error": "Truncation risk at 20 char"
    }),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["fr"], "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.main_menu.start_game [fr]",
      "message": "TMS job created for ui.main_menu.start_game",
      "channel": "slack"
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations failed: ui.main_menu.start_game [fr]",
      "message": "Truncation risk at 20 char for ui.main_menu.start_game",
      "channel": "slack"
    }),

    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.main_menu.start_game", "locale": "fr", "target_string": "Jouer"}]
    }),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "fr", "validation_status": "passed"
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1027, "changed_keys": ["ui.main_menu.start_game"], "locales_processed": ["fr"], "status": "completed"
    }),
  ],
  outputs=[
    "context consulted (fr)",
    "fr failed",
    "tms_job created",
    "notifications sent",
    "fr translation recorded",
    "fr passed",
    "localization workflow completed"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_038",
  instruction=(
    "You will persist deterministic labeling, linking, and an ES (Spanish) settings workflow. "
    "Your success criteria: work_130 is tagged with 'localization'; a 'relates_to' link from work_045 to work_150 exists; "
    "you consult the current ES value for 'ui.settings.audio'; a high-priority ES job with UI metadata is captured; "
    "a completed workflow for PR 1028 exists; and an update notification using the template "
    "title='Validations passed: ui.settings.audio [es]' and message='Validations passed for es for ui.settings.audio' is sent to Slack. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_130", "label_name": "localization"}),
    Action(name="link_work_items", kwargs={"parent_id": "work_045", "child_id": "work_150", "link_type": "relates_to"}),
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "es"}),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["es"], "priority": "high", "metadata": {"component": "ui"}
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1028, "changed_keys": ["ui.settings.audio"], "locales_processed": ["es"],
      "overflow_issues": 0, "status": "completed", "metadata": {"component": "ui"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [es]",
      "message": "Validations passed for es for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "work_130 tagged",
    "work_045→work_150 linked",
    "context consulted (es)",
    "tms_job created",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_039",
  instruction=(
    "You complete a deterministic dual-locale rollout for 'ui.main_menu.start_game' in ZH and JA. "
    "Your success criteria: you consult the current ZH and JA values; a high-priority UI/Main Menu job targeting ZH and JA is recorded; "
    "a completed workflow for PR 1029 exists; and an info notification is sent using the template "
    "title='Job queued: ui.main_menu.start_game [zh,ja]' and message='TMS job created for ui.main_menu.start_game'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "zh"}),
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "ja"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["zh", "ja"],
      "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1029,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["zh", "ja"],
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.main_menu.start_game [zh,ja]",
      "message": "TMS job created for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (zh/ja)",
    "tms_job created",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_040",
  instruction=(
    "You will perform a full ZH localization cycle for 'ui.main_menu.start_game' with traceable linkage. "
    "Success criteria: a medium-priority ZH job is captured; the translation '开始游戏' is recorded; "
    "validation is in passed state; work_050 → work_150 link (relates_to) exists; "
    "a completed workflow for PR 1040 exists; and a notification announces ZH validation passed. "
    "Use tool-generated IDs/timestamps only. Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["zh"], "priority": "medium",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.main_menu.start_game", "locale": "zh", "target_string": "开始游戏"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "zh", "validation_status": "passed"
    }),
    Action(name="link_work_items", kwargs={"parent_id": "work_050", "child_id": "work_150", "link_type": "relates_to"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1040,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["zh"],
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.main_menu.start_game [zh]",
      "message": "Validations passed for zh for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],

  outputs=[
    "tms_job created",
    "zh translation recorded",
    "zh validation passed",
    "work_050→work_150 linked",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_041",
  instruction=(
    "You capture a FR/DE audio update and its validation with clear traceability. "
    "Your success criteria: the current FR and DE values for 'ui.settings.audio' are consulted; "
    "a high-priority job for FR and DE in UI/Settings is recorded; exactly one translation for FR and one for DE ('Audio') are recorded; "
    "both locales are in a passed validation state; a completed workflow for PR 1031 exists; and an update notification confirms FR/DE audio validated. "
    "Use tool-generated IDs/timestamps only. Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "fr"}),
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "de"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["fr", "de"],
      "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),

    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.settings.audio", "locale": "fr", "target_string": "Audio"},
        {"string_key": "ui.settings.audio", "locale": "de", "target_string": "Audio"}
      ]
    }),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "fr", "validation_status": "passed"
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "de", "validation_status": "passed"
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1031,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["fr", "de"],
      "overflow_issues": 0,
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [fr,de]",
      "message": "Validations passed for fr,de for ui.settings.audio",
      "channel": "slack"
    }),
  ],

  outputs=[
    "context consulted (fr,de)",
    "tms_job created",
    "fr/de translations recorded",
    "fr/de validation passed",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_042",
  instruction=(
    "You reflect a CI-aware FR/ES audio update with exact, minimal records. "
    "Your success criteria: build run 'run_001' and commit 'abc123def456789' are consulted read-only; "
    "a high-priority UI/Settings job is captured with that CI context; exactly one FR and one ES translation ('Audio') are recorded; "
    "FR validation is marked passed (no error recorded); a completed workflow for PR 1022 exists with the CI context; "
    "and an update notification confirms completion. Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_build_run", kwargs={"id": "run_001"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["fr", "es"],
      "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "settings", "build_run_id": "run_001", "commit_sha": "abc123def456789"}
    }),

    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.settings.audio", "locale": "fr", "target_string": "Audio"},
        {"string_key": "ui.settings.audio", "locale": "es", "target_string": "Audio"}
      ]
    }),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "fr", "validation_status": "passed"
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1022,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["fr", "es"],
      "overflow_issues": 0,
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "settings", "build_run_id": "run_001", "commit_sha": "abc123def456789"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [fr]",
      "message": "Validations passed for fr for ui.settings.audio",
      "channel": "slack"
    }),
  ],

  outputs=[
    "context consulted (run_001, abc123def456789)",
    "tms_job created",
    "FR/ES translations recorded",
    "FR validation passed",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_043",
  instruction=(
    "You document a deterministic DE overflow detection and resolution for 'ui.main_menu.start_game'. "
    "Your success criteria: the current value is consulted; validation is first recorded as failed (Text exceeds 200px width) and then recorded as passed; "
    "a high-priority UI/Main Menu job is captured; a completed workflow for PR 1023 exists with owner and test-result metadata; "
    "and an update notification confirms resolution. Use tool-generated IDs/timestamps only. Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "de"}),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "de",
      "validation_status": "failed", "validation_error": "Text exceeds 200px width"
    }),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["de"], "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "de", "validation_status": "passed"
    }),

    Action(name="create_localization_workflow", kwargs={
    "pr_number": 1023,
    "changed_keys": ["ui.main_menu.start_game"],
    "locales_processed": ["de"],
    "overflow_issues": 1,
    "status": "completed",
    "metadata": {
        "component": "ui",
        "subcomponent": "main_menu",
        "owner": "tool-generated",          
        "test_result_id": "tool-generated"  
    }
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.main_menu.start_game [de]",
      "message": "Validations passed for de for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],

  outputs=[
    "context consulted (de)",
    "de failed",
    "tms_job created",
    "de passed",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_044",
  instruction=(
    "You capture the current ES value for 'ui.settings.audio', then persist a deterministic linkage and ES settings update. "
    "Your success criteria: a medium-priority UI/Settings job is captured; work_045 → work_130 is linked (relates_to) and work_130 is tagged with 'localization'; "
    "exactly one ES translation ('Audio') is recorded; a completed workflow for PR 1024 exists; and an update notification confirms link + ES audio done. "
    "Use tool-generated IDs/timestamps only. Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "es"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["es"], "priority": "medium",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),

    Action(name="link_work_items", kwargs={"parent_id": "work_045", "child_id": "work_130", "link_type": "relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_130", "label_name": "localization"}),

    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.settings.audio", "locale": "es", "target_string": "Audio"}
      ]
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1024,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["es"],
      "overflow_issues": 0,
      "status": "completed",
      "metadata": {"component": "ui"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Link + ES audio done",
      "message": "work_130 linked; ES update completed",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (es)",
    "tms_job created",
    "work_045→work_130 linked",
    "work_130 tagged",
    "es translation recorded",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_045",
  instruction=(
    "You document a subtitle timing adjustment for the hero intro cut with VO traceability. "
    "Your success criteria: a medium-priority VO job is captured with metadata.asset_path='hero intro cut'; "
    "work_055 → work_160 is linked with link_type='relates_to'; "
    "a completed workflow for PR 1025 exists referencing the VO key 'vo.hero.intro_01' "
    "(changed_keys=['vo.hero.intro_01'], locales_processed=['en']); "
    "and an update Slack notification is sent with title='Subtitle timing adjusted' and message='vo.hero.intro_01 adjusted'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "target_locales": ["en"],
      "priority": "medium",
      "metadata": {"asset_path": "hero intro cut"}
    }),
    Action(name="link_work_items", kwargs={
      "parent_id": "work_055",
      "child_id": "work_160",
      "link_type": "relates_to"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1025,
      "changed_keys": ["vo.hero.intro_01"],
      "locales_processed": ["en"],
      "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Subtitle timing adjusted",
      "message": "vo.hero.intro_01 adjusted",
      "channel": "slack"
    }),
  ],
  outputs=[
    "tms_job created",
    "work items linked",
    "localization workflow completed",
    "notification sent"
  ]
),



Task(
  annotator="dev_ops",
  user_id="V6_046",
  instruction=(
    "You ensure a ZH main-menu update is reflected with minimal, deterministic artifacts. "
    "Your success criteria: the current ZH value for 'ui.main_menu.start_game' is consulted; "
    "a high-priority UI/Main Menu job is captured; exactly one ZH translation ('开始游戏') is recorded with no extra fields; "
    "validation is set to passed with no error; a completed workflow for PR 1026 exists with asset metadata; "
    "and an update notification confirms ZH updated. Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "zh"}),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["zh"], "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.main_menu.start_game", "locale": "zh", "target_string": "开始游戏"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game", "locale": "zh", "validation_status": "passed"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1026,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["zh"],
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.main_menu.start_game [zh]",
      "message": "Validations passed for zh for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (zh)", "tms_job created",
    "zh translation recorded", "zh validation passed",
    "localization workflow completed", "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_047",
  instruction=(
    "You document a deterministic DE overflow detection and resolution for 'ui.main_menu.start_game'. "
    "Your deliverables must show: a validation history where DE first fails with validation_error 'Text exceeds 200px width' and later passes; "
    "an update Slack notification with title 'Validations failed: ui.main_menu.start_game [de]' and message 'Text exceeds 200px width for ui.main_menu.start_game'; "
    "a single high-priority TMS job targeting 'de' under UI/Main Menu; and a completed workflow for PR 1027 with "
    "changed_keys=['ui.main_menu.start_game'], locales_processed=['de'], overflow_issues=1, status='completed'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game",
      "locale": "de",
      "validation_status": "failed",
      "validation_error": "Text exceeds 200px width"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations failed: ui.main_menu.start_game [de]",
      "message": "Text exceeds 200px width for ui.main_menu.start_game",
      "channel": "slack"
    }),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["de"],
      "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game",
      "locale": "de",
      "validation_status": "passed"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1027,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["de"],
      "overflow_issues": 1,
      "status": "completed"
    }),
  ],
  outputs=[
    "de failed",
    "notification sent",
    "tms_job created",
    "de passed",
    "localization workflow completed"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_048",
  instruction=(
    "You will persist a deterministic JA rollout for 'ui.settings.audio' with linkage. "
    "Outcomes required: the current JA value for 'ui.settings.audio' is consulted read-only; a high-priority UI/Settings TMS job targeting 'ja' is recorded; "
    "work_045 → work_150 is linked with link_type='relates_to' and work_150 is tagged 'localization'; a completed localization workflow for PR 1028 exists with "
    "changed_keys=['ui.settings.audio'], locales_processed=['ja'], overflow_issues=0, status='completed'; and an info Slack notification is sent using "
    "title='Job queued: ui.settings.audio [ja]' and message='TMS job created for ui.settings.audio'. Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={
      "string_key": "ui.settings.audio",
      "locale": "ja"
    }),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["ja"],
      "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),
    Action(name="link_work_items", kwargs={
      "parent_id": "work_045",
      "child_id": "work_150",
      "link_type": "relates_to"
    }),
    Action(name="tag_work_item_with_label", kwargs={
      "work_item_id": "work_150",
      "label_name": "localization"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1028,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["ja"],
      "overflow_issues": 0,
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.settings.audio [ja]",
      "message": "TMS job created for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (ja)",
    "tms_job created",
    "link created",
    "label applied",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_049",
  instruction=(
    "You consult the current ES record for 'ui.settings.audio' (read-only), then apply a deterministic ES update with validation and traceability. "
    "Your success criteria: exactly one ES translation ('Audio') is recorded with no extra fields; ES validation is set to passed with no error; "
    "a medium-priority UI/Settings job is captured; a completed workflow for PR 1029 exists; and an update notification confirms the translation applied. "
    "Use tool-generated IDs/timestamps only. Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "es"}),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.settings.audio", "locale": "es", "target_string": "Audio"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "es", "validation_status": "passed"
    }),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["es"], "priority": "medium",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1029,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["es"],
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [es]",
      "message": "Validations passed for es for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (es)", "es translation recorded",
    "es validation passed", "tms_job created",
    "localization workflow completed", "notification sent"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_050",
  instruction=(
    "You will persist a deterministic UI batch rollout for FR/ES/DE using the existing 'localization' label and minimal fixed fields. "
    "Outcomes required: a high-priority UI batch job for FR/ES/DE is captured; a completed workflow for PR 1030 exists over "
    "changed_keys=['ui.main_menu.start_game','ui.settings.audio'] and locales_processed=['fr','es','de']; work_130 is tagged with "
    "the existing 'localization' label; and an info Slack notification is sent using the exact strings "
    "title='Localization workflow completed: ui.main_menu.start_game, ui.settings.audio [fr,es,de]' and "
    "message='Localization workflow completed for ui.main_menu.start_game, ui.settings.audio (fr, es, de)'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["fr", "es", "de"],
      "priority": "high",
      "metadata": {"component": "ui"}
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1030,
      "changed_keys": ["ui.main_menu.start_game", "ui.settings.audio"],
      "locales_processed": ["fr", "es", "de"],
      "status": "completed",
      "metadata": {"component": "ui"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Localization workflow completed: ui.main_menu.start_game, ui.settings.audio [fr,es,de]",
      "message": "Localization workflow completed for ui.main_menu.start_game, ui.settings.audio (fr, es, de)",
      "channel": "slack"
    }),
    Action(name="tag_work_item_with_label", kwargs={
      "work_item_id": "work_130",
      "label_name": "localization"
    }),
  ],
  outputs=[
    "tms_job created",
    "localization workflow completed",
    "notification sent",
    "label applied"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_051",
  instruction=(
    "You will consult CI context and persist a JA main-menu update with traceability. "
    "Outcomes required: build run 'run_001' and test result 'test_result_001' are consulted read-only; a high-priority UI/Main Menu job "
    "targeting JA is recorded; exactly one JA translation ('ゲーム開始') is recorded for 'ui.main_menu.start_game'; a completed workflow for "
    "PR 1031 exists including build_run_id='run_001' and test_result_id='test_result_001'; and an update Slack notification is sent using the exact strings "
    "title='JA start label applied: ui.main_menu.start_game [ja]' and "
    "message='JA start label applied for ui.main_menu.start_game'. "
    "Use tool-generated IDs/timestamps only. Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_build_run", kwargs={"id": "run_001"}),
    Action(name="get_test_result", kwargs={"id": "test_result_001"}),
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "ja"}),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["ja"],
      "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),
    Action(name="record_translations", kwargs={
      "entries": [{"string_key": "ui.main_menu.start_game", "locale": "ja", "target_string": "ゲーム開始"}]
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1031,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["ja"],
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "main_menu", "build_run_id": "run_001", "test_result_id": "test_result_001"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "JA start label applied: ui.main_menu.start_game [ja]",
      "message": "JA start label applied for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (run_001, test_result_001, ja string read)",
    "tms_job created",
    "ja translation recorded",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_052",
  instruction=(
    "You will capture a deterministic IT/PT settings update. Outcomes required: a high-priority UI/Settings job for IT and PT is recorded; "
    "the current IT and PT values for 'ui.settings.audio' are consulted read-only; exactly one IT translation ('Audio') and one PT translation ('Áudio') "
    "are recorded (entries include only string_key, locale, target_string); both locales are set to validation 'passed'; a completed workflow "
    "for PR 1032 exists; and an update notification confirms validation using the exact strings "
    "title='Validations passed: ui.settings.audio [it,pt]' and message='Validations passed for it,pt for ui.settings.audio'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["it", "pt"],
      "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "it"}),
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "pt"}),

    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.settings.audio", "locale": "it", "target_string": "Audio"},
        {"string_key": "ui.settings.audio", "locale": "pt", "target_string": "Áudio"}
      ]
    }),

    Action(name="update_locale_validation", kwargs={"string_key": "ui.settings.audio", "locale": "it", "validation_status": "passed"}),
    Action(name="update_locale_validation", kwargs={"string_key": "ui.settings.audio", "locale": "pt", "validation_status": "passed"}),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1032,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["it", "pt"],
      "overflow_issues": 0,
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [it,pt]",
      "message": "Validations passed for it,pt for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "tms_job created",
    "context consulted (it, pt)",
    "it/pt translations recorded",
    "it passed",
    "pt passed",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_053",
  instruction=(
    "You will execute a deterministic RU/PL main-menu rollout. Outcomes required: a high-priority UI/Main Menu job for RU/PL is recorded; "
    "the current RU and PL values for 'ui.main_menu.start_game' are consulted read-only; exactly one RU translation ('Начать игру') and one PL translation "
    "('Rozpocznij grę') are recorded (entries include only string_key, locale, target_string); both locales are set to validation 'passed'; "
    "a completed workflow for PR 1033 exists; and an update notification confirms validation using the exact strings "
    "title='Validations passed: ui.main_menu.start_game [ru,pl]' and message='Validations passed for ru,pl for ui.main_menu.start_game'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["ru", "pl"],
      "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "ru"}),
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "pl"}),

    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.main_menu.start_game", "locale": "ru", "target_string": "Начать игру"},
        {"string_key": "ui.main_menu.start_game", "locale": "pl", "target_string": "Rozpocznij grę"}
      ]
    }),

    Action(name="update_locale_validation", kwargs={"string_key": "ui.main_menu.start_game", "locale": "ru", "validation_status": "passed"}),
    Action(name="update_locale_validation", kwargs={"string_key": "ui.main_menu.start_game", "locale": "pl", "validation_status": "passed"}),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1033,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["ru", "pl"],
      "overflow_issues": 0,
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.main_menu.start_game [ru,pl]",
      "message": "Validations passed for ru,pl for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=[
    "tms_job created",
    "context consulted (ru, pl)",
    "ru/pl translations recorded",
    "ru passed",
    "pl passed",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_054",
  instruction=(
    "You will record a deterministic FR overflow detect/resolve. Outcomes required: the current FR value for 'ui.main_menu.start_game' is consulted read-only; "
    "validation is recorded as failed with validation_error='Text exceeds 200px width' and subsequently recorded as passed; a high-priority UI/Main Menu job "
    "for FR is captured; a completed workflow for PR 1034 exists; and an update notification confirms resolution using the exact strings "
    "title='Validations passed: ui.main_menu.start_game [fr]' and message='Validations passed for fr for ui.main_menu.start_game'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "fr"}),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game",
      "locale": "fr",
      "validation_status": "failed",
      "validation_error": "Text exceeds 200px width"
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game",
      "locale": "fr",
      "validation_status": "passed"
    }),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["fr"],
      "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1034,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["fr"],
      "overflow_issues": 1,
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.main_menu.start_game [fr]",
      "message": "Validations passed for fr for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (fr)",
    "fr failed",
    "fr passed",
    "tms_job created",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_055",
  instruction=(
    "You will persist a deterministic ES/FR settings and linkage update. Outcomes required: a medium-priority UI/Settings job for ES/FR is captured; "
    "work_045 → work_131 is linked with link_type='relates_to'; work_131 is tagged with 'localization'; a completed workflow for PR 1035 exists over "
    "changed_keys=['ui.settings.audio'] and locales_processed=['es','fr']; and a 'job queued' Slack notification is sent using the exact strings "
    "title='Job queued: ui.settings.audio [es,fr]' and message='TMS job created for ui.settings.audio' with notification_type='info'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["es", "fr"],
      "priority": "medium",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),
    Action(name="link_work_items", kwargs={
      "parent_id": "work_045",
      "child_id": "work_131",
      "link_type": "relates_to"
    }),
    Action(name="tag_work_item_with_label", kwargs={
      "work_item_id": "work_131",
      "label_name": "localization"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1035,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["es", "fr"],
      "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.settings.audio [es,fr]",
      "message": "TMS job created for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "tms_job created",
    "work items linked",
    "work item tagged",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_056",
  instruction=(
    "You will capture a deterministic VO timing update and artifacts. Outcomes required: subtitle_001 timing is updated to start 0.20s and end 2.50s; "
    "a medium-priority VO job is captured; a completed workflow for PR 1036 exists; and a 'job queued' Slack notification is sent using the exact strings "
    "title='Job queued: subtitle_001 [en]' and message='TMS job created for subtitle_001' with notification_type='info'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="update_subtitle_timing", kwargs={
      "id": "subtitle_001",
      "updates": {"subtitle_start": 0.20, "subtitle_end": 2.50}
    }),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["en"],
      "priority": "medium",
      "metadata": {"component": "vo"}
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1036,
      "changed_keys": [],
      "locales_processed": ["en"],
      "overflow_issues": 0,
      "status": "completed",
      "metadata": {"component": "vo"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: subtitle_001 [en]",
      "message": "TMS job created for subtitle_001",
      "channel": "slack"
    }),
  ],
  outputs=[
    "subtitle_001 updated",
    "tms_job created",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_057",
  instruction=(
    "You will persist a deterministic KO main-menu update. Outcomes required: a high-priority UI/Main Menu job for KO is captured; "
    "exactly one KO translation ('게임 시작') is recorded (entry includes only string_key, locale, target_string); KO validation is set to 'passed'; "
    "a completed workflow for PR 1037 exists; and an update notification confirms validation using "
    "title='Validations passed: ui.main_menu.start_game [ko]' and message='Validations passed for ko for ui.main_menu.start_game'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["ko"],
      "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),

    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.main_menu.start_game", "locale": "ko", "target_string": "게임 시작"}
      ]
    }),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.main_menu.start_game",
      "locale": "ko",
      "validation_status": "passed"
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1037,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["ko"],
      "overflow_issues": 0,
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.main_menu.start_game [ko]",
      "message": "Validations passed for ko for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=[
    "tms_job created",
    "ko translation recorded",
    "ko validation passed",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_058",
  instruction=(
    "You capture CI context and persist a deterministic UI batch rollout for IT/PT/FR. Success criteria: build run 'run_001' and commit "
    "'abc123def456789' are consulted read-only; exactly one IT/PT/FR translation ('Audio') each is recorded (entries include only string_key, locale, target_string); "
    "all three locales are validated as passed; a high-priority UI job with that CI metadata is recorded; work_045 → work_130 is linked with link_type='relates_to' "
    "and work_130 is tagged 'localization'; a completed workflow for PR 1038 exists with the CI metadata; and an info notification confirms validation using "
    "title='Validations passed: ui.settings.audio [fr,it,pt]' and message='Validations passed for fr,it,pt for ui.settings.audio'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_build_run", kwargs={"id": "run_001"}),
    Action(name="get_source_change", kwargs={"commit_sha": "abc123def456789"}),
    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.settings.audio", "locale": "it", "target_string": "Audio"},
        {"string_key": "ui.settings.audio", "locale": "pt", "target_string": "Audio"},
        {"string_key": "ui.settings.audio", "locale": "fr", "target_string": "Audio"}
      ]
    }),
    Action(name="update_locale_validation", kwargs={"string_key": "ui.settings.audio", "locale": "it", "validation_status": "passed"}),
    Action(name="update_locale_validation", kwargs={"string_key": "ui.settings.audio", "locale": "pt", "validation_status": "passed"}),
    Action(name="update_locale_validation", kwargs={"string_key": "ui.settings.audio", "locale": "fr", "validation_status": "passed"}),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["it", "pt", "fr"],
      "priority": "high",
      "metadata": {"component": "ui", "build_run_id": "run_001", "commit_sha": "abc123def456789"}
    }),
    Action(name="link_work_items", kwargs={"parent_id": "work_045", "child_id": "work_130", "link_type": "relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_130", "label_name": "localization"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1038,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["it", "pt", "fr"],
      "overflow_issues": 0,
      "status": "completed",
      "metadata": {"component": "ui", "build_run_id": "run_001", "commit_sha": "abc123def456789"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Validations passed: ui.settings.audio [fr,it,pt]",
      "message": "Validations passed for fr,it,pt for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (run_001, abc123def456789)",
    "it/pt/fr translations recorded",
    "it/pt/fr validation passed",
    "tms_job created",
    "work_045→work_130 linked and labeled",
    "localization workflow completed",
    "notification sent"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_059",
  instruction=(
    "You will triage a CI build failure and start a DE remediation with traceability. Success criteria: build run 'run_003', commit 'abc123def456789', "
    "and test_result 'test_result_001' are consulted read-only; a high-priority job for DE is recorded with the CI metadata; work_110 → work_210 is linked "
    "with link_type='relates_to'; an in-progress workflow for PR 1039 exists over 'ui.main_menu.start_game'; and an update notification uses the deterministic "
    "template title='Job queued: ui.main_menu.start_game [de]' and message='TMS job created for ui.main_menu.start_game'. Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_build_run", kwargs={"id": "run_003"}),
    Action(name="get_source_change", kwargs={"commit_sha": "abc123def456789"}),
    Action(name="get_test_result", kwargs={"id": "test_result_001"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["de"],
      "priority": "high",
      "metadata": {
        "component": "ui",
        "subcomponent": "main_menu",
        "build_run_id": "run_003",
        "commit_sha": "abc123def456789",
        "test_result_id": "test_result_001"
      }
    }),

    Action(name="link_work_items", kwargs={"parent_id": "work_110", "child_id": "work_210", "link_type": "relates_to"}),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1039,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["de"],
      "status": "in_progress",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Job queued: ui.main_menu.start_game [de]",
      "message": "TMS job created for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=[
    "CI context consulted (run_003, abc123def456789, test_result_001)",
    "remediation tms_job created",
    "work items linked",
    "workflow started (in_progress)",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_060",
  instruction=(
    "You will persist a deterministic JA settings apply v2. Success criteria: exactly one JA translation ('オーディオ') is recorded for 'ui.settings.audio' "
    "(entry includes only string_key, locale, target_string); JA validation is set to passed; a medium-priority UI/Settings job targeting JA is captured; "
    "a completed workflow for PR 1040 exists; and an update notification confirms validation using "
    "title='Validations passed: ui.settings.audio [ja]' and message='Validations passed for ja for ui.settings.audio'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.settings.audio", "locale": "ja", "target_string": "オーディオ"}
      ]
    }),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio",
      "locale": "ja",
      "validation_status": "passed"
    }),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["ja"],
      "priority": "medium",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1040,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["ja"],
      "overflow_issues": 0,
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [ja]",
      "message": "Validations passed for ja for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "ja translation recorded",
    "ja validation passed",
    "tms_job created",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_061",
  instruction=(
    "You complete an audited FR/ES settings-audio application with CI traceability. "
    "Success: build run 'run_001' is consulted read-only; a high-priority UI/Settings job for FR/ES is recorded with CI metadata "
    "(build_run_id 'run_001'); exactly one FR and one ES translation ('Audio') are recorded (entries include only string_key, locale, target_string); "
    "both locales are validated 'passed' with validation_error 'None'; work_045→work_130 is linked with link_type='relates_to' and work_130 is tagged 'localization'; "
    "a completed workflow for PR 1041 exists with the same CI metadata; and an info notification confirms completion using "
    "title='Localization completed: ui.settings.audio [fr,es]' and message='Completed rollout for ui.settings.audio (fr, es)'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_build_run", kwargs={"id": "run_001"}),

    Action(name="record_translations", kwargs={"entries": [
      {"string_key": "ui.settings.audio", "locale": "fr", "target_string": "Audio"},
      {"string_key": "ui.settings.audio", "locale": "es", "target_string": "Audio"}
    ]}),
    Action(name="update_locale_validation", kwargs={"string_key": "ui.settings.audio", "locale": "fr", "validation_status": "passed", "validation_error": "None"}),
    Action(name="update_locale_validation", kwargs={"string_key": "ui.settings.audio", "locale": "es", "validation_status": "passed", "validation_error": "None"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["fr", "es"], "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "settings", "build_run_id": "run_001"}
    }),

    Action(name="link_work_items", kwargs={"parent_id": "work_045", "child_id": "work_130", "link_type": "relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_130", "label_name": "localization"}),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1041, "changed_keys": ["ui.settings.audio"], "locales_processed": ["fr", "es"],
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "settings", "build_run_id": "run_001"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Localization completed: ui.settings.audio [fr,es]",
      "message": "Completed rollout for ui.settings.audio (fr, es)",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (run_001)",
    "fr/es translations recorded",
    "fr/es validation passed",
    "tms_job created",
    "work_045→work_130 linked",
    "work_130 labeled",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_062",
  instruction=(
    "You complete an audited IT main-menu update with CI traceability. "
    "Success: build run 'run_001' is consulted read-only; the current IT value is consulted; exactly one IT translation ('Inizia') is recorded "
    "(entry includes only string_key, locale, target_string); IT validation is 'passed' with validation_error 'None'; "
    "a high-priority UI/Main Menu job is recorded with metadata (build_run_id 'run_001'); work_045→work_140 is linked with link_type='relates_to' and tagged 'localization'; "
    "a completed workflow for PR 1042 exists; and an info notification confirms completion using "
    "title='Localization completed: ui.main_menu.start_game [it]' and message='Completed rollout for ui.main_menu.start_game (it)'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_build_run", kwargs={"id": "run_001"}),
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "it"}),

    Action(name="record_translations", kwargs={"entries": [
      {"string_key": "ui.main_menu.start_game", "locale": "it", "target_string": "Inizia"}
    ]}),
    Action(name="update_locale_validation", kwargs={"string_key": "ui.main_menu.start_game", "locale": "it", "validation_status": "passed", "validation_error": "None"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["it"], "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "main_menu", "build_run_id": "run_001"}
    }),

    Action(name="link_work_items", kwargs={"parent_id": "work_045", "child_id": "work_140", "link_type": "relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_140", "label_name": "localization"}),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1042, "changed_keys": ["ui.main_menu.start_game"], "locales_processed": ["it"],
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "main_menu", "build_run_id": "run_001"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Localization completed: ui.main_menu.start_game [it]",
      "message": "Completed rollout for ui.main_menu.start_game (it)",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (run_001, it string read)",
    "it translation recorded",
    "it validation passed",
    "tms_job created",
    "work_045→work_140 linked",
    "work_140 labeled",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_063",
  instruction=(
    "You run a batch rollout for JA/KO tied to asset 'assets/ui/main_menu.json'. "
    "Success: a high-priority UI job targets JA/KO with metadata.asset_path='assets/ui/main_menu.json'; exactly four translations are recorded "
    "(ui.main_menu.start_game: JA 'ゲーム開始', KO '게임 시작'; ui.settings.audio: JA 'オーディオ', KO '오디오') with entries containing only string_key, locale, target_string; "
    "work_060→work_132 is linked with link_type='relates_to'; a completed workflow for PR 1043 exists over "
    "changed_keys=['ui.main_menu.start_game','ui.settings.audio'] and locales_processed=['ja','ko']; and an info notification confirms completion using "
    "title='Batch complete: ui.main_menu.start_game, ui.settings.audio [ja,ko]' and "
    "message='Completed rollout for ui.main_menu.start_game and ui.settings.audio (ja, ko)'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["ja", "ko"], "priority": "high",
      "metadata": {"component": "ui", "asset_path": "assets/ui/main_menu.json"}
    }),
    Action(name="record_translations", kwargs={"entries": [
      {"string_key": "ui.main_menu.start_game", "locale": "ja", "target_string": "ゲーム開始"},
      {"string_key": "ui.main_menu.start_game", "locale": "ko", "target_string": "게임 시작"},
      {"string_key": "ui.settings.audio", "locale": "ja", "target_string": "オーディオ"},
      {"string_key": "ui.settings.audio", "locale": "ko", "target_string": "오디오"}
    ]}),
    Action(name="link_work_items", kwargs={"parent_id": "work_060", "child_id": "work_132", "link_type": "relates_to"}),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1043, "changed_keys": ["ui.main_menu.start_game", "ui.settings.audio"],
      "locales_processed": ["ja", "ko"], "status": "completed",
      "metadata": {"component": "ui"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Batch complete: ui.main_menu.start_game, ui.settings.audio [ja,ko]",
      "message": "Completed rollout for ui.main_menu.start_game and ui.settings.audio (ja, ko)",
      "channel": "slack"
    }),
  ],
  outputs=[
    "tms_job created",
    "translations recorded",
    "work items linked",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_064",
  instruction=(
    "You complete an audited DE truncation remediation for 'ui.settings.audio' with CI traceability. "
    "Show, in the resulting artifacts, that you consulted build run 'run_001' and read the current DE value without modifying it; "
    "that the validation lifecycle captured a failure ('Truncation risk in 180px') which ultimately resolves to 'passed'; "
    "that exactly one DE translation is recorded as 'Audio' (translation entries include only: string_key, locale, target_string); "
    "that the effort is attributed to a single high-priority UI/Settings TMS job annotated with the build run ID ('run_001'); "
    "that work_045 and work_130 are related via a 'relates_to' link and work_130 carries the 'localization' label; "
    "that PR 1044 is closed as completed with overflow_issues=1; "
    "and that completion is confirmed via an info Slack notification with "
    "title='Localization completed: ui.settings.audio [de]' and "
    "message='Completed remediation and rollout for ui.settings.audio (de)'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_build_run", kwargs={"id": "run_001"}),
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "de"}),

    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "de",
      "validation_status": "failed", "validation_error": "Truncation risk in 180px"
    }),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["de"], "priority": "high",
      "metadata": {"build_run_id": "run_001"}
    }),

    Action(name="record_translations", kwargs={
      "entries": [
        {"string_key": "ui.settings.audio", "locale": "de", "target_string": "Audio"}
      ]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key": "ui.settings.audio", "locale": "de",
      "validation_status": "passed", "validation_error": "None"
    }),

    Action(name="link_work_items", kwargs={
      "parent_id": "work_045", "child_id": "work_130", "link_type": "relates_to"
    }),
    Action(name="tag_work_item_with_label", kwargs={
      "work_item_id": "work_130", "label_name": "localization"
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1044,
      "changed_keys": ["ui.settings.audio"],
      "locales_processed": ["de"],
      "overflow_issues": 1,
      "status": "completed"
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Localization completed: ui.settings.audio [de]",
      "message": "Completed remediation and rollout for ui.settings.audio (de)",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (run_001, de string read)",
    "de failed then passed",
    "tms_job created",
    "de translation recorded",
    "work_045→work_130 linked and labeled",
    "localization workflow completed",
    "notification sent"
  ]
),



Task(
  annotator="dev_ops",
  user_id="V6_065",
  instruction=(
    "You will perform a deterministic IT/PT main-menu apply for string_key 'ui.main_menu.start_game'. "
    "Success: the current value for 'ui.main_menu.start_game' is consulted read-only for both it and pt; "
    "exactly one PT 'Iniciar' and one IT 'Inizia' translation entry are recorded (entries include only string_key, locale, target_string); "
    "a medium-priority UI/Main Menu job is captured with metadata {'component':'ui','subcomponent':'main_menu'}; "
    "a completed workflow for PR 1045 exists referencing changed_keys=['ui.main_menu.start_game'] and locales_processed=['it','pt']; "
    "and an update Slack notification is sent with title='Localization applied: ui.main_menu.start_game [it,pt]' "
    "and message='Applied translations for ui.main_menu.start_game (it,pt)'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "it"}),
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "pt"}),

    Action(name="record_translations", kwargs={"entries": [
      {"string_key": "ui.main_menu.start_game", "locale": "pt", "target_string": "Iniciar"},
      {"string_key": "ui.main_menu.start_game", "locale": "it", "target_string": "Inizia"}
    ]}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en",
      "target_locales": ["it", "pt"],
      "priority": "medium",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1045,
      "changed_keys": ["ui.main_menu.start_game"],
      "locales_processed": ["it", "pt"],
      "status": "completed"
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Localization applied: ui.main_menu.start_game [it,pt]",
      "message": "Applied translations for ui.main_menu.start_game (it,pt)",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (it,pt)",
    "pt/it translations recorded",
    "tms_job created",
    "localization workflow completed",
    "notification sent"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_066",
  instruction=(
    "You will refresh the French 'Settings Audio' string. "
    "Success: existing FR string consulted; medium-priority UI/Settings job captured; one FR translation ('Audio (actualisé)') recorded and validated 'passed'; "
    "work_050→work_140 linked (relates_to) and work_140 tagged 'localization'; completed workflow for PR 1046; and an update notification. "
    "Use tool-generated IDs/timestamps only. Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "fr"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["fr"], "priority": "medium",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),

    Action(name="record_translations", kwargs={"entries": [
      {"string_key": "ui.settings.audio", "locale": "fr", "target_string": "Audio (actualisé)"}
    ]}),
    Action(name="update_locale_validation", kwargs={"string_key": "ui.settings.audio", "locale": "fr", "validation_status": "passed"}),

    Action(name="link_work_items", kwargs={"parent_id": "work_050", "child_id": "work_140", "link_type": "relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id": "work_140", "label_name": "localization"}),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1046, "changed_keys": ["ui.settings.audio"], "locales_processed": ["fr"],
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [fr]",
      "message": "Validations passed for fr for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted (fr)",
    "tms_job created",
    "translation recorded and validated",
    "work items linked and labeled",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_067",
  instruction=(
    "You apply a VO timing polish for 'subtitle_001'. "
    "Success: subtitle_001 is updated to start 0.15s and end 2.40s; a medium-priority EN timing job is recorded; "
    "a completed workflow for PR 1047 references the timing key (changed_keys=['subtitle_001'], locales_processed=['en']); "
    "and an info notification confirms the adjustment using title='Subtitle timing adjusted' and message='subtitle_001 adjusted'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="update_subtitle_timing", kwargs={"id": "subtitle_001", "updates": {"subtitle_start": 0.15, "subtitle_end": 2.40}}),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["en"], "priority": "medium"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1047, "changed_keys": ["subtitle_001"], "locales_processed": ["en"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Subtitle timing adjusted",
      "message": "subtitle_001 adjusted",
      "channel": "slack"
    }),
  ],
  outputs=["subtitle_001 updated", "tms_job created", "localization workflow completed", "notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_068",
  instruction=(
    "You perform a deterministic ZH main-menu update v2. "
    "Success: the current ZH value for 'ui.main_menu.start_game' is consulted read-only; "
    "a high-priority UI/Main Menu job for ZH is recorded with metadata.component='ui' and metadata.subcomponent='main_menu'; "
    "exactly one ZH translation ('开始游戏') is recorded (entry includes only string_key, locale, target_string); "
    "ZH validation is set to 'passed'; a completed workflow for PR 1048 exists with the same metadata; "
    "and an update notification confirms validation using title='Validations passed: ui.main_menu.start_game [zh]' and "
    "message='Validations passed for zh for ui.main_menu.start_game'. Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.main_menu.start_game", "locale": "zh"}),
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["zh"], "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),
    Action(name="record_translations", kwargs={"entries": [
      {"string_key": "ui.main_menu.start_game", "locale": "zh", "target_string": "开始游戏"}
    ]}),
    Action(name="update_locale_validation", kwargs={"string_key": "ui.main_menu.start_game", "locale": "zh", "validation_status": "passed"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1048, "changed_keys": ["ui.main_menu.start_game"], "locales_processed": ["zh"],
      "status": "completed", "metadata": {"component": "ui", "subcomponent": "main_menu"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.main_menu.start_game [zh]",
      "message": "Validations passed for zh for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=["context consulted", "tms_job created", "zh translation recorded", "zh validation passed", "localization workflow completed", "notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_069",
  instruction=(
    "You handle a Spanish main-menu update triggered by commit 'def234abc' for asset 'assets/ui/main_menu.json'. "
    "Success: a high-priority UI/Main Menu job is recorded with metadata.commit_sha='def234abc' and metadata.asset_path='assets/ui/main_menu.json'; "
    "exactly one ES translation ('Comenzar juego') is recorded (entry includes only string_key, locale, target_string); "
    "work_070→work_170 is linked with link_type='relates_to'; a completed workflow for PR 1049 exists; "
    "and an info notification uses the 'Job queued' template with "
    "title='Job queued: ui.main_menu.start_game [es]' and message='TMS job created for ui.main_menu.start_game'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["es"], "priority": "high",
      "metadata": {"commit_sha": "def234abc", "asset_path": "assets/ui/main_menu.json"}
    }),
    Action(name="record_translations", kwargs={"entries": [
      {"string_key": "ui.main_menu.start_game", "locale": "es", "target_string": "Comenzar juego"}
    ]}),
    Action(name="link_work_items", kwargs={"parent_id": "work_070", "child_id": "work_170", "link_type": "relates_to"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1049, "changed_keys": ["ui.main_menu.start_game"], "locales_processed": ["es"], "status": "completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type": "info",
      "title": "Job queued: ui.main_menu.start_game [es]",
      "message": "TMS job created for ui.main_menu.start_game",
      "channel": "slack"
    }),
  ],
  outputs=["tms_job created", "translation recorded", "work items linked", "localization workflow completed", "notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_070",
  instruction=(
    "You will capture a deterministic FR/DE settings validation after consulting the current value read-only. "
    "Success: high-priority UI/Settings job for FR/DE; one FR and one DE translation ('Audio'); both locales validated 'passed'; "
    "completed workflow for PR 1050; and an update notification. Use tool-generated IDs/timestamps only. "
    "Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "fr"}),
    Action(name="get_loc_string", kwargs={"string_key": "ui.settings.audio", "locale": "de"}),

    Action(name="create_tms_job", kwargs={
      "source_locale": "en", "target_locales": ["fr", "de"], "priority": "high",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),

    Action(name="record_translations", kwargs={"entries": [
      {"string_key": "ui.settings.audio", "locale": "fr", "target_string": "Audio"},
      {"string_key": "ui.settings.audio", "locale": "de", "target_string": "Audio"}
    ]}),
    Action(name="update_locale_validation", kwargs={"string_key": "ui.settings.audio", "locale": "fr", "validation_status": "passed"}),
    Action(name="update_locale_validation", kwargs={"string_key": "ui.settings.audio", "locale": "de", "validation_status": "passed"}),

    Action(name="create_localization_workflow", kwargs={
      "pr_number": 1050, "changed_keys": ["ui.settings.audio"], "locales_processed": ["fr", "de"],
      "status": "completed",
      "metadata": {"component": "ui", "subcomponent": "settings"}
    }),

    Action(name="send_notification", kwargs={
      "notification_type": "update",
      "title": "Validations passed: ui.settings.audio [fr,de]",
      "message": "Validations passed for fr,de for ui.settings.audio",
      "channel": "slack"
    }),
  ],
  outputs=[
    "context consulted",
    "tms_job created",
    "fr/de translations recorded",
    "fr/de validation passed",
    "localization workflow completed",
    "notification sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_071",
  instruction=(
    "You persist a deterministic RU main-menu update v2 for 'ui.main_menu.start_game'. "
    "Success: a high-priority UI/Main Menu job for RU is recorded; exactly one RU translation ('Начать игру') is recorded "
    "(entry includes only string_key, locale, target_string); RU validation is set to 'passed'; a completed workflow for PR 1051 exists; "
    "and an update notification confirms validation using title='Validations passed: ui.main_menu.start_game [ru]' and "
    "message='Validations passed for ru for ui.main_menu.start_game'. Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["ru"],"priority":"high",
      "metadata":{"component":"ui","subcomponent":"main_menu"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"ui.main_menu.start_game","locale":"ru","target_string":"Начать игру"}]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key":"ui.main_menu.start_game","locale":"ru","validation_status":"passed"
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1051,"changed_keys":["ui.main_menu.start_game"],"locales_processed":["ru"],
      "status":"completed","metadata":{"component":"ui","subcomponent":"main_menu"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"update",
      "title":"Validations passed: ui.main_menu.start_game [ru]",
      "message":"Validations passed for ru for ui.main_menu.start_game",
      "channel":"slack"
    }),
  ],
  outputs=["tms_job created","ru translation recorded","ru validation passed","localization workflow completed","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_072",
  instruction=(
    "You orchestrate a dual-locale main-menu remediation for 'ui.main_menu.start_game' with CI identifiers, keeping translation entries free of validation fields. "
    "Success: CI metadata (commit 'c0ffee000000045', build 'run_045', test 'test_result_045') is captured on the job; "
    "FR 'Commencer' and DE 'Starten' are recorded; FR validation fails ('Text exceeds 200px width') then passes ('None'); DE validation passes ('None'); "
    "work_045→work_230 is linked with link_type='relates_to' and work_230 is tagged 'label_001'; a completed workflow for PR 2001 includes the same CI metadata; "
    "and two notifications are sent using title='Job queued: ui.main_menu.start_game [fr,de]' / message='TMS job created for ui.main_menu.start_game' (info) "
    "and title='Validations passed: ui.main_menu.start_game [fr,de]' / message='Validations passed for fr,de for ui.main_menu.start_game' (update). "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["fr","de"],
      "metadata":{"commit_sha":"c0ffee000000045","build_run_id":"run_045","test_result_id":"test_result_045"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[
        {"string_key":"ui.main_menu.start_game","locale":"fr","target_string":"Commencer"},
        {"string_key":"ui.main_menu.start_game","locale":"de","target_string":"Starten"}
      ]
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key":"ui.main_menu.start_game","locale":"fr","validation_status":"failed","validation_error":"Text exceeds 200px width"
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key":"ui.main_menu.start_game","locale":"fr","validation_status":"passed","validation_error":"None"
    }),
    Action(name="update_locale_validation", kwargs={
      "string_key":"ui.main_menu.start_game","locale":"de","validation_status":"passed","validation_error":"None"
    }),
    Action(name="link_work_items", kwargs={"parent_id":"work_045","child_id":"work_230","link_type":"relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_230","label_name":"label_001"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":2001,"changed_keys":["ui.main_menu.start_game"],"locales_processed":["fr","de"],
      "status":"completed",
      "metadata":{"commit_sha":"c0ffee000000045","build_run_id":"run_045","test_result_id":"test_result_045"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Job queued: ui.main_menu.start_game [fr,de]",
      "message":"TMS job created for ui.main_menu.start_game",
      "channel":"slack"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"update",
      "title":"Validations passed: ui.main_menu.start_game [fr,de]",
      "message":"Validations passed for fr,de for ui.main_menu.start_game",
      "channel":"slack"
    }),
  ],
  outputs=[
    "tms_job created","fr/de translations recorded","fr failed then passed","de passed",
    "work_045→work_230 linked","label applied","workflow completed","notifications sent"
  ]
),

Task(
  annotator="dev_ops",
  user_id="V6_073",
  instruction=(
    "You execute a tri-locale rollout for 'ui.settings.audio' with CI context and a JA overflow correction. "
    "Success criteria (goal-based, not step order): the job captures CI metadata "
    "{commit_sha:'a1b2c3d4e5f6', build_run_id:'run_046', test_result_id:'test_result_046'}; "
    "FR 'Audio', ES 'Audio', and JA 'オーディオ' are recorded (entries include only string_key, locale, target_string); "
    "FR/ES validations are 'passed' with validation_error 'None'; JA has one 'failed' reading with validation_error 'Text exceeds 200px width' "
    "and ultimately 'passed' after recording the JA correction 'サウンド'; work_045→work_150 is linked with link_type='relates_to' and work_150 is tagged 'label_001'; "
    "a completed workflow for PR 2002 exists referencing changed_keys=['ui.settings.audio'] and locales_processed=['fr','es','ja'] and the same CI metadata; "
    "and deterministic queued/completed Slack notifications are sent for 'ui.settings.audio' and locales [fr,es,ja]. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en",
      "target_locales":["fr","es","ja"],
      "metadata":{"component":"ui","subcomponent":"settings",
                  "commit_sha":"a1b2c3d4e5f6","build_run_id":"run_046","test_result_id":"test_result_046"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[
        {"string_key":"ui.settings.audio","locale":"fr","target_string":"Audio"},
        {"string_key":"ui.settings.audio","locale":"es","target_string":"Audio"},
        {"string_key":"ui.settings.audio","locale":"ja","target_string":"オーディオ"}
      ]
    }),
    Action(name="update_locale_validation", kwargs={"string_key":"ui.settings.audio","locale":"fr","validation_status":"passed","validation_error":"None"}),
    Action(name="update_locale_validation", kwargs={"string_key":"ui.settings.audio","locale":"es","validation_status":"passed","validation_error":"None"}),
    Action(name="update_locale_validation", kwargs={"string_key":"ui.settings.audio","locale":"ja","validation_status":"failed","validation_error":"Text exceeds 200px width"}),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"ui.settings.audio","locale":"ja","target_string":"サウンド"}]
    }),
    Action(name="update_locale_validation", kwargs={"string_key":"ui.settings.audio","locale":"ja","validation_status":"passed","validation_error":"None"}),
    Action(name="link_work_items", kwargs={"parent_id":"work_045","child_id":"work_150","link_type":"relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_150","label_name":"label_001"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":2002,"changed_keys":["ui.settings.audio"],"locales_processed":["fr","es","ja"],
      "status":"completed",
      "metadata":{"component":"ui","subcomponent":"settings",
                  "commit_sha":"a1b2c3d4e5f6","build_run_id":"run_046","test_result_id":"test_result_046"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Job queued: ui.settings.audio [fr,es,ja]",
      "message":"TMS job created for ui.settings.audio",
      "channel":"slack"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"update",
      "title":"Validations passed: ui.settings.audio [fr,es,ja]",
      "message":"Validations passed for fr,es,ja for ui.settings.audio",
      "channel":"slack"
    }),
  ],
  outputs=[
    "tms_job created",
    "fr/es/ja translations recorded",
    "fr/es passed",
    "ja failed then passed",
    "work_045→work_150 linked",
    "label applied",
    "workflow completed",
    "notifications sent"
  ]
),


Task(
  annotator="dev_ops",
  user_id="V6_074",
  instruction=(
    "You perform a VO timing remediation for 'subtitle_001' with CI context. "
    "Success: subtitle_001 timing is updated to start 0.20s and end 2.50s; work_045→work_160 is linked with link_type='relates_to' and labeled 'label_001'; "
    "a completed workflow for PR 2003 exists with metadata.commit_sha='feedface047', metadata.build_run_id='run_047', metadata.test_result_id='test_result_047'; "
    "and two notifications are sent using title='Job queued: subtitle_001 [en]' / message='TMS job created for subtitle_001' (info) and "
    "title='Subtitle timing adjusted' / message='subtitle_001 adjusted' (update). Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="update_subtitle_timing", kwargs={"id":"subtitle_001","updates":{"subtitle_start":0.20,"subtitle_end":2.50}}),
    Action(name="link_work_items", kwargs={"parent_id":"work_045","child_id":"work_160","link_type":"relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_160","label_name":"label_001"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":2003,"changed_keys":["subtitle_001"],"locales_processed":["en"],
      "status":"completed",
      "metadata":{"component":"vo","commit_sha":"feedface047","build_run_id":"run_047","test_result_id":"test_result_047"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Job queued: subtitle_001 [en]",
      "message":"TMS job created for subtitle_001",
      "channel":"slack"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"update",
      "title":"Subtitle timing adjusted",
      "message":"subtitle_001 adjusted",
      "channel":"slack"
    }),
  ],
  outputs=["subtitle_001 updated","work_045→work_160 linked","label applied","workflow completed","notifications sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_075",
  instruction=(
    "You resolve a DE audio settings bug discovered from CI (build 'run_008', commit 'ace111') for 'ui.settings.audio'. "
    "Success: a high-priority UI/Settings job is recorded with that CI metadata; the corrected DE translation ('Audio (korrigiert)') is recorded; "
    "work_120→work_220 is linked with link_type='relates_to' and tagged with label_003; a completed workflow for PR 1075 exists; "
    "and an update notification confirms validation using title='Validations passed: ui.settings.audio [de]' and "
    "message='Validations passed for de for ui.settings.audio'. Use tool-generated IDs/timestamps only. "
    "Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["de"],"priority":"high",
      "metadata":{"component":"ui","subcomponent":"settings","build_run_id":"run_008","commit_sha":"ace111"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"ui.settings.audio","locale":"de","target_string":"Audio (korrigiert)"}]
    }),
    Action(name="update_locale_validation", kwargs={"string_key":"ui.settings.audio","locale":"de","validation_status":"passed"}),
    Action(name="link_work_items", kwargs={"parent_id":"work_120","child_id":"work_220","link_type":"relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_220","label_name":"label_003"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1075,"changed_keys":["ui.settings.audio"],"locales_processed":["de"],
      "status":"completed","metadata":{"component":"ui","subcomponent":"settings"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"update",
      "title":"Validations passed: ui.settings.audio [de]",
      "message":"Validations passed for de for ui.settings.audio",
      "channel":"slack"
    }),
  ],
  outputs=["tms_job created","translation recorded","de validation passed","work items linked and tagged","workflow completed","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_076",
  instruction=(
    "You execute a FR/ES main-menu batch update for asset 'assets/ui/main_menu.json'. "
    "Success: one medium-priority job targets FR and ES; four translations are recorded "
    "(ui.main_menu.start_game: FR 'Lancer la partie', ES 'Iniciar partida'; ui.main_menu.quit_game: FR 'Quitter', ES 'Salir'); "
    "work_080→work_180 is linked with link_type='relates_to'; a completed workflow for PR 1076 exists; and an info notification announces completion using "
    "title='Batch completed: ui.main_menu.start_game, ui.main_menu.quit_game [fr,es]' and "
    "message='Batch completed for fr,es for ui.main_menu.start_game, ui.main_menu.quit_game'. Use tool-generated IDs/timestamps only. "
    "Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["fr","es"],"priority":"medium",
      "metadata":{"asset_path":"assets/ui/main_menu.json"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[
        {"string_key":"ui.main_menu.start_game","locale":"fr","target_string":"Lancer la partie"},
        {"string_key":"ui.main_menu.start_game","locale":"es","target_string":"Iniciar partida"},
        {"string_key":"ui.main_menu.quit_game","locale":"fr","target_string":"Quitter"},
        {"string_key":"ui.main_menu.quit_game","locale":"es","target_string":"Salir"}
      ]
    }),
    Action(name="link_work_items", kwargs={"parent_id":"work_080","child_id":"work_180","link_type":"relates_to"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1076,"changed_keys":["ui.main_menu.start_game","ui.main_menu.quit_game"],
      "locales_processed":["fr","es"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Batch completed: ui.main_menu.start_game, ui.main_menu.quit_game [fr,es]",
      "message":"Batch completed for fr,es for ui.main_menu.start_game, ui.main_menu.quit_game",
      "channel":"slack"
    }),
  ],
  outputs=["tms_job created","4 translations recorded","work items linked","localization workflow completed","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_077",
  instruction=(
    "You document a timing adjustment requirement for JA subtitle 'subtitle_007' (10.5–14.2s) tied to 'assets/subtitles/ja/level1_intro.vtt'. "
    "Your required outcomes: work_181 is labeled 'label_001'; a medium-priority JA-targeted timing job is recorded with the asset path; "
    "a completed workflow for PR 1077 includes the required_timing metadata; and an info notification is sent to user_003. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_181","label_name":"label_001"}),
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["ja"],"priority":"medium",
      "metadata":{"asset_path":"assets/subtitles/ja/level1_intro.vtt"}
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1077,"changed_keys":["subtitle_007"],"locales_processed":["ja"],
      "status":"completed",
      "metadata":{"required_timing":{"id":"subtitle_007","start":10.5,"end":14.2}}
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Job queued: subtitle_007 [ja]",
      "message":"TMS job created for subtitle_007",
      "recipient_id":"user_003",
      "channel":"slack"
    }),
  ],
  outputs=["work item labeled","tms_job created","workflow completed with timing metadata","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_078",
  instruction=(
    "You run the full localization rollout for new feature string 'ui.feature.new_button' into Chinese. "
    "Success: a high-priority ZH job is recorded; the ZH translation ('新功能') is recorded; work_081→work_182 is linked with link_type='relates_to' and work_182 is tagged 'label_001'; "
    "a completed workflow for PR 1078 exists; and an update notification confirms completion using "
    "title='Localization completed: ui.feature.new_button [zh]' and message='Localization completed for zh for ui.feature.new_button'. "
    "Use tool-generated IDs/timestamps only. Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={"source_locale":"en","target_locales":["zh"],"priority":"high"}),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"ui.feature.new_button","locale":"zh","target_string":"新功能"}]
    }),
    Action(name="link_work_items", kwargs={"parent_id":"work_081","child_id":"work_182","link_type":"relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_182","label_name":"label_001"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1078,"changed_keys":["ui.feature.new_button"],"locales_processed":["zh"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"update",
      "title":"Localization completed: ui.feature.new_button [zh]",
      "message":"Localization completed for zh for ui.feature.new_button",
      "channel":"slack"
    }),
  ],
  outputs=["tms_job created","translation recorded","work_081→work_182 linked","work_182 labeled","localization workflow completed","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_079",
  instruction=(
    "You log an investigation into a localization issue in 'src/game/engine/renderer.cpp'. "
    "Your success criteria: file ownership for that path is consulted (read-only); a high-priority DE investigation job is recorded with metadata.file_path='src/game/engine/renderer.cpp'; "
    "work_082→work_183 is linked with link_type='relates_to'; an in_progress workflow for PR 1079 exists referencing changed_keys=['src/game/engine/renderer.cpp'] and locales_processed=['de']; "
    "and an info Slack notification is sent to user_001 using title='Job queued: src/game/engine/renderer.cpp [de]' and message='TMS job created for src/game/engine/renderer.cpp'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_ownership_for_path", kwargs={"file_path":"src/game/engine/renderer.cpp"}),
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["de"],"priority":"high",
      "metadata":{"file_path":"src/game/engine/renderer.cpp"}
    }),
    Action(name="link_work_items", kwargs={"parent_id":"work_082","child_id":"work_183","link_type":"relates_to"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1079,"changed_keys":["src/game/engine/renderer.cpp"],"locales_processed":["de"],"status":"in_progress"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Job queued: src/game/engine/renderer.cpp [de]",
      "message":"TMS job created for src/game/engine/renderer.cpp",
      "recipient_id":"user_001",
      "channel":"slack"
    }),
  ],
  outputs=["file ownership consulted","investigation job created","work items linked","workflow created (in_progress)","notification sent"]
),


Task(
  annotator="dev_ops",
  user_id="V6_080",
  instruction=(
    "You fix a German main-menu UI overflow from commit 'bde222' by shortening 'ui.main_menu.quit_game' to 'Beenden'. "
    "Success: a high-priority DE job is recorded with metadata.commit_sha='bde222'; the DE translation is recorded; "
    "work_125→work_225 is linked with link_type='relates_to' and tagged with label_003; a completed workflow for PR 1080 exists; "
    "and a Slack update notifies completion using title='DE overflow fix applied: ui.main_menu.quit_game [de]' and "
    "message='Text shortened to \"Beenden\" for ui.main_menu.quit_game (de).'. Use tool-generated IDs/timestamps only. "
    "Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["de"],"priority":"high",
      "metadata":{"commit_sha":"bde222"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"ui.main_menu.quit_game","locale":"de","target_string":"Beenden"}]
    }),
    Action(name="link_work_items", kwargs={"parent_id":"work_125","child_id":"work_225","link_type":"relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_225","label_name":"label_003"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1080,"changed_keys":["ui.main_menu.quit_game"],"locales_processed":["de"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"update",
      "title":"DE overflow fix applied: ui.main_menu.quit_game [de]",
      "message":"Text shortened to \"Beenden\" for ui.main_menu.quit_game (de).",
      "channel":"slack"
    }),
  ],
  outputs=["tms_job created","translation recorded","work items linked and tagged","localization workflow completed","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_081",
  instruction=(
    "You manage a refresh of a French VO line for asset 'vo/fr/hero_intro_01.wav'. "
    "Your required outcomes: link work_083→work_184 (relates_to); create a medium-priority FR VO job with the asset path; "
    "record a new FR translation for 'vo.hero.intro_01' ('Le héros arrive.'); create a completed workflow for PR 1081; "
    "and send an update notification to user_006. Use tool-generated IDs/timestamps only. "
    "Translation entries must include only: string_key, locale, target_string."
  ),
  actions=[
    Action(name="link_work_items", kwargs={"parent_id":"work_083","child_id":"work_184","link_type":"relates_to"}),
    Action(name="create_tms_job", kwargs={
      "priority":"medium",
      "target_locales":["fr"],
      "metadata":{"asset_path":"vo/fr/hero_intro_01.wav"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"vo.hero.intro_01","locale":"fr","target_string":"Le héros arrive."}]
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1081,"changed_keys":["vo.hero.intro_01"],"locales_processed":["fr"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"update",
      "title":"Validations passed: vo.hero.intro_01 [fr]",
      "message":"Validations passed for fr for vo.hero.intro_01",
      "recipient_id":"user_006",
      "channel":"slack"
    }),
  ],
  outputs=["work items linked","tms_job created","translation recorded","workflow created","notification sent"]
),


Task(
  annotator="dev_ops",
  user_id="V6_082",
  instruction=(
    "You perform a deterministic setup for a new Spanish localization job. "
    "Success: a medium-priority ES job is created; a placeholder translation for 'ui.new_feature.title' ('[PLACEHOLDER]') is recorded "
    "(entry includes only string_key, locale, target_string); work_090→work_190 is linked with link_type='relates_to' and work_190 is tagged 'label_001'; "
    "a completed workflow for PR 1082 exists; and an info notification is sent to user_007 using "
    "title='Job queued: ui.new_feature.title [es]' and message='TMS job created for ui.new_feature.title'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={"source_locale":"en","target_locales":["es"],"priority":"medium"}),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"ui.new_feature.title","locale":"es","target_string":"[PLACEHOLDER]"}]
    }),
    Action(name="link_work_items", kwargs={"parent_id":"work_090","child_id":"work_190","link_type":"relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_190","label_name":"label_001"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1082,"changed_keys":["ui.new_feature.title"],"locales_processed":["es"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Job queued: ui.new_feature.title [es]",
      "message":"TMS job created for ui.new_feature.title",
      "recipient_id":"user_007",
      "channel":"slack"
    }),
  ],
  outputs=["tms_job created","placeholder recorded","work_090→work_190 linked","work_190 labeled","workflow completed","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_083",
  instruction=(
    "You run a multi-language validation sweep for 'ui.settings.audio' on ES/DE/FR in a pre-populated database. "
    "Your required outcomes: read current strings for ES, DE, FR; set validation to 'passed' for all three; "
    "document in a single completed workflow for PR 1083; and send a summary info notification to user_008. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="get_loc_string", kwargs={"string_key":"ui.settings.audio","locale":"es"}),
    Action(name="get_loc_string", kwargs={"string_key":"ui.settings.audio","locale":"de"}),
    Action(name="get_loc_string", kwargs={"string_key":"ui.settings.audio","locale":"fr"}),
    Action(name="update_locale_validation", kwargs={"string_key":"ui.settings.audio","locale":"es","validation_status":"passed"}),
    Action(name="update_locale_validation", kwargs={"string_key":"ui.settings.audio","locale":"de","validation_status":"passed"}),
    Action(name="update_locale_validation", kwargs={"string_key":"ui.settings.audio","locale":"fr","validation_status":"passed"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1083,"changed_keys":["ui.settings.audio"],"locales_processed":["es","de","fr"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Validations passed: ui.settings.audio [es,de,fr]",
      "message":"Validations passed for es,de,fr for ui.settings.audio",
      "recipient_id":"user_008",
      "channel":"slack"
    }),
  ],
  outputs=["context captured for ES/DE/FR","validation passed for ES/DE/FR","workflow created","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_084",
  instruction=(
    "You process a marketing-driven Japanese main title update triggered by commit 'fab444'. "
    "Your required outcomes: a high-priority JA job with commit metadata is recorded; the JA title for 'ui.main_menu.title' ('究極の冒険') is recorded "
    "(entry includes only string_key, locale, target_string); work_091→work_191 is linked with link_type='relates_to'; "
    "a completed workflow for PR 1084 exists; and an info notification to user_009 is sent using "
    "title='Job queued: ui.main_menu.title [ja]' and message='TMS job created for ui.main_menu.title'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["ja"],"priority":"high",
      "metadata":{"commit_sha":"fab444"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"ui.main_menu.title","locale":"ja","target_string":"究極の冒険"}]
    }),
    Action(name="link_work_items", kwargs={"parent_id":"work_091","child_id":"work_191","link_type":"relates_to"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1084,"changed_keys":["ui.main_menu.title"],"locales_processed":["ja"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Job queued: ui.main_menu.title [ja]",
      "message":"TMS job created for ui.main_menu.title",
      "recipient_id":"user_009",
      "channel":"slack"
    }),
  ],
  outputs=["tms_job created","translation recorded","work items linked","workflow created","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_085",
  instruction=(
    "You execute a CI-to-fix workflow for a Korean failure (build 'run_009', commit 'caf333'). "
    "Your required outcomes: a high-priority KO job with CI metadata (build_run_id 'run_009', commit_sha 'caf333') is created; "
    "the corrected KO string for 'ui.settings.video' ('비디오') is recorded (entry includes only string_key, locale, target_string); "
    "work_092→work_192 is linked with link_type='relates_to' and work_192 is tagged with label_001; a completed workflow for PR 1085 exists; "
    "and an update notification to user_010 confirms validation using title='Validations passed: ui.settings.video [ko]' and "
    "message='Validations passed for ko for ui.settings.video'. Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["ko"],"priority":"high",
      "metadata":{"build_run_id":"run_009","commit_sha":"caf333"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"ui.settings.video","locale":"ko","target_string":"비디오"}]
    }),
    Action(name="link_work_items", kwargs={"parent_id":"work_092","child_id":"work_192","link_type":"relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_192","label_name":"label_001"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1085,"changed_keys":["ui.settings.video"],"locales_processed":["ko"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"update",
      "title":"Validations passed: ui.settings.video [ko]",
      "message":"Validations passed for ko for ui.settings.video",
      "recipient_id":"user_010",
      "channel":"slack"
    }),
  ],
  outputs=["tms_job created","translation recorded","work items linked and tagged","workflow created","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_086",
  instruction=(
    "You complete the deprecation of legacy asset 'assets/ui/legacy_menu.json'. "
    "Ensure the system state reflects deprecation as follows (use tool-generated IDs/timestamps only): "
    "a relationship of type 'relates_to' exists from parent work_093 to child work_193; work_193 is tagged with label_004 ('Deprecation Candidate'); "
    "a medium-priority EN job exists with metadata.asset_path='assets/ui/legacy_menu.json'; "
    "a workflow for PR 1086 exists with status='deprecated' and changed_keys=['assets/ui/legacy_menu.json']; "
    "and an info Slack notification was sent to user_012 with title='Asset deprecated: assets/ui/legacy_menu.json' and "
    "message='Deprecation logged for assets/ui/legacy_menu.json (PR 1086), see work_193.'."
  ),
  actions=[
    Action(name="link_work_items", kwargs={"parent_id":"work_093","child_id":"work_193","link_type":"relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_193","label_id":"label_004"}),
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["en"],"priority":"medium",
      "metadata":{"asset_path":"assets/ui/legacy_menu.json"}
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1086,"changed_keys":["assets/ui/legacy_menu.json"],"locales_processed":[],
      "status":"deprecated"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Asset deprecated: assets/ui/legacy_menu.json",
      "message":"Deprecation logged for assets/ui/legacy_menu.json (PR 1086), see work_193.",
      "recipient_id":"user_012","channel":"slack"
    }),
  ],
  outputs=["work items linked","work item tagged","tms_job created","workflow created","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_087",
  instruction=(
    "You perform a tone/nuance update for Japanese based on commit 'ccc555'. "
    "Your required outcomes: create a medium-priority JA job with metadata {'commit_sha':'ccc555'}; "
    "record JA for 'ui.main_menu.quit_game' as 'ゲームを終了' (entries include only string_key, locale, target_string); "
    "create a completed workflow for PR 1087 with changed_keys=['ui.main_menu.quit_game']; and "
    "send an update Slack notification to user_013 with "
    "title='Translation applied: ui.main_menu.quit_game [ja]' and "
    "message='Translation applied for ui.main_menu.quit_game (ja)'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["ja"],"priority":"medium",
      "metadata":{"commit_sha":"ccc555"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"ui.main_menu.quit_game","locale":"ja","target_string":"ゲームを終了"}]
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1087,"changed_keys":["ui.main_menu.quit_game"],"locales_processed":["ja"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"update",
      "title":"Translation applied: ui.main_menu.quit_game [ja]",
      "message":"Translation applied for ui.main_menu.quit_game (ja)",
      "recipient_id":"user_013","channel":"slack"
    }),
  ],
  outputs=["tms_job created","translation updated","workflow created","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_088",
  instruction=(
    "You set up a new German localization job tied to CI build 'run_010'. "
    "Your required outcomes: create a medium-priority DE job with metadata {'build_run_id':'run_010'}; "
    "record a placeholder for 'ui.new_feature.confirm' as '[PLATZHALTER]' (entries include only string_key, locale, target_string); "
    "link work_094→work_194 with link_type='relates_to' and tag work_194 with label_001; "
    "create a completed workflow for PR 1088 with changed_keys=['ui.new_feature.confirm']; and "
    "send an info Slack notification to user_014 with "
    "title='Job queued: ui.new_feature.confirm [de]' and "
    "message='TMS job created for ui.new_feature.confirm'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["de"],"priority":"medium",
      "metadata":{"build_run_id":"run_010"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"ui.new_feature.confirm","locale":"de","target_string":"[PLATZHALTER]"}]
    }),
    Action(name="link_work_items", kwargs={"parent_id":"work_094","child_id":"work_194","link_type":"relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_194","label_id":"label_001"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1088,"changed_keys":["ui.new_feature.confirm"],"locales_processed":["de"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Job queued: ui.new_feature.confirm [de]",
      "message":"TMS job created for ui.new_feature.confirm",
      "recipient_id":"user_014","channel":"slack"
    }),
  ],
  outputs=["tms_job created","placeholder recorded","work items linked and tagged","workflow created","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_089",
  instruction=(
    "You run a batch ES localization for three settings strings. "
    "Your required outcomes: create one medium-priority ES job; "
    "record translations for 'ui.settings.video' ('Vídeo'), 'ui.settings.controls' ('Controles'), and 'ui.settings.gameplay' ('Jugabilidad') "
    "(entries include only string_key, locale, target_string); "
    "create a completed workflow for PR 1089 with changed_keys=['ui.settings.video','ui.settings.controls','ui.settings.gameplay']; and "
    "send an info Slack notification to user_015 with "
    "title='Translations applied: ui.settings.video, ui.settings.controls, ui.settings.gameplay [es]' and "
    "message='Translations applied for es for ui.settings.video, ui.settings.controls, ui.settings.gameplay'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={"source_locale":"en","target_locales":["es"],"priority":"medium"}),
    Action(name="record_translations", kwargs={
      "entries":[
        {"string_key":"ui.settings.video","locale":"es","target_string":"Vídeo"},
        {"string_key":"ui.settings.controls","locale":"es","target_string":"Controles"},
        {"string_key":"ui.settings.gameplay","locale":"es","target_string":"Jugabilidad"}
      ]
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1089,
      "changed_keys":["ui.settings.video","ui.settings.controls","ui.settings.gameplay"],
      "locales_processed":["es"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Translations applied: ui.settings.video, ui.settings.controls, ui.settings.gameplay [es]",
      "message":"Translations applied for es for ui.settings.video, ui.settings.controls, ui.settings.gameplay",
      "recipient_id":"user_015","channel":"slack"
    }),
  ],
  outputs=["tms_job created","3 translations recorded","workflow created","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_090",
  instruction=(
    "You process a new cinematic subtitle text for asset 'assets/cinematics/level2_outro.mp4'. "
    "Your required outcomes: create a medium-priority FR subtitle-text job with metadata {'asset_path':'assets/cinematics/level2_outro.mp4'}; "
    "record FR for 'vo.level2.outro_line1' as 'La bataille est gagnée.' (entries include only string_key, locale, target_string); "
    "link work_196→work_195 with link_type='relates_to'; and send an info Slack notification to user_001 with "
    "title='Text ready for timing: vo.level2.outro_line1 [fr]' and "
    "message='French text ready for timing for assets/cinematics/level2_outro.mp4 (vo.level2.outro_line1)'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["fr"],"priority":"medium",
      "metadata":{"asset_path":"assets/cinematics/level2_outro.mp4"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"vo.level2.outro_line1","locale":"fr","target_string":"La bataille est gagnée."}]
    }),
    Action(name="link_work_items", kwargs={"parent_id":"work_196","child_id":"work_195","link_type":"relates_to"}),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Text ready for timing: vo.level2.outro_line1 [fr]",
      "message":"French text ready for timing for assets/cinematics/level2_outro.mp4 (vo.level2.outro_line1)",
      "recipient_id":"user_001","channel":"slack"
    }),
  ],
  outputs=["tms_job created","translation recorded","work items linked","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_091",
  instruction=(
    "You roll out new tooltip translations for Save across Italian and Portuguese. "
    "Your required outcomes: create one medium-priority IT/PT job with metadata {'component':'ui','subcomponent':'tooltips'}; "
    "record 'ui.tooltip.save' as 'Salva' (it) and 'Salvar' (pt) (entries include only string_key, locale, target_string); "
    "link work_095→work_202 with link_type='relates_to' and tag work_202 with label_001; "
    "create a completed workflow for PR 1091 with changed_keys=['ui.tooltip.save']; and "
    "send an info Slack notification to user_012 with "
    "title='Translations applied: ui.tooltip.save [it,pt]' and "
    "message='Translations applied for it,pt for ui.tooltip.save'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["it","pt"],"priority":"medium",
      "metadata":{"component":"ui","subcomponent":"tooltips"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[
        {"string_key":"ui.tooltip.save","locale":"it","target_string":"Salva"},
        {"string_key":"ui.tooltip.save","locale":"pt","target_string":"Salvar"}
      ]
    }),
    Action(name="link_work_items", kwargs={"parent_id":"work_095","child_id":"work_202","link_type":"relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_202","label_id":"label_001"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1091,"changed_keys":["ui.tooltip.save"],"locales_processed":["it","pt"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Translations applied: ui.tooltip.save [it,pt]",
      "message":"Translations applied for it,pt for ui.tooltip.save",
      "recipient_id":"user_012","channel":"slack"
    }),
  ],
  outputs=["tms_job created","it/pt translations recorded","work items linked and tagged","workflow created","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_092",
  instruction=(
    "You start remediation for failed automation run 'automation_run_005' affecting German. "
    "Your required outcomes: create a high-priority DE job with metadata {'automation_run_id':'automation_run_005'}; "
    "link work_097→work_197 with link_type='relates_to'; open a workflow for PR 1092 with status 'in_progress' "
    "and changed_keys=[]; and send an info Slack notification to user_003 with "
    "title='Remediation started: automation_run_005 [de]' and "
    "message='Manual remediation for automation_run_005 has begun. See work_197.'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["de"],"priority":"high",
      "metadata":{"automation_run_id":"automation_run_005"}
    }),
    Action(name="link_work_items", kwargs={"parent_id":"work_097","child_id":"work_197","link_type":"relates_to"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1092,"changed_keys":[],"locales_processed":["de"],"status":"in_progress"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Remediation started: automation_run_005 [de]",
      "message":"Manual remediation for automation_run_005 has begun. See work_197.",
      "recipient_id":"user_003","channel":"slack"
    }),
  ],
  outputs=["tms_job created","work items linked","workflow created","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_093",
  instruction=(
    "You manage a dual-locale VO refresh for 'vo.generic.greeting'. "
    "Your required outcomes: create one medium-priority FR/ES job; record FR 'Bonjour.' and ES 'Hola.' "
    "(entries include only string_key, locale, target_string); create a completed workflow for PR 1093 with "
    "changed_keys=['vo.generic.greeting']; and send an info Slack notification to user_004 with "
    "title='VO refreshed: vo.generic.greeting [fr,es]' and "
    "message='VO refreshed for fr,es for vo.generic.greeting'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={"source_locale":"en","target_locales":["fr","es"],"priority":"medium"}),
    Action(name="record_translations", kwargs={
      "entries":[
        {"string_key":"vo.generic.greeting","locale":"fr","target_string":"Bonjour."},
        {"string_key":"vo.generic.greeting","locale":"es","target_string":"Hola."}
      ]
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1093,"changed_keys":["vo.generic.greeting"],"locales_processed":["fr","es"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"VO refreshed: vo.generic.greeting [fr,es]",
      "message":"VO refreshed for fr,es for vo.generic.greeting",
      "recipient_id":"user_004","channel":"slack"
    }),
  ],
  outputs=["tms_job created","FR/ES translations recorded","workflow created","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_094",
  instruction=(
    "You correct a Japanese placeholder string from commit 'ddd666'. "
    "Your required outcomes: create a medium-priority JA job with metadata {'commit_sha':'ddd666'}; "
    "record '{count} 発' for 'ui.hud.ammo_count' (entries include only string_key, locale, target_string); "
    "create a completed workflow for PR 1094 with changed_keys=['ui.hud.ammo_count']; and "
    "send an info Slack notification to user_005 with "
    "title='Placeholder corrected: ui.hud.ammo_count [ja]' and "
    "message='Placeholder corrected for ui.hud.ammo_count (ja)'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["ja"],"priority":"medium",
      "metadata":{"commit_sha":"ddd666"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"ui.hud.ammo_count","locale":"ja","target_string":"{count} 発"}]
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1094,"changed_keys":["ui.hud.ammo_count"],"locales_processed":["ja"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Placeholder corrected: ui.hud.ammo_count [ja]",
      "message":"Placeholder corrected for ui.hud.ammo_count (ja)",
      "recipient_id":"user_005","channel":"slack"
    }),
  ],
  outputs=["tms_job created","translation corrected","workflow created","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_095",
  instruction=(
    "You process archival of legacy KO string 'ui.legacy.button'. "
    "Your required outcomes: link work_098→work_198 with link_type='relates_to' and tag work_198 with label_004; "
    "create a medium-priority KO job; create a workflow for PR 1095 with status 'pending_deprecation' and "
    "changed_keys=['ui.legacy.button']; and send an info Slack notification to user_006 with "
    "title='String marked for archival: ui.legacy.button [ko]' and "
    "message='Korean string ui.legacy.button marked for archival; see work_198.'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="link_work_items", kwargs={"parent_id":"work_098","child_id":"work_198","link_type":"relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_198","label_id":"label_004"}),
    Action(name="create_tms_job", kwargs={"source_locale":"en","target_locales":["ko"],"priority":"medium"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1095,"changed_keys":["ui.legacy.button"],"locales_processed":["ko"],"status":"pending_deprecation"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"String marked for archival: ui.legacy.button [ko]",
      "message":"Korean string ui.legacy.button marked for archival; see work_198.",
      "recipient_id":"user_006","channel":"slack"
    }),
  ],
  outputs=["work items linked","work item tagged","tms_job created","workflow created","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_096",
  instruction=(
    "You deploy a critical Spanish EULA update tied to asset 'assets/legal/eula_es.txt'. "
    "Your required outcomes: create a high-priority ES job with metadata {'asset_path':'assets/legal/eula_es.txt'}; "
    "record 'Acuerdo de licencia de usuario final actualizado.' for 'text.legal.eula' (entries include only string_key, locale, target_string); "
    "create a completed workflow for PR 1096 with changed_keys=['text.legal.eula'] and metadata {'sensitivity':'high'}; and "
    "send an update Slack notification to user_007 with "
    "title='Localization completed: text.legal.eula [es]' and "
    "message='Localization completed for es for text.legal.eula'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["es"],"priority":"high",
      "metadata":{"asset_path":"assets/legal/eula_es.txt"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"text.legal.eula","locale":"es","target_string":"Acuerdo de licencia de usuario final actualizado."}]
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1096,"changed_keys":["text.legal.eula"],"locales_processed":["es"],
      "status":"completed","metadata":{"sensitivity":"high"}
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"update",
      "title":"Localization completed: text.legal.eula [es]",
      "message":"Localization completed for es for text.legal.eula",
      "recipient_id":"user_007","channel":"slack"
    }),
  ],
  outputs=["tms_job created","legal text recorded","localization workflow completed","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_097",
  instruction=(
    "You create DE subtitle text and document required timing for subtitle_011 (vo.level5.warning). "
    "Your required outcomes: create a medium-priority DE job with metadata {'component':'vo'}; "
    "record 'Achtung!' for 'vo.level5.warning' (entries include only string_key, locale, target_string); "
    "create a completed workflow for PR 1097 with changed_keys=['vo.level5.warning','subtitle_011'] and "
    "metadata {'required_timing':{'id':'subtitle_011','start':30.1,'end':31.5}}; and "
    "send an info Slack notification to user_008 with "
    "title='Workflow completed with timing: vo.level5.warning [de]' and "
    "message='Timing 30.1–31.5s captured for subtitle_011 (vo.level5.warning).'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["de"],"priority":"medium",
      "metadata":{"component":"vo"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"vo.level5.warning","locale":"de","target_string":"Achtung!"}]
    }),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1097,"changed_keys":["vo.level5.warning","subtitle_011"],"locales_processed":["de"],
      "status":"completed","metadata":{"required_timing":{"id":"subtitle_011","start":30.1,"end":31.5}}
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Workflow completed with timing: vo.level5.warning [de]",
      "message":"Timing 30.1–31.5s captured for subtitle_011 (vo.level5.warning).",
      "recipient_id":"user_008","channel":"slack"
    }),
  ],
  outputs=["tms_job created","translation recorded","localization workflow completed with timing metadata","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_098",
  instruction=(
    "You batch-update three French store item descriptions. "
    "Your required outcomes: create a medium-priority FR job; record FR strings "
    "for item.desc.sword ('Une épée tranchante.'), item.desc.shield ('Un bouclier robuste.'), and "
    "item.desc.potion ('Restaure la santé.') (entries include only string_key, locale, target_string); "
    "link work_099→work_199 with link_type='relates_to'; create a completed workflow for PR 1098 "
    "with changed_keys=['item.desc.sword','item.desc.shield','item.desc.potion']; and send an info Slack notification to user_009 with "
    "title='Translations applied: item.desc.sword,item.desc.shield,item.desc.potion [fr]' and "
    "message='Translations applied for fr for item.desc.sword,item.desc.shield,item.desc.potion'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={"source_locale":"en","target_locales":["fr"],"priority":"medium"}),
    Action(name="record_translations", kwargs={
      "entries":[
        {"string_key":"item.desc.sword","locale":"fr","target_string":"Une épée tranchante."},
        {"string_key":"item.desc.shield","locale":"fr","target_string":"Un bouclier robuste."},
        {"string_key":"item.desc.potion","locale":"fr","target_string":"Restaure la santé."}
      ]
    }),
    Action(name="link_work_items", kwargs={"parent_id":"work_099","child_id":"work_199","link_type":"relates_to"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1098,
      "changed_keys":["item.desc.sword","item.desc.shield","item.desc.potion"],
      "locales_processed":["fr"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Translations applied: item.desc.sword,item.desc.shield,item.desc.potion [fr]",
      "message":"Translations applied for fr for item.desc.sword,item.desc.shield,item.desc.potion",
      "recipient_id":"user_009","channel":"slack"
    }),
  ],
  outputs=["tms_job created","3 translations recorded","work_099→work_199 linked","localization workflow completed","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_099",
  instruction=(
    "You improve clarity of Chinese error message 'error.connection.failed'. "
    "Your required outcomes: create a medium-priority ZH job; record '连接失败，请检查您的网络。' "
    "for 'error.connection.failed' (entries include only string_key, locale, target_string); "
    "tag work_201 with label_001; create a completed workflow for PR 1099 with changed_keys=['error.connection.failed']; and "
    "send an info Slack notification to user_010 with "
    "title='Localization completed: error.connection.failed [zh]' and "
    "message='Localization completed for zh for error.connection.failed'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={"source_locale":"en","target_locales":["zh"],"priority":"medium"}),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"error.connection.failed","locale":"zh","target_string":"连接失败，请检查您的网络。"}]
    }),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_201","label_id":"label_001"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1099,"changed_keys":["error.connection.failed"],"locales_processed":["zh"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Localization completed: error.connection.failed [zh]",
      "message":"Localization completed for zh for error.connection.failed",
      "recipient_id":"user_010","channel":"slack"
    }),
  ],
  outputs=["tms_job created","translation recorded","work_201 tagged","localization workflow completed","notification sent"]
),

Task(
  annotator="dev_ops",
  user_id="V6_100",
  instruction=(
    "You execute a release-candidate localization workflow: CI build 'run_011' and commit 'eee777' require a JA fix for "
    "'ui.common.loading' ('ロード中...'). Your required outcomes: create a high-priority JA/ES/DE job with metadata "
    "{'commit_sha':'eee777','build_run_id':'run_011'}; record the JA fix for 'ui.common.loading' ('ロード中...') "
    "(entry includes only string_key, locale, target_string); link work_100→work_200 with link_type='relates_to' and tag work_200 with label_001; "
    "create a completed workflow for PR 1100 with changed_keys=['ui.common.loading']; and send an info Slack notification to user_011 with "
    "title='Localization completed: ui.common.loading [ja,es,de]' and "
    "message='Localization completed for ja,es,de for ui.common.loading'. "
    "Use tool-generated IDs/timestamps only."
  ),
  actions=[
    Action(name="create_tms_job", kwargs={
      "source_locale":"en","target_locales":["ja","es","de"],"priority":"high",
      "metadata":{"commit_sha":"eee777","build_run_id":"run_011"}
    }),
    Action(name="record_translations", kwargs={
      "entries":[{"string_key":"ui.common.loading","locale":"ja","target_string":"ロード中..."}]
    }),
    Action(name="link_work_items", kwargs={"parent_id":"work_100","child_id":"work_200","link_type":"relates_to"}),
    Action(name="tag_work_item_with_label", kwargs={"work_item_id":"work_200","label_id":"label_001"}),
    Action(name="create_localization_workflow", kwargs={
      "pr_number":1100,"changed_keys":["ui.common.loading"],"locales_processed":["ja","es","de"],"status":"completed"
    }),
    Action(name="send_notification", kwargs={
      "notification_type":"info",
      "title":"Localization completed: ui.common.loading [ja,es,de]",
      "message":"Localization completed for ja,es,de for ui.common.loading",
      "recipient_id":"user_011","channel":"slack"
    }),
  ],
  outputs=["tms_job created","JA translation recorded","work_100→work_200 linked and tagged","localization workflow completed","notification sent"]
)

]