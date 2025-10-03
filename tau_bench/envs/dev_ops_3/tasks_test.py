from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="res_001",
        instruction=(
            "As a triage engineer, a new crash event, 'crash_002', has been reported. Your responsibility is to examine this crash from 'Character Motion Rendering' project (proj_033), locate the original bug ticket related to its fingerprint, determine the code owner for the module that encountered the crash, and assign the bug ticket to that individual. Lastly, you need to connect the new crash event to the bug ticket with a 'duplicate' relationship, following the notification policy."
        ),
        actions=[
            Action(
                name="GetCrashEventDetails",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="FindWorkItemByCrashFingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="GetCodeOwnerForModule",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_002",
        instruction=(
            "As a DevOps specialist, a build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_033) has failed subsequent to the last known good commit 'xyz789abc123def'. Your task is to execute a comprehensive triage. You must uncover the root cause of the failure and make sure a bug ticket is established with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket should be assigned to the Game Engine Platform Team lead, following the notification policy."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_033",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_003",
        instruction=(
            "As a reliability engineer, handle a full triage for the build failure of commit 'abc123def456789' in the 'Game Engine Core Migration' project (proj_001) with the issue signature 'issue: 'TextureManager::loadTexture' was not declared in this scope'. The previous successful commit was 'xyz789abc123def'. Determine if this is a recurring problem and include that detail in your final bug report following policy. Identify the root cause and ensure creation of a critical-priority bug ticket titled 'Recurring Compilation Failure: issue: 'TextureManager::loadTexture' was not declared in this scope'. The description should state 'Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents.'. Assign the ticket to the correct owner and follow policy for sending the necessary notifications."
        ),
        actions=[
            Action(
                name="FindSimilarIncidents",
                kwargs={
                    "issue_signature": "issue: 'TextureManager::loadTexture' was not declared in this scope"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_001",
                    "item_type": "bug",
                    "title": "Recurring Compilation Failure: issue: 'TextureManager::loadTexture' was not declared in this scope",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "critical"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_004",
        instruction=(
            "As a DevOps specialist, coordinate a comprehensive triage for the failed build of commit 'abc123def456789' within the 'Game Texture Loading' project (proj_066) after the latest good commit 'xyz789abc123def'. Your duty is to uncover the failure's root cause and ensure a bug ticket is created, titled 'Build Failure Investigation for run_001'. The description must be 'Bisect identified 'abc123def456789' as the first bad commit.'. This ticket should be assigned to the Game Engine Platform Team lead, and ensure compliance with the notification policy."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_066",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_005",
        instruction=(
            "As a localization manager, a fresh batch of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_313). Your duty is to make sure these lines are incorporated into the French and German localization workflows. If there is already a tms job named 'Integrate New VO Lines: hero_quest_18' associated with the project, include the new string key. If not, initiate a new TMS job and create a high-priority tracking ticket titled 'Track TMS Job for New Strings' with the description 'Tracking TMS job for new string translation.'. The ticket needs to be assigned to the Game Engine Platform Team lead, linked to the tms job, and must comply with the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_313",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_313",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_006",
        instruction=(
            "As a triage engineer, a new crash event, 'crash_002', has been reported. Your responsibility is to analyze this crash from the 'Character Motion Rendering' project (proj_044), identify the original bug ticket associated with its fingerprint, locate the code owner for the module that malfunctioned, and then allocate the bug ticket to that owner. Finally, you should connect the new crash event to the bug ticket with a 'duplicate' relationship, and follow the notification policy."
        ),
        actions=[
            Action(
                name="GetCrashEventDetails",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="FindWorkItemByCrashFingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="GetCodeOwnerForModule",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_007",
        instruction=(
            "As a triage engineer, your responsibility includes handling a newly reported crash event, 'crash_002'. This involves examining the crash within the 'Character Motion Rendering' project (proj_077), identifying the original bug ticket linked to its fingerprint, determining the code owner for the affected module, and assigning the bug ticket to that owner. You should also connect the new crash event to the bug ticket, marking it as a 'duplicate', while following the notification policy."
        ),
        actions=[
            Action(
                name="GetCrashEventDetails",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="FindWorkItemByCrashFingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="GetCodeOwnerForModule",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_008",
        instruction=(
            "Your role as a build manager involves managing issues like the recent nightly build failure for the 'Game Analytics & Telemetry Platform' project (proj_505) caused by a symbolication error with symbol_003. You need to review the build run related to commit 'ghi789def456abc', locate the absent symbol bundle, create a task of high priority for the Game Engine Platform Team to explore the symbol generation issue, and ensure the task is associated with the failed build run. The task must be titled 'Missing Symbols in Nightly AI Build' and detailed with 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_505",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_009",
        instruction=(
            "You are a DevOps specialist. A build for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_433) has experienced failure following the last successful commit 'xyz789abc123def'. Handle a comprehensive triage. Determine the root cause of the failure and ensure a bug ticket is created with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. Ensure the ticket is assigned to the Game Engine Platform Team lead, complying with the notification policy."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_433",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_010",
        instruction=(
            "You are a localization manager. A fresh set of voice-over lines has been recorded needing integration into the 'Network Security Enhancement' project (proj_757) with the localization string 'vo.hero.intro_14'. Coordinate the creation of a new TMS job for these lines named 'Integrate New VO Lines: hero_quest_14', aimed at French and German. Subsequently, generate a high-priority tracking ticket for the Game Engine Platform Team lead titled 'Track TMS Job for New Strings' and described as 'Tracking TMS job for new string translation.'. Link the ticket to the new TMS job, adhering to the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_757",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_757",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_011",
        instruction=(
            "As a build manager, your role involves dealing with the issue of the nightly build for the 'Game Analytics & Telemetry Platform' project (proj_315) which encountered a failure due to a symbolication error involving symbol_003. Your responsibility is to scrutinize the build run corresponding to commit 'ghi789def456abc', locate the missing symbol bundle, and organize a high-priority task for the Game Engine Platform Team to delve into the symbol generation process, ensuring the task is linked to the failed build run. The task should be titled 'Missing Symbols in Nightly AI Build' with the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_315",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_012",
        instruction=(
            "In your capacity as a localization manager, you are handling a set of newly recorded voice-over lines that need integration into the 'Epic Adventure Game' project (proj_021) using the localization string 'vo.hero.intro_01'. Your assignment is to generate a new TMS job for these lines, titled 'Integrate New VO Lines: hero_quest_01', with a focus on French and German. Following this, establish a high-priority tracking ticket for the Game Engine Platform Team lead titled 'Track TMS Job for New Strings' with the description 'Tracking TMS job for new string translation.'. This ticket needs to be linked to the new TMS job and comply with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_021",
                    "job_name": "Integrate New VO Lines: hero_quest_01",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_01"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_021",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_013",
        instruction=(
            "You work as a triage engineer. A new incident, 'crash_002', has been logged. Your responsibility is to analyze this crash from the 'Character Motion Rendering' project (proj_055), identify the original bug ticket using its fingerprint, determine the code owner for the crashed module, and then assign that bug ticket to the identified code owner. Next, you must relate the new crash event to the bug ticket with a 'duplicate' status, all while following the notification policy."
        ),
        actions=[
            Action(
                name="GetCrashEventDetails",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="FindWorkItemByCrashFingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="GetCodeOwnerForModule",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_014",
        instruction=(
            "You serve as a localization specialist. The German translation for the string key 'ui.main_menu.start_game' has a validation issue due to text overflow. Your responsibility is to launch the standard remediation procedure for this type of issue. Ensure that the validation status remains 'failed'; if not, update it. If the actual width of the German translation surpasses the designated max width for the string key, it is crucial to open a high-priority bug ticket under the 'Localization' project (proj_052) titled 'Fix German Translation for Start Game Button', with the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. This ticket needs to be assigned to the Game Engine Platform Team lead, linked to the localization string, and comply with the notification policy."
        ),
        actions=[
            Action(
                name="FindTranslationByKeyAndLocale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_052",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_015",
        instruction=(
            "As a triage engineer, a new crash event labeled 'crash_002' has been logged. Your responsibility is to examine this crash within the 'Character Motion Rendering' project (proj_066), trace the original bug ticket matched to its fingerprint, identify the code owner of the faulty module, and assign the bug ticket accordingly. Conclusively, link the new crash event to the bug ticket with a 'duplicate' relationship, following the notification policy."
        ),
        actions=[
            Action(
                name="GetCrashEventDetails",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="FindWorkItemByCrashFingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="GetCodeOwnerForModule",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_016",
        instruction=(
            "In your role as a DevOps specialist, a build failure for commit 'abc123def456789' occurred in the 'Game Texture Loading' project (proj_533) after the last successful commit 'xyz789abc123def'. Your objective is to conduct a comprehensive triage. Determine the root cause of the failure, create a bug ticket titled 'Build Failure Investigation for run_001' with the description 'Bisect identified 'abc123def456789' as the first bad commit.', and allocate it to the Game Engine Platform Team lead, all while adhering to the notification policy."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_533",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_017",
        instruction=(
            "As a localization specialist, identify that the French translation for the string key 'ui.main_menu.start_game' is not grammatically correct. Your role is to generate a high-priority bug report within the 'Localization' project (proj_021) directed to the Game Engine Platform Team lead, entitled 'Fix Grammar in French Translation for ui.main_menu.start_game', and described as 'The French translation for 'ui.main_menu.start_game' contains a grammatical error and must be corrected.'. Ensure the ticket is connected to the string key for tracking purposes and complies with the notification policy."
        ),
        actions=[
            Action(
                name="FindTranslationByKeyAndLocale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "fr"
                },
            ),Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_021",
                    "item_type": "bug",
                    "title": "Fix Grammar in French Translation for ui.main_menu.start_game",
                    "description": "The French translation for 'ui.main_menu.start_game' contains a grammatical error and must be corrected."
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_018",
        instruction=(
            "As a build manager, note that the nightly build for the 'Game Analytics & Telemetry Platform' project (proj_325) encountered failure due to a symbolication error involving symbol_003. Your assignment is to review the build process for commit 'ghi789def456abc', locate the absent symbol bundle, formulate a high-priority task for the Game Engine Platform Team to scrutinize the symbol generation process, and associate the task with the failed build run. The task should be titled 'Missing Symbols in Nightly AI Build' with the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_325",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_019",
        instruction=(
            "As a triage engineer, you have been alerted to a new crash event, 'crash_002'. Your responsibility is to delve into this issue within the 'Character Motion Rendering' project (proj_099), trace the original bug ticket associated with its fingerprint, identify the code owner for the problematic module, and then delegate the bug ticket to that person. In the final step, make sure to connect the new crash event to the bug ticket by establishing a 'duplicate' relationship, while complying with the notification policy."
        ),
        actions=[
            Action(
                name="GetCrashEventDetails",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="FindWorkItemByCrashFingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="GetCodeOwnerForModule",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_020",
        instruction=(
            "Assume the role of a reliability engineer. A build failure related to commit 'abc123def456789' has occurred in the 'Game Texture Loading' project (proj_123), showing the issue 'issue: 'TextureManager::loadTexture' was not declared in this scope'. The previous successful commit was 'xyz789abc123def'. Your mission is to carry out a comprehensive triage for this failure. Should you ascertain this to be a recurring problem, make sure the final bug report reflects this information as per the policy. It's vital to pinpoint the root cause and ensure a critical-priority bug ticket is generated titled 'Recurring Compilation Failure: issue: 'TextureManager::loadTexture' was not declared in this scope' with a description 'Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents.'. Assign the ticket to the appropriate owner, and send out the necessary notifications following the policy."
        ),
        actions=[
            Action(
                name="FindSimilarIncidents",
                kwargs={
                    "issue_signature": "issue: 'TextureManager::loadTexture' was not declared in this scope"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_123",
                    "item_type": "bug",
                    "title": "Recurring Compilation Failure: issue: 'TextureManager::loadTexture' was not declared in this scope",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "critical"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_021",
        instruction=(
            "As a DevOps specialist, you need to address a build failure for commit 'abc123def456789' in the 'Game Texture Loading' project (proj_044) following the last successful commit 'xyz789abc123def'. Your responsibility is to conduct a full triage, pinpoint the cause of the failure, and ensure a bug ticket is created with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. This ticket should be assigned to the lead of the Game Engine Platform Team, following the notification guidelines."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_044",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_022",
        instruction=(
            "As a localization manager, ensure the integration of newly recorded voice-over lines for the localization string 'vo.hero.intro_18' into the French and German localization processes for the 'Multi-Platform Game Infrastructure' project (proj_613). If a current tms job titled 'Integrate New VO Lines: hero_quest_18' exists, incorporate the new string key. If not, establish a new TMS job and ensure a high-priority tracking ticket is generated with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. This ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and comply with the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_613",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_613",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_023",
        instruction=(
            "As a build manager, handle the situation where the nightly build for the 'Game Analytics & Telemetry Platform' project (proj_005) encountered a symbolication error due to symbol_005. Your responsibility is to look into the build run for commit 'ghi789def456abc', locate the missing symbol bundle, generate a high-priority task for the Game Engine Platform Team to examine the symbol generation process, and connect the task to the unsuccessful build run. The task must be titled 'Missing Symbols in Nightly AI Build' with a description stating 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_005). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_005"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_005",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_005). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_024",
        instruction=(
            "Acting as a DevOps specialist, address the situation where a build for commit 'abc123def456789' within the 'Game Texture Loading' project (proj_055) failed following the last successful commit 'xyz789abc123def'. Your role is to coordinate a complete triage. You must determine the root cause of the failure and ensure that a bug ticket is issued with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket should be assigned to the Game Engine Platform Team lead, and must comply with the notification policy."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_055",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_025",
        instruction=(
            "As a localization manager, ensure that the newly recorded voice-over lines for the localization string 'vo.hero.intro_18' are incorporated into the French and German localization workflows for the 'Multi-Platform Game Infrastructure' project (proj_623). If there's already an existing tms job titled 'Integrate New VO Lines: hero_quest_18' for this project, incorporate the new string key there. If not, initiate a new TMS job and establish a high-priority tracking ticket titled 'Track TMS Job for New Strings' with the description 'Tracking TMS job for new string translation.'. The ticket should be assigned to the Game Engine Platform Team lead, connected to the tms job, and comply with the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_623",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_623",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_026",
        instruction=(
            "As a localization manager, integrate the newly recorded voice-over lines into the 'Epic Adventure Game' project (proj_131) using the localization string 'vo.hero.intro_01'. Initiate a new TMS job for these lines named 'Integrate New VO Lines: hero_quest_01', focusing on French and German. Subsequently, set up a high-priority tracking ticket for the Game Engine Platform Team lead titled 'Track TMS Job for New Strings' with the description 'Tracking TMS job for new string translation.'. Make sure to link the ticket to the new TMS job and ensure it follows the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_131",
                    "job_name": "Integrate New VO Lines: hero_quest_01",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_01"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_131",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_027",
        instruction=(
            "You are tasked as a localization manager. Newly recorded voice-over lines for the localization string 'vo.hero.intro_18' need integration into the 'Multi-Platform Game Infrastructure' project (proj_203) for French and German. Check for an existing tms job named 'Integrate New VO Lines: hero_quest_18' for this project to add the new string key. If such a job doesn't exist, initiate a new TMS job and initiate a high-priority tracking ticket titled 'Track TMS Job for New Strings'. The description should read 'Tracking TMS job for new string translation.'. Ensure that this ticket is assigned to the Game Engine Platform Team lead, linked to the tms job, and complies with the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_203",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_203",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_028",
        instruction=(
            "As a reliability engineer, you need to address a failed build for commit 'abc123def456789' within the 'Game Texture Loading' project (proj_023) due to the issue 'issue: 'TextureManager::loadTexture' was not declared in this scope'. Note that 'xyz789abc123def' was the last successful commit. Your responsibility is to thoroughly investigate this failure. If deemed a recurring problem, ensure that your final bug report reflects this according to policy. Identify the root cause and prioritize the creation of a critical bug ticket titled 'Recurring Compilation Failure: issue: 'TextureManager::loadTexture' was not declared in this scope'. Include the description 'Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents.'. This ticket should be assigned to the appropriate owner, and necessary notifications must follow the policy."
        ),
        actions=[
            Action(
                name="FindSimilarIncidents",
                kwargs={
                    "issue_signature": "issue: 'TextureManager::loadTexture' was not declared in this scope"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_023",
                    "item_type": "bug",
                    "title": "Recurring Compilation Failure: issue: 'TextureManager::loadTexture' was not declared in this scope",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "critical"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_029",
        instruction=(
            "As a localization manager, handle the integration of newly recorded voice-over lines into the 'Epic Adventure Game' project (proj_141) using the localization string 'vo.hero.intro_01'. Coordinate the creation of a new TMS job for these lines under the name 'Integrate New VO Lines: hero_quest_01', focusing on French and German. Next, generate a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. Link the ticket to the new TMS job and ensure compliance with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_141",
                    "job_name": "Integrate New VO Lines: hero_quest_01",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_01"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_141",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_030",
        instruction=(
            "As a localization manager, oversee the integration of newly recorded voice-over lines for the localization string 'vo.hero.intro_18' within the 'Multi-Platform Game Infrastructure' project (proj_213) into the French and German localization pipelines. If a tms job named 'Integrate New VO Lines: hero_quest_18' already exists for the project, add the new string key. Otherwise, initiate a new TMS job and coordinate the creation of a high-priority tracking ticket titled 'Track TMS Job for New Strings' with the description 'Tracking TMS job for new string translation.'. Ensure the ticket is assigned to the Game Engine Platform Team lead, linked to the tms job, and complies with the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_213",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_213",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_031",
        instruction=(
            "As a localization manager, your responsibilities include integrating a new set of voice-over lines into the 'Edge Computing Platform' project (proj_020) using the localization string 'vo.hero.intro_02'. Your role involves initiating a new TMS job named 'Integrate New VO Lines: hero_quest_02', focusing on the French and German languages. Following this, you should generate a high-priority tracking ticket for the Game Engine Platform Team lead titled 'Track TMS Job for New Strings', with the description 'Tracking TMS job for new string translation.'. The ticket needs to be associated with the new TMS job and comply with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_020",
                    "job_name": "Integrate New VO Lines: hero_quest_02",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_02"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_020",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_032",
        instruction=(
            "In your capacity as a triage engineer, a new crash event, 'crash_002', has been brought to your attention. Your duties involve examining this crash from the 'Character Motion Rendering' project (proj_055), identifying the original bug ticket linked with its fingerprint, determining the code owner for the affected module, and assigning the bug ticket to that owner. Finally, ensure that the new crash event is linked to the bug ticket with a 'duplicate' relationship, and make sure to follow the notification policy."
        ),
        actions=[
            Action(
                name="GetCrashEventDetails",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="FindWorkItemByCrashFingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="GetCodeOwnerForModule",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_033",
        instruction=(
            "As a DevOps specialist, a build associated with commit 'abc123def456789' in the 'Game Texture Loading' project (proj_633) has failed subsequent to the last confirmed successful commit 'xyz789abc123def'. Your responsibility is to handle a comprehensive triage. Determine the fundamental issue causing the failure and ensure the creation of a bug ticket titled 'Build Failure Investigation for run_001' and described as 'Bisect identified 'abc123def456789' as the first bad commit.'. This ticket should be allocated to the Game Engine Platform Team lead and follow the notification policy."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_633",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_034",
        instruction=(
            "In your role as a localization manager, a new batch of voice-over lines has been recorded for integration into the 'Database Infrastructure Upgrade' project (proj_006), featuring the localization string 'vo.hero.intro_15'. Your task involves coordinating a new TMS job for these lines, entitled 'Integrate New VO Lines: hero_quest_15', with a focus on French and German languages. Subsequently, ensure the creation of a high-priority tracking ticket for the Game Engine Platform Team lead under the title 'Track TMS Job for New Strings' described as 'Tracking TMS job for new string translation.'. The ticket should be connected to the newly created TMS job and must comply with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_006",
                    "job_name": "Integrate New VO Lines: hero_quest_15",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_15"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_006",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_035",
        instruction=(
            "As a triage engineer, a new crash event labeled 'crash_002' has been reported. Your responsibility is to examine this crash from the 'Character Motion Rendering' project (proj_066), locate the original bug ticket linked with its fingerprint, identify the code owner for the affected module, and then allocate the bug ticket to that owner. Ensure you establish a 'duplicate' relationship between the new crash event and the bug ticket, following the notification policy."
        ),
        actions=[
            Action(
                name="GetCrashEventDetails",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="FindWorkItemByCrashFingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="GetCodeOwnerForModule",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_036",
        instruction=(
            "As a localization manager, a new batch of voice-over lines has been recorded that must be integrated into the 'Green Computing Initiative' project (proj_019) using the localization string 'vo.hero.intro_02'. Your duty is to organize a new TMS job for these lines, titled 'Integrate New VO Lines: hero_quest_03', with the target languages French and German. Subsequently, generate a high-priority tracking ticket for the Game Engine Platform Team lead named 'Track TMS Job for New Strings', including the description 'Tracking TMS job for new string translation.'. The ticket should be linked to the new TMS job, in compliance with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_019",
                    "job_name": "Integrate New VO Lines: hero_quest_03",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_02"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_019",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_037",
        instruction=(
            "You are a DevOps specialist. The build associated with commit 'abc123def456789' within the 'Game Texture Loading' project (proj_661) has encountered a failure after the previous successful commit 'xyz789abc123def'. Your responsibility is to handle a comprehensive triage. You must identify the underlying cause of the failure and ensure a bug ticket is raised with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. This ticket needs to be assigned to the Game Engine Platform Team lead and must conform to the notification policy."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_661",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_038",
        instruction=(
            "You are a reliability manager. A critical, release-blocking build failure has occurred for commit 'abc123def456789' within the 'Game Engine Core Migration' project (proj_031) following the last known successful commit 'xyz789abc123def'. The failure’s issue signature is 'issue: 'TextureManager::loadTexture' was not declared in this scope'. Your role is to manage a comprehensive, thorough triage and trigger the remediation sequence. You must uncover the root cause, establish if this issue has recurred and deliver a detailed analysis to the development team. Post-investigation, you are required to generate a critical-priority bug ticket titled 'CRITICAL: Release Blocker - Build Failure in Game Engine' with a description summing up your findings: 'Critical build failure for commit 'abc123def456789' is blocking a major patch deployment. Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents.'. To examine associated assets, create a high-priority task for the Game Engine Platform Team lead titled 'Verify Asset Integrity After Renderer Fix' with the description 'The renderer fix in work_028 may affect texture loading. Please ensure that the asset 'asset_011' still renders correctly.'. Additionally, create a compliance record for the incident containing details; compliance_type 'incident_response', requirement 'critical_build_failure_triage', status 'in_progress', and details 'Triage for critical build failure 'run_001' is in progress. See bug 'work_028' for details.'. This record should be assigned to the Game Engine Platform Team lead and must adhere to the notification policy."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="FindSimilarIncidents",
                kwargs={
                    "issue_signature": "issue: 'TextureManager::loadTexture' was not declared in this scope"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_031",
                    "item_type": "bug",
                    "title": "CRITICAL: Release Blocker - Build Failure in Game Engine",
                    "description": "Critical build failure for commit 'abc123def456789' is blocking a major patch deployment. Bisect identified 'abc123def456789' as the first bad commit. This is a recurring issue with 2 similar past incidents."
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "critical"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_031",
                    "item_type": "task",
                    "title": "Verify Asset Integrity After Renderer Fix",
                    "description": "The renderer fix in work_028 may affect texture loading. Please verify that the asset 'asset_011' is still rendering correctly."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_029",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "work_029",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateComplianceRecord",
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
                name="CreateNotificationRecord",
                kwargs={
                    "message": "compliance_013"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_014"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_039",
        instruction=(
            "As a triage engineer, a critical crash event labeled 'crash_002' has been flagged. Your objective is to examine this crash, locate the original bug ticket linked to its fingerprint, identify the code owner for the crashed module, and allocate the bug ticket to that owner. Lastly, you must connect the recent crash event to the bug ticket with a 'duplicate' relation and comply with the notification policy."
        ),
        actions=[
            Action(
                name="GetCrashEventDetails",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="FindWorkItemByCrashFingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="GetCodeOwnerForModule",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_040",
        instruction=(
            "Serving as a build manager, the nightly build for the 'Database Infrastructure Upgrade' project (proj_006) encountered a failure due to a symbolication error concerning symbol_007. Your task is to scrutinize the build run for commit 'jkl012ghi789def', discover the missing symbol bundle, establish a high-priority task for the Game Engine Platform Team to explore the symbol generation process, and associate the task with the failed build run. The task must carry the title 'Missing Symbols in Nightly AI Build' and the description, 'The nightly build for commit jkl012ghi789def failed due to missing symbols (symbol_007). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "jkl012ghi789def"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_007"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_006",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit jkl012ghi789def failed due to missing symbols (symbol_007). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_006",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_041",
        instruction=(
            "Handle the role of a localization manager. A new set of voice-over lines has been recorded that needs to be integrated into the 'Data Pipeline Optimization' project (proj_018) with the localization string 'vo.hero.intro_03'. Coordinate the creation of a new TMS job for these lines named 'Integrate New VO Lines: hero_quest_03', targeting French and German. Following this, create a high-priority tracking ticket addressed to the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. Ensure the ticket is linked to the new TMS job, complying with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_018",
                    "job_name": "Integrate New VO Lines: hero_quest_03",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_03"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_018",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_042",
        instruction=(
            "Function as a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_335) has encountered a failure due to a symbolication error concerning symbol_003. Your responsibility is to examine the build run for commit 'ghi789def456abc', locate the missing symbol bundle, and initiate a high-priority task for the Game Engine Platform Team to scrutinize the symbol generation process. Attach the task to the failed build run. The task must carry the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to examine the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_335",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_043",
        instruction=(
            "As a localization manager, you are tasked with a new set of voice-over lines that must be integrated into the 'Network Security Enhancement' project (proj_747), specifically using the localization string 'vo.hero.intro_14'. Your responsibilities include creating a new TMS job for these lines, titled 'Integrate New VO Lines: hero_quest_14', targeting both French and German. Following this, initiate a high-priority tracking ticket for the Game Engine Platform Team lead. Title the ticket 'Track TMS Job for New Strings' and use the description 'Tracking TMS job for new string translation.'. Ensure the ticket is linked to the new TMS job and complies with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_747",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_747",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_044",
        instruction=(
            "In your role as a DevOps specialist, a build failure has occurred for commit 'abc123def456789' within the 'Game Texture Loading' project (proj_662) right after the stable commit 'xyz789abc123def'. Your job is to conduct a comprehensive triage. Identify the root cause of the failure and make sure a bug ticket is generated with the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket must be directed to the Game Engine Platform Team lead and must comply with the notification policy."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_662",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_045",
        instruction=(
            "Handle the integration of newly recorded voice-over lines into the 'Network Security Enhancement' project (proj_454) using the localization string 'vo.hero.intro_14'. Your assignment is to coordinate the creation of a new TMS job for these lines under the name 'Integrate New VO Lines: hero_quest_14', focusing on French and German. Following this, you need to produce a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. Link the ticket to the newly created TMS job, ensuring compliance with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_454",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_454",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_046",
        instruction=(
            "Ensure the new set of voice-over lines for the localization string 'vo.hero.intro_04' is incorporated into the 'Data Pipeline Optimization' project (proj_017), targeting French and German. If there is a pre-existing tms job under the name 'Integrate New VO Lines: hero_quest_04', add the new string key. If not, establish a new TMS job and take care that a high-priority tracking ticket is produced with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket should be delegated to the Game Engine Platform Team lead, associated with the tms job, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_017",
                    "job_name": "Integrate New VO Lines: hero_quest_04",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_04"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_017",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_047",
        instruction=(
            "As a DevOps specialist, a build related to commit 'abc123def456789' in the 'Game Texture Loading' project (proj_833) has encountered a failure following the last successful commit 'xyz789abc123def'. Your responsibility is to coordinate a comprehensive triage. It is essential to determine the root cause of this failure and to ensure the creation of a bug ticket titled 'Build Failure Investigation for run_001', with a description stating 'Bisect identified 'abc123def456789' as the first bad commit.'. The ticket should be assigned to the Game Engine Platform Team lead, following the notification policy."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_833",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_048",
        instruction=(
            "As a triage engineer, a significant crash event, 'crash_002', has been reported. You are required to explore this crash to uncover the original bug ticket linked to its fingerprint, determine the code owner of the module that crashed, and then reassign the bug ticket to that owner. Lastly, ensure the new crash event is connected to the bug ticket with a 'duplicate' relationship."
        ),
        actions=[
            Action(
                name="GetCrashEventDetails",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="FindWorkItemByCrashFingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="GetCodeOwnerForModule",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_049",
        instruction=(
            "As a build manager, handle the failed nightly build for the 'Game Analytics & Telemetry Platform' project (proj_355) due to a symbolication error with symbol_003. Your responsibility is to examine the build run for commit 'ghi789def456abc', locate the missing symbol bundle, organize a high-priority task for the Game Engine Platform Team to look into the symbol generation process, and associate the task with the failed build run. The task should be titled 'Missing Symbols in Nightly AI Build' and include the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_355",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_050",
        instruction=(
            "As a build manager, manage the failed nightly build for the 'Game Analytics & Telemetry Platform' project (proj_005) which encountered a symbolication error concerning symbol_007. It's your duty to scrutinize the build run for commit 'ghi789def456abc', find the absent symbol bundle, coordinate a high-priority task for the Game Engine Platform Team to probe into the symbol generation process, and connect the task to the failed build run. The task should be named 'Missing Symbols in Nightly AI Build' with the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_007). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_007"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_005",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_007). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_051",
        instruction=(
            "You are a localization manager. Integrate a new set of voice-over lines recorded for the 'Legacy System Modernization' project (proj_016) using the localization string 'vo.hero.intro_05'. Your responsibility is to establish a new TMS job named 'Integrate New VO Lines: hero_quest_05', directed at French and German. Proceed to create a high-priority tracking ticket for the Game Engine Platform Team lead, titled 'Track TMS Job for New Strings' with the description 'Tracking TMS job for new string translation.', ensuring it is linked to the new TMS job."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_016",
                    "job_name": "Integrate New VO Lines: hero_quest_05",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_05"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_016",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_052",
        instruction=(
            "You are a localization specialist. There is a text overflow issue causing the German translation for the string key 'ui.main_menu.start_game' to fail validation. Your role is to commence the standard remediation process for this type of error. Verify the validation status is 'failed', updating the status as necessary. Should the German translation's actual width surpass the set maximum width for that string key, ensure a high-priority bug ticket is created within the 'Localization' project (proj_064), entitled 'Fix German Translation for Start Game Button' with the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. This ticket must be assigned to the Game Engine Platform Team lead, connected to the localization string, and comply with the notification guidelines."
        ),
        actions=[
            Action(
                name="FindTranslationByKeyAndLocale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_064",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_053",
        instruction=(
            "You serve as a localization manager. A fresh batch of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_643). Your responsibility is to incorporate these lines into the French and German localization workflows. If there is an existing TMS job titled 'Integrate New VO Lines: hero_quest_18' related to the project, append the new string key. If not, initiate a new TMS job and ensure a high-priority tracking ticket is generated with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket needs to be assigned to the Game Engine Platform Team lead, associated with the TMS job, and comply with the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_643",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_643",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_054",
        instruction=(
            "You hold the position of a localization manager. Newly recorded voice-over lines require integration into the 'Game Security & Anti-Cheat Framework' project (proj_004) using the localization string 'vo.hero.intro_17'. Your assignment is to set up a new TMS job for these lines named 'Integrate New VO Lines: hero_quest_17', targeting French and German. Subsequently, you must generate a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. This ticket should be connected to the new TMS job and comply with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_004",
                    "job_name": "Integrate New VO Lines: hero_quest_17",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_17"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_004",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_055",
        instruction=(
            "You are a build manager. The nightly build for the 'Game Analytics & Telemetry Platform' project (proj_005) encountered a failure with a symbolication error due to symbol_008. Your responsibility is to look into the build run for commit 'ghi789def456abc', locate the missing symbol bundle, create an urgent task for the Game Engine Platform Team to examine the symbol generation process, and connect the task to the failed build run. The task should be titled 'Missing Symbols in Nightly AI Build' and described as 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_008). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_008"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_005",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_008). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_056",
        instruction=(
            "You are a localization manager. A new batch of voice-over lines for the localization string 'vo.hero.intro_06' has been recorded for the 'Automated Testing Infrastructure' project (proj_015). You need to ensure these lines are incorporated into the French and German localization pipelines. If there exists an existing tms job named 'Integrate New VO Lines: hero_quest_06' associated with the project, add the new string key. If not, you must establish a new TMS job and ensure the creation of a high-priority tracking ticket with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and follow the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_015",
                    "job_name": "Integrate New VO Lines: hero_quest_06",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_06"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_015",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_057",
        instruction=(
            "Act as a localization manager. A new batch of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_543). Your role is to make certain these lines are incorporated into the French and German localization pipelines. When a tms job titled 'Integrate New VO Lines: hero_quest_18' already exists for the project, incorporate the new string key into it. If not, set up a new TMS job and guarantee a high-priority tracking ticket is established with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket should be assigned to the Game Engine Platform Team lead, linked to the tms job, and comply with the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_543",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_543",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_058",
        instruction=(
            "Serve as a localization specialist. The German translation for the string key 'ui.main_menu.start_game' did not pass validation due to a text overflow problem. Your duty is to start the standard remediation process for such failures. You must confirm the validation status is 'failed', otherwise adjust the status. If the actual width of the German translation surpasses the defined max width for that string key, ensure a high-priority bug ticket is generated in the 'Localization' project (proj_073) with the title 'Fix German Translation for Start Game Button' and the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. The ticket must be assigned to the head of the Game Engine Platform Team, linked to the localization string, and follow the notification policy."
        ),
        actions=[
            Action(
                name="FindTranslationByKeyAndLocale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_073",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_059",
        instruction=(
            "Acting as a localization manager, address the integration of newly recorded voice-over lines for the localization string 'vo.hero.intro_18' for the 'Multi-Platform Game Infrastructure' project (proj_747). Your responsibility is to incorporate these in the French and German localization pipelines. If a tms job named 'Integrate New VO Lines: hero_quest_18' already exists for this project, append the new string key. If not, initiate a new TMS job and set up a high-priority tracking ticket titled 'Track TMS Job for New Strings', featuring the description 'Tracking TMS job for new string translation.'. This ticket should be allocated to the Game Engine Platform Team lead, linked with the tms job, and must comply with the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_747",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_747",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_060",
        instruction=(
            "As a DevOps specialist, manage the issue of a failed build for commit 'abc123def456789' within the 'Game Texture Loading' project (proj_933), following the last successful commit 'xyz789abc123def'. Conduct a comprehensive triage to pinpoint the root cause of the failure, ensuring a bug ticket is generated bearing the title 'Build Failure Investigation for run_001' and the description 'Bisect identified 'abc123def456789' as the first bad commit.'. This ticket should be directed to the Game Engine Platform Team lead and must comply with the notification policy."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "abc123def456789"
                },
            ),
            Action(
                name="RunGitBisect",
                kwargs={
                    "failing_commit_sha": "abc123def456789",
                    "last_known_good_commit_sha": "xyz789abc123def"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_933",
                    "item_type": "bug",
                    "title": "Build Failure Investigation for run_001",
                    "description": "Bisect identified 'abc123def456789' as the first bad commit."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#failure",
                    "message": "notification_013"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_061",
        instruction=(
            "As a localization manager, your task is to handle the integration of a newly recorded set of voice-over lines into the 'Container Registry Security' project (proj_014) using the localization string 'vo.hero.intro_07'. You should coordinate the creation of a new TMS job for these lines titled 'Integrate New VO Lines: hero_quest_07', targeting both French and German languages. Subsequently, initiate a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. Ensure the ticket is linked with the new TMS job and complies with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_014",
                    "job_name": "Integrate New VO Lines: hero_quest_07",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_07"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_014",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_062",
        instruction=(
            "Your responsibility as a localization manager is to ensure the integration of new voice-over lines for the localization string 'vo.hero.intro_18' within the 'Multi-Platform Game Infrastructure' project (proj_810). These lines need to be incorporated into both French and German localization pipelines. If a current TMS job named 'Integrate New VO Lines: hero_quest_18' is associated with the project, incorporate the new string key. If not, initiate a new TMS job and make sure to create a high-priority tracking ticket with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket is to be assigned to the Game Engine Platform Team lead, linked to the TMS job, and must adhere to the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_810",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_810",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_063",
        instruction=(
            "Manage localization efforts as a localization manager. The task involves integrating newly recorded voice-over lines for the localization string 'vo.hero.intro_18' into the French and German workflows for the 'Multi-Platform Game Infrastructure' project (proj_813). If there currently exists a tms job named 'Integrate New VO Lines: hero_quest_18' for this project, ensure the new string key is added. If not, initiate a new TMS job and create a high-priority tracking ticket titled 'Track TMS Job for New Strings', with a description 'Tracking TMS job for new string translation.'. Assign this ticket to the Game Engine Platform Team lead, link it to the tms job, and follow the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_813",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_813",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_064",
        instruction=(
            "Oversee localization management as a localization manager. You need to facilitate the integration of newly recorded voice-over lines for the localization string 'vo.hero.intro_18' into the French and German pipelines for the 'Multi-Platform Game Infrastructure' project (proj_003). If an existing tms job named 'Integrate New VO Lines: hero_quest_18' is present for this project, incorporate the new string key. If absent, generate a new TMS job and establish a high-priority tracking ticket with the title 'Track TMS Job for New Strings' and described as 'Tracking TMS job for new string translation.'. This ticket should be assigned to the Game Engine Platform Team lead, linked to the tms job, and must comply with the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_003",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_003",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_065",
        instruction=(
            "As a build manager, the nightly build for the 'Game Analytics & Telemetry Platform' project (proj_365) has encountered a failure due to a symbolication error with symbol_003. Your mission is to examine the build run for commit 'ghi789def456abc', identify the missing symbol bundle, open a high-priority task for the Game Engine Platform Team to review the symbol generation process, and connect this task with the failed build run. The task should bear the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_365",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_066",
        instruction=(
            "As a localization manager, you need to integrate a fresh set of voice-over lines into the 'Network Security Enhancement' project (proj_737) with localization string 'vo.hero.intro_14'. Your responsibility is to establish a new TMS job for these lines titled 'Integrate New VO Lines: hero_quest_14', aimed at French and German. Then, initiate a high-priority tracking ticket for the Game Engine Platform Team lead, with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. This ticket must be associated with the new TMS job, following the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_737",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_737",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_067",
        instruction=(
            "As a localization specialist, handle the issue where the German translation for string key 'ui.main_menu.start_game' has failed validation due to text overflow. Initiate the standard process for such failures ensuring the validation status reflects 'failed', updating if necessary. Should the German translation width surpass the allowed max width for the string key, coordinate the creation of a high-priority bug ticket in the 'Localization' project (proj_085) titled 'Fix German Translation for Start Game Button'. This ticket should describe 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds UI width constraints and must be shortened.'. Assign the ticket to the Game Engine Platform Team lead, link it to the localization string, and follow the notification policy."
        ),
        actions=[
            Action(
                name="FindTranslationByKeyAndLocale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_085",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_068",
        instruction=(
            "Act as a localization manager regarding the new voice-over lines recorded for the localization string 'vo.hero.intro_18' in the 'Multi-Platform Game Infrastructure' project (proj_903). Ensure the integration of these lines into the French and German localization workflows. If a TMS job titled 'Integrate New VO Lines: hero_quest_18' is already present, append the new string key. Otherwise, establish a new TMS job and generate a high-priority tracking ticket titled 'Track TMS Job for New Strings', with the description 'Tracking TMS job for new string translation.'. Assign this ticket to the Game Engine Platform Team lead, attach it to the TMS job, and comply with the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_903",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_903",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_069",
        instruction=(
            "As a localization manager, a new set of voice-over lines has been recorded that should be integrated into the 'Network Security Enhancement' project (proj_444) using the localization string 'vo.hero.intro_14'. Your responsibility is to set up a new TMS job for these lines with the title 'Integrate New VO Lines: hero_quest_14', focusing on the French and German languages. Subsequently, generate a high-priority tracking ticket for the Game Engine Platform Team lead, titled 'Track TMS Job for New Strings', with the description 'Tracking TMS job for new string translation.'. This ticket must be associated with the new TMS job and comply with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_444",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_444",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_070",
        instruction=(
            "As a build manager, the nightly build for the 'Game Analytics & Telemetry Platform' project (proj_005) has encountered a failure due to a symbolication error involving symbol_004. Your duty is to examine the build run for commit 'ghi789def456abc', identify the missing symbol bundle, create a high-priority task for the Game Engine Platform Team to scrutinize the symbol generation process, and connect the task to the failed build run. The task should bear the title 'Missing Symbols in Nightly AI Build' and the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_004). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_004"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_005",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_004). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_071",
        instruction=(
            "You are serving as a build manager. There is a failure in the nightly build of the 'Game Analytics & Telemetry Platform' project (proj_375) due to a symbolication issue involving symbol_003. Your role involves examining the build run associated with commit 'ghi789def456abc', identifying the missing symbol bundle, creating a top-priority task for the Game Engine Platform Team to look into the symbol generation process, and connecting the task to the unsuccessful build run. The task needs the title 'Missing Symbols in Nightly AI Build' and description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_375",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_072",
        instruction=(
            "You take on the role of a localization manager. A novel collection of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_902). Your assignment is to guarantee these lines are incorporated into the French and German localization workflows. If a tms job called 'Integrate New VO Lines: hero_quest_18' already pertains to the project, insert the new string key. On the other hand, set up a new TMS job and make sure a top-priority tracking ticket is generated with the title 'Track TMS Job for New Strings' and description 'Tracking TMS job for new string translation.'. Assign the ticket to the Game Engine Platform Team lead, associate it with the tms job, and ensure it follows the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_902",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_902",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_073",
        instruction=(
            "As a localization manager, handle the integration of a new set of voice-over lines for the localization string 'vo.hero.intro_18' within the 'Multi-Platform Game Infrastructure' project (proj_347). Ensure these lines are processed into the French and German localization pipelines. If a tms job called 'Integrate New VO Lines: hero_quest_18' already exists for the project, add the new string key. If not, initiate a new TMS job and create a high-priority tracking ticket titled 'Track TMS Job for New Strings' with the description 'Tracking TMS job for new string translation.'. This ticket must be assigned to the Game Engine Platform Team lead, associated with the tms job, and comply with the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_347",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_347",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_074",
        instruction=(
            "As a localization manager, coordinate the integration of a new batch of voice-over lines for the localization string 'vo.hero.intro_19' within the 'Game Build Pipeline Modernization' project (proj_002). Ensure incorporation into the French and German localization pipelines. If there is a tms job named 'Integrate New VO Lines: hero_quest_19' related to the project, include the new string key there. If absent, establish a new TMS job and ensure the creation of a high-priority tracking ticket titled 'Track TMS Job for New Strings', described as 'Tracking TMS job for new string translation.'. This ticket must be allocated to the Game Engine Platform Team lead, linked to the tms job, and follow the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_002",
                    "job_name": "Integrate New VO Lines: hero_quest_19",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_19"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_002",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_075",
        instruction=(
            "As a build manager, address the issue with the nightly build of the 'Game Analytics & Telemetry Platform' project (proj_005) which encountered a symbolication error involving symbol_003. Your responsibility is to examine the build run linked to commit 'ghi789def456abc', locate the missing symbol bundle, establish a high-priority task for the Game Engine Platform Team to explore the symbol generation process, and associate the task with the failed build run. Ensure the task is titled 'Missing Symbols in Nightly AI Build' and includes the description 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_003"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_005",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_003). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_076",
        instruction=(
            "Act as a localization manager where newly recorded voice-over lines are ready for integration into the 'Network Security Enhancement' project (proj_434) using the localization string 'vo.hero.intro_14'. Your mission is to initiate a new TMS job for these lines titled 'Integrate New VO Lines: hero_quest_14', aimed at French and German. Following this, produce a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and a description 'Tracking TMS job for new string translation.'. The ticket must be connected to the new TMS job and be in line with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_434",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_434",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_077",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_653). Handle the integration of these lines into the French and German localization pipelines. If there is an existing tms job named 'Integrate New VO Lines: hero_quest_18' for the project, incorporate the new string key. If not, create a new TMS job and coordinate a high-priority tracking ticket with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket should be assigned to the Game Engine Platform Team lead, linked to the tms job, and comply with the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_653",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_653",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_078",
        instruction=(
            "You are a localization manager. A new set of voice-over lines for the localization string 'vo.hero.intro_18' has been recorded for the 'Multi-Platform Game Infrastructure' project (proj_901). Coordinate the integration of these lines into the French and German localization pipelines. When there exists a tms job named 'Integrate New VO Lines: hero_quest_18' associated with the project, add the new string key. If absent, establish a new TMS job and ensure a high-priority tracking ticket is generated with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. The ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and follow the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_901",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_901",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_079",
        instruction=(
            "As a localization manager, your role involves incorporating a fresh batch of voice-over lines into the 'Epic Adventure Game' project (proj_161) using the localization string 'vo.hero.intro_01'. Start by establishing a new TMS job titled 'Integrate New VO Lines: hero_quest_01', aimed at French and German languages. Afterward, prepare a high-priority tracking ticket directed to the Game Engine Platform Team lead. The ticket should be titled 'Track TMS Job for New Strings' and described as 'Tracking TMS job for new string translation.'. Make sure the ticket is connected to the newly created TMS job and complies with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_161",
                    "job_name": "Integrate New VO Lines: hero_quest_01",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_01"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_161",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_080",
        instruction=(
            "As a build manager, you need to address the failed nightly build for the 'Game Analytics & Telemetry Platform' project (proj_005) due to a symbolication error associated with symbol_002. Begin by investigating the build run for the commit 'ghi789def456abc' to locate the missing symbol bundle. Then, organize a high-priority task for the Game Engine Platform Team to examine the symbol generation process. Ensure the task is linked to the failed build run. The task must be named 'Missing Symbols in Nightly AI Build' and described as 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_002). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_002"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_005",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_002). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_081",
        instruction=(
            "As a localization manager, handle the integration of a newly recorded set of voice-over lines into the 'Network Security Enhancement' project (proj_424) with the localization string 'vo.hero.intro_14'. You need to initiate a new TMS job for these lines named 'Integrate New VO Lines: hero_quest_14', ensuring it's directed towards the French and German languages. Subsequently, you must coordinate the creation of a high-priority tracking ticket for the Game Engine Platform Team lead. The ticket should be titled 'Track TMS Job for New Strings' and have the description 'Tracking TMS job for new string translation.'. Ensure this ticket is linked to the new TMS job and complies with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_424",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_424",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_082",
        instruction=(
            "As a localization manager, handle the integration of a newly recorded set of voice-over lines into the 'Network Security Enhancement' project (proj_727) with the localization string 'vo.hero.intro_14'. You need to initiate a new TMS job for these lines named 'Integrate New VO Lines: hero_quest_14', ensuring it's directed towards the French and German languages. Subsequently, you must coordinate the creation of a high-priority tracking ticket for the Game Engine Platform Team lead. The ticket should be titled 'Track TMS Job for New Strings' and have the description 'Tracking TMS job for new string translation.'. Ensure this ticket is linked to the new TMS job and complies with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_727",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_727",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_083",
        instruction=(
            "As a localization manager, you are responsible for handling the integration of a newly recorded set of voice-over lines for the localization string 'vo.hero.intro_18' within the 'Multi-Platform Game Infrastructure' project (proj_663). Ensure that these lines are incorporated into the French and German localization workflows. If a tms job titled 'Integrate New VO Lines: hero_quest_18' already exists for the project, append the new string key to it. Otherwise, coordinate the creation of a new TMS job and initiate a high-priority tracking ticket titled 'Track TMS Job for New Strings' with the description 'Tracking TMS job for new string translation.'. This ticket must be assigned to the lead of the Game Engine Platform Team, connected to the tms job, and comply with the notification protocols."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_663",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_663",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_084",
        instruction=(
            "As a localization manager, handle the integration of newly recorded voice-over lines that need to be incorporated into the 'Game Engine Core Migration' project (proj_001) with the localization string 'vo.hero.intro_20'. Coordinate the creation of a new TMS job for these lines, named 'Integrate New VO Lines: hero_quest_20', targeting the French and German languages. Subsequently, initiate a high-priority tracking ticket for the Game Engine Platform Team lead with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. This ticket must be linked to the new TMS job and adhere to the notification policies."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_001",
                    "job_name": "Integrate New VO Lines: hero_quest_20",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_20"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_001",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_085",
        instruction=(
            "As a localization manager, your role involves handling a new set of voice-over lines for the localization string 'vo.hero.intro_18' recorded for the 'Multi-Platform Game Infrastructure' project (proj_673). Your duty is to ensure these lines are incorporated into the French and German localization workflows. If there is already a tms job named 'Integrate New VO Lines: hero_quest_18' associated with the project, include the new string key. If not, initiate a new TMS job and ensure a high-priority tracking ticket is created with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. Assign the ticket to the Game Engine Platform Team lead, link it to the tms job, and follow the notification protocol."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_673",
                    "job_name": "Integrate New VO Lines: hero_quest_18",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_18"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_673",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_086",
        instruction=(
            "As a localization specialist, your responsibility is to address a validation issue with the German translation for the string key 'ui.main_menu.start_game' due to text overflow. You must coordinate the execution of the standard remediation procedure for this validation failure. Ensure the validation status is 'failed', updating the status if necessary. If the actual width of the German translation surpasses the allowed max width for that string key, ensure a high-priority bug ticket is opened in the 'Localization' project (proj_864) with the title 'Fix German Translation for Start Game Button' and the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. The ticket should be assigned to the lead of the Game Engine Platform Team, linked to the localization string, and comply with the notification standards."
        ),
        actions=[
            Action(
                name="FindTranslationByKeyAndLocale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_864",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_087",
        instruction=(
            "As a localization manager, manage the integration of a new batch of voice-over lines into the 'Epic Adventure Game' project (proj_181), utilizing the localization string 'vo.hero.intro_01'. Your objective is to coordinate a new TMS job titled 'Integrate New VO Lines: hero_quest_01', with target languages French and German. Additionally, create a high-priority tracking ticket for the Game Engine Platform Team lead, titled 'Track TMS Job for New Strings' with a description of 'Tracking TMS job for new string translation.'. This ticket must relate to the newly established TMS job and comply with the existing notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_181",
                    "job_name": "Integrate New VO Lines: hero_quest_01",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_01"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_181",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_088",
        instruction=(
            "As a localization specialist, address the validation failure of the German translation for the string key 'ui.main_menu.start_game', attributed to a text overflow issue. Your role is to initiate the standard remediation process for such failures. Verify the validation status is 'failed', and update it if necessary. Should you verify that the actual width of the German translation surpasses the designated max width for this string key, ensure the creation of a high-priority bug ticket within the 'Localization' project (proj_118). The ticket should be titled 'Fix German Translation for Start Game Button' and include the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. Assign the ticket to the leader of the Game Engine Platform Team, ensure it is linked to the localization string, and adhere to the notification policy."
        ),
        actions=[
            Action(
                name="FindTranslationByKeyAndLocale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_118",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_089",
        instruction=(
            "As a localization specialist, handle the issue where the German translation for string key 'ui.main_menu.start_game' did not pass validation because of a text overflow problem. Begin the normal remediation procedure suited for such failures. Confirm that the validation status reads 'failed', and update it if necessary. Should the German translation's actual width surpass the specified limit for that string key, it's crucial to create a high-priority bug ticket in the 'Localization' project (proj_854), titled 'Fix German Translation for Start Game Button'. Include the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. This ticket must be assigned to the lead of the Game Engine Platform Team, linked to the localization string, and follow the notification protocol."
        ),
        actions=[
            Action(
                name="FindTranslationByKeyAndLocale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_854",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_090",
        instruction=(
            "As a localization specialist, manage the failure of the German translation for string key 'ui.main_menu.start_game' that did not pass validation due to a text overflow issue. Initiate the regular remediation process for such failures. Make sure the validation status is marked as 'failed', or update it if it isn't. If the actual width of the German translation is beyond the predetermined maximum width for that string key, you need to ensure a high-priority bug ticket is created in the 'Localization' project (proj_844) with the title 'Fix German Translation for Start Game Button'. The description should be 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. It is imperative to assign this ticket to the lead of the Game Engine Platform Team, link it to the localization string, and comply with the notification policy."
        ),
        actions=[
            Action(
                name="FindTranslationByKeyAndLocale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_844",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_091",
        instruction=(
            "As a localization manager, you are to handle the integration of newly recorded voice-over lines for the localization string 'vo.hero.intro_13' within the 'Developer Portal' project (proj_008). Make sure these lines are added to the French and German localization workflows. If there is an existing tms job titled 'Integrate New VO Lines: hero_quest_13' related to the project, include the new string key there. If not, create a new TMS job and ensure a high-priority tracking ticket is established with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. This ticket must be assigned to the Game Engine Platform Team lead, linked to the tms job, and comply with the notification policy."
        ),
        actions=[
            Action(
                name="ListTmsJobs",
                kwargs={},
            ),
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_008",
                    "job_name": "Integrate New VO Lines: hero_quest_13",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_13"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_008",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_092",
        instruction=(
            "In your role as a localization specialist, your responsibility is to coordinate the standard remediation process for a validation failure concerning the German translation of the string key 'ui.main_menu.start_game' due to a text overflow. You need to verify that the validation status is marked as 'failed', or update the status if necessary. If it is determined that the current width of the German translation surpasses the designated max width for that string key, a high-priority bug ticket must be created in the 'Localization' project (proj_031) with the title 'Fix German Translation for Start Game Button' and the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. The ticket should be assigned to the lead of the Game Engine Platform Team, linked to the localization string, and conform to the notification policy."
        ),
        actions=[
            Action(
                name="FindTranslationByKeyAndLocale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_031",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_093",
        instruction=(
            "Assume the role of localization manager. There are freshly recorded voice-over lines to be incorporated into the 'Network Security Enhancement' project (proj_707) using the localization string 'vo.hero.intro_14'. Your responsibility includes setting up a new TMS job for these lines, titled 'Integrate New VO Lines: hero_quest_14', with a focus on French and German languages. Subsequently, you need to organize a high-priority tracking ticket for the Game Engine Platform Team lead, titled 'Track TMS Job for New Strings', and outlined with the description 'Tracking TMS job for new string translation.'. Ensure the ticket is associated with the new TMS job and follows the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_707",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_707",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_094",
        instruction=(
            "Act as a localization manager. New voice-over lines have been recorded and require integration into the 'Network Security Enhancement' project (proj_717) utilizing the localization string 'vo.hero.intro_14'. Your task is to coordinate a new TMS job for these lines, named 'Integrate New VO Lines: hero_quest_14', directed towards French and German. Then, establish a high-priority tracking ticket for the Game Engine Platform Team lead with the header 'Track TMS Job for New Strings' and the note 'Tracking TMS job for new string translation.'. The ticket must be linked appropriately to the new TMS job and comply with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_717",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_717",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_095",
        instruction=(
            "Assume the role of a build manager. The nightly build for the 'Asset Bundle Validation' project (proj_078) encountered a failure due to a symbolication error associated with symbol_008. Your responsibility is to scrutinize the build run for commit 'ghi789def456abc', identify the absent symbol bundle, initiate a high-priority task for the Game Engine Platform Team to examine the symbol generation process, and associate the task with the failed build run. Title the task 'Missing Symbols in Nightly AI Build' and describe it as 'The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_008). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures.'."
        ),
        actions=[
            Action(
                name="FindBuildRun",
                kwargs={
                    "commit_sha": "ghi789def456abc"
                },
            ),
            Action(
                name="GetSymbolBundleDetails",
                kwargs={
                    "symbol_id": "symbol_008"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_078",
                    "item_type": "task",
                    "title": "Missing Symbols in Nightly AI Build",
                    "description": "The nightly build for commit ghi789def456abc failed due to missing symbols (symbol_008). The Game Engine Platform Team needs to investigate the symbol generation process to prevent future failures."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "run_004",
                    "link_type": "related"
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_096",
        instruction=(
            "Take on the responsibilities of a localization manager. A new batch of voice-over lines has been recorded and needs to be integrated into the 'Network Security Enhancement' project (proj_007) using the localization string 'vo.hero.intro_14'. Your objective is to establish a new TMS job for these lines with the name 'Integrate New VO Lines: hero_quest_14', focusing on French and German. Subsequently, generate a high-priority tracking ticket for the Game Engine Platform Team lead, titled 'Track TMS Job for New Strings' and described as 'Tracking TMS job for new string translation.'. The ticket must be connected to the new TMS job and comply with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_007",
                    "job_name": "Integrate New VO Lines: hero_quest_14",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_14"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_007",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_097",
        instruction=(
            "As a localization manager, handle the integration of a new set of voice-over lines into the 'Epic Adventure Game' project (proj_521) using the localization string 'vo.hero.intro_01'. Your role involves establishing a new TMS job titled 'Integrate New VO Lines: hero_quest_01', focusing on French and German. Following this, coordinate the creation of a high-priority tracking ticket for the Game Engine Platform Team lead, titled 'Track TMS Job for New Strings', with a description of 'Tracking TMS job for new string translation.'. Ensure the ticket is linked to the new TMS job, complying with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_521",
                    "job_name": "Integrate New VO Lines: hero_quest_01",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_01"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_521",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_098",
        instruction=(
            "As a triage engineer, handle the investigation of the newly reported crash event, 'crash_002'. Your task is to examine this crash from the 'Character Motion Rendering' project (proj_088), identify the original bug ticket connected to its fingerprint, determine the code owner of the module that experienced the crash, and assign the bug ticket to this owner. Finally, you must connect the new crash event to the bug ticket with a 'duplicate' relationship, ensuring adherence to the notification policy."
        ),
        actions=[
            Action(
                name="GetCrashEventDetails",
                kwargs={
                    "crash_id": "crash_002"
                }
            ),
            Action(
                name="FindWorkItemByCrashFingerprint",
                kwargs={
                    "fingerprint": "renderer_character_load_access_violation_xyz"
                }
            ),
            Action(
                name="GetCodeOwnerForModule",
                kwargs={
                    "module_name": "GameEngine.dll"
                }
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_026",
                    "updates": {
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_026",
                    "child_id": "crash_002",
                    "link_type": "duplicate"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_026"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#bug-triage",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_099",
        instruction=(
            "As a localization manager, manage the integration of a newly recorded set of voice-over lines into the 'Epic Adventure Game' project (proj_421) using the localization string 'vo.hero.intro_01'. Coordinate a new TMS job for these lines titled 'Integrate New VO Lines: hero_quest_01', making sure to target French and German. Proceed to generate a high-priority tracking ticket for the Game Engine Platform Team lead, with the title 'Track TMS Job for New Strings' and the description 'Tracking TMS job for new string translation.'. Ensure the ticket links to the new TMS job and complies with the notification policy."
        ),
        actions=[
            Action(
                name="CreateTmsJob",
                kwargs={
                    "project_id": "proj_421",
                    "job_name": "Integrate New VO Lines: hero_quest_01",
                    "source_locale": "en",
                    "target_locales": ["fr", "de"],
                    "string_keys": ["vo.hero.intro_01"]
                }
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                }
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_421",
                    "item_type": "task",
                    "title": "Track TMS Job for New Strings",
                    "description": "Tracking TMS job for new string translation."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "assignee_id": "user_001",
                        "priority": "high"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "tms_job_006",
                    "link_type": "related"
                }
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_100",
        instruction=(
            "Function as a localization specialist to address the German translation failure for the string key 'ui.main_menu.start_game' that didn't pass validation due to text overflow. Oversee the instigation of the standard remediation process for this failure. Confirm the validation status is 'failed', or otherwise amend the status. If it's found that the German translation's actual width surpasses the maximum defined width for the string key, ensure a high-priority bug ticket is raised in the 'Localization' project (proj_043) with the title 'Fix German Translation for Start Game Button' and the description 'The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened.'. Assign the ticket to the lead of the Game Engine Platform Team, ensuring it's linked to the localization string and adheres to the notification policy."
        ),
        actions=[
            Action(
                name="FindTranslationByKeyAndLocale",
                kwargs={
                    "string_key": "ui.main_menu.start_game",
                    "locale": "de"
                },
            ),
            Action(
                name="FindTeamByName",
                kwargs={
                    "name": "Game Engine Platform Team"
                },
            ),
            Action(
                name="CreateWorkItem",
                kwargs={
                    "project_id": "proj_043",
                    "item_type": "bug",
                    "title": "Fix German Translation for Start Game Button",
                    "description": "The German translation 'Spiel starten' for key 'ui.main_menu.start_game' exceeds the UI width constraints and must be shortened."
                },
            ),
            Action(
                name="UpdateWorkItem",
                kwargs={
                    "work_item_id": "work_028",
                    "updates": {
                        "priority": "high",
                        "assignee_id": "user_001"
                    }
                },
            ),
            Action(
                name="LinkWorkItems",
                kwargs={
                    "parent_id": "work_028",
                    "child_id": "loc_string_001",
                    "link_type": "related"
                },
            ),
            Action(
                name="CreateNotificationRecord",
                kwargs={
                    "message": "work_028"
                }
            ),
            Action(
                name="PostSlackMessage",
                kwargs={
                    "channel": "#localization-issues",
                    "message": "notification_013"
                }
            ),
        ],
        outputs=[]
    ),
]
