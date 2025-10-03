# Copyright Sierra

tasks = [
    {
        "annotator": dev_ops,
        "user_id": "V6_001",
        "instruction": "Handle the localization of the pause-menu 'Start Game' string using only the existing CI metadata (commit 'def789ghi012345', build run 'run_002', test 'test_result_045'). The task is to deliver a high-priority localization update specifically for 'ui.main_menu.start_game' in the locales ['es','it'], with translations as ('Comenzar' for es, 'Avvia' for it), ensuring locale validations are passed, updating the localization workflow for PR 1601, correct tagging and relationship on the corresponding work items (work_055 \u2192 work_140, relates_to; label_002 on work_140), and ensuring notifications indicate that the task was queued and validations were successful. Utilize tool-generated IDs/timestamps and adhere to domain rules for deterministic parameters; refrain from creating custom IDs or names, and omit the 'id' field in translation entries (each entry should contain only: string_key, locale, target_string). Use tool outputs to determine the operational sequence to fulfill these success criteria.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "job_type": "translation",
                    "source_locale": "en",
                    "target_locales": [
                        "es",
                        "it"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "pause_menu",
                        "commit_sha": "def789ghi012345",
                        "build_run_id": "run_002",
                        "test_result_id": "test_result_045"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "es",
                            "target_string": "Comenzar"
                        },
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "it",
                            "target_string": "Avvia"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "es",
                    "validation_status": "passed"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "it",
                    "validation_status": "passed"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_055",
                    "child_id": "work_140",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_140",
                    "label_id": "label_002"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1601,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "es",
                        "it"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "pause_menu",
                        "commit_sha": "def789ghi012345",
                        "build_run_id": "run_002",
                        "test_result_id": "test_result_045"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.main_menu.start_game [es,it]",
                    "message": "TMS job created for ui.main_menu.start_game",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.main_menu.start_game [es,it]",
                    "message": "Validations passed for es,it for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "es/it translations recorded",
                "es passed",
                "it passed",
                "work_055→work_140 linked",
                "label_002 applied",
                "localization workflow completed",
                "notifications sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_002",
        "instruction": "Coordinate a deterministic German localization update for 'ui.settings.audio' utilizing only necessary read-only context checks. The criteria for success include: a high-priority localization task for the update, recording the 'de' translation as 'Audio', ensuring validation for 'de' is successful, completing the localization workflow for PR 1602 that includes this key and locale, providing a deterministic notification that the task was queued and validations were successful, and refraining from providing custom IDs/timestamps. Translation entries are to include only: string_key, locale, target_string. Depend on tool defaults and follow domain rules for all IDs, timestamps, and naming conventions.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "job_type": "translation",
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "de",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1602,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.settings.audio [de]",
                    "message": "TMS job created for ui.settings.audio",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [de]",
                    "message": "Validations passed for de for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context captured (de)",
                "tms_job created",
                "de translation recorded",
                "de passed",
                "localization workflow completed",
                "notifications sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_003",
        "instruction": "Handle the documentation and response to a German overflow on 'ui.main_menu.start_game' using existing records for context. The criteria for success include: locale 'de' marked failed with validation_error 'Text exceeds 200px width'; a high-priority localization job for this issue; a finished localization workflow for PR 1010 reflecting this key and locale with overflow_issues=1; and a deterministic notification showing the validation failure. Do not provide any custom IDs or timestamps. Translation entries are not needed for this task.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de",
                    "validation_status": "failed",
                    "validation_error": "Text exceeds 200px width"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations failed: ui.main_menu.start_game [de]",
                    "message": "Text exceeds 200px width",
                    "channel": "slack"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1010,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "overflow_issues": 1,
                    "status": "completed"
                }
            }
        ],
        "outputs": [
                "de validation failed with overflow",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_004",
        "instruction": "Coordinate the remediation of the Spanish main menu localization issue found in CI (build run 'run_003', commit 'abc123def456789') for string_key 'ui.main_menu.start_game'. The criteria for success are: a high-priority localization job within that CI context; the Spanish translation recorded as 'Iniciar'; validations in a passed state for 'es'; a completed localization workflow for PR 1006; and clear notifications indicating the job was queued and validations were successful. Depend on tool-generated IDs/timestamps and domain rules for deterministic parameters. Do not provide custom IDs or timestamps. When documenting translations, each entry must include only: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_003"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "job_type": "translation",
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu",
                        "build_run_id": "run_003",
                        "commit_sha": "abc123def456789"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "es",
                            "target_string": "Iniciar"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "es",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1006,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu",
                        "build_run_id": "run_003",
                        "commit_sha": "abc123def456789"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.main_menu.start_game [es]",
                    "message": "TMS job created for ui.main_menu.start_game",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.main_menu.start_game [es]",
                    "message": "Validations passed for es for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "CI context captured",
                "tms_job created",
                "es translation recorded",
                "es passed",
                "localization workflow completed",
                "notifications sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_005",
        "instruction": "Handle the application of the Japanese audio update for 'ui.settings.audio' using CI traceability associated with build run 'run_001' and commit 'abc123def456789'. Your success criteria must include: capturing a medium-priority localization job with that CI context; recording the Japanese translation as '\u30aa\u30fc\u30c7\u30a3\u30aa'; confirming the 'ja' validation in a passed state; linking work_045 \u2192 work_120 (relates_to) and ensuring 'localization' is labeled on work_120; finalizing the localization workflow for PR 5005; and issuing clear notifications for both the queuing of the job and successful validations. Depend on tool-generated IDs/timestamps and domain rules without creating custom IDs or timestamps. Translation entries must solely consist of: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings",
                        "build_run_id": "run_001",
                        "commit_sha": "abc123def456789"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "ja",
                            "target_string": "オーディオ"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "ja",
                    "validation_status": "passed"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_120",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_120",
                    "label_name": "localization"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 5005,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "ja"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings",
                        "build_run_id": "run_001",
                        "commit_sha": "abc123def456789"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.settings.audio [ja]",
                    "message": "TMS job created for ui.settings.audio",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [ja]",
                    "message": "Validations passed for ja for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (run_001)",
                "tms_job created",
                "ja translation recorded",
                "ja passed",
                "work_045→work_120 linked",
                "work_120 tagged",
                "localization workflow completed",
                "notifications sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_006",
        "instruction": "Coordinate the deterministic German rollout for 'ui.settings.audio' with complete traceability. Your success metrics should involve: a medium-priority localization job targeted at this key; the recording of the 'de' translation as 'Audio'; ensuring 'de' validation is passed; completing the localization workflow for PR 1008; establishing a relates_to link work_045 \u2192 work_130; and providing clear notifications that the job was queued and validations succeeded. Use tool-generated IDs/timestamps and domain rules for deterministic parameters without creating custom IDs or timestamps. When saving translations, each entry must include solely: string_key, locale, target_string.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "job_type": "translation",
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "ui"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "de",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de",
                    "validation_status": "passed"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_130",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1008,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.settings.audio [de]",
                    "message": "TMS job created for ui.settings.audio",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [de]",
                    "message": "Validations passed for de for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "de translation recorded",
                "de passed",
                "work_045→work_130 linked",
                "localization workflow completed",
                "notifications sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_007",
        "instruction": "Handle the finalization of the German validation state for 'ui.main_menu.start_game' with CI context utilizing build run 'run_003' and commit 'abc123def456789'. The criteria for completion are: validation for locale 'de' in a passed state; a medium-priority localization job associated with this CI context; finalization of the localization workflow for PR 1009; application of a 'localization' label to work_130; and clear notifications indicating the job was queued and that validations were successful. Depend on tool-generated IDs/timestamps and domain rules; refrain from providing custom IDs or timestamps. Translation entries are not necessary for this task.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_003"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "job_type": "translation",
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "build_run_id": "run_003",
                        "commit_sha": "abc123def456789"
                    }
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1009,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "build_run_id": "run_003",
                        "commit_sha": "abc123def456789"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.main_menu.start_game [de]",
                    "message": "TMS job created for ui.main_menu.start_game",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.main_menu.start_game [de]",
                    "message": "Validations passed for de for ui.main_menu.start_game",
                    "channel": "slack"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_130",
                    "label_name": "localization"
                }
            }
        ],
        "outputs": [
                "context consulted (run_003, de string read)",
                "de passed",
                "tms_job created",
                "localization workflow completed",
                "notification sent",
                "label applied"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_008",
        "instruction": "Coordinate documentation of a German overflow for 'ui.main_menu.start_game' and compile a remediation plan. Successful completion is defined by: locale 'de' marked as failed with validation_error 'Text exceeds 200px width'; logging a high-priority localization job (including reviewer context for user_006 if applicable); the candidate German translation 'Starten' documented; conclusion of the localization workflow for PR 1010 with overflow_issues=1; and an update notification detailing the failure. Depend on tool-generated IDs/timestamps and domain rules; avoid providing custom IDs or timestamps. Ensure each translation entry includes only: string_key, locale, target_string.",
        "actions": [
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de",
                    "validation_status": "failed",
                    "validation_error": "Text exceeds 200px width"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "job_type": "translation",
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "high",
                    "assigned_reviewers": [
                        "user_006"
                    ]
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "de",
                            "target_string": "Starten"
                        }
                    ]
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1010,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "overflow_issues": 1,
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validation failed: ui.main_menu.start_game [de]",
                    "message": "Text exceeds 200px width for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "de validation failed (overflow)",
                "tms_job created",
                "de translation recorded",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_009",
        "instruction": "Handle an ES audio rollout for 'ui.settings.audio' utilizing explicit templates and audit context. Your success criteria are: verifying the current ES value for 'ui.settings.audio' is consulted (read-only); establishing a medium-priority ES TMS job with metadata {'component':'ui','subcomponent':'settings'}; ensuring one Spanish translation is documented as 'Audio' (each entry must include only string_key, locale, target_string); setting validation for 'es' to 'passed'; verifying a completed localization workflow for PR 1011 referencing changed_keys=['ui.settings.audio'], locales_processed=['es'], and the same UI/Settings metadata; and dispatching two Slack notifications using deterministic templates: (info) title='Job queued: ui.settings.audio [es]' / message='TMS job created for ui.settings.audio' and (update) title='Validations passed: ui.settings.audio [es]' / message='Validations passed for es for ui.settings.audio'. Use only tool-generated IDs/timestamps.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "es",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1011,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.settings.audio [es]",
                    "message": "TMS job created for ui.settings.audio",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [es]",
                    "message": "Validations passed for es for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (es)",
                "tms_job created",
                "es translation recorded",
                "es validation passed",
                "localization workflow completed",
                "notifications sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_010",
        "instruction": "Coordinate a deterministic German update for 'ui.settings.audio' with traceability and lightweight coordination. Your success criteria include: setting up a medium-priority localization job; recording one German translation as 'Audio'; ensuring validation for 'de' is in a passed state; completing a localization workflow for PR 1012; sending two notifications (job queued and validations passed); establishing a relates_to link work_045 \u2192 work_130; and applying the 'localization' label to work_130. Depend on tool-generated IDs/timestamps and domain rules; refrain from providing custom IDs or timestamps. Each translation entry must only contain: string_key, locale, target_string.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "medium"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "de",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1012,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.settings.audio [de]",
                    "message": "TMS job created for ui.settings.audio",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [de]",
                    "message": "Validations passed for de for ui.settings.audio",
                    "channel": "slack"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_130",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_130",
                    "label_name": "localization"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "de translation recorded",
                "de passed",
                "localization workflow completed",
                "notifications sent",
                "work_045→work_130 linked",
                "work_130 tagged"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_011",
        "instruction": "Handle the completion of the Japanese main-menu start label as per localization policy. Your criteria for successful completion include: work_130 being marked with the 'localization' label; a high-priority localization task for 'ja' concerning the main menu; ensuring that the Japanese translation '\u30b2\u30fc\u30e0\u958b\u59cb' is documented for 'ui.main_menu.start_game'; validation successfully passing for 'ja'; the localization workflow for PR 1015 being finalized; and an informational notification outlining the update. Depend on tool-generated IDs/timestamps and domain regulations; refrain from creating any custom IDs or timestamps. Each translation record must consist of just: string_key, locale, target_string.",
        "actions": [
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_130",
                    "label_name": "localization"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja"
                    ],
                    "priority": "high"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "ja",
                            "target_string": "ゲーム開始"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "ja",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1015,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "ja"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Validations passed: ui.main_menu.start_game [ja]",
                    "message": "Validations passed for ja for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "label applied",
                "tms_job created",
                "ja translation recorded",
                "ja validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_012",
        "instruction": "Coordinate the recording of a deterministic ES audio update. Your criteria for success include: work_130 being tagged with the 'localization' label; a high-priority localization task for 'es' related to settings; confirming the Spanish translation 'Audio' for 'ui.settings.audio'; validation passing for 'es'; completing the localization workflow for PR 1014; and a summary notification outlining the modification. Rely solely on tool-generated IDs/timestamps; do not create custom IDs or timestamps. Each translation record should include solely: string_key, locale, target_string.",
        "actions": [
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_130",
                    "label_name": "localization"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "high"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "es",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1014,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [es]",
                    "message": "Validations passed for es for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "label applied",
                "tms_job created",
                "es translation recorded",
                "es validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_013",
        "instruction": "Handle a Japanese main-menu remediation task. Your success criteria involve: verifying (read-only) the current entry for 'ui.main_menu.start_game' in 'ja'; executing a high-priority localization task for 'ja' on the main menu; ensuring the Japanese translation '\u30b2\u30fc\u30e0\u958b\u59cb' is noted; validation status confirmed as passed; achieving a finished localization workflow for PR 1015; and an informational notification signaling readiness. Utilize tool-generated IDs/timestamps exclusively. Each translation entry is required to include: string_key, locale, target_string only.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "ja"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja"
                    ],
                    "priority": "high"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "ja",
                            "target_string": "ゲーム開始"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "ja",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1015,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "ja"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.main_menu.start_game [ja]",
                    "message": "Validations passed for ja for ui.main_menu.start_game",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Ready for release: ui.main_menu.start_game [ja]",
                    "message": "Localization for ja for ui.main_menu.start_game is ready.",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (ja)",
                "tms_job created",
                "ja translation recorded",
                "ja validation passed",
                "localization workflow completed",
                "validation update notification sent",
                "readiness info notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_014",
        "instruction": "Coordinate a deterministic recording of an ES settings batch with context and validation. Your success criteria include: reviewing (read-only) the current ES text for 'ui.settings.audio'; conducting a high-priority localization operation for 'es' on settings; ensuring the Spanish translation 'Audio' is noted for 'ui.settings.audio'; setting validation status to passed (excluding error field); finalizing a localization workflow for PR 1016; and generating an update notification that summarizes the recording. Use solely tool-generated IDs/timestamps. Translation entries must include only: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "high"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "es",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1016,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [es]",
                    "message": "Validations passed for es for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context captured",
                "tms_job created",
                "es translation recorded",
                "es validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_015",
        "instruction": "Handle a JA VO timing remediation with CI traceability. Success criteria include: capturing CI context by consulting build run 'run_003' and commit 'abc123def456789'; consulting the current JA settings-audio entry in a read-only manner; a recorded high-priority localization job for 'ja' on settings with CI metadata (build run and commit); completion of a localization workflow for PR 1017 with identical CI metadata and overflow_issues=0; establishing a relates_to link from work_045 to work_140; and issuing an info notification with title='Timing updated: ui.settings.audio [ja]' and message='Timing updated for ja for ui.settings.audio'. Utilize tool-generated IDs/timestamps solely.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_003"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "ja"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja"
                    ],
                    "priority": "high",
                    "metadata": {
                        "build_run_id": "run_003",
                        "commit_sha": "abc123def456789",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1017,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "ja"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "build_run_id": "run_003",
                        "commit_sha": "abc123def456789",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_140",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Timing updated: ui.settings.audio [ja]",
                    "message": "Timing updated for ja for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "CI context consulted (run_003, abc123def456789)",
                "baseline ja value consulted",
                "tms_job created",
                "localization workflow completed",
                "work_045→work_140 linked",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": loc_integration,
        "user_id": "V6_016",
        "instruction": "Coordinate a DE review by using repository context to persist deterministic records. Criteria for success are: consulting CI context (build run 'run_001', commit 'abc123def456789', test_result 'test_result_001', ownership for 'src/game/engine/renderer.cpp') and reading the existing DE localization for 'ui.main_menu.start_game'; recording a high-priority DE job for the main menu with CI/ownership metadata; setting validation to passed for 'de'; recording the translation 'Starten' for 'ui.main_menu.start_game'; completing a localization workflow for PR 1016 carrying identical CI metadata; and broadcasting an info notification for the build-triggered review. Use tool-generated IDs/timestamps exclusively. Every translation entry must include only: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "getSourceChange",
                "arguments": {
                    "commit_sha": "abc123def456789"
                },
            },
            {
                "name": "getTestResult",
                "arguments": {
                    "id": "test_result_001"
                },
            },
            {
                "name": "getOwnershipForPath",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu",
                        "commit_sha": "abc123def456789",
                        "build_run_id": "run_001",
                        "test_result_id": "test_result_001",
                        "owner_id": "user_001",
                        "file_path": "src/game/engine/renderer.cpp"
                    }
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de",
                    "validation_status": "passed"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "de",
                            "target_string": "Starten"
                        }
                    ]
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.main_menu.start_game [de]",
                    "message": "TMS job created for ui.main_menu.start_game",
                    "channel": "slack"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1016,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "commit_sha": "abc123def456789",
                        "build_run_id": "run_001",
                        "test_result_id": "test_result_001",
                        "owner_id": "user_001",
                        "file_path": "src/game/engine/renderer.cpp"
                    }
                }
            }
        ],
        "outputs": [
                "context consulted (build, commit, test, ownership, de string)",
                "tms_job created",
                "de validation passed",
                "de translation recorded",
                "notification sent",
                "localization workflow completed"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_017",
        "instruction": "You need to handle a Japanese refresh for settings audio involving context and traceability. Your success criteria are that the current JA value for 'ui.settings.audio' is consulted (read-only); the translation '\u30aa\u30fc\u30c7\u30a3\u30aa' is recorded; validation is set to passed; a high-priority JA job for settings is documented; a relates_to link from work_045 to work_150 is created and the 'localization' label is applied to work_150; the localization workflow for PR 1018 is completed; and you receive an info notification that the job was queued. Ensure only tool-generated IDs/timestamps are used. Each translation entry must include only: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "ja"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "ja",
                            "target_string": "オーディオ"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "ja",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja"
                    ],
                    "priority": "high"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_150",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_150",
                    "label_name": "localization"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1018,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "ja"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.settings.audio [ja]",
                    "message": "TMS job created for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context captured (ja)",
                "ja translation recorded",
                "ja validation passed",
                "tms_job created",
                "work_045→work_150 linked",
                "label applied",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_018",
        "instruction": "Coordinate a deterministic ES audio application that incorporates context and validation. Your success criteria include consulting the current ES text for 'ui.settings.audio'; a medium-priority ES job for settings being documented; tagging work_140 with the existing 'localization' label; ensuring validation is set to passed (no error field); recording the translation 'Audio'; completing the localization workflow for PR 1019; and receiving an update notification. Make use of tool-generated IDs/timestamps only. Each translation entry must include only: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "medium"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_140",
                    "label_name": "localization"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es",
                    "validation_status": "passed"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "es",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1019,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [es]",
                    "message": "Validations passed for es for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted",
                "tms_job created",
                "label applied",
                "es validation passed",
                "es translation recorded",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_019",
        "instruction": "Handle a deterministic ES audio rollout while considering CI context and establishing epic linkage. Success criteria include: consultation of CI (build run 'run_001' and commit 'abc123def456789') and review of the current ES text; recording a medium-priority ES job for settings with CI metadata (build run and commit); documenting one translation for 'ui.settings.audio' ('Audio'); validation marked as passed; linking work_045 to work_150 with a 'localization' label on work_150; completing the localization workflow for PR 1020 using the same CI metadata; and ensuring two notifications demonstrate job queued and job completed. Strictly use tool-generated IDs and timestamps. Every translation entry must exclusively comprise: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "commit_sha": "abc123def456789",
                        "build_run_id": "run_001"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "es",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es",
                    "validation_status": "passed"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_150",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_150",
                    "label_name": "localization"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1020,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed",
                    "metadata": {
                        "commit_sha": "abc123def456789",
                        "build_run_id": "run_001"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.settings.audio [es]",
                    "message": "TMS job created for ui.settings.audio",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Job completed: ui.settings.audio [es]",
                    "message": "Job completed for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (run_001, abc123def456789, es read)",
                "tms_job created",
                "es translation recorded",
                "es validation passed",
                "work_045→work_150 linked",
                "work_150 tagged",
                "localization workflow completed",
                "notifications sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_020",
        "instruction": "Coordinate finalization of a deterministic ES validation and workflow. Success criteria necessitate: passing validation for 'ui.settings.audio' in 'es'; documenting a medium-priority ES job for settings; completing the localization workflow for PR 1021; and issuing an info notification to verify ES validation. Strictly employ tool-generated IDs and timestamps.",
        "actions": [
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "medium"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1021,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Validations passed: ui.settings.audio [es]",
                    "message": "Validations passed for es for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "es validation passed",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_021",
        "instruction": "Handle the finalization of the Italian main-menu start label in a deterministic manner. Success criteria include: consulting the current IT text for 'ui.main_menu.start_game'; recording the translation 'Avvia'; setting the validation for 'it' to passed; recording a medium-priority IT job for the main menu; completing a localization workflow for PR 1022; and receiving an info notification confirming the update. Only utilize tool-generated IDs/timestamps. Each translation entry must solely consist of: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "it"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "it",
                            "target_string": "Avvia"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "it",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "it"
                    ],
                    "priority": "medium"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1022,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "it"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Validations passed: ui.main_menu.start_game [it]",
                    "message": "Validations passed for it for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "it string consulted",
                "it translation recorded",
                "it validation passed",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_022",
        "instruction": "Coordinate the shipment of a deterministic DE settings-audio update. Success criteria encompass: documenting the translation 'Audio' for 'ui.settings.audio'; setting the validation for 'de' to passed; documenting a medium-priority DE job for settings; completing a localization workflow for PR 1023; and receiving an update notification confirming the change. Restrict to using tool-generated IDs/timestamps. Each translation entry should include only: string_key, locale, target_string.",
        "actions": [
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "de",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "medium"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1023,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [de]",
                    "message": "Validations passed for de for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "de translation recorded",
                "de validation passed",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_023",
        "instruction": "Handle the documentation of a Spanish overflow for the main-menu start label and ensure remediation is captured. Your success criteria include: validation for 'ui.main_menu.start_game' in 'es' is marked failed with the error 'Text exceeds 200px width'; a high-priority ES job for the main menu is logged; the candidate translation 'Iniciar' is recorded; a completed localization workflow for PR 1024 that includes one overflow issue; and an updated Slack notification is sent using the exact strings title='Validations failed: ui.main_menu.start_game [es]' and message='Text exceeds 200px width for ui.main_menu.start_game'. Use only tool-generated IDs/timestamps. Each translation entry must consist of only: string_key, locale, target_string.",
        "actions": [
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "es",
                    "validation_status": "failed",
                    "validation_error": "Text exceeds 200px width"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "high"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "es",
                            "target_string": "Iniciar"
                        }
                    ]
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1024,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed",
                    "overflow_issues": 1
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations failed: ui.main_menu.start_game [es]",
                    "message": "Text exceeds 200px width for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "es validation failed (overflow)",
                "tms_job created",
                "es translation recorded",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_024",
        "instruction": "Coordinate the finalization of a deterministic JA validation for settings audio, including workflow and notice. Your success criteria are as follows: validation for 'ui.settings.audio' in 'ja' is set to passed; a medium-priority JA job for settings is noted; a completed localization workflow for PR 1025; and an informative notification confirms JA validation. Use only tool-generated IDs/timestamps.",
        "actions": [
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "ja",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja"
                    ],
                    "priority": "medium"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1025,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "ja"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Validations passed: ui.settings.audio [ja]",
                    "message": "Validations passed for ja for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "ja validation passed",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_025",
        "instruction": "Handle the application of a deterministic ES/IT settings-audio rollout. Your success criteria include: the translations captured ('Audio' for 'es' and 'it') for 'ui.settings.audio'; ensuring validations for 'es' and 'it' are set to passed; recording a high-priority job targeting both locales; completing a localization workflow for PR 1026; establishing a relates_to link from work_045 to work_160 and applying the 'localization' label to work_160; and receiving notifications acknowledging the rollout. Rely on tool-generated IDs/timestamps only. Each translation entry must only contain: string_key, locale, target_string.",
        "actions": [
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "es",
                            "target_string": "Audio"
                        },
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "it",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es",
                    "validation_status": "passed"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "it",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es",
                        "it"
                    ],
                    "priority": "high"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1026,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es",
                        "it"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_160",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_160",
                    "label_name": "localization"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.settings.audio [es,it]",
                    "message": "TMS job created for ui.settings.audio",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [es,it]",
                    "message": "Validations passed for es,it for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "es/it translations recorded",
                "es passed",
                "it passed",
                "tms_job created",
                "localization workflow completed",
                "work_045→work_160 linked",
                "work_160 tagged",
                "notifications sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_026",
        "instruction": "Coordinate the persistence of an ES settings workflow with epic linkage and basic TMS context. Achieve success by consulting the current ES value for 'ui.settings.audio'; creating a relates_to link from work_045 to work_150; recording a medium-priority ES job for settings with UI metadata; completing the workflow for PR 1027; and generating an update notification confirming the linkage. Utilize tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_150",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1027,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Linkage confirmed: work_045→work_150",
                    "message": "Relates_to linkage established between work_045 and work_150.",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (es)",
                "work_045→work_150 linked",
                "tms_job created",
                "es validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_027",
        "instruction": "Manage a CI-aware FR main-menu deployment with labeling. Success criteria: reference build run 'run_001' and consult commit 'abc123def456789'; document the translation 'Commencer' for 'ui.main_menu.start_game' in 'fr'; ensure validation is marked as passed; tag work_120 and work_140 with \"localization\"; record a medium-priority FR job with CI metadata; complete a workflow for PR 1028; and issue an info notification. Use only tool-generated IDs/timestamps. Each translation entry must solely contain: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "fr",
                            "target_string": "Commencer"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "fr",
                    "validation_status": "passed"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_120",
                    "label_name": "localization"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_140",
                    "label_name": "localization"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "commit_sha": "abc123def456789",
                        "build_run_id": "run_001"
                    }
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1028,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "fr"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.main_menu.start_game [fr]",
                    "message": "TMS job created for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (run_001, abc123def456789)",
                "fr translation recorded",
                "fr validation passed",
                "work_120 tagged",
                "work_140 tagged",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_028",
        "instruction": "Maintain a ZH validation result and audit records within TMS context. Success criteria: reference the current ZH main-menu text; ensure validation is marked as passed; document a medium-priority ZH job with UI metadata; complete a workflow for PR 1029; and send an info notification confirming ZH validation. Utilize tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "zh"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "zh",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "zh"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "ui"
                    }
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1029,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "zh"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Validations passed: ui.main_menu.start_game [zh]",
                    "message": "Validations passed for zh for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (zh)",
                "zh validation passed",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_029",
        "instruction": "Initiate a deterministic ZH settings-audio update across systems. The success criteria are: a high-priority ZH job for settings must be logged; the translation '\u97f3\u9891' for 'ui.settings.audio' must be documented; validation should be confirmed as passed; the workflow for PR 1030 must be completed; and an update notification must be issued. Utilize tool-generated IDs/timestamps exclusively. Ensure each translation entry comprises just: string_key, locale, target_string.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "zh"
                    ],
                    "priority": "high"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "zh",
                            "target_string": "音频"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "zh",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1030,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "zh"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [zh]",
                    "message": "Validations passed for zh for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "zh translation recorded",
                "zh validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_030",
        "instruction": "Log a deterministic DE overflow resolution concerning the main-menu start label. Success criteria require: validation for 'ui.main_menu.start_game' in 'de' is marked as passed; the workflow for PR 1031 is completed; and an update notification confirming resolution is issued. Employ tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1031,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.main_menu.start_game [de]",
                    "message": "Validations passed for de for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "de validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_031",
        "instruction": "Handle the process of ensuring the system displays an ES audio validation with traceable linkage and job context. Success criteria: consult the current ES entry for 'ui.settings.audio'; ensure a medium-priority ES job for settings is recorded; document the translation 'Audio'; establish a relates_to link from work_045 to work_140; set validation to passed; complete the workflow for PR 1032; and send an info notification confirming validation. Use only tool-generated IDs/timestamps. Each translation entry must consist solely of: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "ui"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "es",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_140",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1032,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Validations passed: ui.settings.audio [es]",
                    "message": "Validations passed for es for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (es)",
                "tms_job created",
                "es translation recorded",
                "work_045→work_140 linked",
                "es validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_032",
        "instruction": "Coordinate the documentation of a DE overflow discovery and remediation with full traceability. Success criteria: consult the current DE value for 'ui.main_menu.start_game'; record the validation as failed with error 'Text exceeds 200px width'; capture a high-priority DE job for the main menu with UI/Main Menu metadata; send an update notification referencing the overflow; document the translation 'Starten'; set follow-up validation to passed; and complete the workflow for PR 1022. Utilize tool-generated IDs/timestamps exclusively. Each translation entry must consist solely of: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de",
                    "validation_status": "failed",
                    "validation_error": "Text exceeds 200px width"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations failed: ui.main_menu.start_game [de]",
                    "message": "Text exceeds 200px width",
                    "channel": "slack"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "de",
                            "target_string": "Starten"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1022,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                }
            }
        ],
        "outputs": [
                "context consulted (de)",
                "de failed",
                "tms_job created",
                "notification sent",
                "de translation recorded",
                "de passed",
                "localization workflow completed"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_033",
        "instruction": "Handle the capture of a deterministic FR settings-audio tone update. The criteria for success include: consulting the FR entry for 'ui.settings.audio'; initiating a high-priority FR job for settings with UI metadata; ensuring the translation 'Audio' is documented for FR; validating as passed; finalizing a workflow for PR 1023; and issuing an info notification. Ensure usage of tool-generated IDs/timestamps exclusively. Translation entries must consist solely of: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "fr"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "fr",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "fr",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1023,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "fr"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.settings.audio [fr]",
                    "message": "TMS job created for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (fr)",
                "tms_job created",
                "fr translation recorded",
                "fr validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_034",
        "instruction": "Coordinate the persistence of a linkage, label, and JA settings update. The criteria for your success are: establishing a relates_to link from work_045 to work_150; tagging work_150 with 'localization'; documenting a high-priority JA job for UI/Settings; recording the translation '\u30aa\u30fc\u30c7\u30a3\u30aa' for 'ui.settings.audio'; completing a workflow for PR 1024 reflecting 'ui.settings.audio' for the locale 'ja'; and providing an info notification that the job was queued. Utilize tool-generated IDs/timestamps exclusively. Translation entries must contain solely: string_key, locale, target_string.",
        "actions": [
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_150",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_150",
                    "label_name": "localization"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "ja",
                            "target_string": "オーディオ"
                        }
                    ]
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1024,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "ja"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.settings.audio [ja]",
                    "message": "TMS job created for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "work_045→work_150 linked",
                "work_150 tagged",
                "tms_job created",
                "ja translation recorded",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_035",
        "instruction": "Handle VO subtitle retiming ensuring CI/TMS traceability is maintained. The criteria for success include: consulting build run 'run_001'; adjusting subtitle_001 to begin at 0.10s and finish at 2.40s; recording a medium-priority EN job with VO metadata within the CI context; linking work_045 to work_160 and tagging work_160 as 'localization'; completing the workflow for PR 4025; and sending a notification regarding the retime update. Use only tool-generated IDs/timestamps.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "updateSubtitleTiming",
                "arguments": {
                    "id": "subtitle_001",
                    "updates": {
                        "subtitle_start": 0.1,
                        "subtitle_end": 2.4
                    }
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "en"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "vo",
                        "build_run_id": "run_001",
                        "commit_sha": "abc123def456789"
                    }
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_160",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_160",
                    "label_name": "localization"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 4025,
                    "changed_keys": [
                        "subtitle_001"
                    ],
                    "locales_processed": [
                        "en"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "vo",
                        "build_run_id": "run_001",
                        "commit_sha": "abc123def456789"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Subtitle retimed: subtitle_001",
                    "message": "subtitle_001 retimed to 0.10–2.40",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (run_001)",
                "subtitle_001 retimed",
                "tms_job created",
                "work_045→work_160 linked",
                "work_160 tagged",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_036",
        "instruction": "Coordinate the CI-aware ES audio application for the key 'ui.settings.audio'. The expected outcomes are: consulting build run 'run_003' and commit 'abc123def456789' in a read-only mode; capturing a medium-priority ES job with metadata {'build_run_id':'run_003','commit_sha':'abc123def456789'}; documenting one ES translation as 'Audio'; setting validation to 'passed'; establishing a link from work_045 to work_170 marked as 'relates_to' and tagging work_170 as 'localization'; completing the workflow for PR 4026 with consistent CI metadata; and sending an info notification titled 'Job queued: ui.settings.audio [es]' with the message 'TMS job created for ui.settings.audio'. Use only tool-generated IDs/timestamps. Translation entries should solely include: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_003"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "build_run_id": "run_003",
                        "commit_sha": "abc123def456789"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "es",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es",
                    "validation_status": "passed"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_170",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_170",
                    "label_name": "localization"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 4026,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed",
                    "metadata": {
                        "build_run_id": "run_003",
                        "commit_sha": "abc123def456789"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.settings.audio [es]",
                    "message": "TMS job created for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (run_003, abc123def456789)",
                "tms_job created",
                "es translation recorded",
                "es validation passed",
                "work_045→work_170 linked",
                "work_170 tagged",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_037",
        "instruction": "Document a FR truncation detection and fix along with traceability. Success criteria: consult the current FR value for 'ui.main_menu.start_game'; log validation as failed with error 'Truncation risk at 20 char'; capture a high-priority FR job for the main menu using UI/Main Menu metadata; dispatch an update notification related to the issue; record translation 'Jouer'; set follow-up validation to passed; ensure a completed workflow for PR 1027 is present. Use tool-generated IDs/timestamps exclusively. Include in translation entries only: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "fr"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "fr",
                    "validation_status": "failed",
                    "validation_error": "Truncation risk at 20 char"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.main_menu.start_game [fr]",
                    "message": "TMS job created for ui.main_menu.start_game",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations failed: ui.main_menu.start_game [fr]",
                    "message": "Truncation risk at 20 char for ui.main_menu.start_game",
                    "channel": "slack"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "fr",
                            "target_string": "Jouer"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "fr",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1027,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "fr"
                    ],
                    "status": "completed"
                }
            }
        ],
        "outputs": [
                "context consulted (fr)",
                "fr failed",
                "tms_job created",
                "notifications sent",
                "fr translation recorded",
                "fr passed",
                "localization workflow completed"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_038",
        "instruction": "Maintain deterministic labeling, linking, and an ES (Spanish) settings workflow. Success criteria: tag work_130 with 'localization'; ensure a 'relates_to' link from work_045 to work_150 is present; consult the current ES value for 'ui.settings.audio'; capture a high-priority ES job using UI metadata; ensure a completed workflow for PR 1028 is present; send an update notification using the template title='Validations passed: ui.settings.audio [es]' and message='Validations passed for es for ui.settings.audio' to Slack. Employ tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_130",
                    "label_name": "localization"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_150",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui"
                    }
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1028,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [es]",
                    "message": "Validations passed for es for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "work_130 tagged",
                "work_045→work_150 linked",
                "context consulted (es)",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_039",
        "instruction": "Handle a deterministic dual-locale rollout for 'ui.main_menu.start_game' in ZH and JA. Your success criteria: consult the current ZH and JA values; ensure a high-priority UI/Main Menu job targeting ZH and JA is documented; confirm a completed workflow for PR 1029 exists; and send an info notification using the template title='Job queued: ui.main_menu.start_game [zh,ja]' and message='TMS job created for ui.main_menu.start_game'. Utilize IDs/timestamps generated by tools exclusively.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "zh"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "ja"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "zh",
                        "ja"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1029,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "zh",
                        "ja"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.main_menu.start_game [zh,ja]",
                    "message": "TMS job created for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (zh/ja)",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_040",
        "instruction": "Coordinate a complete ZH localization cycle for 'ui.main_menu.start_game' with traceable linkage. Success criteria: capture a medium-priority ZH job; record the translation '\u5f00\u59cb\u6e38\u620f'; confirm validation is in passed state; verify work_050 \u2192 work_150 link (relates_to) exists; ensure a completed workflow for PR 1040 is present; and notify that ZH validation has passed. Only use IDs/timestamps generated by tools. Ensure translation entries include only: string_key, locale, target_string.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "zh"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "zh",
                            "target_string": "开始游戏"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "zh",
                    "validation_status": "passed"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_050",
                    "child_id": "work_150",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1040,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "zh"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.main_menu.start_game [zh]",
                    "message": "Validations passed for zh for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "zh translation recorded",
                "zh validation passed",
                "work_050→work_150 linked",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_041",
        "instruction": "Manage a FR/DE audio update and ensure its validation with clear traceability. The success criteria are: the current FR and DE values for 'ui.settings.audio' are reviewed; a high-priority job for FR and DE in UI/Settings is documented; precisely one translation for FR and one for DE ('Audio') are recorded; both locales must pass validation; a completed workflow for PR 1031 is present; and an update notification confirms that FR/DE audio is validated. Rely solely on tool-generated IDs/timestamps. Translation entries should strictly include: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "fr"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr",
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "fr",
                            "target_string": "Audio"
                        },
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "de",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "fr",
                    "validation_status": "passed"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1031,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "fr",
                        "de"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [fr,de]",
                    "message": "Validations passed for fr,de for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (fr,de)",
                "tms_job created",
                "fr/de translations recorded",
                "fr/de validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_042",
        "instruction": "Coordinate a CI-aware FR/ES audio update with precise, minimal documentation. The success criteria are: build run 'run_001' and commit 'abc123def456789' are accessed read-only; a high-priority UI/Settings job is documented with the CI context; one FR and one ES translation ('Audio') are precisely recorded; FR's validation is marked as passed, with no errors documented; a finished workflow for PR 1022 is verified within the CI context; and an update notification confirms the task's completion. Depend on tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr",
                        "es"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings",
                        "build_run_id": "run_001",
                        "commit_sha": "abc123def456789"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "fr",
                            "target_string": "Audio"
                        },
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "es",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "fr",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1022,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "fr",
                        "es"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings",
                        "build_run_id": "run_001",
                        "commit_sha": "abc123def456789"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [fr]",
                    "message": "Validations passed for fr for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (run_001, abc123def456789)",
                "tms_job created",
                "FR/ES translations recorded",
                "FR validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_043",
        "instruction": "Handle documentation of a deterministic DE overflow detection and resolution for 'ui.main_menu.start_game'. Your success criteria: verify the current value; initially record validation as failed (Text exceeds 200px width) and subsequently, record it as passed; capture a high-priority UI/Main Menu job; ensure an existing completed workflow for PR 1023 with owner and test-result metadata; and confirm resolution with an update notification. Utilize tool-generated IDs/timestamps only. Translation entries must be limited to: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de",
                    "validation_status": "failed",
                    "validation_error": "Text exceeds 200px width"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1023,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "overflow_issues": 1,
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu",
                        "owner": "tool-generated",
                        "test_result_id": "tool-generated"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.main_menu.start_game [de]",
                    "message": "Validations passed for de for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (de)",
                "de failed",
                "tms_job created",
                "de passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_044",
        "instruction": "Coordinate capturing the current ES value for 'ui.settings.audio', and then maintain a deterministic linkage and update ES settings. Your success criteria: capture a medium-priority UI/Settings job; establish a relation between work_045 and work_130 (relates_to) and tag work_130 with 'localization'; ensure exactly one ES translation ('Audio') is documented; confirm a completed workflow for PR 1024; and verify an update notification confirms link + ES audio completion. Only use tool-generated IDs/timestamps. Translation entries must consist exclusively of: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_130",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_130",
                    "label_name": "localization"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "es",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1024,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Link + ES audio done",
                    "message": "work_130 linked; ES update completed",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (es)",
                "tms_job created",
                "work_045→work_130 linked",
                "work_130 tagged",
                "es translation recorded",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_045",
        "instruction": "Handle documentation for a subtitle timing adjustment associated with the hero intro cut while ensuring VO traceability. Your success criteria include capturing a medium-priority VO job tagged with metadata.asset_path='hero intro cut'; linking work_055 to work_160 with link_type='relates_to'; maintaining a finalized workflow for PR 1025 that references the VO key 'vo.hero.intro_01' (changed_keys=['vo.hero.intro_01'], locales_processed=['en']); and dispatching a Slack notification update titled 'Subtitle timing adjusted' with the message 'vo.hero.intro_01 adjusted'. Utilize tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "target_locales": [
                        "en"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "asset_path": "hero intro cut"
                    }
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_055",
                    "child_id": "work_160",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1025,
                    "changed_keys": [
                        "vo.hero.intro_01"
                    ],
                    "locales_processed": [
                        "en"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Subtitle timing adjusted",
                    "message": "vo.hero.intro_01 adjusted",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "work items linked",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_046",
        "instruction": "Coordinate to ensure a ZH main-menu update appears with minimal, deterministic artifacts. Your success criteria involve consulting the current ZH value for 'ui.main_menu.start_game'; capturing a high-priority UI/Main Menu job; recording precisely one ZH translation ('\u5f00\u59cb\u6e38\u620f') without additional fields; setting validation to passed without any errors; maintaining a finalized workflow for PR 1026 with asset metadata; and confirming a ZH update through notification. Utilize tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "zh"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "zh"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "zh",
                            "target_string": "开始游戏"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "zh",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1026,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "zh"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.main_menu.start_game [zh]",
                    "message": "Validations passed for zh for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (zh)",
                "tms_job created",
                "zh translation recorded",
                "zh validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_047",
        "instruction": "Handle the documentation of a deterministic DE overflow detection and resolution concerning 'ui.main_menu.start_game'. Your deliverables should display: an account of validation history indicating an initial failure with validation_error 'Text exceeds 200px width', followed by a successful pass; a Slack notification update titled 'Validations failed: ui.main_menu.start_game [de]' and message 'Text exceeds 200px width for ui.main_menu.start_game'; a solitary high-priority TMS job focused on 'de' within UI/Main Menu; and a finalized workflow for PR 1027 with changed_keys=['ui.main_menu.start_game'], locales_processed=['de'], overflow_issues=1, status='completed'. Employ tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de",
                    "validation_status": "failed",
                    "validation_error": "Text exceeds 200px width"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations failed: ui.main_menu.start_game [de]",
                    "message": "Text exceeds 200px width for ui.main_menu.start_game",
                    "channel": "slack"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1027,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "overflow_issues": 1,
                    "status": "completed"
                }
            }
        ],
        "outputs": [
                "de failed",
                "notification sent",
                "tms_job created",
                "de passed",
                "localization workflow completed"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_048",
        "instruction": "Coordinate the persistence of a deterministic JA rollout linked to 'ui.settings.audio'. Required outcomes include: consulting the current JA value for 'ui.settings.audio' in a read-only mode; recording a high-priority UI/Settings TMS job for 'ja'; linking work_045 \u2192 work_150 with link_type='relates_to' and tagging work_150 as 'localization'; ensuring a completed localization workflow for PR 1028 with changed_keys=['ui.settings.audio'], locales_processed=['ja'], overflow_issues=0, status='completed'; and dispatching an info Slack notification with the title 'Job queued: ui.settings.audio [ja]' and the message 'TMS job created for ui.settings.audio'. Utilize tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "ja"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_150",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_150",
                    "label_name": "localization"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1028,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "ja"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.settings.audio [ja]",
                    "message": "TMS job created for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (ja)",
                "tms_job created",
                "link created",
                "label applied",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_049",
        "instruction": "Handle the consultation of the current ES record for 'ui.settings.audio' (read-only), followed by deploying a deterministic ES update ensuring validation and traceability. Your criteria for success include: only one ES translation ('Audio') being documented with no additional fields; ES validation should be marked as passed without error; a medium-priority UI/Settings job is logged; a completed workflow for PR 1029 is present; and there is an update notification confirming the translation application. Only use tool-generated IDs/timestamps. Ensure translation entries contain exclusively: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "es",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1029,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [es]",
                    "message": "Validations passed for es for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (es)",
                "es translation recorded",
                "es validation passed",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_050",
        "instruction": "Coordinate the persistence of a deterministic UI batch rollout for FR/ES/DE using the current 'localization' label with minimal fixed fields. Required outcomes are: capturing a high-priority UI batch job for FR/ES/DE; verifying a completed workflow for PR 1030 over changed_keys=['ui.main_menu.start_game','ui.settings.audio'] and locales_processed=['fr','es','de']; tagging work_130 with the existing 'localization' label; and dispatching an info Slack notification with the precise strings title='Localization workflow completed: ui.main_menu.start_game, ui.settings.audio [fr,es,de]' and message='Localization workflow completed for ui.main_menu.start_game, ui.settings.audio (fr, es, de)'. Utilize only tool-generated IDs/timestamps.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr",
                        "es",
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui"
                    }
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1030,
                    "changed_keys": [
                        "ui.main_menu.start_game",
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "fr",
                        "es",
                        "de"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Localization workflow completed: ui.main_menu.start_game, ui.settings.audio [fr,es,de]",
                    "message": "Localization workflow completed for ui.main_menu.start_game, ui.settings.audio (fr, es, de)",
                    "channel": "slack"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_130",
                    "label_name": "localization"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "localization workflow completed",
                "notification sent",
                "label applied"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_051",
        "instruction": "Handle CI context to store an update to the JA main-menu with traceability. Required outcomes: reference build run 'run_001' and test result 'test_result_001' in a read-only manner; log a high-priority UI/Main Menu job aimed at JA; ensure exactly one JA translation ('\u30b2\u30fc\u30e0\u958b\u59cb') is documented for 'ui.main_menu.start_game'; verify the existence of a completed workflow for PR 1031, which includes build_run_id='run_001' and test_result_id='test_result_001'; and send a Slack notification update using the precise strings title='JA start label applied: ui.main_menu.start_game [ja]' and message='JA start label applied for ui.main_menu.start_game'. Only utilize tool-generated IDs/timestamps. Translation entries must solely contain: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "getTestResult",
                "arguments": {
                    "id": "test_result_001"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "ja"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "ja",
                            "target_string": "ゲーム開始"
                        }
                    ]
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1031,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "ja"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu",
                        "build_run_id": "run_001",
                        "test_result_id": "test_result_001"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "JA start label applied: ui.main_menu.start_game [ja]",
                    "message": "JA start label applied for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (run_001, test_result_001, ja string read)",
                "tms_job created",
                "ja translation recorded",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_052",
        "instruction": "Coordinate a deterministic update to IT/PT settings. Required outcomes: log a high-priority UI/Settings job for both IT and PT; reference the current IT and PT values for 'ui.settings.audio' in a read-only fashion; ensure the recording of exactly one IT translation ('Audio') and one PT translation ('\u00c1udio') (entries must include only string_key, locale, target_string); validate both locales to 'passed'; confirm the existence of a completed workflow for PR 1032; and a notification for validation confirmation must be sent using the exact strings title='Validations passed: ui.settings.audio [it,pt]' and message='Validations passed for it,pt for ui.settings.audio'. Utilize tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "it",
                        "pt"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "it"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "pt"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "it",
                            "target_string": "Audio"
                        },
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "pt",
                            "target_string": "Áudio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "it",
                    "validation_status": "passed"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "pt",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1032,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "it",
                        "pt"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [it,pt]",
                    "message": "Validations passed for it,pt for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "context consulted (it, pt)",
                "it/pt translations recorded",
                "it passed",
                "pt passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_053",
        "instruction": "Handle a deterministic RU/PL main-menu rollout. Outcomes needed: a high-priority UI/Main Menu task for RU/PL is documented; the current RU and PL values for 'ui.main_menu.start_game' are referenced read-only; only one RU translation ('\u041d\u0430\u0447\u0430\u0442\u044c \u0438\u0433\u0440\u0443') and one PL translation ('Rozpocznij gr\u0119') are recorded (entries only include string_key, locale, target_string); both locales are marked as having 'passed' validation; a completed workflow exists for PR 1033; and an update notification confirms validation with the precise strings title='Validations passed: ui.main_menu.start_game [ru,pl]' and message='Validations passed for ru,pl for ui.main_menu.start_game'. Utilize tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ru",
                        "pl"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "ru"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "pl"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "ru",
                            "target_string": "Начать игру"
                        },
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "pl",
                            "target_string": "Rozpocznij grę"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "ru",
                    "validation_status": "passed"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "pl",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1033,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "ru",
                        "pl"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.main_menu.start_game [ru,pl]",
                    "message": "Validations passed for ru,pl for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "context consulted (ru, pl)",
                "ru/pl translations recorded",
                "ru passed",
                "pl passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_054",
        "instruction": "Coordinate a deterministic FR overflow detection/resolution. Necessary outcomes: the current FR value for 'ui.main_menu.start_game' is accessed read-only; validation is logged as failed with validation_error='Text exceeds 200px width' and then recorded as passed; a high-priority UI/Main Menu job for FR is documented; a completed workflow for PR 1034 is in place; and an update notification confirms resolution with the exact strings title='Validations passed: ui.main_menu.start_game [fr]' and message='Validations passed for fr for ui.main_menu.start_game'. Employ tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "fr"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "fr",
                    "validation_status": "failed",
                    "validation_error": "Text exceeds 200px width"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "fr",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1034,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "fr"
                    ],
                    "overflow_issues": 1,
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.main_menu.start_game [fr]",
                    "message": "Validations passed for fr for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (fr)",
                "fr failed",
                "fr passed",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_055",
        "instruction": "Handle the persistence of a deterministic ES/FR settings and linkage update. Required outcomes include: a medium-priority UI/Settings job for ES/FR is captured; work_045 is connected to work_131 with link_type='relates_to'; work_131 needs to be tagged with 'localization'; a completed workflow must exist for PR 1035 with changed_keys=['ui.settings.audio'] and locales_processed=['es','fr']; and a 'job queued' Slack notification should be sent containing the exact strings title='Job queued: ui.settings.audio [es,fr]' and message='TMS job created for ui.settings.audio' with notification_type='info'. Only use tool-generated IDs/timestamps.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es",
                        "fr"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_131",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_131",
                    "label_name": "localization"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1035,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es",
                        "fr"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.settings.audio [es,fr]",
                    "message": "TMS job created for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "work items linked",
                "work item tagged",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_056",
        "instruction": "Coordinate the capture of a deterministic VO timing update along with artifacts. Required results are: subtitle_001 timing is updated to start 0.20s and end 2.50s; capture a medium-priority VO job; ensure there is a completed workflow for PR 1036; and send a 'job queued' Slack notification using the precise strings title='Job queued: subtitle_001 [en]' and message='TMS job created for subtitle_001' with notification_type='info'. Make sure to utilize tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "updateSubtitleTiming",
                "arguments": {
                    "id": "subtitle_001",
                    "updates": {
                        "subtitle_start": 0.2,
                        "subtitle_end": 2.5
                    }
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "en"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "vo"
                    }
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1036,
                    "changed_keys": [],
                    "locales_processed": [
                        "en"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "vo"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: subtitle_001 [en]",
                    "message": "TMS job created for subtitle_001",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "subtitle_001 updated",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_057",
        "instruction": "Handle a deterministic KO main-menu update. Required outcomes: ensure a high-priority UI/Main Menu job for KO is captured; record exactly one KO translation ('\uac8c\uc784 \uc2dc\uc791') including only string_key, locale, target_string; validation for KO is confirmed as 'passed'; ensure a completed workflow for PR 1037 exists; and verify an update notification that confirms validation with title='Validations passed: ui.main_menu.start_game [ko]' and message='Validations passed for ko for ui.main_menu.start_game'. Only use tool-generated IDs/timestamps.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ko"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "ko",
                            "target_string": "게임 시작"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "ko",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1037,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "ko"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.main_menu.start_game [ko]",
                    "message": "Validations passed for ko for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "ko translation recorded",
                "ko validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_058",
        "instruction": "Coordinate capturing CI context and maintaining a deterministic UI batch rollout for IT/PT/FR. Success conditions: consult build run 'run_001' and commit 'abc123def456789' in read-only mode; document exactly one IT/PT/FR translation ('Audio') each, including only string_key, locale, target_string; validate that all three locales are passed; record a high-priority UI job containing the CI metadata; ensure work_045 \u2192 work_130 has link_type='relates_to' and work_130 is tagged as 'localization'; verify a completed workflow for PR 1038 with the CI metadata; and confirm an info notification that validates using title='Validations passed: ui.settings.audio [fr,it,pt]' and message='Validations passed for fr,it,pt for ui.settings.audio'. Make use of tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "getSourceChange",
                "arguments": {
                    "commit_sha": "abc123def456789"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "it",
                            "target_string": "Audio"
                        },
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "pt",
                            "target_string": "Audio"
                        },
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "fr",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "it",
                    "validation_status": "passed"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "pt",
                    "validation_status": "passed"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "fr",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "it",
                        "pt",
                        "fr"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "build_run_id": "run_001",
                        "commit_sha": "abc123def456789"
                    }
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_130",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_130",
                    "label_name": "localization"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1038,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "it",
                        "pt",
                        "fr"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "build_run_id": "run_001",
                        "commit_sha": "abc123def456789"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Validations passed: ui.settings.audio [fr,it,pt]",
                    "message": "Validations passed for fr,it,pt for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (run_001, abc123def456789)",
                "it/pt/fr translations recorded",
                "it/pt/fr validation passed",
                "tms_job created",
                "work_045→work_130 linked and labeled",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_059",
        "instruction": "Address a CI build failure and initiate a DE remediation with traceability. Success criteria: consult build run 'run_003', commit 'abc123def456789', and test_result 'test_result_001' in a read-only manner; ensure a high-priority DE job is recorded with the CI metadata; link work_110 to work_210 with link_type='relates_to'; verify the existence of an in-progress workflow for PR 1039 over 'ui.main_menu.start_game'; and ensure an update notification uses the deterministic template title='Job queued: ui.main_menu.start_game [de]' and message='TMS job created for ui.main_menu.start_game'. Use exclusively tool-generated IDs/timestamps.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_003"
                },
            },
            {
                "name": "getSourceChange",
                "arguments": {
                    "commit_sha": "abc123def456789"
                },
            },
            {
                "name": "getTestResult",
                "arguments": {
                    "id": "test_result_001"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu",
                        "build_run_id": "run_003",
                        "commit_sha": "abc123def456789",
                        "test_result_id": "test_result_001"
                    }
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_110",
                    "child_id": "work_210",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1039,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "status": "in_progress",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Job queued: ui.main_menu.start_game [de]",
                    "message": "TMS job created for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "CI context consulted (run_003, abc123def456789, test_result_001)",
                "remediation tms_job created",
                "work items linked",
                "workflow started (in_progress)",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_060",
        "instruction": "Securely store a deterministic JA settings apply v2. Success criteria: record exactly one JA translation ('\u30aa\u30fc\u30c7\u30a3\u30aa') for 'ui.settings.audio' (entry includes only string_key, locale, target_string); set JA validation to passed; capture a medium-priority UI/Settings job targeting JA; confirm the completion of a workflow for PR 1040; and verify an update notification confirms validation using title='Validations passed: ui.settings.audio [ja]' and message='Validations passed for ja for ui.settings.audio'. Use only tool-generated IDs/timestamps.",
        "actions": [
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "ja",
                            "target_string": "オーディオ"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "ja",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1040,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "ja"
                    ],
                    "overflow_issues": 0,
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [ja]",
                    "message": "Validations passed for ja for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "ja translation recorded",
                "ja validation passed",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_061",
        "instruction": "Handle the completion of an audited FR/ES settings-audio application with CI traceability. Success is achieved when build run 'run_001' is consulted read-only; a high-priority UI/Settings job for FR/ES is recorded with CI metadata (build_run_id 'run_001'); precisely one FR and one ES translation ('Audio') are recorded (the entries should include only string_key, locale, target_string); both locales pass validation with validation_error 'None'; work_045\u2192work_130 is linked using link_type='relates_to' and work_130 is identified as 'localization'; a finished workflow for PR 1041 is present with identical CI metadata; and an info notification confirms completion with title='Localization completed: ui.settings.audio [fr,es]' and message='Completed rollout for ui.settings.audio (fr, es)'. Utilize tool-generated IDs/timestamps solely.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "fr",
                            "target_string": "Audio"
                        },
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "es",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "fr",
                    "validation_status": "passed",
                    "validation_error": "None"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es",
                    "validation_status": "passed",
                    "validation_error": "None"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr",
                        "es"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings",
                        "build_run_id": "run_001"
                    }
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_130",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_130",
                    "label_name": "localization"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1041,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "fr",
                        "es"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings",
                        "build_run_id": "run_001"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Localization completed: ui.settings.audio [fr,es]",
                    "message": "Completed rollout for ui.settings.audio (fr, es)",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (run_001)",
                "fr/es translations recorded",
                "fr/es validation passed",
                "tms_job created",
                "work_045→work_130 linked",
                "work_130 labeled",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_062",
        "instruction": "Coordinate the completion of an audited IT main-menu update with CI traceability. Success is indicated by consulting build run 'run_001' read-only; the current IT value is audited; exactly one IT translation ('Inizia') is recorded (the entry should consist only of string_key, locale, target_string); IT validation passes with validation_error 'None'; a high-priority UI/Main Menu job is filed with metadata (build_run_id 'run_001'); work_045\u2192work_140 is linked as link_type='relates_to' and marked 'localization'; a completed workflow for PR 1042 is found; and an info notification confirms completion using title='Localization completed: ui.main_menu.start_game [it]' and message='Completed rollout for ui.main_menu.start_game (it)'. Employ tool-generated IDs/timestamps solely.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "it"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "it",
                            "target_string": "Inizia"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "it",
                    "validation_status": "passed",
                    "validation_error": "None"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "it"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu",
                        "build_run_id": "run_001"
                    }
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_140",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_140",
                    "label_name": "localization"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1042,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "it"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu",
                        "build_run_id": "run_001"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Localization completed: ui.main_menu.start_game [it]",
                    "message": "Completed rollout for ui.main_menu.start_game (it)",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (run_001, it string read)",
                "it translation recorded",
                "it validation passed",
                "tms_job created",
                "work_045→work_140 linked",
                "work_140 labeled",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_063",
        "instruction": "Handle the batch rollout for JA/KO associated with asset 'assets/ui/main_menu.json'. A high-priority UI job must focus on JA/KO with metadata.asset_path='assets/ui/main_menu.json'; ensure exactly four translations are logged (ui.main_menu.start_game: JA '\u30b2\u30fc\u30e0\u958b\u59cb', KO '\uac8c\uc784 \uc2dc\uc791'; ui.settings.audio: JA '\u30aa\u30fc\u30c7\u30a3\u30aa', KO '\uc624\ub514\uc624') with entries limited to string_key, locale, target_string; connect work_060 with work_132 using link_type='relates_to'; verify there is a complete workflow for PR 1043 involving changed_keys=['ui.main_menu.start_game','ui.settings.audio'] and locales_processed=['ja','ko']; and confirm completion with an info notification titled 'Batch complete: ui.main_menu.start_game, ui.settings.audio [ja,ko]' and message 'Completed rollout for ui.main_menu.start_game and ui.settings.audio (ja, ko)'. Rely on tool-generated IDs/timestamps.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja",
                        "ko"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "asset_path": "assets/ui/main_menu.json"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "ja",
                            "target_string": "ゲーム開始"
                        },
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "ko",
                            "target_string": "게임 시작"
                        },
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "ja",
                            "target_string": "オーディオ"
                        },
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "ko",
                            "target_string": "오디오"
                        }
                    ]
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_060",
                    "child_id": "work_132",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1043,
                    "changed_keys": [
                        "ui.main_menu.start_game",
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "ja",
                        "ko"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Batch complete: ui.main_menu.start_game, ui.settings.audio [ja,ko]",
                    "message": "Completed rollout for ui.main_menu.start_game and ui.settings.audio (ja, ko)",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "translations recorded",
                "work items linked",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_064",
        "instruction": "Coordinate an audited remediation of DE truncation for 'ui.settings.audio' with CI traceability. Demonstrate within the artifacts that build run 'run_001' was referenced and the current DE value was read without alteration; the validation lifecycle must have detected a failure ('Truncation risk in 180px') which ultimately transitions to 'passed'; record exactly one DE translation as 'Audio' with translation entries only including: string_key, locale, target_string; ensure the work is associated with a single high-priority UI/Settings TMS job marked with the build run ID ('run_001'); that work_045 is connected to work_130 using a 'relates_to' link and work_130 features the 'localization' label; confirm PR 1044 is finalized with overflow_issues=1; and confirm completion using an info Slack notification titled 'Localization completed: ui.settings.audio [de]' and message 'Completed remediation and rollout for ui.settings.audio (de)'. Utilize tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "getBuildRun",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de",
                    "validation_status": "failed",
                    "validation_error": "Truncation risk in 180px"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "build_run_id": "run_001"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "de",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de",
                    "validation_status": "passed",
                    "validation_error": "None"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_130",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_130",
                    "label_name": "localization"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1044,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "overflow_issues": 1,
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Localization completed: ui.settings.audio [de]",
                    "message": "Completed remediation and rollout for ui.settings.audio (de)",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (run_001, de string read)",
                "de failed then passed",
                "tms_job created",
                "de translation recorded",
                "work_045→work_130 linked and labeled",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_065",
        "instruction": "Handle a fixed IT/PT main-menu apply for string_key 'ui.main_menu.start_game'. Ensure success by verifying: the current value for 'ui.main_menu.start_game' is reviewed in a read-only manner for both IT and PT locales; precisely one PT 'Iniciar' and one IT 'Inizia' translation entry is documented (entries incorporate only string_key, locale, target_string); a medium-priority UI/Main Menu task is logged with metadata {'component':'ui','subcomponent':'main_menu'}; a completed workflow for PR 1045 is present, referencing changed_keys=['ui.main_menu.start_game'] and locales_processed=['it','pt']; and an update Slack notification is dispatched with title='Localization applied: ui.main_menu.start_game [it,pt]' and message='Applied translations for ui.main_menu.start_game (it,pt)'. Employ tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "it"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "pt"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "pt",
                            "target_string": "Iniciar"
                        },
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "it",
                            "target_string": "Inizia"
                        }
                    ]
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "it",
                        "pt"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1045,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "it",
                        "pt"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Localization applied: ui.main_menu.start_game [it,pt]",
                    "message": "Applied translations for ui.main_menu.start_game (it,pt)",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (it,pt)",
                "pt/it translations recorded",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_066",
        "instruction": "Coordinate the refresh of the French 'Settings Audio' string. Achieve success by consulting the existing FR string; recording a medium-priority UI/Settings task; documenting and validating one FR translation ('Audio (actualis\u00e9)') as 'passed'; linking work_050 to work_140 (relates_to) and tagging work_140 as 'localization'; ensuring a completed workflow for PR 1046; and dispatching an update notification. Utilize tool-generated IDs/timestamps exclusively. Translation entries must include only: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "fr"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "fr",
                            "target_string": "Audio (actualisé)"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "fr",
                    "validation_status": "passed"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_050",
                    "child_id": "work_140",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_140",
                    "label_name": "localization"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1046,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "fr"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [fr]",
                    "message": "Validations passed for fr for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted (fr)",
                "tms_job created",
                "translation recorded and validated",
                "work items linked and labeled",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_067",
        "instruction": "Handle a VO timing polish for 'subtitle_001'. Success: subtitle_001 has been adjusted to start at 0.15s and end at 2.40s; a medium-priority EN timing job is logged; the completed workflow for PR 1047 cites the timing key (changed_keys=['subtitle_001'], locales_processed=['en']); and an info notification verifies the modification with title='Subtitle timing adjusted' and message='subtitle_001 adjusted'. Use tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "updateSubtitleTiming",
                "arguments": {
                    "id": "subtitle_001",
                    "updates": {
                        "subtitle_start": 0.15,
                        "subtitle_end": 2.4
                    }
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "en"
                    ],
                    "priority": "medium"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1047,
                    "changed_keys": [
                        "subtitle_001"
                    ],
                    "locales_processed": [
                        "en"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Subtitle timing adjusted",
                    "message": "subtitle_001 adjusted",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "subtitle_001 updated",
                "tms_job created",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_068",
        "instruction": "Coordinate a deterministic ZH main-menu update v2. Success: the current ZH value for 'ui.main_menu.start_game' is accessed read-only; a high-priority UI/Main Menu task for ZH is documented with metadata.component='ui' and metadata.subcomponent='main_menu'; precisely one ZH translation ('\u5f00\u59cb\u6e38\u620f') is archived (entry includes only string_key, locale, target_string); ZH validation is marked as 'passed'; a finalized workflow for PR 1048 is present with the same metadata; and an update notification confirms validation using title='Validations passed: ui.main_menu.start_game [zh]' and message='Validations passed for zh for ui.main_menu.start_game'. Use tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "zh"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "zh"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "zh",
                            "target_string": "开始游戏"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "zh",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1048,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "zh"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.main_menu.start_game [zh]",
                    "message": "Validations passed for zh for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted",
                "tms_job created",
                "zh translation recorded",
                "zh validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_069",
        "instruction": "Coordinate a Spanish main-menu update triggered by commit 'def234abc' for asset 'assets/ui/main_menu.json'. Success: a high-priority UI/Main Menu job is recorded with metadata.commit_sha='def234abc' and metadata.asset_path='assets/ui/main_menu.json'; exactly one ES translation ('Comenzar juego') is recorded (entry includes only string_key, locale, target_string); work_070\u2192work_170 is linked with link_type='relates_to'; a completed workflow for PR 1049 exists; and an info notification uses the 'Job queued' template with title='Job queued: ui.main_menu.start_game [es]' and message='TMS job created for ui.main_menu.start_game'. Use tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "high",
                    "metadata": {
                        "commit_sha": "def234abc",
                        "asset_path": "assets/ui/main_menu.json"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "es",
                            "target_string": "Comenzar juego"
                        }
                    ]
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_070",
                    "child_id": "work_170",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1049,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.main_menu.start_game [es]",
                    "message": "TMS job created for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "translation recorded",
                "work items linked",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_070",
        "instruction": "Manage the capture of a deterministic FR/DE settings validation after consulting the current value in read-only mode. Success: high-priority UI/Settings job for FR/DE; one FR and one DE translation ('Audio'); both locales validated 'passed'; completed workflow for PR 1050; and an update notification. Use tool-generated IDs/timestamps only. Translation entries must include only: string_key, locale, target_string.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "fr"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr",
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "fr",
                            "target_string": "Audio"
                        },
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "de",
                            "target_string": "Audio"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "fr",
                    "validation_status": "passed"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1050,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "fr",
                        "de"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [fr,de]",
                    "message": "Validations passed for fr,de for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context consulted",
                "tms_job created",
                "fr/de translations recorded",
                "fr/de validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_071",
        "instruction": "Handle the persistence of a deterministic RU main-menu update v2 for 'ui.main_menu.start_game'. Success involves recording a high-priority UI/Main Menu job specifically for RU; ensuring one exact RU translation ('\u041d\u0430\u0447\u0430\u0442\u044c \u0438\u0433\u0440\u0443') is logged (entry includes only string_key, locale, target_string); setting RU validation status to 'passed'; verifying the existence of a completed workflow for PR 1051; and acknowledging an update notification that confirms validation using title='Validations passed: ui.main_menu.start_game [ru]' and message='Validations passed for ru for ui.main_menu.start_game'. Tool-generated IDs/timestamps should be used exclusively.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ru"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "ru",
                            "target_string": "Начать игру"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "ru",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1051,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "ru"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "main_menu"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.main_menu.start_game [ru]",
                    "message": "Validations passed for ru for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "ru translation recorded",
                "ru validation passed",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_072",
        "instruction": "Coordinate a dual-locale main-menu remediation for 'ui.main_menu.start_game' with CI identifiers, ensuring translation entries lack validation fields. Successful orchestration includes capturing CI metadata (commit 'c0ffee000000045', build 'run_045', test 'test_result_045') on the job; recording FR 'Commencer' and DE 'Starten'; managing FR validation which initially fails ('Text exceeds 200px width') then succeeds ('None'); DE validation is confirmed as passed ('None'); linking work_045 to work_230 with link_type='relates_to' and tagging work_230 with 'label_001'; including identical CI metadata in the completed workflow for PR 2001; and dispatching two notifications using title='Job queued: ui.main_menu.start_game [fr,de]' / message='TMS job created for ui.main_menu.start_game' (info) and title='Validations passed: ui.main_menu.start_game [fr,de]' / message='Validations passed for fr,de for ui.main_menu.start_game' (update). Ensure usage of tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr",
                        "de"
                    ],
                    "metadata": {
                        "commit_sha": "c0ffee000000045",
                        "build_run_id": "run_045",
                        "test_result_id": "test_result_045"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "fr",
                            "target_string": "Commencer"
                        },
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "de",
                            "target_string": "Starten"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "fr",
                    "validation_status": "failed",
                    "validation_error": "Text exceeds 200px width"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "fr",
                    "validation_status": "passed",
                    "validation_error": "None"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de",
                    "validation_status": "passed",
                    "validation_error": "None"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_230",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_230",
                    "label_name": "label_001"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 2001,
                    "changed_keys": [
                        "ui.main_menu.start_game"
                    ],
                    "locales_processed": [
                        "fr",
                        "de"
                    ],
                    "status": "completed",
                    "metadata": {
                        "commit_sha": "c0ffee000000045",
                        "build_run_id": "run_045",
                        "test_result_id": "test_result_045"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.main_menu.start_game [fr,de]",
                    "message": "TMS job created for ui.main_menu.start_game",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.main_menu.start_game [fr,de]",
                    "message": "Validations passed for fr,de for ui.main_menu.start_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "fr/de translations recorded",
                "fr failed then passed",
                "de passed",
                "work_045→work_230 linked",
                "label applied",
                "workflow completed",
                "notifications sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_073",
        "instruction": "Handle a tri-locale rollout for 'ui.settings.audio' incorporating CI context and a JA overflow correction. Success criteria (goal-oriented, not sequential): the task should capture CI metadata {commit_sha:'a1b2c3d4e5f6', build_run_id:'run_046', test_result_id:'test_result_046'}; FR 'Audio', ES 'Audio', and JA '\u30aa\u30fc\u30c7\u30a3\u30aa' must be recorded (entries comprise only of string_key, locale, target_string); FR/ES validations achieve 'passed' with no validation_error; JA contains one 'failed' entry with validation_error 'Text exceeds 200px width' which ultimately 'passes' after noting the JA correction '\u30b5\u30a6\u30f3\u30c9'; link work_045\u2192work_150 using link_type='relates_to' with work_150 tagged 'label_001'; a completed workflow for PR 2002 should reference changed_keys=['ui.settings.audio'] and locales_processed=['fr','es','ja'] maintaining the same CI metadata; and send deterministic queued/completed Slack notifications for 'ui.settings.audio' and locales [fr,es,ja]. Ensure use of tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr",
                        "es",
                        "ja"
                    ],
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings",
                        "commit_sha": "a1b2c3d4e5f6",
                        "build_run_id": "run_046",
                        "test_result_id": "test_result_046"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "fr",
                            "target_string": "Audio"
                        },
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "es",
                            "target_string": "Audio"
                        },
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "ja",
                            "target_string": "オーディオ"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "fr",
                    "validation_status": "passed",
                    "validation_error": "None"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es",
                    "validation_status": "passed",
                    "validation_error": "None"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "ja",
                    "validation_status": "failed",
                    "validation_error": "Text exceeds 200px width"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "ja",
                            "target_string": "サウンド"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "ja",
                    "validation_status": "passed",
                    "validation_error": "None"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_150",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_150",
                    "label_name": "label_001"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 2002,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "fr",
                        "es",
                        "ja"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings",
                        "commit_sha": "a1b2c3d4e5f6",
                        "build_run_id": "run_046",
                        "test_result_id": "test_result_046"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.settings.audio [fr,es,ja]",
                    "message": "TMS job created for ui.settings.audio",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [fr,es,ja]",
                    "message": "Validations passed for fr,es,ja for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "fr/es/ja translations recorded",
                "fr/es passed",
                "ja failed then passed",
                "work_045→work_150 linked",
                "label applied",
                "workflow completed",
                "notifications sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_074",
        "instruction": "Coordinate VO timing remediation for 'subtitle_001' utilizing CI context. Ensure success by updating subtitle_001 timing to begin at 0.20s and conclude at 2.50s; connect work_045\u2192work_160 with link_type='relates_to' and assign label 'label_001'; ensure a completed workflow for PR 2003 with metadata.commit_sha='feedface047', metadata.build_run_id='run_047', metadata.test_result_id='test_result_047'; dispatch two notifications with title='Job queued: subtitle_001 [en]' / message='TMS job created for subtitle_001' (info) and title='Subtitle timing adjusted' / message='subtitle_001 adjusted' (update). Ensure the use of tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "updateSubtitleTiming",
                "arguments": {
                    "id": "subtitle_001",
                    "updates": {
                        "subtitle_start": 0.2,
                        "subtitle_end": 2.5
                    }
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_045",
                    "child_id": "work_160",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_160",
                    "label_name": "label_001"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 2003,
                    "changed_keys": [
                        "subtitle_001"
                    ],
                    "locales_processed": [
                        "en"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "vo",
                        "commit_sha": "feedface047",
                        "build_run_id": "run_047",
                        "test_result_id": "test_result_047"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: subtitle_001 [en]",
                    "message": "TMS job created for subtitle_001",
                    "channel": "slack"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Subtitle timing adjusted",
                    "message": "subtitle_001 adjusted",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "subtitle_001 updated",
                "work_045→work_160 linked",
                "label applied",
                "workflow completed",
                "notifications sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_075",
        "instruction": "Handle a DE audio settings bug identified from CI (build 'run_008', commit 'ace111') for 'ui.settings.audio'. Success is achieved when a high-priority UI/Settings job is logged with the referenced CI data; the corrected DE translation ('Audio (korrigiert)') is recorded; work_120\u2192work_220 is connected using link_type='relates_to' and assigned label_003; a completed workflow for PR 1075 is available; and an update notification verifies validation with title='Validations passed: ui.settings.audio [de]' along with message='Validations passed for de for ui.settings.audio'. Utilize only tool-generated IDs/timestamps. Translation entries must consist solely of: string_key, locale, target_string.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings",
                        "build_run_id": "run_008",
                        "commit_sha": "ace111"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.audio",
                            "locale": "de",
                            "target_string": "Audio (korrigiert)"
                        }
                    ]
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de",
                    "validation_status": "passed"
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_120",
                    "child_id": "work_220",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_220",
                    "label_name": "label_003"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1075,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "status": "completed",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "settings"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.audio [de]",
                    "message": "Validations passed for de for ui.settings.audio",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "translation recorded",
                "de validation passed",
                "work items linked and tagged",
                "workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_076",
        "instruction": "Coordinate a FR/ES main-menu batch update for asset 'assets/ui/main_menu.json'. Success is defined as a medium-priority job focusing on FR and ES; four translations are documented (ui.main_menu.start_game: FR 'Lancer la partie', ES 'Iniciar partida'; ui.main_menu.quit_game: FR 'Quitter', ES 'Salir'); work_080\u2192work_180 is tied with link_type='relates_to'; a completed workflow for PR 1076 is present; and an info notification signals completion with the title='Batch completed: ui.main_menu.start_game, ui.main_menu.quit_game [fr,es]' and message='Batch completed for fr,es for ui.main_menu.start_game, ui.main_menu.quit_game'. Only employ tool-generated IDs/timestamps. Translation entries must contain only: string_key, locale, target_string.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr",
                        "es"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "asset_path": "assets/ui/main_menu.json"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "fr",
                            "target_string": "Lancer la partie"
                        },
                        {
                            "string_key": "ui.main_menu.start_game",
                            "locale": "es",
                            "target_string": "Iniciar partida"
                        },
                        {
                            "string_key": "ui.main_menu.quit_game",
                            "locale": "fr",
                            "target_string": "Quitter"
                        },
                        {
                            "string_key": "ui.main_menu.quit_game",
                            "locale": "es",
                            "target_string": "Salir"
                        }
                    ]
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_080",
                    "child_id": "work_180",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1076,
                    "changed_keys": [
                        "ui.main_menu.start_game",
                        "ui.main_menu.quit_game"
                    ],
                    "locales_processed": [
                        "fr",
                        "es"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Batch completed: ui.main_menu.start_game, ui.main_menu.quit_game [fr,es]",
                    "message": "Batch completed for fr,es for ui.main_menu.start_game, ui.main_menu.quit_game",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "4 translations recorded",
                "work items linked",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_077",
        "instruction": "Handle a need for timing adjustments for JA subtitle 'subtitle_007' (10.5\u201314.2s) linked to 'assets/subtitles/ja/level1_intro.vtt'. Your expected results: work_181 should be designated 'label_001'; a medium-priority JA-targeted timing entry is created with the asset path; a finished workflow for PR 1077 incorporates the required_timing details; and an info notification is dispatched to user_003. Rely exclusively on tool-generated IDs/timestamps.",
        "actions": [
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_181",
                    "label_name": "label_001"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "asset_path": "assets/subtitles/ja/level1_intro.vtt"
                    }
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1077,
                    "changed_keys": [
                        "subtitle_007"
                    ],
                    "locales_processed": [
                        "ja"
                    ],
                    "status": "completed",
                    "metadata": {
                        "required_timing": {
                            "id": "subtitle_007",
                            "start": 10.5,
                            "end": 14.2
                        }
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: subtitle_007 [ja]",
                    "message": "TMS job created for subtitle_007",
                    "recipient_id": "user_003",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "work item labeled",
                "tms_job created",
                "workflow completed with timing metadata",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_078",
        "instruction": "Coordinate the entire localization deployment for new feature string 'ui.feature.new_button' into Chinese. Achievements: a high-priority ZH task is logged; the ZH translation ('\u65b0\u529f\u80fd') is registered; work_081\u2192work_182 must be interlinked using link_type='relates_to' and work_182 is marked 'label_001'; a finalized workflow for PR 1078 must be present; and a notification confirms completion with the title='Localization completed: ui.feature.new_button [zh]' and message='Localization completed for zh for ui.feature.new_button'. Deploy only tool-generated IDs/timestamps. Translation entries should comprise solely: string_key, locale, target_string.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "zh"
                    ],
                    "priority": "high"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.feature.new_button",
                            "locale": "zh",
                            "target_string": "新功能"
                        }
                    ]
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_081",
                    "child_id": "work_182",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_182",
                    "label_name": "label_001"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1078,
                    "changed_keys": [
                        "ui.feature.new_button"
                    ],
                    "locales_processed": [
                        "zh"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Localization completed: ui.feature.new_button [zh]",
                    "message": "Localization completed for zh for ui.feature.new_button",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "translation recorded",
                "work_081→work_182 linked",
                "work_182 labeled",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_079",
        "instruction": "Initiate an investigation into a localization problem in 'src/game/engine/renderer.cpp'. Your measures of success include consulting the file ownership as read-only for that path, recording a high-priority DE investigation job with metadata.file_path='src/game/engine/renderer.cpp', linking work_082\u2192work_183 with link_type='relates_to', ensuring an in_progress workflow for PR 1079 that references changed_keys=['src/game/engine/renderer.cpp'] and locales_processed=['de'], and sending an info Slack notification to user_001 featuring title='Job queued: src/game/engine/renderer.cpp [de]' and message='TMS job created for src/game/engine/renderer.cpp'. Employ tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "getOwnershipForPath",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "file_path": "src/game/engine/renderer.cpp"
                    }
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_082",
                    "child_id": "work_183",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1079,
                    "changed_keys": [
                        "src/game/engine/renderer.cpp"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "status": "in_progress"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: src/game/engine/renderer.cpp [de]",
                    "message": "TMS job created for src/game/engine/renderer.cpp",
                    "recipient_id": "user_001",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "file ownership consulted",
                "investigation job created",
                "work items linked",
                "workflow created (in_progress)",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_080",
        "instruction": "Address a German main-menu UI overflow from commit 'bde222' by modifying 'ui.main_menu.quit_game' to 'Beenden'. Your success criteria: documenting a high-priority DE job with metadata.commit_sha='bde222', logging the DE translation, linking work_125\u2192work_225 with link_type='relates_to' and marking it with label_003, ensuring a completed workflow for PR 1080, and informing via Slack update about completion titled 'DE overflow fix applied: ui.main_menu.quit_game [de]' with message 'Text shortened to \"Beenden\" for ui.main_menu.quit_game (de).'. Use tool-generated IDs/timestamps exclusively. Translation entries must consist of: string_key, locale, target_string only.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "commit_sha": "bde222"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.quit_game",
                            "locale": "de",
                            "target_string": "Beenden"
                        }
                    ]
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_125",
                    "child_id": "work_225",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_225",
                    "label_name": "label_003"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1080,
                    "changed_keys": [
                        "ui.main_menu.quit_game"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "DE overflow fix applied: ui.main_menu.quit_game [de]",
                    "message": "Text shortened to \"Beenden\" for ui.main_menu.quit_game (de).",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "translation recorded",
                "work items linked and tagged",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_081",
        "instruction": "Handle a refresh of a French VO line for asset 'vo/fr/hero_intro_01.wav'. Required outcomes include: linking work_083\u2192work_184 (relates_to); creating a medium-priority FR VO job with the asset path; recording a new FR translation for 'vo.hero.intro_01' ('Le h\u00e9ros arrive.'); establishing a completed workflow for PR 1081; and sending an update notification to user_006. Utilize tool-generated IDs/timestamps only. Translation entries must comprise solely: string_key, locale, target_string.",
        "actions": [
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_083",
                    "child_id": "work_184",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "priority": "medium",
                    "target_locales": [
                        "fr"
                    ],
                    "metadata": {
                        "asset_path": "vo/fr/hero_intro_01.wav"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "vo.hero.intro_01",
                            "locale": "fr",
                            "target_string": "Le héros arrive."
                        }
                    ]
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1081,
                    "changed_keys": [
                        "vo.hero.intro_01"
                    ],
                    "locales_processed": [
                        "fr"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: vo.hero.intro_01 [fr]",
                    "message": "Validations passed for fr for vo.hero.intro_01",
                    "recipient_id": "user_006",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "work items linked",
                "tms_job created",
                "translation recorded",
                "workflow created",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_082",
        "instruction": "Coordinate a deterministic setup for a new Spanish localization job. For success: ensure a medium-priority ES job is created; a placeholder translation for 'ui.new_feature.title' ('[PLACEHOLDER]') is recorded (entry includes only string_key, locale, target_string); ensure work_090\u2192work_190 is linked with link_type='relates_to' and work_190 is tagged 'label_001'; confirm a completed workflow for PR 1082 exists; and an info notification is sent to user_007 using title='Job queued: ui.new_feature.title [es]' and message='TMS job created for ui.new_feature.title'. Employ tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "medium"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.new_feature.title",
                            "locale": "es",
                            "target_string": "[PLACEHOLDER]"
                        }
                    ]
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_090",
                    "child_id": "work_190",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_190",
                    "label_name": "label_001"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1082,
                    "changed_keys": [
                        "ui.new_feature.title"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.new_feature.title [es]",
                    "message": "TMS job created for ui.new_feature.title",
                    "recipient_id": "user_007",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "placeholder recorded",
                "work_090→work_190 linked",
                "work_190 labeled",
                "workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_083",
        "instruction": "Carry out a multi-language verification pass for 'ui.settings.audio' on ES/DE/FR within a pre-existing database. Your necessary outcomes are: review current strings for ES, DE, FR; mark validation as 'passed' for all three languages; list in one completed workflow for PR 1083; and dispatch a summary info notification to user_008. Only use tool-generated IDs/timestamps.",
        "actions": [
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de"
                },
            },
            {
                "name": "getLocString",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "fr"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "es",
                    "validation_status": "passed"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "de",
                    "validation_status": "passed"
                },
            },
            {
                "name": "updateLocaleValidation",
                "arguments": {
                    "string_key": "ui.settings.audio",
                    "locale": "fr",
                    "validation_status": "passed"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1083,
                    "changed_keys": [
                        "ui.settings.audio"
                    ],
                    "locales_processed": [
                        "es",
                        "de",
                        "fr"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Validations passed: ui.settings.audio [es,de,fr]",
                    "message": "Validations passed for es,de,fr for ui.settings.audio",
                    "recipient_id": "user_008",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "context captured for ES/DE/FR",
                "validation passed for ES/DE/FR",
                "workflow created",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_084",
        "instruction": "Handle a marketing-motivated update for the Japanese main title instigated by commit 'fab444'. Your needed outcomes are: a high-priority JA job with commit metadata is documented; the JA title for 'ui.main_menu.title' ('\u7a76\u6975\u306e\u5192\u967a') is noted (entry includes only string_key, locale, target_string); work_091\u2192work_191 is associated with link_type='relates_to'; there's a completed workflow for PR 1084; and an info notification to user_009 is sent using title='Job queued: ui.main_menu.title [ja]' and message='TMS job created for ui.main_menu.title'. Only use tool-generated IDs/timestamps.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja"
                    ],
                    "priority": "high",
                    "metadata": {
                        "commit_sha": "fab444"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.title",
                            "locale": "ja",
                            "target_string": "究極の冒険"
                        }
                    ]
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_091",
                    "child_id": "work_191",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1084,
                    "changed_keys": [
                        "ui.main_menu.title"
                    ],
                    "locales_processed": [
                        "ja"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.main_menu.title [ja]",
                    "message": "TMS job created for ui.main_menu.title",
                    "recipient_id": "user_009",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "translation recorded",
                "work items linked",
                "workflow created",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_085",
        "instruction": "Handle a CI-to-fix workflow addressing a Korean failure (build 'run_009', commit 'caf333'). Required outcomes include the creation of a high-priority KO job with CI metadata (build_run_id 'run_009', commit_sha 'caf333'); recording of the corrected KO string for 'ui.settings.video' ('\ube44\ub514\uc624') (the entry should only include string_key, locale, target_string); establishing a link from work_092 to work_192 with link_type='relates_to' and tagging work_192 with label_001; ensuring the existence of a completed workflow for PR 1085; and sending an update notification to user_010 to confirm validation using title='Validations passed: ui.settings.video [ko]' and message='Validations passed for ko for ui.settings.video'. Utilize tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ko"
                    ],
                    "priority": "high",
                    "metadata": {
                        "build_run_id": "run_009",
                        "commit_sha": "caf333"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.video",
                            "locale": "ko",
                            "target_string": "비디오"
                        }
                    ]
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_092",
                    "child_id": "work_192",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_192",
                    "label_name": "label_001"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1085,
                    "changed_keys": [
                        "ui.settings.video"
                    ],
                    "locales_processed": [
                        "ko"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Validations passed: ui.settings.video [ko]",
                    "message": "Validations passed for ko for ui.settings.video",
                    "recipient_id": "user_010",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "translation recorded",
                "work items linked and tagged",
                "workflow created",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_086",
        "instruction": "Coordinate the deprecation of legacy asset 'assets/ui/legacy_menu.json'. Ensure the system state indicates deprecation as follows (utilize tool-generated IDs/timestamps only): a relationship of type 'relates_to' exists from parent work_093 to child work_193; work_193 is tagged with label_004 ('Deprecation Candidate'); there is a medium-priority EN job with metadata.asset_path='assets/ui/legacy_menu.json'; a workflow for PR 1086 exists with status='deprecated' and changed_keys=['assets/ui/legacy_menu.json']; and an informational Slack notification was sent to user_012 with title='Asset deprecated: assets/ui/legacy_menu.json' and message='Deprecation logged for assets/ui/legacy_menu.json (PR 1086), see work_193.'.",
        "actions": [
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_093",
                    "child_id": "work_193",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_193",
                    "label_id": "label_004"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "en"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "asset_path": "assets/ui/legacy_menu.json"
                    }
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1086,
                    "changed_keys": [
                        "assets/ui/legacy_menu.json"
                    ],
                    "locales_processed": [],
                    "status": "deprecated"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Asset deprecated: assets/ui/legacy_menu.json",
                    "message": "Deprecation logged for assets/ui/legacy_menu.json (PR 1086), see work_193.",
                    "recipient_id": "user_012",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "work items linked",
                "work item tagged",
                "tms_job created",
                "workflow created",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_087",
        "instruction": "Handle a tone/nuance update for Japanese using commit 'ccc555'. Your required outcomes are: initiate a medium-priority JA job with metadata {'commit_sha':'ccc555'}; document JA for 'ui.main_menu.quit_game' as '\u30b2\u30fc\u30e0\u3092\u7d42\u4e86' (entries comprise only string_key, locale, target_string); finalize a completed workflow for PR 1087 with changed_keys=['ui.main_menu.quit_game']; and dispatch an update Slack notification to user_013 with title='Translation applied: ui.main_menu.quit_game [ja]' and message='Translation applied for ui.main_menu.quit_game (ja)'. Utilize tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "commit_sha": "ccc555"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.main_menu.quit_game",
                            "locale": "ja",
                            "target_string": "ゲームを終了"
                        }
                    ]
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1087,
                    "changed_keys": [
                        "ui.main_menu.quit_game"
                    ],
                    "locales_processed": [
                        "ja"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Translation applied: ui.main_menu.quit_game [ja]",
                    "message": "Translation applied for ui.main_menu.quit_game (ja)",
                    "recipient_id": "user_013",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "translation updated",
                "workflow created",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_088",
        "instruction": "Coordinate a new German localization job associated with CI build 'run_010'. The required outcomes are: initiate a medium-priority DE job with metadata {'build_run_id':'run_010'}; document a placeholder for 'ui.new_feature.confirm' as '[PLATZHALTER]' (entries comprise only string_key, locale, target_string); connect work_094\u2192work_194 with link_type='relates_to' and mark work_194 with label_001; finalize a completed workflow for PR 1088 with changed_keys=['ui.new_feature.confirm']; and send an info Slack notification to user_014 with title='Job queued: ui.new_feature.confirm [de]' and message='TMS job created for ui.new_feature.confirm'. Utilize tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "build_run_id": "run_010"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.new_feature.confirm",
                            "locale": "de",
                            "target_string": "[PLATZHALTER]"
                        }
                    ]
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_094",
                    "child_id": "work_194",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_194",
                    "label_id": "label_001"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1088,
                    "changed_keys": [
                        "ui.new_feature.confirm"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Job queued: ui.new_feature.confirm [de]",
                    "message": "TMS job created for ui.new_feature.confirm",
                    "recipient_id": "user_014",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "placeholder recorded",
                "work items linked and tagged",
                "workflow created",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_089",
        "instruction": "Handle a batch ES localization task for three settings strings. Your required outcomes: generate one medium-priority ES job; document translations for 'ui.settings.video' ('V\u00eddeo'), 'ui.settings.controls' ('Controles'), and 'ui.settings.gameplay' ('Jugabilidad') (entries should include only string_key, locale, target_string); finalize a completed workflow for PR 1089 with changed_keys=['ui.settings.video','ui.settings.controls','ui.settings.gameplay']; and distribute an info Slack notification to user_015 with title='Translations applied: ui.settings.video, ui.settings.controls, ui.settings.gameplay [es]' and message='Translations applied for es for ui.settings.video, ui.settings.controls, ui.settings.gameplay'. Utilize tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "medium"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.settings.video",
                            "locale": "es",
                            "target_string": "Vídeo"
                        },
                        {
                            "string_key": "ui.settings.controls",
                            "locale": "es",
                            "target_string": "Controles"
                        },
                        {
                            "string_key": "ui.settings.gameplay",
                            "locale": "es",
                            "target_string": "Jugabilidad"
                        }
                    ]
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1089,
                    "changed_keys": [
                        "ui.settings.video",
                        "ui.settings.controls",
                        "ui.settings.gameplay"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Translations applied: ui.settings.video, ui.settings.controls, ui.settings.gameplay [es]",
                    "message": "Translations applied for es for ui.settings.video, ui.settings.controls, ui.settings.gameplay",
                    "recipient_id": "user_015",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "3 translations recorded",
                "workflow created",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_090",
        "instruction": "Coordinate the processing of new cinematic subtitle text for asset 'assets/cinematics/level2_outro.mp4'. Your required outcomes: establish a medium-priority FR subtitle-text job with metadata {'asset_path':'assets/cinematics/level2_outro.mp4'}; record FR for 'vo.level2.outro_line1' as 'La bataille est gagn\u00e9e.' (entries should include only string_key, locale, target_string); associate work_196\u2192work_195 with link_type='relates_to'; and circulate an info Slack notification to user_001 with title='Text ready for timing: vo.level2.outro_line1 [fr]' and message='French text ready for timing for assets/cinematics/level2_outro.mp4 (vo.level2.outro_line1)'. Utilize tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "asset_path": "assets/cinematics/level2_outro.mp4"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "vo.level2.outro_line1",
                            "locale": "fr",
                            "target_string": "La bataille est gagnée."
                        }
                    ]
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_196",
                    "child_id": "work_195",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Text ready for timing: vo.level2.outro_line1 [fr]",
                    "message": "French text ready for timing for assets/cinematics/level2_outro.mp4 (vo.level2.outro_line1)",
                    "recipient_id": "user_001",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "translation recorded",
                "work items linked",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_091",
        "instruction": "Handle the deployment of new tooltip translations for Save in both Italian and Portuguese. Your required goals: generate a medium-priority IT/PT job with metadata {'component':'ui','subcomponent':'tooltips'}; catalog 'ui.tooltip.save' as 'Salva' (it) and 'Salvar' (pt) (entries should include only string_key, locale, target_string); associate work_095\u2192work_202 with link_type='relates_to' and tag work_202 with label_001; develop a concluded workflow for PR 1091 with changed_keys=['ui.tooltip.save']; and dispatch an informational Slack message to user_012 with title='Translations applied: ui.tooltip.save [it,pt]' and message='Translations applied for it,pt for ui.tooltip.save'. Utilize tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "it",
                        "pt"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "ui",
                        "subcomponent": "tooltips"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.tooltip.save",
                            "locale": "it",
                            "target_string": "Salva"
                        },
                        {
                            "string_key": "ui.tooltip.save",
                            "locale": "pt",
                            "target_string": "Salvar"
                        }
                    ]
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_095",
                    "child_id": "work_202",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_202",
                    "label_id": "label_001"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1091,
                    "changed_keys": [
                        "ui.tooltip.save"
                    ],
                    "locales_processed": [
                        "it",
                        "pt"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Translations applied: ui.tooltip.save [it,pt]",
                    "message": "Translations applied for it,pt for ui.tooltip.save",
                    "recipient_id": "user_012",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "it/pt translations recorded",
                "work items linked and tagged",
                "workflow created",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_092",
        "instruction": "Initiate remediation for the unsuccessful automation run 'automation_run_005' impacting German. Your objectives: establish a high-priority DE job with metadata {'automation_run_id':'automation_run_005'}; connect work_097\u2192work_197 with link_type='relates_to'; initiate a workflow for PR 1092 in the status 'in_progress' with changed_keys=[]; and issue an informational Slack notification to user_003 with title='Remediation started: automation_run_005 [de]' and message='Manual remediation for automation_run_005 has begun. See work_197.'. Use tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "automation_run_id": "automation_run_005"
                    }
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_097",
                    "child_id": "work_197",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1092,
                    "changed_keys": [],
                    "locales_processed": [
                        "de"
                    ],
                    "status": "in_progress"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Remediation started: automation_run_005 [de]",
                    "message": "Manual remediation for automation_run_005 has begun. See work_197.",
                    "recipient_id": "user_003",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "work items linked",
                "workflow created",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_093",
        "instruction": "Handle a dual-locale VO refresh for 'vo.generic.greeting'. Your required outcomes: establish one medium-priority FR/ES job; capture FR 'Bonjour.' and ES 'Hola.' (entries include only string_key, locale, target_string); construct a completed workflow for PR 1093 with changed_keys=['vo.generic.greeting']; and dispatch an information Slack notification to user_004 with title='VO refreshed: vo.generic.greeting [fr,es]' and message='VO refreshed for fr,es for vo.generic.greeting'. Use tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr",
                        "es"
                    ],
                    "priority": "medium"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "vo.generic.greeting",
                            "locale": "fr",
                            "target_string": "Bonjour."
                        },
                        {
                            "string_key": "vo.generic.greeting",
                            "locale": "es",
                            "target_string": "Hola."
                        }
                    ]
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1093,
                    "changed_keys": [
                        "vo.generic.greeting"
                    ],
                    "locales_processed": [
                        "fr",
                        "es"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "VO refreshed: vo.generic.greeting [fr,es]",
                    "message": "VO refreshed for fr,es for vo.generic.greeting",
                    "recipient_id": "user_004",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "FR/ES translations recorded",
                "workflow created",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_094",
        "instruction": "Coordinate the correction of a Japanese placeholder string from commit 'ddd666'. Your required outcomes: set up a medium-priority JA job with metadata {'commit_sha':'ddd666'}; log '{count} \u767a' for 'ui.hud.ammo_count' (entries include only string_key, locale, target_string); build a completed workflow for PR 1094 with changed_keys=['ui.hud.ammo_count']; and convey an info Slack notification to user_005 with title='Placeholder corrected: ui.hud.ammo_count [ja]' and message='Placeholder corrected for ui.hud.ammo_count (ja)'. Use tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "commit_sha": "ddd666"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.hud.ammo_count",
                            "locale": "ja",
                            "target_string": "{count} 発"
                        }
                    ]
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1094,
                    "changed_keys": [
                        "ui.hud.ammo_count"
                    ],
                    "locales_processed": [
                        "ja"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Placeholder corrected: ui.hud.ammo_count [ja]",
                    "message": "Placeholder corrected for ui.hud.ammo_count (ja)",
                    "recipient_id": "user_005",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "translation corrected",
                "workflow created",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_095",
        "instruction": "Handle the archival of the legacy KO string 'ui.legacy.button'. The required outcomes are: connect work_098 to work_198 using link_type='relates_to' and apply label_004 to work_198; establish a medium-priority KO job; organize a workflow for PR 1095 with the status 'pending_deprecation' and changed_keys=['ui.legacy.button']; and dispatch an informational Slack notification to user_006 with title='String marked for archival: ui.legacy.button [ko]' and message='Korean string ui.legacy.button marked for archival; see work_198.'. Ensure to use tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_098",
                    "child_id": "work_198",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_198",
                    "label_id": "label_004"
                },
            },
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ko"
                    ],
                    "priority": "medium"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1095,
                    "changed_keys": [
                        "ui.legacy.button"
                    ],
                    "locales_processed": [
                        "ko"
                    ],
                    "status": "pending_deprecation"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "String marked for archival: ui.legacy.button [ko]",
                    "message": "Korean string ui.legacy.button marked for archival; see work_198.",
                    "recipient_id": "user_006",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "work items linked",
                "work item tagged",
                "tms_job created",
                "workflow created",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_096",
        "instruction": "Conduct a critical deployment of the Spanish EULA update associated with asset 'assets/legal/eula_es.txt'. The required outcomes are: initiate a high-priority ES job with metadata {'asset_path':'assets/legal/eula_es.txt'}; document 'Acuerdo de licencia de usuario final actualizado.' for 'text.legal.eula' (entries are limited to string_key, locale, target_string); complete a workflow for PR 1096 with changed_keys=['text.legal.eula'] and metadata {'sensitivity':'high'}; and issue an update Slack notification to user_007 with title='Localization completed: text.legal.eula [es]' and message='Localization completed for es for text.legal.eula'. Ensure to use tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "es"
                    ],
                    "priority": "high",
                    "metadata": {
                        "asset_path": "assets/legal/eula_es.txt"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "text.legal.eula",
                            "locale": "es",
                            "target_string": "Acuerdo de licencia de usuario final actualizado."
                        }
                    ]
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1096,
                    "changed_keys": [
                        "text.legal.eula"
                    ],
                    "locales_processed": [
                        "es"
                    ],
                    "status": "completed",
                    "metadata": {
                        "sensitivity": "high"
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "update",
                    "title": "Localization completed: text.legal.eula [es]",
                    "message": "Localization completed for es for text.legal.eula",
                    "recipient_id": "user_007",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "legal text recorded",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_097",
        "instruction": "Handle the creation of DE subtitle text and document the necessary timing for subtitle_011 (vo.level5.warning). Your required outcomes: establish a medium-priority DE job with metadata {'component':'vo'}; log 'Achtung!' for 'vo.level5.warning' (entries include only string_key, locale, target_string); finalize a completed workflow for PR 1097 with changed_keys=['vo.level5.warning','subtitle_011'] and metadata {'required_timing':{'id':'subtitle_011','start':30.1,'end':31.5}}; and dispatch an info Slack notification to user_008 with title='Workflow completed with timing: vo.level5.warning [de]' and message='Timing 30.1\u201331.5s captured for subtitle_011 (vo.level5.warning).'. Ensure to use tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "de"
                    ],
                    "priority": "medium",
                    "metadata": {
                        "component": "vo"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "vo.level5.warning",
                            "locale": "de",
                            "target_string": "Achtung!"
                        }
                    ]
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1097,
                    "changed_keys": [
                        "vo.level5.warning",
                        "subtitle_011"
                    ],
                    "locales_processed": [
                        "de"
                    ],
                    "status": "completed",
                    "metadata": {
                        "required_timing": {
                            "id": "subtitle_011",
                            "start": 30.1,
                            "end": 31.5
                        }
                    }
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Workflow completed with timing: vo.level5.warning [de]",
                    "message": "Timing 30.1–31.5s captured for subtitle_011 (vo.level5.warning).",
                    "recipient_id": "user_008",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "translation recorded",
                "localization workflow completed with timing metadata",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_098",
        "instruction": "Coordinate a batch update of three French store item descriptions. Your required outcomes: initiate a medium-priority FR job; document FR strings for item.desc.sword ('Une \u00e9p\u00e9e tranchante.'), item.desc.shield ('Un bouclier robuste.'), and item.desc.potion ('Restaure la sant\u00e9.') (entries include only string_key, locale, target_string); connect work_099\u2192work_199 with link_type='relates_to'; complete a workflow for PR 1098 with changed_keys=['item.desc.sword','item.desc.shield','item.desc.potion']; and send an info Slack notification to user_009 with title='Translations applied: item.desc.sword,item.desc.shield,item.desc.potion [fr]' and message='Translations applied for fr for item.desc.sword,item.desc.shield,item.desc.potion'. Ensure to use tool-generated IDs/timestamps only.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "fr"
                    ],
                    "priority": "medium"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "item.desc.sword",
                            "locale": "fr",
                            "target_string": "Une épée tranchante."
                        },
                        {
                            "string_key": "item.desc.shield",
                            "locale": "fr",
                            "target_string": "Un bouclier robuste."
                        },
                        {
                            "string_key": "item.desc.potion",
                            "locale": "fr",
                            "target_string": "Restaure la santé."
                        }
                    ]
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_099",
                    "child_id": "work_199",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1098,
                    "changed_keys": [
                        "item.desc.sword",
                        "item.desc.shield",
                        "item.desc.potion"
                    ],
                    "locales_processed": [
                        "fr"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Translations applied: item.desc.sword,item.desc.shield,item.desc.potion [fr]",
                    "message": "Translations applied for fr for item.desc.sword,item.desc.shield,item.desc.potion",
                    "recipient_id": "user_009",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "3 translations recorded",
                "work_099→work_199 linked",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_099",
        "instruction": "Handle the enhancement of clarity for the Chinese error message 'error.connection.failed'. Your required outcomes: initiate a medium-priority ZH job; document '\u8fde\u63a5\u5931\u8d25\uff0c\u8bf7\u68c0\u67e5\u60a8\u7684\u7f51\u7edc\u3002' for 'error.connection.failed' (entries include only string_key, locale, target_string); tag work_201 with label_001; finalize a workflow for PR 1099 with changed_keys=['error.connection.failed']; and dispatch an info Slack notification to user_010 with title='Localization completed: error.connection.failed [zh]' and message='Localization completed for zh for error.connection.failed'. Utilize tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "zh"
                    ],
                    "priority": "medium"
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "error.connection.failed",
                            "locale": "zh",
                            "target_string": "连接失败，请检查您的网络。"
                        }
                    ]
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_201",
                    "label_id": "label_001"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1099,
                    "changed_keys": [
                        "error.connection.failed"
                    ],
                    "locales_processed": [
                        "zh"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Localization completed: error.connection.failed [zh]",
                    "message": "Localization completed for zh for error.connection.failed",
                    "recipient_id": "user_010",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "translation recorded",
                "work_201 tagged",
                "localization workflow completed",
                "notification sent"
        ]
    }
    ,
    {
        "annotator": dev_ops,
        "user_id": "V6_100",
        "instruction": "Coordinate a release-candidate localization workflow: CI build 'run_011' and commit 'eee777' necessitate a JA correction for 'ui.common.loading' ('\u30ed\u30fc\u30c9\u4e2d...'). Your required outcomes: initiate a high-priority JA/ES/DE job with metadata {'commit_sha':'eee777','build_run_id':'run_011'}; register the JA correction for 'ui.common.loading' ('\u30ed\u30fc\u30c9\u4e2d...') (entry includes only string_key, locale, target_string); connect work_100\u2192work_200 with link_type='relates_to' and tag work_200 with label_001; finalize a workflow for PR 1100 with changed_keys=['ui.common.loading']; and send an info Slack notification to user_011 with title='Localization completed: ui.common.loading [ja,es,de]' and message='Localization completed for ja,es,de for ui.common.loading'. Employ tool-generated IDs/timestamps exclusively.",
        "actions": [
            {
                "name": "createTmsJob",
                "arguments": {
                    "source_locale": "en",
                    "target_locales": [
                        "ja",
                        "es",
                        "de"
                    ],
                    "priority": "high",
                    "metadata": {
                        "commit_sha": "eee777",
                        "build_run_id": "run_011"
                    }
                },
            },
            {
                "name": "recordTranslations",
                "arguments": {
                    "entries": [
                        {
                            "string_key": "ui.common.loading",
                            "locale": "ja",
                            "target_string": "ロード中..."
                        }
                    ]
                },
            },
            {
                "name": "linkWorkItems",
                "arguments": {
                    "parent_id": "work_100",
                    "child_id": "work_200",
                    "link_type": "relates_to"
                },
            },
            {
                "name": "tagWorkItemWithLabel",
                "arguments": {
                    "work_item_id": "work_200",
                    "label_id": "label_001"
                },
            },
            {
                "name": "createLocalizationWorkflow",
                "arguments": {
                    "pr_number": 1100,
                    "changed_keys": [
                        "ui.common.loading"
                    ],
                    "locales_processed": [
                        "ja",
                        "es",
                        "de"
                    ],
                    "status": "completed"
                },
            },
            {
                "name": "sendNotification",
                "arguments": {
                    "notification_type": "info",
                    "title": "Localization completed: ui.common.loading [ja,es,de]",
                    "message": "Localization completed for ja,es,de for ui.common.loading",
                    "recipient_id": "user_011",
                    "channel": "slack"
                }
            }
        ],
        "outputs": [
                "tms_job created",
                "JA translation recorded",
                "work_100→work_200 linked and tagged",
                "localization workflow completed",
                "notification sent"
        ]
    }
]
