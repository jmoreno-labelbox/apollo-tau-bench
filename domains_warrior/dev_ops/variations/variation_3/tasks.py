from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="res_001",
        instruction=(
            "You are a triage engineer. A new crash event, 'crash_002', has been reported. Your task is to investigate this crash from 'Character Motion Rendering' project (proj_033), find the original bug ticket associated with its fingerprint, find the code owner for the module that crashed, and then assign the bug ticket to that owner. Finally, you must link the new crash event to the bug ticket with a 'duplicate' relationship, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="get_crash_event_details",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="find_work_item_by_crash_fingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="get_code_owner_for_module",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_002",
        instruction=(
            "You are a DevOps specialist. A build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_033) has failed after the last known good commit 'xyz789abc123def'. Your task is to perform a full triage. You need to identify the root cause of the failure and ensure a bug ticket is created with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket must be assigned to the Game Engine Platform Team lead, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_033",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_003",
        instruction=(
            "You are a reliability engineer. A build for commit 'abc123def456789' in the 'Game Engine Core Migration' project (proj_001) has failed with the issue signature 'issue: 'TextureManager::loadTexture' was not declared in this scope'. The last known good commit was 'xyz789abc123def'. Your task is to perform a full triage of this failure. If you determine that this is a recurring issue, your final bug report must include that information according to policy. You need to identify the root cause and ensure a critical-priority bug ticket is created with the title 'Recurring Compilation Failure: issue: 'TextureManager::loadTexture' was not declared in this scope' and the description 'Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents.'. The ticket must be assigned to the correct owner, and the appropriate notifications must be sent according to policy."
        ),
        actions=[
            Action(
                name="find_similar_incidents",
                kwargs={
                    "issue_signature": "issue: 'TextureManager::loadTexture' was not declared in this scope"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_001",
                    "item_type": "bug",
                    "title": "Recurring Compilation Failure: issue: 'TextureManager::loadTexture' was not declared in this scope",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "critical"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_004",
        instruction=(
            "You are a DevOps specialist. A build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_066) has failed after the last known good commit 'xyz789abc123def'. Your task is to perform a full triage. You need to identify the root cause of the failure and ensure a bug ticket is created with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket must be assigned to the Game Engine Platform Team lead, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_066",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_005",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_313). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_313",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_313",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_006",
        instruction=(
            "You are a triage engineer. A new crash event, 'crash_002', has been reported. Your task is to investigate this crash from 'Character Motion Rendering' project (proj_044), find the original bug ticket associated with its fingerprint, find the code owner for the module that crashed, and then assign the bug ticket to that owner. Finally, you must link the new crash event to the bug ticket with a 'duplicate' relationship, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="get_crash_event_details",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="find_work_item_by_crash_fingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="get_code_owner_for_module",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_007",
        instruction=(
            "You are a triage engineer. A new crash event, 'crash_002', has been reported. Your task is to investigate this crash from 'Character Motion Rendering' project (proj_077), find the original bug ticket associated with its fingerprint, find the code owner for the module that crashed, and then assign the bug ticket to that owner. Finally, you must link the new crash event to the bug ticket with a 'duplicate' relationship, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="get_crash_event_details",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="find_work_item_by_crash_fingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="get_code_owner_for_module",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_008",
        instruction=(
            "You are a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_505) has failed with a symbolication error related to symbol_003. Your task is to investigate the build run for commit 'ghi789def456abc', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_505",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_009",
        instruction=(
            "You are a DevOps specialist. A build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_433) has failed after the last known good commit 'xyz789abc123def'. Your task is to perform a full triage. You need to identify the root cause of the failure and ensure a bug ticket is created with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket must be assigned to the Game Engine Platform Team lead, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_433",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_010",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Network Security Enhancement' project (proj_757) with the localization string 'vo.hero.intro_14'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_14', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_757",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_757",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_011",
        instruction=(
            "You are a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_315) has failed with a symbolication error related to symbol_003. Your task is to investigate the build run for commit 'ghi789def456abc', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_315",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_012",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Epic Adventure Game' project (proj_021) with the localization string 'vo.hero.intro_01'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_01', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_021",
                    "job_name": "Integrate New VO Lines: hero_quest_01",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_01"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_021",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_013",
        instruction=(
            "You are a triage engineer. A new crash event, 'crash_002', has been reported. Your task is to investigate this crash from 'Character Motion Rendering' project (proj_055), find the original bug ticket associated with its fingerprint, find the code owner for the module that crashed, and then assign the bug ticket to that owner. Finally, you must link the new crash event to the bug ticket with a 'duplicate' relationship, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="get_crash_event_details",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="find_work_item_by_crash_fingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="get_code_owner_for_module",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_014",
        instruction=(
            "You are a localization specialist. The German translation for the string key 'ui.main_menu.start_game' has failed validation due to a text overflow issue. Your task is to initiate the standard remediation process for this type of failure. You must ensure the validation status is 'failed', otherwise update the status. If you find that the actual width of the German translation exceeds the defined max width for that string key, you must ensure a high-priority bug ticket is created in the 'Localization' project (proj_052) with the title 'Fix German Translation for Start Game Button' and the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. The ticket must be assigned to the lead of the Game Engine Platform Team, linked to the localization string, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_translation_by_key_and_locale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_052",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_015",
        instruction=(
            "You are a triage engineer. A new crash event, 'crash_002', has been reported. Your task is to investigate this crash from 'Character Motion Rendering' project (proj_066), find the original bug ticket associated with its fingerprint, find the code owner for the module that crashed, and then assign the bug ticket to that owner. Finally, you must link the new crash event to the bug ticket with a 'duplicate' relationship, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="get_crash_event_details",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="find_work_item_by_crash_fingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="get_code_owner_for_module",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_016",
        instruction=(
            "You are a DevOps specialist. A build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_533) has failed after the last known good commit 'xyz789abc123def'. Your task is to perform a full triage. You need to identify the root cause of the failure and ensure a bug ticket is created with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket must be assigned to the Game Engine Platform Team lead, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_533",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_017",
        instruction=(
            "You are a localization specialist. The French translation for the string key 'ui.main_menu.start_game' is grammatically incorrect. Your task is to create a high-priority bug report in the 'Localization' project (proj_021) for the Game Engine Platform Team lead with the title 'Fix Grammar in French Translation for ui.main_menu.start_game' and the description 'The French translation for 'ui.main_menu.start_game' contains a grammatical error and must be corrected.'. The ticket must be linked to the string key for tracking, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_translation_by_key_and_locale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "fr"
                },
            ),Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_021",
                    "item_type": "bug",
                    "title": "Fix Grammar in French Translation for ui.main_menu.start_game",
                    "description": "The French translation for 'ui.main_menu.start_game' contains a grammatical error and must be corrected."
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_018",
        instruction=(
            "You are a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_325) has failed with a symbolication error related to symbol_003. Your task is to investigate the build run for commit 'ghi789def456abc', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_325",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_019",
        instruction=(
            "You are a triage engineer. A new crash event, 'crash_002', has been reported. Your task is to investigate this crash from 'Character Motion Rendering' project (proj_099), find the original bug ticket associated with its fingerprint, find the code owner for the module that crashed, and then assign the bug ticket to that owner. Finally, you must link the new crash event to the bug ticket with a 'duplicate' relationship, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="get_crash_event_details",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="find_work_item_by_crash_fingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="get_code_owner_for_module",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_020",
        instruction=(
            "You are a reliability engineer. A build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_123) has failed with the issue signature 'issue: 'TextureManager::loadTexture' was not declared in this scope'. The last known good commit was 'xyz789abc123def'. Your task is to perform a full triage of this failure. If you determine that this is a recurring issue, your final bug report must include that information according to policy. You need to identify the root cause and ensure a critical-priority bug ticket is created with the title 'Recurring Compilation Failure: issue: 'TextureManager::loadTexture' was not declared in this scope' and the description 'Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents.'. The ticket must be assigned to the correct owner, and the appropriate notifications must be sent according to policy."
        ),
        actions=[
            Action(
                name="find_similar_incidents",
                kwargs={
                    "issue_signature": "issue: 'TextureManager::loadTexture' was not declared in this scope"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_123",
                    "item_type": "bug",
                    "title": "Recurring Compilation Failure: issue: 'TextureManager::loadTexture' was not declared in this scope",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "critical"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_021",
        instruction=(
            "You are a DevOps specialist. A build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_044) has failed after the last known good commit 'xyz789abc123def'. Your task is to perform a full triage. You need to identify the root cause of the failure and ensure a bug ticket is created with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket must be assigned to the Game Engine Platform Team lead, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_044",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_022",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_613). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_613",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_613",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_023",
        instruction=(
            "You are a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_005) has failed with a symbolication error related to symbol_005. Your task is to investigate the build run for commit 'ghi789def456abc', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_005). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_005"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_005",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_005). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_024",
        instruction=(
            "You are a DevOps specialist. A build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_055) has failed after the last known good commit 'xyz789abc123def'. Your task is to perform a full triage. You need to identify the root cause of the failure and ensure a bug ticket is created with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket must be assigned to the Game Engine Platform Team lead, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_055",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_025",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_623). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_623",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_623",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_026",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Epic Adventure Game' project (proj_131) with the localization string 'vo.hero.intro_01'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_01', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked it to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_131",
                    "job_name": "Integrate New VO Lines: hero_quest_01",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_01"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_131",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_027",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_203). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_203",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_203",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_028",
        instruction=(
            "You are a reliability engineer. A build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_023) has failed with the issue signature 'issue: 'TextureManager::loadTexture' was not declared in this scope'. The last known good commit was 'xyz789abc123def'. Your task is to perform a full triage of this failure. If you determine that this is a recurring issue, your final bug report must include that information according to policy. You need to identify the root cause and ensure a critical-priority bug ticket is created with the title 'Recurring Compilation Failure: issue: 'TextureManager::loadTexture' was not declared in this scope' and the description 'Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents.'. The ticket must be assigned to the correct owner, and the appropriate notifications must be sent according to policy."
        ),
        actions=[
            Action(
                name="find_similar_incidents",
                kwargs={
                    "issue_signature": "issue: 'TextureManager::loadTexture' was not declared in this scope"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_023",
                    "item_type": "bug",
                    "title": "Recurring Compilation Failure: issue: 'TextureManager::loadTexture' was not declared in this scope",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "critical"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_029",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Epic Adventure Game' project (proj_141) with the localization string 'vo.hero.intro_01'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_01', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_141",
                    "job_name": "Integrate New VO Lines: hero_quest_01",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_01"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_141",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_030",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_213). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_213",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_213",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_031",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Edge Computing Platform' project (proj_020) with the localization string 'vo.hero.intro_02'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_02', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_020",
                    "job_name": "Integrate New VO Lines: hero_quest_02",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_02"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_020",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_032",
        instruction=(
            "You are a triage engineer. A new crash event, 'crash_002', has been reported. Your task is to investigate this crash from 'Character Motion Rendering' project (proj_055), find the original bug ticket associated with its fingerprint, find the code owner for the module that crashed, and then assign the bug ticket to that owner. Finally, you must link the new crash event to the bug ticket with a 'duplicate' relationship, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="get_crash_event_details",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="find_work_item_by_crash_fingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="get_code_owner_for_module",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_033",
        instruction=(
            "You are a DevOps specialist. A build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_633) has failed after the last known good commit 'xyz789abc123def'. Your task is to perform a full triage. You need to identify the root cause of the failure and ensure a bug ticket is created with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket must be assigned to the Game Engine Platform Team lead, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_633",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_034",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Database Infrastructure Upgrade' project (proj_006) with the localization string 'vo.hero.intro_15'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_15', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_006",
                    "job_name": "Integrate New VO Lines: hero_quest_15",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_15"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_006",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_035",
        instruction=(
            "You are a triage engineer. A new crash event, 'crash_002', has been reported. Your task is to investigate this crash from 'Character Motion Rendering' project (proj_066), find the original bug ticket associated with its fingerprint, find the code owner for the module that crashed, and then assign the bug ticket to that owner. Finally, you must link the new crash event to the bug ticket with a 'duplicate' relationship, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="get_crash_event_details",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="find_work_item_by_crash_fingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="get_code_owner_for_module",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_036",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Green Computing Initiative' project (proj_019) with the localization string 'vo.hero.intro_02'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_03', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_019",
                    "job_name": "Integrate New VO Lines: hero_quest_03",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_02"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_019",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_037",
        instruction=(
            "You are a DevOps specialist. A build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_661) has failed after the last known good commit 'xyz789abc123def'. Your task is to perform a full triage. You need to identify the root cause of the failure and ensure a bug ticket is created with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket must be assigned to the Game Engine Platform Team lead, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_661",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_038",
        instruction=(
            "You are a reliability manager. A critical, release-blocking build failure has occurred for commit 'abc123def456789' in the 'Game Engine Core Migration' project (proj_031) after the last known good commit 'xyz789abc123def'. The failure has the issue signature 'issue: 'TextureManager::loadTexture' was not declared in this scope'. Your task is to perform a full, in-depth triage and initiate the remediation process. You need to identify the root cause, determine if this is a recurring issue, and provide the development team with a detailed analysis. After your investigation, you must create a critical-priority bug ticket with the title 'CRITICAL: Release Blocker - Build Failure in Game Engine' and a description summarizing your findings: 'Critical build failure for commit 'abc123def456789' is blocking a major patch deployment. Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents.'. To verify any related assets, you'd want to create a separate high-prioity task for the Game Engine Platform Team lead, with the title 'Verify Asset Integrity After Renderer Fix' and the description 'The renderer fix in work_028 may affect texture loading. Please verify that the asset 'asset_011' is still rendering correctly.'. You also want to create a compliance record for the incident with the details; compliance_type 'incident_response', requirement 'critical_build_failure_triage', status 'in_progress', and details 'Triage for critical build failure 'run_001' is in progress. See bug 'work_028' for details.'. The record must be assigned to Game Engine Platform Team lead and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="find_similar_incidents",
                kwargs={
                    "issue_signature": "issue: 'TextureManager::loadTexture' was not declared in this scope"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_031",
                    "item_type": "bug",
                    "title": "CRITICAL: Release Blocker - Build Failure in Game Engine",
                    "description": "Critical build failure for commit 'abc123def456789' is blocking a major patch deployment. Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents."
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "critical"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_031",
                    "item_type": "task",
                    "title": "Verify Asset Integrity After Renderer Fix",
                    "description": "The renderer fix in work_028 may affect texture loading. Please verify that the asset 'asset_011' is still rendering correctly."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_029",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "work_029",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_compliance_record",
                kwargs={
                    "project_id": "proj_031",
                    "compliance_type": "incident_response",
                    "requirement": "critical_build_failure_triage",
                    "status": "in_progress",
                    "details": "Triage for critical build failure 'run_001' is in progress. See bug 'work_028' for details.",
                    "assignee_id": "user_001"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "compliance_013"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_014"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_039",
        instruction=(
            "You are a triage engineer. A critical crash event, 'crash_002', has been reported. Your task is to investigate this crash, find the original bug ticket associated with its fingerprint, find the code owner for the module that crashed, and then assign the bug ticket to that owner. Finally, you must link the new crash event to the bug ticket with a 'duplicate' relationship, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="get_crash_event_details",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="find_work_item_by_crash_fingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="get_code_owner_for_module",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_040",
        instruction=(
            "You are a build manager. The nightly build for the 'Database Infrastructure Upgrade' project (proj_006) has failed with a symbolication error related to symbol_007. Your task is to investigate the build run for commit 'jkl012ghi789def', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit jkl012ghi789def failed due to missing symbols (symbol_007). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "jkl012ghi789def"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_007"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_006",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit jkl012ghi789def failed due to missing symbols (symbol_007). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_006",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_041",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Data Pipeline Optimization' project (proj_018) with the localization string 'vo.hero.intro_03'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_03', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_018",
                    "job_name": "Integrate New VO Lines: hero_quest_03",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_03"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_018",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_042",
        instruction=(
            "You are a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_335) has failed with a symbolication error related to symbol_003. Your task is to investigate the build run for commit 'ghi789def456abc', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_335",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_043",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Network Security Enhancement' project (proj_747) with the localization string 'vo.hero.intro_14'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_14', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_747",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_747",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_044",
        instruction=(
            "You are a DevOps specialist. A build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_662) has failed after the last known good commit 'xyz789abc123def'. Your task is to perform a full triage. You need to identify the root cause of the failure and ensure a bug ticket is created with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket must be assigned to the Game Engine Platform Team lead, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_662",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_045",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Network Security Enhancement' project (proj_454) with the localization string 'vo.hero.intro_14'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_14', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_454",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_454",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_046",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_04' has been recorded for the 'Data Pipeline Optimization' project (proj_017). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_04' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_017",
                    "job_name": "Integrate New VO Lines: hero_quest_04",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_04"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_017",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_047",
        instruction=(
            "You are a DevOps specialist. A build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_833) has failed after the last known good commit 'xyz789abc123def'. Your task is to perform a full triage. You need to identify the root cause of the failure and ensure a bug ticket is created with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket must be assigned to the Game Engine Platform Team lead, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_833",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_048",
        instruction=(
            "You are a triage engineer. A significant crash event, 'crash_002', has been reported. Your task is to investigate this crash, find the original bug ticket associated with its fingerprint, find the code owner for the module that crashed, and then assign the bug ticket to that owner. Finally, you must link the new crash event to the bug ticket with a 'duplicate' relationship."
        ),
        actions=[
            Action(
                name="get_crash_event_details",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="find_work_item_by_crash_fingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="get_code_owner_for_module",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_049",
        instruction=(
            "You are a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_355) has failed with a symbolication error related to symbol_003. Your task is to investigate the build run for commit 'ghi789def456abc', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_355",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_050",
        instruction=(
            "You are a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_005) has failed with a symbolication error related to symbol_007. Your task is to investigate the build run for commit 'ghi789def456abc', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_007). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_007"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_005",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_007). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_051",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Legacy System Modernization' project (proj_016) with the localization string 'vo.hero.intro_05'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_05', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.', and link it to the new TMS job."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_016",
                    "job_name": "Integrate New VO Lines: hero_quest_05",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_05"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_016",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_052",
        instruction=(
            "You are a localization specialist. The German translation for the string key 'ui.main_menu.start_game' has failed validation due to a text overflow issue. Your task is to initiate the standard remediation process for this type of failure. You must ensure the validation status is 'failed', otherwise update the status. If you find that the actual width of the German translation exceeds the defined max width for that string key, you must ensure a high-priority bug ticket is created in the 'Localization' project (proj_064) with the title 'Fix German Translation for Start Game Button' and the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. The ticket must be assigned to the lead of the Game Engine Platform Team, linked to the localization string, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_translation_by_key_and_locale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_064",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_053",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_643). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_643",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_643",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_054",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Game Security & Anti-Cheat Framework' project (proj_004) with the localization string 'vo.hero.intro_17'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_17', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_004",
                    "job_name": "Integrate New VO Lines: hero_quest_17",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_17"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_004",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_055",
        instruction=(
            "You are a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_005) has failed with a symbolication error related to symbol_008. Your task is to investigate the build run for commit 'ghi789def456abc', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_008). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_008"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_005",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_008). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_056",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_06' has been recorded for the 'Automated Testing Infrastructure' project (proj_015). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_06' related to the project, add the new string key. Otherwise, you must create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_015",
                    "job_name": "Integrate New VO Lines: hero_quest_06",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_06"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_015",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_057",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_543). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_543",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_543",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_058",
        instruction=(
            "You are a localization specialist. The German translation for the string key 'ui.main_menu.start_game' has failed validation due to a text overflow issue. Your task is to initiate the standard remediation process for this type of failure. You must ensure the validation status is 'failed', otherwise update the status. If you find that the actual width of the German translation exceeds the defined max width for that string key, you must ensure a high-priority bug ticket is created in the 'Localization' project (proj_073) with the title 'Fix German Translation for Start Game Button' and the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. The ticket must be assigned to the lead of the Game Engine Platform Team, linked to the localization string, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_translation_by_key_and_locale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_073",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_059",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_747). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_747",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_747",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_060",
        instruction=(
            "You are a DevOps specialist. A build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_933) has failed after the last known good commit 'xyz789abc123def'. Your task is to perform a full triage. You need to identify the root cause of the failure and ensure a bug ticket is created with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket must be assigned to the Game Engine Platform Team lead, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="run_git_bisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_933",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_061",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Container Registry Security' project (proj_014) with the localization string 'vo.hero.intro_07'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_07', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_014",
                    "job_name": "Integrate New VO Lines: hero_quest_07",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_07"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_014",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_062",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_810). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_810",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_810",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_063",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_813). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_813",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_813",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_064",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_003). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_003",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_003",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_065",
        instruction=(
            "You are a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_365) has failed with a symbolication error related to symbol_003. Your task is to investigate the build run for commit 'ghi789def456abc', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_365",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_066",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Network Security Enhancement' project (proj_737) with the localization string 'vo.hero.intro_14'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_14', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_737",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_737",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_067",
        instruction=(
            "You are a localization specialist. The German translation for the string key 'ui.main_menu.start_game' has failed validation due to a text overflow issue. Your task is to initiate the standard remediation process for this type of failure. You must ensure the validation status is 'failed', otherwise update the status. If you find that the actual width of the German translation exceeds the defined max width for that string key, you must ensure a high-priority bug ticket is created in the 'Localization' project (proj_085) with the title 'Fix German Translation for Start Game Button' and the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. The ticket must be assigned to the lead of the Game Engine Platform Team, linked to the localization string, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_translation_by_key_and_locale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_085",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_068",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_903). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_903",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_903",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_069",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Network Security Enhancement' project (proj_444) with the localization string 'vo.hero.intro_14'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_14', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_444",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_444",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_070",
        instruction=(
            "You are a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_005) has failed with a symbolication error related to symbol_004. Your task is to investigate the build run for commit 'ghi789def456abc', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_004). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_004"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_005",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_004). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_071",
        instruction=(
            "You are a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_375) has failed with a symbolication error related to symbol_003. Your task is to investigate the build run for commit 'ghi789def456abc', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_375",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_072",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_902). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_902",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_902",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_073",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_347). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_347",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_347",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_074",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_19' has been recorded for the 'Game Build Pipeline Modernization' project (proj_002). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_19' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_002",
                    "job_name": "Integrate New VO Lines: hero_quest_19",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_19"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_002",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_075",
        instruction=(
            "You are a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_005) has failed with a symbolication error related to symbol_003. Your task is to investigate the build run for commit 'ghi789def456abc', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_005",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_076",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Network Security Enhancement' project (proj_434) with the localization string 'vo.hero.intro_14'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_14', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_434",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_434",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_077",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_653). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_653",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_653",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_078",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_901). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_901",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_901",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_079",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Epic Adventure Game' project (proj_161) with the localization string 'vo.hero.intro_01'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_01', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_161",
                    "job_name": "Integrate New VO Lines: hero_quest_01",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_01"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_161",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_080",
        instruction=(
            "You are a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_005) has failed with a symbolication error related to symbol_002. Your task is to investigate the build run for commit 'ghi789def456abc', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_002). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_002"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_005",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_002). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_081",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Network Security Enhancement' project (proj_424) with the localization string 'vo.hero.intro_14'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_14', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_424",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_424",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_082",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Network Security Enhancement' project (proj_727) with the localization string 'vo.hero.intro_14'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_14', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_727",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_727",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_083",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_663). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_663",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_663",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_084",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Game Engine Core Migration' project (proj_001) with the localization string 'vo.hero.intro_20'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_20', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_001",
                    "job_name": "Integrate New VO Lines: hero_quest_20",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_20"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_001",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_085",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_673). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_673",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_673",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_086",
        instruction=(
            "You are a localization specialist. The German translation for the string key 'ui.main_menu.start_game' has failed validation due to a text overflow issue. Your task is to initiate the standard remediation process for this type of failure. You must ensure the validation status is 'failed', otherwise update the status. If you find that the actual width of the German translation exceeds the defined max width for that string key, you must ensure a high-priority bug ticket is created in the 'Localization' project (proj_864) with the title 'Fix German Translation for Start Game Button' and the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. The ticket must be assigned to the lead of the Game Engine Platform Team, linked to the localization string, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_translation_by_key_and_locale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_864",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_087",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Epic Adventure Game' project (proj_181) with the localization string 'vo.hero.intro_01'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_01', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_181",
                    "job_name": "Integrate New VO Lines: hero_quest_01",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_01"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_181",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_088",
        instruction=(
            "You are a localization specialist. The German translation for the string key 'ui.main_menu.start_game' has failed validation due to a text overflow issue. Your task is to initiate the standard remediation process for this type of failure. You must ensure the validation status is 'failed', otherwise update the status. If you find that the actual width of the German translation exceeds the defined max width for that string key, you must ensure a high-priority bug ticket is created in the 'Localization' project (proj_118) with the title 'Fix German Translation for Start Game Button' and the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. The ticket must be assigned to the lead of the Game Engine Platform Team, linked to the localization string, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_translation_by_key_and_locale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_118",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_089",
        instruction=(
            "You are a localization specialist. The German translation for the string key 'ui.main_menu.start_game' has failed validation due to a text overflow issue. Your task is to initiate the standard remediation process for this type of failure. You must ensure the validation status is 'failed', otherwise update the status. If you find that the actual width of the German translation exceeds the defined max width for that string key, you must ensure a high-priority bug ticket is created in the 'Localization' project (proj_854) with the title 'Fix German Translation for Start Game Button' and the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. The ticket must be assigned to the lead of the Game Engine Platform Team, linked to the localization string, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_translation_by_key_and_locale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_854",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_090",
        instruction=(
            "You are a localization specialist. The German translation for the string key 'ui.main_menu.start_game' has failed validation due to a text overflow issue. Your task is to initiate the standard remediation process for this type of failure. You must ensure the validation status is 'failed', otherwise update the status. If you find that the actual width of the German translation exceeds the defined max width for that string key, you must ensure a high-priority bug ticket is created in the 'Localization' project (proj_844) with the title 'Fix German Translation for Start Game Button' and the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. The ticket must be assigned to the lead of the Game Engine Platform Team, linked to the localization string, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_translation_by_key_and_locale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_844",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_091",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_13' has been recorded for the 'Developer Portal' project (proj_008). Your task is to ensure these lines are integrated into the French and German localization pipelines. When there is an existing tms job named 'Integrate New VO Lines: hero_quest_13' related to the project, add the new string key. Otherwise, create a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="list_tms_jobs",
                kwargs={},
            ),
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_008",
                    "job_name": "Integrate New VO Lines: hero_quest_13",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_13"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_008",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_092",
        instruction=(
            "You are a localization specialist. The German translation for the string key 'ui.main_menu.start_game' has failed validation due to a text overflow issue. Your task is to initiate the standard remediation process for this type of failure. You must ensure the validation status is 'failed', otherwise update the status. If you find that the actual width of the German translation exceeds the defined max width for that string key, you must ensure a high-priority bug ticket is created in the 'Localization' project (proj_031) with the title 'Fix German Translation for Start Game Button' and the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. The ticket must be assigned to the lead of the Game Engine Platform Team, linked to the localization string, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_translation_by_key_and_locale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_031",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_093",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Network Security Enhancement' project (proj_707) with the localization string 'vo.hero.intro_14'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_14', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_707",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_707",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_094",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Network Security Enhancement' project (proj_717) with the localization string 'vo.hero.intro_14'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_14', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_717",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_717",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_095",
        instruction=(
            "You are a build manager. The nightly build for the 'Asset Bundle Validation' project (proj_078) has failed with a symbolication error related to symbol_008. Your task is to investigate the build run for commit 'ghi789def456abc', find the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to investigate the symbol generation process, and link the task to the failed build run. The task should have the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_008). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="find_build_run",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="get_symbol_bundle_details",
                kwargs={
                    "symbol_id": "symbol_008"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_078",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_008). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_096",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Network Security Enhancement' project (proj_007) with the localization string 'vo.hero.intro_14'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_14', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_007",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_007",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_097",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Epic Adventure Game' project (proj_521) with the localization string 'vo.hero.intro_01'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_01', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_521",
                    "job_name": "Integrate New VO Lines: hero_quest_01",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_01"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_521",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_098",
        instruction=(
            "You are a triage engineer. A new crash event, 'crash_002', has been reported. Your task is to investigate this crash from 'Character Motion Rendering' project (proj_088), find the original bug ticket associated with its fingerprint, find the code owner for the module that crashed, and then assign the bug ticket to that owner. Finally, you must link the new crash event to the bug ticket with a 'duplicate' relationship, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="get_crash_event_details",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="find_work_item_by_crash_fingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="get_code_owner_for_module",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_099",
        instruction=(
            "You are a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Epic Adventure Game' project (proj_421) with the localization string 'vo.hero.intro_01'. Your task is to create a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_01', targeting French and German. You must then create a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be linked to the new TMS job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="create_tms_job",
                kwargs={
                    "project_id": "proj_421",
                    "job_name": "Integrate New VO Lines: hero_quest_01",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_01"]
                }
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_421",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="res_100",
        instruction=(
            "You are a localization specialist. The German translation for the string key 'ui.main_menu.start_game' has failed validation due to a text overflow issue. Your task is to initiate the standard remediation process for this type of failure. You must ensure the validation status is 'failed', otherwise update the status. If you find that the actual width of the German translation exceeds the defined max width for that string key, you must ensure a high-priority bug ticket is created in the 'Localization' project (proj_043) with the title 'Fix German Translation for Start Game Button' and the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. The ticket must be assigned to the lead of the Game Engine Platform Team, linked to the localization string, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="find_translation_by_key_and_locale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),
            Action(
                name="find_team_by_name",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="create_work_item",
                kwargs={
                    "project_id": "proj_043",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="update_work_item",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="link_work_items",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="create_notification_record",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="post_slack_message",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[],
    ),
]
